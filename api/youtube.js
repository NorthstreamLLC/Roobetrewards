// Latest YouTube uploads via the channel's public RSS feed — no API key required.
// Env vars (Vercel → Settings → Environment Variables):
//   YOUTUBE_CHANNEL_ID   e.g. UCxxxxxxxxxxxxxxxxxxxxxx      (preferred)
//   YOUTUBE_CHANNEL_URL  e.g. https://www.youtube.com/@handle (resolved automatically)
let idCache = { id: null, exp: 0 };

async function resolveChannelId() {
  const direct = process.env.YOUTUBE_CHANNEL_ID;
  if (direct) return direct;
  const url = process.env.YOUTUBE_CHANNEL_URL || "https://www.youtube.com/@DAILYGambling";
  if (idCache.id && Date.now() < idCache.exp) return idCache.id;
  const r = await fetch(url, {
    headers: { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" },
    signal: AbortSignal.timeout(7000),
  });
  if (!r.ok) throw new Error(`channel page ${r.status}`);
  const html = await r.text();
  const m =
    html.match(/"channelId":"(UC[\w-]{22})"/) ||
    html.match(/channel\/(UC[\w-]{22})/) ||
    html.match(/"externalId":"(UC[\w-]{22})"/);
  if (!m) throw new Error("channel id not found");
  idCache = { id: m[1], exp: Date.now() + 24 * 3600 * 1000 };
  return m[1];
}

function parseFeed(xml, limit) {
  const out = [];
  const entries = xml.split("<entry>").slice(1);
  for (const e of entries.slice(0, limit)) {
    const pick = (tag) => {
      const m = e.match(new RegExp(`<${tag}[^>]*>([\\s\\S]*?)</${tag}>`));
      return m ? m[1].trim() : null;
    };
    const id = pick("yt:videoId");
    if (!id) continue;
    const thumb = (e.match(/<media:thumbnail url="([^"]+)"/) || [])[1];
    const views = (e.match(/<media:statistics views="(\d+)"/) || [])[1];
    out.push({
      id,
      title: (pick("title") || "").replace(/&amp;/g, "&").replace(/&quot;/g, '"').replace(/&#39;/g, "'"),
      published: pick("published"),
      url: `https://www.youtube.com/watch?v=${id}`,
      thumbnail: thumb || `https://i.ytimg.com/vi/${id}/hqdefault.jpg`,
      views: views ? Number(views) : null,
    });
  }
  return out;
}

module.exports = async (req, res) => {
  res.setHeader("Cache-Control", "s-maxage=1800, stale-while-revalidate=3600");
  try {
    const cid = await resolveChannelId();
    if (!cid) return res.status(200).json({ videos: null, note: "YouTube channel not configured" });
    const limit = Math.min(12, Math.max(1, parseInt(req.query?.limit, 10) || 8));
    const r = await fetch(`https://www.youtube.com/feeds/videos.xml?channel_id=${cid}`, {
      signal: AbortSignal.timeout(7000),
    });
    if (!r.ok) throw new Error(`feed ${r.status}`);
    const videos = parseFeed(await r.text(), limit);
    return res.status(200).json({ videos, channelId: cid, channelUrl: `https://www.youtube.com/channel/${cid}` });
  } catch (err) {
    return res.status(200).json({ videos: null, error: String(err) });
  }
};
