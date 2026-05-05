#!/usr/bin/env python3
"""NotebookLM Batch Operations Script.

.. deprecated::
    Superseded by the local web UI introduced in 0.4.0. Install the optional
    `[ui]` extra and run::

        pip install "notebooklm-py[ui]"
        notebooklm ui

    See ``docs/web-ui.md`` for the three-panel interface that subsumes every
    flow this script provides (select, dedup, source-table, source-download,
    note-download, download-all) plus live progress and one-click Markdown
    export of chat history.

Wraps the `notebooklm` CLI to provide batch operations:
  select          - Interactive notebook selection
  dedup           - Deduplicate sources
  source-table    - List sources as markdown table
  source-download - Download all sources
  note-download   - Download all notes
  download-all    - Download sources + artifacts + notes

Requires: notebooklm CLI installed and logged in.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def run_cmd(args, check=True):
    """Run a subprocess with clean output (no Rich formatting)."""
    env = os.environ.copy()
    env["NO_COLOR"] = "1"
    env["COLUMNS"] = "999"
    result = subprocess.run(
        args,
        capture_output=True,
        text=True,
        env=env,
    )
    if check and result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(f"Command failed: {' '.join(args)}\n{detail}")
    return result


def run_json_cmd(args):
    """Run command and parse stdout as JSON."""
    result = run_cmd(args)
    return json.loads(result.stdout)


def sanitize_filename(name, max_length=100):
    """Replace unsafe chars while preserving CJK characters, then truncate."""
    # Keep alphanumeric, CJK, spaces, hyphens, underscores, dots
    safe = re.sub(r"[^\w\u4e00-\u9fff\s.\-]", "_", name)
    safe = re.sub(r"\s+", " ", safe).strip()
    if len(safe) > max_length:
        safe = safe[:max_length].rstrip()
    return safe or "untitled"


def get_notebook_info():
    """Return (notebook_id, notebook_title) from current context."""
    data = run_json_cmd(["notebooklm", "status", "--json"])
    if not data.get("has_context"):
        raise RuntimeError("No notebook selected. Run: notebooklm use <id>")
    nb = data["notebook"]
    return nb["id"], nb.get("title") or nb["id"]


def parse_note_list_output(text):
    """Parse Rich table output from `note list` into list of {id, title}."""
    notes = []
    for line in text.splitlines():
        # Rich tables use │ as column delimiter
        if "│" not in line:
            continue
        parts = [p.strip() for p in line.split("│")]
        # Filter out empty strings from leading/trailing │
        parts = [p for p in parts if p]
        if len(parts) < 2:
            continue
        # Skip header row
        candidate_id = parts[0]
        if candidate_id.lower() == "id" or set(candidate_id) <= {"-", " ", "─"}:
            continue
        # Looks like a UUID-ish ID
        if len(candidate_id) > 8:
            notes.append({"id": candidate_id, "title": parts[1]})
    return notes


def parse_note_get_output(text):
    """Parse `note get` text output into {id, title, content}."""
    result = {"id": "", "title": "", "content": ""}
    lines = text.splitlines()
    content_start = None
    for i, line in enumerate(lines):
        if line.startswith("ID:"):
            result["id"] = line[len("ID:") :].strip()
        elif line.startswith("Title:"):
            result["title"] = line[len("Title:") :].strip()
        elif line.startswith("Content:"):
            rest = line[len("Content:") :].strip()
            content_start = i
            if rest:
                result["content"] = rest
            break
    if content_start is not None:
        # Everything after "Content:" line is the content
        remaining = "\n".join(lines[content_start + 1 :])
        if result["content"]:
            result["content"] += "\n" + remaining
        else:
            result["content"] = remaining
    return result


# ---------------------------------------------------------------------------
# Feature 1: Select Notebook
# ---------------------------------------------------------------------------


def cmd_select():
    """Interactive notebook selection."""
    data = run_json_cmd(["notebooklm", "list", "--json"])
    notebooks = data.get("notebooks", [])
    if not notebooks:
        print("No notebooks found.")
        return

    print("\nAvailable notebooks:\n")
    for nb in notebooks:
        title = nb.get("title", "(untitled)")
        created = nb.get("created_at", "")
        if created:
            created = f"  ({created[:10]})"
        print(f"  {nb['index']:>3}. {title}{created}")
        print(f"       {nb['id']}")

    print()
    try:
        choice = input(f"Select notebook [1-{len(notebooks)}]: ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return

    try:
        idx = int(choice) - 1
    except ValueError:
        print(f"Invalid choice: {choice}")
        return

    if idx < 0 or idx >= len(notebooks):
        print(f"Out of range: {choice}")
        return

    selected = notebooks[idx]
    print(f"\nSelecting: {selected['title']}")
    run_cmd(["notebooklm", "use", selected["id"]])
    print("Done.")


# ---------------------------------------------------------------------------
# Feature 2: Source Deduplication
# ---------------------------------------------------------------------------


def cmd_dedup():
    """Find and remove duplicate sources."""
    nb_id, nb_title = get_notebook_info()
    print(f"Notebook: {nb_title}\n")

    data = run_json_cmd(["notebooklm", "source", "list", "--json", "-n", nb_id])
    sources = data.get("sources", [])
    if not sources:
        print("No sources found.")
        return

    # Group by (title, type, url)
    groups = {}
    for src in sources:
        key = (src.get("title", ""), src.get("type", ""), src.get("url") or "")
        groups.setdefault(key, []).append(src)

    duplicates_found = False
    for key, group in groups.items():
        if len(group) < 2:
            continue
        duplicates_found = True
        title, stype, url = key
        print(f"Duplicate group ({len(group)} copies):")
        print(f"  Title: {title}")
        print(f"  Type:  {stype}")
        if url:
            print(f"  URL:   {url}")

        # Keep the last one (highest index / latest), delete the rest
        to_keep = group[-1]
        to_delete = group[:-1]
        print(f"  Keeping: index={to_keep['index']}  id={to_keep['id']}")

        for src in to_delete:
            print(f"  Delete:  index={src['index']}  id={src['id']}")
            try:
                confirm = input("    Confirm delete? [y/N]: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\n    Skipped.")
                continue
            if confirm == "y":
                try:
                    run_cmd(["notebooklm", "source", "delete", src["id"], "-y", "-n", nb_id])
                    print("    Deleted.")
                except RuntimeError as e:
                    print(f"    Error: {e}")
            else:
                print("    Skipped.")
        print()

    if not duplicates_found:
        print("No duplicate sources found.")


# ---------------------------------------------------------------------------
# Feature 3: Source List as Markdown Table
# ---------------------------------------------------------------------------


def cmd_source_table():
    """Print sources as a markdown table."""
    nb_id, nb_title = get_notebook_info()
    data = run_json_cmd(["notebooklm", "source", "list", "--json", "-n", nb_id])
    sources = data.get("sources", [])

    print(f"# Sources: {nb_title}\n")
    print("| # | Title | Type | URL |")
    print("|---|-------|------|-----|")
    for src in sources:
        idx = src.get("index", "")
        title = src.get("title", "").replace("|", "\\|")
        stype = src.get("type", "").replace("SourceType.", "")
        url = src.get("url") or ""
        print(f"| {idx} | {title} | {stype} | {url} |")

    print(f"\nTotal: {len(sources)} sources")


# ---------------------------------------------------------------------------
# Feature 4: Source Download
# ---------------------------------------------------------------------------

_TYPE_EXT_MAP = {
    "SourceType.PDF": ".pdf",
    "SourceType.DOCX": ".docx",
    "SourceType.PPTX": ".pptx",
    "SourceType.CSV": ".csv",
}

# String forms of the office source types that should now route through the
# new ``notebooklm.conversion`` module (download + markitdown → Markdown).
_FILE_TYPES_TO_MARKDOWN = ("SourceType.PDF", "SourceType.DOCX", "SourceType.PPTX")
# Direct binary download (Markdown conversion would lose downstream utility).
_DIRECT_DOWNLOAD_TYPES = ("SourceType.CSV",)
# Image source — direct download with extension picked at runtime.
_IMAGE_TYPE = "SourceType.IMAGE"


def _ext_from_url(url):
    """Try to extract file extension from URL path."""
    from urllib.parse import urlparse

    path = urlparse(url).path
    _, ext = os.path.splitext(path)
    if ext and len(ext) <= 6:
        return ext
    return None


def _run_markdown_conversion(url, source_kind_str, target_path, keep_original):
    """Synchronous wrapper around ``notebooklm.conversion.source_to_markdown``.

    ``source_kind_str`` is the CLI's string representation (e.g. ``"SourceType.PDF"``).
    Returns the conversion strategy on success; raises on failure.
    """
    import asyncio

    from notebooklm.conversion import ConversionOptions, source_to_markdown
    from notebooklm.types import SourceType

    # Map CLI string back to enum. Falls back to a plain string lookup which
    # the str-Enum supports natively.
    kind_map = {
        "SourceType.WEB_PAGE": SourceType.WEB_PAGE,
        "SourceType.PDF": SourceType.PDF,
        "SourceType.DOCX": SourceType.DOCX,
        "SourceType.PPTX": SourceType.PPTX,
    }
    kind = kind_map.get(source_kind_str)
    if kind is None:
        raise RuntimeError(f"unsupported source kind for markdown conversion: {source_kind_str}")

    options = ConversionOptions.from_env(keep_original=keep_original)
    result = asyncio.run(source_to_markdown(url, kind, target_path, options=options))
    return result.strategy


def _download_image_source(url, base_dir, safe_title):
    """Download an image source as-is, picking the extension at runtime.

    Returns a tuple ``(final_path, status, retried)`` where ``status`` is one
    of ``"done"``, ``"skipped"`` and ``retried`` is True when the slash-retry
    helper kicked in. Raises ``RuntimeError`` on HTTP / transport failure so
    the caller can print an error message and continue.
    """
    import httpx

    from notebooklm.conversion._images import _pick_image_extension, known_image_extensions
    from notebooklm.conversion._url_retry import fetch_with_slash_retry, slash_retried

    # Skip-if-exists: any sibling with a known image extension means we've
    # already saved this image (possibly in a previous run that picked a
    # different extension).
    for ext in known_image_extensions():
        candidate = base_dir / f"{safe_title}{ext}"
        if candidate.exists():
            return candidate, "skipped", False

    try:
        with httpx.Client(timeout=30.0, follow_redirects=True) as client:
            response = fetch_with_slash_retry(client, url)
            if response.status_code < 200 or response.status_code >= 300:
                raise RuntimeError(f"HTTP {response.status_code}")
            ext = _pick_image_extension(url, response.headers.get("content-type"))
            final = base_dir / f"{safe_title}{ext}"
            tmp = final.with_suffix(final.suffix + ".tmp")
            try:
                with tmp.open("wb") as fh:
                    for chunk in response.iter_bytes():
                        fh.write(chunk)
                tmp.replace(final)
            except Exception:
                tmp.unlink(missing_ok=True)
                raise
            retried = slash_retried(response)
    except httpx.HTTPError as exc:
        raise RuntimeError(f"image download transport error: {exc}") from exc

    return final, "done", retried


def _download_csv_source(url, filepath):
    """Download a CSV (or other direct-binary) source to ``filepath``.

    Uses ``fetch_with_slash_retry`` so a 404/403 with a misnormalized URL
    gets one retry with the trailing slash toggled. Returns True when the
    helper recorded a retry, False otherwise. Raises ``RuntimeError`` on
    HTTP / transport failure.
    """
    import httpx

    from notebooklm.conversion._url_retry import fetch_with_slash_retry, slash_retried

    tmp = filepath.with_suffix(filepath.suffix + ".tmp")
    try:
        with httpx.Client(timeout=60.0, follow_redirects=True) as client:
            response = fetch_with_slash_retry(client, url)
            if response.status_code < 200 or response.status_code >= 300:
                raise RuntimeError(f"HTTP {response.status_code}")
            with tmp.open("wb") as fh:
                for chunk in response.iter_bytes():
                    fh.write(chunk)
            tmp.replace(filepath)
            return slash_retried(response)
    except httpx.HTTPError as exc:
        tmp.unlink(missing_ok=True)
        raise RuntimeError(f"download transport error: {exc}") from exc
    except Exception:
        tmp.unlink(missing_ok=True)
        raise


def cmd_source_download(base_dir=None, keep_original=False, legacy_pdf=False, concurrency=5):
    """Download all sources with type-specific strategies.

    Default behavior produces ``.md`` for ``WEB_PAGE``, ``PDF``, ``DOCX``, and
    ``PPTX`` sources via the ``notebooklm.conversion`` module. ``CSV`` stays a
    direct download. ``MARKDOWN`` and ``PASTED_TEXT`` come from the CLI's
    ``source fulltext`` command.

    Set ``keep_original=True`` to keep the original ``.pdf``/``.docx``/``.pptx``
    binary alongside the produced ``.md``. Set ``legacy_pdf=True`` to revert
    ``WEB_PAGE`` sources to the previous ``wkhtmltopdf`` path (one-release
    escape hatch).

    ``concurrency`` is accepted for parity with the web UI / orchestrator
    (range 1..10, default 5) but currently informational only — this script
    runs sequentially. A warning is printed when ``concurrency > 1``.
    """
    if concurrency > 1:
        print(
            f"Warning: --concurrency={concurrency} is accepted for parity with "
            "the web UI but this script is sequential; downloads will run "
            "one at a time."
        )
    nb_id, nb_title = get_notebook_info()
    if base_dir is None:
        base_dir = Path(sanitize_filename(nb_title)) / "sources"
    else:
        base_dir = Path(base_dir)
    base_dir.mkdir(parents=True, exist_ok=True)

    data = run_json_cmd(["notebooklm", "source", "list", "--json", "-n", nb_id])
    sources = data.get("sources", [])
    if not sources:
        print("No sources to download.")
        return

    print(f"Downloading {len(sources)} sources to: {base_dir}/\n")

    for src in sources:
        title = src.get("title", "untitled")
        stype = src.get("type", "")
        url = src.get("url") or ""
        src_id = src["id"]
        safe_title = sanitize_filename(title)

        # Determine strategy based on type and URL.
        if stype in _FILE_TYPES_TO_MARKDOWN and url:
            # PDF / DOCX / PPTX → Markdown via markitdown.
            filename = safe_title + ".md"
            filepath = base_dir / filename
            if filepath.exists():
                print(f"  [skip] {filename} (exists)")
                continue
            try:
                strategy = _run_markdown_conversion(url, stype, filepath, keep_original)
                print(f"  [{strategy}] {filename}")
            except Exception as e:
                print(f"    Error: {e}")

        elif stype in _DIRECT_DOWNLOAD_TYPES and url:
            # Direct file download (CSV stays binary).
            ext = _ext_from_url(url) or _TYPE_EXT_MAP.get(stype, ".bin")
            filename = safe_title + ext
            filepath = base_dir / filename
            if filepath.exists():
                print(f"  [skip] {filename} (exists)")
                continue
            try:
                retried = _download_csv_source(url, filepath)
            except Exception as e:
                print(f"    Error: {e}")
                continue
            label = "download (slash-retry)" if retried else "download"
            print(f"  [{label}] {filename}")

        elif stype == _IMAGE_TYPE and url:
            # IMAGE: download as-is, with extension picked at runtime.
            try:
                final, status, retried = _download_image_source(url, base_dir, safe_title)
            except Exception as e:
                print(f"    Error: {e}")
                continue
            if status == "skipped":
                label = "skip"
            elif retried:
                label = "image (slash-retry)"
            else:
                label = "image"
            print(f"  [{label}] {final.name}")

        elif stype == "SourceType.WEB_PAGE" and url:
            if legacy_pdf:
                # Opt-in legacy path: convert web page to PDF via wkhtmltopdf.
                filename = safe_title + ".pdf"
                filepath = base_dir / filename
                if filepath.exists():
                    print(f"  [skip] {filename} (exists)")
                    continue
                if not shutil.which("wkhtmltopdf"):
                    print(f"  [todo] {filename} - wkhtmltopdf not found")
                    print("    Install: sudo apt install wkhtmltopdf  OR  brew install wkhtmltopdf")
                    todo = base_dir / (safe_title + ".todo")
                    if not todo.exists():
                        todo.write_text(f"WEB_PAGE: {url}\nInstall wkhtmltopdf to download.\n")
                    continue
                print(f"  [legacy-pdf] {filename}")
                try:
                    run_cmd(["wkhtmltopdf", "--quiet", url, str(filepath)], check=False)
                    if not filepath.exists():
                        print("    Warning: wkhtmltopdf may have failed")
                except Exception as e:
                    print(f"    Error: {e}")
            else:
                # New default: convert web page to Markdown via markdown.new (with fallback).
                filename = safe_title + ".md"
                filepath = base_dir / filename
                if filepath.exists():
                    print(f"  [skip] {filename} (exists)")
                    continue
                try:
                    strategy = _run_markdown_conversion(url, stype, filepath, keep_original)
                    # Show the friendly strategy label.
                    label = {
                        "remote": "markdown.new",
                        "fallback": "fallback",
                        "browser": "browser",
                    }.get(strategy, strategy)
                    print(f"  [{label}] {filename}")
                except Exception as e:
                    print(f"    Error: {e}")

        elif stype in ("SourceType.MARKDOWN", "SourceType.PASTED_TEXT") or (
            not url
            and stype
            not in (
                "SourceType.WEB_PAGE",
                "SourceType.YOUTUBE",
                "SourceType.GOOGLE_DOCS",
                "SourceType.GOOGLE_SLIDES",
                "SourceType.GOOGLE_SPREADSHEET",
                "SourceType.GOOGLE_DRIVE_AUDIO",
                "SourceType.GOOGLE_DRIVE_VIDEO",
            )
        ):
            # Extract fulltext via CLI
            filename = safe_title + ".md"
            filepath = base_dir / filename
            if filepath.exists():
                print(f"  [skip] {filename} (exists)")
                continue
            print(f"  [fulltext] {filename}")
            try:
                run_cmd(
                    ["notebooklm", "source", "fulltext", src_id, "-o", str(filepath), "-n", nb_id]
                )
            except RuntimeError as e:
                print(f"    Error: {e}")

        else:
            # Unknown or unsupported type — create .todo placeholder
            filename = safe_title + ".todo"
            filepath = base_dir / filename
            if filepath.exists():
                print(f"  [skip] {filename} (exists)")
                continue
            print(f"  [todo] {filename} ({stype})")
            filepath.write_text(f"Source: {title}\nType: {stype}\nURL: {url}\n")

    print("\nSource download complete.")


# ---------------------------------------------------------------------------
# Feature 5: Note Download
# ---------------------------------------------------------------------------


def cmd_note_download(base_dir=None):
    """Download all notes as markdown files."""
    nb_id, nb_title = get_notebook_info()
    if base_dir is None:
        base_dir = Path(sanitize_filename(nb_title)) / "notes"
    else:
        base_dir = Path(base_dir)
    base_dir.mkdir(parents=True, exist_ok=True)

    # note list has no --json flag, parse the Rich table
    result = run_cmd(["notebooklm", "note", "list", "-n", nb_id], check=False)
    if result.returncode != 0:
        print(f"Note list failed: {result.stderr.strip()}")
        return

    notes = parse_note_list_output(result.stdout)
    if not notes:
        print("No notes found.")
        return

    print(f"Downloading {len(notes)} notes to: {base_dir}/\n")

    for note in notes:
        note_id = note["id"]
        # Fetch full note content
        try:
            get_result = run_cmd(["notebooklm", "note", "get", note_id, "-n", nb_id])
        except RuntimeError as e:
            print(f"  [error] {note_id}: {e}")
            continue

        parsed = parse_note_get_output(get_result.stdout)
        title = parsed.get("title") or "Untitled"
        content = parsed.get("content") or ""

        filename = sanitize_filename(title) + ".md"
        filepath = base_dir / filename
        if filepath.exists():
            print(f"  [skip] {filename} (exists)")
            continue

        print(f"  [save] {filename}")
        filepath.write_text(content, encoding="utf-8")

    print("\nNote download complete.")


# ---------------------------------------------------------------------------
# Feature 6: Download All
# ---------------------------------------------------------------------------

# Artifact types that support --all flag
_BATCH_ARTIFACT_TYPES = [
    "audio",
    "video",
    "slide-deck",
    "infographic",
    "report",
    "mind-map",
    "data-table",
]

# Artifact types that use individual download (no --all)
_SINGLE_ARTIFACT_TYPES = [
    ("quiz", "quiz.json"),
    ("flashcards", "flashcards.json"),
]


def cmd_download_all():
    """Download sources, artifacts, and notes for the current notebook."""
    nb_id, nb_title = get_notebook_info()
    safe_title = sanitize_filename(nb_title)
    base = Path(safe_title)

    sources_dir = base / "sources"
    artifacts_dir = base / "artifacts"
    notes_dir = base / "notes"

    for d in [sources_dir, artifacts_dir, notes_dir]:
        d.mkdir(parents=True, exist_ok=True)

    # 1) Sources
    print("=" * 60)
    print("Downloading SOURCES")
    print("=" * 60)
    cmd_source_download(base_dir=sources_dir)

    # 2) Artifacts
    print("\n" + "=" * 60)
    print("Downloading ARTIFACTS")
    print("=" * 60)

    for atype in _BATCH_ARTIFACT_TYPES:
        print(f"\n--- {atype} ---")
        try:
            run_cmd(
                [
                    "notebooklm",
                    "download",
                    atype,
                    "--all",
                    str(artifacts_dir),
                    "--no-clobber",
                    "-n",
                    nb_id,
                ]
            )
            print("  Done.")
        except RuntimeError:
            print(f"  No {atype} artifacts or download failed.")

    for atype, default_name in _SINGLE_ARTIFACT_TYPES:
        print(f"\n--- {atype} ---")
        outpath = artifacts_dir / default_name
        if outpath.exists():
            print(f"  [skip] {default_name} (exists)")
            continue
        try:
            run_cmd(
                [
                    "notebooklm",
                    "download",
                    atype,
                    str(outpath),
                    "-n",
                    nb_id,
                ]
            )
            print("  Done.")
        except RuntimeError:
            print(f"  No {atype} artifacts or download failed.")

    # 3) Notes
    print("\n" + "=" * 60)
    print("Downloading NOTES")
    print("=" * 60)
    cmd_note_download(base_dir=notes_dir)

    print("\n" + "=" * 60)
    print(f"All downloads saved to: {base}/")
    print("=" * 60)


# ---------------------------------------------------------------------------
# Interactive menu
# ---------------------------------------------------------------------------

_MENU_ITEMS = [
    ("select", "Select a notebook", cmd_select),
    ("dedup", "Deduplicate sources", cmd_dedup),
    ("source-table", "List sources as markdown table", cmd_source_table),
    ("source-download", "Download all sources", cmd_source_download),
    ("note-download", "Download all notes", cmd_note_download),
    ("download-all", "Download everything (sources + artifacts + notes)", cmd_download_all),
]


def interactive_menu():
    """Show interactive numbered menu when no subcommand given."""
    print("NotebookLM Batch Operations\n")
    for i, (_, desc, _) in enumerate(_MENU_ITEMS, 1):
        print(f"  {i}. {desc}")
    print("  0. Exit\n")

    try:
        choice = input("Choose [0-6]: ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return

    try:
        idx = int(choice)
    except ValueError:
        print(f"Invalid choice: {choice}")
        return

    if idx == 0:
        return
    if idx < 1 or idx > len(_MENU_ITEMS):
        print(f"Out of range: {choice}")
        return

    _, _, func = _MENU_ITEMS[idx - 1]
    try:
        func()
    except RuntimeError as e:
        print(f"\nError: {e}")
    except json.JSONDecodeError as e:
        print(f"\nError: failed to parse CLI output as JSON: {e}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def _parse_concurrency(raw):
    """argparse type validator: int in [1..10]."""
    try:
        n = int(raw)
    except (TypeError, ValueError) as exc:
        raise argparse.ArgumentTypeError(f"concurrency must be an integer, got {raw!r}") from exc
    if n < 1 or n > 10:
        raise argparse.ArgumentTypeError(f"concurrency must be between 1 and 10, got {n}")
    return n


def main():
    parser = argparse.ArgumentParser(
        description="NotebookLM Batch Operations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Run without arguments for an interactive menu.",
    )
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("select", help="Interactive notebook selection")
    sub.add_parser("dedup", help="Deduplicate sources")
    sub.add_parser("source-table", help="List sources as markdown table")

    sd_parser = sub.add_parser(
        "source-download",
        help="Download all sources (web/PDF/DOCX/PPTX as Markdown by default)",
    )
    sd_parser.add_argument(
        "--keep-original",
        action="store_true",
        help="Also keep the original PDF/DOCX/PPTX binary alongside the .md file",
    )
    sd_parser.add_argument(
        "--legacy-pdf",
        action="store_true",
        help="Restore the previous behavior of converting WEB_PAGE sources to PDF "
        "via wkhtmltopdf (one-release escape hatch; will be removed)",
    )
    sd_parser.add_argument(
        "--concurrency",
        type=_parse_concurrency,
        default=5,
        metavar="N",
        help="Maximum parallel downloads (1..10, default 5). Currently "
        "informational for this sequential script.",
    )

    sub.add_parser("note-download", help="Download all notes")
    sub.add_parser("download-all", help="Download everything (sources + artifacts + notes)")

    args = parser.parse_args()

    dispatch = {
        "select": cmd_select,
        "dedup": cmd_dedup,
        "source-table": cmd_source_table,
        "source-download": lambda: cmd_source_download(
            keep_original=getattr(args, "keep_original", False),
            legacy_pdf=getattr(args, "legacy_pdf", False),
            concurrency=getattr(args, "concurrency", 5),
        ),
        "note-download": cmd_note_download,
        "download-all": cmd_download_all,
    }

    if args.command:
        try:
            dispatch[args.command]()
        except RuntimeError as e:
            print(f"\nError: {e}", file=sys.stderr)
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"\nError: failed to parse CLI output as JSON: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        interactive_menu()


if __name__ == "__main__":
    main()
