"""FastAPI application factory for the local NotebookLM web UI."""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.base import BaseHTTPMiddleware

from .._history import ConversationStore
from ..auth import AuthTokens
from ..client import NotebookLMClient
from ..exceptions import AuthError, NotebookLMError
from .jobs import JobRegistry

logger = logging.getLogger(__name__)

PACKAGE_DIR = Path(__file__).parent
STATIC_DIR = PACKAGE_DIR / "static"
TEMPLATES_DIR = PACKAGE_DIR / "templates"


# ---------------------------------------------------------------- middleware


class LoopbackOnlyMiddleware(BaseHTTPMiddleware):
    """Refuse non-loopback clients at the request level.

    The server should already bind to 127.0.0.1, but this provides a second
    layer of defense and protects against misconfiguration in tests.
    """

    _ALLOWED = {"127.0.0.1", "::1", "localhost", "testclient"}

    async def dispatch(self, request: Request, call_next):
        client = request.client.host if request.client else None
        if client and client not in self._ALLOWED:
            return JSONResponse(
                {"error": "forbidden", "detail": "loopback connections only"},
                status_code=status.HTTP_403_FORBIDDEN,
            )
        return await call_next(request)


# ----------------------------------------------------------------- app state


class AppState:
    """Runtime state carried on `app.state`."""

    def __init__(self) -> None:
        self.client: NotebookLMClient | None = None
        self.auth_error: str | None = None
        self.history = ConversationStore()
        self.jobs = JobRegistry()


# ------------------------------------------------------------- exception → JSON


def _error_response(exc: Exception, default_status: int = 500) -> JSONResponse:
    if isinstance(exc, AuthError):
        return JSONResponse(
            {"error": "auth", "detail": str(exc) or "authentication required"},
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    if isinstance(exc, HTTPException):
        return JSONResponse(
            {"error": "http", "detail": exc.detail},
            status_code=exc.status_code,
        )
    if isinstance(exc, NotebookLMError):
        return JSONResponse(
            {"error": exc.__class__.__name__, "detail": str(exc)},
            status_code=status.HTTP_502_BAD_GATEWAY,
        )
    return JSONResponse(
        {"error": "internal", "detail": str(exc) or "internal error"},
        status_code=default_status,
    )


# ------------------------------------------------------------------- factory


def create_app(*, client: NotebookLMClient | None = None) -> FastAPI:
    """Create and configure the FastAPI app.

    Args:
        client: Pre-built NotebookLMClient (used by tests). If None, the app
            attempts `AuthTokens.from_storage()` at startup.
    """

    state = AppState()
    state.client = client

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        if state.client is None:
            try:
                tokens = await AuthTokens.from_storage()
                state.client = NotebookLMClient(tokens)
                await state.client._core.open()
                state.auth_error = None
            except Exception as e:  # noqa: BLE001 — auth failure is recoverable via UI
                logger.info("Auth not loaded at startup: %s", e)
                state.auth_error = str(e) or "no auth state found"
                state.client = None
        else:
            # Tests may pass a pre-built client; ensure it's open.
            try:
                await state.client._core.open()
            except Exception:
                pass
        try:
            yield
        finally:
            if state.client is not None:
                try:
                    await state.client._core.close()
                except Exception:
                    pass

    app = FastAPI(title="NotebookLM UI", lifespan=lifespan)
    app.state.nb = state
    app.add_middleware(LoopbackOnlyMiddleware)

    # Mount static + templates only if directories exist (always do for the
    # real package; tests can run without templates).
    if STATIC_DIR.exists():
        app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
    if TEMPLATES_DIR.exists():
        app.state.templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
    else:
        app.state.templates = None

    @app.exception_handler(Exception)
    async def _exc_handler(_request: Request, exc: Exception) -> JSONResponse:
        return _error_response(exc)

    @app.exception_handler(HTTPException)
    async def _http_handler(_request: Request, exc: HTTPException) -> JSONResponse:
        return _error_response(exc)

    # Register routes
    from .routes import artifacts, auth, chat, jobs, notebooks, notes, pages, sources

    app.include_router(pages.router)
    app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
    app.include_router(notebooks.router, prefix="/api/notebooks", tags=["notebooks"])
    app.include_router(sources.router, prefix="/api/notebooks", tags=["sources"])
    app.include_router(notes.router, prefix="/api/notebooks", tags=["notes"])
    app.include_router(artifacts.router, prefix="/api/notebooks", tags=["artifacts"])
    app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
    app.include_router(jobs.router, prefix="/api/jobs", tags=["jobs"])

    return app


def get_state(request: Request) -> AppState:
    """Helper for routes to access the shared `AppState`."""
    return request.app.state.nb


def require_client(request: Request) -> NotebookLMClient:
    state = get_state(request)
    if state.client is None:
        raise AuthError(state.auth_error or "not authenticated")
    return state.client
