"""HTML pages: notebook picker, notebook view."""

from __future__ import annotations

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from ..app import get_state

router = APIRouter()


def _templates(request: Request) -> Jinja2Templates | None:
    return request.app.state.templates


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    templates = _templates(request)
    if templates is None:
        return HTMLResponse("<p>UI templates not installed.</p>")
    state = get_state(request)
    auth_ok = state.client is not None
    return templates.TemplateResponse(
        request,
        "picker.html",
        {"auth_ok": auth_ok, "auth_detail": state.auth_error},
    )


@router.get("/notebook/{notebook_id}", response_class=HTMLResponse)
async def notebook_view(request: Request, notebook_id: str):
    templates = _templates(request)
    if templates is None:
        return HTMLResponse("<p>UI templates not installed.</p>")
    state = get_state(request)
    auth_ok = state.client is not None
    return templates.TemplateResponse(
        request,
        "notebook.html",
        {
            "notebook_id": notebook_id,
            "auth_ok": auth_ok,
            "auth_detail": state.auth_error,
        },
    )


@router.get("/healthz")
async def healthz():
    return JSONResponse({"ok": True})
