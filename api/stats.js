// Public aggregate stats for the transparency report.
//
// Deliberately narrow. Community wager totals and player counts are NOT exposed
// here — publishing them tells competitors the size of our affiliate deal, so
// removing the tile from the page without closing the endpoint would be pointless.
// Everything returned is a completed-claim count. No usernames, no amounts per
// person, nothing that identifies a player.
const { redis } = require("../lib/redis");

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
  const merch = await countByStatus("merch:index", (id) => `merch:claim:${id}`);
  return res.status(200).json({
    generated: Date.now(),
    merchClaims: merch ? { shipped: merch.shipped || 0 } : null,
  });
};
