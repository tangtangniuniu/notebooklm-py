"""Smoke tests for notebook_batch.py CLI flag plumbing."""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

import pytest

# Add the project root to sys.path so we can import notebook_batch.py.
_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))


@pytest.fixture
def batch():
    """Re-import notebook_batch fresh per-test."""
    if "notebook_batch" in sys.modules:
        del sys.modules["notebook_batch"]
    return importlib.import_module("notebook_batch")


def test_argparse_exposes_keep_original_and_legacy_pdf(batch, capsys):
    """The ``source-download`` subparser must expose both new flags."""
    # We rely on the script's help output; argparse parsers are constructed
    # inside ``main()`` so calling them directly would duplicate the wiring.
    import subprocess

    result = subprocess.run(
        [sys.executable, str(_ROOT / "notebook_batch.py"), "source-download", "--help"],
        capture_output=True,
        text=True,
    )
    assert "--keep-original" in result.stdout
    assert "--legacy-pdf" in result.stdout


def test_run_markdown_conversion_maps_source_kinds(batch, tmp_path, monkeypatch):
    """Verify ``_run_markdown_conversion`` translates CLI strings → SourceType."""
    from notebooklm.types import SourceType

    captured: dict = {}

    async def fake_source_to_markdown(url, kind, target, *, options):
        captured["url"] = url
        captured["kind"] = kind
        captured["keep_original"] = options.keep_original
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("# stub", encoding="utf-8")

        from notebooklm.conversion import ConversionResult

        return ConversionResult(
            target=target, strategy="markitdown", bytes_written=8, duration_ms=1
        )

    monkeypatch.setattr(batch, "_run_markdown_conversion", batch._run_markdown_conversion)

    # Inject the fake into the conversion module's namespace before the
    # batch's helper imports it.
    import notebooklm.conversion as _conversion

    monkeypatch.setattr(_conversion, "source_to_markdown", fake_source_to_markdown)

    target = tmp_path / "out.md"
    strategy = batch._run_markdown_conversion(
        "https://example.com/file.pdf",
        "SourceType.PDF",
        target,
        keep_original=True,
    )
    assert strategy == "markitdown"
    assert captured["url"] == "https://example.com/file.pdf"
    assert captured["kind"] == SourceType.PDF
    assert captured["keep_original"] is True


def test_run_markdown_conversion_rejects_unknown_kind(batch, tmp_path):
    target = tmp_path / "out.md"
    with pytest.raises(RuntimeError, match="unsupported source kind"):
        batch._run_markdown_conversion(
            "https://example.com",
            "SourceType.YOUTUBE",
            target,
            keep_original=False,
        )


def test_download_image_source_picks_extension_from_content_type(batch, tmp_path, monkeypatch):
    """The image branch should sniff Content-Type and write the right file."""
    import httpx

    captured: dict = {}

    class _FakeResponse:
        def __init__(self):
            self.status_code = 200
            self.headers = {"content-type": "image/png"}
            self.extensions: dict = {}

        def iter_bytes(self):
            yield b"fake-png-bytes" * 64

    class _FakeClient:
        def __init__(self, **kwargs):
            captured.update(kwargs)

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def request(self, method, url, **kwargs):
            captured["method"] = method
            captured["url"] = url
            return _FakeResponse()

    monkeypatch.setattr(httpx, "Client", _FakeClient)

    final, status, retried = batch._download_image_source(
        "https://cdn.example/cover", tmp_path, "Cover"
    )
    assert status == "done"
    assert retried is False
    assert final.name == "Cover.png"
    assert final.read_bytes() == b"fake-png-bytes" * 64


def test_download_image_source_skips_when_sibling_exists(batch, tmp_path):
    """An existing `<title>.<known-image-ext>` sibling should short-circuit."""
    existing = tmp_path / "Cover.jpg"
    existing.write_bytes(b"already there")

    final, status, retried = batch._download_image_source(
        "https://cdn.example/cover", tmp_path, "Cover"
    )
    assert status == "skipped"
    assert retried is False
    assert final == existing
    assert existing.read_bytes() == b"already there"


# ---------------------------------------------------------------- concurrency


def test_concurrency_flag_accepts_in_range(batch):
    import subprocess

    for n in (1, 5, 10):
        result = subprocess.run(
            [
                sys.executable,
                str(_ROOT / "notebook_batch.py"),
                "source-download",
                f"--concurrency={n}",
                "--help",
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"--concurrency={n} should be accepted"


def test_concurrency_flag_rejects_out_of_range(batch):
    import subprocess

    for n in (0, 11, -1, 100):
        result = subprocess.run(
            [
                sys.executable,
                str(_ROOT / "notebook_batch.py"),
                "source-download",
                f"--concurrency={n}",
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0, f"--concurrency={n} should be rejected"
        assert "concurrency" in (result.stderr + result.stdout).lower()


def test_concurrency_flag_rejects_non_integer(batch):
    import subprocess

    result = subprocess.run(
        [
            sys.executable,
            str(_ROOT / "notebook_batch.py"),
            "source-download",
            "--concurrency=abc",
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "integer" in (result.stderr + result.stdout).lower()
