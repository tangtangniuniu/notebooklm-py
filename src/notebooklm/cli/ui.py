"""`notebooklm ui` — start the local web UI server."""

from __future__ import annotations

import socket
import sys
import threading
import time
import webbrowser

import click

DEFAULT_PORT = 8765
PORT_PROBE_WINDOW = 11  # 8765..8775 inclusive


def _try_bind(host: str, port: int) -> bool:
    """Return True if `host:port` is bindable right now."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((host, port))
        return True
    except OSError:
        return False


def _pick_port(host: str, requested: int | None) -> int | None:
    if requested is not None:
        return requested if _try_bind(host, requested) else None
    for offset in range(PORT_PROBE_WINDOW):
        port = DEFAULT_PORT + offset
        if _try_bind(host, port):
            return port
    return None


@click.command("ui")
@click.option("--port", type=int, default=None, help="Port (default: probe 8765–8775).")
@click.option(
    "--host",
    default="127.0.0.1",
    show_default=True,
    help="Bind address. Loopback only; non-loopback addresses are refused.",
)
@click.option("--no-browser", is_flag=True, help="Do not auto-open a browser.")
def ui_command(port: int | None, host: str, no_browser: bool):
    """Launch the local NotebookLM UI in the default browser."""

    if host not in {"127.0.0.1", "localhost", "::1"}:
        click.echo(f"Refusing to bind {host!r}: UI must run on loopback only.", err=True)
        sys.exit(2)

    try:
        from notebooklm.web import create_app
    except ImportError as e:
        click.echo(str(e), err=True)
        sys.exit(1)

    chosen = _pick_port(host, port)
    if chosen is None:
        if port is not None:
            click.echo(f"Port {port} is busy.", err=True)
        else:
            click.echo(
                f"No free port in {DEFAULT_PORT}-{DEFAULT_PORT + PORT_PROBE_WINDOW - 1}; "
                "specify --port",
                err=True,
            )
        sys.exit(1)

    url = f"http://{host}:{chosen}"
    click.echo(f"Serving NotebookLM UI at {url}")

    if not no_browser:
        # Delay slightly so the server has a chance to bind before the
        # browser opens.
        def _open_later() -> None:
            time.sleep(0.6)
            try:
                webbrowser.open(url)
            except Exception:
                pass

        threading.Thread(target=_open_later, daemon=True).start()

    import uvicorn

    app = create_app()
    uvicorn.run(app, host=host, port=chosen, log_level="warning", access_log=False)
