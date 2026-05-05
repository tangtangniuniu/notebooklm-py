## Context

The convert-sources-to-markdown change wired Markdown conversion for `WEB_PAGE` / `PDF` / `DOCX` / `PPTX` and direct download for `CSV`. `SourceType.IMAGE` was overlooked — it falls through `_build_source_items`'s tail branch and produces a `<title>.todo` placeholder. Image binaries are silently dropped by the batch downloader.

Two call sites need the fix: `src/notebooklm/web/jobs.py` (orchestrator) and `notebook_batch.py:cmd_source_download` (legacy script). Both already have a "direct download" code path used by `CSV`; we extend it to cover `IMAGE`.

Picking a sensible filename extension is the only non-trivial decision. `Content-Type` is the most reliable signal but not always present; the URL path can have a useful extension; otherwise we need a default.

## Goals / Non-Goals

**Goals:**
- `SourceType.IMAGE` sources download as their original bytes, with a sensible extension, in both call sites.
- Reuse the existing direct-download mechanics — no new HTTP client, no new optional dependency, no new package.
- Tests cover the extension-picker matrix (Content-Type, URL path, default) and an end-to-end orchestrator run.

**Non-Goals:**
- Downloading images embedded inside notes (`![alt](url)` in Markdown content). That's a different feature and would require markdown asset rewriting.
- Re-encoding, resizing, or otherwise modifying the image. Bytes-identical output.
- OCR or markitdown-based conversion of images. (Markdown-from-image was out of scope of the previous change too.)
- Probing the URL with a HEAD request before downloading. We pick the extension during/after the GET so we only do one round-trip.

## Decisions

### D1. Single shared helper for extension picking

Add `_pick_image_extension(url, response) -> str` in `src/notebooklm/conversion/_images.py` (a new sibling to `_files.py` / `_url.py`). Both call sites import it.

```python
_CONTENT_TYPE_EXT = {
    "image/jpeg": ".jpg",
    "image/jpg": ".jpg",
    "image/png": ".png",
    "image/gif": ".gif",
    "image/webp": ".webp",
    "image/svg+xml": ".svg",
    "image/bmp": ".bmp",
    "image/tiff": ".tif",
    "image/x-icon": ".ico",
    "image/heic": ".heic",
    "image/avif": ".avif",
}

def _pick_image_extension(url: str, content_type: str | None) -> str:
    if content_type:
        primary = content_type.split(";", 1)[0].strip().lower()
        if primary in _CONTENT_TYPE_EXT:
            return _CONTENT_TYPE_EXT[primary]
    path = urlparse(url).path
    _, ext = splitext(path)
    if ext and len(ext) <= 6 and ext.lower() in {v for v in _CONTENT_TYPE_EXT.values()}:
        return ext.lower()
    return ".png"
```

We pin to *known* image extensions on the URL-path branch so a malicious / malformed URL like `https://x.example/file.exe` can't trick us into writing `image.exe`. The default (`.png`) is the most common image format and gives a reasonable filename.

The helper takes `content_type` as an opaque string (rather than a full `httpx.Response`) so it's pure and easy to unit-test without HTTP fixtures.

**Alternatives considered:**
- Inline the table inside `web/jobs.py`. **Rejected** — `notebook_batch.py` would need its own copy and they'd drift.
- Use Python's `mimetypes.guess_extension`. **Rejected** — its mapping is platform-dependent (different on macOS/Linux/Windows) and can return surprising results (`.jpe` for JPEG on some systems). A small explicit dict is more predictable.

### D2. New `_make_image_downloader` runner in `web/jobs.py`

Two-phase: open an `httpx.AsyncClient.stream("GET", url)`, peek at the response headers to pick the extension, then rename the orchestrator's pre-built target path before streaming bytes to disk. Returns the strategy string `"image"` so the SSE event surfaces it like the other strategies.

```python
def _make_image_downloader(url, target):
    async def run() -> str | None:
        async with httpx.AsyncClient(...) as client:
            async with client.stream("GET", url) as resp:
                if resp.status_code < 200 or resp.status_code >= 300:
                    raise RuntimeError(f"HTTP {resp.status_code}")
                ext = _pick_image_extension(url, resp.headers.get("content-type"))
                final = target.with_suffix(ext)
                final.parent.mkdir(parents=True, exist_ok=True)
                tmp = final.with_suffix(final.suffix + ".tmp")
                with tmp.open("wb") as fh:
                    async for chunk in resp.aiter_bytes():
                        fh.write(chunk)
                tmp.replace(final)
        return "image"
    return run
```

The orchestrator builds the JobItem with a placeholder target path (e.g. `<title>.img`); the runner rewrites the suffix at runtime. This means `JobItem.target_path` won't match the eventual file path until the runner finishes — a small wrinkle. Mitigation: also expose the final path on `JobItem.message` so the SSE consumer can show it.

**Alternatives considered:**
- HEAD probe first, then build the JobItem with the right path. **Rejected** — doubles the HTTP request count and many image hosts disable HEAD.
- Pre-pick the extension from URL path only, ignore Content-Type. **Rejected** — too many image URLs lack an extension (CDN-style URLs, `?id=...` parameters).

### D3. CSV-style direct passthrough in `notebook_batch.py`

The legacy script already has a CSV branch that calls `urllib.request.urlretrieve`. Extend the type check to include `SourceType.IMAGE` and switch from `urlretrieve` to a small `httpx`-based helper that exposes the response headers (so we can pick the extension). Use the same `_pick_image_extension` helper.

The legacy script logs `[image] {filename}` on success.

### D4. JobItem placeholder path strategy

When the orchestrator builds an image item it writes the JobItem's `target_path` as `<title>.img` (a sentinel). The runner changes the suffix to the real extension and stores the final path on `JobItem.message` along with the strategy:

```python
item.message = f"image:{final.name}"
```

This way the SSE feed can render "image: cover.png" or similar. A client that only cares about the strategy can split on `:` and take the prefix.

Cleaner alternative: extend `JobItem` with a `final_path` attribute. **Rejected for now** — would touch every existing runner just for this one corner case.

## Risks / Trade-offs

- **Mismatched skip-if-exists behavior**: the orchestrator's skip check looks at `target_path` (the placeholder `<title>.img`). The real file lives at `<title>.png` (or similar). Re-running a batch will always re-download images because the placeholder never exists. → Mitigation: in `_build_source_items`, after picking the title, also pre-check the directory for any sibling that matches `<title>.<known-image-ext>` and skip the item upfront if one is present. Documented in tasks.md.
- **CDN URLs without extensions and without Content-Type**: the helper returns `.png`, which may be wrong (e.g. for an actual JPEG). The bytes are still saved correctly; only the filename is suboptimal. We accept this — images render fine in viewers regardless of extension.
- **Very large images** (many MB): we stream the response, so memory is bounded. The orchestrator's existing per-item timeout still applies via `ConversionOptions.timeout`. (Image downloads don't go through the conversion module per se, but we plumb a timeout through anyway.)
- **SVG with embedded `<script>`**: we save it as-is. Users who view the file in a browser get the script behavior. → Mitigation: not our problem — we don't claim to sanitize images; SVG-as-XSS is an upstream concern. Documented in CHANGELOG.

## Migration Plan

1. Add `_pick_image_extension` and `_make_image_downloader` (or extend the orchestrator's existing direct-download flow) — net additions, no other paths affected.
2. Add `SourceType.IMAGE` to `_DIRECT_DOWNLOAD_KINDS` — moves IMAGE from the `.todo` branch into direct download.
3. Update tests + CHANGELOG.
4. Release.

**Rollback**: revert step 2 alone — IMAGE goes back to the `.todo` placeholder. The new helpers stay (unused) and don't affect any other code path.

## Open Questions

- Should we also surface the final image path on the orchestrator's SSE `event: complete` payload (per-item summary)? Currently completion only sends counts. Probably a follow-up; not blocking.
- Is `.png` the right default fallback, or should we go with `.bin`? `.png` is more user-friendly (most viewers will render it). `.bin` is more honest. Sticking with `.png` until a user complains.
