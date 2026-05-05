# web-ui-server Specification

## Purpose
TBD - created by archiving change add-web-ui. Update Purpose after archive.
## Requirements
### Requirement: UI launch command
The system SHALL provide a `notebooklm ui` CLI subcommand that starts a local FastAPI server, prints the URL, and opens the default browser to that URL.

#### Scenario: Default launch
- **WHEN** the user runs `notebooklm ui` with no arguments
- **THEN** the system binds an HTTP server to `127.0.0.1:8765`, prints `Serving NotebookLM UI at http://127.0.0.1:8765` to stdout, and attempts to open the URL in the default browser

#### Scenario: Port already in use
- **WHEN** the user runs `notebooklm ui` and port 8765 is already bound
- **THEN** the system tries ports 8766–8775 in order and binds to the first available, printing the chosen URL

#### Scenario: All candidate ports busy
- **WHEN** ports 8765–8775 are all bound
- **THEN** the system exits with a non-zero status and prints `No free port in 8765-8775; specify --port`

#### Scenario: Explicit port override
- **WHEN** the user runs `notebooklm ui --port 9000`
- **THEN** the system binds to `127.0.0.1:9000` and does not try other ports

#### Scenario: Headless environment with no browser
- **WHEN** browser auto-launch fails or `--no-browser` is passed
- **THEN** the system still serves the UI and prints the URL to stdout, exiting normally only on Ctrl+C

### Requirement: Server binds to loopback only
The system SHALL bind the UI server to `127.0.0.1` and SHALL NOT accept connections from non-loopback addresses by default.

#### Scenario: Remote connection attempt
- **WHEN** a request originates from any address other than `127.0.0.1` / `::1`
- **THEN** the connection is refused at the socket level

### Requirement: JSON API mirrors client capabilities
The system SHALL expose JSON HTTP endpoints that wrap `NotebookLMClient` operations: list notebooks, select notebook, list/add/rename/delete sources, list/get/create notes, list artifacts, ask chat questions, and trigger artifact generation.

#### Scenario: Notebook list endpoint
- **WHEN** the browser issues `GET /api/notebooks`
- **THEN** the system returns `200 OK` with a JSON array of `{id, title, created_at, source_count}` for every notebook the authenticated user owns

#### Scenario: Source addition endpoint
- **WHEN** the browser issues `POST /api/notebooks/<id>/sources` with `{type: "url", value: "https://example.com"}`
- **THEN** the system calls `client.sources.add_url(id, value)` and returns the resulting source descriptor

#### Scenario: Auth failure response
- **WHEN** any API endpoint encounters an `AuthError` from the underlying client
- **THEN** the system returns HTTP 401 with `{error: "auth", detail: "<message>"}` and the frontend displays the auth-refresh banner

### Requirement: Auth state and refresh
The system SHALL load authentication via `AuthTokens.from_storage()` at startup, surface auth status in the UI, and provide a refresh action that calls `client.refresh_auth()` without restarting the server.

#### Scenario: Server starts with valid auth
- **WHEN** `~/.config/notebooklm/storage_state.json` exists and contains valid cookies
- **THEN** the UI loads with the notebook picker enabled

#### Scenario: Server starts with no auth state
- **WHEN** no storage state exists
- **THEN** the UI displays a "Run `notebooklm login` in your terminal" panel and disables all notebook actions

#### Scenario: Refresh after expired CSRF
- **WHEN** the user clicks "Refresh auth" after a 401
- **THEN** the system calls `client.refresh_auth()`, and on success removes the banner and re-enables actions; on failure surfaces the error and keeps the banner

### Requirement: Server-Sent Events channels
The system SHALL provide SSE endpoints for chat streaming (`GET /api/chat/<conversation_id>/stream`) and batch download progress (`GET /api/jobs/<job_id>/stream`).

#### Scenario: Chat token streaming
- **WHEN** the browser opens an EventSource at `/api/chat/<id>/stream` while a chat turn is in flight
- **THEN** the server emits `event: token` messages as the answer arrives and a final `event: done` with the complete turn record

#### Scenario: Batch progress events
- **WHEN** the browser opens an EventSource at `/api/jobs/<job_id>/stream` for an active job
- **THEN** the server emits `event: item` messages with `{item_id, status, progress, message}` and a final `event: complete` with the job summary

### Requirement: Optional install extra
The system SHALL be installable as `notebooklm-py[ui]` to pull in web-only dependencies (`fastapi`, `uvicorn`, `sse-starlette`, `jinja2`), and the `notebooklm ui` command SHALL fail with a helpful message if those dependencies are missing.

#### Scenario: UI command without ui extra
- **WHEN** a user runs `notebooklm ui` after `pip install notebooklm-py` (no extra)
- **THEN** the command exits with status 1 and prints `notebooklm ui requires the [ui] extra. Install with: pip install notebooklm-py[ui]`

