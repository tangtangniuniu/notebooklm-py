"""In-process batch download orchestrator for the web UI.

A `BatchJob` represents one user-submitted batch (e.g. download all sources
plus all audio plus all notes for notebook X). The orchestrator:

- Expands the user's category selection into concrete `JobItem` entries by
  consulting the `NotebookLMClient`.
- Runs items concurrently up to a configurable limit (default 3).
- Skips items whose target file already exists, unless ``force`` is set.
- Captures per-item errors so one failure doesn't abort the whole job.
- Streams every state transition into a per-job ``asyncio.Queue`` for SSE.
- Supports cancellation: queued items become ``cancelled``, in-flight items
  finish naturally.

State is in-memory; jobs are tied to the server lifetime by design (D6 in the
design doc).
"""

from __future__ import annotations

import asyncio
import logging
import shutil
import subprocess
from collections.abc import Awaitable, Callable, Iterable
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx

from .._filename import sanitize_filename
from ..client import NotebookLMClient
from ..conversion import (
    ConversionError,
    ConversionOptions,
    ConversionResult,
    source_to_markdown,
)
from ..conversion._images import (
    IMAGE_STRATEGY,
    _pick_image_extension,
    known_image_extensions,
)
from ..conversion._url_retry import (
    astream_with_slash_retry,
    fetch_with_slash_retry,
    slash_retried,
)
from ..types import ArtifactType, SourceType

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------- categories

CATEGORIES = (
    "sources",
    "audio",
    "video",
    "slide-deck",
    "infographic",
    "report",
    "mind-map",
    "data-table",
    "quiz",
    "flashcards",
    "notes",
)

# Map artifact category names to ArtifactType enum values.
_ARTIFACT_KIND_MAP: dict[str, ArtifactType] = {
    "audio": ArtifactType.AUDIO,
    "video": ArtifactType.VIDEO,
    "slide-deck": ArtifactType.SLIDE_DECK,
    "infographic": ArtifactType.INFOGRAPHIC,
    "report": ArtifactType.REPORT,
    "mind-map": ArtifactType.MIND_MAP,
    "data-table": ArtifactType.DATA_TABLE,
    "quiz": ArtifactType.QUIZ,
    "flashcards": ArtifactType.FLASHCARDS,
}

# Source kinds that route to ``source_to_markdown`` (file→Markdown via markitdown).
# CSV stays on the direct-download path because losing the CSV format would
# break spreadsheet imports downstream (see design doc, open-question #3).
_FILE_SOURCE_KINDS: tuple[SourceType, ...] = (
    SourceType.PDF,
    SourceType.DOCX,
    SourceType.PPTX,
)

# Source kinds that still get a direct binary download (no Markdown conversion).
_DIRECT_DOWNLOAD_KINDS: tuple[SourceType, ...] = (SourceType.CSV, SourceType.IMAGE)

# Direct-download extensions for ``_DIRECT_DOWNLOAD_KINDS``.
# IMAGE is intentionally absent — its extension is picked at runtime by
# ``_pick_image_extension`` from the response Content-Type / URL path.
_SOURCE_EXT_MAP: dict[SourceType, str] = {
    SourceType.CSV: ".csv",
}

# Artifact-kind to file extension for downloaded files.
_ARTIFACT_EXT_MAP: dict[ArtifactType, str] = {
    ArtifactType.AUDIO: ".mp4",
    ArtifactType.VIDEO: ".mp4",
    ArtifactType.SLIDE_DECK: ".pdf",
    ArtifactType.INFOGRAPHIC: ".png",
    ArtifactType.REPORT: ".md",
    ArtifactType.MIND_MAP: ".json",
    ArtifactType.DATA_TABLE: ".csv",
    ArtifactType.QUIZ: ".json",
    ArtifactType.FLASHCARDS: ".json",
}


# ----------------------------------------------------------------- data types


@dataclass
class JobItem:
    """One concrete download to perform.

    The ``runner`` is awaited to do the actual work. It MAY return a string,
    which the orchestrator will use as the item's progress message (e.g. the
    conversion strategy: ``"markdown.new"`` / ``"fallback"`` / ``"markitdown"``).
    Returning ``None`` is fine for runners that don't need to report a message.
    """

    item_id: str
    category: str
    label: str
    target_path: Path
    runner: Callable[[], Awaitable[str | None]]
    status: str = "queued"
    message: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "item_id": self.item_id,
            "category": self.category,
            "label": self.label,
            "target_path": str(self.target_path),
            "status": self.status,
            "message": self.message,
        }


@dataclass
class BatchJob:
    """A live batch download job."""

    job_id: str
    notebook_id: str
    target_dir: Path
    items: list[JobItem]
    force: bool = False
    concurrency: int = 3
    keep_original: bool = False
    legacy_pdf: bool = False
    status: str = "pending"  # pending → running → done | partial | cancelled
    started_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    cancel_event: asyncio.Event = field(default_factory=asyncio.Event)
    queue: asyncio.Queue = field(default_factory=asyncio.Queue)
    task: asyncio.Task | None = None

    @property
    def total(self) -> int:
        return len(self.items)

    def counts(self) -> dict[str, int]:
        c = {"queued": 0, "running": 0, "done": 0, "skipped": 0, "error": 0, "cancelled": 0}
        for it in self.items:
            c[it.status] = c.get(it.status, 0) + 1
        return c

    def to_dict(self) -> dict[str, Any]:
        c = self.counts()
        return {
            "job_id": self.job_id,
            "notebook_id": self.notebook_id,
            "target_dir": str(self.target_dir),
            "status": self.status,
            "total": self.total,
            "started_at": self.started_at,
            **c,
        }


class JobRegistry:
    """In-memory registry of jobs."""

    def __init__(self) -> None:
        self._jobs: dict[str, BatchJob] = {}

    def add(self, job: BatchJob) -> None:
        self._jobs[job.job_id] = job

    def get(self, job_id: str) -> BatchJob | None:
        return self._jobs.get(job_id)

    def list(self) -> list[BatchJob]:
        return list(self._jobs.values())


# ----------------------------------------------------------- builder + runner


async def build_items(
    client: NotebookLMClient,
    notebook_id: str,
    target_dir: Path,
    categories: Iterable[str],
    *,
    keep_original: bool = False,
    legacy_pdf: bool = False,
) -> list[JobItem]:
    """Expand the chosen categories into concrete `JobItem`s.

    ``keep_original``: when True, file sources (PDF/DOCX/PPTX) keep the original
    binary alongside the produced ``.md``. Plumbed through to
    ``source_to_markdown`` via ``ConversionOptions``.

    ``legacy_pdf``: when True, ``WEB_PAGE`` sources are routed through the
    legacy ``wkhtmltopdf`` runner (producing ``<title>.pdf``) instead of the
    new Markdown converter. One-release escape hatch for users who depended
    on the old behavior; will be removed in a future minor version.
    """
    requested = [c for c in categories if c in CATEGORIES]
    if not requested:
        return []

    items: list[JobItem] = []
    target_dir.mkdir(parents=True, exist_ok=True)

    for cat in requested:
        if cat == "sources":
            items.extend(
                await _build_source_items(
                    client,
                    notebook_id,
                    target_dir,
                    keep_original=keep_original,
                    legacy_pdf=legacy_pdf,
                )
            )
        elif cat == "notes":
            items.extend(await _build_note_items(client, notebook_id, target_dir))
        else:
            items.extend(await _build_artifact_items(client, notebook_id, target_dir, cat))

    return items


async def _build_source_items(
    client: NotebookLMClient,
    notebook_id: str,
    target_dir: Path,
    *,
    keep_original: bool = False,
    legacy_pdf: bool = False,
) -> list[JobItem]:
    sources = await client.sources.list(notebook_id)
    out: list[JobItem] = []
    options = ConversionOptions.from_env(keep_original=keep_original)

    for src in sources:
        title = sanitize_filename(src.title or "untitled")
        # Decide strategy by source type.
        if src.kind in _FILE_SOURCE_KINDS and src.url:
            # PDF/DOCX/PPTX → Markdown via markitdown.
            tgt = target_dir / f"{title}.md"
            out.append(
                JobItem(
                    item_id=f"src-{src.id}",
                    category="sources",
                    label=src.title or src.id,
                    target_path=tgt,
                    runner=_make_source_to_markdown(src.url, src.kind, tgt, options),
                )
            )
        elif src.kind == SourceType.IMAGE and src.url:
            # IMAGE: download as-is. The runner picks the real extension at
            # runtime from Content-Type / URL path; we use a placeholder
            # `<title>.img` here. For skip-if-exists, we pre-scan the dir
            # for any `<title>.<known-image-ext>` sibling and, if found,
            # point ``target_path`` at it so the orchestrator's normal
            # skip check picks it up.
            existing = _find_existing_image(target_dir, title)
            tgt = existing if existing is not None else target_dir / f"{title}.img"
            out.append(
                JobItem(
                    item_id=f"src-{src.id}",
                    category="sources",
                    label=src.title or src.id,
                    target_path=tgt,
                    runner=_make_image_downloader(src.url, target_dir, title, options),
                )
            )
        elif src.kind in _DIRECT_DOWNLOAD_KINDS and src.url:
            # CSV stays binary — Markdown conversion would lose spreadsheet utility.
            ext = _SOURCE_EXT_MAP.get(src.kind, ".bin")
            tgt = target_dir / f"{title}{ext}"
            out.append(
                JobItem(
                    item_id=f"src-{src.id}",
                    category="sources",
                    label=src.title or src.id,
                    target_path=tgt,
                    runner=_make_url_downloader(src.url, tgt),
                )
            )
        elif src.kind == SourceType.WEB_PAGE and src.url:
            if legacy_pdf:
                tgt = target_dir / f"{title}.pdf"
                out.append(
                    JobItem(
                        item_id=f"src-{src.id}",
                        category="sources",
                        label=src.title or src.id,
                        target_path=tgt,
                        runner=_make_webpage_pdf_legacy(src.url, tgt),
                    )
                )
            else:
                tgt = target_dir / f"{title}.md"
                out.append(
                    JobItem(
                        item_id=f"src-{src.id}",
                        category="sources",
                        label=src.title or src.id,
                        target_path=tgt,
                        runner=_make_source_to_markdown(src.url, SourceType.WEB_PAGE, tgt, options),
                    )
                )
        elif src.kind in (SourceType.MARKDOWN, SourceType.PASTED_TEXT) or (
            not src.url
            and src.kind
            not in (
                SourceType.WEB_PAGE,
                SourceType.YOUTUBE,
                SourceType.GOOGLE_DOCS,
                SourceType.GOOGLE_SLIDES,
                SourceType.GOOGLE_SPREADSHEET,
                SourceType.GOOGLE_DRIVE_AUDIO,
                SourceType.GOOGLE_DRIVE_VIDEO,
            )
        ):
            tgt = target_dir / f"{title}.md"
            out.append(
                JobItem(
                    item_id=f"src-{src.id}",
                    category="sources",
                    label=src.title or src.id,
                    target_path=tgt,
                    runner=_make_fulltext_runner(client, notebook_id, src.id, tgt),
                )
            )
        else:
            tgt = target_dir / f"{title}.todo"
            placeholder = (
                f"Source: {src.title}\nType: {src.kind}\nURL: {src.url or ''}\n"
                "Unsupported source type for direct download.\n"
            )
            out.append(
                JobItem(
                    item_id=f"src-{src.id}",
                    category="sources",
                    label=src.title or src.id,
                    target_path=tgt,
                    runner=_make_text_writer(tgt, placeholder),
                )
            )
    return out


async def _build_note_items(
    client: NotebookLMClient, notebook_id: str, target_dir: Path
) -> list[JobItem]:
    notes = await client.notes.list(notebook_id)
    out: list[JobItem] = []
    for n in notes:
        title = sanitize_filename(n.title or "Untitled")
        tgt = target_dir / f"{title}.md"
        out.append(
            JobItem(
                item_id=f"note-{n.id}",
                category="notes",
                label=n.title or n.id,
                target_path=tgt,
                runner=_make_text_writer(tgt, n.content or ""),
            )
        )
    return out


async def _build_artifact_items(
    client: NotebookLMClient, notebook_id: str, target_dir: Path, category: str
) -> list[JobItem]:
    kind = _ARTIFACT_KIND_MAP[category]
    artifacts = await client.artifacts.list(notebook_id, kind)
    completed = [a for a in artifacts if a.is_completed]
    out: list[JobItem] = []
    ext = _ARTIFACT_EXT_MAP.get(kind, ".bin")
    for a in completed:
        title = sanitize_filename(a.title or category)
        tgt = target_dir / f"{title}{ext}"
        out.append(
            JobItem(
                item_id=f"art-{a.id}",
                category=category,
                label=a.title or a.id,
                target_path=tgt,
                runner=_make_artifact_downloader(client, notebook_id, kind, a.id, tgt),
            )
        )
    return out


# ------------------------------------------------------------ runner builders


def _make_url_downloader(url: str, target: Path) -> Callable[[], Awaitable[str | None]]:
    async def run() -> str | None:
        return await asyncio.to_thread(_download_url_sync, url, target)

    return run


def _download_url_sync(url: str, target: Path) -> str | None:
    """Stream ``url`` to ``target`` with one slash-retry on 403/404.

    Returns ``"download (slash-retry)"`` when the slash-retry kicked in, ``None``
    otherwise — the orchestrator surfaces this on the SSE event payload.
    """
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(target.suffix + ".tmp")
    try:
        with httpx.Client(timeout=60.0, follow_redirects=True) as client:
            response = fetch_with_slash_retry(client, url)
            if response.status_code < 200 or response.status_code >= 300:
                raise RuntimeError(f"download failed: HTTP {response.status_code}")
            with tmp.open("wb") as fh:
                for chunk in response.iter_bytes():
                    fh.write(chunk)
            tmp.replace(target)
            retried = slash_retried(response)
    except httpx.HTTPError as exc:
        tmp.unlink(missing_ok=True)
        raise RuntimeError(f"download failed: {exc}") from exc
    except Exception:
        tmp.unlink(missing_ok=True)
        raise
    return "download (slash-retry)" if retried else None


def _find_existing_image(target_dir: Path, title: str) -> Path | None:
    """Return an existing `<title>.<known-image-ext>` sibling if one exists.

    Used by the orchestrator's pre-skip check so re-running a batch doesn't
    redownload an image that's already present under a different extension
    than the helper would pick this run.
    """
    for ext in known_image_extensions():
        candidate = target_dir / f"{title}{ext}"
        if candidate.exists():
            return candidate
    return None


def _make_image_downloader(
    url: str,
    target_dir: Path,
    title: str,
    options: ConversionOptions,
) -> Callable[[], Awaitable[str | None]]:
    """Build a runner that streams an image source and picks the extension.

    The runner streams the response body, sniffs ``Content-Type`` from the
    response headers (falling back to the URL path / a default), writes
    the bytes to ``<title>.<ext>`` via a temp-file rename, and returns
    a strategy message of the form ``"image:<final-name>"``.
    """
    headers = {"User-Agent": options.effective_user_agent}

    async def run() -> str | None:
        target_dir.mkdir(parents=True, exist_ok=True)
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
                    raise RuntimeError(f"image download failed: HTTP {response.status_code}")
                ext = _pick_image_extension(url, response.headers.get("content-type"))
                final = target_dir / f"{title}{ext}"
                tmp = final.with_suffix(final.suffix + ".tmp")
                try:
                    with tmp.open("wb") as fh:
                        async for chunk in response.aiter_bytes():
                            fh.write(chunk)
                    tmp.replace(final)
                except Exception:
                    tmp.unlink(missing_ok=True)
                    raise
                retried = slash_retried(response)
        except httpx.HTTPError as exc:
            raise RuntimeError(f"image download transport error: {exc}") from exc
        message = f"{IMAGE_STRATEGY}:{final.name}"
        if retried:
            message += " (slash-retry)"
        return message

    return run


def _make_source_to_markdown(
    url: str,
    kind: SourceType,
    target: Path,
    options: ConversionOptions,
) -> Callable[[], Awaitable[str | None]]:
    """Build a runner that converts a source URL to Markdown.

    The runner returns the conversion strategy (``"remote"`` / ``"fallback"`` /
    ``"markitdown"``) so the orchestrator can surface it in SSE ``event: item``
    payloads as a useful progress message.
    """

    async def run() -> str | None:
        try:
            result: ConversionResult = await source_to_markdown(url, kind, target, options=options)
        except ConversionError:
            # Bubble up — orchestrator's run_one wraps this as item.status="error".
            raise
        message = _format_strategy_message(result.strategy)
        if result.slash_retried:
            message = f"{message} (slash-retry)"
        return message

    return run


def _format_strategy_message(strategy: str) -> str:
    """Render a strategy literal as a UI-friendly progress message.

    Mirrors the log/progress prefixes documented in the design (D7).
    """
    return {
        "remote": "markdown.new",
        "fallback": "fallback",
        "markitdown": "markitdown",
        "fulltext": "fulltext",
        "passthrough": "passthrough",
        "legacy-pdf": "legacy-pdf",
    }.get(strategy, strategy)


def _make_webpage_pdf_legacy(url: str, target: Path) -> Callable[[], Awaitable[str | None]]:
    """Legacy ``wkhtmltopdf`` runner — opt-in only via ``--legacy-pdf``.

    Will be removed in a future minor version once users have migrated to the
    Markdown default. Behavior is identical to the previous default.
    """

    async def run() -> str | None:
        wkhtmltopdf = shutil.which("wkhtmltopdf")
        target.parent.mkdir(parents=True, exist_ok=True)
        if not wkhtmltopdf:
            target.with_suffix(".todo").write_text(
                f"WEB_PAGE: {url}\nInstall wkhtmltopdf to convert this source to PDF.\n",
                encoding="utf-8",
            )
            raise RuntimeError("wkhtmltopdf not installed; wrote .todo placeholder")
        await asyncio.to_thread(
            subprocess.run,
            [wkhtmltopdf, "--quiet", url, str(target)],
            check=True,
        )
        return _format_strategy_message("legacy-pdf")

    return run


def _make_fulltext_runner(
    client: NotebookLMClient, notebook_id: str, source_id: str, target: Path
) -> Callable[[], Awaitable[str | None]]:
    async def run() -> str | None:
        ft = await client.sources.get_fulltext(notebook_id, source_id)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(ft.content or "", encoding="utf-8")
        return _format_strategy_message("fulltext")

    return run


def _make_text_writer(target: Path, content: str) -> Callable[[], Awaitable[str | None]]:
    async def run() -> str | None:
        target.parent.mkdir(parents=True, exist_ok=True)
        await asyncio.to_thread(target.write_text, content, "utf-8")
        return None

    return run


def _make_artifact_downloader(
    client: NotebookLMClient,
    notebook_id: str,
    kind: ArtifactType,
    artifact_id: str,
    target: Path,
) -> Callable[[], Awaitable[str | None]]:
    async def run() -> str | None:
        target.parent.mkdir(parents=True, exist_ok=True)
        out = str(target)
        if kind == ArtifactType.AUDIO:
            await client.artifacts.download_audio(notebook_id, out, artifact_id=artifact_id)
        elif kind == ArtifactType.VIDEO:
            await client.artifacts.download_video(notebook_id, out, artifact_id=artifact_id)
        elif kind == ArtifactType.SLIDE_DECK:
            await client.artifacts.download_slide_deck(notebook_id, out, artifact_id=artifact_id)
        elif kind == ArtifactType.INFOGRAPHIC:
            await client.artifacts.download_infographic(notebook_id, out, artifact_id=artifact_id)
        elif kind == ArtifactType.REPORT:
            await client.artifacts.download_report(notebook_id, out, artifact_id=artifact_id)
        elif kind == ArtifactType.MIND_MAP:
            await client.artifacts.download_mind_map(notebook_id, out, artifact_id=artifact_id)
        elif kind == ArtifactType.DATA_TABLE:
            await client.artifacts.download_data_table(notebook_id, out, artifact_id=artifact_id)
        elif kind == ArtifactType.QUIZ:
            await client.artifacts.download_quiz(notebook_id, out, artifact_id=artifact_id)
        elif kind == ArtifactType.FLASHCARDS:
            await client.artifacts.download_flashcards(notebook_id, out, artifact_id=artifact_id)
        else:
            raise RuntimeError(f"unsupported artifact kind: {kind}")
        return None

    return run


# --------------------------------------------------------- job orchestration


async def run_job(job: BatchJob) -> None:
    """Run a job to completion. Emits progress events via `job.queue`."""
    job.status = "running"
    sem = asyncio.Semaphore(job.concurrency)
    await job.queue.put({"event": "started", "data": job.to_dict()})

    async def run_one(item: JobItem) -> None:
        if job.cancel_event.is_set():
            item.status = "cancelled"
            await _emit(job, item)
            return
        async with sem:
            if job.cancel_event.is_set():
                item.status = "cancelled"
                await _emit(job, item)
                return
            if not job.force and item.target_path.exists():
                item.status = "skipped"
                item.message = "file exists"
                await _emit(job, item)
                return
            item.status = "running"
            await _emit(job, item)
            try:
                outcome = await item.runner()
                item.status = "done"
                # Runner may return a short message (e.g. conversion strategy)
                # that the SSE consumer can surface; default to empty.
                item.message = outcome or ""
            except Exception as e:  # noqa: BLE001 — capture every failure mode at the boundary
                item.status = "error"
                item.message = str(e)
                logger.warning("job %s item %s error: %s", job.job_id, item.item_id, e)
            await _emit(job, item)

    await asyncio.gather(*(run_one(it) for it in job.items), return_exceptions=False)

    counts = job.counts()
    if job.cancel_event.is_set():
        job.status = "cancelled"
    elif counts.get("error", 0) > 0:
        job.status = "partial"
    else:
        job.status = "done"

    await job.queue.put(
        {
            "event": "complete",
            "data": {"job_id": job.job_id, **counts, "total": job.total, "status": job.status},
        }
    )
    await job.queue.put(None)  # sentinel


async def _emit(job: BatchJob, item: JobItem) -> None:
    await job.queue.put({"event": "item", "data": item.to_dict()})
