"""Batch download jobs: create / get / stream / cancel."""

from __future__ import annotations

import asyncio
import json
import uuid
from pathlib import Path
from typing import Any

from fastapi import APIRouter, Body, HTTPException, Request
from sse_starlette.sse import EventSourceResponse

from ..app import get_state, require_client
from ..jobs import BatchJob, build_items, run_job

router = APIRouter()


@router.post("")
async def create_job(request: Request, payload: dict[str, Any] = Body(...)):
    client = require_client(request)
    state = get_state(request)

    notebook_id = payload.get("notebook_id")
    target_dir = payload.get("target_dir")
    categories = payload.get("categories") or []
    if not notebook_id or not target_dir:
        raise HTTPException(400, "notebook_id and target_dir required")
    if not categories:
        raise HTTPException(400, "no categories selected")

    keep_original = bool(payload.get("keep_original", False))
    legacy_pdf = bool(payload.get("legacy_pdf", False))

    raw_concurrency = payload.get("concurrency", 3)
    try:
        concurrency = int(raw_concurrency)
    except (TypeError, ValueError) as exc:
        raise HTTPException(400, "concurrency must be an integer between 1 and 10") from exc
    if concurrency < 1 or concurrency > 10:
        raise HTTPException(400, "concurrency must be between 1 and 10")

    target_path = Path(target_dir).expanduser().resolve()
    items = await build_items(
        client,
        notebook_id,
        target_path,
        categories,
        keep_original=keep_original,
        legacy_pdf=legacy_pdf,
    )
    if not items:
        raise HTTPException(400, "selection produced no items")

    job = BatchJob(
        job_id=str(uuid.uuid4()),
        notebook_id=notebook_id,
        target_dir=target_path,
        items=items,
        force=bool(payload.get("force", False)),
        concurrency=concurrency,
        keep_original=keep_original,
        legacy_pdf=legacy_pdf,
    )
    state.jobs.add(job)
    job.task = asyncio.create_task(run_job(job))
    return {"job_id": job.job_id, "total_items": job.total, "status": "pending"}


@router.get("/{job_id}")
async def get_job(request: Request, job_id: str):
    state = get_state(request)
    job = state.jobs.get(job_id)
    if not job:
        raise HTTPException(404, "job not found")
    return job.to_dict()


@router.post("/{job_id}/cancel")
async def cancel_job(request: Request, job_id: str):
    state = get_state(request)
    job = state.jobs.get(job_id)
    if not job:
        raise HTTPException(404, "job not found")
    job.cancel_event.set()
    return {"cancelled": job_id}


@router.get("/{job_id}/stream")
async def stream_job(request: Request, job_id: str):
    state = get_state(request)
    job = state.jobs.get(job_id)
    if not job:
        raise HTTPException(404, "job not found")

    async def event_gen():
        # Replay current item snapshot first so reconnects see state.
        for it in job.items:
            yield {"event": "item", "data": json.dumps(it.to_dict())}
        while True:
            ev = await job.queue.get()
            if ev is None:
                return
            yield {"event": ev["event"], "data": json.dumps(ev["data"])}

    return EventSourceResponse(event_gen())
