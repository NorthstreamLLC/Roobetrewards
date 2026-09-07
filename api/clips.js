// Recent clips for the watch page.
// Kick has no clips endpoint in its official public API, so we try the site API
// (may be blocked from datacenter IPs) and fall back to the YouTube feed.
const CHANNEL = "dailygambling";

function fromKick(json) {
  const arr = json?.clips || json?.data || (Array.isArray(json) ? json : []);
  return (arr || [])
    .map((c) => ({
      id: c.id ?? c.clip_id,
      title: c.title || "Clip",
      url: c.id ? `https://kick.com/${CHANNEL}?clip=${c.id}` : `https://kick.com/${CHANNEL}/clips`,
      thumbnail: c.thumbnail_url || c.thumbnail?.src || c.thumbnail || null,
      duration: typeof c.duration === "number" ? c.duration : null,
      views: typeof c.views === "number" ? c.views : c.view_count ?? null,
      created: c.created_at || null,
      source: "kick",
    }))
    .filter((c) => c.id);
}

module.exports = async (req, res) => {
  res.setHeader("Cache-Control", "s-maxage=1800, stale-while-revalidate=3600");
  const limit = Math.min(12, Math.max(1, parseInt(req.query?.limit, 10) || 4));

  // 1) Kick clips (unofficial endpoint)
  try {
    const r = await fetch(
      `https://kick.com/api/v2/channels/${CHANNEL}/clips?sort=date&time=all`,
      {
        headers: {
          "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36",
          Accept: "application/json",
        },
        signal: AbortSignal.timeout(7000),
      }
    );
    if (r.ok) {
      const clips = fromKick(await r.json()).slice(0, limit);
      if (clips.length) return res.status(200).json({ clips, src: "kick" });
    }
  } catch (e) {
    /* fall through */
  }

  // 2) Fallback: latest YouTube uploads (same host, already configured)
  try {
    const proto = req.headers["x-forwarded-proto"] || "https";
    const host = req.headers.host;
    const r = await fetch(`${proto}://${host}/api/youtube?limit=${limit}`, {
      signal: AbortSignal.timeout(7000),
    });
    const d = await r.json();
    if (d?.videos?.length) {
      return res.status(200).json({
        clips: d.videos.map((v) => ({
          id: v.id,
          title: v.title,
          url: v.url,
          thumbnail: v.thumbnail,
          duration: null,
          views: v.views,
          created: v.published,
          source: "youtube",
        })),
        src: "youtube",
      });
    }
  } catch (e) {
    /* fall through */
  }

  return res.status(200).json({ clips: null, note: "no clip source available" });
};
