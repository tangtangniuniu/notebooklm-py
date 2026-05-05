## Why

Today the batch downloader converts web pages to PDF via the external `wkhtmltopdf` binary and leaves PDF/DOCX/PPTX sources as their original binary blobs. That produces files that are awkward to read, hard to diff, expensive to feed to LLMs, and unavailable at all when `wkhtmltopdf` is not installed (the runner emits a `.todo` placeholder and fails). Markdown is token-efficient, diffable, and matches the existing `MARKDOWN`/`PASTED_TEXT`/`notes` outputs, so converting *every* readable source to Markdown gives users one consistent, LLM-friendly artifact and removes the hard dependency on a system PDF tool.

## What Changes

- **BREAKING**: `WEB_PAGE` sources downloaded by the batch orchestrator (`src/notebooklm/web/jobs.py`) and the standalone `notebook_batch.py` produce `<title>.md` instead of `<title>.pdf`.
- HTML → Markdown conversion uses `https://markdown.new/<original-url>` as the primary path (per the `markdown-url` skill), then falls back to a local converter (`httpx.get` + a lightweight HTML→Markdown step) when `markdown.new` is unreachable, returns 4xx/5xx, is rate-limited, or returns content that fails a sanity check.
- PDF / DOCX / PPTX sources downloaded by the batch orchestrator are converted to `<title>.md` using the `markitdown` library (per the `markitdown` skill), with the original binary kept as a sibling file (`<title>.pdf`/`.docx`/`.pptx`) only when the user opts in via a flag; default behavior is Markdown-only.
- A new `notebooklm.conversion` module owns the conversion strategies (URL→MD remote, URL→MD local fallback, file→MD via markitdown) so both the web batch runner and the legacy `notebook_batch.py` script share one implementation.
- `wkhtmltopdf` is no longer required. If the user explicitly requests PDF output for a web page (new opt-in flag, e.g. `--keep-pdf`), the existing `wkhtmltopdf` path is preserved as a secondary mode; otherwise it is removed from the default runner.
- Dependency additions: `markitdown[all]` for office/PDF conversion; `httpx` (already a transitive dep — confirm during design); a small HTML→Markdown library (e.g. `markdownify`) for the fallback path.
- CLI / web UI surfaces the new behavior in messages (e.g. `[markdown.new]`, `[fallback]`, `[markitdown]` log prefixes replace the old `[wkhtmltopdf]` prefix) and the README/docs are updated.

## Capabilities

### New Capabilities
- `source-markdown-conversion`: Strategies and policies for turning a NotebookLM source (web URL, PDF, DOCX, PPTX, etc.) into a Markdown file, including remote (`markdown.new`) and local fallback paths, file-format dispatch, error handling, and filename rules.

### Modified Capabilities
- `batch-download-orchestrator`: The `sources` category SHALL produce Markdown for `WEB_PAGE`, `PDF`, `DOCX`, and `PPTX` source types (replacing the current PDF/binary outputs), and SHALL no longer treat missing `wkhtmltopdf` as a hard failure for the default flow.

## Impact

- **Affected code**:
  - `src/notebooklm/web/jobs.py` — replace `_make_webpage_pdf` and the PDF/DOCX/PPTX branch in `_build_source_items`; introduce calls into the new conversion module.
  - `notebook_batch.py` — same conversion strategy swap inside `cmd_source_download`.
  - New `src/notebooklm/conversion/` package: `url_to_markdown.py`, `file_to_markdown.py`, plus shared types/errors.
  - `pyproject.toml` — add `markitdown[all]` and any HTML→Markdown lib to the appropriate extras (likely `[all]` and a new `[markdown]` extra).
  - CLI/web messages and docs (`docs/cli-reference.md`, `docs/configuration.md`, `README.md`, `docs/web-ui.md`).
- **External dependencies**: `markdown.new` (network-reachable), `markitdown` Python package (and its optional system deps for PDF/Office). `wkhtmltopdf` becomes optional.
- **Tests**: New unit tests for the conversion module (mocked `markdown.new`, mocked `httpx`, fixture `.pdf`/`.docx`/`.pptx` files); update existing job/integration tests that assume `.pdf` outputs for web pages.
- **User-visible behavior**: File extensions for web/PDF/DOCX/PPTX sources change from binary to `.md`. Users with scripts grepping `.pdf` outputs will need to adjust. Document this clearly in the changelog and migration notes.
