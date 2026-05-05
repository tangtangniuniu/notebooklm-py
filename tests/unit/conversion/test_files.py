"""Tests for ``notebooklm.conversion._files`` (file→Markdown via markitdown)."""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path

import pytest

from notebooklm.conversion import (
    ConversionDependencyError,
    ConversionOptions,
    LocalConversionError,
    file_to_markdown,
)

FIXTURES = Path(__file__).resolve().parents[2] / "fixtures" / "conversion"


def _fixture_response_args(fixture_name: str, content_type: str) -> dict:
    """Helper to build pytest-httpx response kwargs for a binary fixture."""
    data = (FIXTURES / fixture_name).read_bytes()
    return {
        "content": data,
        "headers": {"content-type": content_type},
        "status_code": 200,
    }


# --------------------------------------------------------------- success path


@pytest.mark.asyncio
async def test_pdf_file_to_markdown_success(httpx_mock, tmp_path):
    httpx_mock.add_response(
        url="https://example.com/source.pdf",
        **_fixture_response_args("sample.pdf", "application/pdf"),
    )
    target = tmp_path / "out" / "doc.md"
    result = await file_to_markdown(
        "https://example.com/source.pdf",
        target,
        source_extension=".pdf",
    )
    assert result.strategy == "markitdown"
    assert result.target == target
    assert target.exists()
    assert result.bytes_written == target.stat().st_size
    assert result.duration_ms > 0
    # Original binary should NOT be kept by default.
    assert not target.with_suffix(".pdf").exists()


@pytest.mark.asyncio
async def test_docx_file_to_markdown_success(httpx_mock, tmp_path):
    httpx_mock.add_response(
        url="https://example.com/source.docx",
        **_fixture_response_args(
            "sample.docx",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ),
    )
    target = tmp_path / "doc.md"
    result = await file_to_markdown(
        "https://example.com/source.docx",
        target,
        source_extension=".docx",
    )
    assert result.strategy == "markitdown"
    text = target.read_text(encoding="utf-8")
    # The DOCX fixture contains "Hello DOCX" — markitdown should surface it.
    assert "Hello DOCX" in text


@pytest.mark.asyncio
async def test_pptx_file_to_markdown_success(httpx_mock, tmp_path):
    httpx_mock.add_response(
        url="https://example.com/deck.pptx",
        **_fixture_response_args(
            "sample.pptx",
            "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        ),
    )
    target = tmp_path / "deck.md"
    result = await file_to_markdown(
        "https://example.com/deck.pptx",
        target,
        source_extension=".pptx",
    )
    assert result.strategy == "markitdown"
    text = target.read_text(encoding="utf-8")
    assert "Hello PPTX" in text


# ------------------------------------------------------- keep_original=True


@pytest.mark.asyncio
async def test_keep_original_keeps_binary_sibling(httpx_mock, tmp_path):
    httpx_mock.add_response(
        url="https://example.com/source.docx",
        **_fixture_response_args(
            "sample.docx",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ),
    )
    target = tmp_path / "doc.md"
    options = ConversionOptions(keep_original=True)
    await file_to_markdown(
        "https://example.com/source.docx",
        target,
        source_extension=".docx",
        options=options,
    )
    # Both files exist side-by-side.
    assert target.exists()
    sibling = target.with_suffix(".docx")
    assert sibling.exists()
    # Sibling must be the original bytes (or at least non-zero size).
    assert sibling.stat().st_size == (FIXTURES / "sample.docx").stat().st_size


# -------------------------------------------------------- parent-dir creation


@pytest.mark.asyncio
async def test_parent_dirs_created(httpx_mock, tmp_path):
    httpx_mock.add_response(
        url="https://example.com/source.pdf",
        **_fixture_response_args("sample.pdf", "application/pdf"),
    )
    target = tmp_path / "deeply" / "nested" / "out" / "doc.md"
    await file_to_markdown(
        "https://example.com/source.pdf",
        target,
        source_extension=".pdf",
    )
    assert target.exists()


# ----------------------------------------------------- missing dependency


@pytest.mark.asyncio
async def test_missing_markitdown_raises_dependency_error(httpx_mock, tmp_path, monkeypatch):
    # Simulate ``markitdown`` being uninstalled by injecting None into sys.modules.
    monkeypatch.setitem(sys.modules, "markitdown", None)
    httpx_mock.add_response(
        url="https://example.com/source.pdf",
        **_fixture_response_args("sample.pdf", "application/pdf"),
    )
    target = tmp_path / "doc.md"
    with pytest.raises(ConversionDependencyError, match="markitdown"):
        await file_to_markdown(
            "https://example.com/source.pdf",
            target,
            source_extension=".pdf",
        )
    # No partial Markdown file should exist.
    assert not target.exists()


# -------------------------------------------------------- markitdown raising


@pytest.mark.asyncio
async def test_markitdown_failure_wraps_as_local_error(httpx_mock, tmp_path, monkeypatch):
    """Force markitdown to raise; confirm ``LocalConversionError`` and clean state."""
    httpx_mock.add_response(
        url="https://example.com/source.pdf",
        **_fixture_response_args("sample.pdf", "application/pdf"),
    )

    class _Boom:
        def convert(self, _path: str) -> object:
            raise RuntimeError("simulated markitdown failure")

    import markitdown as _markitdown

    monkeypatch.setattr(_markitdown, "MarkItDown", _Boom)

    target = tmp_path / "doc.md"
    with pytest.raises(LocalConversionError, match="markitdown failed"):
        await file_to_markdown(
            "https://example.com/source.pdf",
            target,
            source_extension=".pdf",
        )
    assert not target.exists()


# ------------------------------------------------------- HTTP download errors


@pytest.mark.asyncio
async def test_download_404_wrapped_as_local_error(httpx_mock, tmp_path):
    httpx_mock.add_response(
        url="https://example.com/missing.pdf",
        status_code=404,
        content=b"not found",
        headers={"content-type": "text/plain"},
    )
    # Slash-retry attempts the toggled URL as well; it also 404s here.
    httpx_mock.add_response(
        url="https://example.com/missing.pdf/",
        status_code=404,
        content=b"not found",
        headers={"content-type": "text/plain"},
    )
    target = tmp_path / "doc.md"
    with pytest.raises(LocalConversionError, match="HTTP 404"):
        await file_to_markdown(
            "https://example.com/missing.pdf",
            target,
            source_extension=".pdf",
        )
    assert not target.exists()


# ------------------------------------------------------------- off-thread


@pytest.mark.asyncio
async def test_event_loop_not_blocked_during_conversion(httpx_mock, tmp_path, monkeypatch):
    """Confirm markitdown is invoked off-thread.

    We swap in a markitdown mock that blocks the calling thread with
    ``time.sleep`` for a small interval. If ``file_to_markdown`` is using
    ``asyncio.to_thread`` correctly, an ``asyncio.sleep`` running concurrently
    should still make progress and finish.
    """
    import time

    httpx_mock.add_response(
        url="https://example.com/source.pdf",
        **_fixture_response_args("sample.pdf", "application/pdf"),
    )

    BLOCK_SECONDS = 0.2

    class _BlockingMarkItDown:
        def convert(self, _path: str) -> object:
            time.sleep(BLOCK_SECONDS)

            class _Result:
                text_content = "# off-thread sentinel"

            return _Result()

    import markitdown as _markitdown

    monkeypatch.setattr(_markitdown, "MarkItDown", _BlockingMarkItDown)

    async def _async_progress() -> int:
        ticks = 0
        # Sleep less than BLOCK_SECONDS in total so we finish before
        # markitdown returns. If the loop is blocked, we'd see ticks == 0.
        for _ in range(5):
            await asyncio.sleep(BLOCK_SECONDS / 50)
            ticks += 1
        return ticks

    target = tmp_path / "doc.md"
    progress_task = asyncio.create_task(_async_progress())
    result = await file_to_markdown(
        "https://example.com/source.pdf",
        target,
        source_extension=".pdf",
    )
    ticks = await progress_task

    assert result.strategy == "markitdown"
    # The async progress must have completed all five ticks while markitdown
    # was busy in its worker thread.
    assert ticks == 5


# --------------------------------------------------------------- slash-retry


@pytest.mark.asyncio
async def test_file_download_slash_retry_recovers_from_404(httpx_mock, tmp_path):
    """A 404 on the original URL triggers a slash-retry; the second try wins.

    The success path is then reported on the ConversionResult's ``slash_retried``
    flag so the orchestrator can append ``(slash-retry)`` to the progress message.
    """
    httpx_mock.add_response(
        url="https://example.com/source.pdf/",
        status_code=404,
    )
    httpx_mock.add_response(
        url="https://example.com/source.pdf",
        **_fixture_response_args("sample.pdf", "application/pdf"),
    )
    target = tmp_path / "doc.md"
    result = await file_to_markdown(
        "https://example.com/source.pdf/",
        target,
        source_extension=".pdf",
    )
    assert result.strategy == "markitdown"
    assert result.slash_retried is True
    assert target.exists()


@pytest.mark.asyncio
async def test_file_download_no_slash_retry_flag_on_happy_path(httpx_mock, tmp_path):
    httpx_mock.add_response(
        url="https://example.com/source.pdf",
        **_fixture_response_args("sample.pdf", "application/pdf"),
    )
    target = tmp_path / "doc.md"
    result = await file_to_markdown(
        "https://example.com/source.pdf",
        target,
        source_extension=".pdf",
    )
    assert result.strategy == "markitdown"
    assert result.slash_retried is False
