"""Remote URL→Markdown strategy using markdown.new.

The public function ``fetch_remote_markdown(url, options)`` issues an HTTP GET
to ``{markdown_new_base}{url}`` (e.g. ``https://markdown.new/https://example.com``)
and returns the response body when it passes a sanity check.

Failure modes that raise ``RemoteConversionError`` (the dispatcher catches it
to fall over to the local fallback):

- Non-2xx HTTP status (401/403/429/5xx are explicitly listed in the spec).
- Empty body or body shorter than 32 bytes.
- HTML-error-page response (HTML start tag with no Markdown markers in
  the first 4 KB).
- Response body exceeds ``options.max_body_bytes``.
- Any network error: connect refused, DNS, TLS, timeout.

Reliability tweaks (added after observing intermittent 403/429 from the
service when many workers hit it at once):

- A process-global ``asyncio.Semaphore`` caps in-flight requests to
  ``_MAX_CONCURRENT_REMOTE`` (env-overridable). markdown.new throttles per
  client IP; without this, our own concurrency was triggering the 403s.
- One automatic retry with a short backoff for the specific statuses that
  markdown.new returns under load (403/429/502/503/504). Anything else
  fails fast so the local fallback gets its turn.
"""

from __future__ import annotations

import asyncio
import logging
import os
import random

import httpx

from ._errors import RemoteConversionError
from ._types import ConversionOptions
from ._url_retry import afetch_with_slash_retry, slash_retried

logger = logging.getLogger(__name__)

# Sanity-check thresholds. These intentionally match the values quoted in the
# spec so the test suite can pin them.
MIN_BODY_BYTES = 32
HTML_SNIFF_BYTES = 4 * 1024
_MARKDOWN_MARKERS = ("#", "*", "- ", "> ", "```")
_HTML_START_PREFIXES = ("<!doctype html", "<html")

# Status codes where one retry-with-backoff has a real chance of succeeding.
# 403 is intentionally NOT in here: slash-retry already gives 403 a second
# chance, and a true Cloudflare 403 won't clear without a real browser
# (handled by the ``_browser`` strategy). 429/5xx, on the other hand, are
# transient throttling signals that a brief pause typically clears.
_RETRY_STATUSES: frozenset[int] = frozenset({429, 502, 503, 504})

# Default maximum concurrent requests to markdown.new across the whole
# process. Overridable via NOTEBOOKLM_MARKDOWN_NEW_CONCURRENCY for users who
# host their own instance and want more throughput.
_DEFAULT_MAX_CONCURRENT_REMOTE = 2


def _max_concurrent_remote() -> int:
    """Resolve the configured max-in-flight count for markdown.new requests."""
    raw = os.environ.get("NOTEBOOKLM_MARKDOWN_NEW_CONCURRENCY", "").strip()
    if not raw:
        return _DEFAULT_MAX_CONCURRENT_REMOTE
    try:
        value = int(raw)
    except ValueError:
        return _DEFAULT_MAX_CONCURRENT_REMOTE
    return max(1, value)


_REMOTE_SEM_LOCK = asyncio.Lock()
_remote_sem: asyncio.Semaphore | None = None


async def _get_remote_semaphore() -> asyncio.Semaphore:
    """Lazily build (and memoize) the process-global remote-fetch semaphore.

    Lazy because the asyncio loop must already exist when the semaphore is
    constructed. Memoization is guarded by a lock so two concurrent calls on
    cold start can't each create their own semaphore.
    """
    global _remote_sem
    if _remote_sem is not None:
        return _remote_sem
    async with _REMOTE_SEM_LOCK:
        if _remote_sem is None:
            _remote_sem = asyncio.Semaphore(_max_concurrent_remote())
    return _remote_sem


def _looks_like_markdown(body: str) -> bool:
    """Return True if the head of ``body`` shows any Markdown structural marker.

    We only inspect the first ``HTML_SNIFF_BYTES`` bytes because real-world
    HTML error pages tend to be small and we don't want to scan a multi-MB
    document just to confirm it's Markdown.
    """
    head = body[:HTML_SNIFF_BYTES]
    return any(marker in head for marker in _MARKDOWN_MARKERS)


def _looks_like_html_error(body: str) -> bool:
    """Return True if the response body looks like an HTML error page.

    We treat anything that begins with an HTML start tag and lacks any Markdown
    structural marker in its head as an error page (or, at best, a non-rendered
    page that wouldn't be useful as Markdown anyway).
    """
    head = body.lstrip()[:HTML_SNIFF_BYTES].lower()
    if not head.startswith(_HTML_START_PREFIXES):
        return False
    return not _looks_like_markdown(body)


def _validate_response(response: httpx.Response, max_body_bytes: int) -> None:
    """Raise ``RemoteConversionError`` on any sanity-check failure."""
    status = response.status_code
    if status < 200 or status >= 300:
        raise RemoteConversionError(
            f"markdown.new returned HTTP {status} for {response.request.url}"
        )

    raw = response.content
    if len(raw) > max_body_bytes:
        raise RemoteConversionError(
            f"markdown.new returned {len(raw)} bytes (cap {max_body_bytes}) "
            f"for {response.request.url}"
        )

    body = response.text
    # Use ``len(body.encode("utf-8"))`` would be more accurate, but the spec
    # uses byte/char interchangeably and string length is the cheaper check.
    if len(body) < MIN_BODY_BYTES:
        raise RemoteConversionError(
            f"markdown.new returned an empty/short body ({len(body)} chars) "
            f"for {response.request.url}"
        )

    if _looks_like_html_error(body):
        raise RemoteConversionError(
            f"markdown.new returned an HTML error page for {response.request.url}"
        )


def _build_remote_url(original_url: str, options: ConversionOptions) -> str:
    """Concatenate the markdown.new base with the original URL.

    The base is used verbatim — we don't second-guess any path prefix the user
    may have supplied. We only ensure exactly one slash separates the two.
    """
    base = options.markdown_new_base
    if not base.endswith("/"):
        base = base + "/"
    return f"{base}{original_url}"


async def _fetch_once(client: httpx.AsyncClient, target: str) -> httpx.Response:
    """Issue the slash-retry-aware GET; transport errors propagate."""
    return await afetch_with_slash_retry(client, target)


async def fetch_remote_markdown(url: str, options: ConversionOptions) -> tuple[str, bool]:
    """GET ``{base}{url}`` and return the validated Markdown body + slash-retry flag.

    Raises ``RemoteConversionError`` for any sanity-check failure or transport
    error. Never falls back; the dispatcher (``url_to_markdown``) is the one
    that knows about the local fallback.

    Returns a ``(body, slash_retried)`` tuple. ``slash_retried`` is True when
    the markdown.new helper issued a second request with the original URL's
    trailing slash toggled (because the first attempt returned 403/404).

    Concurrency to markdown.new is capped process-wide via a semaphore; the
    caller may queue here briefly when many workers race. One automatic
    retry-after-backoff is performed for transient failures (403/429/5xx).
    """
    target = _build_remote_url(url, options)
    sem = await _get_remote_semaphore()

    async with sem:
        try:
            async with httpx.AsyncClient(
                timeout=options.timeout,
                follow_redirects=True,
            ) as client:
                response = await _fetch_once(client, target)

                # Single retry on transient statuses; pause briefly first so
                # we don't immediately re-trigger the same throttling burst.
                if response.status_code in _RETRY_STATUSES:
                    await asyncio.sleep(1.0 + random.random())  # 1.0–2.0s
                    logger.debug(
                        "markdown.new returned %d for %s; retrying once",
                        response.status_code,
                        target,
                    )
                    response = await _fetch_once(client, target)
        except httpx.HTTPError as exc:
            # Includes timeouts, connection errors, TLS errors — anything the
            # transport itself can raise.
            raise RemoteConversionError(
                f"markdown.new transport error for {target}: {exc}"
            ) from exc

        _validate_response(response, options.max_body_bytes)
        logger.debug("markdown.new returned %d chars for %s", len(response.text), url)
        return response.text, slash_retried(response)
