// Starts the Kick OAuth login (PKCE + state, per Kick docs)
const crypto = require("crypto");
const { redis } = require("../../lib/redis");
const SITE = "https://roobetcasinorewards.com";

module.exports = async (req, res) => {
  try {
    const verifier = crypto.randomBytes(32).toString("base64url");
    const state = crypto.randomBytes(16).toString("base64url");
    const challenge = crypto.createHash("sha256").update(verifier).digest("base64url");
    await redis("SET", `oauth:${state}`, verifier, "EX", 600); // 10 min to complete login

    const u = new URL("https://id.kick.com/oauth/authorize");
    u.searchParams.set("response_type", "code");
    u.searchParams.set("client_id", process.env.KICK_CLIENT_ID);
    u.searchParams.set("redirect_uri", `${SITE}/api/kick/callback`);
    u.searchParams.set("scope", "user:read");
    u.searchParams.set("code_challenge", challenge);
    u.searchParams.set("code_challenge_method", "S256");
    u.searchParams.set("state", state);
    res.statusCode = 302;
    res.setHeader("Location", u.toString());
    res.end();
  } catch (e) {
    res.statusCode = 302;
    res.setHeader("Location", "/giveaways?login=error#raffle");
    res.end();
  }
};
