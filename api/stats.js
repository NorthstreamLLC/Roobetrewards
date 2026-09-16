// Public aggregate stats for the transparency report.
// Deliberately aggregate-only: no usernames, no amounts per person, nothing that
// identifies a player. Everything here is a count or a sum.
const { redis } = require("../lib/redis");

function periodDates() {
  const n = new Date();
  const y = n.getUTCFullYear(), m = n.getUTCMonth();
  const startThis = Date.UTC(y, m, 16);
  const start = n.getTime() >= startThis ? new Date(startThis) : new Date(Date.UTC(y, m - 1, 16));
  const end = new Date(Date.UTC(start.getUTCFullYear(), start.getUTCMonth() + 1, 16));
  return { start: start.toISOString(), end: end.toISOString() };
}

// counts by status for a Redis-backed index, without exposing any record
async function countByStatus(indexKey, keyFn) {
  try {
    const ids = (await redis("ZRANGE", indexKey, 0, -1)) || [];
    if (!ids.length) return { total: 0 };
    const rows = (await redis("MGET", ...ids.map(keyFn))) || [];
    const out = { total: 0 };
    for (const r of rows) {
      if (!r) continue;
      let o; try { o = JSON.parse(r); } catch { continue; }
      out.total++;
      const s = o.status || "pending";
      out[s] = (out[s] || 0) + 1;
    }
    return out;
  } catch {
    return null;
  }
}

module.exports = async (req, res) => {
  res.setHeader("Cache-Control", "s-maxage=600, stale-while-revalidate=1800");
  const period = periodDates();
  const out = { period, generated: Date.now() };

  // Community wager for the current leaderboard period, summed from the same
  // affiliate data the public leaderboard uses (top 100 tracked players).
  try {
    const proto = req.headers["x-forwarded-proto"] || "https";
    const host = req.headers.host;
    const r = await fetch(`${proto}://${host}/api/leaderboard`, { signal: AbortSignal.timeout(8000) });
    const d = await r.json();
    if (d && Array.isArray(d.entries) && d.entries.length) {
      out.leaderboard = {
        players: d.entries.length,
        wagered: Math.round(d.entries.reduce((a, e) => a + (Number(e.wagered) || 0), 0)),
        topWagered: Math.round(Number(d.entries[0].wagered) || 0),
        updated: d.updated || null,
        note: "Sum of the top 100 tracked players under codes DAILY and ELITE for the current period.",
      };
    } else {
      out.leaderboard = null;
    }
  } catch {
    out.leaderboard = null;
  }

  const [vip, merch] = await Promise.all([
    countByStatus("vip:index", (id) => `vip:sub:${id}`),
    countByStatus("merch:index", (id) => `merch:claim:${id}`),
  ]);
  out.vipTransfers = vip;
  out.merchClaims = merch;

  return res.status(200).json(out);
};
