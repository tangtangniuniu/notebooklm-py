"""Note list / get / create."""

from __future__ import annotations

from fastapi import APIRouter, Body, HTTPException, Request

from ..app import require_client

router = APIRouter()


def _serialize_note(n) -> dict:
    return {
        "id": n.id,
        "notebook_id": n.notebook_id,
        "title": n.title,
        "content": n.content,
        "created_at": n.created_at.isoformat() if n.created_at else None,
    }


@router.get("/{notebook_id}/notes")
async def list_notes(request: Request, notebook_id: str):
    client = require_client(request)
    notes = await client.notes.list(notebook_id)
    return {"notes": [_serialize_note(n) for n in notes]}


@router.get("/{notebook_id}/notes/{note_id}")
async def get_note(request: Request, notebook_id: str, note_id: str):
    client = require_client(request)
    n = await client.notes.get(notebook_id, note_id)
    if not n:
        raise HTTPException(404, "note not found")
    return _serialize_note(n)


@router.post("/{notebook_id}/notes")
async def create_note(
    request: Request,
    notebook_id: str,
    title: str = Body("New Note"),
    content: str = Body(""),
):
    client = require_client(request)
    n = await client.notes.create(notebook_id, title, content)
    return _serialize_note(n)
