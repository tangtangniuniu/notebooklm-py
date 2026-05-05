// SSE helper with auto-reconnect.
// Usage:
//   const es = sseConnect("/api/jobs/abc/stream", { onEvent: { item: handleItem, complete: handleComplete } });
//   es.close();

export function sseConnect(url, opts = {}) {
  const onEvent = opts.onEvent || {};
  const onError = opts.onError || ((e) => console.warn("SSE error", e));
  const onOpen = opts.onOpen || (() => {});
  let attempt = 0;
  let closed = false;
  let source = null;

  function open() {
    if (closed) return;
    source = new EventSource(url);
    source.onopen = () => {
      attempt = 0;
      onOpen();
    };
    source.onerror = (e) => {
      onError(e);
      if (closed) return;
      // Browser auto-reconnects, but if the connection closes hard we backoff.
      try { source.close(); } catch (_) {}
      const delay = Math.min(1000 * Math.pow(2, attempt++), 15000);
      setTimeout(open, delay);
    };
    for (const [name, handler] of Object.entries(onEvent)) {
      source.addEventListener(name, (ev) => {
        let data = ev.data;
        try { data = JSON.parse(ev.data); } catch (_) {}
        handler(data, ev);
      });
    }
  }
  open();

  return {
    close() {
      closed = true;
      if (source) try { source.close(); } catch (_) {}
    },
  };
}
