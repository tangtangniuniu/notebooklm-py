## ADDED Requirements

### Requirement: Slash-retry on 404/403 for source fetches
The conversion module's URL-fetching paths (the file-to-Markdown download, the markdown.new remote attempt, and the local fallback's HTML fetch) SHALL — on receiving an HTTP `404` or `403` — issue exactly one retry to the same URL with the path component's trailing slash toggled (stripped if present, appended if absent), preserving the query string and fragment. The retry SHALL NOT fire for any other status code, for transport errors, or for a path of `/`.

For the markdown.new remote attempt, the slash-retry applies to the *original* source URL (the one being converted), not to the markdown.new base; the base URL is used verbatim.

A successful slash-retry SHALL be flagged on the returned response so callers (the orchestrator, the strategy reporter) can surface the recovery in user-facing messages.

#### Scenario: file-to-Markdown download recovers via slash-retry
- **WHEN** the file-to-Markdown strategy fetches a PDF URL AND the host returns HTTP 404 AND the slash-toggled URL returns HTTP 200
- **THEN** the system uses the second response's body as the markitdown input and the conversion completes successfully

#### Scenario: markdown.new remote attempt slash-retries the source URL
- **WHEN** the remote URL-to-Markdown attempt issues `{markdown_new_base}https://example.com/foo/` AND the response is an HTTP 404 marker AND a request to `{markdown_new_base}https://example.com/foo` returns a valid Markdown body
- **THEN** the system uses the second response and reports `strategy = "remote"` (with the slash-retry recovery flag set)

#### Scenario: Local fallback slash-retries the original URL
- **WHEN** the local fallback fetches `https://example.com/foo` AND the host returns HTTP 403 AND a request to `https://example.com/foo/` returns HTTP 200 with HTML content
- **THEN** the system runs the second response's HTML through the local HTML-to-Markdown converter and reports `strategy = "fallback"` (with the slash-retry recovery flag set)

#### Scenario: 410 Gone is not retried
- **WHEN** the conversion module fetches a URL AND the host returns HTTP 410 (Gone)
- **THEN** the system raises the appropriate conversion error immediately and does not slash-retry

#### Scenario: 5xx and 429 are not retried by the slash-retry helper
- **WHEN** the conversion module fetches a URL AND the host returns HTTP 500, 502, 503, 504, or 429
- **THEN** the slash-retry helper does not issue a second request; the existing per-strategy failure handling applies (remote-conversion failure triggers the local fallback for the markdown.new path; file-to-Markdown raises `LocalConversionError`)

#### Scenario: Transport error not retried
- **WHEN** the conversion module's HTTP request fails with a network / DNS / TLS / timeout error
- **THEN** the slash-retry helper does not issue a second request and the underlying transport error propagates as before
