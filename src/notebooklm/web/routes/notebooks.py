"""Notebook list / get / create / rename / delete."""

from __future__ import annotations

from fastapi import APIRouter, Body, Request

from ..app import require_client

router = APIRouter()


def _serialize_notebook(nb) -> dict:
    return {
        "id": nb.id,
        "title": nb.title,
        "created_at": nb.created_at.isoformat() if nb.created_at else None,
        "source_count": getattr(nb, "sources_count", 0),
        "is_owner": getattr(nb, "is_owner", True),
    }


@router.get("")
async def list_notebooks(request: Request):
    client = require_client(request)
    notebooks = await client.notebooks.list()
    notebooks.sort(key=lambda n: n.created_at or 0, reverse=True)
    return {"notebooks": [_serialize_notebook(nb) for nb in notebooks]}


@router.get("/{notebook_id}")
async def get_notebook(request: Request, notebook_id: str):
    client = require_client(request)
    nb = await client.notebooks.get(notebook_id)
    return _serialize_notebook(nb)


@router.post("")
async def create_notebook(request: Request, title: str = Body(..., embed=True)):
    client = require_client(request)
    nb = await client.notebooks.create(title)
    return _serialize_notebook(nb)


@router.patch("/{notebook_id}")
async def rename_notebook(request: Request, notebook_id: str, title: str = Body(..., embed=True)):
    client = require_client(request)
    nb = await client.notebooks.rename(notebook_id, title)
    return _serialize_notebook(nb)


@router.delete("/{notebook_id}")
async def delete_notebook(request: Request, notebook_id: str):
    client = require_client(request)
    await client.notebooks.delete(notebook_id)
    return {"deleted": notebook_id}
