"""Slash-toggle retry helper for source-fetch HTTP calls.

A surprisingly common failure mode for source-download requests is that the
host returns ``404`` or ``403`` for a URL whose canonical form differs by a
trailing slash. The fix is cheap and deterministic: try once, and if that
specific failure shows up, toggle the trailing slash on the path and try
again.

This module exposes three small wrappers — one for non-streaming async, one
for streaming async (as an ``@asynccontextmanager``), and one sync flavor —
that callers reach for in place of ``client.get`` / ``client.stream`` /
``client.get`` (sync). They never retry on transport errors, never retry
more than once, and never retry status codes other than 404/403.

When a retry actually happens, the returned response carries
``response.extensions["slash_retried"] = True`` so callers can append a
``(slash-retry)`` suffix to user-facing progress messages.
"""

from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any
from urllib.parse import urlsplit, urlunsplit

import httpx

# Statuses where slash normalization is a plausible cause. Anything else
# (5xx, 429, 410, transport errors) is left for the caller's existing
# error path.
_SLASH_RETRY_STATUSES: frozenset[int] = frozenset({403, 404})


def _toggle_trailing_slash(url: str) -> str | None:
    """Return the URL with the path's trailing slash toggled, or ``None``.

    ``None`` means "no meaningful alternate" — currently this happens only
    for the root path ``/``, where stripping would leave the empty path
    and appending would be a no-op against the original.

    The query string and fragment are preserved verbatim. Only the path
    component is touched.
    """
    parts = urlsplit(url)
    path = parts.path
    if path == "" or path == "/":
        return None
    new_path = path[:-1] if path.endswith("/") else path + "/"
    return urlunsplit(parts._replace(path=new_path))


def _mark_retried(response: httpx.Response, retried: bool) -> None:
    """Record the slash-retry outcome on the response's extensions dict."""
    response.extensions["slash_retried"] = retried


def slash_retried(response: httpx.Response) -> bool:
    """Return True if this response came from a slash-retry second attempt."""
    return bool(response.extensions.get("slash_retried", False))


async def afetch_with_slash_retry(
    client: httpx.AsyncClient,
    url: str,
    *,
    method: str = "GET",
    **kwargs: Any,
) -> httpx.Response:
    """Async non-streaming request with one slash-retry on 403/404.

    Behaves like ``client.request(method, url, **kwargs)`` for any non
    403/404 outcome. On 403/404 with a meaningful alternate URL, retries
    once with the slash toggled and returns the second response. On
    transport errors (any subclass of ``httpx.HTTPError``) the exception
    propagates from the first attempt; we do not retry transport failures.
    """
    response = await client.request(method, url, **kwargs)
    if response.status_code in _SLASH_RETRY_STATUSES:
        alt = _toggle_trailing_slash(url)
        if alt is not None:
            response2 = await client.request(method, alt, **kwargs)
            _mark_retried(response2, True)
            return response2
    _mark_retried(response, False)
    return response


@asynccontextmanager
async def astream_with_slash_retry(
    client: httpx.AsyncClient,
    method: str,
    url: str,
    **kwargs: Any,
) -> AsyncIterator[httpx.Response]:
    """Async streaming request with one slash-retry on 403/404.

    Mirrors ``client.stream(method, url, **kwargs)`` semantics. The first
    attempt is opened, and if its status code is 403/404 we close it
    cleanly and open a second stream with the slash-toggled URL. The
    yielded response carries ``slash_retried`` on its extensions dict.
    """
    cm = client.stream(method, url, **kwargs)
    response = await cm.__aenter__()
    if response.status_code in _SLASH_RETRY_STATUSES:
        alt = _toggle_trailing_slash(url)
        if alt is not None:
            # Close the first stream cleanly before opening another.
            await cm.__aexit__(None, None, None)
            async with client.stream(method, alt, **kwargs) as response2:
                _mark_retried(response2, True)
                yield response2
            return
    try:
        _mark_retried(response, False)
        yield response
    finally:
        await cm.__aexit__(None, None, None)


def fetch_with_slash_retry(
    client: httpx.Client,
    url: str,
    *,
    method: str = "GET",
    **kwargs: Any,
) -> httpx.Response:
    """Sync non-streaming request with one slash-retry on 403/404.

    Used by ``notebook_batch.py`` (which is sync). Same retry rules as the
    async helper.
    """
    response = client.request(method, url, **kwargs)
    if response.status_code in _SLASH_RETRY_STATUSES:
        alt = _toggle_trailing_slash(url)
        if alt is not None:
            response2 = client.request(method, alt, **kwargs)
            _mark_retried(response2, True)
            return response2
    _mark_retried(response, False)
    return response
