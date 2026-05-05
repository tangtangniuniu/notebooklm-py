"""Chat: ask, list/replay/export conversations.

Note: streaming is not implemented in this version because the underlying
`client.chat.ask` returns the answer as a single result. The endpoints below
return the completed turn in one response and persist it via
`ConversationStore`. Future work can add an SSE variant once the chat client
exposes a streaming API.
"""

from __future__ import annotations

from dataclasses import asdict
from urllib.parse import quote

from fastapi import APIRouter, Body, Request
from fastapi.responses import Response

from ..._history import ConversationStore, Turn
from ..app import get_state, require_client

router = APIRouter()


@router.post("/{conversation_id}/ask")
async def ask(
    request: Request,
    conversation_id: str,
    notebook_id: str = Body(..., embed=True),
    question: str = Body(..., embed=True),
):
    client = require_client(request)
    state = get_state(request)
    result = await client.chat.ask(notebook_id, question, conversation_id=conversation_id)
    citations = [asdict(r) for r in result.references]
    turn = Turn(
        question=question,
        answer=result.answer,
        conversation_id=result.conversation_id or conversation_id,
        citations=citations,
    )
    state.history.append_turn(notebook_id, turn)
    return {
        "conversation_id": result.conversation_id or conversation_id,
        "turn_number": result.turn_number,
        "answer": result.answer,
        "citations": citations,
        "ts": turn.ts,
    }


@router.get("/conversations")
async def list_conversations(request: Request, notebook_id: str):
    state = get_state(request)
    summaries = state.history.list_conversations(notebook_id)
    return {
        "conversations": [
            {
                "conversation_id": s.conversation_id,
                "started_at": s.started_at,
                "ended_at": s.ended_at,
                "turn_count": s.turn_count,
            }
            for s in summaries
        ]
    }


@router.get("/conversations/{conversation_id}")
async def get_conversation(request: Request, conversation_id: str, notebook_id: str):
    state = get_state(request)
    turns = state.history.replay(notebook_id, conversation_id)
    return {
        "conversation_id": conversation_id,
        "turns": [
            {
                "question": t.question,
                "answer": t.answer,
                "ts": t.ts,
                "turn_id": t.turn_id,
                "citations": t.citations,
            }
            for t in turns
        ],
    }


@router.get("/conversations/{conversation_id}/export")
async def export_conversation(request: Request, conversation_id: str, notebook_id: str):
    """Render a single conversation as Markdown and download it."""
    state = get_state(request)
    client = require_client(request)
    nb = await client.notebooks.get(notebook_id)
    title = nb.title or notebook_id
    md = state.history.export_markdown(notebook_id, title, conversation_id=conversation_id)
    filename = ConversationStore.export_filename(title)
    return Response(
        content=md,
        media_type="text/markdown; charset=utf-8",
        headers={"Content-Disposition": f"attachment; filename*=UTF-8''{quote(filename)}"},
    )


@router.get("/conversations/export-all")
async def export_all_conversations(request: Request, notebook_id: str):
    state = get_state(request)
    client = require_client(request)
    nb = await client.notebooks.get(notebook_id)
    title = nb.title or notebook_id
    md = state.history.export_markdown(notebook_id, title)
    filename = ConversationStore.export_filename(title)
    return Response(
        content=md,
        media_type="text/markdown; charset=utf-8",
        headers={"Content-Disposition": f"attachment; filename*=UTF-8''{quote(filename)}"},
    )
