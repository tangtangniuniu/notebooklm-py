## Context

NotebookLM batch downloads currently materialize sources as binary blobs:

- `WEB_PAGE` → run `wkhtmltopdf` to render the URL into a PDF (`<title>.pdf`). If the binary is missing, the runner writes a `.todo` placeholder and raises an error.
- `PDF` / `DOCX` / `CSV` → fetch the source's `url` directly via `urllib.request.urlretrieve` and save with the original extension.
- `MARKDOWN` / `PASTED_TEXT` and untyped sources → call `client.sources.get_fulltext()` and write `<title>.md`.

The orchestrator (`src/notebooklm/web/jobs.py:_build_source_items`) and the standalone `notebook_batch.py` both implement this logic separately, with slight drift between them.

The proposal commits to: HTML → Markdown via `markdown.new` (with a local fallback), and PDF/DOCX/PPTX → Markdown via `markitdown`. This needs a single shared module so both call sites converge, plus a clear policy for fallback, error handling, opt-in retention of original binaries, and rate-limit / network-failure recovery.

`httpx>=0.27.0` is already a project dependency, so the local fallback can reuse it. `markitdown[all]` and a small HTML→Markdown library (`markdownify` is the leading candidate) are new additions.

## Goals / Non-Goals

**Goals:**
- One shared `notebooklm.conversion` package consumed by `web/jobs.py` and `notebook_batch.py`.
- Default behavior produces `.md` for `WEB_PAGE`, `PDF`, `DOCX`, `PPTX` sources.
- Primary HTML path uses `https://markdown.new/<original-url>`; on failure a local `httpx` + `markdownify` path produces equivalent Markdown.
- File path uses `markitdown` for PDF/DOCX/PPTX (and any other markitdown-supported types we already touch).
- `wkhtmltopdf` is no longer a hard dependency for the default flow; users who want PDF can opt in via a flag.
- Transparent failure handling: if both remote and fallback fail, the job item is marked `error` with a message that distinguishes the failure stage.
- Tests exercise the conversion module independently from the orchestrator, including mocked `markdown.new` rate-limit responses.

**Non-Goals:**
- Migrating already-downloaded files (no auto-conversion of legacy `.pdf` outputs).
- Rendering JS-heavy pages (out of scope: `markdown.new` and `httpx` are static fetches; users with JS-heavy targets should use the opt-in `--keep-pdf` path or a future headless-browser converter).
- Re-implementing markitdown's format support (we use it as a black box).
- Caching `markdown.new` responses across runs (the orchestrator's existing skip-if-exists semantics already cover repeat invocations).
- Changing how `MARKDOWN`, `PASTED_TEXT`, `YOUTUBE`, or any Google-Drive-backed source is handled — the new code only changes the `WEB_PAGE` and binary-office branches.

## Decisions

### D1. New top-level package `notebooklm.conversion`

Create `src/notebooklm/conversion/__init__.py` with public functions:

```python
async def url_to_markdown(url: str, target: Path, *, options: ConversionOptions | None = None) -> ConversionResult: ...
async def file_to_markdown(file_path: Path, target: Path, *, options: ConversionOptions | None = None) -> ConversionResult: ...
async def source_to_markdown(source_url: str, source_kind: SourceType, target: Path, *, options: ConversionOptions | None = None) -> ConversionResult: ...
```

Internals split into `_remote.py` (markdown.new), `_fallback.py` (httpx + markdownify), `_files.py` (markitdown wrapper), `_types.py` (`ConversionOptions`, `ConversionResult`, custom exceptions).

`source_to_markdown` is the high-level entry point that the batch orchestrator calls — it dispatches by `SourceType` so the callers don't need to know about `markdown.new` vs. `markitdown`.

**Alternatives considered:**
- Inline the logic into `_sources.py`. **Rejected** — bloats an already-busy domain module and forces tests through the full `NotebookLMClient`.
- Single flat module `conversion.py`. **Rejected** — three distinct strategies with different deps justify subfiles for clarity and to keep optional imports lazy.

### D2. `markdown.new` interaction

- URL pattern: `https://markdown.new/{original_url}` (per `markdown-url` skill, no extra encoding — markdown.new accepts the URL appended raw, including its scheme).
- HTTP method: `GET` with `httpx.AsyncClient`, `timeout=ConversionOptions.timeout` (default 30s), `follow_redirects=True`.
- Response handling: treat the response body as Markdown text. The skill notes that the page is a Markdown view; we write `response.text` directly to the target file after a sanity check.
- **Sanity check** (treat as failure → trigger fallback):
  - HTTP status not in `2xx`.
  - `Content-Length == 0` or body shorter than 32 chars.
  - Body looks like an HTML error page (starts with `<!DOCTYPE html>` / `<html` and contains no Markdown signal — i.e. no `#`, `*`, `- `, `> `, or fenced ` ``` ` within the first 4 KB).
  - Status is `401`, `403`, `429`, or `5xx` (per the skill's block/failure signals).
- **Retry policy**: a single attempt — don't sleep-and-retry on `429` because the orchestrator already runs concurrent items and the fallback path is fast. The fallback is the recovery, not a retry of `markdown.new`.

**Alternatives considered:**
- Render via headless Chrome / Playwright for JS-heavy pages. **Rejected** for the default — Playwright is heavyweight and already used only for auth; pulling it into batch downloads is too invasive. Tracked as a future opt-in.
- Use `markdown.new`'s API endpoint if one exists. **Rejected** — the skill is explicit that the URL prefix IS the integration; no separate API is documented.

### D3. Local fallback (`httpx` + `markdownify`)

When `markdown.new` fails the sanity check or raises, the fallback runs:

1. `httpx.AsyncClient.get(url, timeout=..., follow_redirects=True, headers={"User-Agent": DEFAULT_UA})` — `DEFAULT_UA` is a normal browser UA string to dodge naive bot blocks.
2. If the response is HTML (`Content-Type` starts with `text/html` or sniff fails), feed it through `markdownify.markdownify(html, heading_style="ATX", strip=["script", "style"])` — produces clean Markdown.
3. If the response is already plain text or markdown, write it through unchanged.
4. Prepend a one-line front-matter-style header `> Source: <url>\n\n` so the produced file always identifies its origin.

The fallback never re-uses the `markdown.new` URL — it always hits the original.

**Alternatives considered:**
- `html2text`. Considered. `markdownify` produces cleaner output for modern HTML (better handling of `<pre>`, `<code>`, `<table>`) and is more actively maintained. **Tentative**: confirm during implementation; the wrapper hides the choice.
- Custom regex-based stripper. **Rejected** — fragile, reinvents existing libraries.

### D4. File-format conversion via `markitdown`

For `PDF`, `DOCX`, `PPTX`, and any other format markitdown supports that we currently treat as binary:

1. Download the binary to a temp file via the existing `_download_url_sync` helper (renamed/moved into `conversion._files`).
2. Call `MarkItDown().convert(str(tmp_path))` (CPU-bound — wrap with `asyncio.to_thread`).
3. Write `result.text_content` to `<title>.md`.
4. **Original binary**: deleted by default. Kept iff `ConversionOptions.keep_original=True` (surfaced as `--keep-original` in `notebook_batch.py` and a checkbox in the web UI; piped through the batch job spec).
5. If markitdown raises, mark the item `error` — do NOT silently fall back to keeping the binary, since the user explicitly asked for Markdown.

Markitdown is imported lazily inside `_files.py` so the conversion module can still be imported when the optional extra is not installed; calling `file_to_markdown` without it raises a clear `ConversionDependencyError("install notebooklm[markdown] to enable file-to-markdown conversion")`.

**Alternatives considered:**
- Stream-based conversion (`md.convert_stream(fileobj, ...)`). Useful but markitdown's stream API behaves inconsistently for some PDF backends; safer to hit the disk for the temp file. The temp file is unlinked in a `finally` block.
- Use `pypdf` / `python-docx` / `python-pptx` directly. **Rejected** — re-implements what markitdown already does well, and we'd need separate code paths for each format.

### D5. `ConversionOptions` and `ConversionResult`

```python
@dataclass(frozen=True, slots=True)
class ConversionOptions:
    timeout: float = 30.0
    use_remote: bool = True            # disable to force local fallback
    keep_original: bool = False        # for file_to_markdown / source_to_markdown
    user_agent: str | None = None      # override default UA for fallback
    markdown_new_base: str = "https://markdown.new/"  # override for testing/proxy

@dataclass(frozen=True, slots=True)
class ConversionResult:
    target: Path
    strategy: Literal["remote", "fallback", "markitdown", "fulltext", "passthrough"]
    bytes_written: int
    duration_ms: int
```

The orchestrator surfaces `strategy` in its log messages (replacing the old `[wkhtmltopdf]` label). `ConversionResult` is yielded back so the SSE `event: item` payload can include it for the UI.

Three exception types under a common base:
- `ConversionError` (base)
- `RemoteConversionError` — raised internally when `markdown.new` fails the sanity check; caught by the dispatcher to trigger fallback. Not surfaced.
- `LocalConversionError` — raised when the fallback also fails. Surfaced to the orchestrator as the item's terminal error.
- `ConversionDependencyError` — raised when an optional dep (`markitdown`, `markdownify`) is missing.

### D6. Configuration via environment variables

For users running in restricted environments (no outbound `markdown.new`, custom proxies, internal mirrors):

| Env var | Effect | Default |
|---|---|---|
| `NOTEBOOKLM_MARKDOWN_NEW_BASE` | Override `markdown.new` URL | `https://markdown.new/` |
| `NOTEBOOKLM_DISABLE_MARKDOWN_NEW` | If set to `1`, skip remote and go straight to fallback | unset |
| `NOTEBOOKLM_CONVERSION_TIMEOUT` | Override timeout in seconds | `30` |
| `NOTEBOOKLM_CONVERSION_UA` | Override fallback User-Agent | a browser-like default |

Env vars are read in `ConversionOptions.from_env()` and merged with any explicit overrides at the call site. This keeps the public API ergonomic but allows operators to configure deployment-wide behavior without code changes.

### D7. CLI / web UI surface

- Web UI (`src/notebooklm/web/`): batch-job spec gains an optional `keep_original: bool` field; the existing `categories: ["sources", ...]` selection is unchanged. The UI defaults the checkbox to off.
- `notebook_batch.py`: add `--keep-original` flag to `cmd_source_download`. Remove the `wkhtmltopdf` branch from the default; if the user sets `--legacy-pdf` (new flag, off by default), the old path is restored exactly as today (kept as an escape hatch for one release before deletion).
- Log/progress prefixes:
  - `[markdown.new]` for successful remote conversion
  - `[fallback]` when the local httpx/markdownify path runs
  - `[markitdown]` for file → md
  - `[fulltext]` unchanged for the existing get_fulltext path
  - `[passthrough]` when the source was already a markdown / pasted-text and we just wrote it
  - `[legacy-pdf]` if the user opted into `--legacy-pdf`

### D8. Dependency layout

`pyproject.toml` extras:

- `[markdown]` (new): `markitdown[all]`, `markdownify`
- `[all]`: extends to include `[markdown]`
- Core deps unchanged. `httpx` already present.

Importing `notebooklm.conversion` itself never imports `markitdown` or `markdownify` at module-load time — both are imported lazily inside the strategy functions so a base install can still call `url_to_markdown` (remote-only path uses only `httpx`, which is core).

Document install in `docs/configuration.md`:

```bash
uv pip install -e ".[markdown]"   # minimal: markdown conversion only
uv pip install -e ".[all]"        # everything including conversion
```

## Risks / Trade-offs

- **`markdown.new` availability** → Mitigation: local fallback covers downtime, rate limits, and 4xx/5xx; env vars allow operators to disable remote entirely.
- **`markdownify` output quality varies** by source HTML → Mitigation: tests pin a few representative pages; users who need higher fidelity can opt into `--legacy-pdf` for one release. Long-term we could add a Playwright-based renderer as another opt-in.
- **`markitdown` system deps** (e.g. `tesseract` for image OCR inside PDFs) are non-trivial → Mitigation: `[markdown]` extra documents required system packages; failure surfaces a clear `ConversionDependencyError`.
- **BREAKING file extension change** (`.pdf` → `.md` for web sources) silently breaks user scripts → Mitigation: a CHANGELOG entry, a migration note in `docs/configuration.md`, and a one-release `--legacy-pdf` escape hatch keep the old behavior reachable.
- **Privacy**: routing every URL through `markdown.new` exposes those URLs to a third party → Mitigation: document in `docs/configuration.md`; users with sensitive URLs set `NOTEBOOKLM_DISABLE_MARKDOWN_NEW=1`.
- **Larger install footprint** with `markitdown[all]` → Mitigation: gated behind the optional `[markdown]` extra; base install size unchanged.
- **Concurrency on `markdown.new`** could trigger rate limits → Mitigation: the orchestrator already caps concurrency at 3; on `429` we drop straight to fallback rather than backing off. If this proves insufficient, add a per-host semaphore in a follow-up.

## Migration Plan

1. Add the `[markdown]` extra and the new `notebooklm.conversion` package; ship them inert (no caller wired up). Tests for the module land in this step.
2. Wire `web/jobs.py` to call `source_to_markdown`; update the `_SOURCE_EXT_MAP` and the existing tests that assert `.pdf` outputs.
3. Wire `notebook_batch.py` to call the same module; add `--keep-original` and `--legacy-pdf` flags.
4. Update docs (`README.md`, `docs/cli-reference.md`, `docs/configuration.md`, `docs/web-ui.md`) and `CHANGELOG.md` with the breaking change and migration note.
5. Release. Keep `--legacy-pdf` for one minor version, then delete the `wkhtmltopdf` branch.

**Rollback**: revert the wiring commits in step 2 and 3; the new module can stay (unused).

## Open Questions

- Do we want a separate target file when keeping the original binary, or should `keep_original=True` produce both `<title>.md` AND `<title>.pdf`/`.docx`/etc.? (Current plan: yes, both side-by-side. Confirm during specs.)
- Should the fallback path also try `readability-lxml` to extract the article body before running `markdownify`? It produces noticeably cleaner output for news/blog pages but adds a dependency. Default plan: skip for v1, revisit if user feedback warrants it.
- Should `CSV` sources be converted to Markdown tables (markitdown supports this), or kept as `.csv`? Current plan: keep as `.csv` — a Markdown table loses CSV's downstream utility (spreadsheet import). Confirm during specs.
- Naming: is `keep_original` the right field name, or should it be `also_keep_binary` / `keep_source_file`? The choice affects the CLI flag too.
