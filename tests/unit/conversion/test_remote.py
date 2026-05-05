"""Tests for ``notebooklm.conversion._remote``."""

from __future__ import annotations

import asyncio

import httpx
import pytest

from notebooklm.conversion import ConversionOptions, RemoteConversionError
from notebooklm.conversion._remote import (
    HTML_SNIFF_BYTES,
    MIN_BODY_BYTES,
    _looks_like_html_error,
    _looks_like_markdown,
    fetch_remote_markdown,
)

# pytest-httpx provides the ``httpx_mock`` fixture used throughout this file.


# --------------------------------------------------------- sanity-check helpers


def test_looks_like_markdown_accepts_each_marker():
    """Every documented marker should pass the sanity check on its own."""
    for sample in (
        "# heading",
        "* bullet",
        "- bullet item",
        "> quote",
        "```\ncode\n```",
    ):
        assert _looks_like_markdown(sample), f"marker {sample!r} should be markdown"


def test_looks_like_html_error_distinguishes_errors_from_real_pages():
    assert _looks_like_html_error("<!DOCTYPE html><html><body>Oops, 404 not found</body></html>")
    # Real HTML page that happens to start with <html but contains markdown markers
    # in the body — we treat it as Markdown-y enough to keep.
    rendered = "<html><body><h1># Real heading</h1>\n* bullet\n</body></html>"
    assert not _looks_like_html_error(rendered)
    # Clean Markdown — not HTML at all.
    assert not _looks_like_html_error("# Title\n\nBody")


# ------------------------------------------------------------ end-to-end fetch


@pytest.fixture
def options() -> ConversionOptions:
    return ConversionOptions()


@pytest.fixture(autouse=True)
def _no_retry_backoff(monkeypatch):
    """Skip the 1–2s backoff used by the throttle-retry path so tests stay fast."""

    async def _instant(_seconds):
        return None

    monkeypatch.setattr("notebooklm.conversion._remote.asyncio.sleep", _instant)


@pytest.mark.asyncio
async def test_fetch_remote_markdown_success(httpx_mock, options):
    body = "# Hello\n\nReal markdown content with enough length to pass the threshold."
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com/docs",
        text=body,
        status_code=200,
    )

    result, retried = await fetch_remote_markdown("https://example.com/docs", options)
    assert result == body
    assert retried is False


@pytest.mark.asyncio
async def test_fetch_remote_markdown_html_error_page_triggers_failure(httpx_mock, options):
    # Long enough to clear MIN_BODY_BYTES but is just an HTML error page.
    error_html = (
        "<!DOCTYPE html><html><head><title>Error</title></head>"
        "<body><h1>Whoops</h1><p>Something went wrong, please try later.</p></body></html>"
    )
    assert len(error_html) >= MIN_BODY_BYTES
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com/blocked",
        text=error_html,
        status_code=200,
    )

    with pytest.raises(RemoteConversionError, match="HTML error page"):
        await fetch_remote_markdown("https://example.com/blocked", options)


@pytest.mark.asyncio
@pytest.mark.parametrize("status", [401, 403, 429, 500, 502, 503])
async def test_fetch_remote_markdown_non_2xx_triggers_failure(httpx_mock, options, status):
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com",
        text="anything at all that is long enough to pass the size check",
        status_code=status,
    )
    if status == 403:
        # Slash-retry will issue a second request on 403; both attempts fail.
        httpx_mock.add_response(
            url="https://markdown.new/https://example.com/",
            text="anything at all that is long enough to pass the size check",
            status_code=status,
        )
    if status in (429, 502, 503):
        # Throttle-retry path issues a second request after a brief backoff
        # for the transient statuses. Both attempts fail.
        httpx_mock.add_response(
            url="https://markdown.new/https://example.com",
            text="anything at all that is long enough to pass the size check",
            status_code=status,
        )
    with pytest.raises(RemoteConversionError, match=f"HTTP {status}"):
        await fetch_remote_markdown("https://example.com", options)


@pytest.mark.asyncio
async def test_fetch_remote_markdown_short_body_triggers_failure(httpx_mock, options):
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com",
        text="too short",
        status_code=200,
    )
    with pytest.raises(RemoteConversionError, match="empty/short"):
        await fetch_remote_markdown("https://example.com", options)


@pytest.mark.asyncio
async def test_fetch_remote_markdown_network_error_wrapped(httpx_mock, options):
    httpx_mock.add_exception(httpx.ConnectError("refused"))
    with pytest.raises(RemoteConversionError, match="transport error"):
        await fetch_remote_markdown("https://example.com", options)


@pytest.mark.asyncio
async def test_fetch_remote_markdown_custom_base_used_verbatim(httpx_mock):
    options = ConversionOptions(markdown_new_base="https://my-mirror.example/")
    body = "# Mirror response\n\nLong enough body to pass the sanity threshold easily."
    httpx_mock.add_response(
        url="https://my-mirror.example/https://example.com/page",
        text=body,
        status_code=200,
    )
    result, retried = await fetch_remote_markdown("https://example.com/page", options)
    assert result == body
    assert retried is False


@pytest.mark.asyncio
async def test_fetch_remote_markdown_base_without_trailing_slash(httpx_mock):
    """A base without ``/`` should still produce a single-slash URL."""
    options = ConversionOptions(markdown_new_base="https://my-mirror.example")
    body = "# Mirror response\n\nLong enough body to pass the sanity threshold easily."
    httpx_mock.add_response(
        url="https://my-mirror.example/https://example.com/page",
        text=body,
        status_code=200,
    )
    result, retried = await fetch_remote_markdown("https://example.com/page", options)
    assert result == body
    assert retried is False


def test_html_sniff_bytes_is_4kb():
    """Pin the constant so a future refactor can't silently shrink it."""
    assert HTML_SNIFF_BYTES == 4 * 1024


# --------------------------------------------------------------- slash-retry


@pytest.mark.asyncio
async def test_fetch_remote_markdown_slash_retry_recovers_from_404(httpx_mock, options):
    """404 on `/https://example.com/foo/` → strip slash → 200 on `/https://example.com/foo`."""
    body = "# Hello\n\nLong enough body to pass the sanity threshold easily here."
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com/foo/",
        status_code=404,
    )
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com/foo",
        text=body,
        status_code=200,
    )
    text, retried = await fetch_remote_markdown("https://example.com/foo/", options)
    assert text == body
    assert retried is True


@pytest.mark.asyncio
async def test_fetch_remote_markdown_slash_retry_recovers_from_403(httpx_mock, options):
    body = "# Hello\n\nLong enough body to pass the sanity threshold easily here."
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com/foo",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com/foo/",
        text=body,
        status_code=200,
    )
    text, retried = await fetch_remote_markdown("https://example.com/foo", options)
    assert text == body
    assert retried is True


# ----------------------------------------------------- throttle retry on 429/5xx


@pytest.mark.asyncio
async def test_fetch_remote_markdown_429_retries_once_and_succeeds(httpx_mock, options):
    """A transient 429 should clear after one backoff retry."""
    body = "# Recovered\n\nAfter the brief throttling pause this works again, fine."
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com/load",
        status_code=429,
        text="rate limited - try later " * 10,
    )
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com/load",
        text=body,
        status_code=200,
    )
    text, _retried = await fetch_remote_markdown("https://example.com/load", options)
    assert text == body


@pytest.mark.asyncio
async def test_fetch_remote_markdown_502_retries_once_and_succeeds(httpx_mock, options):
    """A transient 502 from the upstream should also be retried once."""
    body = "# OK\n\nUpstream came back to life after a brief blip; fine for tests."
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com/blip",
        status_code=502,
        text="bad gateway " * 10,
    )
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com/blip",
        text=body,
        status_code=200,
    )
    text, _retried = await fetch_remote_markdown("https://example.com/blip", options)
    assert text == body


@pytest.mark.asyncio
async def test_fetch_remote_markdown_403_does_not_throttle_retry(httpx_mock, options):
    """403 is intentionally NOT in the throttle-retry set.

    Slash-retry already gives 403 a second chance; doubling up would just
    delay the inevitable browser-fallback. After slash-retry consumes its
    one second response, no further request should be issued.
    """
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com/blocked",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com/blocked/",
        status_code=403,
    )
    with pytest.raises(RemoteConversionError, match="HTTP 403"):
        await fetch_remote_markdown("https://example.com/blocked", options)
    # Exactly two requests: the original + the slash-retry. No throttle retry.
    assert len(httpx_mock.get_requests()) == 2


# -------------------------------------------------- body-size cap on remote


@pytest.mark.asyncio
async def test_fetch_remote_markdown_oversized_body_rejected(httpx_mock):
    """A response exceeding ``max_body_bytes`` should fail fast.

    Mirrors the same cap on the local fallback — a multi-MB markdown.new
    response would still pin a worker on the validation walk and the
    eventual write.
    """
    options = ConversionOptions(max_body_bytes=256)
    big_body = "# " + ("x" * 4096)
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com/huge",
        text=big_body,
        status_code=200,
    )
    with pytest.raises(RemoteConversionError, match="cap 256"):
        await fetch_remote_markdown("https://example.com/huge", options)


# ----------------------------------------------------------- global throttle


@pytest.mark.asyncio
async def test_remote_concurrency_is_capped(httpx_mock, options, monkeypatch):
    """The process-global semaphore should serialize concurrent requests.

    We force the semaphore to 1 via env, fire multiple coroutines, and
    assert that only one request is ever in flight at a time.
    """
    monkeypatch.setenv("NOTEBOOKLM_MARKDOWN_NEW_CONCURRENCY", "1")
    # Reset the lazy semaphore so the new env value takes effect.
    import notebooklm.conversion._remote as _r

    monkeypatch.setattr(_r, "_remote_sem", None)

    in_flight = 0
    peak = 0
    lock = asyncio.Lock()

    async def _track_request(request):  # noqa: ARG001 — pytest-httpx callback
        nonlocal in_flight, peak
        async with lock:
            in_flight += 1
            peak = max(peak, in_flight)
        await asyncio.sleep(0.05)
        async with lock:
            in_flight -= 1
        return httpx.Response(
            status_code=200,
            text="# Title\n\nBody long enough to pass the threshold sanity check easily.",
        )

    httpx_mock.add_callback(_track_request, url="https://markdown.new/https://example.com/a")
    httpx_mock.add_callback(_track_request, url="https://markdown.new/https://example.com/b")
    httpx_mock.add_callback(_track_request, url="https://markdown.new/https://example.com/c")

    await asyncio.gather(
        fetch_remote_markdown("https://example.com/a", options),
        fetch_remote_markdown("https://example.com/b", options),
        fetch_remote_markdown("https://example.com/c", options),
    )
    assert peak == 1, f"expected serialization with cap=1; saw peak={peak}"
