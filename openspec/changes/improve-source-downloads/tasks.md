## 1. Slash-retry helper

- [x] 1.1 Create `src/notebooklm/conversion/_url_retry.py` with `_toggle_trailing_slash(url) -> str | None` (returns `None` for path `/` so callers can short-circuit), preserving query string and fragment via `urlsplit`/`urlunsplit`
- [x] 1.2 Implement `async def afetch_with_slash_retry(client, url, *, method="GET", **kwargs) -> httpx.Response` for non-streaming calls (used by markdown.new, fallback)
- [x] 1.3 Implement `@asynccontextmanager async def astream_with_slash_retry(client, method, url, **kwargs)` that yields the response and toggles the slash on a 404/403 first attempt (used by image and file streaming)
- [x] 1.4 Implement `def fetch_with_slash_retry(client, url, **kwargs) -> httpx.Response` (sync flavor, used by `notebook_batch.py`)
- [x] 1.5 In all three flavors, set `response.extensions["slash_retried"] = True` only when the *second* attempt is the one returned (false when the first attempt succeeded)
- [x] 1.6 Do NOT slash-retry: status codes other than 404/403, transport errors (`httpx.HTTPError`), or paths equal to `/`
- [x] 1.7 Add unit tests `tests/unit/conversion/test_url_retry.py` covering: 200 first try (no retry, flag false), 404 → 200 with stripped slash (flag true), 403 → 200 with appended slash (flag true), 404 + 404 (flag true on second response, original status returned), 500 first try (no retry), transport error first try (no retry, exception raised), root path `/` skip-retry, query/fragment preservation

## 2. Wire helper into web/jobs.py

- [x] 2.1 Update `_make_image_downloader` to use `astream_with_slash_retry`; if `response.extensions.get("slash_retried")` is true, append ` (slash-retry)` to the returned strategy message (`f"{IMAGE_STRATEGY}:{final.name} (slash-retry)"`)
- [x] 2.2 Update `_download_url_sync` (CSV path): replace `urllib.request.urlretrieve` with an `httpx.Client.stream(...)` call wrapped via `fetch_with_slash_retry`; preserve the existing temp-file rename pattern; surface slash-retry by setting a new return value (e.g. switch `_make_url_downloader` to return `"download (slash-retry)"` when applicable)
- [x] 2.3 Bump `BatchJob.concurrency: int = 5` (was 3)
- [x] 2.4 Add an integration test in `tests/integration/test_jobs_images.py` covering the slash-retry path end-to-end: server returns 404 for `/cover/`, 200 for `/cover` → item completes with message ending in ` (slash-retry)`
- [x] 2.5 Add an integration test for the upper bound: 12-item job at `concurrency=10`, all items terminate cleanly (no leaks, sem release count matches)

## 3. Wire helper into conversion module

- [x] 3.1 Update `conversion/_files.py::_download_to_path` to use `astream_with_slash_retry`; carry the slash-retry flag onto the eventual `ConversionResult` (extend `ConversionResult` with an optional `slash_retried: bool = False` field, default false)
- [x] 3.2 Update `conversion/_remote.py::fetch_remote_markdown` to use `afetch_with_slash_retry` against the *original* source URL embedded in the markdown.new path — i.e. retry by toggling the slash on the original URL, not on the markdown.new base. Set the flag on the response/result.
- [x] 3.3 Update `conversion/_fallback.py` HTML-fetch path similarly via `afetch_with_slash_retry`
- [x] 3.4 Update `conversion/_dispatch.py` (or the relevant dispatcher) so the strategy message rendered by `_format_strategy_message` in `web/jobs.py` includes ` (slash-retry)` when `result.slash_retried` is true
- [x] 3.5 Add unit tests under `tests/unit/conversion/` for each call site: file download slash-retry, remote slash-retry against the original URL (with mock for the markdown.new endpoint), fallback HTML slash-retry

## 4. Wire helper into notebook_batch.py

- [x] 4.1 Switch the CSV branch from `urllib.request.urlretrieve` to `httpx.Client.stream(...)` wrapped via `fetch_with_slash_retry`; print `[download (slash-retry)] {filename}` when the helper recorded a retry
- [x] 4.2 Update `_download_image_source` to use `fetch_with_slash_retry` and append ` (slash-retry)` to the printed `[image]` line on retry success
- [x] 4.3 Add a `--concurrency N` argparse flag (`type=int`, default 5) to the `source-download` and `download-all` subparsers; reject values outside `1..10` with a helpful error
- [x] 4.4 The `--concurrency` flag is read but not actually used by `notebook_batch.py` (which is sequential today). Document this as informational for now and emit a warning when N > 1 (the script doesn't parallelize). If a future change parallelizes this script, the flag will be honored.
- [x] 4.5 Add smoke tests in `tests/unit/test_notebook_batch_flags.py`: `--concurrency 5` accepted, `--concurrency 0` rejected with non-zero exit, `--concurrency 11` rejected, slash-retry on the image branch surfaces in printed output

## 5. Concurrency validation at API boundary

- [x] 5.1 In `src/notebooklm/web/routes/jobs.py::create_job`, validate `1 <= concurrency <= 10` after parsing the payload; raise `HTTPException(400, "concurrency must be between 1 and 10")` on violation
- [x] 5.2 Default the concurrency in `create_job` to 5 (matching `BatchJob` default)
- [x] 5.3 Add a unit test in `tests/integration/test_web_routes.py` (or a new `test_jobs_routes.py`) covering: missing `concurrency` defaults to 5, `concurrency=10` accepted, `concurrency=0` returns 400, `concurrency=11` returns 400, `concurrency="bad"` returns 400 (existing int parsing)

## 6. Web UI control

- [x] 6.1 Replace the hard-coded `concurrency: 3` in the batch dialog form with an `<input type="range" min="1" max="10" value="5">` plus a numeric readout next to it
- [x] 6.2 Persist the selected value in the form's POST body so the API receives it
- [ ] 6.3 Manual UI smoke test: open the batch dialog, slide concurrency to 7, submit, confirm the network request body contains `"concurrency": 7`

## 7. Documentation

- [x] 7.1 Update `docs/web-ui.md` batch-dialog description: concurrency is now a slider 1..10 with default 5, and slash-retry is mentioned in the strategy/progress section
- [x] 7.2 Update `docs/cli-reference.md` "Source → Markdown Conversion (batch)" prefix table: add a note that any prefix may be suffixed with ` (slash-retry)` when the URL recovered via slash toggle; document the new `--concurrency` flag with its accepted range
- [x] 7.3 Update `docs/configuration.md` if needed to mention the concurrency knob (it's runtime-only; mention it briefly under web-UI / CLI sections)
- [x] 7.4 Add a `CHANGELOG.md` entry under `[Unreleased]` ### Changed: "Default batch concurrency raised from 3 to 5; accepted range is now 1..10 (rejected with HTTP 400 / argparse error if outside)" and ### Added: "Source-fetch URLs that return 404/403 now slash-retry once; recoveries are surfaced as `(slash-retry)` in progress messages"

## 8. Verification

- [x] 8.1 Run `ruff format src/ tests/ && ruff check src/ tests/`
- [x] 8.2 Run `mypy src/notebooklm --ignore-missing-imports`
- [x] 8.3 Run `pytest` (no regressions); confirm the new unit and integration tests pass
- [x] 8.4 Run `openspec validate improve-source-downloads` and `openspec validate --specs`
- [ ] 8.5 Manual smoke test: create a notebook with one source URL whose canonical form differs from the indexed form by a trailing slash; run a batch download; confirm the item completes with ` (slash-retry)` suffix and the file lands in the target directory
- [ ] 8.6 Manual smoke test: run a batch with `concurrency=10` against a 15-item notebook; confirm at most 10 items are simultaneously `running` and the job terminates with no orphaned tasks
