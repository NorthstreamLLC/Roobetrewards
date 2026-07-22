// TEMPORARY debug: lists env var NAMES (never values) related to storage. Remove after setup.
module.exports = (req, res) => {
  const names = Object.keys(process.env).filter((k) => /KV|REDIS|UPSTASH|STORAGE/i.test(k)).sort();
  res.setHeader("Cache-Control", "no-store");
  res.status(200).json({ names });
};
