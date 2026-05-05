"""Integration tests for ``SourceType.IMAGE`` handling in the batch orchestrator."""

from __future__ import annotations

from dataclasses import dataclass

import pytest

from notebooklm.types import SourceType
from notebooklm.web import jobs as jobs_module


@dataclass
class FakeSource:
    id: str
    title: str
    url: str | None
    kind: SourceType


class FakeSourcesAPI:
    def __init__(self, sources):
        self._sources = sources

    async def list(self, _: str):
        return list(self._sources)


class FakeClient:
    def __init__(self, sources):
        self.sources = FakeSourcesAPI(sources)


# --------------------------------------------------------------- happy paths


_PNG_BYTES = b"\x89PNG\r\n\x1a\n" + b"x" * 1024  # plausible PNG-like blob
_JPG_BYTES = b"\xff\xd8\xff\xe0" + b"x" * 1024  # plausible JPEG-like blob


@pytest.mark.asyncio
async def test_image_with_content_type_picks_png(httpx_mock, tmp_path):
    httpx_mock.add_response(
        url="https://cdn.example/cover",
        content=_PNG_BYTES,
        headers={"content-type": "image/png"},
        status_code=200,
    )

    client = FakeClient(
        [FakeSource(id="s1", title="Cover", url="https://cdn.example/cover", kind=SourceType.IMAGE)]
    )
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["sources"])
    assert len(items) == 1

    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=1
    )
    await jobs_module.run_job(job)

    assert items[0].status == "done"
    assert items[0].message == "image:Cover.png"
    final = tmp_path / "Cover.png"
    assert final.exists()
    assert final.read_bytes() == _PNG_BYTES


@pytest.mark.asyncio
async def test_image_with_content_type_jpeg_picks_jpg(httpx_mock, tmp_path):
    httpx_mock.add_response(
        url="https://cdn.example/photo",
        content=_JPG_BYTES,
        headers={"content-type": "image/jpeg; charset=binary"},
        status_code=200,
    )
    client = FakeClient(
        [FakeSource(id="s1", title="Photo", url="https://cdn.example/photo", kind=SourceType.IMAGE)]
    )
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["sources"])
    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=1
    )
    await jobs_module.run_job(job)

    assert items[0].status == "done"
    assert items[0].message == "image:Photo.jpg"
    assert (tmp_path / "Photo.jpg").exists()


@pytest.mark.asyncio
async def test_image_url_path_extension_used(httpx_mock, tmp_path):
    """Content-Type missing/generic; URL path extension picked."""
    httpx_mock.add_response(
        url="https://files.example/cover.gif",
        content=b"GIF89a" + b"x" * 1024,
        headers={"content-type": "application/octet-stream"},
        status_code=200,
    )
    client = FakeClient(
        [
            FakeSource(
                id="s1",
                title="Banner",
                url="https://files.example/cover.gif",
                kind=SourceType.IMAGE,
            )
        ]
    )
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["sources"])
    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=1
    )
    await jobs_module.run_job(job)

    assert items[0].status == "done"
    assert items[0].message == "image:Banner.gif"
    assert (tmp_path / "Banner.gif").exists()


@pytest.mark.asyncio
async def test_image_default_fallback_to_png(httpx_mock, tmp_path):
    """No Content-Type, no URL path extension → fallback to .png."""
    httpx_mock.add_response(
        url="https://cdn.example/asset?id=abc",
        content=b"x" * 1024,
        status_code=200,
        # No content-type header.
    )
    client = FakeClient(
        [
            FakeSource(
                id="s1",
                title="Asset",
                url="https://cdn.example/asset?id=abc",
                kind=SourceType.IMAGE,
            )
        ]
    )
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["sources"])
    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=1
    )
    await jobs_module.run_job(job)

    assert items[0].status == "done"
    assert items[0].message == "image:Asset.png"
    assert (tmp_path / "Asset.png").exists()


# ----------------------------------------------------------- skip-if-exists


@pytest.mark.asyncio
async def test_image_skip_if_existing_sibling_extension(httpx_mock, tmp_path):
    """Pre-existing `<title>.jpg` should make a new image source `skipped`,
    even though the helper would default to `.png` for this URL."""
    existing = tmp_path / "Cover.jpg"
    existing.write_bytes(b"already here")

    # Even though we add a mock, the runner should never be called because
    # skip-if-exists kicks in upfront (no httpx_mock.add_response = no
    # configured response = test would crash if it ran).

    client = FakeClient(
        [FakeSource(id="s1", title="Cover", url="https://cdn.example/cover", kind=SourceType.IMAGE)]
    )
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["sources"])
    assert len(items) == 1
    # The orchestrator should have pointed target_path at the existing sibling.
    assert items[0].target_path == existing

    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=1, force=False
    )
    await jobs_module.run_job(job)
    assert items[0].status == "skipped"
    assert items[0].message == "file exists"
    # Existing file untouched.
    assert existing.read_bytes() == b"already here"


@pytest.mark.asyncio
async def test_image_force_redownloads(httpx_mock, tmp_path):
    """With force=True, the orchestrator should still call the runner
    even when a sibling exists. The runner picks a (possibly different)
    extension based on the response."""
    existing_jpg = tmp_path / "Cover.jpg"
    existing_jpg.write_bytes(b"old")

    httpx_mock.add_response(
        url="https://cdn.example/cover",
        content=_PNG_BYTES,
        headers={"content-type": "image/png"},
        status_code=200,
    )

    client = FakeClient(
        [FakeSource(id="s1", title="Cover", url="https://cdn.example/cover", kind=SourceType.IMAGE)]
    )
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["sources"])

    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=1, force=True
    )
    await jobs_module.run_job(job)
    # The runner ran; new file lives at .png (Content-Type wins).
    assert (tmp_path / "Cover.png").exists()
    assert items[0].status == "done"


# ---------------------------------------------------------------- errors


@pytest.mark.asyncio
async def test_image_404_marks_item_error(httpx_mock, tmp_path):
    httpx_mock.add_response(
        url="https://cdn.example/missing",
        status_code=404,
        content=b"not found",
    )
    httpx_mock.add_response(
        url="https://cdn.example/missing/",
        status_code=404,
        content=b"not found either",
    )
    client = FakeClient(
        [
            FakeSource(
                id="s1", title="Missing", url="https://cdn.example/missing", kind=SourceType.IMAGE
            )
        ]
    )
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["sources"])
    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=1
    )
    await jobs_module.run_job(job)

    assert items[0].status == "error"
    assert "HTTP 404" in items[0].message
    # No partial file at any image extension.
    for ext in (".png", ".jpg", ".gif", ".img"):
        assert not (tmp_path / f"Missing{ext}").exists()


# ---------------------------------------------------------- slash-retry


@pytest.mark.asyncio
async def test_image_slash_retry_recovers_from_404(httpx_mock, tmp_path):
    """First attempt 404 with trailing slash; retry without slash succeeds."""
    httpx_mock.add_response(
        url="https://cdn.example/cover/",
        status_code=404,
    )
    httpx_mock.add_response(
        url="https://cdn.example/cover",
        content=_PNG_BYTES,
        headers={"content-type": "image/png"},
        status_code=200,
    )
    client = FakeClient(
        [
            FakeSource(
                id="s1",
                title="Cover",
                url="https://cdn.example/cover/",
                kind=SourceType.IMAGE,
            )
        ]
    )
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["sources"])
    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=1
    )
    await jobs_module.run_job(job)

    assert items[0].status == "done"
    assert items[0].message == "image:Cover.png (slash-retry)"
    assert (tmp_path / "Cover.png").exists()


@pytest.mark.asyncio
async def test_image_slash_retry_recovers_from_403(httpx_mock, tmp_path):
    """First attempt 403 without trailing slash; retry with slash succeeds."""
    httpx_mock.add_response(
        url="https://cdn.example/photo",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://cdn.example/photo/",
        content=_JPG_BYTES,
        headers={"content-type": "image/jpeg"},
        status_code=200,
    )
    client = FakeClient(
        [
            FakeSource(
                id="s1",
                title="Photo",
                url="https://cdn.example/photo",
                kind=SourceType.IMAGE,
            )
        ]
    )
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["sources"])
    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=1
    )
    await jobs_module.run_job(job)

    assert items[0].status == "done"
    assert items[0].message == "image:Photo.jpg (slash-retry)"
    assert (tmp_path / "Photo.jpg").exists()


# -------------------------------------------------- concurrency upper bound


@pytest.mark.asyncio
async def test_high_concurrency_does_not_leak_or_orphan(httpx_mock, tmp_path):
    """At concurrency=10 with 12 items, every item terminates cleanly."""
    sources = []
    for i in range(12):
        url = f"https://cdn.example/item{i}.png"
        sources.append(FakeSource(id=f"s{i}", title=f"Item{i}", url=url, kind=SourceType.IMAGE))
        httpx_mock.add_response(
            url=url, content=_PNG_BYTES, headers={"content-type": "image/png"}, status_code=200
        )

    client = FakeClient(sources)
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["sources"])
    assert len(items) == 12

    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=10
    )
    await jobs_module.run_job(job)

    statuses = [it.status for it in items]
    assert all(s == "done" for s in statuses), f"unexpected statuses: {statuses}"
    for i in range(12):
        assert (tmp_path / f"Item{i}.png").exists()
