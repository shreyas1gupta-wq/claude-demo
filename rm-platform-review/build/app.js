/* Ionic RM Platform Review — render layer.
   DATA and QC are injected above this file at build time by render.py. */

const LS = 'ionic_rm_review_v4';   // bumped: v3 notes were keyed to the 72-RM roster
let notes = {};
try { const s = localStorage.getItem(LS); if (s) notes = JSON.parse(s) || {}; } catch (e) {}
let cur = 0;
const QC_TAB = -1;

/* ---------- formatting ---------- */
const cr = v => {
  v = Number(v);
  if (!v || isNaN(v)) return '<span class=mut>&ndash;</span>';
  return v.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
};
const n0 = v => Number(v || 0).toLocaleString('en-IN');
const f1 = v => Number(v || 0).toFixed(1);
// cr() shows a dash for zero, which is right in a table but wrong mid-sentence
const cr0 = v => Number(v || 0).toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c =>
  ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const signed = (v, d = 1) => (v >= 0 ? '+' : '−') + Math.abs(v).toFixed(d);
const arrow = d => d > 0.01 ? '<span class="arrow pos">&#9650;</span>'
  : (d < -0.01 ? '<span class="arrow neg">&#9660;</span>' : '<span class="arrow mut">&#8226;</span>');
const penColor = p => p >= 0.20 ? 'var(--green)' : (p >= 0.08 ? 'var(--indigo)' : 'var(--coral)');

/* Series colours: snapped from the Ionic brand hues to pass the categorical
   colour checks. Assigned by product identity in fixed order, never by rank. */
const SERIES = { 'Allocate': 'var(--s-allocate)', 'YE': 'var(--s-ye)',
                 'Navigate': 'var(--s-navigate)', 'Co-Pilot': 'var(--s-copilot)' };
const SERIES_FULL = { 'Allocate': 'Allocate', 'YE': 'High Yield Enhancer',
                      'Navigate': 'Navigate', 'Co-Pilot': 'Co-Pilot' };

/* ---------- tooltip ---------- */
const tip = () => document.getElementById('tip');
function showTip(evt, html) {
  const t = tip(); t.innerHTML = html; t.classList.add('on');
  const r = t.getBoundingClientRect();
  let x = evt.clientX + 14, y = evt.clientY - r.height / 2;
  if (x + r.width > window.innerWidth - 8) x = evt.clientX - r.width - 14;
  t.style.left = Math.max(8, x) + 'px';
  t.style.top = Math.min(Math.max(8, y), window.innerHeight - r.height - 8) + 'px';
}
function hideTip() { tip().classList.remove('on'); }
function bindTips(root) {
  root.querySelectorAll('[data-tip]').forEach(el => {
    el.addEventListener('mousemove', e => showTip(e, el.dataset.tip));
    el.addEventListener('mouseleave', hideTip);
  });
}

/* ---------- flags ---------- */
function flagOf(r) {
  const breadth = r.prod.filter(p => p.aug > 0).length;
  if (r.p_aug === 0) return { t: 'No platform book', c: 'none' };
  if ((r.p_aug - r.p_jun) < -0.01) return { t: 'Slipping vs Jun', c: 'slip' };
  if (r.p_mar === 0) return { t: 'Built since Mar', c: 'new' };
  if (breadth === 1) return { t: 'Single-product', c: 'single' };
  return { t: '', c: '' };
}

/* ---------- firm KPI strip ---------- */
function fks() {
  const F = DATA.firm;
  const cells = [
    ['&#8377;' + n0(Math.round(F.tot_aug)), '<span class=u>Cr</span>', 'Total book'],
    ['&#8377;' + cr(F.p_aug), '<span class=u>Cr</span>', 'Platform'],
    [f1(F.p_aug / F.tot_aug * 100) + '%', '', 'Penetration'],
    [n0(F.p_cl), '<span class=u>/ ' + n0(F.cl_aug) + '</span>', 'Platform clients'],
    [n0(F.households), '<span class=u>hh</span>', 'Households'],
    ['&#8377;' + cr(F.f_aug), '<span class=u>Cr</span>', 'Focus'],
    [F.rms, '', 'RMs'],
  ];
  document.getElementById('fks').innerHTML = cells.map(x =>
    `<div class=fk><div class=v>${x[0]}${x[1]}</div><div class=l>${x[2]}</div></div>`).join('');
}

/* ---------- firm platform trend (line, single series, hover crosshair) ---------- */
function trendChart() {
  const pts = DATA.firm.trend;
  const W = 640, H = 190, L = 46, R = 16, T = 14, B = 30;
  const iw = W - L - R, ih = H - T - B;
  const max = Math.ceil(Math.max(...pts.map(p => p[1])) / 100) * 100;
  const x = i => L + (pts.length === 1 ? iw / 2 : i * iw / (pts.length - 1));
  const y = v => T + ih - (v / max) * ih;
  const ticks = [0, max / 4, max / 2, max * 3 / 4, max];

  let g = ticks.map(t =>
    `<line class="axis-line" x1="${L}" x2="${W - R}" y1="${y(t).toFixed(1)}" y2="${y(t).toFixed(1)}"/>
     <text class="tick" x="${L - 8}" y="${(y(t) + 3.5).toFixed(1)}" text-anchor="end">${t}</text>`).join('');
  const path = pts.map((p, i) => `${i ? 'L' : 'M'}${x(i).toFixed(1)},${y(p[1]).toFixed(1)}`).join(' ');
  const area = `M${x(0).toFixed(1)},${y(0).toFixed(1)} ` +
    pts.map((p, i) => `L${x(i).toFixed(1)},${y(p[1]).toFixed(1)}`).join(' ') +
    ` L${x(pts.length - 1).toFixed(1)},${y(0).toFixed(1)} Z`;

  const marks = pts.map((p, i) => {
    const prev = i ? pts[i - 1][1] : null;
    const move = prev === null ? 'first reported point'
      : `${signed(p[1] - prev, 2)}Cr vs ${esc(pts[i - 1][0])}`;
    const t = `<b>${esc(p[0])}</b><br>Platform &#8377;${cr(p[1])}Cr<br>${move}`;
    return `<circle cx="${x(i).toFixed(1)}" cy="${y(p[1]).toFixed(1)}" r="4.5"
       fill="var(--s-allocate)" stroke="#fff" stroke-width="2" data-tip="${t}"/>
      <rect class="hit" x="${(x(i) - 22).toFixed(1)}" y="${T}" width="44" height="${ih}" data-tip="${t}"/>`;
  }).join('');

  // direct-label only the endpoint, per the selective-labelling rule
  const last = pts[pts.length - 1];
  const labels = pts.map((p, i) =>
    `<text class="tick" x="${x(i).toFixed(1)}" y="${H - 10}" text-anchor="middle">${esc(p[0])}</text>`).join('');

  return `<div class="fig">
    <h3>Firm platform build</h3>
    <div class="sub">Core-4 net-funding basis, &#8377;Cr. Reported at milestones, not monthly.
      Mar&#8211;Aug values are the Aug-31 MIS restatement.</div>
    <svg viewBox="0 0 ${W} ${H}" role="img"
      aria-label="Firm platform AUM rising from ${cr(pts[0][1])} crore at ${esc(pts[0][0])} to ${cr(last[1])} crore at ${esc(last[0])}">
      ${g}
      <path d="${area}" fill="var(--s-allocate)" opacity=".08"/>
      <path d="${path}" stroke="var(--s-allocate)" stroke-width="2" fill="none" stroke-linejoin="round"/>
      ${marks}
      <text class="vlab" x="${(x(pts.length - 1) - 6).toFixed(1)}" y="${(y(last[1]) - 12).toFixed(1)}"
        text-anchor="end">&#8377;${cr(last[1])}Cr</text>
      ${labels}
    </svg>
  </div>`;
}

/* ---------- firm product mix (stacked bar + table view) ---------- */
function mixChart() {
  const F = DATA.firm, total = F.p_aug;
  const segs = F.mix.filter(m => m[1] > 0);
  // ink that stays legible on each fill: the two light slots take dark ink
  const ON = { 'Allocate': '#fff', 'YE': '#3D2A05', 'Navigate': '#14224A', 'Co-Pilot': '#fff' };
  const bar = segs.map(m => {
    const share = m[1] / total;
    const t = `<b>${esc(SERIES_FULL[m[0]])}</b><br>&#8377;${cr(m[1])}Cr<br>${f1(share * 100)}% of platform`;
    const label = share >= 0.12 ? `${esc(m[0])} ${f1(share * 100)}%`
      : (share >= 0.055 ? `${f1(share * 100)}%` : '');
    return `<span style="flex:${m[1]};background:${SERIES[m[0]]};color:${ON[m[0]]};
      font-size:10px;font-weight:600;display:flex;align-items:center;justify-content:center;
      white-space:nowrap;overflow:hidden" data-tip="${t}">${label}</span>`;
  }).join('');
  const rows = F.mix.map(m => `<tr>
      <td><i class="swatch" style="background:${SERIES[m[0]]}"></i>${esc(SERIES_FULL[m[0]])}</td>
      <td class="n">&#8377;${cr(m[1])}</td><td class="n">${f1(m[1] / total * 100)}%</td></tr>`).join('');
  return `<div class="fig">
    <h3>Platform mix by product</h3>
    <div class="sub">Core-4 only. Sharpe One and PIPE (&#8377;${cr(F.all_products - total)}Cr)
      sit outside this basis; all platform products together are &#8377;${cr(F.all_products)}Cr.</div>
    <div class="mixbar">${bar}</div>
    <table class="mixtab">
      <thead><tr><th>Product</th><th class="n">Aug-31 &#8377;Cr</th><th class="n">Share</th></tr></thead>
      <tbody>${rows}
        <tr><td><b>Total</b></td><td class="n"><b>&#8377;${cr(total)}</b></td><td class="n"><b>100.0%</b></td></tr>
      </tbody></table>
  </div>`;
}

/* ---------- per-desk RM platform bars (single series) ---------- */
function rmBars(t) {
  const rows = t.rows;
  const W = 1200, rowH = 27, L = 210, R = 104, T = 8;
  const H = T + rows.length * rowH + 20;
  const max = Math.max(...rows.map(r => r.p_aug), 0.0001);
  const iw = W - L - R;
  const bars = rows.map((r, i) => {
    const yy = T + i * rowH;
    const w = Math.max(r.p_aug / max * iw, r.p_aug > 0 ? 2 : 0);
    const pen = r.tot_aug ? r.p_aug / r.tot_aug : 0;
    const tt = `<b>${esc(r.rm)}</b><br>Platform &#8377;${cr(r.p_aug)}Cr of &#8377;${cr(r.tot_aug)}Cr book`
      + `<br>${f1(pen * 100)}% penetration &middot; ${r.p_cl}/${r.cl_aug} clients`
      + `<br>${signed(r.p_aug - r.p_jun, 2)}Cr vs Jun`;
    return `<g data-tip="${tt}">
      <rect class="hit" x="0" y="${yy}" width="${W}" height="${rowH - 2}"/>
      <text class="tick" x="${L - 12}" y="${yy + 16}" text-anchor="end">${esc(r.rm)}</text>
      <rect x="${L}" y="${yy + 7}" width="${w.toFixed(1)}" height="10" rx="4"
        fill="var(--s-allocate)" opacity="${r.p_aug > 0 ? 1 : 0}"/>
      <text class="vlab" x="${(L + w + 8).toFixed(1)}" y="${yy + 16}">${r.p_aug > 0 ? '&#8377;' + cr(r.p_aug) : '&ndash;'}</text>
    </g>`;
  }).join('');
  return `<div class="fig">
    <h3>Platform AUM by RM</h3>
    <div class="sub">Aug-31, core-4, &#8377;Cr. Ranked within the desk. Hover for penetration and movement vs Jun.</div>
    <svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Platform AUM per RM for ${esc(t.ml)}">
      <line class="axis-line" x1="${L}" x2="${L}" y1="${T}" y2="${(T + rows.length * rowH).toFixed(1)}"/>
      ${bars}
    </svg>
  </div>`;
}

/* ---------- per-desk product movement Jun -> Aug (diverging) ---------- */
function deltaStrip(t) {
  if (!t.pdelta) {
    return `<div class="dstrip"><div class="dchip" style="min-width:100%">
      <div class="p">Jun&#8594;Aug product movement</div>
      <div class="v" style="font-size:12px;font-weight:400;color:var(--grey)">
        Not reported for this desk &mdash; it has no market-leader row in the MIS platform-by-product block.</div>
    </div></div>`;
  }
  const order = ['Allocate', 'YE', 'Navigate', 'Co-Pilot'];
  const max = Math.max(...order.map(k => Math.abs(t.pdelta[k] || 0)), 0.0001);
  const chips = order.map(k => {
    const d = t.pdelta[k] || 0, jun = (t.pjun_prod || {})[k] || 0;
    const aug = jun + d;
    const w = Math.abs(d) / max * 50;
    const tt = `<b>${esc(SERIES_FULL[k])}</b><br>Jun-30 &#8377;${cr(jun)}Cr &#8594; Aug-31 &#8377;${cr(aug)}Cr<br>${signed(d, 2)}Cr`;
    return `<div class="dchip" data-tip="${tt}">
      <div class="p"><i class="swatch" style="background:${SERIES[k]}"></i>${esc(k)}</div>
      <div class="v" style="color:${d > 0.005 ? 'var(--pos)' : (d < -0.005 ? 'var(--neg)' : 'var(--grey)')}">
        ${Math.abs(d) < 0.005 ? 'flat' : signed(d, 2)}</div>
      <div class="b"><i style="${d >= 0 ? 'left:50%' : 'right:50%'};width:${w.toFixed(1)}%;
        background:${d > 0.005 ? 'var(--pos)' : (d < -0.005 ? 'var(--neg)' : 'transparent')}"></i></div>
    </div>`;
  }).join('');
  return `<div class="dlab">Platform movement Jun-30 &#8594; Aug-31 by product, &#8377;Cr</div>
    <div class="dstrip">${chips}</div>`;
}

/* ---------- RM card ---------- */
function card(r, idx) {
  const F = flagOf(r);
  const pen = r.tot_aug ? r.p_aug / r.tot_aug : 0;
  const penc = r.cl_aug ? r.p_cl / r.cl_aug : 0;
  const dJun = r.p_aug - r.p_jun;
  const key = DATA.teams[cur].ml + '|' + r.rm;
  const rk = notes[key + '|r'];
  const rem = (rk != null && rk !== '') ? rk : r.remark;
  const act = notes[key + '|a'] || '';
  const focusTag = DATA.firm.focus_basis === 'prior'
    ? '<span class="ptag" title="The Aug-31 MIS reports focus only at team level; these RM figures are carried from the prior cycle pending the RM-wise split.">prior cycle</span>' : '';

  const prows = r.prod.map(p => {
    const share = r.p_aug ? p.aug / r.p_aug : 0;
    const z = p.aug === 0 ? 'z' : '';
    return `<tr><td class="l ${z}"><i class="swatch" style="background:${SERIES[p.name]};${p.aug === 0 ? 'opacity:.25' : ''}"></i>${p.name}</td>
      <td class="${z}">${p.aug ? cr(p.aug) : '&ndash;'}</td>
      <td class="${z}">${r.p_aug && p.aug > 0 ? f1(share * 100) + '%' : '&ndash;'}</td>
      <td class="${z}">${p.cl || '&ndash;'}</td></tr>`;
  }).join('');

  const clTrend = (r.cl_mar != null && r.cl_jun != null)
    ? `${r.cl_mar} &#8594; ${r.cl_jun} &#8594; ${r.cl_aug}`
    : (r.cl_jun != null ? `${r.cl_jun} &#8594; ${r.cl_aug}` : `${r.cl_aug}`);

  return `<div class="card" id="rm_${idx}">
  <div class="chd">
   <div class="rank2">${idx + 1}</div>
   <div><div class="rmn">${esc(r.rm)}</div><div class="meta">${esc(DATA.teams[cur].ml)} &middot; vintage ${r.vintage ? esc(r.vintage) : '&ndash;'} &middot; ${r.cl_aug} clients</div></div>
   ${F.t ? `<span class="pill ${F.c}" style="margin-left:8px">${F.t}</span>` : ''}
   <div class="penbig"><div><div class="pv" style="color:${penColor(pen)}">${(pen * 100).toFixed(0)}%</div><div class="pl">of book in platform</div></div></div>
  </div>
  <div class="remark"><span class="star">&#9733;</span><div class="rtx" contenteditable data-k="${esc(key)}|r">${rem}</div></div>
  <div class="grid">
   <div class="sec"><h4>Book profile</h4>
    <div class="st"><span class=k>Clients Mar&#8594;Jun&#8594;Aug</span><span class=val>${clTrend}</span></div>
    <div class="st"><span class=k>New Jun&#8594;Aug</span><span class="val ${r.new_ja > 0 ? 'pos' : 'mut'}">${r.new_ja > 0 ? '+' + r.new_ja : '0'}${r.new_aum ? ` <span class=mut>(&#8377;${cr(r.new_aum)}Cr)</span>` : ''}</span></div>
    <div class="st"><span class=k>Above &#8377;50L</span><span class=val>${r.g50}</span></div>
    <div class="st"><span class=k>Below &#8377;50L</span><span class=val>${r.l50}</span></div>
   </div>
   <div class="sec"><h4>Total AUM (&#8377;Cr)</h4>
    <div class="st"><span class=k>Mar 31</span><span class=val>${cr(r.tot_mar)}</span></div>
    <div class="st"><span class=k>Jun 30</span><span class=val>${cr(r.tot_jun)}</span></div>
    <div class="st"><span class=k>Aug 31</span><span class="val big">${cr(r.tot_aug)}</span></div>
    <div class="trend"><span class=mut style="font-size:10px">Mar&#8594;Aug</span>${arrow(r.tot_aug - r.tot_mar)}<span class="a ${r.tot_aug - r.tot_mar >= 0 ? 'pos' : 'neg'}">${signed(r.tot_aug - r.tot_mar)}</span></div>
   </div>
   <div class="sec"><h4>Platform penetration</h4>
    <div class="st"><span class=k>Platform Mar</span><span class=val>${cr(r.p_mar)}</span></div>
    <div class="st"><span class=k>Platform Jun</span><span class=val>${cr(r.p_jun)}</span></div>
    <div class="st"><span class=k>Platform Aug</span><span class="val big">${cr(r.p_aug)}</span></div>
    <div class="st"><span class=k>% of total AUM</span><span class="val" style="color:${penColor(pen)}">${f1(pen * 100)}%</span></div>
    <div class="st"><span class=k>Platform clients</span><span class=val>${r.p_cl} / ${r.cl_aug}</span></div>
    <div class="st"><span class=k>% clients on platform</span><span class=val>${(penc * 100).toFixed(0)}%</span></div>
    <div class="trend"><span class=mut style="font-size:10px">Jun&#8594;Aug</span>${arrow(dJun)}<span class="a ${dJun >= 0 ? 'pos' : 'neg'}">${signed(dJun)}</span></div>
   </div>
   <div class="sec"><h4>Product-wise platform &middot; Aug-31</h4>
    <table class="ptab"><thead><tr><th class=l>Product</th><th>&#8377;Cr</th><th>% plat</th><th>Cl.</th></tr></thead>
    <tbody>${prows}</tbody></table>
    <div class="st" style="margin-top:6px"><span class=k>Products held (of 4)</span><span class=val>${r.core_pos}</span></div>
    ${r.recon_uplift ? `<div class="st"><span class=k>incl. RM-level recon</span><span class="val mut">${signed(r.recon_uplift, 2)}</span></div>` : ''}
   </div>
   <div class="sec"><h4>Focussed product${focusTag}</h4>
    <div class="st"><span class=k>Focus Mar</span><span class=val>${cr(r.f_mar)}</span></div>
    <div class="st"><span class=k>Focus Aug</span><span class="val big">${cr(r.f_aug)}</span></div>
    <div class="st"><span class=k>% of total AUM</span><span class=val>${r.tot_aug ? (r.f_aug / r.tot_aug * 100).toFixed(2) + '%' : '&ndash;'}</span></div>
    <div class="st"><span class=k>Focus clients</span><span class=val>${r.f_cl || 0}</span></div>
    <div class="st"><span class=k>Focus + Platform cl.</span><span class="val ${r.cl_focplat > 0 ? 'pos' : 'mut'}">${r.cl_focplat}</span></div>
   </div>
  </div>
  <div class="act"><span class="lbl">Action</span><div class="inp" contenteditable data-k="${esc(key)}|a">${act}</div></div>
 </div>`;
}

/* ---------- desk panel ---------- */
function panel() {
  const t = DATA.teams[cur];
  const pen = t.tot_aug ? t.p_aug / t.tot_aug : 0;
  const dJun = t.p_aug - t.p_jun;
  let h = `<div class="thead"><div><div class="nm">${esc(t.ml)}</div>
    <div class="sb">Firm rank #${t.rank} of ${DATA.teams.length} by platform AUM &middot; ${t.rms} RM${t.rms === 1 ? '' : 's'} &middot; ${n0(t.cl_aug)} clients${t.team8 && t.team8 !== t.ml ? ` &middot; reports into the ${esc(t.team8)} team` : ''}</div></div>
   <div class="tk">
    <div class="col"><div class="v">&#8377;${cr(t.tot_aug)}<span class=u>Cr</span></div><div class="l">Total book</div></div>
    <div class="col"><div class="v">&#8377;${cr(t.p_aug)}<span class=u>Cr</span></div><div class="l">Platform</div></div>
    <div class="col"><div class="v" style="color:${dJun >= 0.005 ? '#8FE3AE' : (dJun < -0.005 ? '#FFB3A8' : '#C9CDF0')}">${dJun >= 0 ? '+' : '&minus;'}${cr(Math.abs(dJun))}<span class=u>Cr</span></div><div class="l">&#916; vs Jun</div></div>
    <div class="col"><div class="v" style="color:var(--amber)">${f1(pen * 100)}%</div><div class="l">Penetration</div></div>
    <div class="col"><div class="v">${t.p_cl}/${n0(t.cl_aug)}</div><div class="l">Plat. clients</div></div>
    <div class="col"><div class="v">&#8377;${cr(t.f_aug)}<span class=u>Cr</span></div><div class="l">Focus</div></div>
   </div></div>`;

  h += deltaStrip(t);
  if (t.f_unattr) {
    const c = t.team8_focus || {};
    const scope = c.desks > 1
      ? `the whole ${esc(c.label)} team` : `the ${esc(c.label)} team`;
    h += `<div class="fig" style="padding:10px 14px"><div class="sub" style="margin:0">
      <b>Focus &#8377;${cr0(t.f_aug)}Cr</b> on this desk includes
      <span class="unattr">&#8377;${cr0(t.f_unattr)}Cr that cannot be attributed to an individual RM</span>.
      The Aug-31 MIS reports focus only for ${scope} &mdash; &#8377;${cr0(c.actual)}Cr against a
      &#8377;${cr0(c.goal)}Cr Q2 goal &mdash; and the per-RM figures account for
      &#8377;${cr0(c.covered)}Cr of it. The &#8377;${cr(t.f_unattr)}Cr balance is shown here rather than
      spread across RMs on a guess.</div></div>`;
  }
  h += `<div class="rmidx">` + t.rows.map((r, i) =>
    `<span class="chip" onclick="document.getElementById('rm_${i}').scrollIntoView({behavior:'smooth',block:'start'})">${esc(r.rm)}</span>`).join('') + `</div>`;
  h += rmBars(t);
  h += t.rows.map((r, i) => card(r, i)).join('');
  return h;
}

/* ---------- QC panel ---------- */
function qcPanel() {
  const suites = QC.suites.map(s =>
    `<div class="s"><div class="k">${esc(s.name)}</div><div class="v ${s.fail ? 'no' : 'ok'}">${s.pass}/${s.total}</div></div>`).join('');
  const tie = QC.ties.map(t => `<tr><td>${esc(t.name)}</td><td class="n">${esc(t.computed)}</td>
      <td class="n">${esc(t.target)}</td><td>${esc(t.source)}</td>
      <td class="${t.ok ? 'ok' : 'no'}">${t.ok ? esc(t.tie) : 'FAIL'}</td></tr>`).join('');
  const samp = QC.sample.map(s => `<tr><td>${esc(s.rm)}</td><td>${esc(s.ml)}</td>
      <td class="n">${cr(s.tot_aug)}</td><td class="n">${s.cl_aug}</td><td class="n">${cr(s.p_aug)}</td>
      <td class="n">${s.p_cl}</td><td class="n">${s.g50}</td><td class="n">${s.l50}</td>
      <td class="${s.ok ? 'ok' : 'no'}">${s.ok ? 'match' : 'FAIL'}</td></tr>`).join('');
  const varr = QC.variance.map(v => `<tr><td>${esc(v.metric)}</td><td class="n">${esc(v.prior)}</td>
      <td class="n">${esc(v.now)}</td><td class="n">${esc(v.delta)}</td></tr>`).join('');
  const stale = QC.stale.map(s => `<tr><td>${esc(s.block)}</td><td>${esc(s.would_inject)}</td>
      <td>${esc(s.truth)}</td><td>${esc(s.instead)}${s.note ? `<br><span class="unattr">${esc(s.note)}</span>` : ''}</td></tr>`).join('');
  const desks = DATA.teams.map(d => `<tr><td>#${d.rank} ${esc(d.ml)}</td><td class="n">${d.rms}</td>
      <td class="n">${cr(d.tot_aug)}</td><td class="n">${n0(d.cl_aug)}</td><td class="n">${cr(d.p_mar)}</td>
      <td class="n">${cr(d.p_jun)}</td><td class="n">${cr(d.p_aug)}</td><td class="n">${d.p_cl}</td>
      <td class="n">${f1(d.p_aug / d.tot_aug * 100)}%</td><td class="n">${cr(d.f_aug)}</td></tr>`).join('');
  const F = DATA.firm;

  return `<div class="qc">
   <h2>Reconciliation</h2>
   <div class="lede">Built from <b>${esc(QC.source)}</b> on ${esc(QC.built)}.
     Every figure below is asserted against a value recomputed row-by-row from the raw
     <code>aum</code> and <code>platform</code> sheets &mdash; never against a workbook summary row,
     several of which are stale. The build aborts if any check fails, so a dashboard that
     exists is a dashboard that ties.</div>
   <div class="suite">${suites}</div>

   <h2>Cross-check &mdash; firm tie-outs</h2>
   <div class="lede">Computed from the 73 RM rows, compared to the independent raw-sheet total.</div>
   <table class="qctab"><thead><tr><th>Measure</th><th class="n">Built</th><th class="n">Raw source</th>
     <th>Where the raw figure comes from</th><th>Tie</th></tr></thead><tbody>${tie}</tbody></table>

   <h2>Desk roll-up</h2>
   <div class="lede">Each desk is the sum of its own RM rows; the desks sum to the firm.
     Platform Mar/Jun are period-end actuals, Aug is live.</div>
   <table class="qctab"><thead><tr><th>Desk</th><th class="n">RMs</th><th class="n">AUM</th>
     <th class="n">Clients</th><th class="n">Plat Mar</th><th class="n">Plat Jun</th><th class="n">Plat Aug</th>
     <th class="n">Plat cl</th><th class="n">Pen.</th><th class="n">Focus</th></tr></thead>
     <tbody>${desks}
     <tr><td><b>FIRM</b></td><td class="n"><b>${F.rms}</b></td><td class="n"><b>${cr(F.tot_aug)}</b></td>
       <td class="n"><b>${n0(F.cl_aug)}</b></td><td class="n"><b>${cr(F.p_mar)}</b></td>
       <td class="n"><b>${cr(F.p_jun)}</b></td><td class="n"><b>${cr(F.p_aug)}</b></td>
       <td class="n"><b>${F.p_cl}</b></td><td class="n"><b>${f1(F.p_aug / F.tot_aug * 100)}%</b></td>
       <td class="n"><b>${cr(F.f_aug)}</b></td></tr></tbody></table>

   <h2>Random check &mdash; ${QC.sample.length} RMs re-derived from raw rows</h2>
   <div class="lede">A seeded sample (seed ${esc(QC.seed)}). For each RM the build re-filters the raw
     client and platform rows one at a time, with no SUMIFS-equivalent shortcut, and compares
     every field including the four product values and their client counts.</div>
   <table class="qctab"><thead><tr><th>RM</th><th>Desk</th><th class="n">AUM</th><th class="n">Clients</th>
     <th class="n">Platform</th><th class="n">Plat cl</th><th class="n">&#8805;50L</th><th class="n">&lt;50L</th>
     <th>Re-derived</th></tr></thead><tbody>${samp}</tbody></table>

   <h2>Movement vs the previous dashboard</h2>
   <table class="qctab"><thead><tr><th>Measure</th><th class="n">Prior (1.1)</th>
     <th class="n">Aug-31 MIS</th><th class="n">Change</th></tr></thead><tbody>${varr}</tbody></table>

   <h2>Source blocks deliberately not used</h2>
   <div class="lede">These blocks in the workbook look authoritative but are stale typed constants.
     Each was verified against a raw recomputation before being excluded.</div>
   <table class="qctab"><thead><tr><th>Block</th><th>What it would have injected</th>
     <th>Actual</th><th>Used instead</th></tr></thead><tbody>${stale}</tbody></table>
  </div>`;
}

/* ---------- chrome ---------- */
function tabs() {
  const desk = DATA.teams.map((t, i) =>
    `<div class="tab ${i === cur ? 'active' : ''}" onclick="go(${i})">
       <span class=rk>#${t.rank}</span><span class=mini>${esc(t.ml)}</span></div>`).join('');
  const qc = `<div class="tabsep"></div><div class="tab ${cur === QC_TAB ? 'active' : ''}" onclick="go(${QC_TAB})">
      <span class=mini>Data QC</span><span class=rk>${QC.total_pass}/${QC.total}</span></div>`;
  document.getElementById('tabs').innerHTML = desk + qc;
}
function go(i) { cur = i; render(); window.scrollTo(0, 0); }

function bind() {
  document.querySelectorAll('[contenteditable]').forEach(el => {
    el.addEventListener('blur', () => {
      notes[el.dataset.k] = el.innerHTML.trim();
      try { localStorage.setItem(LS, JSON.stringify(notes)); } catch (e) {}
    });
  });
}
function reset() {
  if (confirm('Clear all edited remarks and actions?')) {
    notes = {}; localStorage.removeItem(LS); render();
  }
}

function render() {
  fks(); tabs();
  const head = document.getElementById('firmline');
  const body = document.getElementById('panel');
  if (cur === QC_TAB) {
    head.innerHTML = '';
    body.innerHTML = qcPanel();
  } else {
    head.innerHTML = `<div class="figgrid">${trendChart()}${mixChart()}</div>`;
    body.innerHTML = panel();
  }
  bind();
  bindTips(document.body);
}
render();
