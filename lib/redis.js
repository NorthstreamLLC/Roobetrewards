// Upstash Redis REST helper (env vars injected by the Vercel integration)
// Auto-detect the REST URL/token pair regardless of the integration's prefix
// (KV_*, STORAGE_*, UPSTASH_REDIS_*, custom prefixes, etc.)
let URL_, TOKEN;
for (const k of Object.keys(process.env)) {
  if (k.endsWith("REST_API_URL")) {
    const t = process.env[k.replace(/URL$/, "TOKEN")];
    if (process.env[k] && t) { URL_ = process.env[k]; TOKEN = t; break; }
  }
  if (k.endsWith("REST_URL")) {
    const t = process.env[k.replace(/REST_URL$/, "REST_TOKEN")];
    if (process.env[k] && t) { URL_ = process.env[k]; TOKEN = t; break; }
  }
}

async function redis(...cmd) {
  if (!URL_ || !TOKEN) throw new Error("redis not configured");
  const r = await fetch(URL_, {
    method: "POST",
    headers: { Authorization: `Bearer ${TOKEN}`, "Content-Type": "application/json" },
    body: JSON.stringify(cmd),
    signal: AbortSignal.timeout(6000),
  });
  if (!r.ok) throw new Error(`redis ${r.status}`);
  const d = await r.json();
  if (d.error) throw new Error(d.error);
  return d.result;
}

module.exports = { redis };
