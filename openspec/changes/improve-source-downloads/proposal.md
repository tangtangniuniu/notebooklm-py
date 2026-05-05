## Why

Two pain points in the batch source-download flow:

1. **Brittle URL handling**: a non-trivial slice of source URLs (notably user-pasted ones) carry a trailing slash that the origin host rejects with `404`/`403` — and just as often, an URL *without* a trailing slash that the host requires. Today the orchestrator treats either failure as terminal and aborts the item. A single cheap retry with the slash toggled would recover most of these.
2. **Conservative concurrency**: the orchestrator caps each job at `concurrency=3`. Notebooks with 30+ sources take long enough that users complain. Modern hosts and our own bandwidth tolerate 5–10 parallel transfers comfortably; the current default is leftover caution from when the orchestrator was new.

## What Changes

- Add a tiny URL-fetch helper `_fetch_with_slash_retry(client, url, **kwargs)` to `notebooklm.conversion` that issues the request, and on `404`/`403` retries exactly once with the trailing slash toggled (stripped if present, appended if absent). Other non-2xx statuses fail immediately as before. Helper is reused by every source-fetching call site.
- Wire the helper into:
  - `web/jobs.py::_make_image_downloader` (image source streaming)
  - `web/jobs.py::_download_url_sync` (CSV direct download)
  - `conversion/_files.py::_download_to_path` (PDF/DOCX/PPTX → markitdown input)
  - `conversion/_remote.py::fetch_remote_markdown` (markdown.new lookup)
  - `conversion/_fallback.py` (local httpx + markdownify fallback)
  - `notebook_batch.py::_download_image_source` (legacy CLI image branch)
  - `notebook_batch.py` CSV branch (`urllib.request.urlretrieve` → `httpx.get` with the helper, so headers can be inspected)
- Raise the orchestrator's default concurrency from 3 to 5 and clamp the accepted range to `1..10` at the API boundary in `web/routes/jobs.py`. Values outside that range are rejected with HTTP 400.
- Add a `--concurrency N` flag (1..10) to `notebook_batch.py source-download` and `download-all`. Default 5.
- Web UI batch dialog gains a concurrency slider (1..10, default 5) replacing the hard-coded 3.
- Progress message convention: when the slash-retry succeeds, append ` (slash-retry)` to the item's strategy message so the SSE consumer can surface that the recovery kicked in (e.g. `image:cover.png (slash-retry)`).
- Out of scope (deferred): retries on 5xx / 429 / network errors. Those need backoff + jitter and a different design; this proposal is strictly about the cheap deterministic case.

## Capabilities

### New Capabilities
<!-- none -->

### Modified Capabilities
- `batch-download-orchestrator`: concurrency requirement moves from a flat default of 3 to default 5 with a documented `1..10` range and 400-on-out-of-range; new requirement covers slash-retry on 404/403 across every source-fetching strategy.
- `source-markdown-conversion`: file-to-markdown and remote/fallback URL fetches gain the same slash-retry behavior on 404/403 (one retry, then the existing failure path).

## Impact

- **Affected code**:
  - `src/notebooklm/conversion/` — new helper module (e.g. `_url_retry.py`) plus call-site updates in `_files.py`, `_remote.py`, `_fallback.py`.
  - `src/notebooklm/web/jobs.py` — call-site updates in image/CSV downloaders; default `concurrency=3` → `5`.
  - `src/notebooklm/web/routes/jobs.py` — concurrency validation (1..10, HTTP 400 on violation).
  - `src/notebooklm/web/static/` + templates — concurrency slider in the batch dialog (default 5).
  - `notebook_batch.py` — `--concurrency` flag, slash-retry helper application, switch CSV branch from `urllib.request` to `httpx`.
- **No new dependencies**: reuses existing `httpx`. The helper is ~30 lines.
- **Tests**:
  - Unit tests for the slash-retry helper covering: 200 first try (no retry), 404→200 with stripped slash, 403→200 with appended slash, 404 on both attempts, 500 first try (no retry), network error first try (no retry).
  - Integration test in `tests/integration/test_jobs_images.py` exercising the slash-retry path through the image downloader.
  - Validation test for the concurrency range at `web/routes/jobs.py`.
- **User-visible behavior**:
  - Batch jobs with picky-host URLs no longer error-out on the first `404`/`403`; the second attempt usually wins.
  - Default jobs run ~1.7× faster (5 concurrent vs. 3); users can dial up to 10 if their network and the host tolerate it.
  - One new visible suffix in SSE progress messages: `(slash-retry)`.
- **Migration**: none — both behaviors are strict supersets of today's. No breaking changes.
