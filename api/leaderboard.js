// Vercel serverless function — merges the ELITE + DAILY leaderboards into one top 100.
// Keys stay server-side; the browser never sees them.
//
// Environment Variables (Vercel → Project → Settings → Environment Variables):
//   LEADERBOARD_API_URL        = endpoint URL (shared by both codes)
//   LEADERBOARD_API_KEY_ELITE  = API key for code ELITE
//   LEADERBOARD_API_KEY_DAILY  = API key for code DAILY
// Optional (if each code has its own URL):
//   LEADERBOARD_API_URL_ELITE / LEADERBOARD_API_URL_DAILY
//
// If the URL contains {start} / {end}, they're replaced with the current period
// (16th 00:00 UTC -> 15th 24:00 UTC) as ISO dates.

function periodDates() {
  const n = new Date();
  const y = n.getUTCFullYear(), m = n.getUTCMonth();
  const startThis = Date.UTC(y, m, 16);
  const start = n.getTime() >= startThis ? new Date(startThis) : new Date(Date.UTC(y, m - 1, 16));
  const end = new Date(Date.UTC(start.getUTCFullYear(), start.getUTCMonth() + 1, 16));
  return { start: start.toISOString(), end: end.toISOString() };
}

function normalize(data) {
  const arr = Array.isArray(data)
    ? data
    : (data && (data.entries || data.leaderboard || data.data || data.results || data.players)) || [];
  return arr.map((e) => ({
    username: String(e.username ?? e.name ?? e.user ?? e.player ?? "player"),
    wagered: Number(e.weightedWagered ?? e.wagered ?? e.wager ?? e.amount ?? e.total ?? 0),
  }));
}

function mask(n) {
  if (n.includes("*")) return n; // already masked upstream
  const keep = n.slice(0, 3);
  return keep + "*".repeat(Math.min(Math.max(n.length - 3, 2), 12));
}

async function fetchBoard(url, key) {
  if (!url || !key) return [];
  const { start, end } = periodDates();
  const u = url.replace("{start}", encodeURIComponent(start)).replace("{end}", encodeURIComponent(end));
  const r = await fetch(u, { headers: { Authorization: `Bearer ${key}`, "x-api-key": key } });
  if (!r.ok) throw new Error(`upstream ${r.status}`);
  return normalize(await r.json());
}

module.exports = async (req, res) => {
  const base = process.env.LEADERBOARD_API_URL;
  const urlElite = process.env.LEADERBOARD_API_URL_ELITE || base;
  const urlDaily = process.env.LEADERBOARD_API_URL_DAILY || base;
  const keyElite = process.env.LEADERBOARD_API_KEY_ELITE;
  const keyDaily = process.env.LEADERBOARD_API_KEY_DAILY;

  if (!urlElite && !urlDaily) {
    return res.status(200).json({ entries: null, note: "API not configured" });
  }

  try {
    const results = await Promise.allSettled([
      fetchBoard(urlElite, keyElite),
      fetchBoard(urlDaily, keyDaily),
    ]);
    const merged = new Map(); // username -> wagered (summed if same name under both codes)
    for (const r of results) {
      if (r.status !== "fulfilled") continue;
      for (const e of r.value) {
        merged.set(e.username, (merged.get(e.username) || 0) + e.wagered);
      }
    }
    if (!merged.size) throw new Error(results.map(r => r.reason).filter(Boolean).join("; ") || "no data");

    const entries = [...merged.entries()]
      .map(([username, wagered]) => ({ username: mask(username), wagered }))
      .sort((a, b) => b.wagered - a.wagered)
      .slice(0, 100)
      .map((e, i) => ({ rank: i + 1, ...e }));

    res.setHeader("Cache-Control", "s-maxage=300, stale-while-revalidate=600");
    return res.status(200).json({ entries, updated: Date.now() });
  } catch (err) {
    return res.status(200).json({ entries: null, error: String(err) });
  }
};
