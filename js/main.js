/* roobetcasinorewards.com — motion + interactions */
(function () {
  // sticky nav
  const nav = document.querySelector('nav');
  const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 24);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // mobile menu
  const burger = document.querySelector('.burger');
  const links = document.querySelector('.nav-links');
  if (burger) burger.addEventListener('click', () => links.classList.toggle('open'));
  document.querySelectorAll('.dropdown > button').forEach(b => {
    b.addEventListener('click', () => b.parentElement.classList.toggle('open'));
  });

  // scroll reveal
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('on'); io.unobserve(e.target); }
    });
  }, { threshold: 0.12 });
  document.querySelectorAll('.rv').forEach(el => io.observe(el));

  // animated counters  <span data-count="100000" data-prefix="$">
  const fmt = n => n.toLocaleString('en-US');
  const cio = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      cio.unobserve(e.target);
      const el = e.target, target = +el.dataset.count,
        pre = el.dataset.prefix || '', suf = el.dataset.suffix || '',
        t0 = performance.now(), dur = 1600;
      const tick = now => {
        const p = Math.min((now - t0) / dur, 1),
          ease = 1 - Math.pow(1 - p, 3);
        el.textContent = pre + fmt(Math.round(target * ease)) + suf;
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    });
  }, { threshold: 0.4 });
  document.querySelectorAll('[data-count]').forEach(el => cio.observe(el));

  // milestone progress bars
  const mio = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      mio.unobserve(e.target);
      const bar = e.target.querySelector('.bar i');
      if (bar) setTimeout(() => bar.style.width = bar.dataset.w + '%', 150);
    });
  }, { threshold: 0.3 });
  document.querySelectorAll('.mile').forEach(el => mio.observe(el));

  // card tilt
  document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('mousemove', ev => {
      const r = card.getBoundingClientRect(),
        x = (ev.clientX - r.left) / r.width - 0.5,
        y = (ev.clientY - r.top) / r.height - 0.5;
      card.style.transform = `translateY(-6px) rotateX(${-y * 4}deg) rotateY(${x * 4}deg)`;
    });
    card.addEventListener('mouseleave', () => card.style.transform = '');
  });

  // countdown  <span data-deadline="monthly|weekly|daily">
  function next(kind) {
    const n = new Date();
    if (kind === 'daily') {
      const d = new Date(Date.UTC(n.getUTCFullYear(), n.getUTCMonth(), n.getUTCDate() + 1));
      return d;
    }
    if (kind === 'weekly') { // Saturday midnight UTC
      const d = new Date(Date.UTC(n.getUTCFullYear(), n.getUTCMonth(), n.getUTCDate()));
      d.setUTCDate(d.getUTCDate() + ((7 - d.getUTCDay()) % 7 || 7));
      while (d.getUTCDay() !== 0) d.setUTCDate(d.getUTCDate() + 1);
      return d;
    }
    if (kind === 'period16') { // leaderboard period: 16th 00:00 UTC -> next 16th
      const t = Date.UTC(n.getUTCFullYear(), n.getUTCMonth(), 16);
      return new Date(n.getTime() < t ? t : Date.UTC(n.getUTCFullYear(), n.getUTCMonth() + 1, 16));
    }
    return new Date(Date.UTC(n.getUTCFullYear(), n.getUTCMonth() + 1, 1)); // monthly
  }
  document.querySelectorAll('[data-deadline]').forEach(el => {
    const target = next(el.dataset.deadline);
    const upd = () => {
      let s = Math.max(0, (target - Date.now()) / 1000 | 0);
      const d = s / 86400 | 0; s %= 86400;
      const h = s / 3600 | 0; s %= 3600;
      const m = s / 60 | 0; s %= 60;
      el.textContent = `${d}d ${h}h ${m}m ${s}s`;
    };
    upd(); setInterval(upd, 1000);
  });
})();

// point shop card flip
document.querySelectorAll('.flip').forEach(c => {
  c.addEventListener('click', e => {
    if (e.target.closest('a')) return;
    c.classList.toggle('flipped');
  });
});

// entry promo modal (once per session)
(function () {
  const m = document.getElementById('promo-modal');
  if (!m) return;
  try {
    if (sessionStorage.getItem('promoShown')) return;
    sessionStorage.setItem('promoShown', '1');
  } catch (e) { /* private mode: still show once */ }
  setTimeout(() => m.classList.add('show'), 1200);
  const close = () => m.classList.remove('show');
  m.querySelector('.modal-x').addEventListener('click', close);
  m.addEventListener('click', e => { if (e.target === m) close(); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
})();

// ===== live leaderboard =====
(function () {
  const tbl = document.getElementById('lb-table');
  if (!tbl) return;
  const body = document.getElementById('lb-body');
  const wrap = document.getElementById('lb-wrap');
  const btn = document.getElementById('lb-toggle');
  const search = document.getElementById('lb-search');
  const stamp = document.getElementById('lb-updated');
  const tiers = window.LB_TIERS || [];
  let rows = [];

  const usd = n => '$' + n.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  const esc = s => String(s).replace(/[<>&"]/g, c => ({ '<': '&lt;', '>': '&gt;', '&': '&amp;', '"': '&quot;' }[c]));
  const tierOf = r => tiers.find(t => r >= t.from && r <= t.to) || { prize: '—', points: 0 };

  function paint(filter) {
    const q = (filter || '').trim().toLowerCase();
    const list = q ? rows.filter(e => e.username.toLowerCase().includes(q)) : rows;
    if (!list.length) {
      body.innerHTML = '<tr><td colspan="5" style="text-align:center;color:var(--muted);padding:36px">' +
        (q ? 'No player matches “' + esc(filter) + '”. Usernames are masked — try the first 3 letters.' : 'Standings will appear here shortly.') + '</td></tr>';
      return;
    }
    body.innerHTML = list.map(e => {
      const t = tierOf(e.rank), spins = String(t.prize).indexOf('Spins') > -1;
      const medal = e.rank <= 3 ? ['🥇', '🥈', '🥉'][e.rank - 1] : e.rank;
      return '<tr class="' + (e.rank <= 3 ? 'lb-top' : '') + '">' +
        '<td>' + medal + '</td>' +
        '<td>' + esc(e.username) + '</td>' +
        '<td class="lb-wager">' + usd(e.wagered) + '</td>' +
        '<td class="' + (spins ? 'lb-spins' : 'gold-td') + '">' + t.prize + '</td>' +
        '<td class="col-pts">⭐ ' + t.points.toLocaleString('en-US') + '</td>' +
        '</tr>';
    }).join('');
    // searching always shows every match
    if (q) wrap.classList.add('open');
  }

  function render(entries, live, updated) {
    if (!entries || !entries.length) return false;
    rows = entries.slice().sort((a, b) => a.rank - b.rank);
    rows.slice(0, 3).forEach(e => {
      const el = document.querySelector('[data-pod="' + e.rank + '"]');
      if (el) el.innerHTML = '<b>' + esc(e.username) + '</b><br><span style="color:var(--muted);font-size:.85rem">' + usd(e.wagered) + ' wagered</span>';
    });
    paint(search ? search.value : '');
    if (stamp) {
      stamp.innerHTML = live
        ? '<span class="lb-dot"></span> Live · updated ' + new Date(updated || Date.now()).toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit' })
        : 'Showing last saved standings';
    }
    return true;
  }

  // live first — the snapshot is only a safety net
  fetch('/api/leaderboard')
    .then(r => (r.ok ? r.json() : null))
    .then(d => {
      if (!(d && d.entries && d.entries.length && render(d.entries, true, d.updated))) throw new Error('no live data');
    })
    .catch(() => { render(window.LB_DATA && window.LB_DATA.entries, false); });

  if (search) search.addEventListener('input', () => paint(search.value));

  btn.addEventListener('click', () => {
    const open = wrap.classList.toggle('open');
    btn.textContent = open ? 'Show Top 10 Only' : 'Show Full Top 100';
    if (!open) document.getElementById('standings').scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
})();

// ===== live status: nav pill + toast + watch page =====
(function () {
  const pill = document.getElementById('live-pill');
  const status = document.getElementById('watch-status');
  const onWatch = !!document.getElementById('stream-frame');
  let toastShown = false;

  function showToast() {
    if (toastShown || onWatch || sessionStorage.getItem('liveToastClosed')) return;
    toastShown = true;
    const t = document.createElement('div');
    t.className = 'live-toast';
    t.innerHTML = '<span class="live-dot"></span>' +
      '<div><b>DailyGambling is LIVE</b>' +
      '<p>Watch on site &amp; earn ELITE Points for your watch time.</p></div>' +
      '<a class="btn btn-gold" href="/watch">Watch</a>' +
      '<button class="toast-x" aria-label="Dismiss">&times;</button>';
    document.body.appendChild(t);
    requestAnimationFrame(() => setTimeout(() => t.classList.add('show'), 50));
    t.querySelector('.toast-x').addEventListener('click', () => {
      t.classList.remove('show');
      sessionStorage.setItem('liveToastClosed', '1');
      setTimeout(() => t.remove(), 500);
    });
  }

  function apply(live, d) {
    if (pill) pill.classList.toggle('on', live === true);
    const badge = document.getElementById('badge-live');
    const vc = document.getElementById('badge-viewers');
    const st = document.getElementById('stream-title');
    if (badge) badge.classList.toggle('on', live === true);
    if (vc) {
      const n = d && typeof d.viewers === 'number' ? d.viewers : null;
      if (live === true && n !== null) { vc.textContent = n.toLocaleString('en-US') + ' watching'; vc.hidden = false; }
      else vc.hidden = true;
    }
    if (st && live === true && d && d.title) st.textContent = d.title;
    if (status) {
      status.innerHTML = live === true
        ? '<span class="live-dot"></span> LIVE NOW'
        : (live === false ? '💤 Currently offline — replays and next stream on Kick' : '📺 Stream status unavailable');
      status.classList.toggle('is-live', live === true);
    }
    if (live === true) showToast();
    window.dispatchEvent(new CustomEvent('rrLiveData', { detail: d || { live: live } }));
  }

  function check() {
    fetch('/api/live')
      .then(r => (r.ok ? r.json() : null))
      .then(d => apply(d ? d.live : null, d))
      .catch(() => apply(null));
  }
  check();
  setTimeout(check, 8000);
  setInterval(check, 120000);
})();

// ===== live raffle widget (giveaways page) =====
(function () {
  const w = document.getElementById('raffle-widget');
  if (!w) return;
  const $ = id => document.getElementById(id);
  const esc = s => String(s).replace(/[<>&"]/g, c => ({'<':'&lt;','>':'&gt;','&':'&amp;','"':'&quot;'}[c]));

  function countdown(el, endsAt) {
    const upd = () => {
      let s = Math.max(0, (endsAt - Date.now()) / 1000 | 0);
      const d = s / 86400 | 0; s %= 86400;
      const h = s / 3600 | 0; s %= 3600;
      const m = s / 60 | 0;
      el.textContent = `${d}d ${h}h ${m}m`;
    };
    upd(); setInterval(upd, 30000);
  }

  function render(d) {
    const r = d && d.raffle;
    if (!r) {
      $('rf-title').textContent = 'No raffle live right now';
      $('rf-info').innerHTML = 'Next drop is never far away — follow the <a href="https://discord.gg/slotessentials" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">Discord</a> and watch <a href="https://kick.com/dailygambling" target="_blank" rel="noopener" style="color:var(--gold);font-weight:700">DailyGambling live</a> so you never miss one.';
      $('rf-actions').innerHTML = '';
      $('rf-meta').textContent = '';
      return;
    }
    if (r.drawn) {
      $('rf-title').textContent = `🏁 ${r.title} — Winners`;
      $('rf-info').innerHTML = (r.prize ? `<b style="color:var(--gold)">${esc(r.prize)}</b> — ` : '') + 'congratulations to:';
      $('rf-actions').innerHTML = r.winners.map(x => `<span class="btn btn-ghost" style="cursor:default">🎉 ${esc(x)}</span>`).join('');
      $('rf-meta').textContent = 'Winners are contacted by the VIP team. Next raffle soon!';
      return;
    }
    $('rf-title').textContent = `🎟️ ${r.title}`;
    $('rf-info').innerHTML = (r.prize ? `Prize: <b style="color:var(--gold)">${esc(r.prize)}</b><br>` : '') +
      `<span style="font-size:.95rem">Ends in <b style="color:var(--gold)" id="rf-cd">—</b> · <b>${d.count}</b> entries</span>`;
    countdown($('rf-cd'), r.endsAt);
    if (d.entered) {
      $('rf-actions').innerHTML = `<span class="btn btn-gold" style="cursor:default">✅ You're in, ${esc(d.me.username)} — good luck!</span>`;
      $('rf-meta').textContent = 'One entry per Kick account. Winners announced right here.';
    } else if (d.me) {
      $('rf-actions').innerHTML = `<button class="btn btn-gold btn-lg pulse" id="rf-enter">Enter Raffle — Free</button>`;
      $('rf-meta').textContent = `Signed in as ${d.me.username} via Kick.`;
      $('rf-enter').addEventListener('click', () => {
        fetch('/api/raffle', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ action: 'enter' }) })
          .then(r => r.json()).then(load);
      });
    } else {
      $('rf-actions').innerHTML = `<a class="btn btn-gold btn-lg pulse" href="/api/kick/login">Sign in with Kick to Enter</a>`;
      $('rf-meta').textContent = 'Free to enter · one entry per Kick account · active players only.';
    }
  }

  function load() {
    fetch('/api/raffle').then(r => r.ok ? r.json() : null).then(render)
      .catch(() => {
        $('rf-title').textContent = 'Raffle temporarily unavailable';
        $('rf-info').textContent = 'Check back shortly.';
      });
  }
  load();
})();

// ===== latest YouTube uploads =====
(function () {
  const grid = document.getElementById('yt-grid');
  if (!grid) return;
  const esc = s => String(s).replace(/[<>&"]/g, c => ({ '<': '&lt;', '>': '&gt;', '&': '&amp;', '"': '&quot;' }[c]));
  const ago = iso => {
    const d = Math.floor((Date.now() - new Date(iso)) / 86400000);
    if (isNaN(d)) return '';
    return d <= 0 ? 'today' : d === 1 ? '1 day ago' : d < 30 ? d + ' days ago' : Math.floor(d / 30) + ' mo ago';
  };
  fetch('/api/youtube?limit=8')
    .then(r => (r.ok ? r.json() : null))
    .then(d => {
      if (!d || !d.videos || !d.videos.length) throw new Error('none');
      grid.innerHTML = d.videos.map((v, i) =>
        `<a class="vid-card" style="animation-delay:${i * 60}ms" href="${esc(v.url)}" target="_blank" rel="noopener">
           <div class="vid-thumb"><img src="${esc(v.thumbnail)}" alt="${esc(v.title)}" loading="lazy"></div>
           <div class="meta"><h3>${esc(v.title)}</h3><p class="sub">${ago(v.published)}${v.views ? ' · ' + v.views.toLocaleString('en-US') + ' views' : ''}</p></div>
         </a>`).join('');
    })
    .catch(() => {
      grid.innerHTML = '<a class="card" href="https://www.youtube.com/@dailygamba" target="_blank" rel="noopener" style="grid-column:1/-1;text-align:center"><div class="ic" style="margin:0 auto 12px">▶</div><h3>Watch on YouTube</h3><p>Head to the channel for the latest full sessions and bonus hunts.</p></a>';
    });
})();

// ===== watch page: live stats + honest session tracker =====
(function () {
  if (!document.getElementById('stream-frame')) return;
  const $ = id => document.getElementById(id);
  const RATE_PTS = 50, RATE_MIN = 15;          // 50 ELITE Points per 15 minutes
  let liveNow = false, startedAt = null, secs = 0;

  try { secs = parseInt(sessionStorage.getItem('watchSecs') || '0', 10) || 0; } catch (e) {}

  function paintSession() {
    const box = $('sess-box'), bar = $('sess-barwrap');
    if (!box) return;
    const mins = Math.floor(secs / 60);
    const show = liveNow && secs > 0;
    box.hidden = !show; if (bar) bar.hidden = !show;
    if (!show) return;
    $('sess-min').textContent = mins;
    $('sess-pts').textContent = (Math.floor(mins / RATE_MIN) * RATE_PTS).toLocaleString('en-US');
    const pct = ((mins % RATE_MIN) / RATE_MIN) * 100;
    const fill = $('sess-bar'); if (fill) fill.style.width = pct + '%';
  }

  function paintUptime() {
    const el = $('ls-uptime');
    if (!el) return;
    if (!liveNow || !startedAt) { el.hidden = true; return; }
    let s = Math.max(0, Math.floor((Date.now() - startedAt) / 1000));
    const h = Math.floor(s / 3600); s %= 3600;
    const m = Math.floor(s / 60); s %= 60;
    el.querySelector('b').textContent = `${h}:${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
    el.hidden = false;
  }

  window.addEventListener('rrLiveData', e => {
    const d = e.detail || {};
    liveNow = d.live === true;
    startedAt = d.started ? new Date(d.started).getTime() : null;
    const w = $('ls-watching');
    if (w) {
      if (liveNow && typeof d.viewers === 'number') { w.querySelector('b').textContent = d.viewers.toLocaleString('en-US'); w.hidden = false; }
      else w.hidden = true;
    }
    paintUptime(); paintSession();
  });

  setInterval(() => {
    if (!liveNow || document.hidden) return;
    secs += 1;
    try { sessionStorage.setItem('watchSecs', String(secs)); } catch (e) {}
    if (secs % 10 === 0) paintSession();
  }, 1000);
  setInterval(paintUptime, 1000);
})();
