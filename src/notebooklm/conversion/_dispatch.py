"""Source→Markdown high-level dispatcher.

``source_to_markdown(source_url, source_kind, target, *, options)`` is the
entry point used by the batch orchestrator (``web/jobs.py``) and the standalone
``notebook_batch.py`` script. It picks the correct strategy by ``SourceType``:

- ``WEB_PAGE`` → ``url_to_markdown`` (markdown.new + httpx fallback)
- ``PDF`` / ``DOCX`` / ``PPTX`` → ``file_to_markdown`` (download + markitdown)
- Everything else → typed ``ConversionError`` (callers are expected to handle
  unsupported types themselves; the dispatcher has no opinion about
  ``YOUTUBE``, Google Drive sources, or fulltext-backed sources).
"""

from __future__ import annotations

from pathlib import Path

from ..types import SourceType
from ._errors import ConversionError
from ._files import file_to_markdown
from ._types import ConversionOptions, ConversionResult
from ._url import url_to_markdown

# Map binary office source types to the extension we use for both:
# - the tempfile suffix (so markitdown picks the right backend)
# - the kept-original sibling file when ``keep_original=True``
_FILE_SOURCE_EXT: dict[SourceType, str] = {
    SourceType.PDF: ".pdf",
    SourceType.DOCX: ".docx",
    SourceType.PPTX: ".pptx",
}


async def source_to_markdown(
    source_url: str,
    source_kind: SourceType,
    target: Path,
    *,
    options: ConversionOptions | None = None,
) -> ConversionResult:
    """Convert a NotebookLM source to Markdown at ``target``.

    Raises ``ConversionError`` for unsupported source kinds. The caller is
    expected to filter ``YOUTUBE``, ``GOOGLE_DRIVE_*`` and similar before
    invoking this function — keeping the error surface narrow makes
    orchestrator-level decisions (placeholder ``.todo``, fulltext path)
    easier to reason about.
    """
    if source_kind == SourceType.WEB_PAGE:
        return await url_to_markdown(source_url, target, options=options)

    extension = _FILE_SOURCE_EXT.get(source_kind)
    if extension is not None:
        return await file_to_markdown(
            source_url,
            target,
            source_extension=extension,
            options=options,
        )

    raise ConversionError(
        f"source type {source_kind!r} is not supported by source-markdown-conversion"
    )
