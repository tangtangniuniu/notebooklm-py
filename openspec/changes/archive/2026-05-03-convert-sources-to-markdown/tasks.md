## 1. Dependencies and module scaffold

- [x] 1.1 Add a `markdown` optional extra to `pyproject.toml` containing `markitdown[all]` and `markdownify`, and include it in the existing `all` extra
- [x] 1.2 Run `uv lock` (or equivalent) to refresh `uv.lock` for the new extra and confirm the base install is unchanged
- [x] 1.3 Create the package directory `src/notebooklm/conversion/` with an empty `__init__.py`
- [x] 1.4 Create `src/notebooklm/conversion/_types.py` defining `ConversionOptions` (frozen dataclass with `timeout`, `use_remote`, `keep_original`, `user_agent`, `markdown_new_base`), `ConversionResult` (frozen dataclass with `target`, `strategy`, `bytes_written`, `duration_ms`), and the strategy `Literal`
- [x] 1.5 Add `ConversionOptions.from_env()` classmethod that reads `NOTEBOOKLM_MARKDOWN_NEW_BASE`, `NOTEBOOKLM_DISABLE_MARKDOWN_NEW`, `NOTEBOOKLM_CONVERSION_TIMEOUT`, `NOTEBOOKLM_CONVERSION_UA` and merges them with explicit overrides
- [x] 1.6 Create `src/notebooklm/conversion/_errors.py` defining `ConversionError`, `RemoteConversionError`, `LocalConversionError`, `ConversionDependencyError`
- [x] 1.7 Re-export the public API (`url_to_markdown`, `file_to_markdown`, `source_to_markdown`, `ConversionOptions`, `ConversionResult`, exception classes) from `src/notebooklm/conversion/__init__.py`

## 2. Remote URL-to-Markdown via markdown.new

- [x] 2.1 Create `src/notebooklm/conversion/_remote.py` with an async `fetch_remote_markdown(url, options)` that issues `GET {options.markdown_new_base}{url}` via `httpx.AsyncClient`, follows redirects, applies `options.timeout`
- [x] 2.2 Implement the sanity-check helper that flags non-2xx, empty bodies (<32 bytes), and HTML-error-page responses (HTML start tag with no Markdown markers in the first 4 KB)
- [x] 2.3 On any sanity-check failure or network error, raise `RemoteConversionError` carrying the cause; on success return the response body as `str`
- [x] 2.4 Add unit tests under `tests/unit/conversion/test_remote.py` using `pytest-httpx` to cover: 200 with markdown body, 200 with HTML error page, 401/403/429, 5xx, empty body, network timeout, custom base override
- [x] 2.5 Verify a Markdown sanity-check positive on a fixture that contains only `> ` (blockquote) and only fenced code, ensuring all listed markers are accepted

## 3. Local URL-to-Markdown fallback

- [x] 3.1 Create `src/notebooklm/conversion/_fallback.py` with an async `fetch_local_markdown(url, options)` that issues an `httpx.AsyncClient.get` against the original URL with the configured User-Agent, follows redirects, applies `options.timeout`
- [x] 3.2 Detect HTML responses by `Content-Type` (prefix `text/html`) and convert via `markdownify.markdownify(html, heading_style="ATX", strip=["script", "style"])`; lazy-import `markdownify` inside the function
- [x] 3.3 For non-HTML responses, treat the body as already-Markdown / plain text and pass it through unchanged
- [x] 3.4 Always prepend `> Source: <original_url>\n\n` to the produced Markdown before returning it
- [x] 3.5 Raise `ConversionDependencyError` with an actionable install hint when `markdownify` is missing AND the response is HTML
- [x] 3.6 Raise `LocalConversionError` for non-2xx, empty body, and network errors
- [x] 3.7 Add unit tests under `tests/unit/conversion/test_fallback.py` using `pytest-httpx` covering: HTML→MD success, plain-text passthrough, missing-dep error path (monkeypatch import), network failure, custom UA via options and via env var

## 4. URL-to-Markdown dispatcher (`url_to_markdown`)

- [x] 4.1 Implement `url_to_markdown(url, target, *, options)` in `src/notebooklm/conversion/__init__.py` (or a `_url.py` module) that orchestrates remote → fallback flow
- [x] 4.2 When `options.use_remote` is True (and env override allows), attempt `fetch_remote_markdown`; on `RemoteConversionError` log at debug level and fall through
- [x] 4.3 Always try `fetch_local_markdown` if remote did not return content; on `LocalConversionError` re-raise with both remote and local cause messages
- [x] 4.4 On success, write the markdown to `target` via a temp-file rename for atomicity, ensure parent dirs exist, and return a `ConversionResult` with `strategy="remote"` or `strategy="fallback"`, `bytes_written`, and `duration_ms`
- [x] 4.5 Add unit tests for `url_to_markdown` covering: remote success path, remote-fail-then-fallback-success path, both-fail path, `use_remote=False` skipping remote, `NOTEBOOKLM_DISABLE_MARKDOWN_NEW=1` skipping remote

## 5. File-to-Markdown via markitdown

- [x] 5.1 Create `src/notebooklm/conversion/_files.py` with an async `file_to_markdown(file_url, target, *, options, source_extension)` that downloads the source URL to a `tempfile.NamedTemporaryFile`
- [x] 5.2 Lazy-import `markitdown.MarkItDown` inside the function; raise `ConversionDependencyError("install notebooklm[markdown] to enable file-to-markdown conversion")` if missing
- [x] 5.3 Run `MarkItDown().convert(tmp_path)` via `asyncio.to_thread`
- [x] 5.4 Write `result.text_content` to `target` (atomic rename, parent dirs created); when `options.keep_original` is True, copy the temp file to `target.with_suffix(source_extension)` before deleting the temp file
- [x] 5.5 Always remove the temp file in a `finally` block; on `markitdown` exception, re-raise as `LocalConversionError` and ensure no `.md` is left behind
- [x] 5.6 Add unit tests under `tests/unit/conversion/test_files.py` using small fixture files (`tests/fixtures/conversion/sample.pdf`, `sample.docx`, `sample.pptx`) covering: success path, `keep_original=True` produces both files, missing-dep error, markitdown raising, parent-directory creation, off-thread execution (assert event loop is not blocked via a sentinel coroutine)

## 6. High-level `source_to_markdown` dispatcher

- [x] 6.1 Implement `source_to_markdown(source_url, source_kind, target, *, options)` that maps `SourceType.WEB_PAGE` → `url_to_markdown`, `SourceType.PDF` → `file_to_markdown(..., source_extension=".pdf")`, `SourceType.DOCX` → `.docx`, `SourceType.PPTX` → `.pptx`
- [x] 6.2 For unsupported source types, raise a typed `ConversionError` with a clear message ("source type X not supported by source-markdown-conversion")
- [x] 6.3 Add unit tests `tests/unit/conversion/test_dispatch.py` covering each supported `SourceType` and the unsupported-type error path

## 7. Wire batch orchestrator (`web/jobs.py`)

- [x] 7.1 Replace `_make_webpage_pdf` with `_make_webpage_markdown` that calls `source_to_markdown` for `WEB_PAGE`; remove the `wkhtmltopdf` lookup from the default flow
- [x] 7.2 Update `_build_source_items` so the `WEB_PAGE` branch produces `<title>.md` and the `PDF`/`DOCX`/`PPTX` branch routes through `source_to_markdown` (not `_download_url_sync`); CSV stays on the existing direct-download path
- [x] 7.3 Remove `SourceType.PDF` and `SourceType.DOCX` from `_SOURCE_EXT_MAP` (CSV stays); the new branch derives extensions from `source_to_markdown`
- [x] 7.4 Thread a new `keep_original: bool` field through `BatchJob` / job spec → `_build_source_items` → `ConversionOptions(keep_original=...)`
- [x] 7.5 Add an opt-in `legacy_pdf: bool` field to the job spec; when True, restore the previous `wkhtmltopdf` path for `WEB_PAGE` and label progress events with `strategy="legacy-pdf"`
- [x] 7.6 Surface `ConversionResult.strategy` in the `event: item` SSE payload (optional message field, e.g. `message="markdown.new"` / `message="fallback"` / `message="markitdown"`)
- [x] 7.7 Update existing `tests/integration/web/test_jobs.py` (and any unit tests) that assert `.pdf` outputs for `WEB_PAGE` sources or that mock `wkhtmltopdf`; replace with assertions against `.md` outputs and mocked `source_to_markdown`
- [x] 7.8 Add a new integration test that runs the orchestrator end-to-end with a mocked `markdown.new` (via `pytest-httpx`) and asserts the produced `.md` file matches expectations

## 8. Wire `notebook_batch.py` CLI

- [x] 8.1 Replace the `WEB_PAGE` branch in `cmd_source_download` to call `source_to_markdown` and write `<title>.md`
- [x] 8.2 Replace the `PDF`/`DOCX`/`PPTX` branch in `cmd_source_download` to call `source_to_markdown` (CSV branch unchanged)
- [x] 8.3 Add `--keep-original` flag (off by default) that toggles `ConversionOptions.keep_original`
- [x] 8.4 Add `--legacy-pdf` flag (off by default) that, when set, runs the previous `wkhtmltopdf`-based path for web pages
- [x] 8.5 Update progress prefixes: `[markdown.new]` / `[fallback]` / `[markitdown]` / `[legacy-pdf]` / `[fulltext]` / `[passthrough]`
- [x] 8.6 Update or add unit tests covering the CLI flag plumbing and ensuring the legacy path is only invoked under `--legacy-pdf`

## 9. Documentation and changelog

- [x] 9.1 Update `README.md` with the new default behavior (sources export as Markdown), install hint for `[markdown]` extra, and a note that `wkhtmltopdf` is no longer required
- [x] 9.2 Update `docs/cli-reference.md` with the new `--keep-original` and `--legacy-pdf` flags and the new log prefixes
- [x] 9.3 Update `docs/configuration.md` with the four new environment variables (`NOTEBOOKLM_MARKDOWN_NEW_BASE`, `NOTEBOOKLM_DISABLE_MARKDOWN_NEW`, `NOTEBOOKLM_CONVERSION_TIMEOUT`, `NOTEBOOKLM_CONVERSION_UA`) and the privacy note about routing URLs through `markdown.new`
- [x] 9.4 Update `docs/web-ui.md` with the new `keep_original` / `legacy_pdf` job-spec fields and any UI checkbox
- [x] 9.5 Add a `CHANGELOG.md` entry under the next release flagged as **BREAKING**: web-page sources now produce `.md`; PDF/DOCX/PPTX sources now produce `.md`; `--legacy-pdf` is the one-release escape hatch
- [x] 9.6 Add a migration note to `docs/troubleshooting.md` covering "my scripts grep for .pdf — how do I restore the old behavior?" pointing to `--legacy-pdf`

## 10. Verification

- [x] 10.1 Run `ruff format src/ tests/ && ruff check src/ tests/`
- [x] 10.2 Run `mypy src/notebooklm --ignore-missing-imports` (note: `markitdown` and `markdownify` may need stub ignores)
- [x] 10.3 Run `pytest` (all unit + integration tests pass; no regressions in unrelated tests)
- [ ] 10.4 Manual smoke test against a real notebook: download `sources` for one notebook with at least one `WEB_PAGE`, one `PDF`, and one `DOCX`; confirm three `.md` files are produced and `wkhtmltopdf` is not invoked
- [ ] 10.5 Manual smoke test of the `--legacy-pdf` flag against a `WEB_PAGE` source on a system that has `wkhtmltopdf` installed; confirm `.pdf` output and the `[legacy-pdf]` log prefix
- [ ] 10.6 Manual smoke test with `NOTEBOOKLM_DISABLE_MARKDOWN_NEW=1` set; confirm only the local fallback is invoked (verifiable via debug log)
- [x] 10.7 Run `openspec verify --change "convert-sources-to-markdown"` (if available) to confirm spec/implementation alignment
