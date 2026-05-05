"""Tests for ``notebooklm.conversion._browser``.

The Playwright-driven path itself can't be exercised in unit tests (it
needs a real browser binary and network egress), so we test only what we
can deterministically pin:

- The ``ConversionDependencyError`` raised when ``playwright`` is missing.
- The integration with ``url_to_markdown`` when both upstream tiers fail.
- The env-var / option toggles that disable the strategy.

End-to-end "actually launches Chromium" coverage lives in the e2e suite.
"""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path

import pytest

from notebooklm.conversion import (
    ConversionDependencyError,
    ConversionOptions,
    LocalConversionError,
    url_to_markdown,
)
from notebooklm.conversion._browser import fetch_browser_markdown


@pytest.fixture
def target(tmp_path: Path) -> Path:
    return tmp_path / "out" / "page.md"


# --------------------------------------------------- missing optional dependency


@pytest.mark.asyncio
async def test_missing_playwright_raises_dependency_error(monkeypatch):
    """Simulate ``playwright`` not being installed."""
    # Hide both the top-level package and the submodule the strategy imports.
    monkeypatch.setitem(sys.modules, "playwright", None)
    monkeypatch.setitem(sys.modules, "playwright.async_api", None)
    with pytest.raises(ConversionDependencyError, match="Playwright"):
        await fetch_browser_markdown("https://example.com", ConversionOptions())


# ------------------------------------- env / option flags disable browser tier


@pytest.mark.asyncio
async def test_env_disables_browser_fallback(httpx_mock, target, monkeypatch):
    """``NOTEBOOKLM_DISABLE_BROWSER_FALLBACK=1`` should keep Playwright untouched.

    We assert it by failing both prior tiers and verifying that the dispatcher
    raises *without* attempting to import playwright (the env flag short-circuits
    earlier than the dependency check).
    """
    monkeypatch.setenv("NOTEBOOKLM_DISABLE_BROWSER_FALLBACK", "1")
    # If the env flag fails to short-circuit, the missing-import will produce
    # ConversionDependencyError instead of LocalConversionError. So we hide
    # playwright too and assert we never see that error class.
    monkeypatch.setitem(sys.modules, "playwright", None)
    monkeypatch.setitem(sys.modules, "playwright.async_api", None)

    # Both upstream tiers fail. The remote URL has a non-empty path
    # (``/https://example.com``), so its slash-retry fires once. The local
    # original URL has an empty path, so no slash-retry.
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com",
        status_code=403,
        text="cf challenge " * 10,
    )
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com/",
        status_code=403,
        text="cf challenge " * 10,
    )
    httpx_mock.add_response(
        url="https://example.com",
        status_code=403,
        text="cf challenge " * 10,
    )

    with pytest.raises(LocalConversionError) as exc_info:
        await url_to_markdown("https://example.com", target)

    msg = str(exc_info.value)
    # Should NOT mention Playwright — the env flag stopped us before the import.
    assert "Playwright" not in msg
    assert "remote=" in msg
    assert "local=" in msg


@pytest.mark.asyncio
async def test_option_disables_browser_fallback(httpx_mock, target, monkeypatch):
    """``ConversionOptions(use_browser=False)`` should also short-circuit."""
    monkeypatch.setitem(sys.modules, "playwright", None)
    monkeypatch.setitem(sys.modules, "playwright.async_api", None)

    httpx_mock.add_response(
        url="https://markdown.new/https://example.com",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com/",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://example.com",
        status_code=403,
    )

    options = ConversionOptions(use_browser=False)
    with pytest.raises(LocalConversionError) as exc_info:
        await url_to_markdown("https://example.com", target, options=options)
    assert "Playwright" not in str(exc_info.value)


# ------------------------------------------- dispatcher invokes browser tier


@pytest.mark.asyncio
async def test_browser_strategy_invoked_when_first_two_tiers_fail(httpx_mock, target, monkeypatch):
    """When remote + local both fail, the dispatcher should call the browser tier.

    We monkeypatch ``fetch_browser_markdown`` to a stub so the test stays
    hermetic (no real Chromium launch). The test verifies the dispatcher
    routes to it AND records ``strategy='browser'`` in the result.
    """
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com/article",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://markdown.new/https://example.com/article/",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://example.com/article",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://example.com/article/",
        status_code=403,
    )

    seen: list[str] = []

    async def _stub(url, options):  # noqa: ARG001 — signature must match
        seen.append(url)
        return (
            f"> Source: {url}\n\n# Rendered\n\nReal content extracted by the headless browser tier."
        )

    monkeypatch.setattr(
        "notebooklm.conversion._url.fetch_browser_markdown",
        _stub,
    )

    result = await url_to_markdown("https://example.com/article", target)
    assert result.strategy == "browser"
    assert seen == ["https://example.com/article"]
    assert target.read_text(encoding="utf-8").startswith("> Source:")
    assert "# Rendered" in target.read_text(encoding="utf-8")


# ----------------------------------------------- semaphore caps Chromium count


@pytest.mark.asyncio
async def test_browser_semaphore_serializes_calls(monkeypatch):
    """The process-global Chromium-instance gate should serialize concurrent calls.

    A bug here means a 5-worker job spawns 5 Chromium processes and OOM-kills
    the host — exactly the regression we're guarding against.
    """
    # Force a fresh semaphore so this test is order-independent.
    import notebooklm.conversion._browser as _b

    monkeypatch.setattr(_b, "_browser_sem", None)

    in_flight = 0
    peak = 0
    lock = asyncio.Lock()

    async def _stub_capture(url, options):  # noqa: ARG001
        nonlocal in_flight, peak
        async with lock:
            in_flight += 1
            peak = max(peak, in_flight)
        await asyncio.sleep(0.05)
        async with lock:
            in_flight -= 1
        # Return enough HTML that the size cap doesn't fire.
        return "<html><body><h1>Hi</h1>" + ("x" * 200) + "</body></html>"

    monkeypatch.setattr(_b, "_capture_html", _stub_capture)

    await asyncio.gather(
        *(
            fetch_browser_markdown(f"https://example.com/p{i}", ConversionOptions())
            for i in range(4)
        )
    )
    assert peak == 1, f"expected single Chromium at a time; saw peak={peak}"
