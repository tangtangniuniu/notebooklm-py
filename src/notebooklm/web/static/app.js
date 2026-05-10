// notebooklm-py UI — page-level glue. Vanilla ES modules, no framework.
import { sseConnect } from "./sse.js";

// ---------- API helper ----------
async function api(path, opts = {}) {
  const init = {
    method: opts.method || "GET",
    headers: { "Content-Type": "application/json" },
    ...opts,
  };
  if (opts.body && typeof opts.body !== "string" && !(opts.body instanceof FormData)) {
    init.body = JSON.stringify(opts.body);
  } else if (opts.body) {
    init.body = opts.body;
    if (opts.body instanceof FormData) delete init.headers["Content-Type"];
  }
  const res = await fetch(path, init);
  const text = await res.text();
  let json = null;
  try { json = text ? JSON.parse(text) : null; } catch (_) {}
  if (!res.ok) {
    if (res.status === 401) showAuthBanner(json && json.detail);
    const err = new Error((json && json.detail) || res.statusText);
    err.status = res.status;
    err.body = json;
    throw err;
  }
  return json;
}
window._api = api;

function el(tag, attrs = {}, ...children) {
  const node = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === "class") node.className = v;
    else if (k === "html") node.innerHTML = v;
    else if (k === "on") {
      for (const [evName, fn] of Object.entries(v)) node.addEventListener(evName, fn);
    } else if (v !== false && v != null) node.setAttribute(k, v);
  }
  for (const c of children) {
    if (c == null || c === false) continue;
    node.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
  }
  return node;
}
function escapeHtml(s) {
  return String(s ?? "").replace(/[&<>"']/g, (c) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
  }[c]));
}

// ---------- Auth banner ----------
function showAuthBanner(detail) {
  const b = document.getElementById("auth-banner");
  if (!b) return;
  b.classList.remove("hidden");
  const d = b.querySelector(".detail");
  if (d) d.textContent = detail || "Not signed in. Run `notebooklm login` in your terminal, then click Refresh.";
  document.querySelectorAll("[data-auth-required]").forEach((n) => (n.disabled = true));
}
function hideAuthBanner() {
  const b = document.getElementById("auth-banner");
  if (b) b.classList.add("hidden");
  document.querySelectorAll("[data-auth-required]").forEach((n) => (n.disabled = false));
}

async function refreshAuth() {
  try {
    await api("/api/auth/refresh", { method: "POST" });
    hideAuthBanner();
    location.reload();
  } catch (e) {
    showAuthBanner(e.message);
  }
}

async function checkAuth() {
  try {
    const status = await api("/api/auth/status");
    if (status.authenticated) hideAuthBanner();
    else showAuthBanner(status.detail);
  } catch (_) { /* showAuthBanner already invoked by api() on 401 */ }
}

// ---------- Source-type icons ----------
const SRC_ICON = {
  pdf: "📄", docx: "📝", csv: "🗂", web_page: "🌐", youtube: "▶",
  pasted_text: "✏", markdown: "📑", google_docs: "📘", google_slides: "📊",
  google_spreadsheet: "📈", image: "🖼", media: "🎞", unknown: "📎",
};

// ---------- Notebook view ----------
let CURRENT_NB = null;
let CURRENT_CONV = null;
let SELECTED_SOURCE_IDS = new Set();

async function loadNotebook(id) {
  CURRENT_NB = id;
  await Promise.all([loadSources(), loadArtifacts(), startNewConversation()]);
}

async function loadSources() {
  const panel = document.getElementById("sources-list");
  if (!panel) return;
  panel.innerHTML = '<div class="muted" style="padding:12px">Loading…</div>';
  try {
    const { sources } = await api(`/api/notebooks/${CURRENT_NB}/sources`);
    panel.innerHTML = "";
    if (sources.length === 0) {
      panel.innerHTML = '<div class="muted" style="padding:12px">No sources yet. Click "Add source".</div>';
      return;
    }
    const filterText = (document.getElementById("source-search")?.value || "").toLowerCase();
    sources
      .filter((s) => !filterText || (s.title || "").toLowerCase().includes(filterText))
      .forEach((s) => panel.appendChild(renderSourceRow(s)));
  } catch (e) {
    panel.innerHTML = `<div class="banner">${escapeHtml(e.message)}</div>`;
  }
}

function renderSourceRow(src) {
  const icon = SRC_ICON[src.kind] || "📎";
  const checkbox = el("input", {
    type: "checkbox",
    "data-src-id": src.id,
    on: {
      click: (e) => e.stopPropagation(),
      change: (e) => {
        if (e.target.checked) SELECTED_SOURCE_IDS.add(src.id);
        else SELECTED_SOURCE_IDS.delete(src.id);
        updateBulkBar();
      },
    },
  });
  const deleteBtn = el("button", {
    class: "btn-icon",
    title: "Delete",
    on: {
      click: (e) => {
        e.stopPropagation();
        deleteSource(src.id);
      },
    },
  }, "×");
  const row = el(
    "div",
    {
      class: "list-item",
      style: "cursor: pointer;",
      title: src.url ? "Open URL in new tab" : "View content",
      on: { click: () => openSource(src) },
    },
    checkbox,
    el("div", { class: "icon" }, icon),
    el(
      "div",
      { class: "meta" },
      el("div", { class: "title" }, src.title || "(untitled)"),
      el("div", { class: "subtitle" }, src.kind + (src.url ? ` · ${shortenUrl(src.url)}` : "")),
    ),
    el("div", { class: "actions" }, deleteBtn),
  );
  return row;
}

function openSource(src) {
  if (src.url) {
    window.open(src.url, "_blank", "noopener,noreferrer");
    return;
  }
  openSourceViewModal(src);
}

async function openSourceViewModal(src) {
  const modal = document.getElementById("source-view-modal");
  const titleEl = document.getElementById("source-view-title");
  const metaEl = document.getElementById("source-view-meta");
  const contentEl = document.getElementById("source-view-content");
  titleEl.textContent = src.title || "(untitled)";
  metaEl.textContent = `${src.kind}`;
  contentEl.textContent = "Loading…";
  modal.classList.remove("hidden");
  try {
    const ft = await api(`/api/notebooks/${CURRENT_NB}/sources/${src.id}/fulltext`);
    contentEl.textContent = ft.content || "(empty)";
    const parts = [ft.kind];
    if (ft.char_count != null) parts.push(`${ft.char_count} chars`);
    metaEl.textContent = parts.join(" · ");
  } catch (e) {
    contentEl.textContent = `Error: ${e.message}`;
  }
}

function closeSourceViewModal() {
  document.getElementById("source-view-modal").classList.add("hidden");
}

function shortenUrl(u) {
  try { return new URL(u).hostname; } catch (_) { return u.slice(0, 40); }
}

function updateBulkBar() {
  const bar = document.getElementById("bulk-bar");
  if (!bar) return;
  const n = SELECTED_SOURCE_IDS.size;
  if (n === 0) bar.classList.add("hidden");
  else {
    bar.classList.remove("hidden");
    bar.querySelector(".count").textContent = `${n} selected`;
  }
}

async function deleteSource(id) {
  if (!confirm("Delete this source?")) return;
  try {
    await api(`/api/notebooks/${CURRENT_NB}/sources/${id}`, { method: "DELETE" });
    SELECTED_SOURCE_IDS.delete(id);
    updateBulkBar();
    await loadSources();
  } catch (e) {
    alert(e.message);
  }
}

async function bulkDeleteSources() {
  const ids = [...SELECTED_SOURCE_IDS];
  if (ids.length === 0) return;
  if (!confirm(`Delete ${ids.length} sources?`)) return;
  for (const id of ids) {
    try { await api(`/api/notebooks/${CURRENT_NB}/sources/${id}`, { method: "DELETE" }); } catch (_) {}
  }
  SELECTED_SOURCE_IDS.clear();
  updateBulkBar();
  await loadSources();
}

// ---------- Add source modal ----------
function openAddSourceModal() {
  const m = document.getElementById("add-source-modal");
  m.classList.remove("hidden");
  m.querySelector('[data-tab="url"]').click();
}
function closeAddSourceModal() {
  document.getElementById("add-source-modal").classList.add("hidden");
}

async function submitAddSource(kind) {
  const root = document.getElementById("add-source-modal");
  const btn = root.querySelector(".btn-primary");
  btn.disabled = true;
  try {
    if (kind === "url" || kind === "youtube") {
      const url = root.querySelector(`#add-${kind}-input`).value.trim();
      if (!url) return;
      await api(`/api/notebooks/${CURRENT_NB}/sources`, {
        method: "POST",
        body: { type: "url", value: url },
      });
    } else if (kind === "text") {
      const title = root.querySelector("#add-text-title").value.trim() || "Pasted text";
      const content = root.querySelector("#add-text-content").value;
      await api(`/api/notebooks/${CURRENT_NB}/sources`, {
        method: "POST",
        body: { type: "text", title, content },
      });
    } else if (kind === "file") {
      const f = root.querySelector("#add-file-input").files[0];
      if (!f) return;
      const fd = new FormData();
      fd.append("file", f);
      await api(`/api/notebooks/${CURRENT_NB}/sources/file`, { method: "POST", body: fd });
    }
    closeAddSourceModal();
    await loadSources();
  } catch (e) {
    alert(e.message);
  } finally {
    btn.disabled = false;
  }
}

// ---------- Dedup modal ----------
async function openDedupModal() {
  const root = document.getElementById("dedup-modal");
  root.classList.remove("hidden");
  const body = root.querySelector(".modal-body");
  body.innerHTML = '<div class="muted">Scanning…</div>';
  try {
    const { groups } = await api(`/api/notebooks/${CURRENT_NB}/sources/dedup-preview`);
    if (groups.length === 0) {
      body.innerHTML = '<div class="muted">No duplicates found.</div>';
      return;
    }
    body.innerHTML = "";
    groups.forEach((g, gi) => {
      const wrap = el("div", { class: "field" });
      wrap.appendChild(el("label", {}, `Group ${gi + 1}: ${g.title || "(untitled)"} (${g.kind})`));
      g.sources.forEach((s, si) => {
        const isKeep = si === g.sources.length - 1;
        const cb = el("input", {
          type: "checkbox",
          "data-id": s.id,
          ...(isKeep ? {} : { checked: "checked" }),
        });
        wrap.appendChild(el("div", { class: "list-item" }, cb,
          el("div", { class: "meta" },
            el("div", { class: "title" }, s.id.slice(0, 8)),
            el("div", { class: "subtitle" }, isKeep ? "keep (latest)" : "delete"))));
      });
      body.appendChild(wrap);
    });
  } catch (e) {
    body.innerHTML = `<div class="banner">${escapeHtml(e.message)}</div>`;
  }
}
function closeDedupModal() {
  document.getElementById("dedup-modal").classList.add("hidden");
}
async function confirmDedup() {
  const root = document.getElementById("dedup-modal");
  const ids = [...root.querySelectorAll("input[type=checkbox]:checked")].map((c) => c.dataset.id);
  if (ids.length === 0) { closeDedupModal(); return; }
  if (!confirm(`Delete ${ids.length} duplicate sources?`)) return;
  for (const id of ids) {
    try { await api(`/api/notebooks/${CURRENT_NB}/sources/${id}`, { method: "DELETE" }); } catch (_) {}
  }
  closeDedupModal();
  await loadSources();
}

// ---------- Studio / Artifacts ----------
async function loadArtifacts() {
  const panel = document.getElementById("artifacts-list");
  if (!panel) return;
  panel.innerHTML = '<div class="muted" style="padding:12px">Loading…</div>';
  try {
    const { artifacts } = await api(`/api/notebooks/${CURRENT_NB}/artifacts`);
    const groups = {};
    for (const a of artifacts) {
      groups[a.kind] = groups[a.kind] || [];
      groups[a.kind].push(a);
    }
    panel.innerHTML = "";
    const order = ["audio", "video", "report", "slide_deck", "infographic", "mind_map", "data_table", "quiz", "flashcards"];
    for (const kind of order) {
      const list = groups[kind] || [];
      const grp = el("div", { class: "artifact-group" });
      grp.appendChild(el("h4", {}, kind.replace("_", " ")));
      if (list.length === 0) {
        grp.appendChild(el("div", { class: "muted", style: "font-size:12px" }, "(none)"));
      } else {
        for (const a of list) {
          const card = el("div", { class: "artifact-card" },
            el("div", { class: "icon" }, kindIcon(kind)),
            el("div", { class: "meta" },
              el("div", { class: "title" }, a.title || kind),
              el("div", { class: "status" }, a.status_str)));
          grp.appendChild(card);
        }
      }
      panel.appendChild(grp);
    }
  } catch (e) {
    panel.innerHTML = `<div class="banner">${escapeHtml(e.message)}</div>`;
  }
}
function kindIcon(k) {
  return { audio: "🎧", video: "🎬", report: "📋", slide_deck: "🎞", infographic: "🖼",
           mind_map: "🧠", data_table: "📊", quiz: "❓", flashcards: "🃏" }[k] || "✨";
}

// ---------- Chat ----------
async function startNewConversation() {
  CURRENT_CONV = crypto.randomUUID();
  const hist = document.getElementById("chat-history");
  if (hist) {
    hist.innerHTML = `
      <div class="chat-empty">
        <div class="big">Ask anything about this notebook.</div>
        <div>Your conversation is auto-saved and can be exported as Markdown.</div>
      </div>`;
  }
}

async function sendQuestion() {
  const input = document.getElementById("chat-input");
  const q = input.value.trim();
  if (!q) return;
  input.value = "";
  input.style.height = "auto";

  const hist = document.getElementById("chat-history");
  hist.querySelector(".chat-empty")?.remove();
  const turn = el("div", { class: "turn" });
  turn.appendChild(el("div", { class: "question" }, q));
  const ans = el("div", { class: "answer streaming" }, "");
  turn.appendChild(ans);
  hist.appendChild(turn);
  hist.scrollTop = hist.scrollHeight;

  try {
    const result = await api(`/api/chat/${CURRENT_CONV}/ask`, {
      method: "POST",
      body: { notebook_id: CURRENT_NB, question: q },
    });
    ans.classList.remove("streaming");
    ans.textContent = result.answer || "(no answer)";
    if (result.citations && result.citations.length > 0) {
      const c = el("div", { class: "citations" }, "Sources: ");
      result.citations.forEach((cite, i) => {
        const sup = el("a", { href: "#", title: cite.cited_text || "" }, `[${i + 1}]`);
        c.appendChild(sup);
      });
      turn.appendChild(c);
    }
    hist.scrollTop = hist.scrollHeight;
    if (result.conversation_id) CURRENT_CONV = result.conversation_id;
  } catch (e) {
    ans.classList.remove("streaming");
    ans.textContent = `Error: ${e.message}`;
  }
}

async function openConversationsDrawer() {
  const drawer = document.getElementById("conversations-drawer");
  drawer.classList.add("open");
  const body = drawer.querySelector(".drawer-body");
  body.innerHTML = '<div class="muted" style="padding:12px">Loading…</div>';
  try {
    const { conversations } = await api(
      `/api/chat/conversations?notebook_id=${encodeURIComponent(CURRENT_NB)}`,
    );
    body.innerHTML = "";
    if (conversations.length === 0) {
      body.innerHTML = '<div class="muted" style="padding:12px">No conversations yet.</div>';
      return;
    }
    for (const c of conversations) {
      const row = el("div", { class: "list-item", on: { click: () => replayConversation(c.conversation_id) } },
        el("div", { class: "icon" }, "💬"),
        el("div", { class: "meta" },
          el("div", { class: "title" }, `${c.turn_count} turn${c.turn_count === 1 ? "" : "s"}`),
          el("div", { class: "subtitle" }, formatDate(c.ended_at))));
      body.appendChild(row);
    }
  } catch (e) {
    body.innerHTML = `<div class="banner">${escapeHtml(e.message)}</div>`;
  }
}
function closeConversationsDrawer() {
  document.getElementById("conversations-drawer").classList.remove("open");
}

async function replayConversation(convId) {
  CURRENT_CONV = convId;
  const hist = document.getElementById("chat-history");
  hist.innerHTML = '<div class="muted" style="padding:12px">Loading…</div>';
  closeConversationsDrawer();
  try {
    const { turns } = await api(
      `/api/chat/conversations/${convId}?notebook_id=${encodeURIComponent(CURRENT_NB)}`,
    );
    hist.innerHTML = "";
    for (const t of turns) {
      const turn = el("div", { class: "turn" },
        el("div", { class: "question" }, t.question),
        el("div", { class: "answer" }, t.answer));
      hist.appendChild(turn);
    }
    hist.scrollTop = hist.scrollHeight;
  } catch (e) {
    hist.innerHTML = `<div class="banner">${escapeHtml(e.message)}</div>`;
  }
}

function exportConversation() {
  if (!CURRENT_CONV || !CURRENT_NB) return;
  window.location.href =
    `/api/chat/conversations/${CURRENT_CONV}/export?notebook_id=${encodeURIComponent(CURRENT_NB)}`;
}

function formatDate(iso) {
  if (!iso) return "";
  try { return new Date(iso).toLocaleString(); } catch (_) { return iso; }
}

// ---------- Batch download ----------
const CATEGORIES = [
  ["sources", "Sources"], ["audio", "Audio"], ["video", "Video"],
  ["slide-deck", "Slide deck"], ["infographic", "Infographic"], ["report", "Report"],
  ["mind-map", "Mind map"], ["data-table", "Data table"], ["quiz", "Quiz"],
  ["flashcards", "Flashcards"], ["notes", "Notes"],
];

function openBatchModal() {
  const m = document.getElementById("batch-modal");
  m.classList.remove("hidden");
  const wrap = m.querySelector(".categories");
  wrap.innerHTML = "";
  for (const [k, label] of CATEGORIES) {
    const id = `cat-${k}`;
    wrap.appendChild(
      el("label", { class: "list-item", style: "cursor:pointer" },
        el("input", { type: "checkbox", id, value: k, checked: "checked" }),
        el("div", { class: "meta" }, label)),
    );
  }
}
function closeBatchModal() {
  document.getElementById("batch-modal").classList.add("hidden");
}

async function startBatchDownload() {
  const m = document.getElementById("batch-modal");
  const target = m.querySelector("#batch-target").value.trim();
  if (!target) { alert("Enter a target directory."); return; }
  const force = m.querySelector("#batch-force").checked;
  const concurrency = parseInt(m.querySelector("#batch-concurrency").value, 10);
  const categories = [...m.querySelectorAll(".categories input:checked")].map((i) => i.value);
  if (categories.length === 0) { alert("Select at least one category."); return; }
  try {
    const job = await api("/api/jobs", {
      method: "POST",
      body: { notebook_id: CURRENT_NB, target_dir: target, categories, force, concurrency },
    });
    closeBatchModal();
    openJobDrawer(job.job_id);
  } catch (e) {
    alert(e.message);
  }
}

let CURRENT_JOB_SSE = null;
async function openJobDrawer(jobId) {
  const drawer = document.getElementById("job-drawer");
  drawer.classList.add("open");
  const body = drawer.querySelector(".drawer-body");
  body.innerHTML = `
    <div class="job-summary">Job <code>${jobId.slice(0, 8)}</code> — <span class="status">starting…</span></div>
    <div class="job-rows"></div>`;
  drawer.dataset.jobId = jobId;

  if (CURRENT_JOB_SSE) CURRENT_JOB_SSE.close();
  const rows = body.querySelector(".job-rows");
  const status = body.querySelector(".status");
  CURRENT_JOB_SSE = sseConnect(`/api/jobs/${jobId}/stream`, {
    onEvent: {
      item: (data) => upsertJobRow(rows, data),
      progress: (data) => upsertJobRow(rows, { ...data, status: "running" }),
      complete: (data) => {
        status.textContent =
          `Complete — done: ${data.done}, skipped: ${data.skipped}, error: ${data.error}, total: ${data.total}`;
        if (CURRENT_JOB_SSE) CURRENT_JOB_SSE.close();
      },
    },
  });
}
function closeJobDrawer() {
  document.getElementById("job-drawer").classList.remove("open");
  if (CURRENT_JOB_SSE) CURRENT_JOB_SSE.close();
}
async function cancelCurrentJob() {
  const id = document.getElementById("job-drawer").dataset.jobId;
  if (!id) return;
  try { await api(`/api/jobs/${id}/cancel`, { method: "POST" }); } catch (e) { alert(e.message); }
}

function upsertJobRow(parent, data) {
  let row = parent.querySelector(`[data-id="${data.item_id}"]`);
  if (!row) {
    row = el("div", { class: "job-row", "data-id": data.item_id },
      el("div", { class: "icon" }, ""),
      el("span", { class: "badge" }, data.status),
      el("div", { class: "meta" },
        el("div", { class: "title" }, data.label),
        el("div", { class: "subtitle muted" }, data.category)),
      el("div", { class: "msg muted" }, data.message || ""));
    parent.appendChild(row);
  } else {
    const badge = row.querySelector(".badge");
    badge.textContent = data.status;
    badge.className = `badge ${data.status}`;
    row.querySelector(".msg").textContent = data.message || "";
  }
}

// ---------- Wire up ----------
function wireUp() {
  document.getElementById("auth-refresh-btn")?.addEventListener("click", refreshAuth);
  document.getElementById("source-search")?.addEventListener("input", () => loadSources());
  document.getElementById("add-source-btn")?.addEventListener("click", openAddSourceModal);
  document.getElementById("dedup-btn")?.addEventListener("click", openDedupModal);
  document.getElementById("bulk-delete-btn")?.addEventListener("click", bulkDeleteSources);

  document.getElementById("send-btn")?.addEventListener("click", sendQuestion);
  document.getElementById("chat-input")?.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendQuestion();
    }
  });
  document.getElementById("new-conv-btn")?.addEventListener("click", startNewConversation);
  document.getElementById("conv-list-btn")?.addEventListener("click", openConversationsDrawer);
  document.getElementById("export-md-btn")?.addEventListener("click", exportConversation);
  document.getElementById("close-conv-drawer")?.addEventListener("click", closeConversationsDrawer);

  document.getElementById("batch-btn")?.addEventListener("click", openBatchModal);
  document.getElementById("close-batch-modal")?.addEventListener("click", closeBatchModal);
  document.getElementById("start-batch-btn")?.addEventListener("click", startBatchDownload);
  document.getElementById("close-job-drawer")?.addEventListener("click", closeJobDrawer);
  document.getElementById("cancel-job-btn")?.addEventListener("click", cancelCurrentJob);

  document.querySelectorAll(".tabbar button").forEach((b) => {
    b.addEventListener("click", () => {
      document.querySelectorAll(".tabbar button").forEach((x) => x.classList.remove("active"));
      b.classList.add("active");
      const target = b.dataset.tab;
      document.querySelectorAll(".panel").forEach((p) => {
        p.classList.toggle("hidden-mobile", p.dataset.tab !== target);
      });
    });
  });

  // Add-source modal tabs
  const m = document.getElementById("add-source-modal");
  if (m) {
    m.querySelectorAll(".modal-tabs button").forEach((b) => {
      b.addEventListener("click", () => {
        const target = b.dataset.tab;
        m.querySelectorAll(".modal-tabs button").forEach((x) => x.classList.toggle("active", x === b));
        m.querySelectorAll("[data-pane]").forEach((p) => p.classList.toggle("hidden", p.dataset.pane !== target));
        const submit = m.querySelector(".btn-primary");
        submit.dataset.kind = target;
      });
    });
    m.querySelector(".btn-primary")?.addEventListener("click", (e) => submitAddSource(e.target.dataset.kind || "url"));
    m.querySelector(".close-btn")?.addEventListener("click", closeAddSourceModal);
  }

  document.getElementById("close-dedup-modal")?.addEventListener("click", closeDedupModal);
  document.getElementById("confirm-dedup-btn")?.addEventListener("click", confirmDedup);
  document.getElementById("close-source-view-modal")?.addEventListener("click", closeSourceViewModal);
  document.getElementById("close-source-view-btn")?.addEventListener("click", closeSourceViewModal);
  document.getElementById("source-view-modal")?.addEventListener("click", (e) => {
    if (e.target.id === "source-view-modal") closeSourceViewModal();
  });
}

document.addEventListener("DOMContentLoaded", () => {
  wireUp();
  checkAuth();
  if (window.NB_ID) loadNotebook(window.NB_ID);
});
