"""Auth status + refresh endpoints."""

from __future__ import annotations

from fastapi import APIRouter, Request

from ...auth import AuthTokens
from ...client import NotebookLMClient
from ..app import get_state

router = APIRouter()


@router.get("/status")
async def status(request: Request):
    state = get_state(request)
    return {
        "authenticated": state.client is not None,
        "detail": state.auth_error,
    }


@router.post("/refresh")
async def refresh(request: Request):
    state = get_state(request)
    # Try to (re)load storage state; if a client already exists, refresh tokens.
    try:
        if state.client is None:
            tokens = await AuthTokens.from_storage()
            state.client = NotebookLMClient(tokens)
            await state.client._core.open()
        await state.client.refresh_auth()
        state.auth_error = None
        return {"authenticated": True}
    except Exception as e:  # noqa: BLE001
        state.auth_error = str(e)
        state.client = None
        return {"authenticated": False, "detail": str(e)}
