## MODIFIED Requirements

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
