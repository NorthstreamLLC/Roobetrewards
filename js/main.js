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
