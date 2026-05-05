"""Tests for ``notebooklm.conversion._url_retry``."""

from __future__ import annotations

import httpx
import pytest

from notebooklm.conversion._url_retry import (
    _toggle_trailing_slash,
    afetch_with_slash_retry,
    astream_with_slash_retry,
    fetch_with_slash_retry,
    slash_retried,
)

# ----------------------------------------------------------------- toggle


def test_toggle_strips_trailing_slash():
    assert _toggle_trailing_slash("https://x.example/foo/") == "https://x.example/foo"


def test_toggle_appends_trailing_slash():
    assert _toggle_trailing_slash("https://x.example/foo") == "https://x.example/foo/"


def test_toggle_preserves_query_and_fragment():
    assert (
        _toggle_trailing_slash("https://x.example/foo?id=42#section")
        == "https://x.example/foo/?id=42#section"
    )
    assert (
        _toggle_trailing_slash("https://x.example/foo/?id=42#section")
        == "https://x.example/foo?id=42#section"
    )


def test_toggle_root_returns_none():
    """Root path / has no meaningful alternate."""
    assert _toggle_trailing_slash("https://x.example/") is None


def test_toggle_empty_path_returns_none():
    assert _toggle_trailing_slash("https://x.example") is None


# --------------------------------------------------- async non-streaming


@pytest.mark.asyncio
async def test_afetch_no_retry_on_200(httpx_mock):
    httpx_mock.add_response(url="https://x.example/foo", status_code=200, text="ok")
    async with httpx.AsyncClient() as client:
        response = await afetch_with_slash_retry(client, "https://x.example/foo")
    assert response.status_code == 200
    assert slash_retried(response) is False


@pytest.mark.asyncio
async def test_afetch_retries_on_404(httpx_mock):
    """404 on first → strip slash → 200 on second."""
    httpx_mock.add_response(url="https://x.example/foo/", status_code=404)
    httpx_mock.add_response(url="https://x.example/foo", status_code=200, text="ok")
    async with httpx.AsyncClient() as client:
        response = await afetch_with_slash_retry(client, "https://x.example/foo/")
    assert response.status_code == 200
    assert slash_retried(response) is True


@pytest.mark.asyncio
async def test_afetch_retries_on_403(httpx_mock):
    """403 on first → append slash → 200 on second."""
    httpx_mock.add_response(url="https://x.example/foo", status_code=403)
    httpx_mock.add_response(url="https://x.example/foo/", status_code=200, text="ok")
    async with httpx.AsyncClient() as client:
        response = await afetch_with_slash_retry(client, "https://x.example/foo")
    assert response.status_code == 200
    assert slash_retried(response) is True


@pytest.mark.asyncio
async def test_afetch_returns_second_response_when_both_fail(httpx_mock):
    """When both attempts fail, the second response is returned with the flag set."""
    httpx_mock.add_response(url="https://x.example/foo", status_code=404)
    httpx_mock.add_response(url="https://x.example/foo/", status_code=404)
    async with httpx.AsyncClient() as client:
        response = await afetch_with_slash_retry(client, "https://x.example/foo")
    assert response.status_code == 404
    assert slash_retried(response) is True


@pytest.mark.asyncio
async def test_afetch_no_retry_on_500(httpx_mock):
    httpx_mock.add_response(url="https://x.example/foo", status_code=500)
    async with httpx.AsyncClient() as client:
        response = await afetch_with_slash_retry(client, "https://x.example/foo")
    assert response.status_code == 500
    assert slash_retried(response) is False


@pytest.mark.asyncio
async def test_afetch_no_retry_on_429(httpx_mock):
    httpx_mock.add_response(url="https://x.example/foo", status_code=429)
    async with httpx.AsyncClient() as client:
        response = await afetch_with_slash_retry(client, "https://x.example/foo")
    assert response.status_code == 429
    assert slash_retried(response) is False


@pytest.mark.asyncio
async def test_afetch_no_retry_on_410(httpx_mock):
    httpx_mock.add_response(url="https://x.example/foo", status_code=410)
    async with httpx.AsyncClient() as client:
        response = await afetch_with_slash_retry(client, "https://x.example/foo")
    assert response.status_code == 410
    assert slash_retried(response) is False


@pytest.mark.asyncio
async def test_afetch_root_url_no_retry(httpx_mock):
    """Root path can't be slash-toggled; first response returned as-is."""
    httpx_mock.add_response(url="https://x.example/", status_code=404)
    async with httpx.AsyncClient() as client:
        response = await afetch_with_slash_retry(client, "https://x.example/")
    assert response.status_code == 404
    assert slash_retried(response) is False


@pytest.mark.asyncio
async def test_afetch_transport_error_propagates(httpx_mock):
    """Transport errors raise from the first attempt; no retry."""
    httpx_mock.add_exception(httpx.ConnectError("boom"))
    async with httpx.AsyncClient() as client:
        with pytest.raises(httpx.ConnectError):
            await afetch_with_slash_retry(client, "https://x.example/foo")


# --------------------------------------------------------- async streaming


@pytest.mark.asyncio
async def test_astream_no_retry_on_200(httpx_mock):
    httpx_mock.add_response(url="https://x.example/foo", status_code=200, content=b"data")
    async with (
        httpx.AsyncClient() as client,
        astream_with_slash_retry(client, "GET", "https://x.example/foo") as response,
    ):
        assert response.status_code == 200
        assert slash_retried(response) is False
        body = b""
        async for chunk in response.aiter_bytes():
            body += chunk
    assert body == b"data"


@pytest.mark.asyncio
async def test_astream_retries_on_404(httpx_mock):
    httpx_mock.add_response(url="https://x.example/foo/", status_code=404)
    httpx_mock.add_response(url="https://x.example/foo", status_code=200, content=b"ok")
    async with (
        httpx.AsyncClient() as client,
        astream_with_slash_retry(client, "GET", "https://x.example/foo/") as response,
    ):
        assert response.status_code == 200
        assert slash_retried(response) is True


@pytest.mark.asyncio
async def test_astream_retries_on_403(httpx_mock):
    httpx_mock.add_response(url="https://x.example/foo", status_code=403)
    httpx_mock.add_response(url="https://x.example/foo/", status_code=200, content=b"ok")
    async with (
        httpx.AsyncClient() as client,
        astream_with_slash_retry(client, "GET", "https://x.example/foo") as response,
    ):
        assert response.status_code == 200
        assert slash_retried(response) is True


@pytest.mark.asyncio
async def test_astream_no_retry_on_500(httpx_mock):
    httpx_mock.add_response(url="https://x.example/foo", status_code=500)
    async with (
        httpx.AsyncClient() as client,
        astream_with_slash_retry(client, "GET", "https://x.example/foo") as response,
    ):
        assert response.status_code == 500
        assert slash_retried(response) is False


@pytest.mark.asyncio
async def test_astream_root_url_no_retry(httpx_mock):
    httpx_mock.add_response(url="https://x.example/", status_code=404)
    async with (
        httpx.AsyncClient() as client,
        astream_with_slash_retry(client, "GET", "https://x.example/") as response,
    ):
        assert response.status_code == 404
        assert slash_retried(response) is False


# ------------------------------------------------------------ sync flavor


def test_fetch_sync_no_retry_on_200(httpx_mock):
    httpx_mock.add_response(url="https://x.example/foo", status_code=200, text="ok")
    with httpx.Client() as client:
        response = fetch_with_slash_retry(client, "https://x.example/foo")
    assert response.status_code == 200
    assert slash_retried(response) is False


def test_fetch_sync_retries_on_404(httpx_mock):
    httpx_mock.add_response(url="https://x.example/foo/", status_code=404)
    httpx_mock.add_response(url="https://x.example/foo", status_code=200, text="ok")
    with httpx.Client() as client:
        response = fetch_with_slash_retry(client, "https://x.example/foo/")
    assert response.status_code == 200
    assert slash_retried(response) is True


def test_fetch_sync_retries_on_403(httpx_mock):
    httpx_mock.add_response(url="https://x.example/foo", status_code=403)
    httpx_mock.add_response(url="https://x.example/foo/", status_code=200, text="ok")
    with httpx.Client() as client:
        response = fetch_with_slash_retry(client, "https://x.example/foo")
    assert response.status_code == 200
    assert slash_retried(response) is True


def test_fetch_sync_no_retry_on_500(httpx_mock):
    httpx_mock.add_response(url="https://x.example/foo", status_code=500)
    with httpx.Client() as client:
        response = fetch_with_slash_retry(client, "https://x.example/foo")
    assert response.status_code == 500
    assert slash_retried(response) is False
