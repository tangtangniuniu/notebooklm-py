"""URL→Markdown dispatcher (remote primary, local fallback, browser last resort).

``url_to_markdown(url, target, *, options)`` is the public entry point that
the orchestrator calls for ``WEB_PAGE`` sources. It:

1. Attempts the remote ``markdown.new`` strategy when ``options.use_remote``
   is True (and the env override permits it). Failures raise
   ``RemoteConversionError`` internally and are caught here.
2. On remote failure, attempts the local fallback (``httpx`` + ``markdownify``).
3. On local failure, attempts the headless-browser fallback (Playwright)
   when ``options.use_browser`` is True and the optional dependency is
   installed. This is the only strategy that defeats Cloudflare's JS
   challenge. Process-globally rate-limited to one Chromium at a time.
4. Writes the resulting Markdown to ``target`` via a temp-file rename.
5. Returns a ``ConversionResult`` describing which strategy ran.

If every enabled strategy fails, raises ``LocalConversionError`` whose message
mentions each failure cause so the orchestrator can surface it cleanly in the
SSE ``event: item`` payload.
"""

from __future__ import annotations

import logging
import os
import time
from pathlib import Path

from ._browser import fetch_browser_markdown
from ._errors import (
    ConversionDependencyError,
    LocalConversionError,
    RemoteConversionError,
)
from ._fallback import fetch_local_markdown
from ._remote import fetch_remote_markdown
from ._types import ConversionOptions, ConversionResult

logger = logging.getLogger(__name__)


def _atomic_write(target: Path, content: str) -> int:
    """Write ``content`` to ``target`` via a temp-file rename.

    Creates parent dirs as needed. Returns the number of bytes written.
    """
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(target.suffix + ".tmp")
    encoded = content.encode("utf-8")
    try:
        tmp.write_bytes(encoded)
        tmp.replace(target)
    except Exception:
        tmp.unlink(missing_ok=True)
        raise
    return len(encoded)


def _remote_disabled_by_env() -> bool:
    return os.environ.get("NOTEBOOKLM_DISABLE_MARKDOWN_NEW", "").strip() == "1"


def _browser_disabled_by_env() -> bool:
    return os.environ.get("NOTEBOOKLM_DISABLE_BROWSER_FALLBACK", "").strip() == "1"


async def url_to_markdown(
    url: str,
    target: Path,
    *,
    options: ConversionOptions | None = None,
) -> ConversionResult:
    """Convert ``url`` to Markdown and write it to ``target``.

    Tries (in order): markdown.new → local httpx → headless Chromium. Each
    tier can be disabled via options or env vars.
    """
    opts = options or ConversionOptions()
    started = time.monotonic()
    use_remote = opts.use_remote and not _remote_disabled_by_env()
    use_browser = opts.use_browser and not _browser_disabled_by_env()

    remote_error: RemoteConversionError | None = None
    local_error: LocalConversionError | None = None
    body: str | None = None
    strategy: str
    retried = False

    if use_remote:
        try:
            body, retried = await fetch_remote_markdown(url, opts)
            strategy = "remote"
        except RemoteConversionError as exc:
            logger.debug("markdown.new failed for %s; falling back: %s", url, exc)
            remote_error = exc

    if body is None:
        try:
            body, retried = await fetch_local_markdown(url, opts)
            strategy = "fallback"
        except LocalConversionError as exc:
            logger.debug("local fallback failed for %s: %s", url, exc)
            local_error = exc

    if body is None and use_browser:
        try:
            body = await fetch_browser_markdown(url, opts)
            strategy = "browser"
            # Browser path doesn't slash-retry — the URL we render is whatever
            # the user passed; renormalization is the site's job at that point.
            retried = False
        except ConversionDependencyError as exc:
            # No Playwright installed — surface as a hint inside the aggregate
            # error so the user knows the fallback exists but isn't enabled.
            logger.debug("browser fallback unavailable for %s: %s", url, exc)
            local_error = local_error or LocalConversionError(str(exc))
        except LocalConversionError as exc:
            logger.debug("browser fallback failed for %s: %s", url, exc)
            local_error = exc

    if body is None:
        # Build a concise, deterministic aggregate error so the SSE consumer
        # can show all the causes the user might want to see.
        parts: list[str] = []
        if remote_error is not None:
            parts.append(f"remote={remote_error}")
        if local_error is not None:
            parts.append(f"local={local_error}")
        detail = "; ".join(parts) if parts else "no strategy attempted"
        raise LocalConversionError(f"all conversion strategies failed for {url}: {detail}")

    bytes_written = _atomic_write(target, body)
    duration_ms = max(int((time.monotonic() - started) * 1000), 1)
    return ConversionResult(
        target=target,
        strategy=strategy,  # type: ignore[arg-type]
        bytes_written=bytes_written,
        duration_ms=duration_ms,
        slash_retried=retried,
    )
