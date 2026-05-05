# batch-download-orchestrator Specification

## Purpose
TBD - created by archiving change add-web-ui. Update Purpose after archive.
## Requirements
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
- **THEN** for each source in the notebook the system applies the per-type strategy: `WEB_PAGE` is converted to `<title>.md` via the source-markdown-conversion capability (remote `markdown.new` primary path with local fallback); `PDF`, `DOCX`, and `PPTX` are converted to `<title>.md` via the source-markdown-conversion capability (file-to-Markdown via `markitdown`); `CSV` is downloaded directly as `<title>.csv`; `IMAGE` is downloaded directly as `<title>.<ext>` with the extension chosen from the response `Content-Type`, the URL path, or `.png` as a default; `MARKDOWN` and `PASTED_TEXT` are written as `<title>.md` from `client.sources.get_fulltext`; unsupported source types produce a `<title>.todo` placeholder

#### Scenario: Sources category default behavior for web pages
- **WHEN** the `sources` category is included AND the notebook contains a `WEB_PAGE` source AND the user has not opted into `--legacy-pdf` (or the equivalent web UI option)
- **THEN** the resulting file is `<title>.md` and the system does NOT invoke `wkhtmltopdf`

#### Scenario: Sources category opt-in legacy PDF
- **WHEN** the `sources` category is included AND the user passes `--legacy-pdf` (or the equivalent web UI option) AND `wkhtmltopdf` is installed
- **THEN** for each `WEB_PAGE` source the system writes `<title>.pdf` via `wkhtmltopdf` (the previous behavior), and the orchestrator's progress events report `strategy = "legacy-pdf"`

#### Scenario: Sources category retains original binary when requested
- **WHEN** the `sources` category is included with `keep_original=True` (or the equivalent CLI/web UI option) AND the notebook contains a `PDF`, `DOCX`, or `PPTX` source
- **THEN** the system writes both `<title>.md` and the original `<title>.pdf` / `<title>.docx` / `<title>.pptx` to the target directory

#### Scenario: wkhtmltopdf not installed in default flow
- **WHEN** the `sources` category is included AND the notebook contains a `WEB_PAGE` source AND `wkhtmltopdf` is not installed AND the user has not opted into `--legacy-pdf`
- **THEN** the item completes successfully via the source-markdown-conversion capability and produces `<title>.md` without writing any `.todo` placeholder

#### Scenario: Image extension picked from Content-Type
- **WHEN** the `sources` category is included AND the notebook contains an `IMAGE` source whose download response carries a `Content-Type` like `image/jpeg`, `image/png`, `image/gif`, `image/webp`, `image/svg+xml`, `image/bmp`, `image/tiff`, `image/x-icon`, `image/heic`, or `image/avif`
- **THEN** the resulting file is named `<title>.jpg` / `.png` / `.gif` / `.webp` / `.svg` / `.bmp` / `.tif` / `.ico` / `.heic` / `.avif` respectively (case-insensitive `Content-Type` match, parameters such as `; charset=...` ignored)

#### Scenario: Image extension picked from URL path
- **WHEN** an `IMAGE` source's download response has no recognizable `Content-Type` AND the URL path ends with a known image extension (`.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.svg`, `.bmp`, `.tif`, `.tiff`, `.ico`, `.heic`, `.avif`, case-insensitive)
- **THEN** the system uses that extension verbatim (lowercased) for `<title>.<ext>`

#### Scenario: Image extension default fallback
- **WHEN** an `IMAGE` source's download response has neither a recognizable `Content-Type` nor a URL path ending in a known image extension
- **THEN** the system writes the bytes to `<title>.png` (the default fallback) and the download completes successfully

#### Scenario: Image skip-if-exists across known extensions
- **WHEN** the `sources` category is included AND the notebook contains an `IMAGE` source AND a sibling file `<title>.<known-image-ext>` already exists in the target directory AND `force` is false
- **THEN** the item completes immediately with status `skipped` and message `file exists`, regardless of which specific extension the existing file has

#### Scenario: Image strategy reported in progress
- **WHEN** an `IMAGE` source download completes successfully
- **THEN** the orchestrator's `event: item` payload reports a strategy starting with `image` (e.g. `image:cover.png`) so SSE consumers can render the final filename

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

