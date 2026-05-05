## MODIFIED Requirements

### Requirement: Bounded concurrency
The system SHALL execute job items with a configurable maximum concurrency (default 5, accepted range 1..10) and SHALL NOT exceed that limit across all categories within a single job. The system SHALL reject job-creation requests whose concurrency falls outside `1..10` with HTTP 400.

#### Scenario: Default concurrency
- **WHEN** a job has 12 items and concurrency is at default
- **THEN** at most 5 items are in `running` state at any moment

#### Scenario: User-configured concurrency at the upper bound
- **WHEN** the UI passes `concurrency: 10`
- **THEN** at most 10 items are in `running` state at any moment

#### Scenario: User-configured concurrency at the lower bound
- **WHEN** the UI passes `concurrency: 1`
- **THEN** items run strictly sequentially

#### Scenario: Out-of-range concurrency rejected
- **WHEN** the UI submits a batch with `concurrency: 0` or `concurrency: 11` (or any other value outside `1..10`)
- **THEN** the system returns HTTP 400 with an error message indicating the accepted range and creates no job

## ADDED Requirements

### Requirement: Slash-retry recovery on 404/403
For any source-fetching HTTP request the orchestrator issues (image streaming, CSV direct download, file-to-Markdown download, web-page-to-Markdown remote and fallback fetches), the system SHALL — on receiving an HTTP `404` or `403` — issue exactly one retry to the same URL with the path component's trailing slash toggled (stripped if present, appended if absent), preserving the query string and fragment.

The system SHALL NOT slash-retry on any other status code, on transport errors (network, TLS, timeout), on the root path `/` (where there is no slash to toggle meaningfully), or for more than one retry per item.

When the slash-retry attempt returns a 2xx response, the orchestrator SHALL surface the recovery to consumers by appending ` (slash-retry)` to the item's progress/strategy message.

#### Scenario: 404 recovers via stripped slash
- **WHEN** the orchestrator fetches `https://example.com/foo/` for a source download AND the host returns HTTP 404 AND a request to `https://example.com/foo` returns HTTP 200
- **THEN** the orchestrator uses the second response's body as the item's content and the item's progress message is suffixed with ` (slash-retry)`

#### Scenario: 403 recovers via appended slash
- **WHEN** the orchestrator fetches `https://example.com/bar` AND the host returns HTTP 403 AND a request to `https://example.com/bar/` returns HTTP 200
- **THEN** the orchestrator uses the second response's body as the item's content and the item's progress message is suffixed with ` (slash-retry)`

#### Scenario: Both attempts fail with 404
- **WHEN** both `https://example.com/foo` and `https://example.com/foo/` return HTTP 404
- **THEN** the item terminates with status `error` and a message that includes the HTTP status; no further retry is attempted

#### Scenario: 500 status is not retried
- **WHEN** the orchestrator fetches a source URL AND the host returns HTTP 500 (or 502 / 503 / 504 / 429)
- **THEN** the item terminates with status `error` immediately and the slash-toggled URL is not requested

#### Scenario: Transport error is not retried
- **WHEN** the orchestrator fetches a source URL AND the request fails with a transport error (connection refused, DNS failure, TLS error, or timeout)
- **THEN** the item terminates with status `error` immediately and the slash-toggled URL is not requested

#### Scenario: Query string and fragment preserved
- **WHEN** the orchestrator slash-retries a URL like `https://example.com/foo?id=42#section`
- **THEN** the retry URL is `https://example.com/foo/?id=42#section` (path-only toggle; query and fragment unchanged)

#### Scenario: Root URL skipped
- **WHEN** the orchestrator's first attempt fails on a URL whose path is exactly `/`
- **THEN** no slash-retry attempt is made and the item terminates with the original error
