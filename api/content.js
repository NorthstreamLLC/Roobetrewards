// Live-editable site content: promotions + transparency figures.
//
//   GET                -> public, cached. Returns whatever the admin has saved,
//                         or {} if nothing has been set (the built HTML is the default).
//   PUT  ?key=...      -> admin. Replaces a section.
//
// The pages ship with the build-time values baked into the HTML, so Google sees
// real content and there is no blank flash. This endpoint only supplies overrides.
//
// Env: VIP_ADMIN_KEY (same key as the rest of the admin) + the Redis vars
const { redis } = require("../lib/redis");

const KEY = "site:content";
const CTRL = new RegExp("[\\u0000-\\u001f\\u007f]+", "g");
const SECTIONS = ["promos", "transparency"];

const readBody = (req) =>
  new Promise((resolve) => {
    if (req.body && typeof req.body === "object") return resolve(req.body);
    let b = "";
    req.on("data", (c) => (b += c));
    req.on("end", () => { try { resolve(JSON.parse(b || "{}")); } catch { resolve({}); } });
  });

const isAdmin = (req) => {
  const k = process.env.VIP_ADMIN_KEY;
  if (!k) return false;
  const given = req.headers["x-admin-key"] || (req.query && req.query.key) || "";
  return String(given) === k;
};

// Everything written here ends up in the DOM, so strip tags that could execute.
const clean = (v, max = 400) =>
  String(v == null ? "" : v)
    .replace(CTRL, " ")
    .replace(/<\s*\/?\s*(script|iframe|object|embed|style|link|meta)[^>]*>/gi, "")
    .replace(/\son\w+\s*=/gi, " data-x=")
    .replace(/javascript:/gi, "")
    .replace(/\s+/g, " ")
    .trim()
    .slice(0, max);

const COLORS = ["gold", "green", "violet", "cyan", "pink", "red", "blue", "amber"];
const ICONS = ["coins", "gift", "spark", "trophy", "star", "gem", "spin", "shirt", "pad", "target"];

function cleanPromo(p) {
  if (!p || typeof p !== "object") return null;
  const title = clean(p.title, 80);
  if (!title) return null;
  const ladder = (Array.isArray(p.ladder) ? p.ladder : []).slice(0, 6).map((s) => clean(s, 12)).filter(Boolean);
  const at = Math.max(0, Math.min(Number(p.at) || 0, Math.max(ladder.length - 1, 0)));
  return {
    title,
    prize: clean(p.prize, 24),
    unit: clean(p.unit, 24),
    window: clean(p.window, 48),
    ic: ICONS.includes(p.ic) ? p.ic : "coins",
    c: COLORS.includes(p.c) ? p.c : "gold",
    foot: clean(p.foot, 80),
    terms: (Array.isArray(p.terms) ? p.terms : []).slice(0, 6).map((t) => clean(t, 220)).filter(Boolean),
    ladder,
    at,
    deadline: clean(p.deadline, 32),   // ISO date for the hero countdown
  };
}

function cleanPayout(r) {
  if (!Array.isArray(r)) return null;
  const [who, what, amt, when, kind] = r;
  if (!who && !what) return null;
  return [clean(who, 30), clean(what, 70), clean(amt, 20), clean(when, 20),
          ["cash", "merch", "spins", "bonus"].includes(kind) ? kind : "cash"];
}

module.exports = async (req, res) => {
  try {
    if (req.method === "GET") {
      res.setHeader("Cache-Control", "s-maxage=60, stale-while-revalidate=300");
      const raw = await redis("GET", KEY);
      return res.status(200).json(raw ? JSON.parse(raw) : {});
    }

    if (!isAdmin(req)) return res.status(403).json({ error: "forbidden" });
    res.setHeader("Cache-Control", "no-store");

    if (req.method === "PUT" || req.method === "POST") {
      const b = await readBody(req);
      const section = clean(b.section, 20);
      if (!SECTIONS.includes(section)) return res.status(400).json({ error: "unknown section" });

      const raw = await redis("GET", KEY);
      const doc = raw ? JSON.parse(raw) : {};

      if (section === "promos") {
        doc.promos = {
          active: (Array.isArray(b.active) ? b.active : []).slice(0, 3).map(cleanPromo).filter(Boolean),
          past: (Array.isArray(b.past) ? b.past : []).slice(0, 12).map(cleanPromo).filter(Boolean),
        };
      } else {
        const t = b.transparency || {};
        doc.transparency = {
          given_away: clean(t.given_away, 24),
          given_away_note: clean(t.given_away_note, 90),
          milestones_paid: clean(t.milestones_paid, 24),
          milestones_exact: clean(t.milestones_exact, 24),
          milestones_note: clean(t.milestones_note, 90),
          milestones_period: clean(t.milestones_period, 40),
          merch_baseline: Math.max(0, Math.min(Number(t.merch_baseline) || 0, 100000)),
          payouts: (Array.isArray(t.payouts) ? t.payouts : []).slice(0, 30).map(cleanPayout).filter(Boolean),
        };
      }
      doc.updated = Date.now();
      await redis("SET", KEY, JSON.stringify(doc));
      return res.status(200).json({ ok: true, content: doc });
    }

    if (req.method === "DELETE") {
      const section = clean((req.query && req.query.section) || "", 20);
      const raw = await redis("GET", KEY);
      const doc = raw ? JSON.parse(raw) : {};
      if (SECTIONS.includes(section)) delete doc[section];
      else return res.status(400).json({ error: "unknown section" });
      doc.updated = Date.now();
      await redis("SET", KEY, JSON.stringify(doc));
      return res.status(200).json({ ok: true, content: doc });
    }

    return res.status(405).json({ error: "method not allowed" });
  } catch (e) {
    return res.status(500).json({ error: String(e && e.message ? e.message : e) });
  }
};
