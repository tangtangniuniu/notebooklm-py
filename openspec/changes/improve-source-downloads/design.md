## Context

`web/jobs.py` runs a `BatchJob` that fans out per-item downloads. Today:

- Concurrency is hard-coded to 3 via `BatchJob.concurrency: int = 3` and the API route accepts any int from the JSON payload (no validation).
- Every source-fetching call site issues a single HTTP request and surfaces a non-2xx status as a terminal item failure. A common cause of `404`/`403` in practice is a *normalization mismatch* on the host: the URL was indexed with a trailing `/` and the host serves a redirect-less 404, or vice-versa. Users see this most often with notebooks built from blog/Wiki sources.

Both behaviors live in five separate fetch sites (image streamer, CSV `urlretrieve`, file→markitdown stream, markdown.new GET, local fallback GET) plus mirrors in `notebook_batch.py`. Adding the same recovery branch to all five would pull the codebase further apart; a single helper used uniformly is preferable.

## Goals / Non-Goals

**Goals:**
- One reusable helper that adds slash-toggle retry on `404`/`403` to every source-fetching path. Pure function over an existing `httpx.AsyncClient`/`httpx.Client`; no new dependency, no coupling to the orchestrator.
- Default concurrency raised to 5 with a hard-clamped `1..10` range at the API boundary so no caller can flood the host.
- Surface the slash-retry recovery to the user (SSE / CLI prefix) so it's visible — silent retries are a debugging hazard.

**Non-Goals:**
- General-purpose retry-with-backoff for 5xx / 429 / network errors. That needs jitter, retry budgets, and per-host classification — out of scope here.
- Concurrency above 10. Hosts and our own bandwidth start hurting; raising the cap should require a separate proposal with measurements.
- Per-host concurrency overrides. Single global value per job is enough for now.
- Probing the host with HEAD requests before each download. We retry only after the GET fails.

## Decisions

### D1. One async + one sync helper, both 30 lines

Add `notebooklm/conversion/_url_retry.py` exposing two functions:

```python
async def afetch_with_slash_retry(
    client: httpx.AsyncClient,
    url: str,
    *,
    method: str = "GET",
    stream: bool = False,
    **kwargs: Any,
) -> httpx.Response | AsyncContextManager[httpx.Response]:
    ...

def fetch_with_slash_retry(
    client: httpx.Client,
    url: str,
    **kwargs: Any,
) -> httpx.Response:
    ...
```

Behavior — identical for both:

1. Issue the request with `url`.
2. If the response status is `404` or `403`, build the **alternate URL** by toggling the trailing slash on the *path* component only (using `urllib.parse.urlsplit` so query strings and fragments are preserved), and reissue once.
3. Return whichever response wins (or, if both fail with the same status, the second one).
4. Network errors bubble up unchanged on the first attempt — we do not slash-retry transport errors.

The async helper has two flavors because callers split between `client.get(...)` (the markdown.new path) and `client.stream("GET", ...)` (file/image streaming). For the streaming flavor we wrap in an `@asynccontextmanager` so callers can `async with` it the same way they already do.

**Alternatives considered:**
- Bake the retry into `httpx.AsyncClient` via an event hook. **Rejected** — would silently affect every internal HTTP call (auth refresh, RPC calls). We want it scoped to source fetching.
- Add an `tenacity`-style retry decorator. **Rejected** — overkill for one-shot conditional retry; pulls a dependency for ~10 lines of logic.

### D2. Slash toggle is path-only

```python
def _toggle_trailing_slash(url: str) -> str:
    parts = urlsplit(url)
    path = parts.path
    new_path = path[:-1] if path.endswith("/") and len(path) > 1 else path + "/"
    return urlunsplit(parts._replace(path=new_path))
```

Edge cases:
- Root URL `https://x.example/` → no toggle (we don't drop the only `/`); the helper treats this as "no alternate" and returns the original 404/403 response.
- URL with query `https://x.example/foo?q=1` → toggles to `https://x.example/foo/?q=1`. Query and fragment survive.
- URL with `;params` (rare) → preserved by `urlsplit`.

### D3. Concurrency: default 5, clamp 1..10 at API boundary

- `BatchJob.concurrency: int = 5` (was 3).
- `web/routes/jobs.py::create_job`: validate `1 <= concurrency <= 10`; HTTP 400 with `{error: "concurrency must be 1..10"}` otherwise.
- `notebook_batch.py source-download` and `download-all`: new `--concurrency N` arg, validated by argparse's `type=int` plus a manual range check.
- Web UI batch dialog: `<input type="range" min="1" max="10" value="5">` with the live value shown next to it.

We picked **5** as the new default because:
- 3 → 5 is a 1.7× speedup on bandwidth-bound jobs; under that, queueing wait dominates.
- Above 5 hits more host-side throttling on common CDNs.
- 10 is the documented ceiling — anyone needing more should split the job.

**Alternatives considered:**
- Adaptive concurrency (start at 5, ramp to 10 if no errors). **Rejected** — observable but state-heavy; one global per job stays simpler.
- Different default per category (e.g. lower for artifact downloads). **Rejected** — artifact downloads are already serialized inside `ArtifactsAPI`; one knob is fine.

### D4. Visible recovery in progress messages

When the slash-retry succeeds (the second attempt returns 2xx), the helper records the fact on the response (we attach `response.extensions["slash_retried"] = True`). Each call site that surfaces a strategy message appends ` (slash-retry)` when that flag is set. Examples:

- Image: `image:cover.png` → `image:cover.png (slash-retry)`
- markdown.new: `markdown.new` → `markdown.new (slash-retry)`
- CSV (notebook_batch.py): `[download] foo.csv` → `[download] foo.csv (slash-retry)`

The flag is invisible when the first attempt won — no message change for the happy path.

### D5. notebook_batch.py CSV branch switches to httpx

Currently uses `urllib.request.urlretrieve`, which doesn't expose response headers/status to the caller (it raises `HTTPError` on non-2xx). Switch to `httpx.Client.stream("GET", ...)` so the slash-retry helper can sniff the status and so the eventual progress message can include the slash-retry suffix. The image branch already uses httpx; this aligns the two.

## Risks / Trade-offs

- **Slash-retry hides genuine 404s with one extra request.** → Mitigation: only retry once, only on 404/403. We do not retry on 410 (Gone), which is the host's "this used to exist, don't try again" signal. Documented in the spec.
- **Some hosts return 403 for rate-limited requests, not just normalization mismatches.** Retrying with a slash-toggled URL adds load. → Mitigation: 1 retry, total cap is 2× requests in the worst case. Anyone running into rate limits has a different problem (covered by the deferred 429-with-backoff feature).
- **Doubling the default concurrency may surface latent races in the orchestrator.** Items share `target_dir`, but each has a unique target path, so we don't expect conflicts — but unit tests should cover N=10 to be sure. → Mitigation: integration test runs a 10-item job at concurrency=10 and confirms all items terminate with exactly one of `done|skipped|error`.
- **CSV branch switch in notebook_batch.py changes error messages.** Users grepping log output for the old `urllib.error.URLError` text will see different strings. → Mitigation: not a public API; release-notes mention. The new error messages are strictly more informative (HTTP status included).

## Migration Plan

1. Add `notebooklm/conversion/_url_retry.py` (no callers yet).
2. Wire helper into the five fetch sites + the two notebook_batch.py branches.
3. Bump `BatchJob.concurrency` default to 5; add 1..10 validation in `web/routes/jobs.py`.
4. Add `--concurrency` flag to `notebook_batch.py`.
5. Update web UI dialog to a slider (1..10, default 5).
6. Update tests + CHANGELOG.
7. Release.

**Rollback**: revert step 3 alone to restore the old default. Reverting step 2 alone disables the slash-retry without touching concurrency. The two changes are independent.

## Open Questions

- Should the slash-retry also kick in on 301/302 + a 404 at the redirect target? Probably overkill; the host already had a chance to send the right URL. Sticking with direct 404/403.
- Should the web UI remember the last-used concurrency value across sessions (localStorage)? Nice-to-have; deferring to a UX polish change.
- Do we want a per-job override on the slash-retry behavior (e.g. `--no-slash-retry` for users who deliberately want the original failure)? No real-world ask yet; not adding the flag until someone needs it.
