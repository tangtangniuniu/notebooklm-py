"""Local web UI for NotebookLM.

This package powers `notebooklm ui` — a FastAPI server that serves a browser
UI over the existing async client. It is gated behind the `[ui]` install extra.

Direct imports of submodules will fail with a clear, actionable ImportError if
the optional dependencies are missing.
"""

from __future__ import annotations

_INSTALL_HINT = "notebooklm ui requires the [ui] extra. Install with: pip install notebooklm-py[ui]"


def _require_ui_deps() -> None:
    """Raise ImportError with install hint if web dependencies are missing."""
    missing: list[str] = []
    try:
        import fastapi  # noqa: F401
    except ImportError:
        missing.append("fastapi")
    try:
        import uvicorn  # noqa: F401
    except ImportError:
        missing.append("uvicorn")
    try:
        import jinja2  # noqa: F401
    except ImportError:
        missing.append("jinja2")
    try:
        import sse_starlette  # noqa: F401
    except ImportError:
        missing.append("sse-starlette")

    if missing:
        raise ImportError(f"{_INSTALL_HINT} (missing: {', '.join(missing)})")


_require_ui_deps()


def create_app(*args, **kwargs):
    """Lazy import shim — see `web.app.create_app`."""
    from .app import create_app as _impl

    return _impl(*args, **kwargs)


__all__ = ["create_app", "_INSTALL_HINT"]
