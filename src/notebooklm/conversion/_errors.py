"""Exception hierarchy for the conversion package.

Three concrete subclasses give callers granular control:

- ``RemoteConversionError`` — raised by the remote (markdown.new) helper when
  its sanity check fails or the network call errors out. The dispatcher catches
  this internally to trigger the local fallback; orchestrator code never sees
  it directly.
- ``LocalConversionError`` — raised by the local fallback or the file-conversion
  helper when their work definitively fails. Surfaced to the orchestrator and
  treated as the item's terminal error.
- ``ConversionDependencyError`` — raised by lazy-import sites (``markitdown``,
  ``markdownify``) when the optional ``[markdown]`` extra is not installed.
"""

from __future__ import annotations


class ConversionError(Exception):
    """Base class for all conversion-package errors."""


class RemoteConversionError(ConversionError):
    """The markdown.new attempt failed sanity check or raised; trigger fallback.

    Caught by ``url_to_markdown`` and translated into a fallback attempt. Its
    message identifies the failure stage (status / body / network) so the
    eventual ``LocalConversionError`` can quote it when the fallback also fails.
    """


class LocalConversionError(ConversionError):
    """The local conversion path failed; surface to the caller as a terminal error."""


class ConversionDependencyError(ConversionError):
    """An optional dependency (``markitdown`` or ``markdownify``) is missing."""
