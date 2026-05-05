"""Source-Markdown conversion package.

Public API:

- :func:`url_to_markdown` — convert a web URL to Markdown via ``markdown.new``
  with a local ``httpx`` + ``markdownify`` fallback.
- :func:`file_to_markdown` — convert a downloadable office file (PDF, DOCX,
  PPTX, …) to Markdown via ``markitdown``.
- :func:`source_to_markdown` — high-level dispatcher used by the batch
  orchestrator and the legacy ``notebook_batch.py`` script.

- :class:`ConversionOptions` — caller-tunable knobs (timeout, fallback policy,
  keep-original, custom UA, custom markdown.new base).
- :class:`ConversionResult` — outcome of a successful conversion (target,
  strategy, bytes written, duration).
- Exceptions: :class:`ConversionError`, :class:`RemoteConversionError`,
  :class:`LocalConversionError`, :class:`ConversionDependencyError`.

The optional ``markitdown`` and ``markdownify`` dependencies are imported
lazily inside the strategy functions; importing this package does not require
them. Install via ``pip install notebooklm-py[markdown]``.
"""

from __future__ import annotations

from ._dispatch import source_to_markdown
from ._errors import (
    ConversionDependencyError,
    ConversionError,
    LocalConversionError,
    RemoteConversionError,
)
from ._files import file_to_markdown
from ._types import (
    DEFAULT_MARKDOWN_NEW_BASE,
    DEFAULT_TIMEOUT,
    DEFAULT_USER_AGENT,
    ConversionOptions,
    ConversionResult,
    ConversionStrategy,
)
from ._url import url_to_markdown

__all__ = [
    # Public functions
    "url_to_markdown",
    "file_to_markdown",
    "source_to_markdown",
    # Public types
    "ConversionOptions",
    "ConversionResult",
    "ConversionStrategy",
    # Defaults (re-exported for callers that want to compose options)
    "DEFAULT_MARKDOWN_NEW_BASE",
    "DEFAULT_TIMEOUT",
    "DEFAULT_USER_AGENT",
    # Exceptions
    "ConversionError",
    "RemoteConversionError",
    "LocalConversionError",
    "ConversionDependencyError",
]
