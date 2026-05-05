# Web UI

The optional `[ui]` extra ships a local web app that mirrors NotebookLM's
three-panel layout (Sources / Chat / Studio) and adds:

- **Auto-saved Q&A history** — every chat turn is persisted per notebook and
  exportable as Markdown with one click.
- **Batch downloads** — pick any combination of sources, every artifact type,
  and notes; track per-item progress live in the browser.
- **Source dedup** — find duplicates by `(title, kind, url)` and remove them
  in one confirmation step (`notebook_batch.py` parity).

## Install

```bash
pip install "notebooklm-py[ui]"
playwright install chromium     # only needed for `notebooklm login`
```

The `[ui]` extra adds `fastapi`, `uvicorn`, `sse-starlette`, `jinja2`, and
`python-multipart`. Static assets (CSS, JS) ship inside the wheel; no Node
toolchain is required.

## Launch

```bash
notebooklm login   # one-time
notebooklm ui
```

Output:

```
Serving NotebookLM UI at http://127.0.0.1:8765
```

The browser opens automatically. Pass `--no-browser` to skip auto-open. If
8765 is busy the CLI probes 8766–8775; pass `--port 9000` to override.

The server binds to `127.0.0.1` only — non-loopback hosts are refused at the
socket and middleware level.

## Three-panel layout

| Panel | What it does |
| --- | --- |
| **Sources** (left) | List, search, multi-select, add (URL / Text / YouTube / file), rename, delete, dedup. |
| **Chat** (center) | Ask questions; every Q&A is saved to `~/.notebooklm/conversations/<notebook_id>.jsonl`. Browse past conversations from the drawer; export the current one as Markdown. |
| **Studio** (right) | Existing artifacts grouped by type, plus generate / download actions. |

Below 1024px width the panels stack with a tab bar; the layout still works on
tablet but isn't optimized for phones.

## Batch downloads

Click **Download…** in the header. The dialog accepts:

- **Target directory** — relative or absolute. Created if missing.
- **Categories** — sources, audio, video, slide-deck, infographic, report,
  mind-map, data-table, quiz, flashcards, notes. Multi-select.
- **Force re-download** — overwrite existing files. Default is skip-if-exists,
  matching `notebook_batch.py` semantics.

Clicking **Start** kicks off an async job and opens the job drawer. Each item
moves through `queued → running → done | skipped | error`. One failure does
not abort the rest. Cancellation stops queued items; in-flight items run to
completion.

**Concurrency** is controlled by a slider in the batch dialog (range 1..10,
default 5). Values outside that range are rejected by the API with HTTP 400.

**Slash-retry**: source URLs that return `404` or `403` on the first attempt
are retried once with the path's trailing slash toggled (stripped if
present, appended if absent). When that recovery succeeds, the item's
progress message gets a trailing ` (slash-retry)` suffix (e.g.
`markdown.new (slash-retry)`, `image:cover.png (slash-retry)`). Only 404
and 403 are retried; other errors propagate as before.

Source-category strategies follow `notebook_batch.py`:

- **PDF / DOCX / PPTX** with a URL: download the binary, convert to Markdown
  via `markitdown`, and write `<title>.md`. Set the **Keep original** option
  to also retain the binary as a sibling file.
- **Web pages**: convert to Markdown via `https://markdown.new/<url>` (primary)
  with a local `httpx` + `markdownify` fallback when `markdown.new` is
  unreachable, rate-limited, or returns an error page. Output is `<title>.md`.
  Set the **Legacy PDF (wkhtmltopdf)** option to revert to the previous PDF
  output (one-release escape hatch; will be removed).
- **CSV** with a URL: direct file download (`<title>.csv`) — Markdown
  conversion would lose spreadsheet utility.
- **Image** with a URL: download as-is (`<title>.<ext>`). The extension is
  picked from the response `Content-Type` (e.g. `image/png` → `.png`),
  falling back to a known image extension on the URL path, and finally
  defaulting to `.png`. Re-running a batch skips images that already exist
  under any known image extension.
- **Markdown / Pasted text**: write the indexed full text as `.md`.
- **Drive / YouTube / unsupported**: write a `.todo` placeholder.

Notes are written as `<sanitized-title>.md`.

The conversion module honors these environment variables:

| Env var | Effect |
|---|---|
| `NOTEBOOKLM_MARKDOWN_NEW_BASE` | Override the markdown.new base URL |
| `NOTEBOOKLM_DISABLE_MARKDOWN_NEW=1` | Skip the remote attempt, go straight to fallback |
| `NOTEBOOKLM_CONVERSION_TIMEOUT` | Per-request timeout in seconds (default 30) |
| `NOTEBOOKLM_CONVERSION_UA` | User-Agent for the local fallback HTTP request |

## Conversation history

Every Q&A turn is appended to `~/.notebooklm/conversations/<notebook_id>.jsonl`
with this schema:

```json
{
  "ts": "2026-05-02T12:34:56+00:00",
  "conversation_id": "uuid",
  "turn_id": "uuid",
  "question": "What is X?",
  "answer": "X is …",
  "citations": [{"source_id": "…", "cited_text": "…"}]
}
```

**Open past conversations**: `Conversations…` in the chat header.
**Export current conversation**: `⇩ Markdown` in the chat header. The export
includes a YAML metadata header, a `### Question` heading per turn, and a
`**Sources**` block when citations are present.

To export every conversation for a notebook, hit:

```
GET /api/chat/conversations/export-all?notebook_id=<id>
```

## Auth

The UI reuses the storage created by `notebooklm login`. If the cookie store
is missing or expired:

- A red banner appears with instructions.
- Click **Refresh auth** to re-read `storage_state.json` and refresh tokens.
- If that fails, run `notebooklm login` again in your terminal, then click
  **Refresh auth** in the UI.

The UI does not embed an OAuth flow — that's intentional and matches the
rest of the project (the Playwright-driven `notebooklm login` does the work).

## Troubleshooting

**Browser does not open** (headless / WSL): the URL is always printed to
stdout; open it manually. `--no-browser` prevents the auto-open attempt.

**Port conflicts**: the default probe window is 8765–8775. Use `--port` to
pin a specific one.

**Auth banner won't dismiss**: re-run `notebooklm login`. The banner reads
auth state freshly on each refresh.

**Markdown conversion errors**: web-page sources first try
`https://markdown.new/<url>`, then a local `httpx` + `markdownify` fallback.
Failures of both paths surface the underlying causes (HTTP status, network
error, etc.) in the item's progress message. To skip the remote attempt
entirely, set `NOTEBOOKLM_DISABLE_MARKDOWN_NEW=1` before launching the UI.

**Missing optional dependency**: PDF/DOCX/PPTX conversion requires the
`[markdown]` extra. Install via `pip install "notebooklm-py[markdown]"`
(or `[all]`) and restart the UI.

**`wkhtmltopdf` opt-in (legacy)**: select **Legacy PDF (wkhtmltopdf)** in the
batch dialog to revert web-page sources to the prior PDF output. Requires
`wkhtmltopdf` installed (`brew install wkhtmltopdf` / `apt install wkhtmltopdf`).
This option is provided as a one-release escape hatch and will be removed in
a future minor version.

**Updating bundled assets**: bumps go through
`src/notebooklm/web/static/VERSIONS.txt`; the pinned versions document
provenance. If you replace assets, keep the file in sync.

## Limitations

- Single-user, single-host. The server refuses non-loopback connections.
- Batch jobs live in memory; restarting the server cancels in-flight jobs.
  Skip-if-exists makes resumption a one-click retry.
- Chat is request/response, not token-streamed (the underlying client
  returns a single answer). The on-screen typing indicator is cosmetic
  for now.
