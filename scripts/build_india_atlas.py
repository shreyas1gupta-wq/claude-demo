"""Builds docs/learn/artifacts/india-property-atlas.html from research/india_thresholds.json
(the vaulted JST base rate, desk-grade) plus the sourced city figures carried in
research/notes/india-dossiers/. Regenerates from those files, never from memory."""
import json, math, pathlib

J = json.load(open("/home/user/claude-demo/research/india_thresholds.json"))
CN = json.load(open("/home/user/claude-demo/research/china_baserate.json"))
OUT = pathlib.Path("/home/user/claude-demo/docs/learn/artifacts/india-property-atlas.html")

# ---------- chart 1: the micro-market price gradient, log scale ----------
# (city, label, price psf, tier-band) — every figure from a committed dossier
G = [("Dholera", "Dholera SIR land", 1100, "land"),
     ("Ahmedabad", "Naroda", 2500, "out"), ("Hyderabad", "Uppal / Medchal", 3550, "out"),
     ("Lucknow", "Sitapur Rd", 4100, "out"), ("Pune", "Chakan / Talegaon", 5000, "out"),
     ("Mumbai", "Karjat", 5250, "out"), ("Lucknow", "Gomti Ngr Ext", 10200, "mid"),
     ("Ahmedabad", "GIFT City", 10400, "mid"), ("Hyderabad", "Kokapet (built)", 11900, "mid"),
     ("Mumbai", "Ulwe (closings)", 11500, "out"), ("Mumbai", "Ulwe (asking)", 15000, "out"),
     ("Ahmedabad", "Satellite", 14000, "in"), ("Mumbai", "Powai / Chembur", 22000, "mid"),
     ("Pune", "Koregaon Park", 27500, "in"), ("Mumbai", "Vashi / Nerul", 30500, "mid"),
     ("Hyderabad", "Banjara Hills", 31000, "in"), ("Hyderabad", "Kokapet LAND", 31500, "land"),
     ("Mumbai", "Andheri West", 39000, "mid"), ("Mumbai", "Worli / Lower Parel", 60000, "in"),
     ("Mumbai", "Malabar Hill", 90000, "in"), ("Mumbai", "Carmichael Road", 180500, "in")]
G.sort(key=lambda r: r[2])
W, H, PL, PR, PT, PB = 660, 470, 150, 56, 26, 44
lo, hi = 900, 220000
sx = lambda v: PL + (math.log10(v) - math.log10(lo)) / (math.log10(hi) - math.log10(lo)) * (W - PL - PR)
rowh = (H - PT - PB) / len(G)
CLS = {"in": "bin", "mid": "bmid", "out": "bout", "land": "bland"}
g = []
for v in (1000, 3000, 10000, 30000, 100000, 200000):
    g.append(f'<line x1="{sx(v):.1f}" y1="{PT-6}" x2="{sx(v):.1f}" y2="{H-PB}" class="gr"/>'
             f'<text x="{sx(v):.1f}" y="{H-PB+16}" class="ax" text-anchor="middle">'
             f'{"₹"+format(v,",")}</text>')
for i, (city, lab, p, band) in enumerate(G):
    y = PT + i * rowh + rowh / 2
    g.append(f'<line x1="{PL}" y1="{y:.1f}" x2="{sx(p):.1f}" y2="{y:.1f}" class="barln"/>'
             f'<circle cx="{sx(p):.1f}" cy="{y:.1f}" r="4.2" class="{CLS[band]}">'
             f'<title>{city} — {lab}: ₹{p:,}/sqft</title></circle>'
             f'<text x="{PL-8}" y="{y+3.6:.1f}" class="rl" text-anchor="end">{lab}</text>'
             f'<text x="{sx(p)+9:.1f}" y="{y+3.6:.1f}" class="rv">₹{p:,}</text>')
SC1 = (f'<svg viewBox="0 0 {W} {H}" class="chart" role="img" aria-label="Log-scale price per square '
       f'foot across 21 Indian micro-markets, from Dholera land to Carmichael Road">' + "".join(g)
       + f'<text x="{(PL+W-PR)/2:.0f}" y="{H-6}" class="axt" text-anchor="middle">'
       f'price per sq ft, log scale (asking unless marked)</text></svg>')

# ---------- chart 2: the yield placement against the base rate ----------
W2, H2, P2L, P2R = 660, 250, 60, 30
ymin, ymax = 0, 9
sy2 = lambda v: P2L + (v / ymax) * (W2 - P2L - P2R)
tr = CN["modern_era"]["yd_trough"]
pk = CN["modern_era"]["yd_peak"]
y = [f'<rect x="{sy2(0):.1f}" y="52" width="{sy2(pk)-sy2(0):.1f}" height="34" class="zpk"/>',
     f'<rect x="{sy2(pk):.1f}" y="52" width="{sy2(tr)-sy2(pk):.1f}" height="34" class="zmid"/>',
     f'<rect x="{sy2(tr):.1f}" y="52" width="{sy2(ymax)-sy2(tr):.1f}" height="34" class="ztr"/>',
     f'<text x="{sy2(pk/2):.1f}" y="45" class="zl" text-anchor="middle">below the median PEAK yield</text>',
     f'<text x="{sy2((pk+tr)/2):.1f}" y="45" class="zl" text-anchor="middle">peak→trough band</text>',
     f'<text x="{sy2((tr+ymax)/2):.1f}" y="45" class="zl" text-anchor="middle">at or past the median TROUGH</text>',
     f'<line x1="{sy2(pk):.1f}" y1="46" x2="{sy2(pk):.1f}" y2="92" class="med"/>',
     f'<line x1="{sy2(tr):.1f}" y1="46" x2="{sy2(tr):.1f}" y2="92" class="med"/>']
for v in range(0, 10):
    y.append(f'<line x1="{sy2(v):.1f}" y1="92" x2="{sy2(v):.1f}" y2="98" class="gr"/>'
             f'<text x="{sy2(v):.1f}" y="112" class="ax" text-anchor="middle">{v}%</text>')
MK = [("Mumbai / Bandra", 2.0, 4.0, 130, "cn"), ("Hyderabad IT corridor", 2.5, 4.2, 152, "cn"),
      ("Lucknow", 3.0, 3.0, 174, "cn"), ("Ahmedabad citywide", 3.9, 3.9, 196, "cn"),
      ("Kochi Kakkanad", 4.6, 6.0, 218, "ok"), ("Indore Nipania", 8.0, 8.0, 240, "ok")]
for lab, a, b, yy, cls in MK:
    if b > a:
        y.append(f'<line x1="{sy2(a):.1f}" y1="{yy}" x2="{sy2(b):.1f}" y2="{yy}" class="rng {cls}"/>')
    y.append(f'<circle cx="{sy2(a):.1f}" cy="{yy}" r="3.6" class="dot {cls}"/>'
             f'<circle cx="{sy2(b):.1f}" cy="{yy}" r="3.6" class="dot {cls}"/>'
             f'<text x="{sy2(max(b,a))+9:.1f}" y="{yy+3.6}" class="rv">{lab}</text>')
y.append(f'<line x1="{sy2(1.75):.1f}" y1="120" x2="{sy2(1.75):.1f}" y2="250" class="cnl2"/>'
         f'<text x="{sy2(1.75)-6:.1f}" y="132" class="cnt" text-anchor="end">China tier-1 at its 2021 peak</text>')
SC2 = (f'<svg viewBox="0 0 {W2} 262" class="chart" role="img" aria-label="Indian city gross rental '
       f'yields placed against the international peak and trough yield bands">' + "".join(y) + "</svg>")

d1 = J["IN-D1"]["by_threshold"]
era = J["IN-D1"]["era"]
c2 = J["IN-D2_clean"]

html = f"""<title>India Property Atlas</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700&family=Source+Sans+3:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root {{
  --bg:#f7f5f0; --panel:#fdfcf9; --ink:#1f2426; --ink2:#4d5356; --mut:#848a8d;
  --line:#e4e1d8; --s1:#1d6b5f;
  --bad:#a8352a; --badbg:#f8e8e5; --good:#1c6e4a; --goodbg:#e5f2ea;
  --amber:#8a5f00; --amberbg:#f6eed6; --gate:#55647f; --gatebg:#e7ebf2;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg:#13171a; --panel:#1b2024; --ink:#e6e9ea; --ink2:#a6acaf; --mut:#7a8084;
  --line:#2d3338; --s1:#4fb3a1;
  --bad:#dd7168; --badbg:#36211f; --good:#59b986; --goodbg:#1a3025;
  --amber:#d4a33a; --amberbg:#31260e; --gate:#8c9ec0; --gatebg:#1e242d;
}} }}
:root[data-theme="dark"] {{
  --bg:#13171a; --panel:#1b2024; --ink:#e6e9ea; --ink2:#a6acaf; --mut:#7a8084;
  --line:#2d3338; --s1:#4fb3a1;
  --bad:#dd7168; --badbg:#36211f; --good:#59b986; --goodbg:#1a3025;
  --amber:#d4a33a; --amberbg:#31260e; --gate:#8c9ec0; --gatebg:#1e242d;
}}
* {{ box-sizing:border-box; }}
body {{ background:var(--bg); color:var(--ink); font-family:"Source Sans 3",system-ui,sans-serif;
  font-size:15px; line-height:1.55; margin:0; }}
.wrap {{ max-width:1120px; margin:0 auto; padding-block:30px 64px; padding-left:20px; padding-right:20px; }}
h1 {{ font-family:"Archivo",system-ui,sans-serif; font-weight:700; font-size:clamp(26px,4.6vw,40px);
  line-height:1.08; letter-spacing:-.02em; margin:0 0 10px; text-wrap:balance; }}
h2 {{ font-family:"Archivo",system-ui,sans-serif; font-weight:600; font-size:19px; margin:0 0 6px;
  letter-spacing:-.01em; text-wrap:balance; }}
h3 {{ font-family:"Archivo",system-ui,sans-serif; font-weight:600; font-size:15px; margin:20px 0 4px; }}
p {{ margin:6px 0 0; max-width:76ch; }}
.sub {{ color:var(--ink2); font-size:14.5px; max-width:82ch; }}
.eyebrow {{ font-family:"Archivo"; font-size:11.5px; font-weight:600; letter-spacing:.14em;
  text-transform:uppercase; color:var(--s1); margin:0 0 8px; }}
header {{ border-bottom:2px solid var(--ink); padding-bottom:20px; margin-bottom:22px; }}
.prov {{ display:flex; flex-wrap:wrap; gap:6px; margin-top:14px; }}
.badge {{ font-family:"IBM Plex Mono",monospace; font-size:11px; background:var(--gatebg);
  color:var(--gate); padding:3px 9px; border-radius:3px; }}
.grade {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:14px; margin:18px 0 4px; }}
.gr1,.gr2 {{ padding:14px 16px; border-radius:5px; font-size:14px; }}
.gr1 {{ background:var(--goodbg); border-left:3px solid var(--good); }}
.gr2 {{ background:var(--amberbg); border-left:3px solid var(--amber); }}
.gr1 b,.gr2 b {{ font-family:"Archivo"; display:block; margin-bottom:3px; }}
.tiles {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(232px,1fr)); gap:1px;
  background:var(--line); border:1px solid var(--line); border-radius:6px; overflow:hidden; margin:24px 0; }}
.t {{ background:var(--panel); padding:16px 18px; }}
.t .k {{ font-family:"Archivo"; font-size:12px; font-weight:600; letter-spacing:.05em;
  text-transform:uppercase; color:var(--mut); }}
.t .v {{ font-family:"IBM Plex Mono",monospace; font-size:26px; font-weight:500; line-height:1.15;
  margin:5px 0 4px; font-variant-numeric:tabular-nums; }}
.t .d {{ font-size:13px; color:var(--ink2); }}
section {{ margin:34px 0 0; }}
.panel {{ background:var(--panel); border:1px solid var(--line); border-radius:6px; padding:20px 22px; }}
.chartwrap {{ overflow-x:auto; margin:14px 0 4px; }}
svg.chart {{ width:100%; min-width:580px; height:auto; display:block; }}
.gr {{ stroke:var(--line); stroke-width:1; }}
.ax {{ fill:var(--mut); font-family:"IBM Plex Mono",monospace; font-size:10.5px; }}
.axt {{ fill:var(--ink2); font-size:12px; }}
.barln {{ stroke:var(--line); stroke-width:1; }}
.rl {{ fill:var(--ink2); font-size:11px; }}
.rv {{ fill:var(--ink); font-family:"IBM Plex Mono",monospace; font-size:10.5px; }}
.bin {{ fill:var(--bad); }} .bmid {{ fill:var(--s1); }} .bout {{ fill:var(--gate); }}
.bland {{ fill:var(--amber); }}
.zpk {{ fill:var(--badbg); }} .zmid {{ fill:var(--amberbg); }} .ztr {{ fill:var(--goodbg); }}
.zl {{ fill:var(--ink2); font-size:10.5px; }}
.med {{ stroke:var(--ink); stroke-width:1.4; }}
.rng {{ stroke-width:2.4; }} .rng.cn {{ stroke:var(--bad); }} .rng.ok {{ stroke:var(--good); }}
.dot.cn {{ fill:var(--bad); }} .dot.ok {{ fill:var(--good); }}
.cnl2 {{ stroke:var(--gate); stroke-width:1.6; stroke-dasharray:4 3; }}
.cnt {{ fill:var(--gate); font-size:10.5px; font-weight:600; font-family:"Archivo"; }}
.tbl {{ overflow-x:auto; margin:14px 0 0; }}
table {{ border-collapse:collapse; width:100%; min-width:620px; font-size:13.5px; }}
th,td {{ text-align:right; padding:7px 10px; border-bottom:1px solid var(--line);
  vertical-align:top; font-variant-numeric:tabular-nums; }}
th {{ font-family:"Archivo"; font-weight:600; font-size:12px; color:var(--mut);
  text-transform:uppercase; letter-spacing:.04em; }}
th:first-child,td:first-child {{ text-align:left; }}
td.mono,.mono {{ font-family:"IBM Plex Mono",monospace; }}
.pos {{ color:var(--good); font-weight:600; }} .neg {{ color:var(--bad); font-weight:600; }}
.tag {{ font-family:"IBM Plex Mono",monospace; font-size:10px; padding:1px 6px; border-radius:3px;
  background:var(--gatebg); color:var(--gate); white-space:nowrap; }}
.tag.desk {{ background:var(--goodbg); color:var(--good); }}
.tag.snip {{ background:var(--amberbg); color:var(--amber); }}
.tag.bad {{ background:var(--badbg); color:var(--bad); }}
.warn {{ background:var(--amberbg); color:var(--amber); border-radius:5px; padding:13px 16px;
  font-size:13.5px; margin:16px 0 0; max-width:94ch; }}
.note {{ font-size:13px; color:var(--mut); max-width:98ch; margin-top:10px; }}
ul,ol {{ margin:8px 0 0; padding-left:20px; }} li {{ margin:5px 0; max-width:90ch; }}
.legend {{ display:flex; gap:15px; flex-wrap:wrap; font-size:12.5px; color:var(--ink2); margin-top:6px; }}
.sw {{ display:inline-block; width:9px; height:9px; border-radius:50%; margin-right:5px; }}
</style>
<div class="wrap">
<header>
<p class="eyebrow">The Cycle Program · IN programme</p>
<h1>India Property Atlas</h1>
<p class="sub">Seven cities, twenty-one micro-markets, five screened candidates and the two
policy-created markets — each placed against a base rate computed from 48 real house-price crashes
across 18 countries and 150 years. Built as the India counterpart to the desk's China programme, and
deliberately split the same way: what can be computed from vaulted data is kept separate from what
could only be researched.</p>
<div class="prov">
<span class="badge">ledger IN-D1..IN-D2</span><span class="badge">census 1,389 → 1,399</span>
<span class="badge">9 cited dossiers</span><span class="badge">4 cells verified exact</span>
<span class="badge">2026-09-11</span></div>
<div class="grade">
<div class="gr1"><b>Half A — desk-grade <span class="tag desk">VAULT</span></b>
IN-D1/IN-D2 pre-registered before any number was computed, on the vaulted, sha256-manifested
JST panel. Reproducible via <span class="mono">scripts/analyze_india_thresholds.py</span>.</div>
<div class="gr2"><b>Half B — indicative only <span class="tag snip">SNIPPET</span></b>
<b>The vault contains NO India property series and NO India CPI</b> — checked, not assumed. Every
Indian figure here is search-snippet sourced, and <b>no city has a repeat-sales or
transaction-weighted index</b>, so every “+X%” is an asking-price comparison. Research direction,
not evidence.</div>
</div>
</header>

<div class="tiles">
<div class="t"><div class="k">“20% over 5 years”, as cumulative</div><div class="v">3.71%/yr</div>
<div class="d">= <b>−0.75%/yr real</b> at 4.5% CPI, and 68pp of cumulative return behind the desk's
own standing book. A bar that loses money.</div></div>
<div class="t"><div class="k">“20% over 5 years”, as CAGR</div><div class="v">0 of 884</div>
<div class="d">Post-1970 five-year windows clearing <b>20%/yr real</b> in 18 countries. It has never
happened in the modern era of this panel.</div></div>
<div class="t"><div class="k">Hot markets stay hot</div><div class="v">+9.65%/yr</div>
<div class="d">Next-5y real return <i>after</i> a 15%/yr window — my mean-reversion prior
<b>missed</b>. With ~2× crash odds alongside it.</div></div>
<div class="t"><div class="k">Indian REITs vs the G-sec</div><div class="v">4.8–6.2% vs 7.0%</div>
<div class="d">Distribution yields all sit <b>below the sovereign</b>. The sleeve is not compensated
at current prices.</div></div>
</div>

<section>
<h2>1 · The bar, priced against 150 years</h2>
<p class="sub">“Grow more than 20% for the next five years” is two different questions and they point
opposite ways. The vaulted panel answers both, which is the only part of this page that is
desk-grade.</p>
<div class="tbl"><table>
<thead><tr><th>Threshold, real</th><th>Frequency of 5-yr windows</th><th>Countries</th>
<th>Next-5yr real return</th><th>Crash lift</th></tr></thead>
<tbody>
<tr><td class="mono">≥ 5%/yr</td><td class="mono">{d1['5']['freq']:.2%}</td>
<td class="mono">{d1['5']['countries']}</td><td class="mono">{d1['5']['fwd']:+.2f}%</td>
<td class="mono">{d1['5']['lift']:.2f}×</td></tr>
<tr><td class="mono">≥ 10%/yr</td><td class="mono">{d1['10']['freq']:.2%}</td>
<td class="mono">{d1['10']['countries']}</td><td class="mono">{d1['10']['fwd']:+.2f}%</td>
<td class="mono">{d1['10']['lift']:.2f}×</td></tr>
<tr><td class="mono">≥ 15%/yr</td><td class="mono">{d1['15']['freq']:.2%}</td>
<td class="mono">{d1['15']['countries']}</td><td class="mono pos">{d1['15']['fwd']:+.2f}%</td>
<td class="mono">{d1['15']['lift']:.2f}×</td></tr>
<tr><td class="mono"><b>≥ 20%/yr</b></td><td class="mono">{d1['20']['freq']:.2%}</td>
<td class="mono"><b>{d1['20']['countries']}</b></td><td class="mono pos">{d1['20']['fwd']:+.2f}%</td>
<td class="mono">{d1['20']['lift']:.2f}×</td></tr>
</tbody></table></div>
<h3>Three things fall out, and two of them are bars I got wrong</h3>
<ul>
<li><b>Post-1970, zero of {era['post1970']['n']:,} windows cleared 20%/yr real</b> — against
{era['pre1970']['f20']:.2%} pre-1970, and those pre-war extremes are currency artifacts (the panel
maximum is Germany 1927 at +89%/yr). The post-1970 maximum is <b>Ireland 1999 at +17.25%/yr real —
and Ireland 2006 is the worst modern bust in the desk's own episode list at −55.7%.</b> The fastest
modern boom and the worst modern bust are the same country, seven years apart.</li>
<li><b>My mean-reversion prior MISSED.</b> The next five years after a 15%/yr window returned
<b>+9.65%/yr real</b>, and +11.16% after a 20%/yr one. Property momentum beats mean reversion at
this horizon — so a hot Indian micro-market should <i>not</i> be dismissed on
reversion grounds. It simultaneously carries roughly <b>2× crash odds</b>, which makes the correct
treatment ride-it-but-size-it rather than in-or-out.</li>
<li><b>The money-illusion prior also missed, usefully.</b> Excluding hyperinflation windows, only
<b>{c2['illusion_share']:.1%}</b> of ≥20%/yr <i>nominal</i> windows were real-negative, and inflation
supplied {(1 - c2['hot_real_mean']/c2['hot_nom_mean'])*100:.0f}% rather than nearly all of the
headline. Indian nominal price talk carries more real information than assumed.</li>
</ul>
<div class="warn"><b>So the honest answer to the question as asked.</b> Read as 20% cumulative, the
bar is cleared by about half of all windows and loses money in real terms — naming five cities that
clear it is not an investment case. Read as 20% CAGR, it is a ~1-in-50 outcome for a national market
and unprecedented in real terms post-1970. City dispersion does exceed national dispersion — China's
own Wenzhou at −63% and Langfang at over −50% prove it in both directions — so an Indian city
<i>can</i> do it. But it is a <b>bubble-velocity call, not a growth forecast</b>, and this page
presents it as one.</div>
</section>

<section>
<h2>2 · Twenty-one micro-markets, on one log scale</h2>
<p class="sub">The inner-to-outer gradient the principal asked for, across all seven cities at once.
A log scale is the only honest way to show it: the span is roughly <b>160× from Dholera land to
Carmichael Road</b>, and a linear axis would compress everything below Mumbai into a single line.</p>
<div class="chartwrap">{SC1}</div>
<div class="legend"><span><span class="sw" style="background:var(--bad)"></span>inner /
premium</span><span><span class="sw" style="background:var(--s1)"></span>middle</span>
<span><span class="sw" style="background:var(--gate)"></span>outer / periphery</span>
<span><span class="sw" style="background:var(--amber)"></span>raw land</span></div>
<h3>What the gradient shows that a city-level table cannot</h3>
<ul>
<li><b>MMR is two gradients hinged at the harbour, not one.</b> Navi Mumbai's core (Vashi/Nerul,
₹28–33k) prices closer to the western suburbs than to its own southern end (Ulwe/Panvel, ₹13–17k).</li>
<li><b>Hyderabad's Kokapet land trades above its own buildings</b> — about ₹31,500/sqft of raw land
against ₹11,900/sqft for built flats in the same micro-market, off a government auction at
₹137.25cr/acre. That is precisely the Chinese 面粉贵过面包 (“flour costlier than bread”) pattern the
desk documented in its China land dossier, now appearing in India independently.</li>
<li><b>Asking is not closing.</b> Ulwe asking prices (₹13.5–16.6k) run <b>25–30% above</b> what
actually registers (₹10.5–12.5k). Both points are plotted so the gap is visible rather than averaged
away.</li>
<li>Tier-2 inner premium (Ahmedabad's Satellite at ₹14,000) sits <i>below</i> Mumbai's outer
periphery pricing — the tier gradient dominates the inner/outer gradient.</li>
</ul>
</section>

<section>
<h2>3 · The law this programme kept rediscovering: announcement moves the price, completion confirms it</h2>
<p class="sub">Three agents working independently on different cities reached the same finding, which
is the strongest evidence on this page and the one that should change behaviour.</p>
<div class="tbl"><table>
<thead><tr><th>Catalyst</th><th>Status</th><th>The price move</th><th>When it happened</th></tr></thead>
<tbody>
<tr><td>Navi Mumbai International Airport</td><td class="mono">Commercial ops 25-Dec-2025;
international 15-Jul-2026</td><td class="mono">Panvel <b>+76%</b> since 2021</td>
<td class="neg">Mostly <b>before the first flight</b></td></tr>
<tr><td>Jewar / Noida International Airport</td><td class="mono">Flying 15-Jun-2026</td>
<td class="mono">Noida belt <b>+142–158%</b>/5yr</td><td class="neg">Mostly before the first flight</td></tr>
<tr><td>Samruddhi Mahamarg (Nagpur)</td><td class="mono">Fully delivered 5-Jun-2025</td>
<td class="mono">Corridor land ≈<b>3.7×</b></td><td class="neg">Pre-completion</td></tr>
<tr><td>Delhi–Dehradun Expressway</td><td class="mono">Delivered 14-Apr-2026</td>
<td class="mono"><b>+23%</b></td><td class="neg">In the <b>9 months before</b> opening</td></tr>
<tr><td>Virar–Alibaug corridor</td><td class="mono">Barely under construction</td>
<td class="mono">Alibaug land <b>+30–35%</b></td><td class="neg">On anticipation alone</td></tr>
<tr><td>Completed MMR metro / Atal Setu / Coastal Rd</td><td class="mono">Delivered</td>
<td class="mono">8–15%/yr <i>continuing</i></td><td class="pos">After — but smaller</td></tr>
</tbody></table></div>
<div class="warn"><b>The uncomfortable corollary, and it is the single most decision-relevant
sentence on this page.</b> Evidence that a catalyst has been <i>delivered</i> is evidence that the
re-rating has <i>already happened</i>. Every one of the five best-evidenced candidate cities below has
a delivered catalyst — which means the screen's own logic argues against buying the screen's own
winners. What remains after delivery is the smaller continuing premium (8–15%/yr on completed MMR
infrastructure), not the step change. The investable window is before announcement, and by
construction nobody can screen for it.</div>
</section>

<section>
<h2>4 · The five candidates, classed by what is supposed to drive them</h2>
<p class="sub">Screened on observable evidence rather than picked from intuition, and each classed by
driver — because the desk's China work established that the <b>policy-backed</b> class is the fragile
one: provincial-capital status there bought roughly double the appreciation through the boom and zero
protection in the bust.</p>
<div class="tbl"><table>
<thead><tr><th>City</th><th>Driver class</th><th>Catalyst</th><th>Status</th><th>5-yr move</th>
<th>Evidence</th></tr></thead>
<tbody>
<tr><td><b>Noida / Gr. Noida / Yamuna Expwy</b></td><td>Infrastructure</td>
<td class="mono">Jewar airport</td><td class="mono pos">Delivered 15-Jun-2026</td>
<td class="mono">+142–158%</td><td>Strong</td></tr>
<tr><td><b>Nagpur</b></td><td>Infrastructure</td><td class="mono">Samruddhi Mahamarg</td>
<td class="mono pos">Delivered 5-Jun-2025</td><td class="mono">land ≈3.7×</td><td>Strong</td></tr>
<tr><td><b>Dehradun</b></td><td>Infrastructure</td><td class="mono">Delhi–Dehradun Expwy</td>
<td class="mono pos">Delivered 14-Apr-2026</td><td class="mono">+23% pre-open</td>
<td>Strong — cleanest pre/post pair</td></tr>
<tr><td><b>Visakhapatnam</b></td><td>Infra + demand <span class="tag bad">RECLASSIFIED</span></td>
<td class="mono">Bhogapuram airport</td><td class="mono pos">Delivered 17-Aug-2026</td>
<td class="mono">—</td><td>Medium</td></tr>
<tr><td><b>Kochi</b></td><td>Infra + demand</td><td class="mono">Metro Phase 2</td>
<td class="mono">&gt;40% built</td><td class="mono">—</td>
<td>Strong — most internally consistent data</td></tr>
</tbody></table></div>
<div class="warn" style="background:var(--gatebg);color:var(--gate)"><b>A correction to my own
brief, made by the agent rather than by me.</b> I classed Visakhapatnam as policy-backed alongside
Amravati. Its “executive capital” status has in fact been <b>legislated away entirely</b>, with
Amaravati made sole and permanent AP capital around April 2026. That reclassifies Vizag to
infrastructure-plus-demand — and it cuts the other way for Amaravati, whose near-term legal position
is stronger than the policy-cities dossier implied, while the 2029 risk stays live (a sole-capital
statute and an opposition campaigning on an alternative are not contradictory).</div>
<h3>The rest of the screen, stated honestly</h3>
<ul>
<li><b>Highest credible yields</b>: Kochi's Kakkanad at 4.6–6% and Indore's Nipania to 8%. Surat's
portal-reported 11–12% is flagged as a likely single-source artifact and <b>not adopted</b>.</li>
<li><b>Weakest evidence behind the loudest narrative: Varanasi.</b> No NHB coverage, single-source
pricing throughout, and neither named catalyst confirmed delivered. The Ayodhya-analogue framing is
reasonable; the data to support it does not yet exist.</li>
<li><b>Dholera is a land-banking bet, not an investable market.</b> The Tata–PSMC fab is a real,
dated, roughly half-complete industrial delivery — but no residential absorption figure exists
anywhere, land prices are unreconciled across ₹550–1,667/sqft, and multiple sources document active
fraud risk including a Gujarat High Court land case.</li>
<li><b>GIFT City</b> has roughly doubled since 2021 (~16%/yr) on about 48% of planned space allotted,
with independent journalistic description of it emptying after working hours — anticipation ahead of
real but partial delivery.</li>
</ul>
</section>

<section>
<h2>5 · Amravati and Ayodhya — the policy-created pair</h2>
<p class="sub">Analysed separately from the growth cities on purpose, because the China base rate says
this class behaves differently. And <b>Amravati is a worse case than the Chinese one</b>: there the
capital designation was never withdrawn.</p>
<div class="tbl"><table>
<thead><tr><th></th><th>Amravati</th><th>Ayodhya</th></tr></thead>
<tbody>
<tr><td>The run-up</td><td class="mono">₹15–70 lakh/acre (2014-15) → reported ≈₹5 cr/acre by the
2018-19 peak</td><td class="mono"><b>2.2–3.5×</b> on the Nov-2019 verdict and Aug-2020 Bhoomi Pujan
alone</td></tr>
<tr><td>The shock</td><td class="mono neg"><b>Designation legally stripped for five years</b> (2019);
area sales −40 to −50%, prices ≈−25%; farmer annuities disrupted</td>
<td class="mono">By 2023 — a year <i>before</i> consecration — deed prices already ran
<b>41% to 1,235% above circle rate</b></td></tr>
<tr><td>Now</td><td class="mono">Revived 2024; sq-yd prices ≈<b>3–4×</b> (₹10–15k → ₹40–60k)</td>
<td class="mono">Post-Jan-2024 move real but <b>narrower</b> — prime frontage only</td></tr>
<tr><td>The unpriced risk</td><td class="mono neg">≈100,000 people against a 3.5m target; permanent
buildings at groundbreaking stage; <b>the same party that shelved it is campaigning for 2029 on an
alternative capital</b></td><td class="mono">The event everyone watched (Jan-2024) was the
<b>least informative moment</b> in the sequence</td></tr>
</tbody></table></div>
<div class="warn"><b>The shared risk is an absence, not a number.</b> Neither city has an independent
transaction-volume series, and every source describes the same buyer type — NRIs, developers, retail
speculators — with <b>no cash-flow-priced later-stage buyer visible anywhere</b>. The same diagnostic
that found China's institutional market marking residential at a ~5.5% cap rate while its retail
market sat at 2.0–2.6% comes back <i>empty</i> here, because there is no institutional mark at all.
Ayodhya at least has a real and growing footfall and hotel-demand base; Amravati has none. A
widely-quoted “15× in three years” Ayodhya claim traces to a developer marketing a project in the
town, states no base price, and is <b>flagged promotional and not adopted</b>.</div>
</section>

<section>
<h2>6 · Yields, and the placement that matters most</h2>
<p class="sub">The base rate says property busts historically <i>end</i> near a 5.2% gross yield and
that the median yield <i>at the peak</i> was 3.29%. Placing Indian cities on that scale is the
sharpest thing this page does — and the answer depends on which of two irreconcilable data families
is right.</p>
<div class="chartwrap">{SC2}</div>
<div class="legend"><span><span class="sw" style="background:var(--bad)"></span>at or below the
median PEAK yield</span><span><span class="sw" style="background:var(--good)"></span>at or past the
median TROUGH yield</span></div>
<h3>Two families, and which one is right decides the answer</h3>
<ul>
<li><b>Portal and broker micro-market surveys</b> put Mumbai/Bandra at 2.0–4.0%, Hyderabad's IT
corridor 2.5–4.2%, Lucknow ~3%, Ahmedabad citywide 3.9% — i.e. Indian metros sit <b>at or below the
historical PEAK yield</b>, the same zone China's tier-1 occupied at its 2021 top (~1.7–1.8%).</li>
<li><b>Global Property Guide's city cut</b> puts Delhi and Kolkata at 5.8–6.3% with a 5.16% national
blend — i.e. India sits <b>at or past the historical TROUGH yield</b>, which is the opposite
conclusion.</li>
<li>The two cannot both be right, and the gap is 2–3 percentage points on the single most
consequential number on the page. It is now the top item on the desk's India runsheet.</li>
</ul>
<div class="warn"><b>The carry test, which is unambiguous and surprising.</b> Gross yield minus the
mortgage rate runs <b>−2.0pp</b> (national blend against the best 7.10% loan rate) to <b>−5.0pp</b>
(realistic prime-urban 3–4% against a representative ~8% effective rate). <b>India's negative carry
is WIDER than China's −0.9 to −1.3pp</b> — so on the pure carry test Indian residential is
<i>less</i> attractive than Chinese residential, which is not the intuitive result. Two honest
qualifiers: India's higher nominal growth makes a negative carry more sustainable, and home-loan
rates have fallen to 7.10–8.45% after 125bp of cuts through 2025 — lower than this desk assumed when
it set the question.</div>
</section>

<section>
<h2>7 · REITs — the desk's admitted gap, closed with a negative answer</h2>
<p class="sub">SNAPSHOT-1 sized a 2% REIT allocation and flagged it as not desk-researched at all.
It is now researched, and the finding does not support adding to it at current prices.</p>
<div class="tbl"><table>
<thead><tr><th>REIT</th><th>Distribution yield</th><th>vs 10-yr G-sec ≈7.0%</th><th>Price vs NAV</th></tr></thead>
<tbody>
<tr><td>Mindspace</td><td class="mono">4.8%</td><td class="mono neg">−2.2pp</td>
<td class="mono">5–11% discount</td></tr>
<tr><td>Nexus Select</td><td class="mono">5.4%</td><td class="mono neg">−1.6pp</td>
<td class="mono">small premium</td></tr>
<tr><td>Embassy</td><td class="mono">5.75%</td><td class="mono neg">−1.25pp</td>
<td class="mono">5–11% discount</td></tr>
<tr><td>Brookfield India</td><td class="mono">6.2%</td><td class="mono neg">−0.8pp</td>
<td class="mono">5–11% discount</td></tr>
</tbody></table></div>
<p><b>Every Indian REIT distributes less than the sovereign bond</b> while carrying property,
leverage and equity risk. That is a negative risk premium on its face. Three of the four trade at 5–11%
discounts to NAV, which is the market saying the same thing about the assets. <b>No residential or
retail-residential REIT exists in India</b> — confirmed, so the sleeve cannot express a residential
view even if the desk wanted one. And the total-return-since-listing figures are unusable: Nexus
alone carries three mutually inconsistent sourced numbers (+39%, +80%, +29.3%/yr) and none was
adopted.</p>
<div class="warn">CONSUMPTION: SNAPSHOT-1's 2% REIT line stops being “unresearched” and becomes
“researched and not compensated”. That is a smaller allocation question than it looks — but it is
now an answered one, and the answer is not to fund it from the equity sleeve at these yields.</div>
</section>

<section>
<h2>8 · Is Indian property run on black money — and would removing it crash the market?</h2>
<p class="sub">The principal's question, and it is answerable because the experiment has already
partly run. The answer is <b>sideways, not crash</b> — and the mechanism is specific.</p>
<div class="tbl"><table>
<thead><tr><th>Segment</th><th>Cash intensity</th><th>Why</th></tr></thead>
<tbody>
<tr><td><b>Land and agricultural</b></td><td class="mono neg">Highest (~40%+)</td>
<td>Structurally outside GST and RERA's reach entirely</td></tr>
<tr><td>Resale / secondary and premium</td><td class="mono">High, no clean figure</td>
<td>No developer, no bank underwriting, no escrow</td></tr>
<tr><td>Branded primary, bank-financed</td><td class="mono pos">Lowest</td>
<td>Bounded by RERA's 70% escrow and bank underwriting</td></tr>
</tbody></table></div>
<h3>What actually happened across the 2016-17 formalisation stack</h3>
<p class="sub">Demonetisation (Nov 2016), the Benami Amendment (Nov 2016), RERA (May 2017), GST
(Jul 2017) and Section 269ST capping cash receipts at ₹2 lakh (Apr 2017) — five shocks in nine
months.</p>
<ul>
<li><b>Prices did not crash.</b> All-India RBI house-price growth decelerated from ~7–8%/yr to
~3–4%/yr and <b>never went negative</b> — real-terms stagnation, which independently matches this
programme's own Mumbai finding of flat-to-negative real prices 2014–2021.</li>
<li><b>Supply crashed instead.</b> New launches <b>−44%</b> over five years against sales down only
about <b>12%</b>. A volume retrenchment, not a price collapse.</li>
<li><b>The mechanism: the index-setting buyer was never the cash-dependent one.</b> The marginal
price-setting buyer became the formal, bank-financed end-user — the least cash-exposed participant —
while the cash-heavy resale, land and premium segments absorbed the adjustment in <i>transaction
volume</i>. Credit substitution helped but is bounded: mortgage-to-GDP is still only ~11–12%, and it
froze on its own in the 2018-19 NBFC crisis.</li>
</ul>
<div class="warn"><b>No audited figure for the cash share of Indian property exists anywhere</b> —
every number in circulation is a consultant claim, an old study, a self-selected survey or an
anecdote. Two specific cautions, including one on a figure this desk itself quoted: Anarock's
“black money in housing down 75–80% since Nov 2016” covers housing rather than all real estate, its
own stated mechanism is <b>compositional</b> (branded developers capturing share) rather than a
re-measurement of cash per transaction, and Anarock is commercially aligned with the developers the
claim credits. The LocalCircles prevalence figures rest on a single self-selected online panel with
no benchmark for bias direction. Both are directionally useful; neither is a measurement.</div>
<p><b>So a full removal would most likely repeat the 2016-21 shape</b>: a volume effect concentrated
in land, resale and tier-2/3, not a fresh price crash. That matters directly for §4, because
several candidates' stories rest on exactly the land and plotted segments that would absorb it —
Dholera most of all, and Kokapet's land-above-its-own-building print is the same signal in a metro.
Cash persists where GST and RERA cannot reach, sustained by the circle-rate gap: Maharashtra's own
ready reckoner sat frozen 2019–22.</p>
</section>

<section class="panel">
<h2>Method, limits, and what would make this better</h2>
<h3>What is desk-grade and what is not</h3>
<p class="sub">IN-D1/IN-D2 were pre-registered before any number was computed, run on the vaulted
JST panel, and four cells were verified exact on a separate code path (window count 1,934; T≥15
frequency 2.33% and forward +9.65%; T≥20 0.98% and +11.16%; post-1970 frequencies 0.00% and 0.45%).
Three of five bars MISSED and are recorded as misses. Everything about India itself is
snippet-sourced.</p>
<h3>The limits that actually bind</h3>
<ul>
<li><b>No India property data in the vault at all</b> — no price series, no CPI. So there is no India
base rate, only a placement against 18 advanced economies that contain no EM and nothing at India's
urbanization stage.</li>
<li><b>No repeat-sales or transaction-weighted index exists for any city researched.</b> Every “+X%”
on this page is an asking-price or listed-rate comparison, and the one place both were obtainable
(Ulwe) showed asking running 25–30% above closings.</li>
<li><b>Carpet versus built-up versus super-built-up</b> moves a per-sq-ft figure 20–35% and can
reverse a ranking. Every dossier states the basis where the source did; where it did not, the figure
is flagged rather than converted.</li>
<li><b>Circle rates, jantri rates and government auction prices are not market prices.</b> Ahmedabad
and Pune produced only floor-versus-asking comparisons, which is a different measurement from
MMR's asking-versus-closing, and the dossier says so rather than substituting one for the other.</li>
<li>IN-D1's windows OVERLAP, so frequencies are exposure shares rather than independent trials and
no significance is claimed.</li>
<li><b>The one China-identified India vulnerability remains open.</b> Unlisted and tier-2/3 developer
leverage: bank CRE credit (₹6.7 lakh cr, +21.5% YoY) and system NPAs are public, but nothing
segments them listed-versus-unlisted or by tier, and rating coverage reaches only the rated
universe — exactly the population China's defaults came from. This leg <b>confirmed the gap rather
than closing it</b>.</li>
</ul>
<h3>The five pulls that would fix it</h3>
<p class="sub">Added to the desk's runsheet the same day, in priority order: NHB RESIDEX and any
repeat-sales index; IGR/sub-registrar registration microdata (the only genuinely point-in-time
Indian property data, and the cleanest test of the black-money question); circle-rate and jantri
histories by ward; city rental indices with method, to resolve the 2–3pp yield-family conflict that
decides §6; and the unlisted-developer-leverage segmentation.</p>
<p class="note">Sources of record: trial-ledger entries IN-D1..IN-D2 (registration committed before
the run) · scripts/analyze_india_thresholds.py · research/india_thresholds.json ·
research/china_baserate.json (the CN base rate used for every placement) ·
research/notes/india-dossiers/ (nine cited dossiers, each with its own confidence tags and gaps
section) · research/frontier/india-property-plan.md §0 for the bar arithmetic and the vault check.
Regenerates via scripts/build_india_atlas.py, never from memory.</p>
</section>
</div>
"""
OUT.write_text(html)
print(f"written {OUT} ({len(html):,} bytes) · {len(G)} micro-markets · {len(MK)} yield rows")
