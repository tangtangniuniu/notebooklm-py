## Why

`SourceType.IMAGE` sources currently produce a `<title>.todo` placeholder when the batch downloader hits them — the image binary is never actually saved. That's a documentation hole left behind by the convert-sources-to-markdown change, which only specified the `WEB_PAGE` / `PDF` / `DOCX` / `PPTX` / `CSV` / `MARKDOWN` / `PASTED_TEXT` paths. Users who add image sources to a notebook (screenshots, diagrams, charts) lose them on every batch download. Markdown conversion makes no sense for an image — it should be saved as-is, the same way `CSV` already is.

## What Changes

- Add `SourceType.IMAGE` to the orchestrator's direct-download path in `src/notebooklm/web/jobs.py` and the equivalent branch in `notebook_batch.py:cmd_source_download`. Output filename is `<title>.<ext>`.
- Pick the file extension by: (1) sniffing the response `Content-Type` header (`image/jpeg` → `.jpg`, `image/png` → `.png`, `image/gif` → `.gif`, `image/webp` → `.webp`, `image/svg+xml` → `.svg`); (2) falling back to the URL path's extension if the header is missing or generic; (3) defaulting to `.png` if neither yields one.
- Touch the existing `_make_url_downloader` helper in `web/jobs.py` so it can return the chosen extension to the JobItem builder (or build the path inline using a small `_pick_image_extension(url, response)` helper).
- Update progress messages: a successful image download logs as `[image]` (not `[download]`, which is generic) so users can tell at a glance.
- No CLI / web UI flag changes — image sources just start working in the existing batch flow.
- Out of scope (deferred): downloading images embedded inside note Markdown (`![alt](url)` references). That's a different concern (markdown asset rewriting), tracked separately.

## Capabilities

### New Capabilities
<!-- none -->

### Modified Capabilities
- `batch-download-orchestrator`: The `Sources category download strategies` scenario in `Categories supported` adds a clause for `IMAGE` sources (download as-is with the sniffed/inferred extension). One new scenario covers the extension-fallback policy. No other requirements change.

## Impact

- **Affected code**:
  - `src/notebooklm/web/jobs.py` — extend `_DIRECT_DOWNLOAD_KINDS` to include `SourceType.IMAGE`, add `_pick_image_extension(url, response)` (or similar), and adjust `_build_source_items` so the image branch derives the target path after a HEAD/GET probe (or simply uses URL path + a sniff at runtime, with a renamed temp-file move on completion).
  - `src/notebooklm/web/jobs.py` — small adjustment to `_make_url_downloader` (or a new `_make_image_downloader`) so it can both stream the bytes AND surface the chosen extension as a strategy message (`"image"`) for the SSE event.
  - `notebook_batch.py` — mirror the change inside `cmd_source_download`: the new branch picks the extension before saving and uses an `[image]` log prefix.
- **No new dependencies**: uses the existing `httpx` (already core) for the download. No `markitdown` / no `markdownify`.
- **Tests**:
  - Unit tests for the extension-picker (`Content-Type` map, URL-path fallback, default).
  - Integration test exercising an `IMAGE` source through `build_items` → `run_job` and confirming the resulting file is bytes-identical to the mocked response and has the right extension.
- **User-visible behavior**: image sources, which previously produced a `.todo` placeholder, now download as `<title>.png` (or `.jpg` / `.gif` / `.webp` / `.svg` etc.) alongside the other source files. No regression for any other source type.
