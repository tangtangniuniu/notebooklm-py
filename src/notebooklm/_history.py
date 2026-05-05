"""Per-notebook conversation history with append-only JSONL persistence.

Each chat Q&A turn is written as one JSON line to
``<config_dir>/conversations/<notebook_id>.jsonl``. The store provides:

- `append_turn(notebook_id, turn)` — atomic append, safe under concurrent writes
- `list_conversations(notebook_id)` — distinct conversation IDs with metadata
- `replay(notebook_id, conversation_id)` — every turn for a conversation
- `export_markdown(...)` — formatted Markdown for one or all conversations

All filesystem access is restricted to the conversations directory; notebook
IDs containing path separators or `..` are rejected.
"""

from __future__ import annotations

import json
import os
import re
import uuid
from collections.abc import Iterable
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ._filename import sanitize_filename
from .paths import get_home_dir

# Notebook IDs are UUIDs in the wild; we accept any token of safe characters.
_SAFE_ID = re.compile(r"^[A-Za-z0-9._-]+$")


@dataclass
class Turn:
    """A single Q&A turn persisted in the conversation log."""

    question: str
    answer: str
    conversation_id: str
    turn_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    ts: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    citations: list[dict[str, Any]] = field(default_factory=list)

    def to_json_line(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False) + "\n"

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Turn:
        return cls(
            question=str(data.get("question", "")),
            answer=str(data.get("answer", "")),
            conversation_id=str(data.get("conversation_id", "")),
            turn_id=str(data.get("turn_id", "")),
            ts=str(data.get("ts", "")),
            citations=list(data.get("citations") or []),
        )


@dataclass
class ConversationSummary:
    """Aggregate metadata for one conversation in a notebook's log."""

    conversation_id: str
    started_at: str
    ended_at: str
    turn_count: int


class ConversationStore:
    """Filesystem-backed conversation log."""

    def __init__(self, root: Path | None = None):
        self._root = (root or (get_home_dir() / "conversations")).resolve()

    @property
    def root(self) -> Path:
        return self._root

    # ------------------------------------------------------------------ paths
    def _path_for(self, notebook_id: str) -> Path:
        if (
            not notebook_id
            or not _SAFE_ID.match(notebook_id)
            or notebook_id in {".", ".."}
            or notebook_id.startswith(".")
        ):
            raise ValueError(f"unsafe notebook_id: {notebook_id!r}")
        path = (self._root / f"{notebook_id}.jsonl").resolve()
        # Defense-in-depth: ensure result stays under root.
        try:
            path.relative_to(self._root)
        except ValueError as e:
            raise ValueError(f"path escapes conversations dir: {path}") from e
        return path

    # -------------------------------------------------------------- mutation
    def append_turn(self, notebook_id: str, turn: Turn) -> None:
        path = self._path_for(notebook_id)
        path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        line = turn.to_json_line().encode("utf-8")
        # O_APPEND-protected single write keeps us safe under concurrent writers.
        fd = os.open(
            str(path),
            os.O_WRONLY | os.O_CREAT | os.O_APPEND,
            0o600,
        )
        try:
            os.write(fd, line)
        finally:
            os.close(fd)

    # ----------------------------------------------------------------- query
    def _iter_turns(self, notebook_id: str) -> Iterable[Turn]:
        path = self._path_for(notebook_id)
        if not path.exists():
            return
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    yield Turn.from_dict(json.loads(line))
                except json.JSONDecodeError:
                    # Skip corrupted lines rather than failing the whole replay.
                    continue

    def list_conversations(self, notebook_id: str) -> list[ConversationSummary]:
        groups: dict[str, list[Turn]] = {}
        for turn in self._iter_turns(notebook_id):
            groups.setdefault(turn.conversation_id, []).append(turn)
        summaries = [
            ConversationSummary(
                conversation_id=cid,
                started_at=min(t.ts for t in turns),
                ended_at=max(t.ts for t in turns),
                turn_count=len(turns),
            )
            for cid, turns in groups.items()
            if cid
        ]
        summaries.sort(key=lambda s: s.ended_at, reverse=True)
        return summaries

    def replay(self, notebook_id: str, conversation_id: str) -> list[Turn]:
        turns = [t for t in self._iter_turns(notebook_id) if t.conversation_id == conversation_id]
        turns.sort(key=lambda t: t.ts)
        return turns

    # ----------------------------------------------------------------- export
    def export_markdown(
        self,
        notebook_id: str,
        notebook_title: str,
        conversation_id: str | None = None,
    ) -> str:
        """Render the log as Markdown.

        If `conversation_id` is None, all conversations for the notebook are
        included, each under a `## Conversation <n>` heading.
        """
        groups: dict[str, list[Turn]] = {}
        for turn in self._iter_turns(notebook_id):
            groups.setdefault(turn.conversation_id, []).append(turn)
        for turns in groups.values():
            turns.sort(key=lambda t: t.ts)

        if conversation_id is not None:
            target = {conversation_id: groups.get(conversation_id, [])}
        else:
            target = dict(
                sorted(groups.items(), key=lambda kv: min(t.ts for t in kv[1]) if kv[1] else "")
            )

        all_turns = [t for ts in target.values() for t in ts]
        if not all_turns:
            started = ended = datetime.now(timezone.utc).isoformat()
        else:
            started = min(t.ts for t in all_turns)
            ended = max(t.ts for t in all_turns)
        total_turns = len(all_turns)

        lines: list[str] = []
        lines.append("---")
        lines.append(f"notebook: {json.dumps(notebook_title, ensure_ascii=False)}")
        lines.append(f"notebook_id: {notebook_id}")
        if conversation_id:
            lines.append(f"conversation_id: {conversation_id}")
        lines.append(f"started_at: {started}")
        lines.append(f"ended_at: {ended}")
        lines.append(f"turn_count: {total_turns}")
        lines.append("---")
        lines.append("")
        lines.append(f"# {notebook_title}")
        lines.append("")

        if conversation_id is not None:
            self._render_turns_to(lines, target.get(conversation_id, []))
        else:
            for i, (cid, turns) in enumerate(target.items(), start=1):
                lines.append(f"## Conversation {i}")
                lines.append("")
                lines.append(f"_id: `{cid}`_")
                lines.append("")
                self._render_turns_to(lines, turns)

        return "\n".join(lines).rstrip() + "\n"

    @staticmethod
    def _render_turns_to(lines: list[str], turns: list[Turn]) -> None:
        if not turns:
            lines.append("_(no turns)_")
            lines.append("")
            return
        for i, turn in enumerate(turns, start=1):
            lines.append(f"### Question {i}")
            lines.append("")
            lines.append(turn.question.strip() or "_(empty)_")
            lines.append("")
            lines.append(f"**Answer** _(at {turn.ts})_")
            lines.append("")
            lines.append(turn.answer.strip() or "_(empty)_")
            lines.append("")
            if turn.citations:
                lines.append("**Sources**")
                lines.append("")
                for j, c in enumerate(turn.citations, start=1):
                    src = c.get("source_id") or "?"
                    snippet = (c.get("cited_text") or "").strip().replace("\n", " ")
                    if snippet:
                        lines.append(f"- [{j}] `{src}` — {snippet[:200]}")
                    else:
                        lines.append(f"- [{j}] `{src}`")
                lines.append("")

    @staticmethod
    def export_filename(notebook_title: str) -> str:
        """`<sanitized-title>-<YYYY-MM-DD>.md`."""
        date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        return f"{sanitize_filename(notebook_title)}-{date}.md"
