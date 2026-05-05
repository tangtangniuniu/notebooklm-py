"""Playwright-backed URL→Markdown strategy (final fallback).

Used by ``url_to_markdown`` when both ``markdown.new`` and the lightweight
``httpx`` fallback fail with status 403/429 (typically because the site is
behind Cloudflare's JS challenge or similar bot protection that no header
massage can defeat). Launches a real headless Chromium via Playwright,
navigates to the URL with stealth-ish defaults, waits for the page to settle,
captures the HTML, and reuses the local fallback's HTML→Markdown conversion.

Hard constraints (these exist because Chromium is heavy):

- A process-global ``asyncio.Semaphore(1)`` ensures at most ONE Chromium
  instance is alive at any moment. Without this, a job with 5 workers could
  spawn 5 browsers and balloon RAM by ~1 GB.
- Playwright is an optional dependency (``[browser]`` extra). If it's not
  installed the strategy raises ``ConversionDependencyError`` with a clear
  install hint; the dispatcher reports it as a terminal failure rather than
  attempting another tier.
- The strategy can be force-disabled via
  ``NOTEBOOKLM_DISABLE_BROWSER_FALLBACK=1`` or
  ``ConversionOptions(use_browser=False)``.
"""

from __future__ import annotations

import asyncio
import logging
from typing import Any

from ._errors import ConversionDependencyError, LocalConversionError
from ._fallback import _convert_html_to_markdown
from ._types import ConversionOptions

logger = logging.getLogger(__name__)

# Cap concurrent Chromium instances across the whole process. Hard-coded to 1
# on purpose: a single headless Chromium uses ~250–400 MB of RSS, and bumping
# this above 1 has been the difference between "slow" and "OOM-kills the
# whole machine" in user reports.
_MAX_CONCURRENT_BROWSERS = 1

# Default per-page wait budget. Most Cloudflare interstitials clear within
# 5–8 seconds; we wait up to this long for `networkidle` before giving up
# and snapshotting whatever's there.
_NAVIGATION_TIMEOUT_MS = 45_000
_NETWORK_IDLE_TIMEOUT_MS = 15_000

_BROWSER_SEM_LOCK = asyncio.Lock()
_browser_sem: asyncio.Semaphore | None = None


async def _get_browser_semaphore() -> asyncio.Semaphore:
    """Lazy, memoized process-global Chromium-instance gate.

    Lazy because the asyncio loop must already exist when the semaphore is
    constructed; memoization is guarded by a lock so two concurrent first
    callers don't each create their own.
    """
    global _browser_sem
    if _browser_sem is not None:
        return _browser_sem
    async with _BROWSER_SEM_LOCK:
        if _browser_sem is None:
            _browser_sem = asyncio.Semaphore(_MAX_CONCURRENT_BROWSERS)
    return _browser_sem


def _import_playwright() -> Any:
    """Import ``playwright.async_api.async_playwright`` lazily.

    Raises ``ConversionDependencyError`` if the optional ``[browser]`` extra
    isn't installed.
    """
    try:
        from playwright.async_api import async_playwright
    except ImportError as exc:  # pragma: no cover - exercised via dep tests
        raise ConversionDependencyError(
            "Playwright is required for the browser fallback. "
            "Install it via `pip install notebooklm-py[browser]` and run "
            "`playwright install chromium`."
        ) from exc
    return async_playwright


async def _capture_html(url: str, options: ConversionOptions) -> str:
    """Open ``url`` in headless Chromium and return the rendered HTML."""
    async_playwright = _import_playwright()

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-dev-shm-usage",
                "--no-sandbox",
            ],
            ignore_default_args=["--enable-automation"],
        )
        try:
            context = await browser.new_context(
                user_agent=options.effective_user_agent,
                viewport={"width": 1280, "height": 800},
                locale="en-US",
                java_script_enabled=True,
            )
            page = await context.new_page()
            try:
                await page.goto(
                    url,
                    wait_until="domcontentloaded",
                    timeout=_NAVIGATION_TIMEOUT_MS,
                )
                # Best-effort wait for the JS challenge / SPA hydration to
                # settle. We swallow timeouts here because some pages never
                # reach networkidle (long-poll widgets, analytics beacons),
                # and even the partial HTML is usually usable.
                try:
                    await page.wait_for_load_state("networkidle", timeout=_NETWORK_IDLE_TIMEOUT_MS)
                except Exception:  # noqa: BLE001 — networkidle is best-effort
                    logger.debug("networkidle not reached for %s; snapshotting anyway", url)

                html = await page.content()
            finally:
                await context.close()
        finally:
            await browser.close()

    return html


async def fetch_browser_markdown(url: str, options: ConversionOptions) -> str:
    """Render ``url`` in headless Chromium and return ``> Source: ...`` Markdown.

    Raises:
        ConversionDependencyError: ``[browser]`` extra not installed.
        LocalConversionError: navigation failure, oversized body, transport
            error, or any unhandled Playwright exception. Wrapped uniformly
            so the dispatcher can quote it in the final aggregate error.
    """
    sem = await _get_browser_semaphore()
    async with sem:
        try:
            html = await _capture_html(url, options)
        except ConversionDependencyError:
            raise
        except Exception as exc:  # noqa: BLE001 — Playwright raises a wide variety
            raise LocalConversionError(f"browser fallback failed for {url}: {exc}") from exc

    if len(html.encode("utf-8", errors="ignore")) > options.max_body_bytes:
        raise LocalConversionError(
            f"browser fallback body exceeded {options.max_body_bytes} bytes for {url}"
        )

    markdown = await _convert_html_to_markdown(html)
    return f"> Source: {url}\n\n{markdown}"
