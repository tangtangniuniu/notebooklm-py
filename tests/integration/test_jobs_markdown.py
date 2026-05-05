"""Integration tests: batch orchestrator wiring of the source-markdown-conversion path.

These tests exercise the full path from ``build_items`` → ``run_job`` for
``WEB_PAGE`` and binary office (``PDF``/``DOCX``/``PPTX``) sources, verifying
that the new conversion module is invoked and the resulting Markdown lands at
the expected file paths.

We mock ``markdown.new`` and the source URLs themselves with ``pytest-httpx``;
no real network is contacted.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pytest

from notebooklm.types import SourceType
from notebooklm.web import jobs as jobs_module

FIXTURES = Path(__file__).resolve().parents[1] / "unit" / "conversion"  # not used
CONVERSION_FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "conversion"


# ----------------------------------------------------------- fake client setup


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


# ----------------------------------------------------------- end-to-end tests


@pytest.mark.asyncio
async def test_web_page_routes_through_markdown_new(httpx_mock, tmp_path):
    body = "# Web page article\n\nReal markdown content with adequate length to pass the threshold."
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com/blog",
        text=body,
        status_code=200,
    )

    client = FakeClient(
        [
            FakeSource(
                id="s1", title="Blog Post", url="https://example.com/blog", kind=SourceType.WEB_PAGE
            )
        ]
    )
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["sources"])

    assert len(items) == 1
    assert items[0].target_path.name == "Blog Post.md"

    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=1
    )
    await jobs_module.run_job(job)

    assert items[0].status == "done"
    # Strategy is surfaced in the SSE-bound message field.
    assert items[0].message == "markdown.new"
    # File written to the expected target path.
    assert items[0].target_path.read_text(encoding="utf-8") == body


@pytest.mark.asyncio
async def test_web_page_falls_back_to_local(httpx_mock, tmp_path, monkeypatch):
    """When markdown.new returns 429, the orchestrator's item should still succeed."""

    # 429 triggers the throttle-retry path — register the response twice so
    # both attempts return the same throttling status.
    async def _instant(_seconds):
        return None

    monkeypatch.setattr("notebooklm.conversion._remote.asyncio.sleep", _instant)
    for _ in range(2):
        httpx_mock.add_response(
            url="https://markdown.new/https://example.com/article",
            status_code=429,
            text="rate limited - try again later " * 5,
        )
    httpx_mock.add_response(
        url="https://example.com/article",
        text="<html><body><h1>Real article</h1><p>body</p></body></html>",
        headers={"content-type": "text/html"},
        status_code=200,
    )

    client = FakeClient(
        [
            FakeSource(
                id="s1",
                title="article",
                url="https://example.com/article",
                kind=SourceType.WEB_PAGE,
            )
        ]
    )
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["sources"])
    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=1
    )
    await jobs_module.run_job(job)

    assert items[0].status == "done"
    assert items[0].message == "fallback"
    text = items[0].target_path.read_text(encoding="utf-8")
    assert "# Real article" in text


@pytest.mark.asyncio
async def test_pdf_source_routed_through_markitdown(httpx_mock, tmp_path):
    httpx_mock.add_response(
        url="https://files.example.com/doc.pdf",
        content=(CONVERSION_FIXTURES / "sample.pdf").read_bytes(),
        headers={"content-type": "application/pdf"},
        status_code=200,
    )

    client = FakeClient(
        [
            FakeSource(
                id="s1",
                title="My Paper",
                url="https://files.example.com/doc.pdf",
                kind=SourceType.PDF,
            )
        ]
    )
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["sources"])

    assert len(items) == 1
    assert items[0].target_path.name == "My Paper.md"

    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=1
    )
    await jobs_module.run_job(job)

    assert items[0].status == "done"
    assert items[0].message == "markitdown"
    assert items[0].target_path.exists()
    # Original binary should NOT be kept by default.
    assert not items[0].target_path.with_suffix(".pdf").exists()


@pytest.mark.asyncio
async def test_docx_keep_original_keeps_binary(httpx_mock, tmp_path):
    httpx_mock.add_response(
        url="https://files.example.com/spec.docx",
        content=(CONVERSION_FIXTURES / "sample.docx").read_bytes(),
        headers={
            "content-type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        },
        status_code=200,
    )

    client = FakeClient(
        [
            FakeSource(
                id="s1",
                title="Spec",
                url="https://files.example.com/spec.docx",
                kind=SourceType.DOCX,
            )
        ]
    )
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["sources"], keep_original=True)
    job = jobs_module.BatchJob(
        job_id="j",
        notebook_id="nb1",
        target_dir=tmp_path,
        items=items,
        concurrency=1,
        keep_original=True,
    )
    await jobs_module.run_job(job)

    assert items[0].status == "done"
    md_path = items[0].target_path
    binary_path = md_path.with_suffix(".docx")
    assert md_path.exists()
    assert binary_path.exists()


@pytest.mark.asyncio
async def test_legacy_pdf_flag_uses_wkhtmltopdf_branch(monkeypatch, tmp_path):
    """When ``legacy_pdf=True``, the orchestrator builds a webpage_pdf runner.

    We only verify that the runner is *built* (target ends in ``.pdf``) and
    that running it without ``wkhtmltopdf`` fails with the expected error,
    matching the prior behavior.
    """
    monkeypatch.setattr("shutil.which", lambda _: None)

    client = FakeClient(
        [FakeSource(id="s1", title="Page", url="https://example.com", kind=SourceType.WEB_PAGE)]
    )
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["sources"], legacy_pdf=True)
    assert len(items) == 1
    assert items[0].target_path.name == "Page.pdf"

    job = jobs_module.BatchJob(
        job_id="j",
        notebook_id="nb1",
        target_dir=tmp_path,
        items=items,
        concurrency=1,
        legacy_pdf=True,
    )
    await jobs_module.run_job(job)
    # Without wkhtmltopdf installed, the legacy path errors out (preserves old behavior).
    assert items[0].status == "error"
    assert "wkhtmltopdf" in items[0].message


@pytest.mark.asyncio
async def test_csv_still_direct_downloaded(httpx_mock, tmp_path):
    """CSV sources should retain their .csv extension (not be markdown-ified)."""

    # We intercept the orchestrator's _download_url_sync via monkeypatch
    # so the test doesn't have to actually go to the network for CSV.

    def fake_download(url, target):
        Path(target).write_text("col1,col2\nv1,v2\n", encoding="utf-8")

    import notebooklm.web.jobs as _jobs_mod

    _jobs_mod._download_url_sync = fake_download

    client = FakeClient(
        [
            FakeSource(
                id="s1", title="data", url="https://files.example.com/data.csv", kind=SourceType.CSV
            )
        ]
    )
    items = await jobs_module.build_items(client, "nb1", tmp_path, ["sources"])
    assert items[0].target_path.suffix == ".csv"

    job = jobs_module.BatchJob(
        job_id="j", notebook_id="nb1", target_dir=tmp_path, items=items, concurrency=1
    )
    await jobs_module.run_job(job)
    assert items[0].status == "done"
