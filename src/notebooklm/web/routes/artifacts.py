"""Artifact list / generate."""

from __future__ import annotations

from fastapi import APIRouter, Body, HTTPException, Request

from ..app import require_client

router = APIRouter()


def _serialize_artifact(a) -> dict:
    return {
        "id": a.id,
        "title": a.title,
        "kind": str(a.kind),
        "status": a.status,
        "status_str": a.status_str,
        "created_at": a.created_at.isoformat() if a.created_at else None,
    }


@router.get("/{notebook_id}/artifacts")
async def list_artifacts(request: Request, notebook_id: str):
    client = require_client(request)
    artifacts = await client.artifacts.list(notebook_id)
    return {"artifacts": [_serialize_artifact(a) for a in artifacts]}


@router.post("/{notebook_id}/artifacts")
async def generate_artifact(
    request: Request,
    notebook_id: str,
    kind: str = Body(..., embed=True),
    instructions: str | None = Body(None, embed=True),
):
    client = require_client(request)
    art_kind = kind.replace("-", "_")
    if art_kind == "audio":
        status = await client.artifacts.generate_audio(notebook_id, instructions=instructions)
    elif art_kind == "video":
        status = await client.artifacts.generate_video(notebook_id, instructions=instructions)
    elif art_kind == "report":
        status = await client.artifacts.generate_report(notebook_id)
    elif art_kind == "quiz":
        status = await client.artifacts.generate_quiz(notebook_id, instructions=instructions)
    elif art_kind == "flashcards":
        status = await client.artifacts.generate_flashcards(notebook_id, instructions=instructions)
    elif art_kind == "infographic":
        status = await client.artifacts.generate_infographic(notebook_id, instructions=instructions)
    elif art_kind == "slide_deck":
        status = await client.artifacts.generate_slide_deck(notebook_id, instructions=instructions)
    elif art_kind == "data_table":
        status = await client.artifacts.generate_data_table(notebook_id, instructions=instructions)
    elif art_kind == "mind_map":
        result = await client.artifacts.generate_mind_map(notebook_id)
        return {"task_id": result.get("note_id"), "status": "completed"}
    else:
        raise HTTPException(400, f"unsupported artifact kind: {kind}")
    return {"task_id": status.task_id, "status": status.status, "error": status.error}
