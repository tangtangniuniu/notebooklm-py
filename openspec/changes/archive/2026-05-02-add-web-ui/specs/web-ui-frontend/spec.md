## ADDED Requirements

### Requirement: Three-panel layout
The system SHALL render a three-panel layout (Sources / Chat / Studio) modeled on the official NotebookLM UI when a notebook is selected and viewport width is at least 1024px.

#### Scenario: Selected notebook view
- **WHEN** the user has selected a notebook
- **THEN** the page renders Sources panel on the left, Chat panel in the center, and Studio panel on the right, each independently scrollable

#### Scenario: Narrow viewport
- **WHEN** viewport width is below 1024px
- **THEN** the panels stack vertically with a top tab bar to switch between Sources / Chat / Studio

### Requirement: Notebook picker
The system SHALL display a notebook picker on initial load, showing every notebook with title, creation date, and source count, and SHALL set the active notebook context when one is selected.

#### Scenario: Open picker
- **WHEN** the user lands on `/` and no notebook context is set
- **THEN** the system displays a list of notebooks sorted by most recently modified, each row showing title, ISO date, and source count

#### Scenario: Select notebook
- **WHEN** the user clicks a notebook row
- **THEN** the active notebook context is set, the URL updates to `/notebook/<id>`, and the three-panel layout loads

#### Scenario: Switch notebook
- **WHEN** the user clicks the notebook title in the header from inside a notebook view
- **THEN** the picker re-opens and selecting a different notebook switches context without losing in-flight chat or download jobs (those jobs remain accessible via the Jobs drawer)

### Requirement: Sources panel
The system SHALL list all sources of the active notebook with a type icon, title, and per-row actions (rename, delete, view fulltext, download). The panel SHALL support multi-select with checkboxes and a search filter.

#### Scenario: Render source list
- **WHEN** a notebook is selected
- **THEN** the Sources panel lists every source with an icon corresponding to its `SourceType` and the title from the underlying record

#### Scenario: Multi-select
- **WHEN** the user checks the boxes for two or more sources
- **THEN** a "Selected: N" toolbar appears with bulk actions (Delete, Add to download)

#### Scenario: Search filter
- **WHEN** the user types into the search input
- **THEN** the source list filters to rows whose title contains the query (case-insensitive); empty query restores the full list

#### Scenario: Add source
- **WHEN** the user clicks "Add source" and chooses URL / Text / YouTube / file upload
- **THEN** the appropriate input modal appears, submission calls the corresponding API, and on success the new source appears in the list

#### Scenario: Deduplicate
- **WHEN** the user clicks "Deduplicate"
- **THEN** the system shows duplicate groups (same title + type + URL), pre-selects all but the latest, and asks the user to confirm deletion before calling delete on each

### Requirement: Chat panel
The system SHALL provide a chat interface that lets the user ask questions against the active notebook, displays the streaming answer, and shows a scrollable history of all Q&A turns for the current conversation.

#### Scenario: Ask a question
- **WHEN** the user types a question and presses Send
- **THEN** the question appears in the chat history, the assistant's reply streams in via SSE, and on completion the turn is appended to the persistent log (per `conversation-history`)

#### Scenario: New conversation
- **WHEN** the user clicks "New conversation"
- **THEN** a fresh `conversation_id` is allocated and the chat area clears; previous conversations remain accessible via the conversation list

#### Scenario: Open prior conversation
- **WHEN** the user opens the conversation list and selects a past conversation
- **THEN** the chat area replays every Q&A turn from the persisted log in order

#### Scenario: Export current conversation
- **WHEN** the user clicks "Export to Markdown" while a conversation is active
- **THEN** the browser downloads a `.md` file produced by the Markdown export from `conversation-history`

### Requirement: Studio and downloads panel
The system SHALL provide a Studio panel that lists existing artifacts, lets the user trigger generation of new artifacts, and provides a batch download form covering sources, all artifact types, and notes.

#### Scenario: List artifacts
- **WHEN** a notebook is selected
- **THEN** the Studio panel lists existing artifacts grouped by type (audio, video, slide-deck, infographic, report, mind-map, data-table, quiz, flashcards) with status and a download action when ready

#### Scenario: Generate artifact
- **WHEN** the user clicks "Generate" on an artifact type
- **THEN** the system kicks off the corresponding `client.artifacts.generate_*` call and shows a progress indicator until completion or failure

#### Scenario: Open batch download dialog
- **WHEN** the user clicks "Download…"
- **THEN** a dialog appears with checkboxes for each category (Sources, each artifact type, Notes), a target directory chooser, a "Force re-download" toggle, and a Start button

#### Scenario: Run batch download
- **WHEN** the user submits the batch download dialog
- **THEN** the system creates a job (per `batch-download-orchestrator`), navigates to a job-progress view, and displays per-item rows updating in real time via SSE

### Requirement: Auth banner
The system SHALL show an auth banner at the top of every page when authentication is missing or has failed, with text instructing the user how to recover and a "Refresh auth" button.

#### Scenario: Missing auth on load
- **WHEN** the page loads and the server reports `auth: missing`
- **THEN** a red banner reads "Not signed in. Run `notebooklm login` in your terminal, then click Refresh." and all action buttons are disabled

#### Scenario: Auth fails mid-session
- **WHEN** any API call returns 401
- **THEN** the banner appears with a "Refresh auth" button that calls the refresh endpoint when clicked

### Requirement: Static assets bundled in package
The system SHALL ship all required CSS/JS assets (Tailwind CSS, HTMX, Alpine.js) inside the installed package and SHALL NOT require a network connection at runtime to render the UI.

#### Scenario: Offline rendering
- **WHEN** the host has no internet access but `notebooklm-py[ui]` is installed
- **THEN** opening the UI in a browser still renders correctly with full styling and interactivity (only NotebookLM API calls fail, not the UI itself)
