## MODIFIED Requirements

### Requirement: Categories supported
The system SHALL support the following download categories, each producing files in the target directory: `sources`, `audio`, `video`, `slide-deck`, `infographic`, `report`, `mind-map`, `data-table`, `quiz`, `flashcards`, `notes`.

#### Scenario: Sources category download strategies
- **WHEN** the `sources` category is included
- **THEN** for each source in the notebook the system applies the per-type strategy: `WEB_PAGE` is converted to `<title>.md` via the source-markdown-conversion capability (remote `markdown.new` primary path with local fallback); `PDF`, `DOCX`, and `PPTX` are converted to `<title>.md` via the source-markdown-conversion capability (file-to-Markdown via `markitdown`); `CSV` is downloaded directly as `<title>.csv`; `MARKDOWN` and `PASTED_TEXT` are written as `<title>.md` from `client.sources.get_fulltext`; unsupported source types produce a `<title>.todo` placeholder

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

#### Scenario: Notes category
- **WHEN** the `notes` category is included
- **THEN** the system writes one `<sanitized-title>.md` file per note containing the note's content

#### Scenario: Artifact category
- **WHEN** an artifact category (e.g., `audio`, `video`, `slide-deck`) is included
- **THEN** the system downloads every existing artifact of that type into the target directory using filenames consistent with `notebooklm download <type> --all`
