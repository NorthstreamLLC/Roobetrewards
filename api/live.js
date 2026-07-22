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
  });
  if (!r.ok) throw new Error(`token ${r.status}`);
  const d = await r.json();
  tokenCache = { token: d.access_token, exp: Date.now() + (d.expires_in - 60) * 1000 };
  return tokenCache.token;
}

function parseLive(obj) {
  // tolerate both official and unofficial response shapes
  if (!obj) return false;
  const ch = Array.isArray(obj.data) ? obj.data[0] : obj.data || obj;
  if (!ch) return false;
  if (typeof ch.is_live === "boolean") return ch.is_live;
  if (ch.stream && typeof ch.stream.is_live === "boolean") return ch.stream.is_live;
  if ("livestream" in ch) return !!ch.livestream;
  return false;
}

module.exports = async (req, res) => {
  res.setHeader("Cache-Control", "s-maxage=60, stale-while-revalidate=120");
  const id = process.env.KICK_CLIENT_ID, secret = process.env.KICK_CLIENT_SECRET;
  try {
    if (id && secret) {
      const t = await appToken(id, secret);
      const r = await fetch(`https://api.kick.com/public/v1/channels?slug=${CHANNEL}`, {
        headers: { Authorization: `Bearer ${t}` },
      });
      if (!r.ok) throw new Error(`channels ${r.status}`);
      return res.status(200).json({ live: parseLive(await r.json()), src: "official" });
    }
    // fallback: unofficial endpoint
    const r = await fetch(`https://kick.com/api/v2/channels/${CHANNEL}`, {
      headers: { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)", Accept: "application/json" },
    });
    if (!r.ok) throw new Error(`unofficial ${r.status}`);
    return res.status(200).json({ live: parseLive(await r.json()), src: "fallback" });
  } catch (err) {
    return res.status(200).json({ live: null, error: String(err) });
  }
};
