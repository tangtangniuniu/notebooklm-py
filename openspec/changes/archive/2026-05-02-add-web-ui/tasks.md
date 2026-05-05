## 1. Project setup

- [x] 1.1 Add optional `[ui]` extra to `pyproject.toml` with `fastapi`, `uvicorn`, `sse-starlette`, `jinja2`, `python-multipart`
- [x] 1.2 Create `src/notebooklm/web/` package skeleton (`__init__.py`, `app.py`, `routes/`, `static/`, `templates/`)
- [x] 1.3 Add an import-time guard in `src/notebooklm/web/__init__.py` that raises a clear `ImportError` with install hint when FastAPI is missing
- [x] 1.4 Vendor pre-built static assets into `src/notebooklm/web/static/`: Tailwind CSS (compiled), HTMX, Alpine.js; record versions in `static/VERSIONS.txt`
- [x] 1.5 Configure `pyproject.toml` to include `web/static/**` and `web/templates/**` as package data

## 2. Conversation history backend (`_history.py`)

- [x] 2.1 Define `Turn` and `Conversation` dataclasses with the schema from `specs/conversation-history`
- [x] 2.2 Implement `ConversationStore` with methods: `append_turn`, `list_conversations(notebook_id)`, `replay(notebook_id, conversation_id)`, `export_markdown(...)`
- [x] 2.3 Implement path resolution under `<config_dir>/conversations/<notebook_id>.jsonl` with path-traversal validation
- [x] 2.4 Implement append with `O_APPEND` to be safe under concurrent writes; one JSON object per line
- [x] 2.5 Implement Markdown exporter producing the YAML metadata header + per-turn `### Question` sections + Sources sub-section
- [x] 2.6 Reuse / port `sanitize_filename` from `notebook_batch.py` into `src/notebooklm/_filename.py` and use it from the exporter
- [x] 2.7 Unit tests: append, list, replay, export single conversation, export entire notebook, path traversal rejection, CJK preservation, concurrent writes

## 3. Batch download orchestrator (`web/jobs.py`)

- [x] 3.1 Define `BatchJob`, `JobItem`, `JobStatus` types and an in-memory `JobRegistry`
- [x] 3.2 Implement `create_job(spec) -> BatchJob` that expands the category selection into concrete `JobItem`s using the active `NotebookLMClient`
- [x] 3.3 Implement source-category strategies matching `notebook_batch.py.cmd_source_download` (PDF/DOCX/PPTX/CSV direct, fulltext for MARKDOWN/PASTED_TEXT, `wkhtmltopdf` for WEB_PAGE, `.todo` placeholder)
- [x] 3.4 Implement artifact-category items wrapping `client.artifacts.*` download calls (audio/video/slide-deck/infographic/report/mind-map/data-table/quiz/flashcards)
- [x] 3.5 Implement notes-category items writing each note's content as `<sanitized-title>.md`
- [x] 3.6 Implement bounded concurrency via an `asyncio.Semaphore` (default 3, configurable per job)
- [x] 3.7 Implement skip-if-exists with a per-job `force` override
- [x] 3.8 Implement per-item progress reporting via an `asyncio.Queue` consumed by the SSE channel
- [x] 3.9 Implement `cancel(job_id)` semantics (queued items → `cancelled`, in-flight run to completion)
- [x] 3.10 Unit tests with a mock client: skip semantics, concurrency cap, error isolation, cancellation, sanitization for CJK titles
- [x] 3.11 Integration test: end-to-end small batch against a fully mocked client and a temporary target directory

## 4. FastAPI server (`web/app.py`, `web/routes/`)

- [x] 4.1 Create `app.py`: FastAPI app factory, lifespan that initializes `AuthTokens.from_storage()` (tolerates missing auth), mounts static + templates
- [x] 4.2 Loopback-only enforcement: refuse non-`127.0.0.1`/`::1` clients via middleware
- [x] 4.3 `routes/auth.py`: `GET /api/auth/status`, `POST /api/auth/refresh`
- [x] 4.4 `routes/notebooks.py`: `GET /api/notebooks`, `GET /api/notebooks/<id>`, create/rename/delete
- [x] 4.5 `routes/sources.py`: list, add (URL/text/YouTube/file), rename, delete, fulltext, dedup-preview, dedup-execute
- [x] 4.6 `routes/notes.py`: list, get, create
- [x] 4.7 `routes/artifacts.py`: list, generate, download
- [x] 4.8 `routes/chat.py`: `POST /api/chat/<conversation_id>/ask`, `GET /api/chat/<conversation_id>/stream` (SSE), `GET /api/chat/conversations?notebook_id=...`, `GET /api/chat/conversations/<id>`, `GET /api/chat/conversations/<id>/export`
- [x] 4.9 `routes/jobs.py`: `POST /api/jobs` (create batch), `GET /api/jobs/<id>`, `GET /api/jobs/<id>/stream` (SSE), `POST /api/jobs/<id>/cancel`
- [x] 4.10 Centralized error handler: map `AuthError` → 401 with structured body; map other client exceptions → 502/500 with safe messages
- [x] 4.11 Integration tests for every route with a mocked `NotebookLMClient` (httpx test client)

## 5. Frontend templates and assets

- [x] 5.1 Base layout `templates/base.html`: header (notebook title, switcher, jobs drawer button), auth banner partial, main content slot, footer
- [x] 5.2 Notebook picker page `templates/picker.html` rendering the list with title/date/source-count and HTMX-driven row click → `/notebook/<id>`
- [x] 5.3 Notebook view `templates/notebook.html` with the three-panel CSS grid layout (Sources / Chat / Studio) responsive ≥1024px, stacked + tab-bar below
- [x] 5.4 Sources panel partial: list with type icons, multi-select checkboxes, search filter (Alpine), per-row actions, "Add source" + "Deduplicate" toolbar buttons
- [x] 5.5 Add-source modal: tabs for URL / Text / YouTube / file upload; HTMX form submit to corresponding API
- [x] 5.6 Deduplicate modal: shows duplicate groups, pre-checked deletes, confirm action
- [x] 5.7 Chat panel partial: scrollable history, input + Send button, "New conversation" + "Conversations…" + "Export to Markdown" controls; SSE consumer for streaming tokens
- [x] 5.8 Conversations drawer: list past conversations with date range and turn count; click to replay
- [x] 5.9 Studio panel partial: artifact list grouped by type with status + download/generate actions
- [x] 5.10 Batch download dialog: category checkboxes, target directory input, force toggle, Start button → POST /api/jobs and navigate to job view
- [x] 5.11 Job view partial / drawer: per-item rows updating from SSE, cancel button, summary on completion
- [x] 5.12 Auth banner partial with "Refresh auth" button wired to POST /api/auth/refresh
- [x] 5.13 Tailwind theming with `prefers-color-scheme` (light + dark variants for all components)
- [x] 5.14 SSE helper `static/sse.js` with reconnect/backoff, used by chat and jobs

## 6. CLI integration

- [x] 6.1 Add `src/notebooklm/cli/ui.py` registering a `notebooklm ui` Click command with options `--port`, `--host` (loopback-locked), `--no-browser`
- [x] 6.2 Implement port probing across 8765–8775 with explicit `--port` override
- [x] 6.3 Detect missing `[ui]` extra and exit with the install-hint message
- [x] 6.4 Auto-open the browser via `webbrowser.open` after server bind; print URL regardless

## 7. Documentation

- [x] 7.1 Add `docs/web-ui.md`: install (`pip install notebooklm-py[ui]`), launch, screenshot tour of the three panels, batch download walkthrough, conversation export, troubleshooting (auth banner, port conflicts, headless launch)
- [x] 7.2 Update `README.md` quickstart with a "Try the UI" callout
- [x] 7.3 Update `docs/configuration.md` to document the `<config_dir>/conversations/` location
- [x] 7.4 Mark `notebook_batch.py` deprecated in its module docstring, pointing at the UI; do not remove
- [x] 7.5 Update `CHANGELOG.md` under the next version

## 8. Quality gates

- [x] 8.1 Run `ruff format src/ tests/`
- [x] 8.2 Run `ruff check src/ tests/` and fix issues
- [x] 8.3 Run `mypy src/notebooklm --ignore-missing-imports`
- [x] 8.4 Run `pytest` with coverage; ensure new modules have meaningful coverage
- [ ] 8.5 Manual smoke test: install `[ui]` extra in a fresh venv, run `notebooklm ui`, log in, select a notebook, run a batch download with at least 5 items, ask a question, export Markdown, open the file
- [ ] 8.6 Playwright e2e (optional): scripted login + UI walkthrough, marked `@pytest.mark.e2e`
