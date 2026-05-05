## 1. Helper module

- [x] 1.1 Create `src/notebooklm/conversion/_images.py` with `_pick_image_extension(url: str, content_type: str | None) -> str`
- [x] 1.2 Pin the `Content-Type` → extension table for: `image/jpeg`, `image/jpg`, `image/png`, `image/gif`, `image/webp`, `image/svg+xml`, `image/bmp`, `image/tiff`, `image/x-icon`, `image/heic`, `image/avif`
- [x] 1.3 Implement the URL-path fallback: parse with `urllib.parse.urlparse`, check the path's extension against the *values* of the `Content-Type` table (so `.exe`, `.html` etc. cannot leak through); accept `.tiff` in addition to `.tif`, normalize to lowercase
- [x] 1.4 Default to `.png` when neither sniff matches; ignore `Content-Type` parameters (`; charset=...`) by splitting on `;` and trimming
- [x] 1.5 Add unit tests `tests/unit/conversion/test_images.py` covering: each MIME → ext mapping, case-insensitive Content-Type, parameters stripped, URL-path fallback hit, URL-path fallback rejected for non-image extensions, default fallback when both miss, malformed Content-Type doesn't crash

## 2. Wire batch orchestrator (`web/jobs.py`)

- [x] 2.1 Add `SourceType.IMAGE` to the existing `_DIRECT_DOWNLOAD_KINDS` tuple (the same list `CSV` already lives in)
- [x] 2.2 Add a new `_make_image_downloader(url, target)` runner that streams the response with `httpx.AsyncClient`, picks the extension from headers via `_pick_image_extension`, renames the placeholder target to `<target-stem>.<ext>` via temp-file rename, and returns the strategy message `f"image:{final.name}"`
- [x] 2.3 In `_build_source_items`, route `SourceType.IMAGE` to `_make_image_downloader` instead of `_make_url_downloader`; build the JobItem with placeholder `target_path = target_dir / f"{title}.img"`
- [x] 2.4 Add a pre-skip check: before appending the IMAGE JobItem, scan the target directory for any `<title>.<known-image-ext>` (using the values of the helper's MIME table); if one exists and `force` is false, mark the item `skipped` with message `file exists` upfront so it doesn't redownload
- [x] 2.5 Add unit / integration tests in `tests/integration/test_jobs_markdown.py` (or a new `test_jobs_images.py`) covering: image source produces the expected extension, the `image:<final-name>` strategy message, skip-if-exists behavior across extensions (e.g. existing `.jpg` skips a new `.png` candidate), default `.png` fallback, error path on HTTP 404

## 3. Wire `notebook_batch.py` CLI

- [x] 3.1 Add a new branch in `cmd_source_download` that handles `"SourceType.IMAGE"` (string match — the CLI prints enum reprs) before the existing direct-download CSV branch; pull the response with `httpx.get` so we can read headers, call `_pick_image_extension`, write the bytes
- [x] 3.2 Use the `[image]` log prefix on success; honor the existing skip-if-exists pattern (scan for `<title>.<known-image-ext>` siblings in `base_dir`)
- [x] 3.3 Add a smoke test similar to `tests/unit/test_notebook_batch_flags.py` confirming the script handles an `IMAGE` source type without crashing and produces the right extension via mocked subprocess output

## 4. Documentation

- [x] 4.1 Update `docs/web-ui.md` source-strategy table: add `IMAGE` row ("downloaded as-is; extension picked from `Content-Type` then URL path then `.png`")
- [x] 4.2 Update `docs/cli-reference.md` "Source → Markdown Conversion (batch)" prefix table: add `[image]` row
- [x] 4.3 Add a `CHANGELOG.md` entry under `[Unreleased]` ### Added: "`SourceType.IMAGE` sources now download as-is via the batch flow (previously produced a `.todo` placeholder)"
- [x] 4.4 Note the SVG-with-script caveat in `docs/troubleshooting.md` ("we save SVGs verbatim; treat untrusted images like any untrusted file")

## 5. Verification

- [x] 5.1 Run `ruff format src/ tests/ && ruff check src/ tests/`
- [x] 5.2 Run `mypy src/notebooklm --ignore-missing-imports`
- [x] 5.3 Run `pytest` (no regressions)
- [x] 5.4 Run `openspec validate image-source-passthrough` and `openspec validate --specs`
- [ ] 5.5 Manual smoke test: add an image source (e.g. PNG screenshot URL) to a real notebook, run a batch download, confirm `<title>.png` lands in the target directory and re-running the batch reports it as `skipped`
