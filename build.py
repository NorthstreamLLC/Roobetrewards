# -*- coding: utf-8 -*-
"""Static site generator for roobetcasinorewards.com"""
import os, json

SITE = "https://roobetcasinorewards.com"
ELITE = "https://roobet.com/?ref=elite"
DAILY = "https://roobet.com/?ref=daily"
KICK = "https://kick.com/dailygambling"
SLOTS = "https://slotessentials.com/rewards/sign-up-bonuses"
KYC = "https://www.howtokyc.com/"
TELEGRAM = "https://t.me/slotessentialsVIP"
DISCORD = "https://discord.gg/dailygamba"
SLOTS_MILES = "https://slotessentials.com/rewards/wager-milestones"
SLOTS_HOME = "https://slotessentials.com"

WEIGHTED = """<div style="margin-top:50px" class="rv"><h2 style="text-align:center">How Weighted Wagering Works</h2>
<p class="lead" style="margin:10px auto 26px;text-align:center">Different game types contribute at different rates — slots and similar gameplay count at the full rate and ensure full payout eligibility.</p>
<div class="cards c3">
  <div class="card center rv"><div class="glow"></div><p class="amount">100%</p><h3 style="font-size:1rem">97% RTP or lower</h3><p>Your full wager amount counts.</p></div>
  <div class="card center rv d1"><div class="glow"></div><p class="amount">50%</p><h3 style="font-size:1rem">Above 97% RTP</h3><p>Only half of your wager counts.</p></div>
  <div class="card center rv d2"><div class="glow"></div><p class="amount">10%</p><h3 style="font-size:1rem">98% RTP and above</h3><p>Mostly Roobet house games.</p></div>
</div></div>"""

LOGO = """<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="24" cy="24" r="21" stroke="#ffc700" stroke-width="4" stroke-dasharray="9 5"/><circle cx="24" cy="24" r="14" fill="#ffc700"/><text x="24" y="30" text-anchor="middle" font-family="Outfit,Arial" font-weight="800" font-size="17" fill="#1a1230">R</text></svg>"""

CHEV = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none"><path d="M6 9l6 6 6-6" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/></svg>'
ARR = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'

MENU_ITEMS = [
    ("leaderboard.html", "🏆", "$50K Wager Leaderboard", "Monthly cash-prize race"),
    ("wager-milestones.html", "🎯", "Wager Milestones", "Up to $11,350 extra / month"),
    ("max-win-merch.html", "👕", "Max Win Merch", "Free merch for every max win"),
    ("free-spins.html", "🎰", "Free Spins Bonus", "Up to 125 exclusive free spins"),
    ("elite-points.html", "⭐", "ELITE Points", "Redeem points for real prizes"),
    ("slot-challenges.html", "🎮", "Slot Challenges", "Complete challenges, win prizes"),
    ("giveaways.html", "🎁", "$5K Giveaways", "Monthly community giveaways"),
    ("roobet-rewards.html", "💰", "Roobet Rewards", "Rakeback, vault & bonuses"),
]

def nav():
    menu = "".join(
        f'<a href="/{f[:-5]}"><span class="ic">{ic}</span><span><b>{t}</b><span>{d}</span></span></a>'
        for f, ic, t, d in MENU_ITEMS)
    return f"""<nav aria-label="Main">
  <div class="nav-inner">
    <a class="brand" href="/">{LOGO}<span><span class="b1">ROOBET</span>REWARDS</span></a>
    <div class="nav-links">
      <div class="dropdown">
        <button aria-haspopup="true">Rewards {CHEV}</button>
        <div class="menu">{menu}</div>
      </div>
      <a href="/leaderboard">Leaderboard</a>
      <a href="/free-spins">Free Spins</a>
      <a href="/max-win-merch">Merch</a>
      <a href="/vip-transfer">VIP Transfer</a>
      <a href="/blog">Blog</a>
    </div>
    <div class="nav-cta">
      <a class="btn btn-ghost" href="/#how-to-sign-up">How to Sign-Up</a>
      <a class="btn btn-ghost" href="/contact">Contact Us</a>
      <a class="btn btn-gold" href="{DAILY}" rel="nofollow sponsored" target="_blank">Join with DAILY</a>
      <button class="burger" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</nav>"""

def footer():
    rew = "".join(f'<a href="/{f[:-5]}">{t}</a>' for f, _, t, _ in MENU_ITEMS[:4])
    rew2 = "".join(f'<a href="/{f[:-5]}">{t}</a>' for f, _, t, _ in MENU_ITEMS[4:])
    rew2 += '<a href="/vip-transfer">VIP Transfer</a><a href="/blog">Blog</a><a href="/#faq">FAQ</a><a href="/contact">Contact Us</a>'
    return f"""<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="brand" href="/">{LOGO}<span><span class="b1">ROOBET</span>REWARDS</span></a>
        <p style="color:var(--muted);font-size:.9rem;margin-top:16px;max-width:280px">The home of the biggest Roobet casino rewards — $100,000 in monthly rewards for players using code <b style="color:var(--gold)">ELITE</b> or <b style="color:var(--gold)">DAILY</b>.</p>
      </div>
      <div><h4>Rewards</h4>{rew}</div>
      <div><h4>More Rewards</h4>{rew2}</div>
      <div><h4>Get Started</h4>
        <a href="{DAILY}" rel="nofollow sponsored" target="_blank">Sign up with code DAILY</a>
        <a href="{ELITE}" rel="nofollow sponsored" target="_blank">Sign up with code ELITE</a>
        <a href="{TELEGRAM}" target="_blank" rel="noopener">VIP Team on Telegram</a>
        <a href="{DISCORD}" target="_blank" rel="noopener">Join our Discord</a>
        <a href="{KYC}" target="_blank" rel="noopener">How to KYC on Roobet</a>
        <a href="{SLOTS}" target="_blank" rel="noopener">Slotessentials Rewards</a>
        <a href="{KICK}" target="_blank" rel="noopener">Watch DailyGambling on Kick</a>
      </div>
    </div>
    <div class="foot-note">
      <span class="badge-18">18+</span>
      <p>Gamble responsibly. You must be of legal gambling age in your jurisdiction to play at Roobet. Gambling involves risk — never wager more than you can afford to lose. If gambling stops being fun, seek help at <a href="https://www.begambleaware.org" style="color:var(--gold)">BeGambleAware.org</a>. This is an independent affiliate website; offers are provided in partnership with Roobet and Slotessentials and may change at any time. Terms &amp; conditions apply to all rewards.</p>
      <p style="margin-top:10px">© 2026 roobetcasinorewards.com — All rights reserved.</p>
    </div>
  </div>
</footer>"""

ORG = {
    "@type": "Organization", "@id": SITE + "/#org",
    "name": "Roobet Casino Rewards", "url": SITE + "/",
    "logo": {"@type": "ImageObject", "url": SITE + "/assets/apple-touch-icon.png"},
    "sameAs": [KICK, DISCORD, TELEGRAM, "https://slotessentials.com"],
}

# Related-links pool for WebPage.isRelatedTo (mirrors the slotessentials schema pattern)
REL_POOL = [
    ("Roobet Casino Rewards Homepage", SITE + "/"),
    ("$50,000 Roobet Wager Leaderboard", SITE + "/leaderboard"),
    ("Roobet Wager Milestones", SITE + "/wager-milestones"),
    ("Roobet Free Spins Bonus", SITE + "/free-spins"),
    ("Roobet Max Win Merch", SITE + "/max-win-merch"),
    ("ELITE Points Shop", SITE + "/elite-points"),
    ("Roobet Slot Challenges", SITE + "/slot-challenges"),
    ("$5,000 Monthly Giveaways", SITE + "/giveaways"),
    ("Roobet Rewards Explained", SITE + "/roobet-rewards"),
    ("Transfer Your VIP Status to Roobet", SITE + "/vip-transfer"),
    ("Roobet Guides & Blog", SITE + "/blog"),
    ("Play on Roobet with code DAILY", DAILY),
    ("Slotessentials", "https://slotessentials.com/"),
    ("How to KYC on Roobet", KYC),
    ("Watch DailyGambling on Kick", KICK),
]

def shell(fname, title, desc, kw, body, schema=None, og_type="website"):
    canon = SITE + ("/" if fname == "index.html" else "/" + fname[:-5])
    page_name = title.split(" — ")[0].split(" | ")[0]

    graph = [
        {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/",
         "name": "Roobet Casino Rewards", "publisher": {"@id": SITE + "/#org"}, "inLanguage": "en"},
        dict(ORG),
    ]
    webpage = {
        "@type": "WebPage", "@id": canon + "#webpage", "url": canon,
        "name": title, "description": desc,
        "isPartOf": {"@id": SITE + "/#website"},
        "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + "/assets/og-image.png"},
        "inLanguage": "en",
        "isRelatedTo": [{"@type": "WebPage", "name": n, "url": u} for n, u in REL_POOL if u.rstrip("/") != canon.rstrip("/")][:12],
    }
    if fname != "index.html":
        webpage["breadcrumb"] = {"@id": canon + "#breadcrumb"}
        graph.append({
            "@type": "BreadcrumbList", "@id": canon + "#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Roobet Casino Rewards", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": page_name, "item": canon},
            ]})

    # merge page-specific entities into the graph, cross-linked via @id
    extras = [schema] if schema and not isinstance(schema, list) else (schema or [])
    id_map = {"FAQPage": "#faq", "Article": "#article", "Product": "#product", "VideoGame": "#game"}
    for s in extras:
        s = dict(s); s.pop("@context", None)
        t = s.get("@type")
        if t == "ContactPage":       # ContactPage IS the WebPage
            webpage["@type"] = "ContactPage"
            continue
        s["@id"] = canon + id_map.get(t, "#entity")
        if "mainEntity" not in webpage and t in id_map:
            webpage["mainEntity"] = {"@id": s["@id"]}
        if t == "Article":
            s["mainEntityOfPage"] = {"@id": canon + "#webpage"}
        graph.append(s)

    graph.insert(2, webpage)
    schema_tag = f'<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": graph})}</script>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-4XLL2RYBWD"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', 'G-4XLL2RYBWD');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{kw}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:site_name" content="Roobet Casino Rewards">
<meta property="og:image" content="{SITE}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE}/assets/og-image.png">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/assets/favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<meta name="theme-color" content="#0d0919">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">
{schema_tag}
</head>
<body>
<div class="orbs"><div class="orb g"></div><div class="orb p"></div><div class="orb p2"></div></div>
<div class="grid-bg"></div>
{nav()}
<main>
{body}
</main>
{footer()}
<div class="modal-back" id="promo-modal" role="dialog" aria-modal="true" aria-label="Free spins offer">
  <div class="modal">
    <button class="modal-x" aria-label="Close">&times;</button>
    <span class="eyebrow">🎁 Exclusive Offer</span>
    <h2>Join Roobet on code <span class="grad">DAILY</span></h2>
    <p class="lead" style="margin:12px auto 24px">…and receive <b style="color:var(--gold)">Free Spins</b> — up to 125 spins at $1.00 each.</p>
    <div class="hero-cta" style="justify-content:center">
      <a class="btn btn-gold btn-lg pulse" href="{DAILY}" rel="nofollow sponsored" target="_blank">Claim with code DAILY {ARR}</a>
      <a class="btn btn-ghost btn-lg" href="/free-spins">See Free Spins Tiers</a>
    </div>
  </div>
</div>
<script src="/js/main.js" defer></script>
</body>
</html>"""

def cta_banner(h, p, extra="", funnel=None):
    if funnel:  # primary CTA -> Slotessentials funnel
        btns = f"""<a class="btn btn-gold btn-lg pulse" href="{SLOTS}" target="_blank" rel="noopener">{funnel} {ARR}</a>
    <a class="btn btn-ghost btn-lg" href="{DAILY}" rel="nofollow sponsored" target="_blank">Or join Roobet with DAILY</a>"""
    else:
        btns = f"""<a class="btn btn-gold btn-lg pulse" href="{DAILY}" rel="nofollow sponsored" target="_blank">Sign up with code DAILY {ARR}</a>
    <a class="btn btn-ghost btn-lg" href="{KYC}" target="_blank" rel="noopener">How to KYC on Roobet</a>"""
    return f"""<section><div class="wrap"><div class="cta-banner rv">
  <span class="coins" style="top:14%;left:8%">🪙</span><span class="coins" style="bottom:18%;right:10%;animation-delay:-2s">💰</span>
  <h2>{h}</h2><p class="lead">{p}</p>
  <div class="hero-cta" style="justify-content:center">
    {btns}
  </div>{extra}
</div></div></section>"""

def crumb(name):
    return f'<p class="breadcrumb rv"><a href="/">Home</a> / <a href="/#rewards">Rewards</a> / {name}</p>'

PAGES = {}

# ================= HOME =================
faq_items = [
    ("What are the best Roobet casino rewards?",
     "Players using code ELITE or DAILY on Roobet unlock the full $100,000 monthly rewards package: the $50,000 Wager Leaderboard, up to $11,350 in Wager Milestones, exclusive Free Spins sign-up bonuses, Max Win Merch, ELITE Points, slot challenges, $5,000 in community giveaways, and VIP status transfer — all stacked on top of Roobet's own rakeback, daily, weekly and monthly bonuses."),
    ("How do I claim Roobet free spins?",
     "Sign up at Roobet with code ELITE or DAILY — your all-time deposit and wager totals unlock the exclusive free spins bonus (not a single deposit): $500 deposited and $5,000 wagered all-time earns 75 free spins at $0.60, $1,000 and $10,000 earns 100 free spins at $0.80, and $2,000 and $20,000 earns 125 free spins at $1.00 each."),
    ("How does the $50,000 Wager Leaderboard work?",
     "Every dollar you wager on Roobet under code ELITE or DAILY earns you a spot on the monthly leaderboard. The top wagerers split $50,000 in prizes each month — climb the ranks for cash prizes, free spins and redeemable points."),
    ("Is there a Roobet sign-up bonus?",
     "Yes — new players joining with code ELITE or DAILY get a +10% welcome rakeboost for 24 hours, access to exclusive free spins packages, and instant entry into all monthly reward programs, on top of Roobet's instant rakeback claimable every 30 minutes."),
    ("How do I earn the $5,000 monthly giveaways?",
     "Giveaways are earned, not raffled to strangers — only active players qualify. Stay active by watching DailyGambling live on Kick, wagering under code DAILY or ELITE on Roobet, and participating in the Slotessentials community, and you'll share in $5,000 of giveaways every month plus ELITE Points redeemable for real prizes."),
    ("What is Roobet rakeback and how often can I claim it?",
     "Instant Rakeback is a percentage of your wagered amount, claimable every 30 minutes — and it never expires. Part is added instantly to your balance and part goes to your vault, which unlocks 3 claims per day. Rakeboosts of up to +20% multiply it further."),
    ("How do I get free Max Win Merch?",
     "Hit a max win on any Pragmatic Play, Hacksaw or Nolimit City slot while playing under code ELITE or DAILY and we'll ship you an exclusive Max Win shirt for that game — free. There are 16 exclusive designs to collect."),
    ("Can I transfer my VIP status to Roobet?",
     "Yes. If you hold VIP status at any other casino, you can transfer it directly to Roobet when you join under code ELITE or DAILY — keeping your level, rakeback rate and bonuses without starting over."),
    ("I have a question — how do I reach the VIP team?",
     f"Message our VIP team directly on Telegram at <a href='{TELEGRAM}' target='_blank' rel='noopener'>t.me/slotessentialsVIP</a> or join the <a href='{DISCORD}' target='_blank' rel='noopener'>SlotEssentials Discord</a> and open a ticket. The VIP team handles reward claims, VIP transfers, merch shipping and any questions about your account."),
]
def linkify(t):
    """Hyperlink codes and channels inside plain-text answers."""
    A = 'style="color:var(--gold);font-weight:700" target="_blank"'
    t = t.replace("code ELITE or DAILY",
                  f'code <a href="{DAILY}" rel="nofollow sponsored" {A}>DAILY</a> or <a href="{ELITE}" rel="nofollow sponsored" {A}>ELITE</a>')
    t = t.replace("code DAILY or ELITE",
                  f'code <a href="{DAILY}" rel="nofollow sponsored" {A}>DAILY</a> or <a href="{ELITE}" rel="nofollow sponsored" {A}>ELITE</a>')
    t = t.replace("DailyGambling live on Kick", f'<a href="{KICK}" rel="noopener" {A}>DailyGambling live on Kick</a>')
    t = t.replace("Slotessentials community", f'<a href="{DISCORD}" rel="noopener" {A}>Slotessentials community</a>')
    return t

faq_items = [(q, linkify(a)) for q, a in faq_items]
faq_schema = {
    "@context": "https://schema.org", "@type": "FAQPage",
    "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq_items],
}
faq_html = "".join(f'<details class="rv"><summary>{q}</summary><div class="a">{a}</div></details>' for q, a in faq_items)
reward_cards = "".join(f"""<a class="card rv d{i%3+1}" href="/{f[:-5]}"><div class="glow"></div><div class="ic">{ic}</div><h3>{t}</h3><p>{d}</p><span class="more">Explore {ARR}</span></a>"""
    for i, (f, ic, t, d) in enumerate([
        ("leaderboard.html", "🏆", "$50,000 Wager Leaderboard", "Wager under code ELITE or DAILY and race for your share of $50,000 in cash prizes — paid out every single month."),
        ("wager-milestones.html", "🎯", "Wager Milestones", "Hit wager targets and claim up to an extra $11,350 each month. Every milestone pays — no raffles, no luck required."),
        ("max-win-merch.html", "👕", "Max Win Merch", "Hit a max win on Pragmatic, Hacksaw or Nolimit slots and get an exclusive shirt shipped free. 16 designs to collect."),
        ("free-spins.html", "🎰", "Exclusive Free Spins", "Up to 125 free spins at $1.00 per spin with our exclusive sign-up bonus tiers. The biggest Roobet free spins deal anywhere."),
        ("vip-transfer.html", "💎", "VIP Status Transfer", "Already VIP somewhere else? Transfer your status straight to Roobet and keep everything you've earned."),
        ("elite-points.html", "⭐", "ELITE Points", "Earn points by watching streams, wagering and staying active — then redeem them for real prizes via Slotessentials."),
        ("slot-challenges.html", "🎮", "Slot Challenges", "Complete casino challenges while you play and stack extra prizes on top of your regular rewards."),
        ("giveaways.html", "🎁", "$5,000 Monthly Giveaways", "We give $5,000 back to the community every month. No catch — only active players earn giveaways."),
        ("roobet-rewards.html", "💰", "Roobet Rewards System", "Instant rakeback every 30 minutes, daily/weekly/monthly bonuses, the Vault and rakeboosts up to +20% — fully explained."),
    ]))

PAGES["index.html"] = dict(
    title="Best Roobet Casino Rewards — $100,000 in Monthly Rewards | Code ELITE & DAILY",
    desc="The best Roobet casino rewards: $100,000 in monthly rewards including a $50,000 wager leaderboard, Roobet free spins, wager milestones, max win merch and more. Join with code ELITE or DAILY.",
    kw="best casino rewards, best roobet casino rewards, roobet free spins, free spins roobet, sign-up bonus, roobet rewards, $100,000 in monthly rewards",
    schema=faq_schema,
    body=f"""
<section class="hero"><div class="wrap hero-grid">
  <div>
    <span class="eyebrow rv">🏆 The #1 Roobet Rewards Hub</span>
    <h1 class="rv d1"><span class="grad" data-count="100000" data-prefix="$">$0</span> in Monthly Rewards.<br>Every Single Month.</h1>
    <p class="lead rv d2">The best Roobet casino rewards on the planet — a $50,000 wager leaderboard, exclusive free spins, wager milestones, max win merch, giveaways and more. All unlocked with code <b style="color:var(--gold)">ELITE</b> or <b style="color:var(--gold)">DAILY</b>.</p>
    <div class="hero-cta rv d3">
      <a class="btn btn-gold btn-lg pulse" href="{DAILY}" rel="nofollow sponsored" target="_blank">Sign up with DAILY {ARR}</a>
      <a class="btn btn-ghost btn-lg" href="{KYC}" target="_blank" rel="noopener">How to KYC on Roobet</a>
    </div>
    <div class="trust rv d4">
      <div><b data-count="50000" data-prefix="$">$0</b><span>Monthly Leaderboard</span></div>
      <div><b data-count="11350" data-prefix="$">$0</b><span>Wager Milestones</span></div>
      <div><b data-count="125" data-suffix="">0</b><span>Free Spins Bonus</span></div>
      <div><b data-count="5000" data-prefix="$">$0</b><span>Monthly Giveaways</span></div>
    </div>
  </div>
  <div class="rv d2"><div class="screen purple"><video autoplay muted loop playsinline src="/assets/home-hero.mp4" aria-label="Roobet rewards showcase"></video></div></div>
</div></section>

<div class="ticker" aria-hidden="true"><div class="ticker-track">
  <span>🏆 <b>$50,000</b> Wager Leaderboard — live now</span><span>🎰 Up to <b>125 Free Spins</b> at $1.00 each</span><span>🎯 Claim up to <b>$11,350</b> in Wager Milestones</span><span>👕 Free <b>Max Win Merch</b> — 16 exclusive designs</span><span>💎 <b>VIP Transfer</b> from any casino</span><span>🎁 <b>$5,000</b> monthly community giveaways</span><span>💰 Instant Rakeback every <b>30 minutes</b></span>
  <span>🏆 <b>$50,000</b> Wager Leaderboard — live now</span><span>🎰 Up to <b>125 Free Spins</b> at $1.00 each</span><span>🎯 Claim up to <b>$11,350</b> in Wager Milestones</span><span>👕 Free <b>Max Win Merch</b> — 16 exclusive designs</span><span>💎 <b>VIP Transfer</b> from any casino</span><span>🎁 <b>$5,000</b> monthly community giveaways</span><span>💰 Instant Rakeback every <b>30 minutes</b></span>
</div></div>

<section id="rewards"><div class="wrap">
  <div class="center rv"><span class="eyebrow">Our Rewards</span><h2>Every Reward. One Code.</h2><p class="lead">Nine reward programs stacked on top of Roobet's own bonus system — this is the full package you unlock with ELITE or DAILY.</p></div>
  <div class="cards c3" style="margin-top:44px">{reward_cards}</div>
</div></section>

<section><div class="wrap">
  <div class="center rv"><span class="eyebrow">How It Works</span><h2>Biggest Rewards in 4 Steps</h2></div>
  <div class="steps" style="margin-top:44px">
    <div class="step rv"><h3>Join with DAILY or ELITE</h3><p>Sign up at Roobet with code <a href="{DAILY}" rel="nofollow sponsored" target="_blank" style="color:var(--gold);font-weight:700">DAILY</a> or <a href="{ELITE}" rel="nofollow sponsored" target="_blank" style="color:var(--gold);font-weight:700">ELITE</a> and transfer your VIP status from any casino.</p></div>
    <div class="step rv d1"><h3>Climb the $50K Leaderboard</h3><p>Every wager counts toward the monthly leaderboard — earn cash prizes, free spins and redeemable points as you climb.</p></div>
    <div class="step rv d2"><h3>Collect Milestones &amp; Points</h3><p>Claim wager milestones up to $11,350/month and score ELITE Points daily via Slotessentials and <a href="{KICK}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">DailyGambling live</a>.</p></div>
    <div class="step rv d3"><h3>Hit Max Wins, Get Merch</h3><p>Every max win you hit on Pragmatic, Hacksaw or Nolimit under our codes unlocks free exclusive Max Win Merch.</p></div>
  </div>
</div></section>

<section style="padding-top:0"><div class="wrap"><div class="cards c2">
  <div class="card rv"><div class="glow"></div><div class="ic">⚡</div><h3>Something to Claim Every 30 Minutes</h3><p>Roobet's Instant Rakeback pays a slice of every wager back to you, claimable every half hour — and it never expires. Stack rakeboosts up to +20% on top. <a href="/roobet-rewards" style="color:var(--gold);font-weight:700">See the full rewards system {ARR}</a></p></div>
  <div class="card rv d1"><div class="glow"></div><div class="ic">🔓</div><h3>The Vault — 3 Claims a Day</h3><p>Part of every reward flows to your Vault, unlocking every 8 hours starting midnight UTC. Daily, weekly and monthly bonuses feed your vault calendar for constant claims.</p></div>
</div></div></section>

<section id="faq"><div class="wrap">
  <div class="center rv"><span class="eyebrow">FAQ</span><h2>Roobet Rewards — Answered</h2></div>
  <div class="faq" style="margin-top:40px">{faq_html}</div>
</div></section>

<section id="how-to-sign-up"><div class="wrap">
  <div class="center rv"><span class="eyebrow">🚀 Getting Started</span><h2>How to Sign Up on Roobet</h2><p class="lead">From zero to claiming rewards in a few minutes — here's the exact path.</p></div>
  <div class="hero-grid" style="margin-top:44px">
    <div>
      <div style="display:grid;gap:14px">
        <div class="mile rv"><span class="amt">Step 1</span><p style="flex:1;color:var(--muted)">Head to Roobet with code <a href="{DAILY}" rel="nofollow sponsored" target="_blank" style="color:var(--gold);font-weight:700">DAILY</a> and create your account — takes under a minute.</p></div>
        <div class="mile rv d1"><span class="amt">Step 2</span><p style="flex:1;color:var(--muted)">Verify your account. New to KYC? Our step-by-step guide at <a href="{KYC}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">HowToKYC.com</a> walks you through it. Any questions? Message our <a href="{TELEGRAM}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">VIP team on Telegram</a>.</p></div>
        <div class="mile rv d2"><span class="amt">Step 3</span><p style="flex:1;color:var(--muted)">Deposit and grab your <a href="free-spins.html" style="color:var(--gold);font-weight:700">free spins tier</a> — your +10% welcome rakeboost is already running.</p></div>
        <div class="mile rv d3"><span class="amt">Step 4</span><p style="flex:1;color:var(--muted)">Already VIP elsewhere? <a href="vip-transfer.html" style="color:var(--gold);font-weight:700">Transfer your status</a>, then start climbing the <a href="leaderboard.html" style="color:var(--gold);font-weight:700">$50K leaderboard</a>.</p></div>
      </div>
      <div class="hero-cta rv" style="margin-top:28px">
        <a class="btn btn-gold btn-lg pulse" href="{DAILY}" rel="nofollow sponsored" target="_blank">Create My Account {ARR}</a>
        <a class="btn btn-ghost btn-lg" href="{KYC}" target="_blank" rel="noopener">KYC Guide</a>
      </div>
    </div>
    <div class="rv d2"><div class="phone purple"><video autoplay muted loop playsinline src="/assets/roo-signup.mp4" aria-label="Roobet sign-up walkthrough"></video></div></div>
  </div>
</div></section>

{cta_banner("Ready for $100,000 in Monthly Rewards?",
"Join Roobet with code ELITE or DAILY, transfer your VIP status, and start claiming the biggest casino rewards package anywhere.")}
""")

# ================= LEADERBOARD =================
try:
    LB_DATA = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "leaderboard-data.json"), encoding="utf-8").read()
except FileNotFoundError:
    LB_DATA = '{"entries":[]}'

LB_TABLE = f"""
<div style="margin-top:70px" id="standings">
  <div class="center rv"><span class="eyebrow">📊 Live Standings</span><h2>Current Top 100</h2>
  <p class="lead">All wagers are weighted and in USD. Everyone in the top 100 also earns <b style="color:var(--gold)">ELITE Points</b>.</p></div>
  <div class="tbl-wrap rv lb-wrap" id="lb-wrap" style="margin-top:36px"><table class="tbl" id="lb-table">
    <thead><tr><th>#</th><th>Player</th><th>Wagered (weighted)</th><th>Prize</th><th>ELITE Points</th></tr></thead>
    <tbody></tbody>
  </table></div>
  <div class="center" style="margin-top:22px"><button class="btn btn-ghost" id="lb-toggle">Show Full Top 100</button></div>
</div>
<script>window.LB_DATA = {LB_DATA};</script>"""

PAGES["leaderboard.html"] = dict(
    title="$50,000 Roobet Wager Leaderboard — Monthly Cash Prizes | Code ELITE & DAILY",
    desc="Compete on the $50,000 monthly Roobet wager leaderboard. Wager under code ELITE or DAILY, climb the ranks and win cash prizes, free spins and redeemable points every month.",
    kw="roobet wager leaderboard, $50,000 leaderboard, roobet leaderboard, best roobet casino rewards, wager race",
    body=f"""
<section class="page-hero"><div class="wrap">
  {crumb("$50K Wager Leaderboard")}
  <span class="eyebrow rv">🏆 Live Every Month</span>
  <h1 class="rv d1"><span class="grad" data-count="50000" data-prefix="$">$0</span> Wager Leaderboard</h1>
  <p class="lead rv d2">Every wager you place on Roobet under code <b style="color:var(--gold)">ELITE</b> or <b style="color:var(--gold)">DAILY</b> pushes you up the monthly leaderboard. Top spots split $50,000 — every single month.</p>
  <div class="hero-cta rv d3" style="justify-content:center">
    <a class="btn btn-gold btn-lg pulse" href="{SLOTS}" target="_blank" rel="noopener">Join the Race {ARR}</a>
  </div>
  <p class="rv d4" style="margin-top:26px;color:var(--muted)">Period: 16th &rarr; 15th, Midnight UTC &nbsp;·&nbsp; Ends in <b style="color:var(--gold);font-variant-numeric:tabular-nums" data-deadline="period16">—</b></p>
</div></section>

<section style="padding-top:20px"><div class="wrap">
  <div class="podium">
    <div class="pod rv"><span class="medal">🥈</span><p class="place">2nd Place</p><p class="pod-user" data-pod="2">—</p><p class="prize">$7,000</p><p style="color:var(--gold);font-weight:700;font-size:.95rem">+ 15,000 ELITE Points</p></div>
    <div class="pod first rv d1"><span class="medal">🥇</span><p class="place">1st Place</p><p class="pod-user" data-pod="1">—</p><p class="prize">$12,500</p><p style="color:var(--gold);font-weight:700;font-size:.95rem">+ 15,000 ELITE Points</p></div>
    <div class="pod rv d2"><span class="medal">🥉</span><p class="place">3rd Place</p><p class="pod-user" data-pod="3">—</p><p class="prize">$5,000</p><p style="color:var(--gold);font-weight:700;font-size:.95rem">+ 15,000 ELITE Points</p></div>
  </div>
  {LB_TABLE}
  <div class="hero-grid" style="margin-top:60px">
    <div>
      <h2 class="rv">How the Leaderboard Works</h2>
      <div style="display:grid;gap:14px;margin-top:20px">
        <div class="mile rv"><span class="amt">Step 1</span><p style="flex:1;color:var(--muted)">Sign up on Roobet with code <b style="color:var(--gold)">ELITE</b> or <b style="color:var(--gold)">DAILY</b>.</p></div>
        <div class="mile rv d1"><span class="amt">Step 2</span><p style="flex:1;color:var(--muted)">Play and climb — slots and similar gameplay count at the full rate. Weighted wagering applies (see below).</p></div>
        <div class="mile rv d2"><span class="amt">Step 3</span><p style="flex:1;color:var(--muted)">Track your rank all month long — payouts hit at the end of each month.</p></div>
        <div class="mile rv d3"><span class="amt">Step 4</span><p style="flex:1;color:var(--muted)">Stack your leaderboard prizes with <a href="/wager-milestones" style="color:var(--gold);font-weight:700">Wager Milestones</a> — the same wagers count twice.</p></div>
      </div>
    </div>
    <div class="rv d2"><div class="phone"><video autoplay muted loop playsinline src="/assets/wager.mp4" aria-label="Wager leaderboard in action"></video></div></div>
  </div>
  {WEIGHTED}
</div></section>

{cta_banner("The Race Is Already Running","Every wager counts from the second you join. Get on the board and claim your share of $50,000.",funnel="Join via Slotessentials")}
""")

# ================= MILESTONES =================
miles = [
    ("$10,000", "$10", False), ("$25,000", "$30", False), ("$50,000", "$60", False),
    ("$100,000", "$100", False), ("$250,000", "$150", True), ("$500,000", "$250", True),
    ("$1,000,000", "$500", True), ("$2,500,000", "$1,000", True), ("$3,500,000", "$1,750", True),
    ("$5,000,000", "$2,500", True), ("$10,000,000", "$5,000", True),
]
mile_html = "".join(
    f'<div class="mile rv"><span class="mw">Wager — {w}</span><span class="mr">{r}{"+" if plus else ""}</span>'
    + (f'<a class="pill claim" href="{SLOTS_MILES}" target="_blank" rel="noopener">Claim</a>' if i == 0
       else '<span class="pill locked">🔒 Locked</span>')
    + '</div>'
    for i, (w, r, plus) in enumerate(miles))
PAGES["wager-milestones.html"] = dict(
    title="Roobet Wager Milestones — Claim Up to $11,350 Extra Monthly | Code ELITE & DAILY",
    desc="Claim up to $11,350 in extra monthly rewards with Roobet wager milestones. Hit wager targets under code ELITE or DAILY and every milestone pays out — guaranteed, no luck needed.",
    kw="roobet wager milestones, wager rewards, roobet bonus, best casino rewards, $11,350 milestones",
    body=f"""
<section class="page-hero"><div class="wrap">
  {crumb("Wager Milestones")}
  <span class="eyebrow rv">🎯 Guaranteed Rewards</span>
  <h1 class="rv d1">Claim Up to <span class="grad" data-count="11350" data-prefix="$">$0</span> Every Month</h1>
  <p class="lead rv d2">No raffles. No luck. Hit a wager milestone under code <b style="color:var(--gold)">ELITE</b> or <b style="color:var(--gold)">DAILY</b> and the reward is yours — every month, the counter resets and you can claim it all again.</p>
  <div class="hero-cta rv d3" style="justify-content:center"><a class="btn btn-gold btn-lg pulse" href="{ELITE}" rel="nofollow sponsored" target="_blank">Start Claiming {ARR}</a></div>
</div></section>

<section style="padding-top:10px"><div class="wrap" style="max-width:860px">
  <h2 class="center rv" style="margin-bottom:30px">Monthly Milestone Track</h2>
  {mile_html}
  <p class="rv" style="color:var(--muted);font-size:.88rem;margin-top:18px;text-align:center">Tiers marked <b style="color:var(--gold)">+</b> can pay even more. Milestones stack with the <a href="/leaderboard" style="color:var(--gold)">$50K Leaderboard</a>: the same wagers count toward both.</p>
  {WEIGHTED}
</div></section>

<section style="padding-top:0"><div class="wrap"><div class="cards c3">
  <div class="card rv"><div class="glow"></div><div class="ic">🔁</div><h3>Resets Monthly</h3><p>Every month is a fresh track. Claim the full $11,350 in extra rewards again and again.</p></div>
  <div class="card rv d1"><div class="glow"></div><div class="ic">➕</div><h3>Stacks with Everything</h3><p>Milestone wagers also count for the leaderboard, ELITE Points and Roobet's own rakeback.</p></div>
  <div class="card rv d2"><div class="glow"></div><div class="ic">💵</div><h3>Guaranteed Payouts</h3><p>Milestones aren't a lottery — hit the number, claim the reward. Simple as that.</p></div>
</div></div></section>

{cta_banner("Your Wagers Should Pay You Twice","Join under ELITE or DAILY and turn every session into leaderboard progress and milestone cash.")}
""")

# ================= FREE SPINS =================
PAGES["free-spins.html"] = dict(
    title="Roobet Free Spins — Exclusive Sign-Up Bonus up to 125 Free Spins | Code ELITE & DAILY",
    desc="Get exclusive Roobet free spins with our sign-up bonus: up to 125 free spins at $1.00 per spin. Deposit, wager, and claim the biggest Roobet free spins package with code ELITE or DAILY.",
    kw="roobet free spins, free spins roobet, sign-up bonus, no deposit free spins, roobet sign up bonus, exclusive free spins",
    schema={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":"How do I get Roobet free spins?","acceptedAnswer":{"@type":"Answer","text":"Sign up at Roobet with code ELITE or DAILY — your all-time deposit and wager totals unlock up to 125 exclusive free spins worth up to $1.00 per spin. It's cumulative, not a single deposit."}},
        {"@type":"Question","name":"Are there no deposit free spins on Roobet?","acceptedAnswer":{"@type":"Answer","text":"Our exclusive free spins packages require a deposit and wager. Active players can also win free spins and prizes through our $5,000 monthly community giveaways and by redeeming ELITE Points — giveaways are earned through activity, not luck."}}]},
    body=f"""
<section class="page-hero"><div class="wrap">
  {crumb("Free Spins Bonus")}
  <span class="eyebrow rv">🎰 Exclusive Sign-Up Bonus</span>
  <h1 class="rv d1">Roobet Free Spins — Up to <span class="grad">125 Spins</span> at $1.00 Each</h1>
  <p class="lead rv d2">The biggest Roobet free spins deal you'll find. Join with code <b style="color:var(--gold)">ELITE</b> or <b style="color:var(--gold)">DAILY</b> — your <b style="color:var(--text)">all-time</b> deposit &amp; wager totals unlock the tiers, so every session gets you closer.</p>
  <div class="hero-cta rv d3" style="justify-content:center"><a class="btn btn-gold btn-lg pulse" href="{SLOTS}" target="_blank" rel="noopener">Claim Free Spins {ARR}</a></div>
</div></section>

<section style="padding-top:10px"><div class="wrap"><div class="cards c3">
  <div class="card rv center"><div class="glow"></div><p class="amount">75 Spins</p><p style="font-weight:700;color:var(--text)">$0.60 per spin — $45 value</p><p style="margin-top:10px">Deposit <b style="color:var(--gold)">$500</b> all-time<br>Wager <b style="color:var(--gold)">$5,000</b> all-time</p></div>
  <div class="card rv d1 center" style="border-color:rgba(255,199,0,.5)"><span class="tag">Most Popular</span><div class="glow"></div><p class="amount">100 Spins</p><p style="font-weight:700;color:var(--text)">$0.80 per spin — $80 value</p><p style="margin-top:10px">Deposit <b style="color:var(--gold)">$1,000</b> all-time<br>Wager <b style="color:var(--gold)">$10,000</b> all-time</p></div>
  <div class="card rv d2 center"><span class="tag">Max Value</span><div class="glow"></div><p class="amount">125 Spins</p><p style="font-weight:700;color:var(--text)">$1.00 per spin — $125 value</p><p style="margin-top:10px">Deposit <b style="color:var(--gold)">$2,000</b> all-time<br>Wager <b style="color:var(--gold)">$20,000</b> all-time</p></div>
</div>
<p class="rv center" style="margin-top:24px;color:var(--muted);font-size:.92rem">Tiers are based on your <b style="color:var(--gold)">all-time</b> deposit and wager totals under code DAILY or ELITE — not a single deposit. Every session counts toward your next tier.</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
  <div class="cards c2">
    <div class="card rv"><div class="glow"></div><div class="ic">🎁</div><h3>More Ways to Win Spins</h3><p>Active players earn entries in our <a href="/giveaways" style="color:var(--gold);font-weight:700">$5,000 monthly giveaways</a> and collect <a href="/elite-points" style="color:var(--gold);font-weight:700">ELITE Points</a> by watching DailyGambling live on Kick — redeemable for prizes including spins.</p></div>
    <div class="card rv d1"><div class="glow"></div><div class="ic">⚡</div><h3>Stack Your Welcome Boost</h3><p>New sign-ups get a +10% welcome rakeboost for 24 hours. Your qualifying wagers also count toward the <a href="/leaderboard" style="color:var(--gold);font-weight:700">$50K Leaderboard</a> and <a href="/wager-milestones" style="color:var(--gold);font-weight:700">Wager Milestones</a> at the same time.</p></div>
  </div>
</div></section>

{cta_banner("125 Free Spins Are Waiting","Sign up with DAILY or ELITE, pick your tier, and spin on us.",funnel="Get Your Free Spins")}
""")

# ================= MAX WIN MERCH =================
merch_sets = [
    ("Pragmatic Play Collection", "🐟", "Max win a Pragmatic Play classic — Gates of Olympus, Sweet Bonanza, Big Bass and more — and claim the matching exclusive shirt."),
    ("Hacksaw Gaming Collection", "⛏️", "Wanted Dead or a Wild, Le Bandit and the rest of the Hacksaw hall of fame — every max win earns the shirt."),
    ("Nolimit City Collection", "🔥", "Survive a Nolimit max win — Mental, Tombstone, Fire in the Hole — and wear the proof."),
    ("Slotessentials General Collection", "⭐", "Exclusive Slotessentials designs for max wins across the rest of the casino."),
]
merch_html = "".join(f"""<div class="card rv d{i%2+1}"><div class="glow"></div><div class="ic">{ic}</div><h3>{t}</h3><p>{d}</p></div>""" for i, (t, ic, d) in enumerate(merch_sets))

MERCH = [
    ("le-bandit", "Le Bandit", "Hacksaw Gaming", "le-bandit-hacksaw.png"),
    ("six-six-six", "Six Six Six", "Hacksaw Gaming", "six-six-six-hacksaw.png"),
    ("gates-of-olympus", "Gates of Olympus", "Pragmatic Play", "gates-of-olympus-pragmatic.png"),
    ("sweet-bonanza", "Sweet Bonanza", "Pragmatic Play", "sweet-bonanza-pragmatic.png"),
    ("sugar-rush", "Sugar Rush", "Pragmatic Play", "sugar-rush-pragmatic.png"),
    ("big-bass", "Big Bass", "Pragmatic Play", "big-bass-pragmatic.png"),
    ("mental", "Mental", "Nolimit City", "mental-nolimit-city.png"),
    ("rip-city-benny-the-beer", "RIP City &amp; Benny the Beer", "Hacksaw Gaming", "rip-city-and-benny-the-beer-hacksaw.png"),
]
shirt_cards = "".join(f"""<a class="card rv d{i%3+1}" href="{slug}-max-win-shirt.html"><div class="glow"></div><img src="assets/{img}" alt="{name} Max Win Shirt — exclusive {prov} merch" loading="lazy" style="border-radius:12px;margin-bottom:16px;filter:drop-shadow(0 12px 30px rgba(0,0,0,.45))"><h3>{name} Max Win Shirt</h3><p>{prov}</p><span class="more">View shirt {ARR}</span></a>""" for i, (slug, name, prov, img) in enumerate(MERCH))
shirt_cards += f"""<div class="card rv center" style="display:flex;flex-direction:column;justify-content:center;align-items:center;min-height:280px"><div class="ic">🔒</div><h3>8 More Designs</h3><p>Revealed as they drop — keep hitting max wins.</p></div>"""
PAGES["max-win-merch.html"] = dict(
    title="Roobet Max Win Merch — Free Exclusive Shirts for Every Max Win | Code ELITE & DAILY",
    desc="Hit a max win on Pragmatic Play, Hacksaw or Nolimit City slots under code ELITE or DAILY and get exclusive Max Win Merch shipped free. 16 exclusive shirt designs to collect.",
    kw="roobet max win merch, max win shirt, pragmatic play max win, hacksaw max win, nolimit max win, free merch casino",
    body=f"""
<section class="page-hero"><div class="wrap">
  {crumb("Max Win Merch")}
  <span class="eyebrow rv">👕 16 Exclusive Designs</span>
  <h1 class="rv d1">Hit a Max Win.<br><span class="grad">Get the Shirt.</span></h1>
  <p class="lead rv d2">Every max win you hit on Roobet under code <b style="color:var(--gold)">ELITE</b> or <b style="color:var(--gold)">DAILY</b> earns you an exclusive Max Win shirt — shipped free, anywhere. Collect all 16.</p>
  <div class="hero-cta rv d3" style="justify-content:center"><a class="btn btn-gold btn-lg pulse" href="{ELITE}" rel="nofollow sponsored" target="_blank">Start Hunting Max Wins {ARR}</a></div>
</div></section>

<section style="padding-top:10px"><div class="wrap">
  <div class="center rv"><span class="eyebrow">👕 The Shirts</span><h2>Available Now</h2></div>
  <div class="cards c3" style="margin-top:36px">{shirt_cards}</div>
  <div class="cards c2" style="margin-top:50px">{merch_html}</div>
  <div class="steps" style="margin-top:50px">
    <div class="step rv"><h3>Play Under Our Codes</h3><p>Max wins only count while playing under ELITE or DAILY on Roobet.</p></div>
    <div class="step rv d1"><h3>Hit the Max Win</h3><p>Land the maximum win on any qualifying Pragmatic, Hacksaw or Nolimit slot.</p></div>
    <div class="step rv d2"><h3>Send Us Proof</h3><p>Share your max win screenshot with the <a href="{TELEGRAM}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">VIP team on Telegram</a>.</p></div>
    <div class="step rv d3"><h3>Get Your Shirt</h3><p>We ship the exclusive design for that game — completely free.</p></div>
  </div>
</div></section>

{cta_banner("The Rarest Merch in Gambling","You can't buy these shirts. You can only win them. Join with ELITE or DAILY and start hunting.")}
""")

# ================= VIP TRANSFER =================
PAGES["vip-transfer.html"] = dict(
    title="Transfer Your VIP Status to Roobet — Keep Your Level & Rewards | Code ELITE & DAILY",
    desc="Transfer your VIP status from any casino directly to Roobet. Keep your level, rakeback and bonuses — no starting over. Join with code ELITE or DAILY for the full rewards package.",
    kw="roobet vip transfer, transfer vip status, roobet vip, casino vip transfer, roobet rewards",
    body=f"""
<section class="page-hero"><div class="wrap">
  <p class="breadcrumb rv"><a href="/">Home</a> / VIP Transfer</p>
  <span class="eyebrow rv">💎 Skip the Grind</span>
  <h1 class="rv d1">Transfer Your <span class="grad">VIP Status</span> to Roobet</h1>
  <p class="lead rv d2">Grinding a VIP level somewhere else? Don't start from zero. Roobet matches your VIP status from any casino — and the moment you transfer, you unlock access to <b style="color:var(--text)">every single reward we offer</b>.</p>
  <div class="hero-cta rv d3" style="justify-content:center">
    <a class="btn btn-gold btn-lg pulse" href="{SLOTS}" target="_blank" rel="noopener">Transfer My VIP {ARR}</a>
    <a class="btn btn-ghost btn-lg" href="{TELEGRAM}" target="_blank" rel="noopener">Message the VIP Team</a>
  </div>
  <p class="rv d4" style="margin-top:20px;color:var(--muted);font-size:.92rem">Prefer Discord? <a href="{DISCORD}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">Open a ticket</a> and we'll take it from there.</p>
</div></section>

<section style="padding-top:10px"><div class="wrap">
  <div class="steps">
    <div class="step rv"><h3>Sign Up</h3><p>Create your Roobet account with code <a href="{DAILY}" rel="nofollow sponsored" target="_blank" style="color:var(--gold);font-weight:700">DAILY</a> or <a href="{ELITE}" rel="nofollow sponsored" target="_blank" style="color:var(--gold);font-weight:700">ELITE</a>.</p></div>
    <div class="step rv d1"><h3>Contact Us</h3><p>Message the <a href="{TELEGRAM}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">VIP team on Telegram</a> or open a <a href="{DISCORD}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">Discord ticket</a>, then fill in the VIP form on Slotessentials.</p></div>
    <div class="step rv d2"><h3>Get Matched</h3><p>Roobet transfers your status — level, rakeback rate and bonuses intact.</p></div>
    <div class="step rv d3"><h3>Unlock Everything</h3><p>Your transferred status opens the door to the full $100K monthly rewards package below.</p></div>
  </div>
</div></section>

<section style="padding-top:0"><div class="wrap">
  <div class="center rv"><span class="eyebrow">🔓 What You Unlock</span><h2>Every Reward. Instantly.</h2><p class="lead">Transferring your VIP status gives you access to all of it — the complete $100,000 monthly rewards package.</p></div>
  <div class="cards c4" style="margin-top:40px">
    <a class="card rv" href="/leaderboard"><div class="glow"></div><div class="ic">🏆</div><h3>$50K Leaderboard</h3><p>Monthly wager race with a $12,500 top prize.</p><span class="more">Explore {ARR}</span></a>
    <a class="card rv d1" href="/wager-milestones"><div class="glow"></div><div class="ic">🎯</div><h3>$11,350 Milestones</h3><p>Guaranteed payouts at every wager tier.</p><span class="more">Explore {ARR}</span></a>
    <a class="card rv d2" href="/free-spins"><div class="glow"></div><div class="ic">🎰</div><h3>Free Spins Bonus</h3><p>Up to 125 exclusive spins at $1.00 each.</p><span class="more">Explore {ARR}</span></a>
    <a class="card rv d3" href="/max-win-merch"><div class="glow"></div><div class="ic">👕</div><h3>Max Win Merch</h3><p>Free exclusive shirts for every max win.</p><span class="more">Explore {ARR}</span></a>
    <a class="card rv" href="/elite-points"><div class="glow"></div><div class="ic">⭐</div><h3>ELITE Points</h3><p>Earn daily, redeem in the Point Shop.</p><span class="more">Explore {ARR}</span></a>
    <a class="card rv d1" href="/slot-challenges"><div class="glow"></div><div class="ic">🎮</div><h3>Slot Challenges</h3><p>Extra prizes for completing challenges.</p><span class="more">Explore {ARR}</span></a>
    <a class="card rv d2" href="/giveaways"><div class="glow"></div><div class="ic">🎁</div><h3>$5K Giveaways</h3><p>Monthly community giveaways for active players.</p><span class="more">Explore {ARR}</span></a>
    <a class="card rv d3" href="/roobet-rewards"><div class="glow"></div><div class="ic">💰</div><h3>Roobet Rewards</h3><p>Rakeback every 30 min, vault &amp; rakeboosts.</p><span class="more">Explore {ARR}</span></a>
  </div>
  <div class="cards c3" style="margin-top:40px">
    <div class="card rv"><div class="glow"></div><div class="ic">📈</div><h3>Higher Level = Bigger Bonuses</h3><p>Daily, weekly and monthly bonus percentages scale with your level — transfer high, earn high from day one.</p></div>
    <div class="card rv d1"><div class="glow"></div><div class="ic">⚡</div><h3>+10% Rank-Up Boosts</h3><p>Every rank-up after your transfer triggers a +10% rakeboost for 60 minutes.</p></div>
    <div class="card rv d2"><div class="glow"></div><div class="ic">🤝</div><h3>Exclusive VIP Team</h3><p>Your transfer is handled personally — plus extra rewards and promos our regular players never see.</p></div>
  </div>
</div></section>

{cta_banner("Your Status Travels With You","Transfer your VIP level and every reward on this site unlocks with it. Questions? The VIP team is one message away.",funnel="Start My VIP Transfer",
extra=f'<p style="margin-top:22px;color:var(--muted)"><a href="{TELEGRAM}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">VIP Team on Telegram</a> &nbsp;·&nbsp; <a href="{DISCORD}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">Open a Discord Ticket</a></p>')}
""")

# ================= ELITE POINTS =================
SHOP = [
    ("$10 Free Balance", "$10", "$5,000", "6,000", "$10 will be credited to your Roobet account."),
    ("$20 Free Balance", "$20", "$7,000", "11,000", "$20 CAD will be credited to your Roobet account."),
    ("$50 Free Balance", "$50", "$10,000", "28,000", "$50 will be credited to your Roobet account."),
    ("$100 Free Balance", "$100", "$15,000", "55,000", "$100 will be credited to your Roobet account."),
    ("$250 Free Balance", "$250", "$20,000", "140,000", "$250 will be credited to your Roobet account."),
    ("$500 Free Balance", "$500", "$50,000", "275,000", "$500 will be credited to your Roobet account."),
    ("$100 Bonus Buy", "$100", "$15,000", "60,000", "$100 Bonus Buy — keep 100% of the return."),
    ("$300 Bonus Buy", "$300", "$30,000", "180,000", "$300 Bonus Buy — keep 100% of the return."),
    ("$500 Bonus Buy", "$500", "$50,000", "300,000", "$500 Bonus Buy — keep 100% of the return."),
    ("$1000 Bonus Buy", "$1,000", "$80,000", "600,000", "$1,000 Bonus Buy — keep 100% of the return."),
]
shop_html = "".join(f"""<div class="flip rv d{i%3+1}"><div class="flip-inner">
<div class="face front"><p class="amount" style="margin:0">{amt}</p><h3 style="font-size:1.05rem">{name}</h3><p style="color:var(--muted);font-size:.88rem">{wag} wagered<br>{pts} points</p><a class="pill claim" href="{SLOTS_HOME}" target="_blank" rel="noopener">Claim</a><span style="font-size:.74rem;color:var(--muted)">Tap card for requirements</span></div>
<div class="face back"><h3 style="font-size:.95rem;color:var(--gold)">Claim Requirements</h3><p style="color:var(--muted);font-size:.83rem">{req} This offer is exclusively available to code ELITE &amp; DAILY affiliates.</p><p style="font-size:.85rem">Minimum Wagered: <b style="color:var(--gold)">{wag}</b></p><p style="font-size:.85rem">Points Required: <b style="color:var(--gold)">{pts} points</b></p><a class="pill claim" href="{SLOTS_HOME}" target="_blank" rel="noopener">Claim</a></div>
</div></div>""" for i, (name, amt, wag, pts, req) in enumerate(SHOP))

PAGES["elite-points.html"] = dict(
    title="ELITE Points — Earn & Redeem for Real Prizes | Slotessentials x Roobet",
    desc="Earn ELITE Points by watching DailyGambling on Kick, wagering under code ELITE or DAILY on Roobet, placing on the leaderboard and staying active on Slotessentials. Redeem for real prizes.",
    kw="elite points, slotessentials points, roobet points, redeem points prizes, dailygambling kick",
    body=f"""
<section class="page-hero"><div class="wrap">
  {crumb("ELITE Points")}
  <span class="eyebrow rv">⭐ Loyalty That Pays</span>
  <h1 class="rv d1">Earn <span class="grad">ELITE Points</span>.<br>Redeem Real Prizes.</h1>
  <p class="lead rv d2">Every stream you watch, every wager you place, every leaderboard finish — it all earns ELITE Points via Slotessentials, redeemable for real prizes.</p>
  <div class="hero-cta rv d3" style="justify-content:center">
    <a class="btn btn-gold btn-lg pulse" href="{ELITE}" rel="nofollow sponsored" target="_blank">Start Earning {ARR}</a>
    <a class="btn btn-ghost btn-lg" href="{KICK}" target="_blank" rel="noopener">Watch DailyGambling Live</a>
  </div>
</div></section>

<section style="padding-top:10px"><div class="wrap"><div class="cards c4">
  <div class="card rv"><div class="glow"></div><div class="ic">📺</div><h3>Watch Streams</h3><p>Earn points live during <a href="{KICK}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">Kick.com/DailyGambling</a> streams — activity is all it takes.</p></div>
  <div class="card rv d1"><div class="glow"></div><div class="ic">🎲</div><h3>Wager on Roobet</h3><p>Active wagering under code ELITE or DAILY earns points automatically.</p></div>
  <div class="card rv d2"><div class="glow"></div><div class="ic">🏆</div><h3>Place on the Leaderboard</h3><p>Leaderboard finishes come with point bonuses on top of cash prizes.</p></div>
  <div class="card rv d3"><div class="glow"></div><div class="ic">💬</div><h3>Stay Active</h3><p>Activity across Slotessentials keeps the points flowing.</p></div>
</div>
<div style="margin-top:70px" id="point-shop">
  <div class="center rv"><span class="eyebrow">🛍️ ELITE Point Shop</span><h2>Redeem Your Points</h2><p class="lead">Free balance and bonus buys — tap any card to see its claim requirements.</p></div>
  <div class="shop" style="margin-top:36px">{shop_html}</div>
</div>

<div style="margin-top:70px">
  <div class="center rv"><span class="eyebrow">📋 How to Claim</span><h2>Claiming Is Simple</h2></div>
  <div class="steps" style="margin-top:36px">
    <div class="step rv"><h3>Press Claim</h3><p>Find the item you want in the shop and press Claim, then fill in the required information.</p></div>
    <div class="step rv d1"><h3>Open a Discord Ticket</h3><p>You'll be prompted to join the <a href="{DISCORD}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">SlotEssentials Discord</a> and open a ticket.</p></div>
    <div class="step rv d2"><h3>Points Deducted</h3><p>Your ELITE Points are automatically deducted from your account.</p></div>
    <div class="step rv d3"><h3>Protected Refunds</h3><p>If the wager requirement isn't met or any issue arises, your points are automatically returned.</p></div>
  </div>
</div>

<div style="margin-top:70px">
  <div class="center rv"><span class="eyebrow">⚡ More Ways to Earn</span><h2>Stack Points Every Day</h2></div>
  <div class="cards c2" style="margin-top:36px">
    <div class="card rv"><div class="glow"></div><div class="ic">📦</div><h3>Daily Case</h3><p>Log into your Slotessentials account and open the Daily Case at the top of the main menu every day. Rewards increase with your level — higher levels earn more points daily.</p></div>
    <div class="card rv d1"><div class="glow"></div><div class="ic">📺</div><h3>Kick Stream — 50 Points / 15 Min</h3><p>Watch <a href="{KICK}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">DailyGambling live on Kick</a> every day — every 15 minutes of activity earns you 50 points.</p></div>
    <div class="card rv d2"><div class="glow"></div><div class="ic">🏆</div><h3>Top 100 Leaderboard</h3><p>Place in the top 100 of the <a href="/leaderboard" style="color:var(--gold);font-weight:700">monthly wager leaderboard</a> each month to earn points.</p></div>
    <div class="card rv d3"><div class="glow"></div><div class="ic">📸</div><h3>Record Win Submissions</h3><p>Submit your record wins on Slotessentials for points. One record win entry per day counts toward your balance.</p></div>
  </div>
</div>

<div class="cta-banner rv" style="margin-top:70px;text-align:left">
  <h2 style="text-align:center">Point Shop Requirements</h2>
  <ul style="max-width:720px;margin:20px auto 0;color:var(--muted);line-height:2;padding-left:20px">
    <li>You must open a ticket in <a href="{DISCORD}" target="_blank" rel="noopener" style="color:var(--gold)">our Discord</a> to claim prizes.</li>
    <li>All redemptions are location specific and have a minimum wager requirement in USD on Roobet — read the disclaimer and terms &amp; conditions upon redemption.</li>
    <li>Redemptions that do not meet the wager requirement will be rejected and points refunded.</li>
    <li>No transfer of points among users.</li>
  </ul>
</div>

<div class="cta-banner rv" style="margin-top:26px">
  <h2>Bonus: +20% Rakeboost</h2>
  <p class="lead">Redeeming an affiliate code triggers a <b style="color:var(--gold)">+20% rakeboost for 72 hours</b> — the biggest boost in the game. Pair it with your points grind.</p>
  <div class="hero-cta" style="justify-content:center"><a class="btn btn-gold btn-lg" href="{DAILY}" rel="nofollow sponsored" target="_blank">Redeem Code DAILY {ARR}</a></div>
</div>
</div></section>
""")

# ================= SLOT CHALLENGES =================
PAGES["slot-challenges.html"] = dict(
    title="Roobet Slot Challenges — Complete Challenges, Claim Extra Prizes | Code ELITE & DAILY",
    desc="Complete Roobet slot challenges while you play and claim extra prizes on top of your regular rewards. Active challenges for players under code ELITE or DAILY.",
    kw="roobet slot challenges, casino challenges, slot challenge prizes, roobet rewards",
    body=f"""
<section class="page-hero"><div class="wrap">
  {crumb("Slot Challenges")}
  <span class="eyebrow rv">🎮 Play With a Mission</span>
  <h1 class="rv d1"><span class="grad">Slot Challenges</span> — Extra Prizes While You Play</h1>
  <p class="lead rv d2">Hit a target multiplier, bonus-hunt a specific slot, land a feature — complete challenges and claim prizes on top of everything else you're earning.</p>
  <div class="hero-cta rv d3" style="justify-content:center"><a class="btn btn-gold btn-lg pulse" href="{ELITE}" rel="nofollow sponsored" target="_blank">Join the Challenges {ARR}</a></div>
</div></section>

<section style="padding-top:10px"><div class="wrap"><div class="cards c3">
  <div class="card rv"><div class="glow"></div><div class="ic">✖️</div><h3>Multiplier Hunts</h3><p>Hit a target multiplier on a featured slot and claim the challenge prize.</p></div>
  <div class="card rv d1"><div class="glow"></div><div class="ic">🎰</div><h3>Featured Slots</h3><p>New challenge slots rotate regularly — fresh targets, fresh prizes.</p></div>
  <div class="card rv d2"><div class="glow"></div><div class="ic">🥇</div><h3>First to Finish</h3><p>Some challenges pay the first player to hit the target — speed matters.</p></div>
</div>
<p class="rv center" style="margin-top:34px;color:var(--muted)">Active challenges are posted in the Slotessentials community and announced live on <a href="{KICK}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">DailyGambling</a> streams.</p>
</div></section>

{cta_banner("A New Challenge Is Always Live","Play with a mission — and get paid extra for it. Join with ELITE or DAILY.")}
""")

# ================= GIVEAWAYS =================
PAGES["giveaways.html"] = dict(
    title="$5,000 Monthly Giveaways — Community Prizes for Active Players | Roobet Casino Rewards",
    desc="We give $5,000 back to our community every month. No catch — only active players earn giveaways. Watch DailyGambling on Kick, wager under code DAILY or ELITE, and win prizes.",
    kw="casino giveaways, roobet giveaway, slotessentials giveaway, community giveaways",
    body=f"""
<section class="page-hero"><div class="wrap">
  {crumb("$5K Giveaways")}
  <span class="eyebrow rv">🎁 Earned by Active Players</span>
  <h1 class="rv d1"><span class="grad" data-count="5000" data-prefix="$">$0</span> in Giveaways.<br>Every Single Month.</h1>
  <p class="lead rv d2">No catch — only active players earn giveaways. We give $5,000 back to the community every month in cash, free spins and prizes for the players who show up.</p>
  <div class="hero-cta rv d3" style="justify-content:center">
    <a class="btn btn-gold btn-lg pulse" href="{KICK}" target="_blank" rel="noopener">Watch &amp; Enter Live {ARR}</a>
    <a class="btn btn-ghost btn-lg" href="{DAILY}" rel="nofollow sponsored" target="_blank">Join Roobet with DAILY</a>
  </div>
</div></section>

<section id="raffle" style="padding-top:10px"><div class="wrap">
  <div class="cta-banner rv" id="raffle-widget">
    <span class="eyebrow">🎟️ Live Raffle</span>
    <h2 id="rf-title">Checking for a live raffle…</h2>
    <p class="lead" id="rf-info">One moment.</p>
    <div class="hero-cta" style="justify-content:center;margin-top:22px" id="rf-actions"></div>
    <p style="margin-top:16px;color:var(--muted);font-size:.88rem" id="rf-meta"></p>
  </div>
</div></section>

<section style="padding-top:0"><div class="wrap"><div class="cards c3">
  <div class="card rv"><div class="glow"></div><div class="ic">📺</div><h3>Live Stream Giveaways</h3><p>Drops happen live on <a href="{KICK}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">Kick.com/DailyGambling</a> — show up, enter, win.</p></div>
  <div class="card rv d1"><div class="glow"></div><div class="ic">💬</div><h3>Community Drops</h3><p>Extra giveaways across the Slotessentials community all month long — <a href="{DISCORD}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">join the Discord</a> so you never miss one.</p></div>
  <div class="card rv d2"><div class="glow"></div><div class="ic">🚀</div><h3>Bigger for Members</h3><p>Players under code ELITE or DAILY get access to boosted, members-only giveaways.</p></div>
</div></div></section>

{cta_banner("Show Up. Stay Active. Get Paid.","Giveaways are earned by the players who are present — be active and take your share of $5,000 every month.")}
""")

# ================= ROOBET REWARDS (native) =================
boosts = [
    ("On Signup", "+10%", "24 hours", "Welcome boost the moment you join"),
    ("On Rank Up", "+10%", "60 minutes", "Every level-up triggers a boost"),
    ("Daily Claim", "+10%", "60 minutes", "Claim your daily bonus, get boosted"),
    ("Weekly Claim", "+10%", "60 minutes", "Weekly bonus claim boost"),
    ("Monthly Claim", "+10%", "60 minutes", "Monthly bonus claim boost"),
    ("Vault Calendar", "+15%", "60 minutes", "Vault calendar claims boost harder"),
    ("Affiliate Code Redemption", "+20%", "72 hours", "The biggest boost — redeem code ELITE or DAILY"),
]
boost_rows = "".join(f'<tr><td>{n}</td><td class="gold-td">{b}</td><td>{d}</td><td style="color:var(--muted)">{note}</td></tr>' for n, b, d, note in boosts)
PAGES["roobet-rewards.html"] = dict(
    title="Roobet Rewards Explained — Rakeback, Vault, Daily/Weekly/Monthly Bonuses & Rakeboosts",
    desc="The complete guide to Roobet rewards: instant rakeback every 30 minutes, daily, weekly and monthly bonuses, the Vault system, level-up bonuses and rakeboosts up to +20%.",
    kw="roobet rewards, roobet rakeback, roobet vault, roobet daily bonus, roobet weekly bonus, roobet monthly bonus, rakeboost",
    schema={"@context":"https://schema.org","@type":"Article","headline":"Roobet Rewards Explained — Rakeback, Vault & Bonuses","author":{"@type":"Organization","name":"Roobet Casino Rewards"},"publisher":{"@type":"Organization","name":"Roobet Casino Rewards"}},
    body=f"""
<section class="page-hero"><div class="wrap">
  {crumb("Roobet Rewards")}
  <span class="eyebrow rv">💰 The Complete Guide</span>
  <h1 class="rv d1">Roobet Rewards, <span class="grad">Fully Explained</span></h1>
  <p class="lead rv d2">Roobet is giving out more money than ever. As long as you're active, you'll have something to claim <b style="color:var(--gold)">every 30 minutes</b>. Here's exactly how every piece works.</p>
  <div class="hero-cta rv d3" style="justify-content:center"><a class="btn btn-gold btn-lg pulse" href="{ELITE}" rel="nofollow sponsored" target="_blank">Unlock All Rewards {ARR}</a></div>
</div></section>

<section style="padding-top:10px"><div class="wrap"><div class="cards c2">
  <div class="card rv"><div class="glow"></div><div class="ic">⚡</div><h3>Instant Rakeback — Every 30 Minutes</h3><p>A percentage of your wagered amount, claimable every 30 minutes — and it <b style="color:var(--text)">never expires</b>. Part lands instantly in your balance; part flows into your Vault for your 3 daily vault claims.</p></div>
  <div class="card rv d1"><div class="glow"></div><div class="ic">🌅</div><h3>Daily Bonus — Midnight UTC</h3><p>Accumulates for up to 72 hours, claimable every 24 hours at midnight UTC. A level-based percentage hits your balance instantly; the rest fills your 7-day vault calendar.</p></div>
  <div class="card rv d2"><div class="glow"></div><div class="ic">📅</div><h3>Weekly Bonus — Saturdays</h3><p>Released every Saturday at 7 PM EST / midnight UTC. Instant percentage to balance based on your level, plus a 14-day vault calendar allocation.</p></div>
  <div class="card rv d3"><div class="glow"></div><div class="ic">🗓️</div><h3>Monthly Bonus — The 1st</h3><p>Drops the 1st of every month at midnight UTC. Instant balance boost by level, plus a 14-day vault calendar allocation. Countdown: <b style="color:var(--gold);font-variant-numeric:tabular-nums" data-deadline="monthly">—</b></p></div>
</div>

<div class="cta-banner rv" style="margin-top:26px">
  <h2>🔐 The Vault — 3 Claims Per Day</h2>
  <p class="lead">The Vault unlocks every 8 hours starting 12:00 AM UTC — three claims a day, and it can't be claimed all at once. Rewards expire 24 hours after collection unlocks, so claim on schedule. Miss a window before your next reward lands and it's gone.</p>
</div>

<h2 class="rv" style="margin-top:60px">Rakeboosts — Stack the Multiplier</h2>
<p class="lead rv" style="margin-bottom:24px">Rakeboosts supercharge your Instant Rakeback claim. They don't stack or queue — you always run on the single highest active boost.</p>
<div class="tbl-wrap rv"><table class="tbl">
<thead><tr><th>Trigger</th><th>Boost</th><th>Duration</th><th>Note</th></tr></thead>
<tbody>{boost_rows}</tbody>
</table></div>

<div class="cards c2" style="margin-top:40px">
  <div class="card rv"><div class="glow"></div><div class="ic">📈</div><h3>Level-Up Bonuses</h3><p>Wagering levels up your account, and every level-up pays a bonus — the higher the level, the bigger the bonus. <a href="/vip-transfer" style="color:var(--gold);font-weight:700">Transfer your VIP status</a> to start high.</p></div>
  <div class="card rv d1"><div class="glow"></div><div class="ic">⏰</div><h3>Claim on Time</h3><p>Unclaimed rewards expire when your next reward becomes available. Active players who claim on schedule extract every dollar the system offers.</p></div>
</div>
</div></section>

{cta_banner("Every 30 Minutes, Something to Claim","Join with code ELITE or DAILY — the +20% code-redemption rakeboost alone runs for 72 hours.")}
""")

# ================= MERCH SHIRT PAGES =================
for slug, name, prov, img in MERCH:
    PAGES[f"{slug}-max-win-shirt.html"] = dict(
        title=f"{name} Max Win Shirt — Free Exclusive {prov} Merch | Roobet Code DAILY & ELITE",
        desc=f"Hit a max win on {name} by {prov} while playing on Roobet under code DAILY or ELITE and get this exclusive {name} Max Win shirt shipped to you free. One of 16 designs to collect.",
        kw=f"{name.lower()} max win shirt, {name.lower()} max win, {prov.lower()} max win merch, roobet max win merch, free casino merch",
        schema={"@context": "https://schema.org", "@type": "Product",
                "name": f"{name} Max Win Shirt",
                "description": f"Exclusive {name} ({prov}) Max Win shirt — earned free by hitting a max win on Roobet under code DAILY or ELITE.",
                "image": f"{SITE}/assets/{img}",
                "brand": {"@type": "Brand", "name": "Slotessentials"}},
        body=f"""
<section class="page-hero" style="padding-bottom:20px"><div class="wrap">
  <p class="breadcrumb rv"><a href="/">Home</a> / <a href="/max-win-merch">Max Win Merch</a> / {name}</p>
</div></section>
<section style="padding-top:0"><div class="wrap"><div class="hero-grid">
  <div class="rv"><div class="card" style="padding:18px"><img src="assets/{img}" alt="{name} Max Win Shirt — exclusive {prov} merch" style="border-radius:12px;filter:drop-shadow(0 16px 40px rgba(0,0,0,.5))"></div></div>
  <div>
    <span class="eyebrow rv">👕 {prov}</span>
    <h1 class="rv d1" style="font-size:clamp(2rem,4vw,3rem)">{name}<br><span class="grad">Max Win Shirt</span></h1>
    <p class="lead rv d2" style="margin:18px 0 26px">You can't buy this shirt — you can only win it. Hit a max win on <b style="color:var(--text)">{name}</b> while playing on Roobet under code <b style="color:var(--gold)">DAILY</b> or <b style="color:var(--gold)">ELITE</b> and we ship it to you free, anywhere.</p>
    <div style="display:grid;gap:12px" class="rv d3">
      <div class="mile"><span class="amt">Step 1</span><p style="flex:1;color:var(--muted)">Play {name} on Roobet under code DAILY or ELITE.</p></div>
      <div class="mile"><span class="amt">Step 2</span><p style="flex:1;color:var(--muted)">Hit the max win and screenshot it.</p></div>
      <div class="mile"><span class="amt">Step 3</span><p style="flex:1;color:var(--muted)">Send proof to the <a href="{TELEGRAM}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">VIP team on Telegram</a> — shirt ships free.</p></div>
    </div>
    <div class="hero-cta rv d4" style="margin-top:28px">
      <a class="btn btn-gold btn-lg pulse" href="{DAILY}" rel="nofollow sponsored" target="_blank">Play {name} on Roobet {ARR}</a>
      <a class="btn btn-ghost btn-lg" href="/max-win-merch">All 16 Designs</a>
    </div>
  </div>
</div></div></section>
{cta_banner("One Spin Away From the Rarest Merch", f"Every max win on {name} under DAILY or ELITE earns the shirt. Start hunting.")}
""")

# ================= CONTACT =================
DISCORD_GAMBA = "https://discord.gg/dailygamba"
PAGES["contact.html"] = dict(
    title="Contact Us — VIP Team on Telegram & Discord | Roobet Casino Rewards",
    desc="Questions about our Roobet rewards? Contact our VIP Team on Telegram or join us on Discord — reward claims, VIP transfers, merch shipping and KYC help, handled personally.",
    kw="contact roobet casino rewards, slotessentials vip team, roobet rewards support, telegram vip, discord",
    schema={"@context": "https://schema.org", "@type": "ContactPage", "name": "Contact Roobet Casino Rewards", "url": SITE + "/contact"},
    body=f"""
<section class="page-hero"><div class="wrap">
  <p class="breadcrumb rv"><a href="/">Home</a> / Contact Us</p>
  <span class="eyebrow rv">💬 We Reply Fast</span>
  <h1 class="rv d1">Questions? <span class="grad">One Message Away.</span></h1>
  <p class="lead rv d2">Have any questions about our rewards? Our VIP team handles every message personally — claims, transfers, merch, KYC, anything.</p>
</div></section>

<section style="padding-top:10px"><div class="wrap">
  <div class="cards c2">
    <div class="card rv center" style="padding:44px 32px"><div class="glow"></div><div class="ic" style="margin:0 auto 18px">✈️</div>
      <h3>VIP Team on Telegram</h3>
      <p style="margin:10px 0 24px">The fastest way to reach us — direct line to the VIP team for rewards, claims and VIP transfers.</p>
      <a class="btn btn-gold btn-lg pulse" href="{TELEGRAM}" target="_blank" rel="noopener">Message on Telegram {ARR}</a>
      <p style="margin-top:14px;color:var(--muted);font-size:.85rem">t.me/slotessentialsVIP</p>
    </div>
    <div class="card rv d1 center" style="padding:44px 32px"><div class="glow"></div><div class="ic" style="margin:0 auto 18px">🎮</div>
      <h3>Prefer Discord?</h3>
      <p style="margin:10px 0 24px">Join the community — open a ticket for claims, or just hang out with the players.</p>
      <a class="btn btn-gold btn-lg" href="{DISCORD_GAMBA}" target="_blank" rel="noopener">Join the Discord {ARR}</a>
      <p style="margin-top:14px;color:var(--muted);font-size:.85rem">discord.gg/dailygamba</p>
    </div>
  </div>
  <div class="cards c4" style="margin-top:40px">
    <div class="card rv"><div class="glow"></div><div class="ic">🎁</div><h3>Reward Claims</h3><p>Milestones, giveaways, points — we verify and pay out.</p></div>
    <div class="card rv d1"><div class="glow"></div><div class="ic">💎</div><h3>VIP Transfers</h3><p>Handled personally, start to finish.</p></div>
    <div class="card rv d2"><div class="glow"></div><div class="ic">👕</div><h3>Merch Shipping</h3><p>Max win proof, sizes and delivery.</p></div>
    <div class="card rv d3"><div class="glow"></div><div class="ic">🪪</div><h3>KYC Help</h3><p>Stuck on verification? We deal with it daily.</p></div>
  </div>
  <p class="rv center" style="margin-top:34px;color:var(--muted)">Quick answers might already be in our <a href="/#faq" style="color:var(--gold);font-weight:700">FAQ</a> or the <a href="/blog" style="color:var(--gold);font-weight:700">guides</a>.</p>
</div></section>

{cta_banner("While You Wait for a Reply…","The $100K monthly rewards don't pause. Join with code DAILY and start claiming.")}
""")

# ================= BLOG =================
BLOG_POSTS = [
    ("roobet-vip-program-rank-system", "Roobet VIP Program & Rank System Explained", "How Roobet VIP ranks work, how players level up, what rewards unlock, and how to transfer VIP status from another casino.", "2026-08-18", "6 min read", "💎"),
    ("roobet-rakeback-cashback-bonus-schedule", "Roobet Rakeback, Cashback & Bonus Schedule", "When Roobet rakeback, daily, weekly and monthly bonuses become available — plus Vault timing, expiry rules and rakeboosts.", "2026-08-18", "7 min read", "💰"),
    ("roobet-deposit-bonus-free-spins", "Roobet Deposit Bonus & Free Spins Guide", "How the Roobet free-spins offer works under code DAILY, including cumulative all-time deposit and wager requirements for every tier.", "2026-08-18", "5 min read", "🎁"),
    ("when-can-you-receive-tips-roobet", "When Can You Receive Tips on Roobet?", "A practical guide to receiving Roobet tips, account eligibility, verification, common restrictions and what to check when a tip does not arrive.", "2026-08-18", "4 min read", "💸"),
    ("how-to-deposit-on-roobet", "How to Deposit on Roobet", "Step-by-step guide to making your first Roobet deposit — crypto options, buying with card, confirmation times, and how to unlock your free spins bonus.", "2026-07-21", "5 min read", "💳"),
    ("how-to-kyc-on-roobet", "How to KYC on Roobet", "What Roobet's verification asks for, when you need it, and how to pass it first try — documents, common mistakes, and how long it takes.", "2026-07-21", "4 min read", "🪪"),
    ("roobet-rewards-guide", "Roobet Rewards: The Complete Guide", "Every Roobet reward explained — rakeback & cashback, deposit bonus, daily/weekly/monthly bonus release times, the VIP program and rank system, plus the $100K monthly extras.", "2026-08-07", "7 min read", "💰"),
    ("best-roobet-slots", "Best Roobet Slots to Play", "The best slots on Roobet right now — RTP, max win potential, and which ones earn you free Max Win Merch under code DAILY or ELITE.", "2026-08-07", "6 min read", "🎰"),
    ("how-to-withdraw-on-roobet", "How to Withdraw on Roobet", "Step-by-step Roobet withdrawal guide — KYC, crypto payouts, timing, fees, why a withdrawal might be blocked, and how tips work.", "2026-08-07", "5 min read", "💸"),
]
blog_cards = "".join(f"""<a class="card rv d{i%3+1}" href="{slug}.html"><div class="glow"></div><div class="ic">{ic}</div><p style="font-size:.8rem;color:var(--muted);margin-bottom:8px">{date} · {read}</p><h3>{t}</h3><p>{d}</p><span class="more">Read guide {ARR}</span></a>""" for i, (slug, t, d, date, read, ic) in enumerate(BLOG_POSTS))

PAGES["blog.html"] = dict(
    title="Roobet Guides & Blog — Deposits, Rewards, Free Spins | Roobet Casino Rewards",
    desc="Guides for getting the most out of Roobet: how to deposit, claim rewards, earn free spins and climb the $50K leaderboard. By the team behind the $100,000 monthly rewards.",
    kw="roobet guides, roobet blog, how to deposit on roobet, roobet tutorials, roobet rewards guide",
    body=f"""
<section class="page-hero"><div class="wrap">
  <p class="breadcrumb rv"><a href="/">Home</a> / Blog</p>
  <span class="eyebrow rv">📚 Guides &amp; Blog</span>
  <h1 class="rv d1">Roobet, <span class="grad">Explained</span></h1>
  <p class="lead rv d2">Practical guides from the team behind the $100,000 monthly rewards — deposits, bonuses, leaderboards and everything in between.</p>
</div></section>
<section style="padding-top:10px"><div class="wrap">
  <div class="cards c3">{blog_cards}
  <div class="card rv center" style="display:flex;flex-direction:column;justify-content:center;align-items:center;min-height:240px"><div class="ic">✍️</div><h3>More Guides Coming</h3><p>New guides drop regularly — follow the <a href="{DISCORD}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">Discord</a> to catch them first.</p></div>
  </div>
</div></section>
{cta_banner("While You're Here","The $100K monthly rewards package is live right now — join with code DAILY and start claiming.")}
""")

deposit_faq = [
    ("How long do Roobet deposits take?", "Crypto deposits are credited after network confirmation — usually within a few minutes. Bitcoin can take longer during network congestion; coins like Litecoin and Solana are typically near-instant."),
    ("Do I need to verify my account before depositing?", "You can deposit quickly after signing up, but verification (KYC) is required to withdraw — it's smart to complete it upfront. Our step-by-step guide at HowToKYC.com walks you through the whole process."),
    ("What is the minimum deposit on Roobet?", "Minimums are small and vary by cryptocurrency. The exclusive free spins bonus starts at $500 in all-time deposits under code DAILY or ELITE — cumulative across all your deposits, not one single deposit."),
    ("Can I deposit on Roobet without crypto?", "Yes — Roobet lets you buy crypto directly in the deposit window with a card via third-party on-ramp providers, which then credits your balance."),
]
deposit_faq_html = "".join(f'<details class="rv"><summary>{q}</summary><div class="a">{a}</div></details>' for q, a in deposit_faq)

PAGES["how-to-deposit-on-roobet.html"] = dict(
    title="How to Deposit on Roobet — Step-by-Step Guide (2026) | Roobet Casino Rewards",
    desc="How to deposit on Roobet in 2026: create your account with code DAILY, pick a crypto or buy with card, send your deposit and unlock up to 125 free spins. Full step-by-step guide.",
    kw="how to deposit on roobet, roobet deposit, roobet deposit methods, roobet crypto deposit, roobet minimum deposit, roobet buy crypto with card",
    schema=[
        {"@context": "https://schema.org", "@type": "Article",
         "headline": "How to Deposit on Roobet — Step-by-Step Guide",
         "datePublished": "2026-07-21", "dateModified": "2026-07-21",
         "author": {"@type": "Organization", "name": "Roobet Casino Rewards"},
         "publisher": {"@type": "Organization", "name": "Roobet Casino Rewards", "logo": {"@type": "ImageObject", "url": SITE + "/assets/apple-touch-icon.png"}},
         "image": SITE + "/assets/og-image.png"},
        {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in deposit_faq]},
    ],
    og_type="article",
    body=f"""
<section class="page-hero"><div class="wrap">
  <p class="breadcrumb rv"><a href="/">Home</a> / <a href="/blog">Blog</a> / How to Deposit on Roobet</p>
  <span class="eyebrow rv">💳 Guide · 5 min read</span>
  <h1 class="rv d1">How to Deposit on <span class="grad">Roobet</span></h1>
  <p class="lead rv d2">Everything you need to make your first deposit — from creating your account to unlocking up to 125 free spins on top of it. Updated July 2026.</p>
</div></section>

<section style="padding-top:10px"><div class="wrap" style="max-width:860px">
  <h2 class="rv">Step 1 — Create Your Account</h2>
  <p class="rv" style="color:var(--muted);margin:12px 0 30px">Head to Roobet using code <a href="{DAILY}" rel="nofollow sponsored" target="_blank" style="color:var(--gold);font-weight:700">DAILY</a> and create your account — it takes under a minute. Signing up under our code activates your +10% welcome rakeboost for 24 hours and makes every deposit count toward the <a href="/free-spins" style="color:var(--gold);font-weight:700">exclusive free spins bonus</a>, the <a href="/leaderboard" style="color:var(--gold);font-weight:700">$50K leaderboard</a> and <a href="/wager-milestones" style="color:var(--gold);font-weight:700">wager milestones</a>.</p>

  <h2 class="rv">Step 2 — Verify Your Account (KYC)</h2>
  <p class="rv" style="color:var(--muted);margin:12px 0 30px">You'll need to verify your identity to withdraw, so it's smartest to do it before your first deposit. It's a one-time process — ID plus a few details. Our sister site <a href="{KYC}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">HowToKYC.com</a> has the full step-by-step walkthrough. Stuck? Message our <a href="{TELEGRAM}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">VIP team on Telegram</a>.</p>

  <h2 class="rv">Step 3 — Choose Your Deposit Method</h2>
  <p class="rv" style="color:var(--muted);margin:12px 0 20px">Open your wallet (top of the screen) and hit Deposit. Roobet is crypto-first, and you have two routes:</p>
  <div class="cards c2 rv" style="margin-bottom:30px">
    <div class="card"><div class="glow"></div><div class="ic">🪙</div><h3>Already Have Crypto</h3><p>Pick your coin — Bitcoin, Ethereum, Litecoin, USDT and other major cryptocurrencies are supported. Roobet shows you a deposit address and QR code for that coin.</p></div>
    <div class="card"><div class="glow"></div><div class="ic">💳</div><h3>Buy With Card</h3><p>No crypto? Use the buy-crypto option in the deposit window — a third-party on-ramp lets you purchase with a card, and it credits straight to your balance.</p></div>
  </div>

  <h2 class="rv">Step 4 — Send Your Deposit</h2>
  <div style="display:grid;gap:12px;margin:20px 0 30px">
    <div class="mile rv"><span class="amt">4.1</span><p style="flex:1;color:var(--muted)">Copy the deposit address (or scan the QR) for your chosen coin.</p></div>
    <div class="mile rv d1"><span class="amt">4.2</span><p style="flex:1;color:var(--muted)"><b style="color:var(--text)">Double-check the network.</b> Sending on the wrong network (e.g. USDT on the wrong chain) can lose your funds — match the network Roobet shows exactly.</p></div>
    <div class="mile rv d2"><span class="amt">4.3</span><p style="flex:1;color:var(--muted)">Send from your wallet or exchange. Account for the network fee so the full amount you intend arrives.</p></div>
    <div class="mile rv d3"><span class="amt">4.4</span><p style="flex:1;color:var(--muted)">Wait for confirmation — usually minutes. Your balance updates automatically.</p></div>
  </div>

  <h2 class="rv">Step 5 — Make Your Deposit Work Harder</h2>
  <p class="rv" style="color:var(--muted);margin:12px 0 20px">This is where playing under code DAILY pays off. Your <b style="color:var(--text)">all-time</b> deposit and wager totals unlock the exclusive free spins bonus — it's cumulative, so every deposit moves you up:</p>
  <div class="cards c3 rv" style="margin-bottom:30px">
    <div class="card center"><p class="amount">75 Spins</p><p style="color:var(--muted)">$500 deposited · $5,000 wagered all-time</p></div>
    <div class="card center" style="border-color:rgba(255,199,0,.5)"><p class="amount">100 Spins</p><p style="color:var(--muted)">$1,000 deposited · $10,000 wagered all-time</p></div>
    <div class="card center"><p class="amount">125 Spins</p><p style="color:var(--muted)">$2,000 deposited · $20,000 wagered all-time</p></div>
  </div>
  <p class="rv" style="color:var(--muted);margin-bottom:30px">Every dollar you then wager counts toward the <a href="/leaderboard" style="color:var(--gold);font-weight:700">$50,000 monthly leaderboard</a>, <a href="/wager-milestones" style="color:var(--gold);font-weight:700">$11,350 in wager milestones</a> and <a href="/elite-points" style="color:var(--gold);font-weight:700">ELITE Points</a> — all at the same time.</p>

  <h2 class="rv" style="margin-bottom:20px">Deposit FAQ</h2>
  <div class="faq rv" style="max-width:none">{deposit_faq_html}</div>
</div></section>

{cta_banner("Ready for Your First Deposit?","Join with code DAILY, deposit, and walk away with up to 125 free spins on top.")}
""")

kyc_faq = [
    ("Is KYC required to play on Roobet?", "You can sign up and deposit quickly, but identity verification is required before you can withdraw. Completing it right after signing up means your winnings are never stuck waiting."),
    ("What documents do I need for Roobet KYC?", "Typically a government-issued photo ID (passport, driver's license or national ID) and a selfie. Depending on your account, proof of address or source-of-funds checks can also be requested."),
    ("How long does Roobet verification take?", "Document checks are usually processed quickly — often within minutes to a few hours. Blurry photos or mismatched details are the most common cause of delays."),
    ("My KYC got rejected — what now?", "Re-submit with a clear, glare-free photo of the original document and make sure your account details exactly match your ID. Still stuck? Message our VIP team on Telegram and we'll help you sort it."),
]
kyc_faq_html = "".join(f'<details class="rv"><summary>{q}</summary><div class="a">{a}</div></details>' for q, a in kyc_faq)

PAGES["how-to-kyc-on-roobet.html"] = dict(
    title="How to KYC on Roobet — Verification Guide (2026) | Roobet Casino Rewards",
    desc="How to KYC on Roobet in 2026: which documents you need, how to pass verification first try, how long it takes, and what to do if it's rejected. Full walkthrough at HowToKYC.com.",
    kw="how to kyc on roobet, roobet kyc, roobet verification, roobet identity verification, roobet documents, roobet kyc rejected",
    schema=[
        {"@context": "https://schema.org", "@type": "Article",
         "headline": "How to KYC on Roobet — Verification Guide",
         "datePublished": "2026-07-21", "dateModified": "2026-07-21",
         "author": {"@type": "Organization", "name": "Roobet Casino Rewards"},
         "publisher": {"@type": "Organization", "name": "Roobet Casino Rewards", "logo": {"@type": "ImageObject", "url": SITE + "/assets/apple-touch-icon.png"}},
         "image": SITE + "/assets/og-image.png"},
        {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in kyc_faq]},
    ],
    og_type="article",
    body=f"""
<section class="page-hero"><div class="wrap">
  <p class="breadcrumb rv"><a href="/">Home</a> / <a href="/blog">Blog</a> / How to KYC on Roobet</p>
  <span class="eyebrow rv">🪪 Guide · 4 min read</span>
  <h1 class="rv d1">How to <span class="grad">KYC</span> on Roobet</h1>
  <p class="lead rv d2">Verification is the one step between you and withdrawing your winnings. Here's how to pass it first try — updated July 2026.</p>
</div></section>

<section style="padding-top:10px"><div class="wrap" style="max-width:860px">
  <h2 class="rv">Why Roobet Asks for KYC</h2>
  <p class="rv" style="color:var(--muted);margin:12px 0 30px">KYC ("Know Your Customer") is standard identity verification every licensed casino runs — it protects your account, prevents fraud, and it's required before withdrawals. You can deposit and play beforehand, but do it early: nobody wants a max win sitting in limbo while documents process. New to the process entirely? Our dedicated sister site <a href="{KYC}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">HowToKYC.com</a> covers every step with screenshots.</p>

  <h2 class="rv">What You'll Need</h2>
  <div class="cards c3 rv" style="margin:20px 0 30px">
    <div class="card center"><div class="glow"></div><div class="ic">🪪</div><h3>Photo ID</h3><p>Passport, driver's license or national ID — valid and undamaged.</p></div>
    <div class="card center"><div class="glow"></div><div class="ic">🤳</div><h3>A Selfie</h3><p>Taken live during verification to match you to your ID.</p></div>
    <div class="card center"><div class="glow"></div><div class="ic">🧾</div><h3>Sometimes More</h3><p>Proof of address or source of funds, if requested on your account.</p></div>
  </div>

  <h2 class="rv">The Process, Step by Step</h2>
  <div style="display:grid;gap:12px;margin:20px 0 30px">
    <div class="mile rv"><span class="amt">Step 1</span><p style="flex:1;color:var(--muted)">Sign up (or log in) — join with code <a href="{DAILY}" rel="nofollow sponsored" target="_blank" style="color:var(--gold);font-weight:700">DAILY</a> to stack the rewards while you're at it.</p></div>
    <div class="mile rv d1"><span class="amt">Step 2</span><p style="flex:1;color:var(--muted)">Open your account settings and find the verification section.</p></div>
    <div class="mile rv d2"><span class="amt">Step 3</span><p style="flex:1;color:var(--muted)">Upload your ID and complete the selfie check. Good lighting, no glare, all four corners of the document visible.</p></div>
    <div class="mile rv d3"><span class="amt">Step 4</span><p style="flex:1;color:var(--muted)">Wait for approval — usually fast. Once verified, deposits, play and withdrawals are all frictionless.</p></div>
  </div>

  <h2 class="rv">Pass It First Try</h2>
  <p class="rv" style="color:var(--muted);margin:12px 0 30px">The three mistakes that cause almost every rejection: blurry or cropped document photos, account details that don't exactly match the ID (name spelling, date of birth), and expired documents. Get those right and it's a one-and-done process. If anything goes sideways, message our <a href="{TELEGRAM}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">VIP team on Telegram</a> or open a ticket in the <a href="{DISCORD}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">Discord</a> — we deal with this daily.</p>

  <h2 class="rv" style="margin-bottom:20px">KYC FAQ</h2>
  <div class="faq rv" style="max-width:none">{kyc_faq_html}</div>

  <p class="rv" style="color:var(--muted);margin-top:30px">Verified and ready? Next up: <a href="/how-to-deposit-on-roobet" style="color:var(--gold);font-weight:700">how to make your first deposit</a> — and how to turn it into up to 125 free spins.</p>
</div></section>

{cta_banner("Verified? Time to Get Rewarded.","Join with code DAILY — your wagers count toward the $50K leaderboard from the very first spin.")}
""")

# ================= BLOG: ROOBET REWARDS GUIDE =================
rw_faq = [
    ("Is there a Roobet deposit bonus?", "Yes — under code DAILY or ELITE your all-time deposits and wagers unlock an exclusive free spins deposit bonus: $500 deposited / $5,000 wagered earns 75 free spins, $1,000 / $10,000 earns 100 spins, and $2,000 / $20,000 earns 125 spins at $1.00 each. New sign-ups also get a +10% welcome rakeboost for 24 hours."),
    ("Does Roobet have cashback?", "Yes — Roobet's cashback is called Instant Rakeback: a percentage of every wager comes back to you, claimable every 30 minutes, and it never expires. Part credits instantly and part flows to your Vault, which unlocks 3 claims per day. Rakeboosts of up to +20% multiply it."),
    ("When does Roobet release the monthly bonus?", "The monthly bonus is released on the 1st of every month at midnight UTC. The weekly bonus drops every Saturday at 7 PM EST / midnight UTC, and the daily bonus can be claimed every 24 hours at midnight UTC."),
    ("How does the Roobet VIP program and rank system work?", "Wagering levels up your account, and every rank-up pays a level-up bonus plus a +10% rakeboost for 60 minutes — the higher your level, the bigger your daily, weekly and monthly bonus percentages. Already VIP at another casino? You can transfer your status directly to Roobet under code DAILY or ELITE."),
    ("What extra rewards do DAILY and ELITE players get?", "On top of Roobet's own system: the $50,000 monthly wager leaderboard, up to $11,350 in wager milestones, exclusive free spins, Max Win Merch, ELITE Points redeemable for real prizes, slot challenges and $5,000 in monthly community giveaways — about $100,000 in total monthly rewards."),
]
rw_faq_html = "".join(f'<details class="rv"><summary>{q}</summary><div class="a">{a}</div></details>' for q, a in rw_faq)

PAGES["roobet-rewards-guide.html"] = dict(
    title="Roobet Rewards: The Complete 2026 Guide — Rakeback, Cashback, VIP Program & Bonuses",
    desc="Every Roobet reward explained: rakeback and cashback every 30 minutes, the deposit bonus, daily/weekly/monthly bonus release times, the VIP program and rank system, and $100,000 in extra monthly rewards with code DAILY or ELITE.",
    kw="roobet rewards, roobet deposit bonus, roobet cashback, roobet rakeback, roobet vip program, roobet vip, roobet rank system, when does roobet release monthly bonus",
    schema=[
        {"@context": "https://schema.org", "@type": "Article",
         "headline": "Roobet Rewards: The Complete 2026 Guide",
         "datePublished": "2026-08-07", "dateModified": "2026-08-07",
         "author": {"@type": "Organization", "name": "Roobet Casino Rewards"},
         "publisher": {"@type": "Organization", "name": "Roobet Casino Rewards", "logo": {"@type": "ImageObject", "url": SITE + "/assets/apple-touch-icon.png"}},
         "image": SITE + "/assets/og-image.png"},
        {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in rw_faq]},
    ],
    og_type="article",
    body=f"""
<section class="page-hero"><div class="wrap">
  <p class="breadcrumb rv"><a href="/">Home</a> / <a href="/blog">Blog</a> / Roobet Rewards Guide</p>
  <span class="eyebrow rv">💰 Guide · 7 min read</span>
  <h1 class="rv d1">Roobet Rewards: <span class="grad">The Complete Guide</span></h1>
  <p class="lead rv d2">Rakeback, cashback, deposit bonuses, the VIP program — and the $100,000 monthly package on top. Everything Roobet pays you, in one place. Updated August 2026.</p>
</div></section>

<section style="padding-top:10px"><div class="wrap" style="max-width:860px">
  <h2 class="rv">Rakeback &amp; Cashback — Every 30 Minutes</h2>
  <p class="rv" style="color:var(--muted);margin:12px 0 30px">Roobet's cashback system is <b style="color:var(--text)">Instant Rakeback</b>: a slice of every wager comes back to you, claimable every 30 minutes, and it never expires. Part hits your balance instantly; part fills your Vault (3 claims a day, every 8 hours). Rakeboosts push it further — +10% on signup and rank-ups, +15% on vault calendar claims, and the big one: <b style="color:var(--gold)">+20% for 72 hours</b> when you redeem code <a href="{DAILY}" rel="nofollow sponsored" target="_blank" style="color:var(--gold);font-weight:700">DAILY</a> or <a href="{ELITE}" rel="nofollow sponsored" target="_blank" style="color:var(--gold);font-weight:700">ELITE</a>. Full mechanics on our <a href="/roobet-rewards" style="color:var(--gold);font-weight:700">Roobet rewards system page</a>.</p>

  <h2 class="rv">The Roobet Deposit Bonus</h2>
  <p class="rv" style="color:var(--muted);margin:12px 0 20px">Roobet doesn't do a classic "match bonus" — under our codes you get something better: an <a href="/free-spins" style="color:var(--gold);font-weight:700">exclusive free spins deposit bonus</a> based on your all-time totals, so every deposit moves you up a tier:</p>
  <div class="cards c3 rv" style="margin-bottom:30px">
    <div class="card center"><p class="amount">75 Spins</p><p style="color:var(--muted)">$500 deposited · $5,000 wagered all-time</p></div>
    <div class="card center" style="border-color:rgba(255,199,0,.5)"><p class="amount">100 Spins</p><p style="color:var(--muted)">$1,000 · $10,000 all-time</p></div>
    <div class="card center"><p class="amount">125 Spins</p><p style="color:var(--muted)">$2,000 · $20,000 all-time</p></div>
  </div>

  <h2 class="rv">Daily, Weekly &amp; Monthly Bonuses — Release Times</h2>
  <div style="display:grid;gap:12px;margin:20px 0 30px">
    <div class="mile rv"><span class="amt">Daily</span><p style="flex:1;color:var(--muted)">Claimable every 24 hours at <b style="color:var(--text)">midnight UTC</b> — accumulates up to 72 hours if you miss a day.</p></div>
    <div class="mile rv d1"><span class="amt">Weekly</span><p style="flex:1;color:var(--muted)">Released every <b style="color:var(--text)">Saturday at 7 PM EST / midnight UTC</b>, with a 14-day vault calendar.</p></div>
    <div class="mile rv d2"><span class="amt">Monthly</span><p style="flex:1;color:var(--muted)">Released on the <b style="color:var(--text)">1st of every month at midnight UTC</b>. Percentages scale with your level. Next drop: <b style="color:var(--gold);font-variant-numeric:tabular-nums" data-deadline="monthly">—</b></p></div>
  </div>

  <h2 class="rv">The VIP Program &amp; Rank System</h2>
  <p class="rv" style="color:var(--muted);margin:12px 0 30px">Wagering levels up your account. Every rank-up pays a <b style="color:var(--text)">level-up bonus</b> and triggers a +10% rakeboost for 60 minutes — and your level sets the instant percentage of every daily, weekly and monthly bonus. The shortcut: if you're already VIP somewhere else, <a href="/vip-transfer" style="color:var(--gold);font-weight:700">transfer your VIP status to Roobet</a> and start at the top instead of grinding from zero. Our VIP team handles it personally.</p>

  <h2 class="rv">The Extra $100,000 — DAILY &amp; ELITE Only</h2>
  <p class="rv" style="color:var(--muted);margin:12px 0 20px">Everything above is Roobet's own system. Playing under our codes stacks a second layer on top:</p>
  <div class="cards c2 rv" style="margin-bottom:30px">
    <a class="card" href="/leaderboard"><div class="glow"></div><div class="ic">🏆</div><h3>$50K Wager Leaderboard</h3><p>Monthly race — $12,500 top prize + 15,000 ELITE Points for the podium.</p><span class="more">Explore {ARR}</span></a>
    <a class="card" href="/wager-milestones"><div class="glow"></div><div class="ic">🎯</div><h3>$11,350 Wager Milestones</h3><p>Guaranteed payouts at every tier, resets monthly.</p><span class="more">Explore {ARR}</span></a>
    <a class="card" href="/elite-points"><div class="glow"></div><div class="ic">⭐</div><h3>ELITE Points Shop</h3><p>Earn daily, redeem free balance and bonus buys.</p><span class="more">Explore {ARR}</span></a>
    <a class="card" href="/max-win-merch"><div class="glow"></div><div class="ic">👕</div><h3>Max Win Merch</h3><p>Free exclusive shirts for every max win you hit.</p><span class="more">Explore {ARR}</span></a>
  </div>

  <h2 class="rv" style="margin-bottom:20px">Roobet Rewards FAQ</h2>
  <div class="faq rv" style="max-width:none">{rw_faq_html}</div>
</div></section>

{cta_banner("Claim the Whole Stack","One code unlocks both layers — Roobet's rewards plus our $100K monthly package. Join with DAILY.")}
""")

# ================= BLOG: BEST ROOBET SLOTS =================
slots_data = [
    ("Gates of Olympus", "Pragmatic Play", "96.5% RTP · 5,000x max win", "Zeus, tumbling wins and random multipliers — the eternal crowd favourite and a leaderboard grinder's staple.", "gates-of-olympus-max-win-shirt.html"),
    ("Sweet Bonanza", "Pragmatic Play", "96.5% RTP · 21,100x max win", "Candy-cluster chaos with 100x bomb multipliers in free spins. Huge win ceiling for a sweet theme.", "sweet-bonanza-max-win-shirt.html"),
    ("Sugar Rush", "Pragmatic Play", "96.5% RTP · 25,000x max win", "Position-based multiplier spots that snowball — one of the biggest max wins in the Pragmatic lineup.", "sugar-rush-max-win-shirt.html"),
    ("Big Bass", "Pragmatic Play", "Fisherman free spins & money collects", "The most famous bonus round in slots. Retrigger the fisherman and the collects stack fast.", "big-bass-max-win-shirt.html"),
    ("Le Bandit", "Hacksaw Gaming", "96.34% RTP · 10,000x max win", "Cluster pays, golden squares and rainbow symbols — Hacksaw at its most explosive.", "le-bandit-max-win-shirt.html"),
    ("Wanted Dead or a Wild", "Hacksaw Gaming", "96.38% RTP · 12,500x max win", "The wild-west volatility monster. Duel and Dead Man's Hand bonuses produce legendary clips.", None),
    ("Mental", "Nolimit City", "96.08% RTP · 66,666x max win", "Nolimit's darkest and most extreme math — for players who want the biggest possible ceiling.", "mental-max-win-shirt.html"),
    ("Six Six Six", "Hacksaw Gaming", "Devilish multipliers & bonus modes", "Hacksaw's occult grid slot — sticky multiplier respins that can turn a bonus into a monster.", "six-six-six-max-win-shirt.html"),
]
slots_cards = "".join(f"""<div class="card rv d{i%2+1}"><div class="glow"></div><span class="tag">{prov}</span><h3>{name}</h3><p style="color:var(--gold);font-weight:700;font-size:.9rem;margin-bottom:8px">{stats}</p><p>{desc}</p>{f'<a class="more" href="{merch}">Max Win Merch available {ARR}</a>' if merch else ''}</div>""" for i, (name, prov, stats, desc, merch) in enumerate(slots_data))

sl_faq = [
    ("What are the best slots on Roobet?", "Player favourites on Roobet include Gates of Olympus, Sweet Bonanza and Sugar Rush from Pragmatic Play, Le Bandit and Wanted Dead or a Wild from Hacksaw Gaming, and Mental from Nolimit City — a mix of high max win potential and bonus-round quality. The best slot for you depends on how much volatility you want."),
    ("Do slots count fully toward the leaderboard and milestones?", "Yes — slots and similar gameplay at 97% RTP or lower contribute at the full 100% rate to weighted wagering, which drives the $50,000 leaderboard and wager milestones. Games above 97% RTP contribute 50%, and 98%+ (mostly house games) contribute 10%."),
    ("Which Roobet slots earn Max Win Merch?", "Hitting the max win on featured Pragmatic Play, Hacksaw Gaming or Nolimit City slots under code DAILY or ELITE earns you an exclusive free shirt for that game — 16 designs exist, including Gates of Olympus, Sweet Bonanza, Sugar Rush, Big Bass, Le Bandit, Six Six Six and Mental."),
    ("Are slot RTPs the same on Roobet as other casinos?", "Providers publish a default RTP for each game, and casinos may license certain RTP configurations. The figures listed here are the providers' standard published values — always check the in-game info panel for the exact RTP of the version you're playing."),
]
sl_faq_html = "".join(f'<details class="rv"><summary>{q}</summary><div class="a">{a}</div></details>' for q, a in sl_faq)

PAGES["best-roobet-slots.html"] = dict(
    title="Best Roobet Slots in 2026 — Top Picks by Max Win, RTP & Bonus Rounds",
    desc="The best slots on Roobet in 2026: Gates of Olympus, Sweet Bonanza, Sugar Rush, Le Bandit, Mental and more — RTP, max win potential, and which slots earn free Max Win Merch under code DAILY or ELITE.",
    kw="best roobet slots, roobet best slots, roobet slots, best slots on roobet, roobet slot picks, roobet max win slots",
    schema=[
        {"@context": "https://schema.org", "@type": "Article",
         "headline": "Best Roobet Slots in 2026 — Top Picks",
         "datePublished": "2026-08-07", "dateModified": "2026-08-07",
         "author": {"@type": "Organization", "name": "Roobet Casino Rewards"},
         "publisher": {"@type": "Organization", "name": "Roobet Casino Rewards", "logo": {"@type": "ImageObject", "url": SITE + "/assets/apple-touch-icon.png"}},
         "image": SITE + "/assets/og-image.png"},
        {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in sl_faq]},
    ],
    og_type="article",
    body=f"""
<section class="page-hero"><div class="wrap">
  <p class="breadcrumb rv"><a href="/">Home</a> / <a href="/blog">Blog</a> / Best Roobet Slots</p>
  <span class="eyebrow rv">🎰 Guide · 6 min read</span>
  <h1 class="rv d1">Best <span class="grad">Roobet Slots</span> to Play in 2026</h1>
  <p class="lead rv d2">The slots our community actually grinds — ranked by max win potential, bonus quality and clip-ability. Every one counts 100% toward the <a href="/leaderboard" style="color:var(--gold);font-weight:700">$50K leaderboard</a>. Updated August 2026.</p>
</div></section>

<section style="padding-top:10px"><div class="wrap" style="max-width:1000px">
  <div class="cards c2">{slots_cards}</div>

  <div class="cta-banner rv" style="margin-top:40px">
    <h2>Why Slots Are the Smart Grind</h2>
    <p class="lead">Weighted wagering means slots at 97% RTP or lower count at the <b style="color:var(--gold)">full 100% rate</b> toward the leaderboard and milestones — house games above 98% RTP only count 10%. Same bankroll, ten times the progress.</p>
    <div class="hero-cta" style="justify-content:center">
      <a class="btn btn-gold btn-lg pulse" href="{DAILY}" rel="nofollow sponsored" target="_blank">Play on Roobet with DAILY {ARR}</a>
      <a class="btn btn-ghost btn-lg" href="/wager-milestones">See Milestone Payouts</a>
    </div>
  </div>

  <h2 class="rv" style="margin-top:60px;margin-bottom:20px">Roobet Slots FAQ</h2>
  <div class="faq rv" style="max-width:none">{sl_faq_html}</div>

  <p class="rv" style="color:var(--muted);margin-top:30px">Deep slot stats, hot &amp; cold data and record win tracking live on our sister site <a href="https://slotessentials.com/slot-database" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">Slotessentials Slot Database</a>.</p>
</div></section>

{cta_banner("Hit a Max Win, Wear the Proof","Every max win on a featured slot under DAILY or ELITE earns exclusive free merch. Start with the list above.")}
""")

# ================= BLOG: HOW TO WITHDRAW =================
wd_faq = [
    ("How long do Roobet withdrawals take?", "Withdrawals are typically processed quickly — often within minutes once approved. Total time depends on the blockchain: Litecoin and Solana are near-instant, Bitcoin can take longer during network congestion."),
    ("Why can't I withdraw from Roobet?", "The most common reasons: your account isn't verified yet (KYC is required for withdrawals), active bonus funds carry wagering conditions, or the withdrawal amount is below the minimum for that coin. If none of those apply, message our VIP team on Telegram and we'll help you sort it."),
    ("Do I need KYC to withdraw on Roobet?", "Yes — identity verification is required before your first withdrawal. Complete it early so your winnings are never stuck waiting. Our guide at HowToKYC.com walks through every step."),
    ("When can you receive tips on Roobet?", "Roobet's tipping feature lets players send balance to each other, but it unlocks with account standing — typically a verified (KYC'd) account with real wagering history, as an anti-abuse measure. If tipping isn't available on your account yet, keep playing and verify, or ask Roobet support for your account's specific requirements."),
    ("Are there withdrawal fees on Roobet?", "You pay the blockchain network fee for the coin you withdraw. Choosing a faster, cheaper chain like Litecoin usually costs a fraction of a Bitcoin transaction."),
]
wd_faq_html = "".join(f'<details class="rv"><summary>{q}</summary><div class="a">{a}</div></details>' for q, a in wd_faq)

PAGES["how-to-withdraw-on-roobet.html"] = dict(
    title="How to Withdraw on Roobet — Step-by-Step Guide (2026) | Roobet Casino Rewards",
    desc="How to withdraw on Roobet in 2026: complete KYC, pick your crypto, avoid network mistakes and get paid fast. Plus withdrawal times, fees, common blockers and how Roobet tips work.",
    kw="how to withdraw on roobet, roobet withdrawal, roobet withdraw, roobet withdrawal time, roobet tips, when can you receive tips roobet",
    schema=[
        {"@context": "https://schema.org", "@type": "Article",
         "headline": "How to Withdraw on Roobet — Step-by-Step Guide",
         "datePublished": "2026-08-07", "dateModified": "2026-08-07",
         "author": {"@type": "Organization", "name": "Roobet Casino Rewards"},
         "publisher": {"@type": "Organization", "name": "Roobet Casino Rewards", "logo": {"@type": "ImageObject", "url": SITE + "/assets/apple-touch-icon.png"}},
         "image": SITE + "/assets/og-image.png"},
        {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in wd_faq]},
    ],
    og_type="article",
    body=f"""
<section class="page-hero"><div class="wrap">
  <p class="breadcrumb rv"><a href="/">Home</a> / <a href="/blog">Blog</a> / How to Withdraw on Roobet</p>
  <span class="eyebrow rv">💸 Guide · 5 min read</span>
  <h1 class="rv d1">How to <span class="grad">Withdraw</span> on Roobet</h1>
  <p class="lead rv d2">You hit the win — now get it out clean. The full withdrawal process, what blocks payouts, and how to avoid the one mistake that loses funds. Updated August 2026.</p>
</div></section>

<section style="padding-top:10px"><div class="wrap" style="max-width:860px">
  <h2 class="rv">Before Anything: Verify Your Account</h2>
  <p class="rv" style="color:var(--muted);margin:12px 0 30px">KYC is required before your first withdrawal — no way around it, and it's why we tell everyone to verify on day one. If you haven't yet, our <a href="/how-to-kyc-on-roobet" style="color:var(--gold);font-weight:700">KYC guide</a> and <a href="{KYC}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">HowToKYC.com</a> get you through it in minutes.</p>

  <h2 class="rv">Withdrawing, Step by Step</h2>
  <div style="display:grid;gap:12px;margin:20px 0 30px">
    <div class="mile rv"><span class="amt">Step 1</span><p style="flex:1;color:var(--muted)">Open your wallet on Roobet and hit <b style="color:var(--text)">Withdraw</b>.</p></div>
    <div class="mile rv d1"><span class="amt">Step 2</span><p style="flex:1;color:var(--muted)">Pick your coin. Tip: Litecoin or Solana are fast with tiny network fees; Bitcoin is slower and pricier.</p></div>
    <div class="mile rv d2"><span class="amt">Step 3</span><p style="flex:1;color:var(--muted)"><b style="color:var(--text)">Paste your wallet address and triple-check the network.</b> Sending to the wrong chain is the one mistake that can permanently lose funds.</p></div>
    <div class="mile rv d3"><span class="amt">Step 4</span><p style="flex:1;color:var(--muted)">Confirm the amount (minding the coin's minimum), submit, and watch it land — usually within minutes.</p></div>
  </div>

  <h2 class="rv">If Your Withdrawal Won't Go Through</h2>
  <div class="cards c3 rv" style="margin:20px 0 30px">
    <div class="card"><div class="glow"></div><div class="ic">🪪</div><h3>Not Verified</h3><p>The #1 blocker. Complete KYC and the button unlocks.</p></div>
    <div class="card"><div class="glow"></div><div class="ic">🎁</div><h3>Bonus Conditions</h3><p>Active bonus funds can carry wagering conditions before cash-out.</p></div>
    <div class="card"><div class="glow"></div><div class="ic">📉</div><h3>Below Minimum</h3><p>Each coin has a small minimum — switch coins or top the amount up.</p></div>
  </div>
  <p class="rv" style="color:var(--muted);margin-bottom:30px">Still stuck? Message our <a href="{TELEGRAM}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">VIP team on Telegram</a> or open a ticket in the <a href="{DISCORD}" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">Discord</a> — withdrawal issues are our daily bread.</p>

  <h2 class="rv" style="margin-bottom:20px">Withdrawals &amp; Tips FAQ</h2>
  <div class="faq rv" style="max-width:none">{wd_faq_html}</div>

  <p class="rv" style="color:var(--muted);margin-top:30px">Full circle: <a href="/how-to-deposit-on-roobet" style="color:var(--gold);font-weight:700">how to deposit</a> → <a href="/how-to-kyc-on-roobet" style="color:var(--gold);font-weight:700">how to KYC</a> → withdraw. And everything you wager in between counts toward the <a href="/roobet-rewards-guide" style="color:var(--gold);font-weight:700">full rewards stack</a>.</p>
</div></section>

{cta_banner("Win It, Then Withdraw It Clean","Join with code DAILY — and when the big one hits, you'll know exactly how to cash it out.")}
""")

# ================= BLOG: VIP PROGRAM & RANK SYSTEM =================
vip_faq = [
    ("How does the Roobet VIP program work?", "Players progress through account ranks by wagering. Higher ranks can unlock larger level-up rewards and access to more valuable ongoing rewards. Exact benefits can depend on account activity and current terms."),
    ("How do I increase my Roobet rank?", "Wager eligible games on your account. Weighted wagering can apply, so some game categories contribute less than slots and similar gameplay."),
    ("Can I transfer VIP status to Roobet?", "Eligible players can request a VIP transfer from another casino. Use the SlotEssentials VIP form, then contact the VIP team on Telegram or open a Discord ticket for help."),
    ("Does ranking up activate a rakeboost?", "Under the current rewards structure, ranking up activates a 10% rakeboost for 60 minutes. Rakeboosts run in parallel rather than stacking; the highest active percentage applies."),
]
PAGES["roobet-vip-program-rank-system.html"] = dict(
    title="Roobet VIP Program & Rank System Explained (2026)",
    desc="Roobet VIP program and rank system explained: how to level up, rank rewards, rakeboosts, VIP transfers and how to access the complete rewards package.",
    kw="roobet vip program, roobet vip, roobet rank system, roobet vip transfer, roobet levels",
    schema=[
        {"@context":"https://schema.org","@type":"Article","headline":"Roobet VIP Program & Rank System Explained","datePublished":"2026-08-18","dateModified":"2026-08-18","author":{"@type":"Organization","name":"Roobet Casino Rewards"},"publisher":{"@type":"Organization","name":"Roobet Casino Rewards"}},
        {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in vip_faq]},
    ],
    body=f"""
<section class="page-hero"><div class="wrap">
  <p class="breadcrumb rv"><a href="/">Home</a> / <a href="/blog">Blog</a> / Roobet VIP Program</p>
  <span class="eyebrow rv">💎 VIP Guide · Updated August 2026</span>
  <h1 class="rv d1">Roobet VIP Program &amp; <span class="grad">Rank System</span></h1>
  <p class="lead rv d2">Roobet rewards active players as they progress through account ranks. Here is how ranking, level-up bonuses, rakeboosts and VIP transfers fit together.</p>
</div></section>
<section style="padding-top:10px"><div class="wrap" style="max-width:900px">
  <h2 class="rv">How Roobet VIP Ranks Work</h2>
  <p class="rv" style="color:var(--muted);margin:12px 0 28px">Your account rank progresses through eligible wagering. The higher your level, the larger your potential level-up bonus. Because wagering can be weighted by game type, the amount displayed as progress may differ from your raw bet total.</p>
  <div class="cards c3 rv">
    <div class="card"><div class="ic">📈</div><h3>Wager &amp; Progress</h3><p>Eligible wagering moves your rank forward. Slots and similar games generally provide the strongest contribution.</p></div>
    <div class="card"><div class="ic">🎉</div><h3>Level-Up Rewards</h3><p>Advancing to a new rank can trigger a level-up bonus and a temporary rakeboost.</p></div>
    <div class="card"><div class="ic">💰</div><h3>Ongoing Rewards</h3><p>Rakeback, daily, weekly, monthly and Vault rewards continue alongside rank progression.</p></div>
  </div>
  <h2 class="rv" style="margin-top:46px">Rank-Up Rakeboost</h2>
  <p class="rv" style="color:var(--muted);margin:12px 0 28px">Ranking up currently activates a <b style="color:var(--text)">10% boost for 60 minutes</b> on Instant Rakeback. Rakeboosts do not stack or queue; if several are active, only the highest percentage applies.</p>
  <h2 class="rv">Transfer Your Existing VIP Status</h2>
  <p class="rv" style="color:var(--muted);margin:12px 0 22px">Already VIP somewhere else? You may be able to transfer that status directly to Roobet and unlock access to our full rewards ecosystem: the $50K leaderboard, wager milestones, free spins, ELITE Points, slot challenges, giveaways, Max Win Merch and VIP support.</p>
  <div class="hero-cta rv"><a class="btn btn-gold btn-lg" href="{SLOTS}" target="_blank" rel="noopener">Start VIP Transfer {ARR}</a><a class="btn btn-ghost btn-lg" href="{TELEGRAM}" target="_blank" rel="noopener">Message VIP Team</a></div>
  <h2 class="rv" style="margin-top:46px">Roobet VIP FAQ</h2>
  <div class="faq rv" style="max-width:none">{"".join(f'<div class="faq-item"><button>{q}<span>+</span></button><div class="answer"><p>{a}</p></div></div>' for q,a in vip_faq)}</div>
  <p class="rv" style="color:var(--muted);margin-top:30px">Next: read the <a href="/roobet-rakeback-cashback-bonus-schedule" style="color:var(--gold);font-weight:700">Roobet bonus schedule</a> or explore our <a href="/roobet-rewards-guide" style="color:var(--gold);font-weight:700">complete rewards guide</a>.</p>
</div></section>
{cta_banner("Bring Your VIP Status With You","Join with code DAILY, submit the VIP form and let our team handle the transfer.")}
""")

# ================= BLOG: RAKEBACK / CASHBACK / BONUS SCHEDULE =================
bonus_faq = [
    ("When does Roobet release the monthly bonus?", "The monthly bonus is currently released on the first day of each month at 00:00 UTC. A portion may be credited immediately and a portion placed into the Vault calendar, subject to level and current terms."),
    ("When does Roobet release the weekly bonus?", "The weekly bonus is currently released every Saturday at 00:00 UTC, equivalent to 7:00 PM EST during standard time."),
    ("How often can I claim Roobet rakeback?", "Instant Rakeback can currently be claimed every 30 minutes. Part may go directly to your balance and part to the Vault."),
    ("Is Roobet cashback the same as rakeback?", "Players often use cashback as a general term for money returned from wagering. Roobet's named recurring feature is Instant Rakeback, alongside daily, weekly, monthly and Vault rewards."),
]
PAGES["roobet-rakeback-cashback-bonus-schedule.html"] = dict(
    title="Roobet Rakeback, Cashback & Bonus Schedule (2026)",
    desc="Roobet rakeback and cashback guide with daily, weekly and monthly bonus release times, Vault claims, expiry rules and every rakeboost percentage.",
    kw="roobet cashback, roobet rakeback, when does roobet release monthly bonus, roobet monthly bonus, roobet weekly bonus",
    schema=[
        {"@context":"https://schema.org","@type":"Article","headline":"Roobet Rakeback, Cashback & Bonus Schedule","datePublished":"2026-08-18","dateModified":"2026-08-18","author":{"@type":"Organization","name":"Roobet Casino Rewards"},"publisher":{"@type":"Organization","name":"Roobet Casino Rewards"}},
        {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in bonus_faq]},
    ],
    body=f"""
<section class="page-hero"><div class="wrap">
  <p class="breadcrumb rv"><a href="/">Home</a> / <a href="/blog">Blog</a> / Rakeback &amp; Bonus Schedule</p>
  <span class="eyebrow rv">💰 Reward Calendar · Updated August 2026</span>
  <h1 class="rv d1">Roobet Rakeback, Cashback &amp; <span class="grad">Bonus Schedule</span></h1>
  <p class="lead rv d2">What players call Roobet cashback is a stack of recurring rewards. Here is when each one becomes claimable and how long you have before it expires.</p>
</div></section>
<section style="padding-top:10px"><div class="wrap" style="max-width:920px">
  <div class="table-wrap rv"><table class="tbl"><thead><tr><th>Reward</th><th>Release / claim time</th><th>Important detail</th></tr></thead><tbody>
    <tr><td><b>Instant Rakeback</b></td><td>Every 30 minutes</td><td>Never expires before being claimed; a portion may enter the Vault.</td></tr>
    <tr><td><b>Daily Bonus</b></td><td>Every 24 hours at 00:00 UTC</td><td>Can accumulate for up to 72 hours.</td></tr>
    <tr><td><b>Weekly Bonus</b></td><td>Saturday at 00:00 UTC</td><td>Vault-calendar portion can be claimable over 14 days.</td></tr>
    <tr><td><b>Monthly Bonus</b></td><td>1st of each month at 00:00 UTC</td><td>Vault-calendar portion can be claimable over 14 days.</td></tr>
    <tr><td><b>The Vault</b></td><td>Up to 3 claims daily, every 8 hours</td><td>Unlocked collections expire after 24 hours and cannot be taken all at once.</td></tr>
  </tbody></table></div>
  <h2 class="rv" style="margin-top:48px">Rakeboost Percentages</h2>
  <div class="cards c3 rv" style="margin-top:20px">
    <div class="card"><h3>+10%</h3><p>Welcome boost for 24 hours; rank-up, daily, weekly and monthly claims for 60 minutes.</p></div>
    <div class="card"><h3>+15%</h3><p>Vault Calendar claim boost for 60 minutes.</p></div>
    <div class="card"><h3>+20%</h3><p>Affiliate-code redemption boost for 72 hours.</p></div>
  </div>
  <p class="rv" style="color:var(--muted);margin:24px 0 40px">Boosts run in parallel but do not stack: the highest active boost is the one that applies. Reward availability and calculations remain subject to Roobet's current account terms.</p>
  <h2 class="rv">Bonus Schedule FAQ</h2>
  <div class="faq rv" style="max-width:none">{"".join(f'<div class="faq-item"><button>{q}<span>+</span></button><div class="answer"><p>{a}</p></div></div>' for q,a in bonus_faq)}</div>
  <p class="rv" style="color:var(--muted);margin-top:30px">See the full <a href="/roobet-rewards" style="color:var(--gold);font-weight:700">Roobet rewards breakdown</a>, then add our <a href="/wager-milestones" style="color:var(--gold);font-weight:700">$11,350 wager milestones</a> and <a href="/leaderboard" style="color:var(--gold);font-weight:700">$50K leaderboard</a>.</p>
</div></section>
{cta_banner("Something to Claim Every 30 Minutes","Join with code DAILY and activate the full rewards stack.")}
""")

# ================= BLOG: DEPOSIT BONUS / FREE SPINS =================
deposit_bonus_faq = [
    ("Does Roobet have a deposit bonus?", "Our code DAILY offer rewards eligible players with free spins after cumulative all-time deposit and wager requirements are reached. It is not limited to one single deposit."),
    ("How many free spins can I receive?", "The current tiers provide 75 free spins after $500 deposited and $5,000 wagered, 100 free spins after $1,000 deposited and $10,000 wagered, or 125 free spins after $2,000 deposited and $20,000 wagered."),
    ("Do deposits have to be made all at once?", "No. The published offer is based on cumulative all-time deposits and wagering under the eligible affiliate code."),
    ("Is this a no-deposit bonus?", "No. The free-spins tiers require both cumulative deposits and wagering. Always review the current offer terms before participating."),
]
PAGES["roobet-deposit-bonus-free-spins.html"] = dict(
    title="Roobet Deposit Bonus & Free Spins — Code DAILY (2026)",
    desc="Roobet deposit bonus and free spins guide: cumulative all-time deposit and wager tiers for 75, 100 or 125 spins when joining with code DAILY.",
    kw="roobet deposit bonus, roobet welcome bonus, roobet free spins, free spins roobet, roobet bonus code daily",
    schema=[
        {"@context":"https://schema.org","@type":"Article","headline":"Roobet Deposit Bonus & Free Spins Guide","datePublished":"2026-08-18","dateModified":"2026-08-18","author":{"@type":"Organization","name":"Roobet Casino Rewards"},"publisher":{"@type":"Organization","name":"Roobet Casino Rewards"}},
        {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in deposit_bonus_faq]},
    ],
    body=f"""
<section class="page-hero"><div class="wrap">
  <p class="breadcrumb rv"><a href="/">Home</a> / <a href="/blog">Blog</a> / Deposit Bonus</p>
  <span class="eyebrow rv">🎁 Code DAILY Offer · Updated August 2026</span>
  <h1 class="rv d1">Roobet Deposit Bonus &amp; <span class="grad">Free Spins</span></h1>
  <p class="lead rv d2">The key detail: these thresholds are cumulative all-time totals—not one giant deposit. Every eligible deposit and wager moves you toward the next tier.</p>
</div></section>
<section style="padding-top:10px"><div class="wrap" style="max-width:940px">
  <div class="cards c3 rv">
    <div class="card center"><span class="eyebrow">Tier 1</span><h2>75 Spins</h2><p><b>$500</b> cumulative deposits<br><b>$5,000</b> cumulative wager<br>$0.60 per spin</p></div>
    <div class="card center"><span class="eyebrow">Tier 2</span><h2>100 Spins</h2><p><b>$1,000</b> cumulative deposits<br><b>$10,000</b> cumulative wager<br>$0.80 per spin</p></div>
    <div class="card center"><span class="eyebrow">Tier 3</span><h2>125 Spins</h2><p><b>$2,000</b> cumulative deposits<br><b>$20,000</b> cumulative wager<br>$1.00 per spin</p></div>
  </div>
  <h2 class="rv" style="margin-top:48px">How to Qualify</h2>
  <div style="display:grid;gap:12px;margin:20px 0 38px">
    <div class="mile rv"><span class="amt">1</span><p style="flex:1;color:var(--muted)">Create your Roobet account using code <a href="{DAILY}" target="_blank" rel="nofollow sponsored" style="color:var(--gold);font-weight:700">DAILY</a>.</p></div>
    <div class="mile rv d1"><span class="amt">2</span><p style="flex:1;color:var(--muted)">Complete KYC and make eligible deposits over time.</p></div>
    <div class="mile rv d2"><span class="amt">3</span><p style="flex:1;color:var(--muted)">Build cumulative weighted wagering until you reach a tier.</p></div>
    <div class="mile rv d3"><span class="amt">4</span><p style="flex:1;color:var(--muted)">Follow the claim process on SlotEssentials or contact the VIP team if you need help.</p></div>
  </div>
  <div class="hero-cta rv"><a class="btn btn-gold btn-lg" href="{SLOTS}" target="_blank" rel="noopener">View Offer &amp; Claim {ARR}</a><a class="btn btn-ghost btn-lg" href="/how-to-deposit-on-roobet">Deposit Guide</a></div>
  <h2 class="rv" style="margin-top:48px">Deposit Bonus FAQ</h2>
  <div class="faq rv" style="max-width:none">{"".join(f'<div class="faq-item"><button>{q}<span>+</span></button><div class="answer"><p>{a}</p></div></div>' for q,a in deposit_bonus_faq)}</div>
</div></section>
{cta_banner("Start Building Toward Your Free Spins","Join Roobet with code DAILY. Your qualifying totals build over time.")}
""")

# ================= BLOG: RECEIVING TIPS =================
tips_faq = [
    ("When can you receive tips on Roobet?", "There is no single public threshold that guarantees tip eligibility for every account. Availability can depend on account standing, verification, feature access and Roobet's current rules. Check whether the feature appears on your account or ask official support."),
    ("Do I need KYC to receive a Roobet tip?", "Verification may be required for account and wallet features. Completing KYC early reduces the chance that a payment, tip or withdrawal is delayed."),
    ("Why did my Roobet tip not arrive?", "Confirm the sender used the correct username, check account notifications and wallet history, and verify that both accounts are eligible. If it remains missing, contact official Roobet support."),
    ("Can the VIP team send or recover Roobet tips?", "Our VIP team can help you understand reward claims, but it cannot access Roobet accounts or override platform restrictions. Account-specific tip issues should be handled by official Roobet support."),
]
PAGES["when-can-you-receive-tips-roobet.html"] = dict(
    title="When Can You Receive Tips on Roobet? Eligibility Guide (2026)",
    desc="When can you receive tips on Roobet? Learn about account eligibility, verification, common restrictions, missing tips and the safest steps to troubleshoot.",
    kw="when can you receive tips roobet, roobet tips, receive tips on roobet, roobet tip eligibility",
    schema=[
        {"@context":"https://schema.org","@type":"Article","headline":"When Can You Receive Tips on Roobet?","datePublished":"2026-08-18","dateModified":"2026-08-18","author":{"@type":"Organization","name":"Roobet Casino Rewards"},"publisher":{"@type":"Organization","name":"Roobet Casino Rewards"}},
        {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in tips_faq]},
    ],
    body=f"""
<section class="page-hero"><div class="wrap">
  <p class="breadcrumb rv"><a href="/">Home</a> / <a href="/blog">Blog</a> / Roobet Tips</p>
  <span class="eyebrow rv">💸 Account Guide · Updated August 2026</span>
  <h1 class="rv d1">When Can You Receive <span class="grad">Tips on Roobet?</span></h1>
  <p class="lead rv d2">Tip access is account-specific. There is no responsible way to promise one universal wager or account-age threshold, but these checks cover the most common eligibility issues.</p>
</div></section>
<section style="padding-top:10px"><div class="wrap" style="max-width:880px">
  <h2 class="rv">Tip Eligibility Checklist</h2>
  <div class="cards c3 rv" style="margin-top:20px">
    <div class="card"><div class="ic">🪪</div><h3>Account Standing</h3><p>Keep your account verified where required and free of unresolved restrictions.</p></div>
    <div class="card"><div class="ic">👤</div><h3>Correct Username</h3><p>The sender must use the exact account username. A typo can send funds to the wrong user.</p></div>
    <div class="card"><div class="ic">🔔</div><h3>Wallet &amp; Notices</h3><p>Check wallet history and notifications before assuming the transfer failed.</p></div>
  </div>
  <h2 class="rv" style="margin-top:48px">What to Do if a Tip Is Missing</h2>
  <ol class="rv" style="color:var(--muted);line-height:2;padding-left:24px;margin:16px 0 34px"><li>Confirm the exact username and amount with the sender.</li><li>Check your wallet history and account notifications.</li><li>Complete any pending verification request.</li><li>Contact official Roobet support with the transaction details; never share your password or seed phrase.</li></ol>
  <div class="card rv" style="border-color:rgba(255,199,0,.35)"><h3>Important distinction</h3><p>Our VIP team can help with our leaderboard, milestones, merch, points and promotional claims. It cannot enter your Roobet account, release platform-held funds or override Roobet's account rules.</p></div>
  <h2 class="rv" style="margin-top:48px">Roobet Tips FAQ</h2>
  <div class="faq rv" style="max-width:none">{"".join(f'<div class="faq-item"><button>{q}<span>+</span></button><div class="answer"><p>{a}</p></div></div>' for q,a in tips_faq)}</div>
  <p class="rv" style="color:var(--muted);margin-top:30px">For wallet fundamentals, see <a href="/how-to-deposit-on-roobet" style="color:var(--gold);font-weight:700">how to deposit</a> and <a href="/how-to-withdraw-on-roobet" style="color:var(--gold);font-weight:700">how to withdraw on Roobet</a>.</p>
</div></section>
{cta_banner("Questions About Our Rewards?","Contact the VIP team for help with DAILY rewards, claims and promotions.")}
""")

# ================= WRITE FILES =================
import re
def post(s):
    # DAILY is the lead code everywhere
    s = s.replace('<b style="color:var(--gold)">ELITE</b> or <b style="color:var(--gold)">DAILY</b>',
                  '<b style="color:var(--gold)">DAILY</b> or <b style="color:var(--gold)">ELITE</b>')
    s = s.replace("ELITE or DAILY", "DAILY or ELITE")
    s = s.replace("Code ELITE & DAILY", "Code DAILY & ELITE")
    s = s.replace("code ELITE or DAILY", "code DAILY or ELITE")
    # hyperlink every standalone gold-bold code mention (never appears in meta tags)
    s = s.replace('<b style="color:var(--gold)">DAILY</b>',
                  f'<a href="{DAILY}" rel="nofollow sponsored" target="_blank" style="color:var(--gold);font-weight:700">DAILY</a>')
    s = s.replace('<b style="color:var(--gold)">ELITE</b>',
                  f'<a href="{ELITE}" rel="nofollow sponsored" target="_blank" style="color:var(--gold);font-weight:700">ELITE</a>')
    # relative paths so pages work from disk and on Vercel
    s = s.replace('href="/css/', 'href="css/').replace('src="/js/', 'src="js/')
    s = s.replace('src="/assets/', 'src="assets/').replace('href="/assets/', 'href="assets/')
    s = re.sub(r'href="/#', 'href="index.html#', s)
    s = re.sub(r'href="/([a-z-]+)"', r'href="\1.html"', s)
    s = s.replace('href="/"', 'href="index.html"')
    return s

out = os.path.dirname(os.path.abspath(__file__))
for fname, p in PAGES.items():
    html = post(shell(fname, p["title"], p["desc"], p["kw"], p["body"], p.get("schema")))
    with open(os.path.join(out, fname), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", fname, len(html))

# sitemap
urls = [SITE + "/"] + [SITE + "/" + f[:-5] for f in PAGES if f != "index.html"]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sm += "".join(f"  <url><loc>{u}</loc><changefreq>weekly</changefreq><priority>{'1.0' if u.endswith('.com/') else '0.8'}</priority></url>\n" for u in urls)
sm += "</urlset>\n"
open(os.path.join(out, "sitemap.xml"), "w").write(sm)

open(os.path.join(out, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

open(os.path.join(out, "vercel.json"), "w").write(json.dumps({
    "cleanUrls": True, "trailingSlash": False,
    "headers": [{"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]}]
}, indent=2))

open(os.path.join(out, "assets", "favicon.svg"), "w").write(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><circle cx="24" cy="24" r="21" fill="none" stroke="#ffc700" stroke-width="4" stroke-dasharray="9 5"/><circle cx="24" cy="24" r="14" fill="#ffc700"/><text x="24" y="30" text-anchor="middle" font-family="Arial" font-weight="800" font-size="17" fill="#1a1230">R</text></svg>')

print("done:", len(PAGES), "pages + sitemap + robots + vercel.json + favicon")
