"""Tests for ``notebooklm.conversion._dispatch`` (high-level source dispatch)."""

from __future__ import annotations

from pathlib import Path

import pytest

from notebooklm.conversion import (
    ConversionError,
    source_to_markdown,
)
from notebooklm.types import SourceType

FIXTURES = Path(__file__).resolve().parents[2] / "fixtures" / "conversion"


# ------------------------------------------------------------- happy-path dispatch


@pytest.mark.asyncio
async def test_dispatch_web_page_uses_url_strategy(httpx_mock, tmp_path):
    body = "# Web page article\n\nReal content with adequate length to pass the body check."
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com/article",
        text=body,
        status_code=200,
    )
    target = tmp_path / "article.md"
    result = await source_to_markdown(
        "https://example.com/article",
        SourceType.WEB_PAGE,
        target,
    )
    assert result.strategy == "remote"
    assert target.read_text(encoding="utf-8") == body


@pytest.mark.asyncio
async def test_dispatch_pdf_uses_file_strategy(httpx_mock, tmp_path):
    httpx_mock.add_response(
        url="https://example.com/source.pdf",
        content=(FIXTURES / "sample.pdf").read_bytes(),
        headers={"content-type": "application/pdf"},
        status_code=200,
    )
    target = tmp_path / "doc.md"
    result = await source_to_markdown(
        "https://example.com/source.pdf",
        SourceType.PDF,
        target,
    )
    assert result.strategy == "markitdown"
    assert target.exists()


@pytest.mark.asyncio
async def test_dispatch_docx_uses_file_strategy(httpx_mock, tmp_path):
    httpx_mock.add_response(
        url="https://example.com/source.docx",
        content=(FIXTURES / "sample.docx").read_bytes(),
        headers={
            "content-type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        },
        status_code=200,
    )
    target = tmp_path / "doc.md"
    result = await source_to_markdown(
        "https://example.com/source.docx",
        SourceType.DOCX,
        target,
    )
    assert result.strategy == "markitdown"
    assert "Hello DOCX" in target.read_text(encoding="utf-8")


@pytest.mark.asyncio
async def test_dispatch_pptx_uses_file_strategy(httpx_mock, tmp_path):
    httpx_mock.add_response(
        url="https://example.com/deck.pptx",
        content=(FIXTURES / "sample.pptx").read_bytes(),
        headers={
            "content-type": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        },
        status_code=200,
    )
    target = tmp_path / "deck.md"
    result = await source_to_markdown(
        "https://example.com/deck.pptx",
        SourceType.PPTX,
        target,
    )
    assert result.strategy == "markitdown"
    assert "Hello PPTX" in target.read_text(encoding="utf-8")


# ----------------------------------------------------------- unsupported types


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "kind",
    [
        SourceType.YOUTUBE,
        SourceType.GOOGLE_DRIVE_VIDEO,
        SourceType.GOOGLE_DOCS,
        SourceType.MARKDOWN,  # handled by orchestrator's fulltext path, not by the dispatcher
        SourceType.PASTED_TEXT,
        SourceType.CSV,  # CSV stays as .csv per design open-question resolution
        SourceType.UNKNOWN,
    ],
)
async def test_dispatch_unsupported_kinds_raise(kind, tmp_path):
    target = tmp_path / "out.md"
    with pytest.raises(ConversionError, match="not supported"):
        await source_to_markdown("https://example.com", kind, target)
    assert not target.exists()
