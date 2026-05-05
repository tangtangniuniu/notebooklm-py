"""File→Markdown strategy via ``markitdown``.

``file_to_markdown(file_url, target, *, options, source_extension)`` downloads
the source URL to a temporary file, runs ``markitdown`` on it (off-thread, so
the event loop is not blocked), and writes the resulting Markdown to ``target``.

Behavior:
- If ``options.keep_original`` is True, the temp file is moved to a sibling
  path (``target.with_suffix(source_extension)``) and the ``.md`` is written
  alongside it.
- Otherwise the temp file is deleted after a successful conversion.
- On any markitdown / I/O failure, the temp file is removed and no ``.md``
  is left behind. The caller sees a ``LocalConversionError``.

``markitdown`` is imported lazily so a base install (without ``[markdown]``)
can still import this module to discover its public API.
"""

from __future__ import annotations

import asyncio
import logging
import shutil
import tempfile
import time
from pathlib import Path

import httpx

from ._errors import ConversionDependencyError, LocalConversionError
from ._types import ConversionOptions, ConversionResult
from ._url_retry import astream_with_slash_retry, slash_retried

logger = logging.getLogger(__name__)


async def _download_to_path(url: str, target: Path, options: ConversionOptions) -> bool:
    """Stream ``url`` to ``target`` (parent dirs already assumed to exist).

    Returns True if the slash-retry helper kicked in (i.e. the second attempt
    was the one that succeeded), False otherwise.

    Raises ``LocalConversionError`` on any non-2xx or transport error; the
    caller is responsible for cleaning up partial files (the dispatcher's
    ``finally`` block handles that).
    """
    headers = {"User-Agent": options.effective_user_agent}
    try:
        async with (
            httpx.AsyncClient(
                timeout=options.timeout,
                follow_redirects=True,
                headers=headers,
            ) as client,
            astream_with_slash_retry(client, "GET", url) as response,
        ):
            if response.status_code < 200 or response.status_code >= 300:
                raise LocalConversionError(
                    f"file download returned HTTP {response.status_code} for {url}"
                )
            with target.open("wb") as fh:
                async for chunk in response.aiter_bytes():
                    fh.write(chunk)
            return slash_retried(response)
    except httpx.HTTPError as exc:
        raise LocalConversionError(f"file download transport error for {url}: {exc}") from exc


def _convert_with_markitdown(path: Path) -> str:
    """Run markitdown on ``path`` and return ``result.text_content``.

    Raises ``ConversionDependencyError`` when markitdown is missing,
    ``LocalConversionError`` for any conversion failure.
    """
    try:
        from markitdown import MarkItDown
    except ImportError as exc:
        raise ConversionDependencyError(
            "markitdown is required for file-to-Markdown conversion. "
            "Install it via `pip install notebooklm-py[markdown]`."
        ) from exc

    try:
        result = MarkItDown().convert(str(path))
    except Exception as exc:  # noqa: BLE001 — markitdown raises a broad set of types
        raise LocalConversionError(f"markitdown failed for {path.name}: {exc}") from exc

    text = getattr(result, "text_content", None)
    if not text:
        raise LocalConversionError(f"markitdown returned empty content for {path.name}")
    return text


async def file_to_markdown(
    file_url: str,
    target: Path,
    *,
    source_extension: str,
    options: ConversionOptions | None = None,
) -> ConversionResult:
    """Download ``file_url``, convert with markitdown, write Markdown to ``target``.

    ``source_extension`` (e.g. ``.pdf``, ``.docx``, ``.pptx``) is used both as
    the temp file's suffix (so markitdown picks the right backend) and as the
    extension of the kept-original sibling file when
    ``options.keep_original`` is True.
    """
    opts = options or ConversionOptions()
    started = time.monotonic()
    target.parent.mkdir(parents=True, exist_ok=True)

    # We need a unique on-disk path to stream the download into, then pass
    # to markitdown. ``NamedTemporaryFile`` gives us that path; we close the
    # handle immediately so the file isn't double-opened, and rely on the
    # ``finally`` block below to remove it.
    with tempfile.NamedTemporaryFile(
        prefix="notebooklm-conv-",
        suffix=source_extension,
        delete=False,
    ) as _tmp:
        tmp_path = Path(_tmp.name)

    try:
        retried = await _download_to_path(file_url, tmp_path, opts)
        text = await asyncio.to_thread(_convert_with_markitdown, tmp_path)

        # Atomic write to target, mirroring `_atomic_write` in _url.py.
        encoded = text.encode("utf-8")
        md_tmp = target.with_suffix(target.suffix + ".tmp")
        try:
            md_tmp.write_bytes(encoded)
            md_tmp.replace(target)
        except Exception:
            md_tmp.unlink(missing_ok=True)
            raise

        if opts.keep_original:
            sibling = target.with_suffix(source_extension)
            shutil.copyfile(tmp_path, sibling)

        bytes_written = len(encoded)
        duration_ms = max(int((time.monotonic() - started) * 1000), 1)
        return ConversionResult(
            target=target,
            strategy="markitdown",
            bytes_written=bytes_written,
            duration_ms=duration_ms,
            slash_retried=retried,
        )
    except Exception:
        # Don't leave a half-written .md on failure.
        target.unlink(missing_ok=True)
        raise
    finally:
        tmp_path.unlink(missing_ok=True)
