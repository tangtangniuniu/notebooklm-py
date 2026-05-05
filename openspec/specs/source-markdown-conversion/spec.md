# source-markdown-conversion Specification

## Purpose

Convert NotebookLM source content (web pages, PDF/DOCX/PPTX office documents)
into Markdown files. Web pages route through `https://markdown.new/<url>` as
the primary path with a local `httpx` + `markdownify` fallback. Office
documents are downloaded then converted via Microsoft's `markitdown` library
(off-thread, so the calling event loop is not blocked). The capability owns
the strategy dispatcher consumed by the batch orchestrator (`web/jobs.py`)
and the standalone `notebook_batch.py` script.

## Requirements

### Requirement: Source-type dispatch
The system SHALL provide a single high-level entry point that converts any supported NotebookLM source into a Markdown file at a caller-supplied target path, dispatching to the appropriate strategy based on the source's `SourceType`.

#### Scenario: Web page dispatch
- **WHEN** a caller invokes the conversion entry point with a `WEB_PAGE` source URL
- **THEN** the system selects the URL-to-Markdown strategy (remote primary, local fallback) and writes a Markdown file to the target path on success

#### Scenario: PDF / DOCX / PPTX dispatch
- **WHEN** a caller invokes the conversion entry point with a `PDF`, `DOCX`, or `PPTX` source URL
- **THEN** the system selects the file-to-Markdown strategy (download then convert via the file converter) and writes a Markdown file to the target path on success

#### Scenario: Unsupported source type
- **WHEN** a caller invokes the conversion entry point with a source type the conversion module does not handle (e.g. `YOUTUBE`, `GOOGLE_DRIVE_VIDEO`)
- **THEN** the system raises a typed error indicating the source type is unsupported and writes no file

### Requirement: Remote URL-to-Markdown via markdown.new
The system SHALL convert HTML URLs to Markdown by issuing an HTTP GET to `{markdown_new_base}{original_url}` (default base `https://markdown.new/`) and writing the response body to the target file when the response passes a sanity check.

#### Scenario: Successful remote conversion
- **WHEN** the remote endpoint returns HTTP 200 with a non-empty Markdown-shaped body
- **THEN** the system writes the body to the target file and reports `strategy = "remote"` in the result

#### Scenario: Configurable base URL
- **WHEN** the caller (or the `NOTEBOOKLM_MARKDOWN_NEW_BASE` environment variable) overrides the markdown.new base URL
- **THEN** the system uses the override exactly, including any path prefix, when constructing the remote request

#### Scenario: Custom timeout
- **WHEN** the caller (or the `NOTEBOOKLM_CONVERSION_TIMEOUT` environment variable) sets a timeout
- **THEN** the system applies that timeout to the remote HTTP request

### Requirement: Remote failure detection
The system SHALL treat the following remote outcomes as a remote-conversion failure that triggers the local fallback, without retrying the remote endpoint:

- Any HTTP status outside the 2xx range, including 401, 403, 429, and any 5xx.
- An empty body or a body shorter than 32 bytes.
- A body that begins with `<!DOCTYPE html>` or `<html` and contains no Markdown structural marker (`#`, `*`, `- `, `> `, or a fenced code marker) within the first 4 KB.
- Any network error (connection refused, DNS failure, TLS failure, timeout).

#### Scenario: Rate-limited remote endpoint
- **WHEN** the remote endpoint returns HTTP 429
- **THEN** the system does not retry the remote endpoint and immediately invokes the local fallback for the same original URL

#### Scenario: Remote returns an error HTML page
- **WHEN** the remote endpoint returns HTTP 200 but the body is an HTML error page with no Markdown markers
- **THEN** the system invokes the local fallback for the same original URL

#### Scenario: Remote disabled by configuration
- **WHEN** the `NOTEBOOKLM_DISABLE_MARKDOWN_NEW` environment variable is set to `1` (or the caller passes `use_remote=False`)
- **THEN** the system skips the remote attempt entirely and runs only the local fallback

### Requirement: Local URL-to-Markdown fallback
The system SHALL provide a local fallback that fetches the original URL with `httpx`, converts HTML responses to Markdown using a local converter, and writes the result to the target file with a one-line `> Source: <original-url>` header.

#### Scenario: Local fallback after remote failure
- **WHEN** the remote conversion fails and the local fallback runs successfully
- **THEN** the system writes the converted Markdown to the target file and reports `strategy = "fallback"` in the result

#### Scenario: HTML response converted to Markdown
- **WHEN** the local fallback fetches a URL whose response `Content-Type` starts with `text/html`
- **THEN** the system runs the HTML body through the local HTML-to-Markdown converter (script and style tags stripped) before writing the file

#### Scenario: Plain-text or Markdown response
- **WHEN** the local fallback fetches a URL whose response is already plain text or Markdown
- **THEN** the system writes the response body unchanged (after the `> Source:` header), without running the HTML converter

#### Scenario: Browser-like User-Agent
- **WHEN** the local fallback issues its HTTP request
- **THEN** the request includes a browser-like `User-Agent` header (overridable via the caller or `NOTEBOOKLM_CONVERSION_UA` environment variable)

#### Scenario: Both remote and local fail
- **WHEN** the remote conversion fails AND the local fallback also fails (network error, non-2xx status, empty body)
- **THEN** the system raises a `LocalConversionError` whose message identifies both the remote and local failure causes, and writes no file

### Requirement: File-to-Markdown via markitdown
The system SHALL convert binary office documents (PDF, DOCX, PPTX, and any other format supported by `markitdown` that the orchestrator dispatches) to Markdown by downloading the file to a temporary location, invoking the `markitdown` library, and writing `result.text_content` to the target file.

#### Scenario: Successful file conversion
- **WHEN** the file-to-Markdown strategy runs against a downloadable PDF / DOCX / PPTX URL
- **THEN** the system downloads the file, invokes `markitdown`, writes the resulting Markdown to the target file, and reports `strategy = "markitdown"` in the result

#### Scenario: Original binary deleted by default
- **WHEN** the file-to-Markdown strategy completes successfully and the caller did not request original retention
- **THEN** the temporary binary file is deleted after conversion and only the `.md` file remains at the target path

#### Scenario: Original binary kept when requested
- **WHEN** the caller passes `keep_original=True`
- **THEN** the system keeps the original binary as a sibling file (`<target-stem>.<original-ext>`) alongside the `.md` file

#### Scenario: Conversion off-thread
- **WHEN** `markitdown` is invoked
- **THEN** the call runs via `asyncio.to_thread` (or equivalent) so the event loop is not blocked

#### Scenario: Markitdown failure
- **WHEN** `markitdown` raises an exception during conversion
- **THEN** the system raises a `LocalConversionError` carrying the underlying message, deletes the temporary binary, and writes no Markdown file

### Requirement: Optional-dependency handling
The system SHALL import `markitdown` and the local HTML-to-Markdown library lazily inside the strategy functions so that the conversion module remains importable when the optional `[markdown]` extra is not installed.

#### Scenario: Missing markitdown at install time
- **WHEN** the caller invokes the file-to-Markdown strategy without `markitdown` installed
- **THEN** the system raises a `ConversionDependencyError` whose message tells the user to install `notebooklm[markdown]`

#### Scenario: Missing local HTML converter
- **WHEN** the caller invokes the local fallback without the local HTML-to-Markdown library installed
- **THEN** the system raises a `ConversionDependencyError` whose message tells the user to install `notebooklm[markdown]`

#### Scenario: Remote-only path stays available
- **WHEN** neither optional library is installed AND the caller invokes the URL-to-Markdown entry point with `use_remote=True` AND the remote attempt succeeds
- **THEN** the conversion completes successfully without touching the optional libraries

### Requirement: Conversion result and strategy reporting
The system SHALL return a `ConversionResult` from every successful conversion that captures the target path, the strategy used, the bytes written, and the elapsed wall time in milliseconds.

#### Scenario: Strategy enumeration
- **WHEN** any conversion succeeds
- **THEN** the result's `strategy` field is one of: `"remote"`, `"fallback"`, `"markitdown"`, `"fulltext"`, `"passthrough"`

#### Scenario: Bytes and duration reported
- **WHEN** a conversion succeeds
- **THEN** the result's `bytes_written` matches the byte length of the file at the target path and `duration_ms` is greater than zero

### Requirement: Filename and target-path semantics
The system SHALL write the converted Markdown to the exact target path supplied by the caller, creating any missing parent directories, and SHALL NOT mutate the target path's stem or extension.

#### Scenario: Caller controls filename
- **WHEN** the caller passes target path `out/克劳德中文教学课程.md`
- **THEN** the system writes the Markdown to that exact path without altering the stem or extension

#### Scenario: Parent directory created
- **WHEN** the caller's target path's parent directory does not yet exist
- **THEN** the system creates the parent directory (and any missing ancestors) before writing the file

#### Scenario: Atomic write on success
- **WHEN** a conversion succeeds
- **THEN** the target file is fully written and contains the complete converted content; no partial file is left at the target path on failure
