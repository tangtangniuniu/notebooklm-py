"""Single-file launcher for the NotebookLM Web UI.

This is the entry point Nuitka compiles into a standalone binary.
It boots the FastAPI app via uvicorn, finds a free local port, and opens the
default browser.

Limitations of the compiled binary:
    - Authentication is NOT bundled. The binary expects a valid
      `~/.notebooklm/storage_state.json` from a prior `notebooklm login`.
      First-time setup still needs a regular Python install with the
      [browser] extra (Playwright cannot be reliably packaged into a
      single-file binary).
    - The binary serves the UI only — none of the CLI subcommands.
"""

from __future__ import annotations

import os
import socket
import sys
import threading
import time
import webbrowser
from pathlib import Path

DEFAULT_PORT = 8765
PROBE_WINDOW = 11  # 8765..8775


def _try_bind(host: str, port: int) -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((host, port))
        return True
    except OSError:
        return False


def _pick_port(host: str, requested: int | None) -> int | None:
    if requested:
        return requested if _try_bind(host, requested) else None
    for offset in range(PROBE_WINDOW):
        port = DEFAULT_PORT + offset
        if _try_bind(host, port):
            return port
    return None


def _parse_args(argv: list[str]) -> dict:
    """Tiny arg parser — avoids Click overhead in the compiled binary."""
    opts = {"host": "127.0.0.1", "port": None, "no_browser": False}
    it = iter(argv)
    for tok in it:
        if tok in ("-h", "--help"):
            print(
                "Usage: notebooklm-ui [--port N] [--host 127.0.0.1] [--no-browser]\n"
                "\n"
                "Launches the NotebookLM Web UI (single-file build).\n"
                "Bind defaults to 127.0.0.1; non-loopback hosts are refused."
            )
            sys.exit(0)
        elif tok == "--port":
            opts["port"] = int(next(it))
        elif tok.startswith("--port="):
            opts["port"] = int(tok.split("=", 1)[1])
        elif tok == "--host":
            opts["host"] = next(it)
        elif tok.startswith("--host="):
            opts["host"] = tok.split("=", 1)[1]
        elif tok == "--no-browser":
            opts["no_browser"] = True
        else:
            print(f"Unknown argument: {tok}", file=sys.stderr)
            sys.exit(2)
    return opts


def _print_auth_hint() -> None:
    """Print a friendly hint when storage_state.json is missing."""
    home = Path(os.environ.get("NOTEBOOKLM_HOME", str(Path.home() / ".notebooklm")))
    storage = home / "storage_state.json"
    if storage.exists():
        return
    print()
    print("=" * 70)
    print(" 未检测到 NotebookLM 认证信息（First-time setup required）")
    print("=" * 70)
    print(f"  期望位置 / Expected at: {storage}")
    print()
    print("  本单文件版本不内置 Playwright，需要先用 pip 版完成首次登录：")
    print("  This binary doesn't bundle Playwright; do first-time login with the")
    print("  pip-installed CLI:")
    print()
    print("    pip install 'notebooklm-py[browser]'")
    print("    playwright install chromium")
    print("    notebooklm login")
    print()
    print("  完成后再次运行本程序即可。UI 仍会启动，但所有需要认证的操作")
    print("  会在页面顶部显示红色横幅，直到登录完成。")
    print("=" * 70)
    print()


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    opts = _parse_args(argv)

    if opts["host"] not in {"127.0.0.1", "localhost", "::1"}:
        print(f"Refusing to bind {opts['host']!r}: UI must run on loopback only.", file=sys.stderr)
        return 2

    chosen = _pick_port(opts["host"], opts["port"])
    if chosen is None:
        if opts["port"]:
            print(f"Port {opts['port']} is busy.", file=sys.stderr)
        else:
            print(
                f"No free port in {DEFAULT_PORT}-{DEFAULT_PORT + PROBE_WINDOW - 1};"
                " specify --port",
                file=sys.stderr,
            )
        return 1

    _print_auth_hint()

    url = f"http://{opts['host']}:{chosen}"
    print(f"Serving NotebookLM UI at {url}")
    print("Press Ctrl+C to stop.")

    if not opts["no_browser"]:
        def _open_later() -> None:
            time.sleep(0.6)
            try:
                webbrowser.open(url)
            except Exception:
                pass

        threading.Thread(target=_open_later, daemon=True).start()

    # Imports kept inside main so the auth hint is printed even if a
    # dependency is somehow missing (rare in a Nuitka build, but defensive).
    import uvicorn

    from notebooklm.web import create_app

    app = create_app()
    uvicorn.run(app, host=opts["host"], port=chosen, log_level="warning", access_log=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
