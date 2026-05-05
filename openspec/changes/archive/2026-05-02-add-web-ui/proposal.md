## Why

NotebookLM users currently have two ways to drive `notebooklm-py`: the `notebooklm` CLI (efficient but command-line only) and `notebook_batch.py` (a thin wrapper that bolts together CLI subprocess calls). Neither offers an interactive, visual workflow for the common case: log in, browse notebooks, pick which sources/artifacts/notes to download, watch progress, ask questions, and keep a record of the conversation. Power users want the breadth of the underlying client (every source type, every artifact type, batch operations) with the ergonomics of the official NotebookLM web UI — and one capability the official UI lacks: durable, exportable Q&A history that survives across sessions and can be saved as Markdown with one click.

## What Changes

- Add a local web UI (`notebooklm ui`) that launches a FastAPI server and opens the user's browser to a three-panel app modeled on the official NotebookLM layout: **Sources** (left), **Chat / Q&A** (center), **Studio & Downloads** (right).
- Login flow inside the UI that drives the existing storage-based auth: detects whether `notebooklm login` state exists, surfaces status, and offers a one-click "refresh auth" action; falls back to instructions for running `notebooklm login` when no state is present.
- Notebook picker: list all notebooks with title / created date / source count; selecting one becomes the active context for the rest of the UI (same semantics as `notebooklm use`).
- Source panel: list sources with type icons, multi-select checkboxes, search filter, and a deduplicate action (matches `notebook_batch.py dedup`). Per-source actions: rename, delete, view fulltext, download.
- Batch download panel: pick any combination of {sources, audio, video, slide-deck, infographic, report, mind-map, data-table, quiz, flashcards, notes} and a target directory; show per-item progress with status (queued → running → done/error/skipped) and a final summary, mirroring `notebook_batch.py download-all` but with live progress instead of console scroll.
- Chat panel: ask questions against the active notebook, stream answers, and **automatically persist every Q&A turn to a per-notebook conversation log** stored in the user's config dir. Conversation list is browsable and searchable.
- One-click "Export to Markdown" for any conversation (or a selected range of turns), producing a formatted `.md` file with metadata header (notebook title, date range, source citations).
- Studio panel: list existing artifacts, trigger generation of new artifacts, and download finished ones — with progress for in-flight generations.
- Reuse existing `NotebookLMClient` — UI is a thin presentation layer over the same async APIs the CLI uses. No changes to RPC layer.

## Capabilities

### New Capabilities
- `web-ui-server`: Local FastAPI server that hosts the UI, exposes a JSON API over the existing `NotebookLMClient`, and streams progress events (SSE/WebSocket) to the browser.
- `web-ui-frontend`: Browser-based three-panel application (Sources / Chat / Studio) implementing the NotebookLM-style layout, notebook selection, source management, batch download with progress, and chat.
- `conversation-history`: Per-notebook persistent storage of chat Q&A turns, with list/search/replay and one-click Markdown export.
- `batch-download-orchestrator`: Async job orchestration for multi-item downloads with per-item progress reporting, skip-if-exists semantics, and structured result summaries (replaces the subprocess-driven flow in `notebook_batch.py`).

### Modified Capabilities
<!-- None: this change adds a new surface alongside the CLI; it consumes existing client APIs without modifying their requirements. -->

## Impact

- **New code**: `src/notebooklm/web/` (FastAPI app, routes, SSE/WebSocket handlers, static frontend assets), `src/notebooklm/_history.py` (conversation persistence), `src/notebooklm/cli/ui.py` (the `notebooklm ui` command).
- **New dependencies (optional extra `[ui]`)**: `fastapi`, `uvicorn`, `sse-starlette` (or `websockets`); frontend bundled as static assets (no Node build step required at install time — ship pre-built or use a CDN-loaded framework like HTMX/Alpine for minimal footprint).
- **Existing code**: No behavior changes to `client.py`, `_core.py`, RPC layer, or the existing CLI commands. The new `ui` subcommand is additive.
- **Storage**: Conversation history stored under the existing config dir (e.g. `~/.config/notebooklm/conversations/<notebook-id>.jsonl`).
- **`notebook_batch.py`**: Becomes redundant for interactive use; can be deprecated in a follow-up, but is out of scope for this change.
- **Docs**: Add `docs/web-ui.md` and update `README.md` quickstart with a "Try the UI" section.
- **Testing**: Unit tests for history store and batch orchestrator; integration tests for the FastAPI routes against a mocked client; the frontend gets smoke tests via Playwright (already a dev dependency for the project's auth flow).
