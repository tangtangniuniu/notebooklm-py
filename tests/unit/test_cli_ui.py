"""Unit tests for `notebooklm ui` CLI command."""

from __future__ import annotations

from unittest.mock import patch

from click.testing import CliRunner

from notebooklm.cli.ui import _pick_port, ui_command


def test_pick_port_uses_explicit_port_when_free():
    with patch("notebooklm.cli.ui._try_bind", return_value=True):
        assert _pick_port("127.0.0.1", 9000) == 9000


def test_pick_port_returns_none_when_explicit_port_busy():
    with patch("notebooklm.cli.ui._try_bind", return_value=False):
        assert _pick_port("127.0.0.1", 9000) is None


def test_pick_port_probes_default_window():
    calls: list[int] = []

    def fake_bind(_host: str, port: int) -> bool:
        calls.append(port)
        return port == 8770

    with patch("notebooklm.cli.ui._try_bind", side_effect=fake_bind):
        assert _pick_port("127.0.0.1", None) == 8770
    # Probed in order until 8770.
    assert calls == [8765, 8766, 8767, 8768, 8769, 8770]


def test_pick_port_returns_none_when_window_exhausted():
    with patch("notebooklm.cli.ui._try_bind", return_value=False):
        assert _pick_port("127.0.0.1", None) is None


def test_ui_refuses_non_loopback_host():
    runner = CliRunner()
    r = runner.invoke(ui_command, ["--host", "0.0.0.0"])
    assert r.exit_code == 2
    assert "loopback only" in r.output


def test_ui_reports_port_busy_with_explicit_port():
    runner = CliRunner()
    with patch("notebooklm.cli.ui._try_bind", return_value=False):
        r = runner.invoke(ui_command, ["--port", "9999"])
    assert r.exit_code == 1
    assert "9999 is busy" in r.output


def test_ui_reports_no_free_port_when_window_full():
    runner = CliRunner()
    with patch("notebooklm.cli.ui._try_bind", return_value=False):
        r = runner.invoke(ui_command)
    assert r.exit_code == 1
    assert "No free port" in r.output


def test_ui_missing_extra_emits_install_hint():
    runner = CliRunner()
    # Simulate the [ui] extra being missing by raising ImportError when
    # `notebooklm.web.create_app` is imported.
    import builtins

    real_import = builtins.__import__

    def fake_import(name, *a, **kw):
        if name == "notebooklm.web" or name.startswith("notebooklm.web"):
            raise ImportError(
                "notebooklm ui requires the [ui] extra. Install with: pip install notebooklm-py[ui]"
            )
        return real_import(name, *a, **kw)

    with patch("builtins.__import__", side_effect=fake_import):
        r = runner.invoke(ui_command, ["--port", "0"])
    assert r.exit_code == 1
    assert "[ui] extra" in r.output
