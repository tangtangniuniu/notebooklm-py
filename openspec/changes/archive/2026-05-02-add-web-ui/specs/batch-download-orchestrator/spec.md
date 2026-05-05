## ADDED Requirements

### Requirement: Job creation
The system SHALL accept a batch download specification (notebook ID, target directory, set of categories with category-specific options, force flag) and create an in-process `BatchJob` with a unique `job_id`.

#### Scenario: Create job
- **WHEN** the UI submits a batch download request with categories `[sources, audio, notes]` and target directory `./out`
- **THEN** the system creates a `BatchJob`, returns `{job_id, total_items, status: "pending"}`, and begins executing items asynchronously

#### Scenario: Empty selection
- **WHEN** the UI submits a batch with zero categories selected
- **THEN** the system returns HTTP 400 with `{error: "no categories selected"}` and creates no job

### Requirement: Categories supported
The system SHALL support the following download categories, each producing files in the target directory: `sources`, `audio`, `video`, `slide-deck`, `infographic`, `report`, `mind-map`, `data-table`, `quiz`, `flashcards`, `notes`.

#### Scenario: Sources category download strategies
- **WHEN** the `sources` category is included
- **THEN** for each source in the notebook the system applies the same per-type strategy as `notebook_batch.py.cmd_source_download` (direct download for PDF/DOCX/PPTX/CSV, fulltext for MARKDOWN/PASTED_TEXT, `wkhtmltopdf` for WEB_PAGE when available, `.todo` placeholder otherwise)

#### Scenario: Notes category
- **WHEN** the `notes` category is included
- **THEN** the system writes one `<sanitized-title>.md` file per note containing the note's content

#### Scenario: Artifact category
- **WHEN** an artifact category (e.g., `audio`, `video`, `slide-deck`) is included
- **THEN** the system downloads every existing artifact of that type into the target directory using filenames consistent with `notebooklm download <type> --all`

### Requirement: Bounded concurrency
The system SHALL execute job items with a configurable maximum concurrency (default 3) and SHALL NOT exceed that limit across all categories within a single job.

#### Scenario: Default concurrency
- **WHEN** a job has 12 items and concurrency is at default
- **THEN** at most 3 items are in `running` state at any moment

#### Scenario: User-configured concurrency
- **WHEN** the UI passes `concurrency: 1`
- **THEN** items run strictly sequentially

### Requirement: Skip-if-exists semantics
The system SHALL skip any item whose target file already exists, marking it `skipped` in the job report, unless the `force` flag is set.

#### Scenario: Skip existing
- **WHEN** an item's target path exists and `force` is false
- **THEN** the item completes immediately with status `skipped` and message `file exists`

#### Scenario: Force re-download
- **WHEN** an item's target path exists and `force` is true
- **THEN** the item proceeds with the download, overwriting the existing file on success

### Requirement: Progress events
The system SHALL emit a progress event for every item state transition (`queued` → `running` → `done` / `error` / `skipped`) on the job's SSE channel, plus a final `complete` event with the full summary.

#### Scenario: Per-item events
- **WHEN** an item transitions state
- **THEN** the SSE channel for the job emits `event: item` with payload `{item_id, category, label, status, message}`

#### Scenario: Completion event
- **WHEN** every item in the job has reached a terminal state
- **THEN** the SSE channel emits `event: complete` with `{job_id, total, done, skipped, error}` and closes

#### Scenario: Streaming progress for large items
- **WHEN** a single item supports incremental progress (e.g., a large file download)
- **THEN** the SSE channel emits `event: progress` payloads `{item_id, bytes_done, bytes_total}` at most once per second per item

### Requirement: Per-item error isolation
The system SHALL capture errors at the item level and SHALL NOT abort the entire job when an individual item fails.

#### Scenario: One item fails
- **WHEN** an item raises an exception during download
- **THEN** the item's status becomes `error` with the exception message captured, and remaining items continue to execute

#### Scenario: Final summary on partial failure
- **WHEN** a job finishes with a mix of `done`, `skipped`, and `error` items
- **THEN** the `complete` event reports the count for each terminal state and the job's overall status is `partial`

### Requirement: Job query and cancellation
The system SHALL allow clients to query a job's current status and to request cancellation. Cancellation SHALL stop scheduling new items; in-flight items run to completion.

#### Scenario: Query running job
- **WHEN** the UI calls `GET /api/jobs/<job_id>`
- **THEN** the system returns the current state: `{job_id, status, total, queued, running, done, skipped, error, started_at}`

#### Scenario: Cancel a job
- **WHEN** the UI calls `POST /api/jobs/<job_id>/cancel` while items remain queued
- **THEN** the queued items transition to `cancelled`, in-flight items complete normally, and the final summary's status is `cancelled`

### Requirement: Filename sanitization
The system SHALL sanitize titles into filesystem-safe names while preserving CJK characters, matching the algorithm used by `notebook_batch.py.sanitize_filename`.

#### Scenario: CJK title preserved
- **WHEN** a source title is `克劳德中文教学课程`
- **THEN** the resulting filename retains those characters (e.g., `克劳德中文教学课程.pdf`)

#### Scenario: Unsafe characters replaced
- **WHEN** a title contains `/`, `:`, or other path-unsafe characters
- **THEN** they are replaced with `_` and the result is truncated to 100 characters
