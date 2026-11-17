/* O Tse & Co. concept: menu, open-now status, first-meeting checklist, contact form, lazy map. */
(() => {
  const zh = document.documentElement.lang.startsWith('zh');
  const T = (en, z) => (zh ? z : en);
  const WA = '447511374988';

  /* ---------- menu ---------- */
  const btn = document.querySelector('.menu-btn');
  const menu = document.getElementById('menu');
  if (btn && menu) {
    const set = (open) => {
      btn.setAttribute('aria-expanded', open);
      menu.hidden = !open;
      document.body.classList.toggle('menu-open', open);
      btn.textContent = open ? T('Close', '關閉') : T('Menu', '選單');
    };
    btn.addEventListener('click', () => set(menu.hidden));
    menu.addEventListener('click', (e) => { if (e.target.closest('a')) set(false); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !menu.hidden) { set(false); btn.focus(); } });
    window.matchMedia('(min-width: 1081px)').addEventListener('change', (m) => { if (m.matches) set(false); });
  }

  /* ---------- open now, in Manchester time (Mon–Fri 9:30–17:30; bank holidays not checked) ---------- */
  const parts = new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/London', weekday: 'short', hour: 'numeric', minute: 'numeric', hourCycle: 'h23' }).formatToParts(new Date());
  const g = (t) => (parts.find((x) => x.type === t) || {}).value;
  const day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'].indexOf(g('weekday'));
  const mins = Number(g('hour')) * 60 + Number(g('minute'));
  const weekday = day >= 0 && day <= 4;
  const open = weekday && mins >= 570 && mins < 1050;
  let txt;
  if (open) txt = T('Open now, until 5:30pm', '現在辦公中，至下午5:30');
  else if (weekday && mins < 570) txt = T('Closed now, opens today at 9:30am', '現在休息，今日上午9:30開門');
  else if (day >= 0 && day < 4) txt = T('Closed now, opens tomorrow at 9:30am', '現在休息，明日上午9:30開門');
  else txt = T('Closed now, opens Monday at 9:30am', '現在休息，星期一上午9:30開門');
  document.querySelectorAll('[data-open]').forEach((el) => {
    el.classList.toggle('is-open', open);
    el.querySelector('[data-open-txt]').textContent = txt + T(' (UK time)', '（英國時間）');
  });

  /* ---------- first-meeting checklist ---------- */
  document.querySelectorAll('[data-check]').forEach((form) => {
    const lists = [...form.querySelectorAll('.ck-list')];
    const count = form.querySelector('[data-count]');
    const waBtn = form.querySelector('[data-ck-wa]');
    const current = () => lists.find((l) => !l.hidden);
    const update = () => {
      const l = current();
      const boxes = [...l.querySelectorAll('input')];
      const done = boxes.filter((b) => b.checked).length;
      count.textContent = T(`${done} of ${boxes.length} found`, `已準備 ${done} / ${boxes.length} 項`);
      const msg = T(`Hello, I would like to book a first meeting about: ${l.dataset.label}.`, `你好，我想預約首次見面，事務類型：${l.dataset.label}。`);
      waBtn.href = `https://wa.me/${WA}?text=${encodeURIComponent(msg)}`;
    };
    form.addEventListener('change', (e) => {
      if (e.target.name === 'matter') lists.forEach((l) => { l.hidden = l.dataset.matter !== e.target.value; });
      update();
    });
    form.addEventListener('submit', (e) => e.preventDefault());
    const pr = form.querySelector('[data-print]');
    if (pr) pr.addEventListener('click', () => window.print());
    update();
  });

  /* ---------- contact form: WhatsApp or email, nothing stored ---------- */
  document.querySelectorAll('[data-ask]').forEach((form) => {
    const err = form.querySelector('[data-err]');
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const f = form.elements;
      let ok = true;
      ['name', 'reach', 'msg'].forEach((k) => {
        const bad = !f[k].value.trim();
        f[k].setAttribute('aria-invalid', bad);
        if (bad) ok = false;
      });
      err.hidden = ok;
      if (!ok) { form.querySelector('[aria-invalid="true"]').focus(); return; }
      const text = `${f.msg.value.trim()}\n\n${T('Name', '名字')}: ${f.name.value.trim()}\n${T('Contact', '聯絡')}: ${f.reach.value.trim()}\n${T('About', '事務類型')}: ${f.topic.value}`;
      const via = e.submitter && e.submitter.value;
      if (via === 'mail') location.href = `mailto:ask@otse.co.uk?subject=${encodeURIComponent(T('Enquiry: ', '查詢：') + f.topic.value)}&body=${encodeURIComponent(text)}`;
      else window.open(`https://wa.me/${WA}?text=${encodeURIComponent(text)}`, '_blank', 'noopener');
    });
  });

  /* ---------- map, loaded when it nears the screen ---------- */
  const box = document.querySelector('[data-map]');
  if (box && 'IntersectionObserver' in window) {
    const load = (src, tag) => new Promise((ok, bad) => {
      const el = document.createElement(tag === 'css' ? 'link' : 'script');
      if (tag === 'css') { el.rel = 'stylesheet'; el.href = src; } else { el.src = src; }
      el.onload = ok; el.onerror = bad;
      document.head.appendChild(el);
    });
    const io = new IntersectionObserver((entries) => {
      if (!entries.some((e) => e.isIntersecting)) return;
      io.disconnect();
      Promise.all([load(box.dataset.css, 'css'), load(box.dataset.src)])
        .then(() => load(box.dataset.mapjs))
        .then(() => window.otseMap && window.otseMap(box))
        .catch(() => { /* the sketch stays */ });
    }, { rootMargin: '400px' });
    io.observe(box);
  }
})();
