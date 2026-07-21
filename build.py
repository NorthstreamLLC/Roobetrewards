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
DISCORD = "https://discord.gg/slotessentials"
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
      <a href="/#faq">FAQ</a>
    </div>
    <div class="nav-cta">
      <a class="btn btn-ghost" href="/#how-to-sign-up">How to Sign-Up</a>
      <a class="btn btn-gold" href="{DAILY}" rel="nofollow sponsored" target="_blank">Join with DAILY</a>
      <button class="burger" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</nav>"""

def footer():
    rew = "".join(f'<a href="/{f[:-5]}">{t}</a>' for f, _, t, _ in MENU_ITEMS[:4])
    rew2 = "".join(f'<a href="/{f[:-5]}">{t}</a>' for f, _, t, _ in MENU_ITEMS[4:])
    rew2 += '<a href="/vip-transfer">VIP Transfer</a>'
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

def shell(fname, title, desc, kw, body, schema=None, og_type="website"):
    canon = SITE + ("/" if fname == "index.html" else "/" + fname[:-5])
    schema_tag = f'<script type="application/ld+json">{json.dumps(schema)}</script>' if schema else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
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
<meta name="twitter:card" content="summary_large_image">
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
     "Sign up at Roobet with code ELITE or DAILY, then deposit and wager to unlock the exclusive free spins bonus: deposit $500 and wager $5,000 for 75 free spins at $0.60, deposit $1,000 and wager $10,000 for 100 free spins at $0.80, or deposit $2,000 and wager $20,000 for 125 free spins at $1.00 each."),
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
home_schema = [
    {"@context": "https://schema.org", "@type": "WebSite", "name": "Roobet Casino Rewards", "url": SITE},
    faq_schema,
]
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
    schema=home_schema,
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
        {"@type":"Question","name":"How do I get Roobet free spins?","acceptedAnswer":{"@type":"Answer","text":"Sign up at Roobet with code ELITE or DAILY, deposit and wager to unlock up to 125 exclusive free spins worth up to $1.00 per spin."}},
        {"@type":"Question","name":"Are there no deposit free spins on Roobet?","acceptedAnswer":{"@type":"Answer","text":"Our exclusive free spins packages require a deposit and wager. Active players can also win free spins and prizes through our $5,000 monthly community giveaways and by redeeming ELITE Points — giveaways are earned through activity, not luck."}}]},
    body=f"""
<section class="page-hero"><div class="wrap">
  {crumb("Free Spins Bonus")}
  <span class="eyebrow rv">🎰 Exclusive Sign-Up Bonus</span>
  <h1 class="rv d1">Roobet Free Spins — Up to <span class="grad">125 Spins</span> at $1.00 Each</h1>
  <p class="lead rv d2">The biggest Roobet free spins deal you'll find. Join with code <b style="color:var(--gold)">ELITE</b> or <b style="color:var(--gold)">DAILY</b>, hit your deposit &amp; wager tier, and the spins are yours.</p>
  <div class="hero-cta rv d3" style="justify-content:center"><a class="btn btn-gold btn-lg pulse" href="{SLOTS}" target="_blank" rel="noopener">Claim Free Spins {ARR}</a></div>
</div></section>

<section style="padding-top:10px"><div class="wrap"><div class="cards c3">
  <div class="card rv center"><div class="glow"></div><p class="amount">75 Spins</p><p style="font-weight:700;color:var(--text)">$0.60 per spin — $45 value</p><p style="margin-top:10px">Deposit <b style="color:var(--gold)">$500</b><br>Wager <b style="color:var(--gold)">$5,000</b></p></div>
  <div class="card rv d1 center" style="border-color:rgba(255,199,0,.5)"><span class="tag">Most Popular</span><div class="glow"></div><p class="amount">100 Spins</p><p style="font-weight:700;color:var(--text)">$0.80 per spin — $80 value</p><p style="margin-top:10px">Deposit <b style="color:var(--gold)">$1,000</b><br>Wager <b style="color:var(--gold)">$10,000</b></p></div>
  <div class="card rv d2 center"><span class="tag">Max Value</span><div class="glow"></div><p class="amount">125 Spins</p><p style="font-weight:700;color:var(--text)">$1.00 per spin — $125 value</p><p style="margin-top:10px">Deposit <b style="color:var(--gold)">$2,000</b><br>Wager <b style="color:var(--gold)">$20,000</b></p></div>
</div></div></section>

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

<section style="padding-top:10px"><div class="wrap"><div class="cards c3">
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
