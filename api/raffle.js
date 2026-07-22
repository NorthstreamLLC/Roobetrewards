// Raffle API — public: view + enter (Kick login required). Admin: create + draw (RAFFLE_ADMIN_KEY).
const crypto = require("crypto");
const { redis } = require("../lib/redis");

const mask = (n) => {
  n = String(n || "player");
  return n.slice(0, 3) + "*".repeat(Math.min(Math.max(n.length - 3, 2), 10));
};

async function session(req) {
  const m = /(?:^|;\s*)rr_sess=([^;]+)/.exec(req.headers.cookie || "");
  if (!m) return null;
  const s = await redis("GET", `sess:${m[1]}`);
  return s ? JSON.parse(s) : null;
}

const current = async () => {
  const c = await redis("GET", "raffle:current");
  return c ? JSON.parse(c) : null;
};

const readBody = (req) => new Promise((rs) => {
  let b = "";
  req.on("data", (c) => (b += c));
  req.on("end", () => { try { rs(JSON.parse(b || "{}")); } catch { rs({}); } });
});

module.exports = async (req, res) => {
  try {
    if (req.method === "GET") {
      const [r, me] = await Promise.all([current(), session(req)]);
      let count = 0, entered = false;
      if (r) {
        count = (await redis("SCARD", `raffle:${r.id}:entries`)) || 0;
        if (me) entered = !!(await redis("SISMEMBER", `raffle:${r.id}:entries`, me.kickId));
      }
      res.setHeader("Cache-Control", "no-store");
      return res.status(200).json({ raffle: r, count, me: me ? { username: me.username } : null, entered });
    }
    if (req.method !== "POST") return res.status(405).json({ error: "method not allowed" });
    const body = await readBody(req);

    if (body.action === "enter") {
      const me = await session(req);
      if (!me) return res.status(401).json({ error: "login required" });
      const r = await current();
      if (!r || r.drawn || Date.now() > r.endsAt) return res.status(400).json({ error: "no open raffle" });
      await redis("SADD", `raffle:${r.id}:entries`, me.kickId);
      await redis("HSET", `raffle:${r.id}:names`, me.kickId, me.username);
      return res.status(200).json({ ok: true, entered: true });
    }

    // ---- admin actions ----
    if (!process.env.RAFFLE_ADMIN_KEY || body.key !== process.env.RAFFLE_ADMIN_KEY) {
      return res.status(403).json({ error: "forbidden" });
    }
    if (body.action === "create") {
      const r = {
        id: Date.now().toString(36),
        title: body.title || "Community Raffle",
        prize: body.prize || "",
        endsAt: new Date(body.endsAt).getTime() || Date.now() + 7 * 864e5,
        winners: [], drawn: false, created: Date.now(),
      };
      await redis("SET", "raffle:current", JSON.stringify(r));
      return res.status(200).json({ ok: true, raffle: r });
    }
    if (body.action === "draw") {
      const r = await current();
      if (!r) return res.status(400).json({ error: "no raffle" });
      const n = Math.max(1, parseInt(body.winners, 10) || 1);
      const ids = (await redis("SMEMBERS", `raffle:${r.id}:entries`)) || [];
      const names = {};
      if (ids.length) {
        const vals = (await redis("HMGET", `raffle:${r.id}:names`, ...ids)) || [];
        ids.forEach((id, i) => (names[id] = vals[i]));
      }
      const pool = [...ids], winners = [];
      while (pool.length && winners.length < n) {
        const i = crypto.randomInt(pool.length); // crypto-secure draw
        winners.push(mask(names[pool[i]]));
        pool.splice(i, 1);
      }
      r.winners = winners; r.drawn = true; r.drawnAt = Date.now();
      await redis("SET", "raffle:current", JSON.stringify(r));
      return res.status(200).json({ ok: true, winners, entries: ids.length });
    }
    if (body.action === "status") {
      const r = await current();
      const count = r ? (await redis("SCARD", `raffle:${r.id}:entries`)) || 0 : 0;
      return res.status(200).json({ raffle: r, count });
    }
    return res.status(400).json({ error: "unknown action" });
  } catch (e) {
    return res.status(200).json({ error: String(e) });
  }
};
