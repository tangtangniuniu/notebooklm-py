"""Internal types for the source-markdown-conversion capability.

`ConversionOptions` captures caller-tunable knobs (timeout, fallback policy,
keep-original toggle, custom UA, custom markdown.new base). `ConversionResult`
reports the strategy that ran plus basic metrics for SSE / log surfacing.

Both dataclasses are frozen and slotted so they're cheap to pass around and
trivially picklable; the public API in ``notebooklm.conversion`` re-exports
them, so callers never need to import this private module directly.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Literal

#: Default browser-like User-Agent for the local fallback. Overridable via
#: ``ConversionOptions.user_agent`` or the ``NOTEBOOKLM_CONVERSION_UA`` env var.
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "notebooklm-py/0.3 Chrome/120.0.0.0 Safari/537.36"
)

#: Default markdown.new base. Overridable via ``ConversionOptions.markdown_new_base``
#: or the ``NOTEBOOKLM_MARKDOWN_NEW_BASE`` env var.
DEFAULT_MARKDOWN_NEW_BASE = "https://markdown.new/"

#: Default per-request timeout (seconds) for both remote and local fetches.
DEFAULT_TIMEOUT = 30.0

#: Default response-body cap. Protects the event loop from a single oversized
#: page (typically a sitemap, image listing, or scraping attempt) that would
#: pin a worker on markdownify for tens of seconds. Overridable via
#: ``ConversionOptions.max_body_bytes`` or the ``NOTEBOOKLM_CONVERSION_MAX_BODY``
#: env var (bytes).
DEFAULT_MAX_BODY_BYTES = 10 * 1024 * 1024  # 10 MiB

#: Strategy enumeration surfaced on `ConversionResult.strategy`.
ConversionStrategy = Literal[
    "remote",  # markdown.new succeeded
    "fallback",  # local httpx + HTML→MD path ran
    "browser",  # headless Chromium (Playwright) + HTML→MD path ran
    "markitdown",  # binary office file converted via markitdown
    "fulltext",  # client.sources.get_fulltext path (orchestrator-level)
    "passthrough",  # source already markdown / pasted text (orchestrator-level)
    "legacy-pdf",  # opt-in wkhtmltopdf path (orchestrator-level)
]


@dataclass(frozen=True, slots=True)
class ConversionOptions:
    """Tunable knobs for a single conversion call.

    Defaults match the behavior the design specifies. Callers normally either
    construct an empty ``ConversionOptions()`` (use defaults) or call
    ``ConversionOptions.from_env(...)`` to pick up deployment-wide overrides.
    """

    timeout: float = DEFAULT_TIMEOUT
    use_remote: bool = True
    use_browser: bool = True
    keep_original: bool = False
    user_agent: str | None = None
    markdown_new_base: str = DEFAULT_MARKDOWN_NEW_BASE
    max_body_bytes: int = DEFAULT_MAX_BODY_BYTES

    @classmethod
    def from_env(cls, **overrides: object) -> ConversionOptions:
        """Build options from env vars, with explicit kwargs winning.

        Env var contract (see design D6):
        - ``NOTEBOOKLM_MARKDOWN_NEW_BASE`` → ``markdown_new_base``
        - ``NOTEBOOKLM_DISABLE_MARKDOWN_NEW=1`` → forces ``use_remote=False``
        - ``NOTEBOOKLM_DISABLE_BROWSER_FALLBACK=1`` → forces ``use_browser=False``
        - ``NOTEBOOKLM_CONVERSION_TIMEOUT`` (float seconds) → ``timeout``
        - ``NOTEBOOKLM_CONVERSION_UA`` → ``user_agent``
        - ``NOTEBOOKLM_CONVERSION_MAX_BODY`` (int bytes) → ``max_body_bytes``
        """
        base = os.environ.get("NOTEBOOKLM_MARKDOWN_NEW_BASE", DEFAULT_MARKDOWN_NEW_BASE)
        disable_remote = os.environ.get("NOTEBOOKLM_DISABLE_MARKDOWN_NEW", "").strip() == "1"
        disable_browser = os.environ.get("NOTEBOOKLM_DISABLE_BROWSER_FALLBACK", "").strip() == "1"
        timeout_raw = os.environ.get("NOTEBOOKLM_CONVERSION_TIMEOUT")
        try:
            timeout = float(timeout_raw) if timeout_raw else DEFAULT_TIMEOUT
        except ValueError:
            timeout = DEFAULT_TIMEOUT
        max_body_raw = os.environ.get("NOTEBOOKLM_CONVERSION_MAX_BODY")
        try:
            max_body_bytes = int(max_body_raw) if max_body_raw else DEFAULT_MAX_BODY_BYTES
        except ValueError:
            max_body_bytes = DEFAULT_MAX_BODY_BYTES
        ua = os.environ.get("NOTEBOOKLM_CONVERSION_UA") or None

        opts = cls(
            timeout=timeout,
            use_remote=not disable_remote,
            use_browser=not disable_browser,
            keep_original=False,
            user_agent=ua,
            markdown_new_base=base,
            max_body_bytes=max_body_bytes,
        )
        if overrides:
            # ``replace`` validates field names for us, raising TypeError on typos.
            return replace(opts, **overrides)  # type: ignore[arg-type]
        return opts

    @property
    def effective_user_agent(self) -> str:
        """Resolved User-Agent (option override → env override → default)."""
        return self.user_agent or DEFAULT_USER_AGENT


@dataclass(frozen=True, slots=True)
class ConversionResult:
    """The outcome of a successful conversion.

    Surfaced by every public conversion function and by the orchestrator's
    SSE ``event: item`` payload.
    """

    target: Path
    strategy: ConversionStrategy
    bytes_written: int
    duration_ms: int
    slash_retried: bool = False
