// Max Win Merch claims.
//   POST                      -> submit a claim (public)
//   GET    ?key=...           -> list claims (admin)
//   PATCH  ?key=...           -> update status / notes (admin)
//   DELETE ?key=...&id=...    -> remove a claim (admin)
//
// Env: VIP_ADMIN_KEY (same key as the VIP transfer panel) + the Redis vars
//      MERCH_PARTNER_KEY (optional): shared with maxwinmerch.com, whose claim form
//      forwards here server-to-server with the header x-partner-key. A partner
//      claim follows the SlotEssentials rules (a replay link, not a screenshot;
//      base bet >= $0.20) and carries an email and shipping address instead of
//      Discord/Telegram. Without the key, the endpoint behaves exactly as before.
const { redis } = require("../lib/redis");

const IDX = "merch:index";
const KEY = (id) => `merch:claim:${id}`;
const STATUSES = ["pending", "verified", "shipped", "rejected"];
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

const clean = (v, max = 120) =>
  String(v == null ? "" : v).replace(CTRL, " ").replace(/\s+/g, " ").trim().slice(0, max);

const isAdmin = (req) => {
  const k = process.env.VIP_ADMIN_KEY;
  if (!k) return false;
  const given = req.headers["x-admin-key"] || (req.query && req.query.key) || "";
  return String(given) === k;
};

const isPartner = (req) => {
  const k = process.env.MERCH_PARTNER_KEY;
  return !!k && String(req.headers["x-partner-key"] || "") === k;
};

const okReplay = (u) => /^https:\/\/[^\s]+$/i.test(String(u || "")) && String(u).length <= 500;

const okBlob = (u) =>
  /^https:\/\/[a-z0-9.-]+\.blob\.vercel-storage\.com\//i.test(String(u || ""));

// A claim forwarded by maxwinmerch.com. Same record and admin queue as the
// site's own claims, flagged with source so the panel can tell them apart.
async function partnerClaim(b, res) {
  const ip = clean(b.clientIp, 45) || "0.0.0.0";
  const rk = `merch:rl:p:${ip}`;
  const n = await redis("INCR", rk);
  if (n === 1) await redis("EXPIRE", rk, 3600);
  if (n > 8) return res.status(429).json({ error: "Too many claims - try again in an hour." });

  const roobet = clean(b.roobet, 40);
  const shirt = clean(b.shirt, 80);
  const size = clean(b.size, 6);
  const replay = okReplay(b.replay) ? String(b.replay).trim() : "";
  const email = clean(b.email, 254);
  const baseBet = Number(b.baseBet);
  const missing = [];
  if (!roobet) missing.push("Roobet username");
  if (!shirt) missing.push("shirt");
  if (!size) missing.push("size");
  if (!replay) missing.push("replay link");
  if (!/^[^\s@]+@[^\s@]+\.[a-z]{2,}$/i.test(email)) missing.push("email");
  if (missing.length) return res.status(400).json({ error: `Still needed: ${missing.join(", ")}.` });
  if (!(baseBet >= 0.2)) return res.status(400).json({ error: "The base bet has to be at least $0.20 USD." });

  const s = b.shipping && typeof b.shipping === "object" ? b.shipping : {};
  const id = Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
  const claim = {
    id, roobet, shirt, size,
    color: clean(b.color, 30),
    discord: "", telegram: "",
    email,
    source: "maxwinmerch",
    slot: clean(b.slot, 80),
    baseBet,
    replay,
    shipping: {
      name: clean(s.name, 100), phone: clean(s.phone, 40),
      address1: clean(s.address1, 160), address2: clean(s.address2, 160),
      city: clean(s.city, 80), postcode: clean(s.postcode, 20), country: clean(s.country, 60),
    },
    notes: clean(b.notes, 600),
    proof: [],
    status: "pending",
    adminNotes: "",
    created: Date.now(),
    updated: Date.now(),
    ip,
  };
  await redis("SET", KEY(claim.id), JSON.stringify(claim));
  await redis("ZADD", IDX, claim.created, claim.id);
  return res.status(200).json({ ok: true, id: claim.id, ref: claim.id.toUpperCase() });
}

module.exports = async (req, res) => {
  res.setHeader("Cache-Control", "no-store");

  try {
    if (req.method === "POST") {
      const b = await readBody(req);
      if (clean(b.website)) return res.status(200).json({ ok: true }); // honeypot

      if (isPartner(req)) return partnerClaim(b, res);

      const ip = ipOf(req);
      const rk = `merch:rl:${ip}`;
      const n = await redis("INCR", rk);
      if (n === 1) await redis("EXPIRE", rk, 3600);
      if (n > 8) return res.status(429).json({ error: "Too many claims - try again in an hour." });

      const roobet = clean(b.roobet, 40);
      const shirt = clean(b.shirt, 80);
      const size = clean(b.size, 6);
      const proof = (Array.isArray(b.proof) ? b.proof : []).filter(okBlob).slice(0, 4);

      const missing = [];
      if (!roobet) missing.push("Roobet username");
      if (!shirt) missing.push("shirt");
      if (!size) missing.push("size");
      if (!proof.length) missing.push("max win screenshot");
      if (missing.length) return res.status(400).json({ error: `Still needed: ${missing.join(", ")}.` });

      const discord = clean(b.discord, 60);
      const telegram = clean(b.telegram, 60).replace(/^@/, "");
      if (!discord && !telegram)
        return res.status(400).json({ error: "Add your Discord or Telegram so we can reach you." });

      const id = Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
      const claim = {
        id, roobet, shirt, size,
        color: clean(b.color, 30),
        discord, telegram,
        notes: clean(b.notes, 600),
        proof,
        status: "pending",
        adminNotes: "",
        created: Date.now(),
        updated: Date.now(),
        ip,
      };

      await redis("SET", KEY(id), JSON.stringify(claim));
      await redis("ZADD", IDX, claim.created, id);
      return res.status(200).json({ ok: true, id, ref: id.toUpperCase() });
    }

    if (!isAdmin(req)) return res.status(403).json({ error: "forbidden" });

    if (req.method === "GET") {
      const ids = (await redis("ZRANGE", IDX, 0, -1, "REV")) || [];
      if (!ids.length) return res.status(200).json({ claims: [], counts: { all: 0 } });
      const rows = (await redis("MGET", ...ids.map(KEY))) || [];
      const claims = rows
        .map((r) => { try { return JSON.parse(r); } catch { return null; } })
        .filter(Boolean);
      const counts = claims.reduce((a, c) => ((a[c.status] = (a[c.status] || 0) + 1), a), {});
      counts.all = claims.length;
      return res.status(200).json({ claims, counts });
    }

    if (req.method === "PATCH" || req.method === "PUT") {
      const b = await readBody(req);
      const id = clean(b.id, 40);
      if (!id) return res.status(400).json({ error: "missing id" });
      const raw = await redis("GET", KEY(id));
      if (!raw) return res.status(404).json({ error: "not found" });
      const claim = JSON.parse(raw);
      if (b.status !== undefined) {
        const s = clean(b.status, 20);
        if (!STATUSES.includes(s)) return res.status(400).json({ error: "bad status" });
        claim.status = s;
      }
      if (b.adminNotes !== undefined) claim.adminNotes = clean(b.adminNotes, 1000);
      claim.updated = Date.now();
      await redis("SET", KEY(id), JSON.stringify(claim));
      return res.status(200).json({ ok: true, claim });
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
