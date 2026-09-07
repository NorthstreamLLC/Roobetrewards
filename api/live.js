// Vercel serverless — is DailyGambling live on Kick?
// Preferred: official Kick API via app credentials (env vars):
//   KICK_CLIENT_ID / KICK_CLIENT_SECRET  (create app at dev.kick.com)
// Fallback: Kick's public channel endpoint (may be blocked from datacenter IPs).
const CHANNEL = "dailygambling";
let tokenCache = { token: null, exp: 0 };

async function appToken(id, secret) {
  if (tokenCache.token && Date.now() < tokenCache.exp) return tokenCache.token;
  const r = await fetch("https://id.kick.com/oauth/token", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({ grant_type: "client_credentials", client_id: id, client_secret: secret }),
    signal: AbortSignal.timeout(6000),
  });
  if (!r.ok) throw new Error(`token ${r.status}`);
  const d = await r.json();
  tokenCache = { token: d.access_token, exp: Date.now() + (d.expires_in - 60) * 1000 };
  return tokenCache.token;
}

function parseStream(obj) {
  // tolerate both official and unofficial response shapes
  const empty = { live: false, viewers: null, title: null, category: null, started: null };
  if (!obj) return empty;
  const ch = Array.isArray(obj.data) ? obj.data[0] : obj.data || obj;
  if (!ch) return empty;
  const ls = ch.stream || ch.livestream || ch.stream_info || {};
  let live = false;
  if (typeof ch.is_live === "boolean") live = ch.is_live;
  else if (typeof ls.is_live === "boolean") live = ls.is_live;
  else if ("livestream" in ch) live = !!ch.livestream;
  const num = (v) => (typeof v === "number" && v >= 0 ? v : null);
  const viewers = num(ls.viewer_count) ?? num(ls.viewers) ?? num(ch.viewer_count) ?? num(ch.viewers);
  const title = ls.stream_title || ls.session_title || ch.stream_title || ch.slug_title || null;
  const cat =
    (ch.category && (ch.category.name || ch.category)) ||
    (ls.category && (ls.category.name || ls.category)) ||
    (Array.isArray(ch.categories) && ch.categories[0] && ch.categories[0].name) ||
    null;
  const started = ls.start_time || ls.started_at || ls.created_at || ch.start_time || null;
  return { live, viewers: live ? viewers : null, title: live ? title : null,
           category: live ? cat : null, started: live ? started : null };
}

module.exports = async (req, res) => {
  res.setHeader("Cache-Control", "s-maxage=60, stale-while-revalidate=120");
  const id = process.env.KICK_CLIENT_ID, secret = process.env.KICK_CLIENT_SECRET;
  try {
    if (id && secret) {
      const t = await appToken(id, secret);
      const r = await fetch(`https://api.kick.com/public/v1/channels?slug=${CHANNEL}`, {
        headers: { Authorization: `Bearer ${t}` },
        signal: AbortSignal.timeout(6000),
      });
      if (!r.ok) throw new Error(`channels ${r.status}`);
      return res.status(200).json({ ...parseStream(await r.json()), src: "official" });
    }
    // fallback: unofficial endpoint
    const r = await fetch(`https://kick.com/api/v2/channels/${CHANNEL}`, {
      headers: { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)", Accept: "application/json" },
      signal: AbortSignal.timeout(6000),
    });
    if (!r.ok) throw new Error(`unofficial ${r.status}`);
    return res.status(200).json({ ...parseStream(await r.json()), src: "fallback" });
  } catch (err) {
    return res.status(200).json({ live: null, error: String(err) });
  }
};
