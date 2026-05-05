"""Tests for ``notebooklm.conversion._url`` (the URL→Markdown dispatcher)."""

from __future__ import annotations

from pathlib import Path

import httpx
import pytest

from notebooklm.conversion import (
    ConversionOptions,
    ConversionResult,
    LocalConversionError,
    url_to_markdown,
)

# -------------------------------------------------------------------- helpers


_SAMPLE_BODY = "# Hello\n\nA respectable amount of markdown content for the threshold check."


@pytest.fixture(autouse=True)
def _disable_browser_fallback_and_backoff(monkeypatch):
    """Keep dispatcher tests deterministic: skip Playwright + retry sleeps."""
    monkeypatch.setenv("NOTEBOOKLM_DISABLE_BROWSER_FALLBACK", "1")

    async def _instant(_seconds):
        return None

    monkeypatch.setattr("notebooklm.conversion._remote.asyncio.sleep", _instant)


@pytest.fixture
def target(tmp_path: Path) -> Path:
    return tmp_path / "out" / "page.md"


# ------------------------------------------------------------ remote success


@pytest.mark.asyncio
async def test_remote_success_writes_md_and_reports_strategy(httpx_mock, target):
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com",
        text=_SAMPLE_BODY,
        status_code=200,
    )
    result = await url_to_markdown("https://example.com", target)

    assert isinstance(result, ConversionResult)
    assert result.target == target
    assert result.strategy == "remote"
    assert result.bytes_written == len(_SAMPLE_BODY.encode("utf-8"))
    assert result.duration_ms > 0
    assert target.read_text(encoding="utf-8") == _SAMPLE_BODY


@pytest.mark.asyncio
async def test_remote_success_creates_parent_dirs(httpx_mock, tmp_path):
    deep = tmp_path / "a" / "b" / "c" / "page.md"
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com",
        text=_SAMPLE_BODY,
        status_code=200,
    )
    await url_to_markdown("https://example.com", deep)
    assert deep.exists()


# --------------------------------------------------- remote-fail-then-fallback


@pytest.mark.asyncio
async def test_remote_429_falls_back_to_local(httpx_mock, target):
    # Remote: rate-limited (first attempt + the throttle-retry attempt both fail).
    for _ in range(2):
        httpx_mock.add_response(
            url="https://markdown.new/https://example.com/blog",
            status_code=429,
            text="Rate limited - try again later " * 5,
        )
    # Fallback: original URL serves a real page.
    httpx_mock.add_response(
        url="https://example.com/blog",
        text="<html><body><h1>Real article</h1><p>Body</p></body></html>",
        headers={"content-type": "text/html"},
        status_code=200,
    )

    result = await url_to_markdown("https://example.com/blog", target)
    assert result.strategy == "fallback"
    text = target.read_text(encoding="utf-8")
    assert text.startswith("> Source: https://example.com/blog")
    assert "# Real article" in text


# ---------------------------------------------------------------- both fail


@pytest.mark.asyncio
async def test_both_remote_and_local_fail_raises_local_with_both_causes(httpx_mock, target):
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com/blocked",
        status_code=403,
        text="Access denied" * 10,
    )
    # Slash-retry on the remote path also fails.
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com/blocked/",
        status_code=403,
        text="Access denied" * 10,
    )
    httpx_mock.add_response(
        url="https://example.com/blocked",
        status_code=503,
        text="Service unavailable" * 10,
    )
    with pytest.raises(LocalConversionError) as exc_info:
        await url_to_markdown("https://example.com/blocked", target)
    msg = str(exc_info.value)
    assert "remote=" in msg
    assert "local=" in msg
    assert not target.exists()


# ------------------------------------------------------------ use_remote=False


@pytest.mark.asyncio
async def test_use_remote_false_skips_markdown_new(httpx_mock, target):
    """When ``use_remote=False`` is passed, only the local fallback runs."""
    httpx_mock.add_response(
        url="https://example.com",
        text="Long enough plain-text content for the body-size threshold check.",
        headers={"content-type": "text/plain"},
        status_code=200,
    )
    options = ConversionOptions(use_remote=False)
    result = await url_to_markdown("https://example.com", target, options=options)
    assert result.strategy == "fallback"

    # No request should have been made to markdown.new at all.
    requests = httpx_mock.get_requests()
    assert all("markdown.new" not in str(r.url) for r in requests)


@pytest.mark.asyncio
async def test_env_disable_remote(httpx_mock, target, monkeypatch):
    """``NOTEBOOKLM_DISABLE_MARKDOWN_NEW=1`` skips markdown.new even when ``use_remote=True``."""
    monkeypatch.setenv("NOTEBOOKLM_DISABLE_MARKDOWN_NEW", "1")
    httpx_mock.add_response(
        url="https://example.com",
        text="Long enough plain-text content for the body-size threshold check.",
        headers={"content-type": "text/plain"},
        status_code=200,
    )
    # use_remote defaults to True; the env override should still kick in.
    result = await url_to_markdown("https://example.com", target)
    assert result.strategy == "fallback"

    requests = httpx_mock.get_requests()
    assert all("markdown.new" not in str(r.url) for r in requests)


# ------------------------------------------------------------ atomic write


@pytest.mark.asyncio
async def test_failure_does_not_leave_partial_file(httpx_mock, target):
    """If every attempt fails, the target file SHOULD NOT exist."""
    # 502 is a retryable status — register both attempts so neither lands.
    for _ in range(2):
        httpx_mock.add_response(
            url="https://markdown.new/https://example.com",
            status_code=502,
            text="Internal server error" * 10,
        )
    httpx_mock.add_exception(httpx.ConnectError("dns fail"))

    with pytest.raises(LocalConversionError):
        await url_to_markdown("https://example.com", target)
    assert not target.exists()
