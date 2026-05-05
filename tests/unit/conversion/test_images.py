"""Tests for ``notebooklm.conversion._images``."""

from __future__ import annotations

import pytest

from notebooklm.conversion._images import (
    DEFAULT_IMAGE_EXTENSION,
    _pick_image_extension,
    known_image_extensions,
)


@pytest.mark.parametrize(
    "content_type,expected",
    [
        ("image/jpeg", ".jpg"),
        ("image/jpg", ".jpg"),
        ("image/png", ".png"),
        ("image/gif", ".gif"),
        ("image/webp", ".webp"),
        ("image/svg+xml", ".svg"),
        ("image/bmp", ".bmp"),
        ("image/tiff", ".tif"),
        ("image/x-icon", ".ico"),
        ("image/heic", ".heic"),
        ("image/avif", ".avif"),
    ],
)
def test_content_type_table(content_type, expected):
    assert _pick_image_extension("https://x.example/file", content_type) == expected


def test_content_type_case_insensitive():
    assert _pick_image_extension("https://x.example/file", "IMAGE/PNG") == ".png"


def test_content_type_strips_parameters():
    assert _pick_image_extension("https://x.example/file", "image/jpeg; charset=utf-8") == ".jpg"


def test_content_type_unknown_falls_back_to_url_path():
    # Content-Type unknown but URL path has a recognized image extension.
    assert _pick_image_extension("https://x.example/cover.PNG", "image/x-foo") == ".png"


def test_url_path_extension_used_when_content_type_missing():
    assert _pick_image_extension("https://x.example/cover.jpg", None) == ".jpg"
    assert _pick_image_extension("https://x.example/cover.JPEG", None) == ".jpg"
    assert _pick_image_extension("https://x.example/cover.tiff", None) == ".tif"


def test_url_path_rejects_non_image_extensions():
    # An adversarial URL ending in .exe must NOT propagate to the filename.
    assert _pick_image_extension("https://x.example/payload.exe", None) == DEFAULT_IMAGE_EXTENSION
    assert _pick_image_extension("https://x.example/index.html", None) == DEFAULT_IMAGE_EXTENSION


def test_default_fallback_when_both_miss():
    # CDN-style URL with no extension and no Content-Type.
    assert _pick_image_extension("https://cdn.example/i?id=abc", None) == DEFAULT_IMAGE_EXTENSION
    assert _pick_image_extension("https://cdn.example/i?id=abc", "") == DEFAULT_IMAGE_EXTENSION


def test_malformed_content_type_does_not_crash():
    # Should treat as missing and fall through to URL path / default.
    assert _pick_image_extension("https://x.example/cover.png", "garbage") == ".png"
    assert _pick_image_extension("https://x.example/", ";;;") == DEFAULT_IMAGE_EXTENSION


def test_known_image_extensions_includes_common_formats():
    exts = known_image_extensions()
    for required in (".jpg", ".png", ".gif", ".webp", ".svg"):
        assert required in exts, f"{required} should be in known set"
