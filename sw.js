const CACHE = "opiskelut-v2";
const SHELL = ["./", "index.html", "manifest.webmanifest", "icon-192.png", "icon-512.png"];
self.addEventListener("install", e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL))); self.skipWaiting(); });
self.addEventListener("activate", e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))); self.clients.claim(); });
self.addEventListener("fetch", e => {
  const u = new URL(e.request.url);
  if (u.origin !== location.origin) return;
  // network first, cache fallback (so updates show up immediately)
  e.respondWith(fetch(e.request).then(r => { if (r.ok && !u.pathname.endsWith("data.enc.json")) { const c = r.clone(); caches.open(CACHE).then(ca => ca.put(e.request, c)); } return r; }).catch(() => caches.match(e.request, {ignoreSearch: true})));
});
