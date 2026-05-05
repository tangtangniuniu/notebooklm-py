"""Unit tests for ConversationStore (`_history.py`) and `_filename.sanitize_filename`."""

from __future__ import annotations

import json
import threading
from pathlib import Path

import pytest

from notebooklm._filename import sanitize_filename
from notebooklm._history import ConversationStore, Turn


@pytest.fixture
def store(tmp_path: Path) -> ConversationStore:
    return ConversationStore(root=tmp_path / "conversations")


# ---------- sanitize_filename ----------


def test_sanitize_filename_preserves_cjk():
    assert sanitize_filename("克劳德中文教学课程") == "克劳德中文教学课程"


def test_sanitize_filename_replaces_unsafe():
    assert sanitize_filename("a/b:c*d?e") == "a_b_c_d_e"


def test_sanitize_filename_truncates():
    out = sanitize_filename("x" * 250, max_length=50)
    assert len(out) == 50


def test_sanitize_filename_empty_falls_back():
    assert sanitize_filename("") == "untitled"
    assert sanitize_filename(None) == "untitled"


# ---------- append + replay + list ----------


def test_append_creates_file_and_writes_one_line(store: ConversationStore):
    turn = Turn(question="Q1?", answer="A1", conversation_id="c1")
    store.append_turn("nb1", turn)

    path = store.root / "nb1.jsonl"
    assert path.exists()
    lines = path.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 1
    assert json.loads(lines[0])["question"] == "Q1?"


def test_append_multiple_turns(store: ConversationStore):
    for i in range(3):
        store.append_turn("nb1", Turn(question=f"Q{i}", answer=f"A{i}", conversation_id="c1"))
    path = store.root / "nb1.jsonl"
    assert len(path.read_text(encoding="utf-8").splitlines()) == 3


def test_replay_returns_turns_in_order(store: ConversationStore):
    for i in range(3):
        store.append_turn("nb1", Turn(question=f"Q{i}", answer=f"A{i}", conversation_id="c1"))
    turns = store.replay("nb1", "c1")
    assert [t.question for t in turns] == ["Q0", "Q1", "Q2"]


def test_replay_unknown_conversation_returns_empty(store: ConversationStore):
    assert store.replay("nb1", "missing") == []


def test_list_conversations_empty_log(store: ConversationStore):
    assert store.list_conversations("nbX") == []


def test_list_conversations_groups_and_orders_by_recency(store: ConversationStore):
    store.append_turn(
        "nb1",
        Turn(question="Qa", answer="Aa", conversation_id="c1", ts="2026-01-01T00:00:00+00:00"),
    )
    store.append_turn(
        "nb1",
        Turn(question="Qb", answer="Ab", conversation_id="c1", ts="2026-01-02T00:00:00+00:00"),
    )
    store.append_turn(
        "nb1",
        Turn(question="Qc", answer="Ac", conversation_id="c2", ts="2026-01-03T00:00:00+00:00"),
    )
    convs = store.list_conversations("nb1")
    assert [c.conversation_id for c in convs] == ["c2", "c1"]
    by_id = {c.conversation_id: c for c in convs}
    assert by_id["c1"].turn_count == 2
    assert by_id["c2"].turn_count == 1


# ---------- export ----------


def test_export_single_conversation(store: ConversationStore):
    store.append_turn("nb1", Turn(question="Hi", answer="Hello!", conversation_id="c1"))
    md = store.export_markdown("nb1", "Test Notebook", conversation_id="c1")
    assert "# Test Notebook" in md
    assert "### Question 1" in md
    assert "Hi" in md
    assert "Hello!" in md
    assert md.startswith("---\n")
    assert "conversation_id: c1" in md


def test_export_all_conversations(store: ConversationStore):
    store.append_turn(
        "nb1", Turn(question="A", answer="x", conversation_id="c1", ts="2026-01-01T00:00:00+00:00")
    )
    store.append_turn(
        "nb1", Turn(question="B", answer="y", conversation_id="c2", ts="2026-01-02T00:00:00+00:00")
    )
    md = store.export_markdown("nb1", "Test")
    assert "## Conversation 1" in md
    assert "## Conversation 2" in md


def test_export_filename_includes_date_and_title():
    name = ConversationStore.export_filename("My Notebook 中文")
    assert name.startswith("My Notebook 中文-")
    assert name.endswith(".md")


def test_export_includes_citations(store: ConversationStore):
    store.append_turn(
        "nb1",
        Turn(
            question="Q",
            answer="A",
            conversation_id="c1",
            citations=[{"source_id": "src-1", "cited_text": "important quote"}],
        ),
    )
    md = store.export_markdown("nb1", "T", conversation_id="c1")
    assert "**Sources**" in md
    assert "src-1" in md
    assert "important quote" in md


# ---------- safety ----------


@pytest.mark.parametrize("bad", ["..", "../etc", "a/b", "a\\b", "", " "])
def test_unsafe_notebook_id_rejected(store: ConversationStore, bad: str):
    with pytest.raises(ValueError):
        store.append_turn(bad, Turn(question="x", answer="y", conversation_id="c"))


def test_concurrent_writes_produce_intact_lines(store: ConversationStore):
    def writer(i: int) -> None:
        for j in range(20):
            store.append_turn(
                "nb1",
                Turn(question=f"q-{i}-{j}", answer="a" * 200, conversation_id="c1"),
            )

    threads = [threading.Thread(target=writer, args=(i,)) for i in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    path = store.root / "nb1.jsonl"
    lines = path.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 80
    for line in lines:
        # Every line must parse as JSON
        parsed = json.loads(line)
        assert parsed["conversation_id"] == "c1"


def test_forward_compat_unknown_fields_ignored(store: ConversationStore):
    path = store.root
    path.mkdir(parents=True, exist_ok=True)
    (path / "nbZ.jsonl").write_text(
        json.dumps(
            {
                "question": "q",
                "answer": "a",
                "conversation_id": "c1",
                "turn_id": "t1",
                "ts": "2026-01-01T00:00:00+00:00",
                "citations": [],
                "future_field": {"deeply": "nested"},
            }
        )
        + "\n",
        encoding="utf-8",
    )
    turns = store.replay("nbZ", "c1")
    assert len(turns) == 1
    assert turns[0].question == "q"
