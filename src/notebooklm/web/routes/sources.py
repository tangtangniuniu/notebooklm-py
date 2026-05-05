"""Source list / add / rename / delete / fulltext / dedup."""

from __future__ import annotations

import tempfile
from pathlib import Path
from typing import Any

from fastapi import APIRouter, Body, File, HTTPException, Request, UploadFile

from ..app import require_client

router = APIRouter()


def _serialize_source(s) -> dict:
    return {
        "id": s.id,
        "title": s.title,
        "url": s.url,
        "kind": str(s.kind),
        "status": s.status,
        "created_at": s.created_at.isoformat() if s.created_at else None,
    }


@router.get("/{notebook_id}/sources")
async def list_sources(request: Request, notebook_id: str):
    client = require_client(request)
    sources = await client.sources.list(notebook_id)
    return {"sources": [_serialize_source(s) for s in sources]}


@router.post("/{notebook_id}/sources")
async def add_source(request: Request, notebook_id: str, payload: dict[str, Any] = Body(...)):
    client = require_client(request)
    kind = payload.get("type")
    if kind == "url":
        url = payload.get("value", "").strip()
        if not url:
            raise HTTPException(400, "url required")
        src = await client.sources.add_url(notebook_id, url)
    elif kind == "text":
        title = payload.get("title", "Pasted text")
        content = payload.get("content", "")
        src = await client.sources.add_text(notebook_id, title, content)
    else:
        raise HTTPException(400, f"unsupported source type: {kind}")
    return _serialize_source(src)


@router.post("/{notebook_id}/sources/file")
async def add_file_source(request: Request, notebook_id: str, file: UploadFile = File(...)):
    client = require_client(request)
    # Persist to a temp file for the client's upload routine.
    suffix = Path(file.filename or "upload").suffix
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        while chunk := await file.read(65536):
            tmp.write(chunk)
        tmp_path = tmp.name
    try:
        src = await client.sources.add_file(notebook_id, tmp_path)
    finally:
        Path(tmp_path).unlink(missing_ok=True)
    return _serialize_source(src)


@router.patch("/{notebook_id}/sources/{source_id}")
async def rename_source(
    request: Request, notebook_id: str, source_id: str, title: str = Body(..., embed=True)
):
    client = require_client(request)
    src = await client.sources.rename(notebook_id, source_id, title)
    return _serialize_source(src)


@router.delete("/{notebook_id}/sources/{source_id}")
async def delete_source(request: Request, notebook_id: str, source_id: str):
    client = require_client(request)
    await client.sources.delete(notebook_id, source_id)
    return {"deleted": source_id}


@router.get("/{notebook_id}/sources/{source_id}/fulltext")
async def get_fulltext(request: Request, notebook_id: str, source_id: str):
    client = require_client(request)
    ft = await client.sources.get_fulltext(notebook_id, source_id)
    return {
        "source_id": ft.source_id,
        "title": ft.title,
        "content": ft.content,
        "kind": str(ft.kind),
        "url": ft.url,
        "char_count": ft.char_count,
    }


@router.get("/{notebook_id}/sources/dedup-preview")
async def dedup_preview(request: Request, notebook_id: str):
    """Return groups of duplicate sources (same title + kind + url)."""
    client = require_client(request)
    sources = await client.sources.list(notebook_id)
    groups: dict[tuple[str, str, str], list] = {}
    for s in sources:
        key = (s.title or "", str(s.kind), s.url or "")
        groups.setdefault(key, []).append(s)
    duplicates = []
    for (title, kind, url), group in groups.items():
        if len(group) < 2:
            continue
        # Sort by created_at so the latest comes last.
        group.sort(key=lambda s: s.created_at or 0)
        duplicates.append(
            {
                "title": title,
                "kind": kind,
                "url": url,
                "sources": [_serialize_source(s) for s in group],
            }
        )
    return {"groups": duplicates}
