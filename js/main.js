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
  const fmtUsd = n => '$' + n.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  const prize = r =>
    r === 1 ? '$12,500' : r === 2 ? '$7,000' : r === 3 ? '$5,000' :
    r === 4 ? '$3,500' : r === 5 ? '$2,500' : r === 6 ? '$2,000' :
    r <= 10 ? '$1,100' : r <= 20 ? '$400' : r <= 30 ? '$250' :
    r <= 40 ? '$150' : r <= 50 ? '$135' :
    r <= 75 ? '100 × $1 Spins' : '50 × $1 Spins';
  const points = r =>
    r <= 15 ? 15000 : r <= 25 ? 10000 : r <= 35 ? 9000 :
    r <= 45 ? 8000 : r <= 65 ? 7000 : r <= 84 ? 6000 : 5000;

  function render(entries) {
    if (!entries || !entries.length) return;
    entries = entries.slice().sort((a, b) => a.rank - b.rank);
    // podium names + wagered
    entries.slice(0, 3).forEach(e => {
      const el = document.querySelector(`[data-pod="${e.rank}"]`);
      if (el) el.innerHTML = `<b>${e.username}</b><br><span style="color:var(--muted);font-size:.85rem">${fmtUsd(e.wagered)} wagered</span>`;
    });
    const tb = tbl.querySelector('tbody');
    tb.innerHTML = entries.map(e => {
      const p = prize(e.rank), spins = p.includes('Spins');
      return `<tr class="${e.rank <= 3 ? 'lb-top' : ''}">
        <td>${e.rank <= 3 ? ['🥇', '🥈', '🥉'][e.rank - 1] : e.rank}</td>
        <td>${e.username}</td>
        <td>${fmtUsd(e.wagered)}</td>
        <td class="${spins ? 'lb-spins' : 'gold-td'}">${p}</td>
        <td>⭐ ${points(e.rank).toLocaleString('en-US')}</td>
      </tr>`;
    }).join('');
  }

  render(window.LB_DATA && window.LB_DATA.entries);

  // upgrade to live API data when deployed (key stays server-side)
  fetch('/api/leaderboard')
    .then(r => r.ok ? r.json() : null)
    .then(d => { if (d && d.entries && d.entries.length) render(d.entries); })
    .catch(() => {});

  // collapse/expand
  const wrap = document.getElementById('lb-wrap'), btn = document.getElementById('lb-toggle');
  btn.addEventListener('click', () => {
    const open = wrap.classList.toggle('open');
    btn.textContent = open ? 'Show Top 10 Only' : 'Show Full Top 100';
    if (!open) wrap.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
})();

// ===== "DailyGambling is LIVE" toast =====
(function () {
  let shown = false;
  function showToast() {
    if (shown || sessionStorage.getItem('liveToastClosed')) return;
    shown = true;
    const t = document.createElement('div');
    t.className = 'live-toast';
    t.innerHTML = `<span class="live-dot"></span>
      <div><b>DailyGambling is LIVE</b>
      <p>Watch on Kick — earn ELITE Points &amp; catch live giveaways.</p></div>
      <a class="btn btn-gold" href="https://kick.com/dailygambling" target="_blank" rel="noopener">Watch</a>
      <button class="toast-x" aria-label="Dismiss">&times;</button>`;
    document.body.appendChild(t);
    requestAnimationFrame(() => setTimeout(() => t.classList.add('show'), 50));
    t.querySelector('.toast-x').addEventListener('click', () => {
      t.classList.remove('show');
      sessionStorage.setItem('liveToastClosed', '1');
      setTimeout(() => t.remove(), 500);
    });
  }
  function check() {
    fetch('/api/live').then(r => r.ok ? r.json() : null)
      .then(d => { if (d && d.live === true) showToast(); })
      .catch(() => {});
  }
  // first check after the promo modal has had its moment
  setTimeout(check, 8000);
  setInterval(check, 180000); // re-check every 3 min
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
