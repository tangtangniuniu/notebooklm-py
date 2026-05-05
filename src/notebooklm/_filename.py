"""Filesystem-safe filename utilities.

Sanitizes user-supplied titles into filesystem-safe names while preserving
CJK characters. Mirrors the algorithm used by `notebook_batch.py` so file
layouts produced by the legacy script and the new UI are compatible.
"""

from __future__ import annotations

import re

_UNSAFE_CHARS = re.compile(r"[^\w一-鿿\s.\-]")
_WHITESPACE = re.compile(r"\s+")


def sanitize_filename(name: str, max_length: int = 100) -> str:
    """Return a filesystem-safe version of `name`.

    Rules:
    - Keep alphanumerics, CJK ideographs (U+4E00..U+9FFF), spaces, dots, dashes, underscores.
    - Replace any other character with `_`.
    - Collapse runs of whitespace into single spaces.
    - Truncate to `max_length` characters (after sanitization).
    - Return `"untitled"` when the result would otherwise be empty.
    """
    if name is None:
        return "untitled"
    safe = _UNSAFE_CHARS.sub("_", str(name))
    safe = _WHITESPACE.sub(" ", safe).strip()
    if len(safe) > max_length:
        safe = safe[:max_length].rstrip()
    return safe or "untitled"
