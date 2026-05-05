"""Tests for ``notebooklm.conversion._fallback``."""

from __future__ import annotations

import asyncio
import sys

import httpx
import pytest

from notebooklm.conversion import (
    DEFAULT_USER_AGENT,
    ConversionDependencyError,
    ConversionOptions,
    LocalConversionError,
)
from notebooklm.conversion._fallback import fetch_local_markdown

# ---------------------------------------------------------- HTML→Markdown path


@pytest.mark.asyncio
async def test_html_response_converted_to_markdown(httpx_mock):
    httpx_mock.add_response(
        url="https://example.com/article",
        text="<html><body><h1>Title</h1><p>Body text</p></body></html>",
        headers={"content-type": "text/html; charset=utf-8"},
        status_code=200,
    )
    md, _retried = await fetch_local_markdown("https://example.com/article", ConversionOptions())
    assert md.startswith("> Source: https://example.com/article\n\n")
    # markdownify should produce ATX-style headings.
    assert "# Title" in md
    assert "Body text" in md


@pytest.mark.asyncio
async def test_script_and_style_stripped(httpx_mock):
    httpx_mock.add_response(
        url="https://example.com/page",
        text=(
            "<html><body>"
            "<script>alert('x')</script>"
            "<style>body{color:red}</style>"
            "<h1>Hello</h1>"
            "</body></html>"
        ),
        headers={"content-type": "text/html"},
        status_code=200,
    )
    md, _retried = await fetch_local_markdown("https://example.com/page", ConversionOptions())
    assert "alert" not in md
    assert "color:red" not in md
    assert "# Hello" in md


# ---------------------------------------------------------- non-HTML passthrough


@pytest.mark.asyncio
async def test_plain_text_passthrough(httpx_mock):
    body = "Already markdown content with **bold** and a code block.\n\n```py\nprint(1)\n```\n"
    httpx_mock.add_response(
        url="https://example.com/raw.md",
        text=body,
        headers={"content-type": "text/markdown"},
        status_code=200,
    )
    md, _retried = await fetch_local_markdown("https://example.com/raw.md", ConversionOptions())
    assert md == f"> Source: https://example.com/raw.md\n\n{body}"


# ----------------------------------------------------------------- error paths


@pytest.mark.asyncio
async def test_non_2xx_raises_local_conversion_error(httpx_mock):
    httpx_mock.add_response(
        url="https://example.com",
        status_code=404,
        text="lots of text to clear the size threshold easily",
    )
    with pytest.raises(LocalConversionError, match="HTTP 404"):
        await fetch_local_markdown("https://example.com", ConversionOptions())


@pytest.mark.asyncio
async def test_short_body_raises(httpx_mock):
    httpx_mock.add_response(
        url="https://example.com",
        status_code=200,
        text="tiny",
    )
    with pytest.raises(LocalConversionError, match="empty/short"):
        await fetch_local_markdown("https://example.com", ConversionOptions())


@pytest.mark.asyncio
async def test_network_error_wrapped(httpx_mock):
    httpx_mock.add_exception(httpx.ConnectTimeout("timeout"))
    with pytest.raises(LocalConversionError, match="transport error"):
        await fetch_local_markdown("https://example.com", ConversionOptions())


# ---------------------------------------------------------- User-Agent header


@pytest.mark.asyncio
async def test_default_user_agent_sent(httpx_mock):
    httpx_mock.add_response(
        url="https://example.com",
        text="Long enough content to pass the body-size threshold trivially.",
        headers={"content-type": "text/plain"},
        status_code=200,
    )
    await fetch_local_markdown("https://example.com", ConversionOptions())
    request = httpx_mock.get_request()
    assert request.headers["user-agent"] == DEFAULT_USER_AGENT


@pytest.mark.asyncio
async def test_user_agent_override_via_options(httpx_mock):
    httpx_mock.add_response(
        url="https://example.com",
        text="Long enough content to pass the body-size threshold trivially.",
        headers={"content-type": "text/plain"},
        status_code=200,
    )
    await fetch_local_markdown(
        "https://example.com",
        ConversionOptions(user_agent="my-custom-ua/1.0"),
    )
    request = httpx_mock.get_request()
    assert request.headers["user-agent"] == "my-custom-ua/1.0"


@pytest.mark.asyncio
async def test_user_agent_override_via_env(httpx_mock, monkeypatch):
    monkeypatch.setenv("NOTEBOOKLM_CONVERSION_UA", "env-ua/2.0")
    httpx_mock.add_response(
        url="https://example.com",
        text="Long enough content to pass the body-size threshold trivially.",
        headers={"content-type": "text/plain"},
        status_code=200,
    )
    # ConversionOptions.from_env() picks up the env var; pass the resulting opts.
    options = ConversionOptions.from_env()
    await fetch_local_markdown("https://example.com", options)
    request = httpx_mock.get_request()
    assert request.headers["user-agent"] == "env-ua/2.0"


# ----------------------------------------------- missing optional dependency


@pytest.mark.asyncio
async def test_missing_markdownify_raises_dependency_error(httpx_mock, monkeypatch):
    """Simulate ``markdownify`` not being installed and assert a clear error."""
    monkeypatch.setitem(sys.modules, "markdownify", None)
    httpx_mock.add_response(
        url="https://example.com/page",
        text="<html><body><h1>Hi</h1></body></html>",
        headers={"content-type": "text/html"},
        status_code=200,
    )
    with pytest.raises(ConversionDependencyError, match="markdownify"):
        await fetch_local_markdown("https://example.com/page", ConversionOptions())


@pytest.mark.asyncio
async def test_missing_markdownify_does_not_block_plain_text(httpx_mock, monkeypatch):
    """Plain-text passthrough doesn't need markdownify."""
    monkeypatch.setitem(sys.modules, "markdownify", None)
    httpx_mock.add_response(
        url="https://example.com",
        text="Plain text body. Long enough to pass the size threshold check trivially.",
        headers={"content-type": "text/plain"},
        status_code=200,
    )
    md, _retried = await fetch_local_markdown("https://example.com", ConversionOptions())
    assert "> Source: https://example.com" in md


# --------------------------------------------------------------- slash-retry


@pytest.mark.asyncio
async def test_local_fallback_slash_retry_recovers_from_404(httpx_mock):
    httpx_mock.add_response(
        url="https://example.com/page/",
        status_code=404,
    )
    httpx_mock.add_response(
        url="https://example.com/page",
        text="<html><body><h1>Recovered</h1></body></html>",
        headers={"content-type": "text/html"},
        status_code=200,
    )
    md, retried = await fetch_local_markdown("https://example.com/page/", ConversionOptions())
    assert "Recovered" in md
    assert retried is True


@pytest.mark.asyncio
async def test_local_fallback_slash_retry_recovers_from_403(httpx_mock):
    httpx_mock.add_response(
        url="https://example.com/article",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://example.com/article/",
        text="<html><body><h1>Readable now</h1></body></html>",
        headers={"content-type": "text/html"},
        status_code=200,
    )
    md, retried = await fetch_local_markdown("https://example.com/article", ConversionOptions())
    assert "Readable now" in md
    assert retried is True


# --------------------------------------------------- browser-style header set


@pytest.mark.asyncio
async def test_browser_style_headers_sent(httpx_mock):
    """The local fallback should send a Chrome-like header set, not just UA.

    Lightweight UA-sniff anti-bot defenses (the most common kind) let through
    requests once Accept / Accept-Language / Sec-Fetch-* look real.
    """
    httpx_mock.add_response(
        url="https://example.com",
        text="Long enough plain text body to easily pass the size threshold check.",
        headers={"content-type": "text/plain"},
        status_code=200,
    )
    await fetch_local_markdown("https://example.com", ConversionOptions())
    request = httpx_mock.get_request()
    # All of these are part of the standard Chrome navigation request.
    assert "text/html" in request.headers["accept"]
    assert request.headers["accept-language"].startswith("en-US")
    assert request.headers["sec-fetch-mode"] == "navigate"
    assert request.headers["sec-fetch-dest"] == "document"
    assert request.headers["upgrade-insecure-requests"] == "1"


# ----------------------------------------------------------- body-size cap


@pytest.mark.asyncio
async def test_body_size_cap_rejects_oversized_response(httpx_mock):
    """A body larger than ``options.max_body_bytes`` should fail fast.

    Without this, markdownify on a multi-MB document would peg the event
    loop and starve every other concurrent worker — exactly the bug we
    saw on real bulk downloads.
    """
    huge_html = "<html><body>" + ("x" * 1024) + "</body></html>"
    httpx_mock.add_response(
        url="https://example.com",
        text=huge_html,
        headers={"content-type": "text/html"},
        status_code=200,
    )
    options = ConversionOptions(max_body_bytes=512)  # smaller than `huge_html`
    with pytest.raises(LocalConversionError, match="exceeded"):
        await fetch_local_markdown("https://example.com", options)


# --------------------------------------------- markdownify offloaded to thread


@pytest.mark.asyncio
async def test_markdownify_runs_off_event_loop(httpx_mock, monkeypatch):
    """The CPU-heavy ``markdownify`` call should run via ``asyncio.to_thread``.

    We patch ``asyncio.to_thread`` to record the call; if the implementation
    regresses to a synchronous in-loop invocation, the patch is bypassed
    and the assertion at the end fails.
    """
    seen: list[str] = []

    real_to_thread = asyncio.to_thread

    async def _record(fn, *args, **kwargs):
        seen.append(fn.__name__)
        return await real_to_thread(fn, *args, **kwargs)

    import asyncio as _asyncio_mod  # local alias for monkeypatch.setattr

    monkeypatch.setattr(_asyncio_mod, "to_thread", _record)

    httpx_mock.add_response(
        url="https://example.com",
        text="<html><body><h1>Hi</h1></body></html>",
        headers={"content-type": "text/html"},
        status_code=200,
    )
    await fetch_local_markdown("https://example.com", ConversionOptions())
    assert any(name.endswith("_convert_html_to_markdown_sync") for name in seen)
