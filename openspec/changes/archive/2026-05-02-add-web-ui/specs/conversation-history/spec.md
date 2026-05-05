## ADDED Requirements

### Requirement: Per-notebook conversation log
The system SHALL persist every chat Q&A turn to an append-only JSONL file scoped to the notebook, located under the user config directory at `<config_dir>/conversations/<notebook_id>.jsonl`.

#### Scenario: First turn in a new notebook
- **WHEN** the user submits a chat question for a notebook that has no existing log
- **THEN** the system creates `<config_dir>/conversations/<notebook_id>.jsonl` with parents created as needed, and writes one JSON line for the completed turn

#### Scenario: Subsequent turns
- **WHEN** the user completes a chat turn for a notebook that already has a log file
- **THEN** the system appends one JSON line to the existing file without rewriting earlier content

#### Scenario: Concurrent writes from two browser tabs
- **WHEN** two chat turns complete near-simultaneously for the same notebook
- **THEN** both turns are written without corruption (each line is a complete, parseable JSON object)

### Requirement: Turn record schema
Each line in the conversation log SHALL be a JSON object with at least the fields: `ts` (ISO 8601 UTC timestamp), `conversation_id` (UUID), `turn_id` (UUID), `question` (string), `answer` (string), and `citations` (array, possibly empty).

#### Scenario: Schema completeness
- **WHEN** a turn is persisted
- **THEN** the resulting JSON object contains all six required fields, even if `citations` is an empty array

#### Scenario: Forward compatibility
- **WHEN** future versions add new optional fields to the turn record
- **THEN** older readers SHALL still parse the file by ignoring unknown fields

### Requirement: List conversations for a notebook
The system SHALL expose an operation that returns the distinct conversation IDs in a notebook's log, each with first/last timestamp and turn count, sorted by most recent activity.

#### Scenario: Listing
- **WHEN** the UI requests the conversation list for a notebook with three conversations
- **THEN** the system returns three entries, each with `conversation_id`, `started_at`, `ended_at`, and `turn_count`, ordered by `ended_at` descending

#### Scenario: Empty log
- **WHEN** the UI requests the conversation list for a notebook with no log file
- **THEN** the system returns an empty list (not an error)

### Requirement: Replay a conversation
The system SHALL expose an operation that returns every turn for a given `conversation_id`, in chronological order.

#### Scenario: Replay existing conversation
- **WHEN** the UI requests turns for an existing `conversation_id`
- **THEN** the system returns every turn whose `conversation_id` matches, in ascending `ts` order

#### Scenario: Unknown conversation_id
- **WHEN** the UI requests turns for a `conversation_id` not present in any log
- **THEN** the system returns an empty list

### Requirement: Markdown export
The system SHALL provide a one-click export that converts a single conversation (or the entire notebook log) into a formatted Markdown document suitable for download.

#### Scenario: Export a single conversation
- **WHEN** the user clicks "Export to Markdown" on an active conversation
- **THEN** the system produces a `.md` document containing:
  - a YAML or `## Metadata` header with notebook title, conversation ID, start/end timestamps, and turn count
  - one section per turn with the question as a `### Question` heading and the answer as the body
  - a "Sources" sub-section listing citations when present

#### Scenario: Export filename
- **WHEN** the export is downloaded
- **THEN** the filename is `<sanitized-notebook-title>-<YYYY-MM-DD>.md`, using the same sanitizer rules as `notebook_batch.py.sanitize_filename` (preserving CJK characters)

#### Scenario: Export entire notebook log
- **WHEN** the user chooses "Export all conversations" for a notebook
- **THEN** the system produces a Markdown document with a `## Conversation <n>` heading per conversation, each containing the same per-turn structure as a single export

### Requirement: Filesystem safety
The system SHALL refuse to read or write conversation files outside the configured conversations directory and SHALL sanitize the `notebook_id` against path traversal.

#### Scenario: Notebook ID with path traversal
- **WHEN** the system is asked to load conversations for an ID containing `..` or path separators
- **THEN** the request is rejected with an error and no file outside the conversations directory is touched
