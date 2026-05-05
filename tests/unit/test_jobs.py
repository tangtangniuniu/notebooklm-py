"""Unit tests for the batch download orchestrator (`web/jobs.py`)."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pytest

from notebooklm.types import ArtifactType, SourceType


@pytest.fixture
def jobs_module():
    """Import lazily — the module lives under web/ which gates on FastAPI."""
    from notebooklm.web import jobs

    return jobs


# ------------------------------------------------------------------ fixtures


@dataclass
class FakeSource:
    id: str
    title: str
    url: str | None
    kind: SourceType


@dataclass
class FakeNote:
    id: str
    title: str
    content: str


@dataclass
class FakeArtifact:
    id: str
    title: str
    kind: ArtifactType
    is_completed: bool = True


class FakeSourcesAPI:
    def __init__(self, sources: list[FakeSource]):
        self._sources = sources
        self.fulltext_calls: list[tuple[str, str]] = []

    async def list(self, _: str) -> list[FakeSource]:
        return list(self._sources)

    async def get_fulltext(self, notebook_id: str, source_id: str) -> Any:
        self.fulltext_calls.append((notebook_id, source_id))

        @dataclass
        class FT:
            content: str

        return FT(content=f"fulltext for {source_id}")


class FakeNotesAPI:
    def __init__(self, notes: list[FakeNote]):
        self._notes = notes

    async def list(self, _: str) -> list[FakeNote]:
        return list(self._notes)


class FakeArtifactsAPI:
    def __init__(self, artifacts: list[FakeArtifact]):
        self._artifacts = artifacts
        self.download_calls: list[tuple[str, str, str]] = []  # (kind, artifact_id, target)

    async def list(self, _: str, kind: ArtifactType | None = None) -> list[FakeArtifact]:
        if kind is None:
            return list(self._artifacts)
        return [a for a in self._artifacts if a.kind == kind]

    def _record(self, kind: str, artifact_id: str, target: str) -> None:
        self.download_calls.append((kind, artifact_id, target))
        Path(target).write_text(f"{kind}-content", encoding="utf-8")

    async def download_audio(self, _, out, artifact_id):
        self._record("audio", artifact_id, out)

    async def download_video(self, _, out, artifact_id):
        self._record("video", artifact_id, out)

    async def download_slide_deck(self, _, out, artifact_id):
        self._record("slide_deck", artifact_id, out)

    async def download_infographic(self, _, out, artifact_id):
        self._record("infographic", artifact_id, out)

    async def download_report(self, _, out, artifact_id):
        self._record("report", artifact_id, out)

    async def download_mind_map(self, _, out, artifact_id):
        self._record("mind_map", artifact_id, out)

    async def download_data_table(self, _, out, artifact_id):
        self._record("data_table", artifact_id, out)

    async def download_quiz(self, _, out, artifact_id):
        self._record("quiz", artifact_id, out)

    async def download_flashcards(self, _, out, artifact_id):
        self._record("flashcards", artifact_id, out)


class FakeClient:
    def __init__(
        self,
        sources: list[FakeSource] | None = None,
        notes: list[FakeNote] | None = None,
        artifacts: list[FakeArtifact] | None = None,
    ):
        self.sources = FakeSourcesAPI(sources or [])
        self.notes = FakeNotesAPI(notes or [])
        self.artifacts = FakeArtifactsAPI(artifacts or [])


# ------------------------------------------------------------------ helpers


async def _drain_queue(job) -> list[dict]:
    events: list[dict] = []
    while True:
        ev = await job.queue.get()
        if ev is None:
            return events
        events.append(ev)


# ------------------------------------------------------------------ tests


@pytest.mark.asyncio
async def test_build_items_empty_categories(jobs_module, tmp_path):
    items = await jobs_module.build_items(FakeClient(), "nb1", tmp_path, [])
    assert items == []


@pytest.mark.asyncio
async def test_notes_writes_one_md_per_note(jobs_module, tmp_path):
    client = FakeClient(notes=[FakeNote(id="n1", title="My Note 中文", content="hello")])
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["notes"])
    assert len(items) == 1
    assert items[0].target_path.name == "My Note 中文.md"

    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=1
    )
    await jobs_module.run_job(job)
    assert items[0].status == "done"
    assert items[0].target_path.read_text(encoding="utf-8") == "hello"


@pytest.mark.asyncio
async def test_skip_if_exists(jobs_module, tmp_path):
    client = FakeClient(notes=[FakeNote(id="n1", title="x", content="hi")])
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["notes"])
    items[0].target_path.write_text("preexisting", encoding="utf-8")

    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=1, force=False
    )
    await jobs_module.run_job(job)
    assert items[0].status == "skipped"
    assert items[0].target_path.read_text(encoding="utf-8") == "preexisting"


@pytest.mark.asyncio
async def test_force_overwrites(jobs_module, tmp_path):
    client = FakeClient(notes=[FakeNote(id="n1", title="x", content="fresh")])
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["notes"])
    items[0].target_path.write_text("preexisting", encoding="utf-8")

    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=1, force=True
    )
    await jobs_module.run_job(job)
    assert items[0].status == "done"
    assert items[0].target_path.read_text(encoding="utf-8") == "fresh"


@pytest.mark.asyncio
async def test_error_isolation(jobs_module, tmp_path):
    notes = [FakeNote(id=str(i), title=f"n{i}", content="ok") for i in range(3)]
    client = FakeClient(notes=notes)
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["notes"])

    async def boom() -> None:
        raise RuntimeError("simulated failure")

    items[1].runner = boom

    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=1
    )
    await jobs_module.run_job(job)
    assert [it.status for it in items] == ["done", "error", "done"]
    assert "simulated failure" in items[1].message
    assert job.status == "partial"


@pytest.mark.asyncio
async def test_concurrency_cap_respected(jobs_module, tmp_path):
    # 6 items, concurrency=2, each holds for a small wait. We assert at most
    # 2 are running at once.
    in_flight = 0
    peak = 0
    lock = asyncio.Lock()

    async def slow(i: int) -> None:
        nonlocal in_flight, peak
        async with lock:
            in_flight += 1
            peak = max(peak, in_flight)
        await asyncio.sleep(0.05)
        async with lock:
            in_flight -= 1

    items = [
        jobs_module.JobItem(
            item_id=f"i{i}",
            category="notes",
            label=f"i{i}",
            target_path=tmp_path / f"f{i}.md",
            runner=lambda i=i: slow(i),
        )
        for i in range(6)
    ]
    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=2
    )
    await jobs_module.run_job(job)
    assert peak <= 2
    assert all(it.status == "done" for it in items)


@pytest.mark.asyncio
async def test_cancel_cancels_pending_items(jobs_module, tmp_path):
    started = asyncio.Event()
    release = asyncio.Event()

    async def gated() -> None:
        started.set()
        await release.wait()

    items = []
    for i in range(5):
        items.append(
            jobs_module.JobItem(
                item_id=f"i{i}",
                category="notes",
                label=f"i{i}",
                target_path=tmp_path / f"f{i}.md",
                runner=gated if i == 0 else (lambda: asyncio.sleep(0.01)),
            )
        )

    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=1
    )
    job_task = asyncio.create_task(jobs_module.run_job(job))
    await started.wait()
    job.cancel_event.set()
    release.set()
    await job_task

    assert items[0].status == "done"
    # Items 1..4 should have been short-circuited via cancellation or run quickly;
    # at least one must be marked cancelled.
    assert any(it.status == "cancelled" for it in items[1:])
    assert job.status == "cancelled"


@pytest.mark.asyncio
async def test_artifact_audio_download(jobs_module, tmp_path):
    client = FakeClient(artifacts=[FakeArtifact(id="a1", title="Cast", kind=ArtifactType.AUDIO)])
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["audio"])
    assert len(items) == 1
    assert items[0].target_path.name == "Cast.mp4"

    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=1
    )
    await jobs_module.run_job(job)
    assert items[0].status == "done"
    assert client.artifacts.download_calls == [("audio", "a1", str(items[0].target_path))]


@pytest.mark.asyncio
async def test_progress_events_emitted(jobs_module, tmp_path):
    client = FakeClient(notes=[FakeNote(id="n1", title="x", content="hi")])
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["notes"])
    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=1
    )

    async def collect() -> list[dict]:
        events: list[dict] = []
        while True:
            ev = await job.queue.get()
            if ev is None:
                return events
            events.append(ev)

    collector = asyncio.create_task(collect())
    await jobs_module.run_job(job)
    events = await collector

    kinds = [e["event"] for e in events]
    assert "started" in kinds
    assert "complete" in kinds
    # At least one running and one done item event.
    item_events = [e for e in events if e["event"] == "item"]
    statuses = [e["data"]["status"] for e in item_events]
    assert "running" in statuses
    assert "done" in statuses


def test_unsupported_source_kind_writes_todo(jobs_module, tmp_path):
    # Build a single source item for a Drive video (no direct download path)
    # and run its runner. Synchronous wrapper so we can use plain pytest.
    source = FakeSource(id="s1", title="vid", url=None, kind=SourceType.GOOGLE_DRIVE_VIDEO)
    client = FakeClient(sources=[source])

    async def go():
        items = await jobs_module.build_items(client, "nb1", tmp_path, ["sources"])
        assert len(items) == 1
        assert items[0].target_path.name == "vid.todo"
        await items[0].runner()
        assert items[0].target_path.read_text(encoding="utf-8").startswith("Source: vid")

    asyncio.run(go())
