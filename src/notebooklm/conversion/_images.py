"""Image-source passthrough helper.

`_pick_image_extension(url, content_type)` chooses a filename extension for
an image source download. It tries, in order:

1. The response ``Content-Type`` header (after stripping parameters and
   lowercasing). Mapped via the explicit ``_CONTENT_TYPE_EXT`` table below.
2. The URL path's extension, accepted only if it matches one of the
   *values* in the table — protecting against malicious / mistyped URLs
   that happen to end in ``.exe`` / ``.html`` / etc.
3. ``.png`` as the default fallback.

The function is pure (takes the Content-Type as a string, not the full
``httpx.Response``) so it's trivial to unit-test without HTTP fixtures.
"""

from __future__ import annotations

import os
from urllib.parse import urlparse

# Explicit MIME → extension table. Listed alphabetically for stable
# diff review. We deliberately don't use ``mimetypes.guess_extension``
# because its mapping varies by platform and can return surprising
# results (e.g. ``.jpe`` for JPEG on some systems).
_CONTENT_TYPE_EXT: dict[str, str] = {
    "image/avif": ".avif",
    "image/bmp": ".bmp",
    "image/gif": ".gif",
    "image/heic": ".heic",
    "image/jpeg": ".jpg",
    "image/jpg": ".jpg",
    "image/png": ".png",
    "image/svg+xml": ".svg",
    "image/tiff": ".tif",
    "image/webp": ".webp",
    "image/x-icon": ".ico",
}

# URL-path extensions we'll accept. Built from the table values plus the
# common alternative spellings (``.jpeg`` and ``.tiff``) that map to the
# same canonical extensions.
_KNOWN_URL_EXTS: frozenset[str] = frozenset(_CONTENT_TYPE_EXT.values()) | {".jpeg", ".tiff"}

# Default when neither sniff yields anything.
DEFAULT_IMAGE_EXTENSION = ".png"

# Strategy label surfaced on ConversionResult / SSE event payloads.
IMAGE_STRATEGY = "image"


def _pick_image_extension(url: str, content_type: str | None) -> str:
    """Pick a file extension for an image download.

    The Content-Type header wins when present and recognized; otherwise
    a known image extension on the URL path is used; otherwise the
    default ``.png`` is returned.
    """
    if content_type:
        # Strip parameters like "; charset=utf-8" and lowercase.
        primary = content_type.split(";", 1)[0].strip().lower()
        ext = _CONTENT_TYPE_EXT.get(primary)
        if ext is not None:
            return ext

    # Fall back to URL path inspection. We accept the trailing extension
    # only if it's a known image extension — this guards against URLs
    # that happen to end in ``.exe`` / ``.html`` / similar.
    path = urlparse(url).path
    _, ext = os.path.splitext(path)
    if ext:
        candidate = ext.lower()
        if candidate in _KNOWN_URL_EXTS:
            # Normalize spelling variants to their canonical form.
            if candidate == ".jpeg":
                return ".jpg"
            if candidate == ".tiff":
                return ".tif"
            return candidate

    return DEFAULT_IMAGE_EXTENSION


def known_image_extensions() -> frozenset[str]:
    """Return the set of canonical image extensions the helper can produce.

    Used by the orchestrator's pre-skip check to decide whether a sibling
    file already exists for an image source (`<title>.<any-known-ext>`).
    """
    return frozenset(_CONTENT_TYPE_EXT.values())
