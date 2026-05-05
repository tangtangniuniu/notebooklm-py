"""Pytest fixtures shared across conversion tests."""

from __future__ import annotations

from pathlib import Path

import pytest


@pytest.fixture
def tmp_target(tmp_path: Path) -> Path:
    """Caller-controlled output path inside an empty tmp directory."""
    return tmp_path / "out" / "page.md"


@pytest.fixture(autouse=True)
def _clear_conversion_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """Strip every env var the conversion module observes before each test.

    Tests opt in to specific values via ``monkeypatch.setenv``; this keeps
    them isolated from a developer's actual environment.
    """
    for var in (
        "NOTEBOOKLM_MARKDOWN_NEW_BASE",
        "NOTEBOOKLM_DISABLE_MARKDOWN_NEW",
        "NOTEBOOKLM_CONVERSION_TIMEOUT",
        "NOTEBOOKLM_CONVERSION_UA",
    ):
        monkeypatch.delenv(var, raising=False)
