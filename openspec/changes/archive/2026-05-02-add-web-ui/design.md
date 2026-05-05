## Context

`notebooklm-py` exposes a complete async Python client (`NotebookLMClient`) and a Click-based CLI. Two surfaces exist today:

1. **CLI** — efficient, scriptable, but command-line only.
2. **`notebook_batch.py`** — a top-level script that shells out to the CLI via `subprocess` to provide six interactive flows (select, dedup, source-table, source-download, note-download, download-all). It re-parses Rich tables from stdout and is brittle.

The official NotebookLM web UI uses a three-panel layout (Sources / Chat / Studio). Users want that ergonomics for `notebooklm-py`, plus capabilities the official UI lacks: durable Q&A history with Markdown export, and arbitrary multi-select batch downloads with live progress.

**Stakeholders**: power users who already drive the CLI; casual users who want a visual surface without leaving Python. Constraints: project is Python-only, async, ships via `pip`/`uv`, no Node toolchain at install time, must run on Linux/macOS/Windows.

## Goals / Non-Goals

**Goals:**
- Single command (`notebooklm ui`) launches a local UI; user does not touch the terminal again for normal workflows.
- Faithfully reproduce NotebookLM's three-panel layout in spirit (Sources / Chat / Studio).
- Replace every `notebook_batch.py` flow with a richer, progress-aware UI equivalent.
- Auto-persist every Q&A turn per notebook and export any conversation as Markdown in one click.
- Reuse `NotebookLMClient` directly — no re-implementation, no subprocess shelling.
- Zero Node build step at install time.

**Non-Goals:**
- Multi-user / multi-tenant deployment. The server binds to `127.0.0.1` and assumes a single local user.
- Authoring a fully custom design system. The UI uses an established CSS framework.
- Replacing the CLI. CLI remains the primary scripting surface.
- Hosting the UI remotely or behind a reverse proxy. (Out of scope; if added later, requires a separate auth story.)
- Mobile responsive layout beyond "doesn't look broken at tablet width."
- Real-time collaboration / multi-tab notebook locking.

## Decisions

### D1: Local web app over native desktop or TUI
- **Choice**: FastAPI server + browser-rendered SPA, launched by `notebooklm ui` which opens the default browser to `http://127.0.0.1:<port>`.
- **Rationale**: The screenshot is a web app; web rendering handles the three-panel + streaming chat layout natively; no native packaging per platform; reuses existing async stack.
- **Alternatives considered**:
  - **PyQt/PySide** — heavyweight install, platform packaging headaches, async integration awkward with Qt event loop.
  - **Textual TUI** — fast and Python-native, but cannot match the screenshot's aesthetic ("美观专业") and the user explicitly referenced the web UI image.
  - **Tauri/Electron** — requires Node toolchain; violates "no Node at install time."

### D2: Frontend = HTMX + Alpine.js + Tailwind (CDN), no build step
- **Choice**: Server-rendered HTML via Jinja2 templates, progressive enhancement with HTMX for partial updates, Alpine.js for local interactivity, Tailwind via Play CDN in dev / pre-built CSS shipped as a static asset for production.
- **Rationale**: Zero build pipeline. Python developers can edit templates directly. HTMX maps cleanly to FastAPI route handlers. Tailwind gives the polished look the user asked for.
- **Alternatives considered**:
  - **React/Vue with Vite** — best DX for complex apps, but introduces Node, npm, and a build step. Disproportionate for a local tool.
  - **Pure server-rendered without HTMX** — works, but full-page reloads kill the chat-streaming UX.
  - **Streamlit / Gradio** — fast to build but inflexible layout; cannot achieve the three-panel design.

### D3: Streaming = Server-Sent Events (SSE), not WebSockets
- **Choice**: SSE for chat token streams and download progress.
- **Rationale**: One-way server-to-client is all we need. SSE is simpler than WebSockets, works through any HTTP/1.1 stack, has built-in reconnect, and FastAPI/`sse-starlette` integration is a few lines.
- **Alternatives considered**:
  - **WebSockets** — full duplex needed only if we add collaboration. Overkill today; can be added later without breaking SSE clients.
  - **Long polling** — works but laggy and wasteful.

### D4: Auth reuses existing `notebooklm login` storage
- **Choice**: The UI does not implement a Google OAuth flow. On startup it loads `AuthTokens.from_storage()`. If absent or expired, the UI shows a "Run `notebooklm login` in your terminal, then click Refresh" panel and offers a button that triggers `client.refresh_auth()`.
- **Rationale**: `notebooklm login` already drives Playwright through Google's sign-in; reimplementing it inside the web UI would mean either embedding a browser (Tauri territory) or trusting the user to paste cookies (worse UX). Consistent with the rest of the project.
- **Alternatives considered**:
  - **In-UI Playwright launch** — feasible but doubles the auth surface area and complicates the "single command" goal.

### D5: Conversation history = append-only JSONL per notebook
- **Choice**: One file per notebook at `<config_dir>/conversations/<notebook_id>.jsonl`. Each line is one Q&A turn: `{ts, question, answer, citations, conversation_id, turn_id}`.
- **Rationale**: Append-only is crash-safe and trivial to tail. Per-notebook scoping matches user mental model. JSONL streams cleanly into the UI without parsing the whole file. Markdown export reads the file and emits formatted output.
- **Alternatives considered**:
  - **SQLite** — overkill for the read/write pattern (always append, scan-by-notebook). Would add a migration story.
  - **Single global JSONL** — forces every read to filter by notebook_id; per-notebook files keep the working set small.
  - **Storing in NotebookLM itself** — Google's chat history API is unreliable and out of our control; the whole point is durability outside Google.

### D6: Batch download = an in-process job queue, not threads or subprocesses
- **Choice**: A `BatchJob` object with `asyncio.Queue` of items and `asyncio.gather` of N workers (default N=3). Each item emits progress events to a per-job SSE channel. State is in-memory; jobs are ephemeral and tied to the server lifetime.
- **Rationale**: All underlying client calls are already async. No need for threading. Bounded concurrency protects the upstream RPC from rate limits. Per-job SSE channels are cheap.
- **Trade-off**: Restarting the server cancels in-flight jobs. Acceptable because (a) the server is local and rarely restarts, and (b) skip-if-exists semantics make resumption a one-click retry.
- **Alternatives considered**:
  - **`subprocess` to existing CLI** (what `notebook_batch.py` does) — slow per-call, fragile output parsing, no live progress. The whole point of this rewrite is to drop this.
  - **Background task queue (Celery/RQ)** — pure overkill for a local single-user app.

### D7: Skip-if-exists everywhere, with explicit "force re-download" affordance
- **Choice**: Every download item checks the destination path and reports `skipped` if present, matching `notebook_batch.py` semantics. UI exposes a "Force re-download" toggle per batch.
- **Rationale**: Users routinely re-run downloads; skipping is the expected default.

### D8: Optional `[ui]` install extra
- **Choice**: `pip install notebooklm-py[ui]` pulls in `fastapi`, `uvicorn`, `sse-starlette`, `jinja2`. Static assets (Alpine, HTMX, Tailwind CSS) ship inside the wheel under `src/notebooklm/web/static/`.
- **Rationale**: Keeps the core install lean for users who only want the library/CLI. Pre-bundled static assets mean no CDN dependency at runtime (CDN is fine for development).

### D9: Port selection
- **Choice**: Default port 8765, configurable via `--port`. If port is busy, try the next 10 ports automatically before giving up.
- **Rationale**: Avoids collisions with common dev servers (3000, 5000, 8000, 8080).

## Risks / Trade-offs

- **[Risk] CSRF token expiry mid-session** → Mitigation: every API route catches the auth-error response from the client, surfaces a banner in the UI with a "Refresh auth" button that calls `client.refresh_auth()`; if that fails, instruct the user to re-run `notebooklm login`.
- **[Risk] Google rate-limiting batch downloads** → Mitigation: bounded worker concurrency (D6, default 3) plus configurable inter-item delay; per-item errors are captured and shown without aborting the whole batch.
- **[Risk] HTMX + Alpine combo can produce hard-to-debug interactions** → Mitigation: keep state on the server side wherever possible; Alpine handles only local UI affordances (toggles, modals); avoid building app state in the client.
- **[Risk] Browser auto-launch fails on headless Linux / WSL** → Mitigation: always print the URL to the terminal as the source of truth; the auto-open is a convenience, not a contract.
- **[Risk] Conversation JSONL grows unbounded** → Mitigation: not a problem at human scale (a heavy user produces <10MB/year), but document the location and add a future "archive old turns" affordance if needed. Out of scope here.
- **[Risk] Static asset duplication if Tailwind is updated** → Mitigation: pin versions in a `web/static/VERSIONS.txt` and document the update process in `docs/web-ui.md`.
- **[Risk] Markdown export of long conversations may include sensitive data the user pasted into questions** → Mitigation: the export is local-only; document that the user controls the file. Don't auto-upload anywhere.
- **[Trade-off] No multi-tab safety**: if two browser tabs drive the same notebook, the last write wins for things like rename. Acceptable for a single-user local tool; document the limitation.
- **[Trade-off] No mobile layout**: design assumes ≥1024px width. Below that, panels stack vertically with a navigation toggle but the experience degrades.

## Migration Plan

This is purely additive — no migration of existing user data or behavior:

1. Land `src/notebooklm/web/` and `src/notebooklm/_history.py` behind the `[ui]` extra.
2. Add `notebooklm ui` subcommand. Existing CLI commands unchanged.
3. Document in `docs/web-ui.md` and add a "Try the UI" callout to `README.md`.
4. Mark `notebook_batch.py` as deprecated in its docstring, pointing at the UI; do not remove yet.
5. After one release cycle of UI usage, propose removing `notebook_batch.py` in a follow-up change.

**Rollback**: `pip install notebooklm-py` (without `[ui]`) is unaffected. Users can ignore the new subcommand. No data migration to undo.

## Open Questions

- **Q1**: Should chat answers stream token-by-token, or arrive as a single completed turn? Streaming requires the underlying `client.chat.ask` to expose a streaming variant — needs a check of `_chat.py`. If not available, fall back to "spinner + final answer" for v1 and add streaming when the client API supports it.
- **Q2**: Should the conversation log capture *citations* (source pointers in the answer)? Depends on what the chat API returns. Default: yes if available, omit otherwise; schema is forward-compatible.
- **Q3**: Should the UI offer a "stop" button for long-running artifact generation? The underlying API may not expose a cancel; if not, the button removes the job from the UI but the upstream task continues. Acceptable for v1.
- **Q4**: Theme (light / dark / auto)? Default to `prefers-color-scheme`; out of scope to add an in-app toggle in v1.
