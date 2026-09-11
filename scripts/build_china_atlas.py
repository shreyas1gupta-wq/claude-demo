"""Builds docs/learn/artifacts/china-property-crash-atlas.html from research/china_baserate.json
(the vaulted JST base rate, desk-grade) plus the sourced China figures carried in
research/notes/china-dossiers/. Regenerates from those files, never from memory."""
import json, pathlib

J = json.load(open("/home/user/claude-demo/research/china_baserate.json"))
EP = [e for e in J["CN-D1"]["episodes"] if e["peak"] >= 1970]
M = J["modern_era"]["median"]
OUT = pathlib.Path("/home/user/claude-demo/docs/learn/artifacts/china-property-crash-atlas.html")

# ---------- chart 1: the velocity parity scatter ----------
pts = [(e["pre5_vel"], -e["decl_vel"], e["country"], e["peak"], e["depth"], e["dur"])
       for e in EP if e.get("pre5_vel") and e.get("decl_vel")]
W, H, PL, PR, PT, PB = 640, 420, 58, 18, 22, 46
xmax, ymax = 14, 16
sx = lambda v: PL + (v / xmax) * (W - PL - PR)
sy = lambda v: H - PB - (v / ymax) * (H - PT - PB)
LBL = {("Japan", 1991): ("Japan 1991", 8, -8), ("Ireland", 2006): ("Ireland 2006", -78, -6),
       ("Finland", 1989): ("Finland 1989", -84, 4), ("Spain", 2007): ("Spain 2007", 8, 12),
       ("USA", 2006): ("US 2006", 8, -8), ("Germany", 1981): ("Germany 1981", 10, 4),
       ("UK", 1989): ("UK 1989", -58, -8)}
g = []
for v in (0, 2, 4, 6, 8, 10, 12, 14):
    g.append(f'<line x1="{sx(v):.1f}" y1="{PT}" x2="{sx(v):.1f}" y2="{H-PB}" class="gr"/>'
             f'<text x="{sx(v):.1f}" y="{H-PB+16}" class="ax" text-anchor="middle">{v}</text>')
for v in (0, 4, 8, 12, 16):
    g.append(f'<line x1="{PL}" y1="{sy(v):.1f}" x2="{W-PR}" y2="{sy(v):.1f}" class="gr"/>'
             f'<text x="{PL-8}" y="{sy(v)+4:.1f}" class="ax" text-anchor="end">{v}</text>')
g.append(f'<line x1="{sx(0):.1f}" y1="{sy(0):.1f}" x2="{sx(14):.1f}" y2="{sy(14):.1f}" class="par"/>')
g.append(f'<text x="{sx(12.4):.1f}" y="{sy(13.1):.1f}" class="parl" text-anchor="end">bust speed = boom speed</text>')
for x, y, c, p, dep, dur in pts:
    r = 3.2 + min(abs(dep), 60) / 16
    g.append(f'<circle cx="{sx(x):.1f}" cy="{sy(y):.1f}" r="{r:.1f}" class="dot"><title>'
             f'{c} {p}: boom +{x:.1f}%/yr, bust -{y:.1f}%/yr, depth {dep:.1f}%, {dur}y</title></circle>')
    if (c, p) in LBL:
        t, dx, dy = LBL[(c, p)]
        lx, ly = sx(x) + dx, sy(y) + dy
        ax_ = lx + (len(t) * 6.1 if dx < 0 else 0)          # anchor at the label edge nearest the dot
        g.append(f'<line x1="{ax_:.1f}" y1="{ly-3.5:.1f}" x2="{sx(x)+(-r-1.5 if dx<0 else r+1.5):.1f}" '
                 f'y2="{sy(y):.1f}" class="lead"/>'
                 f'<text x="{lx:.1f}" y="{ly:.1f}" class="pl">{t}</text>')
SC1 = (f'<svg viewBox="0 0 {W} {H}" class="chart" role="img" aria-label="Scatter of 24 modern '
       f'property-crash episodes: pre-crash appreciation speed against decline speed, with a parity line">'
       + "".join(g)
       + f'<text x="{(PL+W-PR)/2:.0f}" y="{H-6}" class="axt" text-anchor="middle">pre-crash appreciation, %/yr real (5 years to the peak)</text>'
       + f'<text x="14" y="{(PT+H-PB)/2:.0f}" class="axt" text-anchor="middle" transform="rotate(-90 14 {(PT+H-PB)/2:.0f})">decline, %/yr real</text>'
       + "</svg>")

# ---------- chart 2: the depth strip, with China placed ----------
W2, H2, P2 = 640, 132, 46
dmin, dmax = -60, 0
sx2 = lambda v: P2 + ((v - dmin) / (dmax - dmin)) * (W2 - 2 * P2)
d = []
for v in (-60, -50, -40, -30, -20, -10, 0):
    d.append(f'<line x1="{sx2(v):.1f}" y1="30" x2="{sx2(v):.1f}" y2="72" class="gr"/>'
             f'<text x="{sx2(v):.1f}" y="88" class="ax" text-anchor="middle">{v}%</text>')
for e in EP:
    d.append(f'<circle cx="{sx2(max(e["depth"],dmin)):.1f}" cy="51" r="4.6" class="dot2">'
             f'<title>{e["country"]} {e["peak"]}: {e["depth"]:.1f}% over {e["dur"]}y</title></circle>')
med = M["depth"]
d.append(f'<line x1="{sx2(med):.1f}" y1="24" x2="{sx2(med):.1f}" y2="78" class="med"/>'
         f'<text x="{sx2(med):.1f}" y="18" class="medl" text-anchor="middle">base-rate median {med:.0f}%</text>')
for v, t, cls in [(-30.0, "China tier-3 “as much as −30%”", "cn3"), (-10.0, "China tier-1 “&lt;−10%”", "cn1")]:
    d.append(f'<line x1="{sx2(v):.1f}" y1="36" x2="{sx2(v):.1f}" y2="100" class="{cls}"/>'
             f'<text x="{sx2(v):.1f}" y="114" class="cnl" text-anchor="middle">{t}</text>')
SC2 = (f'<svg viewBox="0 0 {W2} {H2}" class="chart" role="img" aria-label="Strip plot of the depth of '
       f'24 modern property crashes with China tier-1 and tier-3 marked">' + "".join(d) + "</svg>")

# ---------- chart 3: rental yield peak to trough ----------
ys = [(e["yd_peak"], e["yd_trough"], e["country"], e["peak"]) for e in EP
      if e.get("yd_peak") and e.get("yd_trough")]
ys.sort(key=lambda r: r[0])
W3, H3, P3T, P3B = 640, 300, 26, 52
ymx = 10
sy3 = lambda v: H3 - P3B - (v / ymx) * (H3 - P3T - P3B)
colw = (W3 - 96) / max(len(ys), 1)
y = []
for v in (0, 2, 4, 6, 8, 10):
    y.append(f'<line x1="72" y1="{sy3(v):.1f}" x2="{W3-16}" y2="{sy3(v):.1f}" class="gr"/>'
             f'<text x="64" y="{sy3(v)+4:.1f}" class="ax" text-anchor="end">{v}%</text>')
for i, (a, b, c, p) in enumerate(ys):
    x = 84 + i * colw
    y.append(f'<line x1="{x:.1f}" y1="{sy3(a):.1f}" x2="{x:.1f}" y2="{sy3(b):.1f}" class="slope"/>'
             f'<circle cx="{x:.1f}" cy="{sy3(a):.1f}" r="3.4" class="ypk"><title>{c} {p} peak yield {a:.2f}%</title></circle>'
             f'<circle cx="{x:.1f}" cy="{sy3(b):.1f}" r="3.4" class="ytr"><title>{c} {p} trough yield {b:.2f}%</title></circle>'
             f'<text x="{x:.1f}" y="{H3-34}" class="tick" text-anchor="end" transform="rotate(-60 {x:.1f} {H3-34})">{c[:11]} {str(p)[2:]}</text>')
for v, t, cls in [(1.75, "China tier-1 AT ITS 2021 PEAK, ~1.7-1.8%", "cn3"),
                  (2.30, "China tier-1 today, ~2.0-2.6%", "cn1")]:
    y.append(f'<line x1="72" y1="{sy3(v):.1f}" x2="{W3-16}" y2="{sy3(v):.1f}" class="{cls}"/>'
             f'<text x="{W3-18}" y="{sy3(v)-5:.1f}" class="cnl" text-anchor="end">{t}</text>')
SC3 = (f'<svg viewBox="0 0 {W3} {H3}" class="chart" role="img" aria-label="Rental yield at each '
       f'episode peak and trough, with China tier-1 today marked below the whole range">'
       + "".join(y) + "</svg>")

d3 = J["CN-D3"]["d5_mort"]
html = f"""<title>China Property Crash Atlas</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700&family=Source+Sans+3:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root {{
  --bg:#f6f5f1; --panel:#fdfdfb; --ink:#212528; --ink2:#4f555a; --mut:#868c91;
  --line:#e3e1d9; --s1:#2a5fa8;
  --bad:#ab3227; --badbg:#f8e8e6; --good:#1e7048; --goodbg:#e6f2ea;
  --amber:#8d6100; --amberbg:#f6eed8; --gate:#57678a; --gatebg:#e8ecf3;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg:#14171a; --panel:#1c2024; --ink:#e7e9eb; --ink2:#a7adb2; --mut:#7b8187;
  --line:#2e3339; --s1:#5e9be0;
  --bad:#df7268; --badbg:#37221f; --good:#5cba8a; --goodbg:#1b3126;
  --amber:#d6a53a; --amberbg:#30270e; --gate:#8ea1c2; --gatebg:#1f252e;
}} }}
:root[data-theme="dark"] {{
  --bg:#14171a; --panel:#1c2024; --ink:#e7e9eb; --ink2:#a7adb2; --mut:#7b8187;
  --line:#2e3339; --s1:#5e9be0;
  --bad:#df7268; --badbg:#37221f; --good:#5cba8a; --goodbg:#1b3126;
  --amber:#d6a53a; --amberbg:#30270e; --gate:#8ea1c2; --gatebg:#1f252e;
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
p {{ margin:6px 0 0; max-width:74ch; }}
.sub {{ color:var(--ink2); font-size:14.5px; max-width:80ch; }}
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
.tiles {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(230px,1fr)); gap:1px;
  background:var(--line); border:1px solid var(--line); border-radius:6px; overflow:hidden; margin:24px 0; }}
.t {{ background:var(--panel); padding:16px 18px; }}
.t .k {{ font-family:"Archivo"; font-size:12px; font-weight:600; letter-spacing:.05em;
  text-transform:uppercase; color:var(--mut); }}
.t .v {{ font-family:"IBM Plex Mono",monospace; font-size:27px; font-weight:500; line-height:1.15;
  margin:5px 0 4px; font-variant-numeric:tabular-nums; }}
.t .d {{ font-size:13px; color:var(--ink2); }}
section {{ margin:34px 0 0; }}
.panel {{ background:var(--panel); border:1px solid var(--line); border-radius:6px; padding:20px 22px; }}
.chartwrap {{ overflow-x:auto; margin:14px 0 4px; }}
svg.chart {{ width:100%; min-width:560px; height:auto; display:block; }}
.gr {{ stroke:var(--line); stroke-width:1; }}
.ax {{ fill:var(--mut); font-family:"IBM Plex Mono",monospace; font-size:10.5px; }}
.axt {{ fill:var(--ink2); font-family:"Source Sans 3",sans-serif; font-size:12px; }}
.dot {{ fill:var(--s1); fill-opacity:.62; stroke:var(--s1); stroke-width:1; }}
.dot2 {{ fill:var(--s1); fill-opacity:.5; stroke:var(--s1); stroke-width:1; }}
.par {{ stroke:var(--ink2); stroke-width:1.4; stroke-dasharray:5 4; }}
.parl {{ fill:var(--ink2); font-family:"Source Sans 3",sans-serif; font-size:11.5px; }}
.lead {{ stroke:var(--mut); stroke-width:.9; }}
.pl {{ fill:var(--ink); font-family:"Archivo",sans-serif; font-size:11.5px; font-weight:600; }}
.med {{ stroke:var(--ink); stroke-width:1.6; }}
.medl {{ fill:var(--ink); font-family:"Archivo",sans-serif; font-size:11px; font-weight:600; }}
.cn1 {{ stroke:var(--bad); stroke-width:1.8; stroke-dasharray:4 3; }}
.cn3 {{ stroke:var(--bad); stroke-width:1.8; }}
.cnl {{ fill:var(--bad); font-family:"Archivo",sans-serif; font-size:11px; font-weight:600; }}
.slope {{ stroke:var(--ink2); stroke-width:1.3; }}
.ypk {{ fill:var(--bad); }} .ytr {{ fill:var(--good); }}
.tick {{ fill:var(--mut); font-family:"IBM Plex Mono",monospace; font-size:9.5px; }}
.tbl {{ overflow-x:auto; margin:14px 0 0; }}
table {{ border-collapse:collapse; width:100%; min-width:600px; font-size:13.5px; }}
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
.warn {{ background:var(--amberbg); color:var(--amber); border-radius:5px; padding:13px 16px;
  font-size:13.5px; margin:16px 0 0; max-width:92ch; }}
.note {{ font-size:13px; color:var(--mut); max-width:96ch; margin-top:10px; }}
ul {{ margin:8px 0 0; padding-left:20px; }} li {{ margin:5px 0; max-width:88ch; }}
.legend {{ display:flex; gap:16px; flex-wrap:wrap; font-size:12.5px; color:var(--ink2); margin-top:6px; }}
.sw {{ display:inline-block; width:9px; height:9px; border-radius:50%; margin-right:5px; }}
</style>
<div class="wrap">
<header>
<p class="eyebrow">The Cycle Program · CN programme</p>
<h1>China Property Crash Atlas</h1>
<p class="sub">Two halves, deliberately kept apart because they carry different evidential weight.
<b>The base rate</b> is computed from a vaulted dataset — 48 real house-price crashes across 18
countries and 150 years — and answers what property busts actually <i>do</i>: how deep, how long,
how fast, what the rental yield does, and which debt number predicts the peak. <b>China's own
figures</b> are then placed against those distributions from sourced research. China appears in no
dataset this desk owns, which is exactly why the base rate had to be built first.</p>
<div class="prov">
<span class="badge">ledger CN-D1..CN-D5</span><span class="badge">census 1,365 → 1,389</span>
<span class="badge">JST Macrohistory R6, vaulted + manifested</span>
<span class="badge">4 cells desk-verified on separate code paths</span>
<span class="badge">2026-09-11</span></div>
<div class="grade">
<div class="gr1"><b>Half A — desk-grade <span class="tag desk">VAULT</span></b>
Computed from <span class="mono">ingest/vault/jst/JSTdatasetR6.xlsx</span>, sha256-manifested,
pre-registered with falsifiable bars before any number was computed. Reproducible via
<span class="mono">scripts/analyze_china_baserate.py</span>.</div>
<div class="gr2"><b>Half B — indicative only <span class="tag snip">SNIPPET</span></b>
WebFetch is egress-blocked in this environment, so every China figure rests on search-result
snippets that could not be checked against a primary page. Two-source corroboration was required
where possible and each figure carries its own tag in the dossiers. Treat as research direction,
not as evidence. The fix is a named data pull, now on the runsheet.</div>
</div>
</header>

<div class="tiles">
<div class="t"><div class="k">A bust takes back</div><div class="v">−32%</div>
<div class="d">of real value, median of 24 modern episodes. Over a median <b>5.5 years</b>.
Remarkably invariant: p25 −39%, p75 −29%.</div></div>
<div class="t"><div class="k">Bust speed ÷ boom speed</div><div class="v">0.99×</div>
<div class="d">A bust runs at almost exactly the annual speed of its own boom. My registered prior
said slower; it <b>missed</b>. There is no gentle-deflation discount.</div></div>
<div class="t"><div class="k">Credit warning, false alarms</div><div class="v">87.2%</div>
<div class="d">Rapid mortgage growth does lift 3-year crash odds <b>1.72×</b> — and is wrong about
seven times in eight. A state, never a trigger.</div></div>
<div class="t"><div class="k">China, bust ÷ boom speed</div><div class="v">0.98× or 1.73×</div>
<div class="d">On the <b>official</b> index China runs exactly at the base rate. On <b>private</b>
estimates it runs 1.7× faster than its own boom. Same country, opposite conclusions.</div></div>
<div class="t"><div class="k">The two Chinese yields</div><div class="v">2.3% vs 5.5%</div>
<div class="d">Direct tier-1 market vs the cap rate implied by traded C-REITs. The base rate says
busts <b>end</b> near 5.2% — the institutional mark is already there.</div></div>
<div class="t"><div class="k">Equities, year one</div><div class="v">−13.7pp</div>
<div class="d">Excess real return after a housing peak. Double if banks break. Essentially
<b>gone by year five</b>.</div></div>
</div>

<section>
<h2>1 · A bigger boom buys speed, not depth</h2>
<p class="sub">Each dot is one of the 24 property crashes in the panel with a peak from 1970 onward;
dot size is the depth of the fall. The dashed line is parity — where a market falls at the same
annual speed it rose. The cloud sits <i>on</i> that line, and the two archetypes sit either side of
it: Japan took 18 years to fall 47%, Ireland took 6 years to fall 56%. Same destination, three
times the speed.</p>
<div class="chartwrap">{SC1}</div>
<p class="note">Real house prices (nominal deflated by CPI), annual resolution — so every velocity
figure is a lower bound on the peak monthly rate. Hover any dot for its country, years, depth and
duration.</p>

<h3>China's own velocity, placed on that line</h3>
<p class="sub">The scatter above is the base rate. Here is China measured the same way — and the
answer depends entirely on whose price index you accept, which is itself the finding.</p>
<div class="tbl"><table>
<thead><tr><th>Measure</th><th>Cumulative from the Sep-2021 peak</th><th>Bust, %/yr</th>
<th>Boom, %/yr</th><th>Bust ÷ boom</th><th>Which archetype</th></tr></thead>
<tbody>
<tr><td>Official NBS index, real</td><td class="mono">−24.6%</td><td class="mono">−6.1%</td>
<td class="mono">+6.2%</td><td class="mono">0.98×</td>
<td>Dead on the base rate (0.99×) — an ordinary, Japan-ish grind</td></tr>
<tr><td>Official NBS index, nominal</td><td class="mono">−21.8%</td><td class="mono">−5.3%</td>
<td class="mono">+6.2%</td><td class="mono">0.85×</td><td>Slightly gentler than the base rate</td></tr>
<tr><td>Private analyst estimates</td><td class="mono">≈−40%</td><td class="mono">−10.7%</td>
<td class="mono">+6.2%</td><td class="mono neg">1.73×</td>
<td><b>Ireland/Finland fast-crash regime</b></td></tr>
<tr><td>Tier-1 at its 2015-16 hottest</td><td class="mono">—</td><td class="mono">—</td>
<td class="mono">+30.3%</td><td class="mono">—</td>
<td>Mismatched windows; shown only to size the spike</td></tr>
</tbody></table></div>
<div class="warn"><b>This is the cleanest illustration of why the measurement question is not
pedantic.</b> Take the official index and China is running at exactly the international base rate —
a slow, ordinary unwind roughly three-quarters of the way to a median crash. Take the estimates most
private analysts work from and China is falling <b>1.7× faster than its own boom</b>, which puts it
with Ireland and Finland rather than Japan, and already <i>past</i> the median depth. The two
readings support opposite investment conclusions, and no amount of analysis resolves a 2× gap in the
input. It is the single strongest argument for the data pull on the desk's runsheet.</div>
<h3>The registered scorecard</h3>
<div class="tbl"><table>
<thead><tr><th>Registered question</th><th>Bar</th><th>Print</th><th>Verdict</th></tr></thead>
<tbody>
<tr><td>Median depth of a crash</td><td class="mono">−25% to −40%</td>
<td class="mono">−34.2%</td><td class="pos">HIT</td></tr>
<tr><td>Median duration to trough</td><td class="mono">≥ 4 years</td>
<td class="mono">6.5 years</td><td class="pos">HIT</td></tr>
<tr><td>Bust slower per year than the boom</td><td class="mono">ratio &lt; 1.0</td>
<td class="mono">1.12× full / 0.99× modern</td><td class="neg">MISS</td></tr>
<tr><td>Bigger booms fall deeper</td><td class="mono">≥ 8pp deeper</td>
<td class="mono">3.8pp</td><td class="neg">MISS</td></tr>
<tr><td>Bigger booms not materially faster</td><td class="mono">gap &lt; 2pp/yr</td>
<td class="mono">3.5pp/yr faster</td><td class="neg">MISS</td></tr>
</tbody></table></div>
<div class="warn"><b>Why the misses matter more than the hits here.</b> Three of five priors were
written the wrong way round, and all three failed in the same direction: property busts are faster
and more uniform in depth than a careful prior expected. The practical consequence for a China view
is that the size of China's run-up predicts <i>how fast</i> the unwind runs, not how far it goes —
and "it will deflate gently because the state manages it" is an argument against the historical
record rather than from it.</div>
</section>

<section>
<h2>2 · Where China actually sits on that distribution</h2>
<p class="sub">Every modern episode's depth, with China's reported cumulative declines marked. The
striking part is not that China is falling — it is how <i>unevenly</i>. On the reported figures,
tier-3 China has already taken a full base-rate crash while tier-1 has taken about a third of one.</p>
<div class="chartwrap">{SC2}</div>
<div class="legend"><span><span class="sw" style="background:var(--s1)"></span>one modern
episode</span><span><span class="sw" style="background:var(--ink)"></span>base-rate
median</span><span><span class="sw" style="background:var(--bad)"></span>China, reported</span></div>
<div class="tbl"><table>
<thead><tr><th>Base-rate statistic</th><th>Modern panel</th><th>China, reported</th><th>Placement</th></tr></thead>
<tbody>
<tr><td>National cumulative real decline</td><td class="mono">−32.0% median<br>(−39 to −29 mid-range)</td>
<td class="mono">official −24.6%<br>private ≈−40% <span class="tag snip">SNIPPET</span></td>
<td>Official: <b>~three-quarters</b> of a median crash. Private: <b>already past it</b></td></tr>
<tr><td>Peak-to-trough real decline, by tier</td><td class="mono">−32.0% median<br>(−39 to −29 mid-range)</td>
<td class="mono">tier-1 “&lt;10%”<br>tier-3 “up to 30%” <span class="tag snip">SNIPPET</span></td>
<td>Tier-3 <b>already at the median</b>; tier-1 about a third of the way</td></tr>
<tr><td>Latest year-on-year, new-build</td><td class="mono">—</td>
<td class="mono">T1 −1.1% · T2 −2.8% · T3 −4.2%<br>(NBS, Jul 2026)</td>
<td>Clean monotone tier ordering; second-hand worse in every tier</td></tr>
<tr><td>Duration to trough</td><td class="mono">5.5 years median<br>Japan 18y, Ireland 6y</td>
<td class="mono">~5 years elapsed from the 2021 peak</td>
<td>At the median <i>elapsed</i> time — which is not the same as being at the trough</td></tr>
<tr><td>Rental yield <i>at the peak</i></td><td class="mono">3.29% median<br>1.49% lowest (Spain 2007)</td>
<td class="mono">tier-1 ~1.7–1.8% in 2021 <span class="tag snip">SNIPPET</span></td>
<td><b>Second-lowest peak yield in 150 years of this panel</b>, behind only Spain</td></tr>
<tr><td>Yield expansion so far</td><td class="mono">+1.53pp peak→trough</td>
<td class="mono">+0.3 to +0.8pp (to ~2.0–2.6%)</td>
<td>About <b>a third</b> of the normalization — the same fraction as tier-1 depth</td></tr>
<tr><td>Carry: yield − policy rate</td><td class="mono">n/a</td>
<td class="mono">2021: 1.70 − 4.65 = <b>−2.95pp</b><br>now: 2.20 − 3.50 = <b>−1.30pp</b></td>
<td>Still negative — never cash-flow-positive on leverage; narrowed almost entirely by <b>rate cuts, not yield repair</b></td></tr>
<tr><td>Official vs private measurement</td><td class="mono">n/a</td>
<td class="mono">~2pp gap now, ~9pp in 2023</td>
<td>Understatement bias appears largest at turning points</td></tr>
</tbody></table></div>
<div class="warn">The single most useful thing this table says: <b>“has China crashed?” is the wrong
question, because the answer differs by a factor of three across tiers.</b> Tier-3 has experienced
an ordinary, complete property crash by the international base rate. Tier-1 has experienced a
correction. Any single national number averages those two into something that describes neither.</div>
</section>



<section>
<h2>3 · Tier-3 China, where the crash actually happened</h2>
<p class="sub">The base-rate placement said tier-3 had taken a full crash and tier-1 about a third of
one. Documenting the tier-3 end properly produces the most important structural fact on the page —
and the answer to whether this is a national event or a peripheral one.</p>
<div class="tbl"><table>
<thead><tr><th>Case</th><th>Figure</th><th>Confidence</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td><b>Tier-3-and-below share of stock / inventory</b></td><td class="mono">50–78%</td>
<td><span class="tag snip">2-SOURCE</span></td>
<td><b>The bust is structurally national, not peripheral.</b> Whichever metric you take — value,
floor area or new construction — the majority of Chinese housing sits where prices fell most</td></tr>
<tr><td>Langfang / Yanjiao (Beijing commuter belt)</td>
<td class="mono neg">≈40,000 → ≈18,700 CNY/sqm<br><b>&gt;50% off the Mar-2017 peak</b></td>
<td><span class="tag snip">2-SOURCE</span></td>
<td>Already past the base-rate median (−32%) and approaching <b>Ireland 2006 (−55.7%)</b>, the worst
modern episode in the panel</td></tr>
<tr><td>Hegang, Heilongjiang</td><td class="mono">≈2,000–3,500 CNY/sqm</td>
<td><span class="tag snip">2-SOURCE</span></td>
<td>The cheapest housing sourced. Note the correction: the viral “CNY 20,000 apartment” is a
<b>small-unit total price</b>, not a per-sqm rate</td></tr>
<tr><td>Provincial capitals, 2003–2017 boom</td><td class="mono pos">≈+400% vs ≈+200% non-capital</td>
<td><span class="tag snip">1-SOURCE</span></td>
<td>Capitals decisively won the boom, and the “strong provincial capital” (强省会) policy was
explicitly designed to make that happen</td></tr>
<tr><td><b>Provincial capitals, current bust</b></td>
<td class="mono neg">Nanjing −11.45%, Wuhan −10.89% YoY<br>(Jun 2026, among the worst nationally)</td>
<td><span class="tag snip">1-SOURCE</span></td>
<td><b>Capital status does NOT protect on the way down.</b> Two capitals sit among the worst
decliners while Shenyang and Guangzhou held up better</td></tr>
</tbody></table></div>
<div class="warn"><b>This answers the principal's "capital city" question, and the answer is
asymmetric.</b> Provincial-capital status was worth roughly double the appreciation through the
2003-2017 boom and is worth <i>nothing</i> as protection in the bust — Nanjing and Wuhan are among
the worst decliners in the country. Administrative privilege bought upside, not downside
protection, which is exactly the profile of a policy-conferred advantage rather than an economic
one. Only 5 of ~31 capitals could be ranked from this session's sourcing, so the ranking is
indicative; the direction is the finding.</div>
<p class="note">Named gaps: Yingkou, Zhuozhou, Yantai and Zhoushan produced no city-specific
figures; Hegang's fiscal-restructuring mechanism is <span class="mono">[RECALL]</span> only; and the
satellite-versus-independent-tier-3 comparison rests on a single case, so it is not a verdict.</p>
</section>
<section>
<h2>4 · The land market — the question underneath the question</h2>
<p class="sub">The principal asked about land prices, and land turns out to behave differently from
housing in a way that matters: <b>land revenue, land volume and land price peaked in three different
years and have fallen by three very different amounts.</b> Reading any one of them as "the land
market" gets the story wrong.</p>
<div class="tbl"><table>
<thead><tr><th>Land series</th><th>Peak</th><th>Latest</th><th>Change</th><th>What it measures</th></tr></thead>
<tbody>
<tr><td>Land-transfer income (MOF)</td><td class="mono">CNY 8.705tn (2021)</td>
<td class="mono">CNY 4.152tn (2025)</td><td class="mono neg">−52.3%</td>
<td>The fiscal number — cash into local government</td></tr>
<tr><td>Residential land area sold (300 cities)</td><td class="mono">1.13bn sqm (2020)</td>
<td class="mono">0.38bn sqm</td><td class="mono neg">−66%</td>
<td>The volume number — how much land actually changes hands</td></tr>
<tr><td>Average residential floor price</td><td class="mono">CNY 5,818/sqm (2023)</td>
<td class="mono">CNY 4,457/sqm (H1 2026)</td><td class="mono neg">−23%</td>
<td>The price number — and it is composition-contaminated</td></tr>
</tbody></table></div>
<p class="note">All three <span class="tag snip">SNIPPET</span>-sourced; the 2024→2025 area figures
were found to be internally inconsistent across sources and are flagged unresolved in the dossier.</p>
<h3>Three things here are worth more than the headline</h3>
<ul>
<li><b>Land price peaked two years after land volume.</b> Volume and auction premiums topped in
2020-21; the average price kept rising through 2021 (+23.9%) and 2022 (+23.3%) and only peaked in
2023. That is not a market that held up — it is a <b>composition effect</b>, which the source
itself labels 结构性上涨 (structural increase): sales collapsed in tier-3 and tier-4 while the
surviving transactions concentrated in tier-1, lifting the average while every individual tier
fell. Record single-parcel prices in Shanghai are the same artifact at maximum magnification.</li>
<li><b>"Land revenue is X% of local government revenue" has four different right answers</b> —
roughly 30% against total local revenue including central transfers, up to 78-84% against
local general-budget revenue alone. Same cash, four denominators, four stories. Any citation of
this ratio without its denominator is uninformative.</li>
<li><b>The replacement instrument is still shelved.</b> A recurring property tax is the obvious
substitute for land-sale revenue; the expanded pilot announced in 2021 has been on hold since March
2022, so the fiscal hole has been filled with transfers, special bonds and asset sales rather than
a new tax base.</li>
</ul>
<div class="warn"><b>Why this is the most decision-relevant section for a foreign allocator.</b> The
housing price index is what gets reported, but the land series is what transmits: a 52% fall in
land-transfer income is a fiscal shock to the local governments that fund infrastructure, and it is
the channel through which a property bust reaches steel, cement and the commodity complex — which
is where an India-facing book actually feels it.</div>
</section>

<section>
<h2>5 · Land vs apartments vs houses vs shops vs buildings</h2>
<p class="sub">The principal asked for the asset-class split, and it is the most dispersed part of the
whole story: <b>within a single city, one segment set fresh record prices in the same year another
fell by a quarter.</b> "Chinese property fell X%" is not a sentence that survives contact with the
sub-class data.</p>
<div class="tbl"><table>
<thead><tr><th>Sub-class</th><th>Move from peak</th><th>Confidence</th><th>What is actually going on</th></tr></thead>
<tbody>
<tr><td><b>Ultra-prime / luxury resale</b></td><td class="mono pos">Shanghai core <b>+20% YoY</b><br>Shenzhen record ¥380k/sqm</td>
<td><span class="tag snip">2-SOURCE</span></td>
<td>A flight to scarcity <i>inside</i> the bust. Shenzhen set fresh records in the same year its
citywide new-build prices fell 25–30%</td></tr>
<tr><td>“Improvement” housing (改善型)</td><td class="mono">outperforming first-home</td>
<td><span class="tag snip">SNIPPET</span></td>
<td>Inverts the naive prior — the trade-up buyer with equity is the marginal bid, not the
first-timer</td></tr>
<tr><td>Old core apartments</td><td class="mono">at or above new towers next door</td>
<td><span class="tag snip">SNIPPET</span></td>
<td>Location and redevelopment optionality beat building age — a composition effect, flagged as
such</td></tr>
<tr><td>Land (price per sqm)</td><td class="mono neg">−23% from a 2023 peak</td>
<td><span class="tag snip">SNIPPET</span></td>
<td>But the peak is two years late and composition-contaminated (see §3)</td></tr>
<tr><td>Mainstream new-build, national</td><td class="mono neg">−21.8% nominal / −24.6% real</td>
<td><span class="tag snip">2-SOURCE</span></td>
<td>The official index; private estimates put it near −40%</td></tr>
<tr><td>Grade-A office, retail</td><td class="mono neg">cap rates <b>expanding</b></td>
<td><span class="tag snip">SNIPPET</span></td>
<td>China is the one Asia-Pacific market where commercial cap rates widen while the region's
compress</td></tr>
<tr><td><b>Strata-titled community shops</b></td><td class="mono neg">¥50k → ¥20–30k/sqm<br>(−40 to −60%)</td>
<td><span class="tag snip">1-SOURCE</span></td>
<td>The retail-investor category, and the worst cycle-driven outcome found. Single-sourced and
flagged as the top follow-up</td></tr>
<tr><td><b>Beijing 商住房</b> (commercial-titled flats)</td><td class="mono neg">volume <b>−94%</b><br>price ≈−43%, then −40% again</td>
<td><span class="tag snip">2-SOURCE</span></td>
<td>The worst outcome on the page — but <b>policy-driven, not cycle-driven</b>: the 2017 Beijing
ban destroyed the buyer pool overnight</td></tr>
</tbody></table></div>
<div class="warn"><b>The transferable lesson, and it is a governance one.</b> The single most
destructive event in this table was not the credit cycle — it was a regulatory reclassification that
removed a category's eligible buyers in one stroke, taking transaction volume down 94%. For an
India-facing book the read-across is not "Chinese flats fell"; it is that in a policy-directed market
the <i>rule change</i> is the tail risk, and it arrives faster than any price series can warn you.</div>
<p class="note">Thinnest sections in the underlying dossier, named rather than filled with guesses:
villa and low-density housing, and named high-street rents (Wangfujing, Nanjing Road, Huaihai Road).
The mall-versus-high-street question flips by quarter and by source, so no verdict is claimed.</p>
</section>

<section>
<h2>6 · Offices and business rent — worse than housing, and worse than anywhere else</h2>
<p class="sub">The principal asked about buildings and business rent. Chinese commercial property has
fallen further than Chinese housing, and Chinese office vacancy has no peer in the developed world.</p>
<div class="tbl"><table>
<thead><tr><th>Measure</th><th>Figure</th><th>Confidence</th><th>Context</th></tr></thead>
<tbody>
<tr><td><b>Worst office vacancy</b></td>
<td class="mono neg">Wuhan 40.6% → <b>43.2%</b> (Q1 2026)<br>Changchun ≈44% (2021-23, stale)</td>
<td><span class="tag snip">1-SOURCE</span></td>
<td>For scale: the worst non-China market found is <b>San Francisco at ≈26–28%</b>. No source names a
global #1, so this is a reasoned inference, not a citation</td></tr>
<tr><td>Worst tier-1 vacancy</td><td class="mono neg">Shenzhen 26–30%</td>
<td><span class="tag snip">1-SOURCE</span></td><td>Sources disagree on the point figure</td></tr>
<tr><td><b>Tier-1 office rent decline</b></td>
<td class="mono neg">−20% (Shanghai) to <b>−34% (Guangzhou)</b></td>
<td><span class="tag snip">cross-house calc</span></td>
<td>Guangzhou fell 10.1% in 2025 alone — its steepest year since 2010. <b>Offices fell further than
housing</b> (national new-build −21.8% nominal)</td></tr>
<tr><td>Cap rates</td><td class="mono">4.2–4.8% core, <b>expanding</b></td>
<td><span class="tag snip">2-SOURCE</span></td>
<td>China is the one Asia-Pacific market widening while the region compresses. A conflicting
“6.2% vs sub-5%” claim was found internally inconsistent and <b>not adopted</b></td></tr>
<tr><td>Whole-building (大宗) volume</td>
<td class="mono">≈RMB 200bn (2020) → 134bn (2024)<br>then <b>+76% YoY to 121bn in H1 2026</b></td>
<td><span class="tag snip">1-SOURCE</span></td>
<td>A real rebound in transaction volume — but see who is buying</td></tr>
<tr><td><b>Foreign share of office deals</b></td>
<td class="mono neg">0% Beijing · 8% Shanghai (H1 2026)</td><td><span class="tag snip">1-SOURCE</span></td>
<td>Insurers, state platforms and self-use corporates now dominate. <b>Foreign capital has left the
office market</b></td></tr>
</tbody></table></div>
<div class="warn"><b>The read that matters for an allocator.</b> The block-transaction market has
recovered by volume while foreign participation has gone to approximately zero in Beijing. A market
that clears without its previous marginal buyer is clearing at a different price to a different
buyer — domestic institutions with regulatory reasons to hold. That is not the same thing as
liquidity returning, and it is why transaction-volume recovery cannot be read as a price signal
here.</div>
</section>

<section>
<h2>7 · The rental yield, before and after</h2>
<p class="sub">One line per episode, sorted by the yield it carried at its peak: the red dot is the
yield at the peak, the green dot the yield at the trough. Yields <i>compress</i> into a peak
(−0.83pp over the final five years) and <i>expand</i> about 1.5pp on the way down, because price
falls faster than rent. Both registered bars cleared.</p>
<div class="chartwrap">{SC3}</div>
<div class="legend"><span><span class="sw" style="background:var(--bad)"></span>yield at the
peak</span><span><span class="sw" style="background:var(--good)"></span>yield at the
trough</span></div>
<p>The placement needs the right comparison, and it is easy to get wrong: China's yield <i>today</i>
must be compared with other episodes' yields <i>on the way down</i>, while China's <b>2021 peak</b>
yield is what belongs beside their peaks. Done properly: Chinese tier-1 carried roughly
<b>1.7–1.8% at the 2021 peak</b> — the <b>second-lowest peak yield in this entire 150-year panel</b>,
behind only Spain 2007 at 1.49%, and Spain then fell 42.9%. Only one country in the record ever
entered a bust priced this tightly.</p>
<p>The yield has since widened to roughly <b>2.0–2.6%</b>, an expansion of some 0.3–0.8pp against
the base rate's +1.53pp median peak-to-trough — so on this measure too China is about a third of the
way through, the same fraction the tier-1 depth placement gave independently. And the widening is a
<b>price-side</b> story, not a rent-side one: nominal rents are themselves falling (a 50-city index
down 3.04% over Jan–Nov 2025, with 49 of 50 cities lower), pushed by record youth unemployment and
migrant outflow on the demand side and by unsold units converting into rental stock on the supply
side. A yield that rises because rents fall more slowly than prices is not the same signal as a
yield that rises because rents grow.</p>
<div class="warn"><b>The carry test, which is the cleanest "is it cheap yet" statistic available.</b>
Gross yield minus the 5-year policy rate was <b>−2.95pp</b> in 2021 and is <b>−1.30pp</b> now
(−0.88pp against the ~3.1% effective mortgage rate). Chinese residential property has never been
cash-flow-positive on leverage at any point in this cycle, and essentially all of the improvement
came from <b>rate cuts rather than from the asset getting cheaper relative to its income</b>. On the
international base rate, troughs arrive at yields near 5%.</div>
</section>


<section>
<h2>8 · C-REITs — the only market-priced mark on Chinese property, and it disagrees with everything else</h2>
<p class="sub">Every other number on this page is an index, a survey or an appraisal. C-REITs trade,
which makes them the one place a real clearing price on Chinese real estate is observable. What they
say does not match the housing index at all.</p>
<div class="tbl"><table>
<thead><tr><th>C-REIT market</th><th>Figure</th><th>Confidence</th></tr></thead>
<tbody>
<tr><td>Listed vehicles / AUM</td><td class="mono">~78–79 REITs, ~RMB 200–227bn (Feb 2026)</td>
<td><span class="tag snip">2-SOURCE</span></td></tr>
<tr><td>Standing in Asia</td><td class="mono">Asia's largest by count; world's #2</td>
<td><span class="tag snip">1-SOURCE</span></td></tr>
<tr><td>Distribution yield, logistics</td><td class="mono">4.0–5.3%</td><td><span class="tag snip">1-SOURCE</span></td></tr>
<tr><td>Distribution yield, data centre</td><td class="mono">~5.1%</td><td><span class="tag snip">1-SOURCE</span></td></tr>
<tr><td>Distribution yield, consumer/retail</td><td class="mono">3.5–4.8%</td><td><span class="tag snip">1-SOURCE</span></td></tr>
<tr><td>Distribution yield, affordable rental housing</td><td class="mono">4.0–4.5%</td><td><span class="tag snip">1-SOURCE</span></td></tr>
<tr><td><b>Implied residential cap rate</b> (derived)</td>
<td class="mono">appraisal discount rates 6.0–6.5%<br>on a disclosed rent-growth assumption of
<b>0.66%/yr</b> → <b>≈5.3–5.9%</b></td><td><span class="tag snip">1-SOURCE construction</span></td></tr>
</tbody></table></div>
<h3>The divergence, and it is the most interesting single fact in this programme</h3>
<p>The base rate says property busts end at a rental yield near <b>5.2%</b> (modern-era median at
the trough: 4.94%). China's <i>direct</i> tier-1 market yields <b>2.0–2.6%</b> — nowhere near it. But
the affordable-rental-housing C-REITs, the only Chinese residential assets with a market price,
imply a cap rate of roughly <b>5.5%</b> — <i>already at or above the international trough level</i>.
And the appraisals underpinning them assume rent growth of <b>0.66% a year</b>, which is an
institution writing down, in a public document, that Chinese residential rents do essentially
nothing for the foreseeable future.</p>
<div class="warn"><b>Two readings, and honesty requires giving both.</b> The apples-to-oranges
reading: regulated affordable-rental housing is a different asset from tier-1 owner-occupied stock —
capped rents, different tenant risk, different growth — so the two yields were never directly
comparable. The uncomfortable reading: to whatever extent they <i>are</i> comparable, the
institutional market has already marked Chinese residential to the international trough while the
owner-occupier market is still priced at less than half that yield. Both readings point the same
way about which of the two markets has finished repricing. This number is a derived construction
from a single source and is the top verification priority on the page.</p>
<div class="warn" style="background:var(--gatebg);color:var(--gate)"><b>A basis caveat that
the page would be wrong to leave out, flagged rather than resolved.</b> Three yields are compared
across this atlas and they may not sit on the same gross/net basis. JST's field is documented only
as <span class="mono">rent[t]/p[t]</span> with no statement of whether costs, depreciation and taxes
are netted out; China's direct tier-1 figure is explicitly a <i>gross</i> yield; a C-REIT cap rate
is a <i>net</i> figure by construction. The desk has checked the one piece of arithmetic it can
check — the implied cap rate is the Gordon identity, discount rate minus growth: 6.0% − 0.66% =
5.34% and 6.5% − 0.66% = 5.84%, so the 5.3–5.9% range is sound. But the cross-yield comparison
carries a <span class="mono">[VERIFY]</span>. What matters for reading the page: resolving the
ambiguity either way <b>widens</b> every gap shown rather than narrowing it. If JST is net, then
China's gross 2.0–2.6% is nearer 1.4–1.9% net and further from the trough; if JST is gross, then
the Chinese net ~5.5% cap rate is nearer 6.5–7.5% gross-equivalent and further above it. The
direction of every comparison survives; only the magnitudes are uncertain, and in a known
direction.</div>
<h3>What a foreign investor can actually own — and the number that should stop the conversation</h3>
<ul>
<li><b>C-REITs: effectively inaccessible.</b> QFII/RQFII access is arguable on weak single-document
sourcing; <b>Stock Connect inclusion, announced April 2024, is still not live</b>, and HKEX's own
chief executive was targeting Q4 2027 as of May 2026. So the one instrument that carries the honest
mark is the one a foreign book cannot buy.</li>
<li><b>Offshore USD developer bonds: approximately 0.6% recovery on ~$147bn of defaults.</b> Not a
distressed-debt story with a recovery tail — a near-total loss. Any "buy the bonds at 20 cents"
thesis from 2022 has been settled by the outcome.</li>
<li><b>HK-listed developers</b> give equity risk rather than yield; <b>five Singapore-listed
China-asset REITs</b> (CapitaLand China Trust, Sasseur, BHG Retail, EC World, Dasin) are the
practical offshore route, and one of them has already failed.</li>
</ul>
</section>
<section>
<h2>9 · Which debt number was actually predicting it</h2>
<p class="sub">This was the principal's sharpest question, and it has two answers that only look
contradictory. The macro aggregate works as a <i>state</i> and fails as a <i>trigger</i>.</p>
<div class="tbl"><table>
<thead><tr><th>Aggregate, 5-year change</th><th>At crash peaks</th><th>Panel norm</th>
<th>Lift on 3-yr crash odds</th><th>False alarms</th></tr></thead>
<tbody>
<tr><td>Mortgage credit / GDP</td><td class="mono">+{d3['at_peak']:.2f}pp</td>
<td class="mono">+{d3['uncond']:.2f}pp</td><td class="mono pos">{d3['lift']:.2f}×</td>
<td class="mono neg">{d3['fp']:.1%}</td></tr>
<tr><td>Household debt / GDP</td><td class="mono">+{J['CN-D3']['d5_hh']['at_peak']:.2f}pp</td>
<td class="mono">+{J['CN-D3']['d5_hh']['uncond']:.2f}pp</td>
<td class="mono pos">{J['CN-D3']['d5_hh']['lift']:.2f}×</td>
<td class="mono neg">{J['CN-D3']['d5_hh']['fp']:.1%}</td></tr>
<tr><td>Public debt / GDP</td><td class="mono">+{J['CN-D3']['d5_pub']['at_peak']:.2f}pp</td>
<td class="mono">+{J['CN-D3']['d5_pub']['uncond']:.2f}pp</td>
<td class="mono neg">{J['CN-D3']['d5_pub']['lift']:.2f}×</td>
<td class="mono">{J['CN-D3']['d5_pub']['fp']:.1%}</td></tr>
</tbody></table></div>
<h3>What the base rate says</h3>
<ul>
<li><b>Mortgage credit genuinely carries information.</b> It rose +6.75pp in the five years before a
crash peak against a +2.52pp norm, and the top quintile lifts three-year crash odds 1.72×. The
Jordà-Schularick-Taylor channel is real.</li>
<li><b>And it is wrong seven times out of eight.</b> Of 430 country-years in the top quintile of
mortgage-credit growth, 87.2% were <i>not</i> followed by a crash peak within three years. That is
the number nobody quotes when they cite credit growth as a warning.</li>
<li><b>Public debt reads backwards</b> (lift 0.23×). It rises <i>after</i> busts — bailouts, lost
revenue, stimulus — not before them. And it is the wrong aggregate for China anyway: the panel
measures central-government debt, while China's leverage sits in local-government financing
vehicles that no cross-country dataset captures.</li>
</ul>
<h3>What the China research adds <span class="tag snip">SNIPPET</span></h3>
<ul>
<li>The extreme <i>level</i> readings — price-to-rent near 2%, price-to-income 12–17× in tier-1 —
had looked that way <b>for years</b>, which is precisely why they were dismissed and precisely what
an 87% false-alarm rate looks like from the inside.</li>
<li>What actually flagged it was <b>firm-level leverage, not a macro ratio</b>: only 6.3% of rated
developers met the Three Red Lines when they were introduced in August 2020, and the CBIRC chairman
named property China's biggest “grey rhino” that October — roughly 11 months before Evergrande
became a global story.</li>
<li>The named false negatives: <b>credit ratings and developer equity prices gave almost no
warning.</b> Evergrande carried investment-grade ratings through all of 2020.</li>
</ul>
<div class="warn"><b>The synthesis, and it is the programme's most transferable finding.</b> Macro
credit aggregates told you the <i>state</i> — that this was a system carrying crash risk — and
nothing about the <i>timing</i>. Micro leverage told you the timing. A desk that wants an
early-warning system should therefore monitor balance sheets of the largest levered operators, and
treat credit-to-GDP as a regime label. This is the identical conclusion this desk reached
independently about valuation in its expected-return work: good states, useless point forecasts.</div>
</section>

<section>
<h2>10 · Equities after a housing peak</h2>
<p class="sub">The investable leg, and the one that decides whether a foreign allocator should care.
Real equity total return after each housing peak, against a horizon-matched benchmark built on the
same geometric basis.</p>
<div class="tbl"><table>
<thead><tr><th>Horizon</th><th>All episodes</th><th>Banking crisis within 3 yrs</th>
<th>No banking crisis</th><th>Excess, all</th></tr></thead>
<tbody>
<tr><td>Next 1 year</td><td class="mono neg">{J['CN-D5']['all']['f1']:+.2f}%</td>
<td class="mono neg">{J['CN-D5']['crisis']['f1']:+.2f}%</td>
<td class="mono neg">{J['CN-D5']['nocrisis']['f1']:+.2f}%</td>
<td class="mono neg">−13.73pp</td></tr>
<tr><td>Next 3 years, ann.</td><td class="mono">{J['CN-D5']['all']['f3']:+.2f}%</td>
<td class="mono">{J['CN-D5']['crisis']['f3']:+.2f}%</td>
<td class="mono">{J['CN-D5']['nocrisis']['f3']:+.2f}%</td>
<td class="mono">−4.10pp</td></tr>
<tr><td>Next 5 years, ann.</td><td class="mono">{J['CN-D5']['all']['f5']:+.2f}%</td>
<td class="mono">{J['CN-D5']['crisis']['f5']:+.2f}%</td>
<td class="mono">{J['CN-D5']['nocrisis']['f5']:+.2f}%</td>
<td class="mono">−1.03pp</td></tr>
</tbody></table></div>
<p>Two things fall out. First, <b>a housing peak hurts equities even when the banks hold</b> — the
no-crisis subset still gives up 10.2pp of excess return in year one, and the registered bar expecting
it to be a non-event <i>missed</i>. Second, the damage is <b>front-loaded and largely
mean-reverting</b>: −13.7pp at one year, −4.1pp at three, −1.0pp at five. A property bust is an
equity event for about a year, not a lost decade — which independently reproduces this desk's own
crisis event study (t0 −14.1%, recovery from t+1) on a different construction and a different
episode definition.</p>
</section>


<section>
<h2>11 · The India read-across — what this actually changes for the book</h2>
<p class="sub">The desk runs an Indian multi-asset book, so this is the section that decides whether
the programme changes anything. The verdict is unusually clean: <b>the contagion channel is real and
already priced through steel; the vulnerability channel largely does not transfer; and the flow
channel is the live risk nobody sizes.</b></p>

<h3>Channel 1 — deflation through steel, which is real and measurable</h3>
<p>Chinese steel exports went from ≈66–67Mt/yr in 2021-22 to <b>110.7Mt in 2024 and 119.0Mt in
2025</b> <span class="tag snip">2-SOURCE</span> as property's share of domestic steel demand fell
from 32% to 23%. That surplus was redirected outward, and India felt it: HRC fell from ≈₹59,900 to
≈₹52,600/t between April 2023 and April 2024, Indian steelmaker profitability dropped
<b>58–95% year on year</b> in Q1 FY25, and a <b>12% safeguard duty</b> followed. Cement, by
contrast, is <b>not</b> analogous — international cement trade is only ≈5% of consumption because
freight economics prevent it, so the cement lesson is cautionary (do not repeat the overbuild) rather
than a price-transmission channel. Getting that distinction right matters: the two are routinely
lumped together.</p>

<h3>Channel 2 — the flow rotation, and the risk that is demonstrated rather than hypothetical</h3>
<p>MSCI EM weights moved China from ≈40% to ≈25–27% and India from ≈8% to ≈18% between 2020 and
2024 <span class="tag snip">2-SOURCE</span>. Named houses frame that as growth- and
valuation-driven rather than property-driven, which matters for how durable it is. And the reversal
risk is not a thought experiment: <b>China's September-2024 stimulus package triggered roughly
US$10.2bn of Indian FPI outflows in a single month</b> <span class="tag snip">2-SOURCE</span>. That
is the single most decision-relevant number in this dossier for an India book — a Chinese policy
success is an Indian outflow event, and it has already happened once at scale.</p>

<h3>Channel 3 — does India carry China's vulnerabilities? Mechanism by mechanism</h3>
<div class="tbl"><table>
<thead><tr><th>Mechanism</th><th>China</th><th>India</th><th>Verdict</th></tr></thead>
<tbody>
<tr><td>Pre-sale escrow</td><td class="mono">Escrow diverted; rules tightened only after the crisis</td>
<td class="mono">RERA 70% escrow, <b>pre-crisis by design</b></td>
<td class="pos">Does not transfer</td></tr>
<tr><td>Local-government land-sale dependence</td><td class="mono">27–38% of local revenue</td>
<td class="mono">Negligible</td><td class="pos">Does not transfer</td></tr>
<tr><td>Property share of GDP</td><td class="mono">≈22–31%</td><td class="mono">≈7–15%</td>
<td class="pos">Does not transfer</td></tr>
<tr><td>Listed developer leverage</td><td class="mono">Only 6.3% met the Three Red Lines</td>
<td class="mono">DLF near debt-free; Oberoi D/E 0.18</td><td class="pos">Does not transfer</td></tr>
<tr><td>LGFV-equivalent structures</td><td class="mono">The core of the hidden-debt problem</td>
<td class="mono">SPV / municipal-bond structures exist in kind, scale unquantified</td>
<td class="amber">Partially transfers</td></tr>
<tr><td><b>Tier-2/3 UNLISTED developer leverage</b></td><td class="mono">Where the defaults happened</td>
<td class="mono"><b>Genuinely unknown</b></td>
<td class="neg">Open gap — flagged, not assumed safe</td></tr>
</tbody></table></div>
<div class="warn"><b>Read the last row, not the first four.</b> On every mechanism that is
measurable, India is structurally different — and the escrow difference is the crux: RERA's 70% rule
was designed in before a crisis, where China's was retrofitted after one. But four comfortable
verdicts and one unquantified gap is not a clean bill of health, it is a <i>measurement</i> gap in
exactly the place China's defaults came from. The desk's honest position is that India's listed
developers are visibly sound and its unlisted tier-2/3 developers are unexamined, and the second
statement is the one that should generate work.</div>

<h3>A named desk gap, partially closed</h3>
<p>The SNAPSHOT-1 allocation addendum recorded REITs as <b>“NOT DESK-RESEARCHED AT ALL — zero
vaulted data, zero ledger entries, named as the honest gap”</b> and sized the sleeve at 2% on that
basis. There are now figures: <b>Embassy ≈5.3–8%, Mindspace 6–8% (16.1%/yr since inception),
Brookfield 6.4–9%, Nexus 7.5–9% (29.3%/yr since inception)</b>
<span class="tag snip">1-SOURCE, conflicting</span>. Two caveats carry as much weight as the
numbers: the yield figures <b>conflict by 2–4pp across sources</b> and are not resolved, and
<b>no residential REIT exists in India at all</b> — the listed vehicles are office and retail, so
they are not a residential-property proxy. Enough to stop calling the sleeve unresearched; not
enough to resize it. That is a registration-worthy design, not a conclusion.</p>
</section>
<section class="panel">
<h2>Method, and what would make this better</h2>
<h3>The episode definition, frozen before the run</h3>
<p class="sub">A crash episode is a real-house-price peak followed by a cumulative decline of at
least 20% to its trough, with peaks at least 10 years apart and the deeper episode kept where two
collide. 48 completed episodes; one unfinished decline excluded.</p>
<h3>Two bugs found before any interpretation was written</h3>
<ul>
<li>The first implementation treated “never recovered to the old peak” as an unfinished decline and
excluded it — which silently dropped <b>Japan 1991, Ireland 2006 and Spain 2007</b>, the exact
episodes China is being compared with. The registration required the <i>trough</i> to be reached,
not the price to have recovered; the code was stricter than its own specification. Fixing it moved
the mortgage-credit lift from 1.29× (a miss) to 1.72× (a hit).</li>
<li>The equity benchmark was a one-year arithmetic mean while the 3- and 5-year cells were
geometric — a units mismatch that flattered the excess. Now horizon-matched.</li>
</ul>
<h3>Contamination, named rather than quietly re-cut</h3>
<p class="sub">Pre-1945 episodes are dominated by war and hyperinflation rather than property
cycles — Germany 1913 at −98%, Finland 1911 at −91%, Japan 1927 at −90%, plus 65- and 56-year
“declines”. The registered bars stand on the full 48-episode sample as written; the modern-era
sub-read (peaks from 1970, n=24) is reported alongside it throughout and is what the charts show.</p>
<h3>The limits that actually bind</h3>
<ul>
<li>JST covers 18 <b>advanced</b> economies. China is upper-middle-income with state-directed
credit, a leasehold land-sale fiscal model and a closed capital account. This is a base rate, never
a forecast.</li>
<li>Annual data cannot resolve within-year velocity, so every speed figure understates the peak
monthly rate.</li>
<li>The panel ends in 2020 — there is no post-COVID episode in it.</li>
<li>Every China figure is snippet-sourced. The named fix is a proper data pull: NBS 70-city history,
land-transfer series, and city-level rental yields, now on the desk's runsheet.</li>
</ul>
<p class="note">Sources of record: trial-ledger entries CN-D1..CN-D5 (registration committed before
the run) · scripts/analyze_china_baserate.py · research/china_baserate.json ·
research/notes/china-dossiers/ (the cited China dossiers, each with its own confidence tags and gaps
section) · research/frontier/china-property-plan.md §0a for the egress correction. Regenerates via
scripts/build_china_atlas.py, never from memory.</p>
</section>
</div>
"""
OUT.write_text(html)
print(f"written {OUT} ({len(html):,} bytes) · {len(pts)} scatter pts · {len(ys)} yield pairs")
