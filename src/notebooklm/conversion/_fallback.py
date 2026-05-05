"""Local fallback URL→Markdown strategy.

When the markdown.new attempt fails (non-2xx, empty, HTML error page, network
error), the dispatcher invokes ``fetch_local_markdown`` to fetch the original
URL directly with ``httpx`` and convert any HTML response to Markdown via
``markdownify``. The returned text always begins with a one-line
``> Source: <url>`` header so downstream readers (and humans) know where the
content originated.

``markdownify`` is imported lazily so the conversion package stays importable
without the optional ``[markdown]`` extra installed; if a caller hits an HTML
response without the dependency, ``ConversionDependencyError`` is raised.

Both the HTTP fetch and the HTML→Markdown conversion enforce a body-size cap
(``ConversionOptions.max_body_bytes``) so a single multi-MB response can't
peg the event loop and starve other workers. The CPU-heavy markdownify call
is run via ``asyncio.to_thread`` for the same reason.
"""

from __future__ import annotations

import asyncio
import logging
import re

import httpx

from ._errors import ConversionDependencyError, LocalConversionError
from ._types import ConversionOptions
from ._url_retry import afetch_with_slash_retry, slash_retried

logger = logging.getLogger(__name__)

# Same threshold as the remote sanity check — a body shorter than this is
# almost certainly an error message rather than useful content.
_MIN_BODY_BYTES = 32

_HTML_CONTENT_TYPES = ("text/html", "application/xhtml+xml")

# Pre-strip <script> and <style> blocks (incl. their inner text) before
# handing HTML to markdownify, which only strips the tags themselves.
_SCRIPT_STYLE_RE = re.compile(
    r"<(script|style)\b[^>]*>.*?</\1\s*>",
    re.IGNORECASE | re.DOTALL,
)


def _browser_headers(user_agent: str) -> dict[str, str]:
    """Browser-style header set used by the local fallback.

    Lightweight bot-protection (basic UA sniffing, missing Accept etc.) lets
    requests through once these headers look like a real Chrome navigation.
    Cloudflare's JS-challenge tier is unaffected — that needs a real browser
    (handled by the optional ``_browser`` strategy).
    """
    return {
        "User-Agent": user_agent,
        "Accept": (
            "text/html,application/xhtml+xml,application/xml;q=0.9,"
            "image/avif,image/webp,image/apng,*/*;q=0.8"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
    }


def _is_html_response(response: httpx.Response) -> bool:
    """Decide whether to run the response body through markdownify."""
    content_type = response.headers.get("content-type", "").lower()
    return any(content_type.startswith(prefix) for prefix in _HTML_CONTENT_TYPES)


def _convert_html_to_markdown_sync(html: str) -> str:
    """Sync core of the HTML→Markdown conversion (CPU-heavy).

    Kept synchronous so callers can hand it to ``asyncio.to_thread``; never
    invoke this directly from an async path — use ``_convert_html_to_markdown``.
    Raises ``ConversionDependencyError`` when ``markdownify`` is missing.
    """
    try:
        from markdownify import markdownify as _markdownify
    except ImportError as exc:
        raise ConversionDependencyError(
            "markdownify is required for the HTML→Markdown fallback. "
            "Install it via `pip install notebooklm-py[markdown]`."
        ) from exc

    cleaned = _SCRIPT_STYLE_RE.sub("", html)
    return _markdownify(cleaned, heading_style="ATX", strip=["script", "style"])


async def _convert_html_to_markdown(html: str) -> str:
    """Run the CPU-heavy HTML→Markdown conversion in a worker thread.

    markdownify on a multi-MB document can take seconds of pure-Python CPU.
    Doing it inline blocks the event loop and starves every other concurrent
    download worker; ``to_thread`` releases the loop while it runs.
    """
    return await asyncio.to_thread(_convert_html_to_markdown_sync, html)


async def fetch_local_markdown(url: str, options: ConversionOptions) -> tuple[str, bool]:
    """Fetch ``url`` directly and return Markdown + slash-retry flag.

    Returns a ``(text, slash_retried)`` tuple where ``text`` is the Markdown
    body (header + content) and ``slash_retried`` is True when the helper
    issued a second request with the URL's trailing slash toggled.

    Raises ``LocalConversionError`` for any non-2xx response, empty body,
    transport error, or response body exceeding ``options.max_body_bytes``.
    """
    headers = _browser_headers(options.effective_user_agent)
    try:
        async with httpx.AsyncClient(
            timeout=options.timeout,
            follow_redirects=True,
            headers=headers,
        ) as client:
            response = await afetch_with_slash_retry(client, url)
    except httpx.HTTPError as exc:
        raise LocalConversionError(f"local fallback transport error for {url}: {exc}") from exc

    status = response.status_code
    if status < 200 or status >= 300:
        raise LocalConversionError(f"local fallback returned HTTP {status} for {url}")

    raw_bytes = response.content
    if len(raw_bytes) > options.max_body_bytes:
        raise LocalConversionError(
            f"local fallback body exceeded {options.max_body_bytes} bytes "
            f"({len(raw_bytes)} bytes) for {url}; refusing to run markdownify"
        )

    body = response.text
    if len(body) < _MIN_BODY_BYTES:
        raise LocalConversionError(
            f"local fallback returned an empty/short body ({len(body)} chars) for {url}"
        )

    # If HTML, convert via markdownify on a worker thread. Otherwise, treat
    # the body as already Markdown / plain text and pass through untouched.
    markdown = await _convert_html_to_markdown(body) if _is_html_response(response) else body

    return f"> Source: {url}\n\n{markdown}", slash_retried(response)
