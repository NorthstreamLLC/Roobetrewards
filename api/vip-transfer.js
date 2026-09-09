// VIP transfer requests.
//   POST                      -> submit a request (public)
//   GET    ?key=...           -> list requests (admin)
//   PATCH  ?key=...           -> update status / notes (admin)
//   DELETE ?key=...&id=...    -> remove a request (admin)
//
// Env: VIP_ADMIN_KEY  (+ the Redis vars the raffle already uses)
const { redis } = require("../lib/redis");

const IDX = "vip:index";        // sorted set: score = created ms, member = id
const KEY = (id) => `vip:sub:${id}`;
const STATUSES = ["pending", "in_review", "completed", "rejected"];
const CTRL = new RegExp("[\\u0000-\\u001f\\u007f]+", "g");

const readBody = (req) =>
  new Promise((resolve) => {
    if (req.body && typeof req.body === "object") return resolve(req.body);
    let b = "";
    req.on("data", (c) => (b += c));
    req.on("end", () => {
      try { resolve(JSON.parse(b || "{}")); } catch { resolve({}); }
    });
  });

const ipOf = (req) =>
  (req.headers["x-forwarded-for"] || "").split(",")[0].trim() || "0.0.0.0";

// strip control characters, collapse whitespace, cap length
const clean = (v, max = 120) =>
  String(v == null ? "" : v).replace(CTRL, " ").replace(/\s+/g, " ").trim().slice(0, max);

const isAdmin = (req) => {
  const k = process.env.VIP_ADMIN_KEY;
  if (!k) return false;
  const given = req.headers["x-admin-key"] || (req.query && req.query.key) || "";
  return String(given) === k;
};

const okBlob = (u) =>
  /^https:\/\/[a-z0-9.-]+\.blob\.vercel-storage\.com\//i.test(String(u || ""));

module.exports = async (req, res) => {
  res.setHeader("Cache-Control", "no-store");

  try {
    // ---------------- public: submit ----------------
    if (req.method === "POST") {
      const b = await readBody(req);
      if (clean(b.website)) return res.status(200).json({ ok: true }); // honeypot

      const ip = ipOf(req);
      const rk = `vip:rl:${ip}`;
      const n = await redis("INCR", rk);
      if (n === 1) await redis("EXPIRE", rk, 3600);
      if (n > 5) return res.status(429).json({ error: "Too many requests - try again in an hour." });

      const roobet = clean(b.roobet, 40);
      const prev = clean(b.prevCasino, 60);
      const proof = (Array.isArray(b.proof) ? b.proof : []).filter(okBlob).slice(0, 6);
      const stats = (Array.isArray(b.stats) ? b.stats : []).filter(okBlob).slice(0, 6);

      const missing = [];
      if (!roobet) missing.push("Roobet username");
      if (!prev) missing.push("previous casino");
      if (!proof.length) missing.push("account + code screenshot");
      if (!stats.length) missing.push("previous casino stats screenshot");
      if (missing.length) return res.status(400).json({ error: `Still needed: ${missing.join(", ")}.` });

      const discord = clean(b.discord, 60);
      const telegram = clean(b.telegram, 60).replace(/^@/, "");
      if (!discord && !telegram)
        return res.status(400).json({ error: "Add your Discord or Telegram so we can reach you." });

      const codeIn = clean(b.code, 8).toUpperCase();
      const id = Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
      const sub = {
        id,
        roobet,
        prevCasino: prev,
        discord,
        telegram,
        code: ["DAILY", "ELITE"].includes(codeIn) ? codeIn : "",
        notes: clean(b.notes, 600),
        proof,
        stats,
        status: "pending",
        adminNotes: "",
        created: Date.now(),
        updated: Date.now(),
        ip,
      };

      await redis("SET", KEY(id), JSON.stringify(sub));
      await redis("ZADD", IDX, sub.created, id);
      return res.status(200).json({ ok: true, id, ref: id.toUpperCase() });
    }

    // ---------------- admin ----------------
    if (!isAdmin(req)) return res.status(403).json({ error: "forbidden" });

    if (req.method === "GET") {
      const ids = (await redis("ZRANGE", IDX, 0, -1, "REV")) || [];
      if (!ids.length) return res.status(200).json({ requests: [], counts: { all: 0 } });
      const rows = (await redis("MGET", ...ids.map(KEY))) || [];
      const requests = rows
        .map((r) => { try { return JSON.parse(r); } catch { return null; } })
        .filter(Boolean);
      const counts = requests.reduce((a, r) => ((a[r.status] = (a[r.status] || 0) + 1), a), {});
      counts.all = requests.length;
      return res.status(200).json({ requests, counts });
    }

    if (req.method === "PATCH" || req.method === "PUT") {
      const b = await readBody(req);
      const id = clean(b.id, 40);
      if (!id) return res.status(400).json({ error: "missing id" });
      const raw = await redis("GET", KEY(id));
      if (!raw) return res.status(404).json({ error: "not found" });
      const sub = JSON.parse(raw);
      if (b.status !== undefined) {
        const s = clean(b.status, 20);
        if (!STATUSES.includes(s)) return res.status(400).json({ error: "bad status" });
        sub.status = s;
      }
      if (b.adminNotes !== undefined) sub.adminNotes = clean(b.adminNotes, 1000);
      sub.updated = Date.now();
      await redis("SET", KEY(id), JSON.stringify(sub));
      return res.status(200).json({ ok: true, request: sub });
    }

    if (req.method === "DELETE") {
      const id = clean((req.query && req.query.id) || "", 40);
      if (!id) return res.status(400).json({ error: "missing id" });
      await redis("DEL", KEY(id));
      await redis("ZREM", IDX, id);
      return res.status(200).json({ ok: true });
    }

    return res.status(405).json({ error: "method not allowed" });
  } catch (e) {
    return res.status(500).json({ error: String(e && e.message ? e.message : e) });
  }
};
