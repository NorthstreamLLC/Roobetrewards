// Screenshot upload for the VIP transfer form.
// Client compresses to JPEG and POSTs { name, data: "<base64>" }; we push it to
// Vercel Blob via the REST API (no SDK / node_modules needed) and return the URL.
//
// Env: BLOB_READ_WRITE_TOKEN  (Vercel → Storage → Blob → connect to this project)
const { redis } = require("../lib/redis");

const MAX_BYTES = 4 * 1024 * 1024; // 4 MB after client-side compression

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

module.exports = async (req, res) => {
  res.setHeader("Cache-Control", "no-store");
  if (req.method !== "POST") return res.status(405).json({ error: "method not allowed" });

  const token = process.env.BLOB_READ_WRITE_TOKEN;
  if (!token) return res.status(500).json({ error: "uploads not configured" });

  try {
    // light abuse guard: 40 uploads per IP per hour
    try {
      const k = `vip:up:${ipOf(req)}`;
      const n = await redis("INCR", k);
      if (n === 1) await redis("EXPIRE", k, 3600);
      if (n > 40) return res.status(429).json({ error: "too many uploads, try again later" });
    } catch { /* redis optional for uploads */ }

    const body = await readBody(req);
    const raw = String(body.data || "").replace(/^data:[^;]+;base64,/, "");
    if (!raw) return res.status(400).json({ error: "no image data" });

    const buf = Buffer.from(raw, "base64");
    if (!buf.length) return res.status(400).json({ error: "invalid image data" });
    if (buf.length > MAX_BYTES) return res.status(413).json({ error: "image too large (max 4MB)" });

    // sniff the magic bytes — only allow real images through
    const sig = buf.subarray(0, 12);
    let type = null;
    if (sig[0] === 0xff && sig[1] === 0xd8) type = "image/jpeg";
    else if (sig[0] === 0x89 && sig[1] === 0x50 && sig[2] === 0x4e && sig[3] === 0x47) type = "image/png";
    else if (sig.subarray(0, 4).toString() === "RIFF" && sig.subarray(8, 12).toString() === "WEBP") type = "image/webp";
    else if (sig.subarray(0, 3).toString() === "GIF") type = "image/gif";
    if (!type) return res.status(415).json({ error: "only JPG, PNG, WEBP or GIF images are accepted" });

    const ext = type.split("/")[1].replace("jpeg", "jpg");
    const safe = String(body.name || "shot")
      .replace(/\.[^.]+$/, "")
      .replace(/[^a-z0-9_-]+/gi, "-")
      .slice(0, 40) || "shot";
    const path = `vip-transfer/${new Date().toISOString().slice(0, 10)}/${safe}.${ext}`;

    // The Blob REST API is versioned via a header and Vercel has bumped it over
    // time; try the known versions rather than pinning one that may age out.
    let r = null, lastErr = "";
    for (const version of ["7", "11", "6", "4"]) {
      r = await fetch(`https://blob.vercel-storage.com/${encodeURI(path)}`, {
        method: "PUT",
        headers: {
          authorization: `Bearer ${token}`,
          "x-api-version": version,
          "x-content-type": type,
          "x-add-random-suffix": "1",
          "x-random-suffix": "1",
          "x-cache-control-max-age": "31536000",
          "content-type": type,
        },
        body: buf,
        signal: AbortSignal.timeout(15000),
      });
      if (r.ok) break;
      lastErr = `${r.status} ${(await r.text().catch(() => "")).slice(0, 160)}`;
      if (r.status !== 400 && r.status !== 404 && r.status !== 426) break; // not a version problem
    }
    if (!r || !r.ok) return res.status(502).json({ error: "upload failed", detail: lastErr });
    const d = await r.json();
    return res.status(200).json({ ok: true, url: d.url, downloadUrl: d.downloadUrl || d.url, size: buf.length });
  } catch (e) {
    return res.status(500).json({ error: String(e && e.message ? e.message : e) });
  }
};
