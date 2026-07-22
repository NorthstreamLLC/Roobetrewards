// Kick OAuth callback: verify state, exchange code (PKCE), create session cookie
const crypto = require("crypto");
const { redis } = require("../../lib/redis");
const SITE = "https://roobetcasinorewards.com";

module.exports = async (req, res) => {
  try {
    const q = new URL(req.url, SITE).searchParams;
    const code = q.get("code"), state = q.get("state");
    const verifier = state && (await redis("GET", `oauth:${state}`));
    if (!code || !verifier) throw new Error("invalid state");
    await redis("DEL", `oauth:${state}`);

    const tr = await fetch("https://id.kick.com/oauth/token", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams({
        grant_type: "authorization_code",
        client_id: process.env.KICK_CLIENT_ID,
        client_secret: process.env.KICK_CLIENT_SECRET,
        redirect_uri: `${SITE}/api/kick/callback`,
        code_verifier: verifier,
        code,
      }),
      signal: AbortSignal.timeout(8000),
    });
    if (!tr.ok) throw new Error(`token ${tr.status}`);
    const tok = (await tr.json()).access_token;

    const ur = await fetch("https://api.kick.com/public/v1/users", {
      headers: { Authorization: `Bearer ${tok}` },
      signal: AbortSignal.timeout(8000),
    });
    if (!ur.ok) throw new Error(`user ${ur.status}`);
    const ud = await ur.json();
    const u0 = (Array.isArray(ud.data) ? ud.data[0] : ud.data) || {};
    const kickId = String(u0.user_id ?? u0.id ?? "");
    const username = String(u0.name ?? u0.username ?? "kick_user");
    if (!kickId) throw new Error("no user id");

    const sid = crypto.randomBytes(24).toString("base64url");
    await redis("SET", `sess:${sid}`, JSON.stringify({ kickId, username }), "EX", 604800); // 7 days
    res.setHeader("Set-Cookie",
      `rr_sess=${sid}; Domain=.roobetcasinorewards.com; Path=/; Max-Age=604800; HttpOnly; Secure; SameSite=Lax`);
    res.statusCode = 302;
    res.setHeader("Location", "/giveaways#raffle");
    res.end();
  } catch (e) {
    res.statusCode = 302;
    res.setHeader("Location", "/giveaways?login=failed#raffle");
    res.end();
  }
};
