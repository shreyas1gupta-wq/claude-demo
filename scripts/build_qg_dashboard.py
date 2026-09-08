"""Build the Quality & Growth Factor Atlas dashboard (QG-D1/D2 prints + factor evidence).
Reads research/notes/qg_d2_stats.json + vault factor CSVs -> docs/learn/artifacts/
quality-growth-factor-atlas.html. All numbers are booked ledger prints; provenance and
artifact flags rendered inline."""
import json

import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"
J = json.load(open("/home/user/claude-demo/research/notes/qg_d2_stats.json"))

ff = pd.read_csv(f"{V}/factors_us/ff6_monthly_1963_2020.csv", parse_dates=["date"]).set_index("date")
q5 = pd.read_csv(f"{V}/factors_us/q5_monthly_1967_2019.csv", parse_dates=["date"]).set_index("date")

# cumulative log growth paths for the factor chart
paths = {}
for nm, s in [("RMW", ff.RMW), ("CMA", ff.CMA), ("q ROE", q5.R_ROE), ("q EG", q5.R_EG)]:
    eq = (1 + s.dropna()).cumprod()
    paths[nm] = np.log(eq)

W, H, PAD = 860, 300, 42
t0 = min(p.index[0] for p in paths.values())
t1 = max(p.index[-1] for p in paths.values())
ymin = min(p.min() for p in paths.values())
ymax = max(p.max() for p in paths.values())


def xy(idx, val):
    x = PAD + (idx - t0).days / (t1 - t0).days * (W - 2 * PAD)
    y = H - PAD - (val - ymin) / (ymax - ymin) * (H - 2 * PAD)
    return x, y


COLS = {"RMW": "var(--s1)", "CMA": "var(--s2)", "q ROE": "var(--s3)", "q EG": "var(--s4)"}
lines = []
for nm, p in paths.items():
    sub = p.iloc[::3]
    pts = " ".join(f"{xy(d, v)[0]:.1f},{xy(d, v)[1]:.1f}" for d, v in sub.items())
    ex, ey = xy(p.index[-1], p.iloc[-1])
    lines.append(
        f'<polyline points="{pts}" fill="none" stroke="{COLS[nm]}" stroke-width="2"/>' +
        f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="4" fill="{COLS[nm]}"><title>{nm}: log growth {p.iloc[-1]:+.2f} at {p.index[-1].year}</title></circle>' +
        f'<text x="{min(ex + 6, W - 4)}" y="{ey + 4:.1f}" class="dl" fill="{COLS[nm]}">{nm}</text>')
gy = []
for lv in [0, 1, 2, 3]:
    if ymin <= lv <= ymax:
        _, y = xy(t1, lv)
        gy.append(f'<line x1="{PAD}" y1="{y:.1f}" x2="{W - PAD}" y2="{y:.1f}" class="grid"/>'
                  f'<text x="{PAD - 6}" y="{y + 4:.1f}" class="tick" text-anchor="end">{np.exp(lv):.0f}x</text>')
for yr in [1970, 1980, 1990, 2000, 2010, 2020]:
    x, _ = xy(pd.Timestamp(f"{yr}-01-01"), ymin)
    gy.append(f'<text x="{x:.1f}" y="{H - PAD + 18}" class="tick" text-anchor="middle">{yr}</text>')
factor_svg = (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Cumulative growth of long-short factor portfolios, log scale">' +
              "".join(gy) + "".join(lines) + "</svg>")


def bars(d, w=520, h=210, fmt="{:+.1f}", flag=None):
    keys = sorted(int(k) for k in d)
    vals = [d[k] if isinstance(list(d)[0], int) else d[str(k)] for k in keys]
    vmax = max(max(vals), 0); vmin = min(min(vals), 0)
    rng = vmax - vmin or 1
    bw = (w - 50) / len(keys) - 6
    out = []
    for i, (k, v) in enumerate(zip(keys, vals)):
        x = 40 + i * ((w - 50) / len(keys)) + 3
        y0 = 16 + (vmax - max(v, 0)) / rng * (h - 52)
        bh = abs(v) / rng * (h - 52)
        out.append(f'<rect x="{x:.1f}" y="{y0:.1f}" width="{bw:.1f}" height="{max(bh, 1):.1f}" rx="3" class="bar">'
                   f'<title>D{k}: {fmt.format(v)}%/yr</title></rect>')
        out.append(f'<text x="{x + bw / 2:.1f}" y="{h - 20}" class="tick" text-anchor="middle">{k}</text>')
        if k in (keys[0], keys[-1]) or v == max(vals) or v == min(vals):
            out.append(f'<text x="{x + bw / 2:.1f}" y="{y0 - 5:.1f}" class="dl2" text-anchor="middle">{fmt.format(v)}</text>')
    zy = 16 + vmax / rng * (h - 52)
    out.append(f'<line x1="38" y1="{zy:.1f}" x2="{w - 8}" y2="{zy:.1f}" class="axis"/>')
    return f'<svg viewBox="0 0 {w} {h}" role="img">' + "".join(out) + "</svg>"


def heat(mat, rows="ROE", cols="axis", flag=False):
    a = np.array(mat)
    lo, hi = a.min(), a.max()
    cells = ""
    for i in range(5):
        cells += f'<tr><th class="rl">{rows} Q{i + 1}</th>'
        for j2 in range(5):
            v = a[i][j2]
            t = (v - lo) / (hi - lo or 1)
            cells += (f'<td style="--t:{t:.2f}" title="{rows} Q{i + 1} x {cols} Q{j2 + 1}: {v:+.1f}%/yr">{v:.1f}</td>')
        cells += "</tr>"
    head = "".join(f"<th>Q{j + 1}</th>" for j in range(5))
    return (f'<table class="hm{" suspect" if flag else ""}"><thead><tr><th></th>{head}</tr></thead>'
            f'<tbody>{cells}</tbody></table>')


def hor_table(block, labels):
    hs = [12, 36, 60, 120]
    head = "".join(f"<th>{l}</th>" for l in labels) + "<th>spread</th>"
    rows = ""
    for h in hs:
        r = block[str(h)] if str(h) in block else block[h]
        vals = [r[str(k)] if str(k) in r else r[k] for k in range(1, len(labels) + 1)]
        sp = vals[-1] - vals[0]
        cells = "".join(f"<td>{v:.1f}</td>" for v in vals)
        rows += f"<tr><td>{h // 12}y</td>{cells}<td><b>{sp:+.1f}</b></td></tr>"
    return (f'<table class="plain"><thead><tr><th>fwd</th>{head}</tr></thead><tbody>{rows}</tbody></table>')


d3 = J["qg_d3"]
d3_all = hor_table(d3["all"], [f"D{i}" for i in range(1, 11)])
d3_big = hor_table(d3["big"], [f"Q{i}" for i in range(1, 6)])

c1 = {int(k): v for k, v in J["c1"].items()}
c6 = {int(k): v for k, v in J["c6"].items()}
big_row = {1: 7.4, 2: 12.0, 3: 7.9, 4: 7.9, 5: 6.2}  # booked diagnostic: ROE quintiles within largest size quintile
c17 = {int(k): v for k, v in J["c17"].items()}
c27 = {int(k): v for k, v in J["c27"].items()}

html = f"""<title>Quality &amp; Growth Factor Atlas</title>
<style>
:root {{
  --bg:#f6f5f1; --panel:#fdfdfb; --ink:#212528; --ink2:#5a5f63; --mut:#8a8f93;
  --line:#e2e0d8; --s1:#2a78d6; --s2:#eb6834; --s3:#1baf7a; --s4:#eda100;
  --heat:42,120,214; --bad:#b3352b; --badbg:#f9e9e7; --good:#1f7a4d; --goodbg:#e7f3ec;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg:#15181c; --panel:#1d2126; --ink:#e8eaec; --ink2:#aab0b5; --mut:#7d838a;
  --line:#30353b; --s1:#3987e5; --s2:#d95926; --s3:#199e70; --s4:#c98500;
  --heat:57,135,229; --bad:#e0736a; --badbg:#3a2422; --good:#5fbe8e; --goodbg:#1e3328;
}} }}
:root[data-theme="dark"] {{
  --bg:#15181c; --panel:#1d2126; --ink:#e8eaec; --ink2:#aab0b5; --mut:#7d838a;
  --line:#30353b; --s1:#3987e5; --s2:#d95926; --s3:#199e70; --s4:#c98500;
  --heat:57,135,229; --bad:#e0736a; --badbg:#3a2422; --good:#5fbe8e; --goodbg:#1e3328;
}}
body {{ background:var(--bg); color:var(--ink); font:15px/1.55 "Source Sans 3",system-ui,sans-serif;
  margin:0; padding:28px 20px 60px; }}
.wrap {{ max-width:1060px; margin:0 auto; display:flex; flex-direction:column; gap:26px; }}
h1 {{ font:700 30px/1.15 "Archivo",system-ui,sans-serif; letter-spacing:-.3px; margin:0; text-wrap:balance; }}
h2 {{ font:650 19px/1.2 "Archivo",system-ui,sans-serif; margin:0 0 4px; }}
.sub {{ color:var(--ink2); max-width:70ch; margin:6px 0 0; }}
.prov {{ display:flex; gap:14px; flex-wrap:wrap; font:12px "IBM Plex Mono",monospace; color:var(--mut); }}
.badge {{ padding:1px 8px; border:1px solid var(--line); border-radius:10px; }}
.verdicts {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:12px; }}
.v {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:14px 16px; }}
.v b {{ font-family:"Archivo"; font-size:16px; }}
.v .num {{ font:600 26px/1.2 "IBM Plex Mono",monospace; font-variant-numeric:tabular-nums; }}
.panel {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:18px 20px; }}
.grid2 {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(430px,1fr)); gap:18px; }}
.grid3 {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:18px; }}
svg {{ width:100%; height:auto; display:block; }}
.bar {{ fill:var(--s1); opacity:.92 }} .bar:hover {{ opacity:1 }}
.grid {{ stroke:var(--line); stroke-width:1 }}
.axis {{ stroke:var(--mut); stroke-width:1.2 }}
.tick {{ font:11px "IBM Plex Mono",monospace; fill:var(--mut) }}
.dl {{ font:600 12px "Archivo",sans-serif }}
.dl2 {{ font:11px "IBM Plex Mono",monospace; fill:var(--ink2) }}
table.hm {{ border-collapse:separate; border-spacing:2px; width:100%;
  font:12.5px "IBM Plex Mono",monospace; font-variant-numeric:tabular-nums; }}
.hm th {{ color:var(--mut); font-weight:500; padding:2px 4px; }}
.hm .rl {{ text-align:right; white-space:nowrap; }}
.hm td {{ text-align:center; padding:7px 4px; border-radius:4px; color:var(--ink);
  background:rgba(var(--heat), calc(.08 + .5*var(--t))); }}
.hm.suspect td {{ opacity:.65 }}
.flag {{ display:inline-block; font:600 11px "Archivo"; letter-spacing:.4px; padding:2px 8px;
  border-radius:9px; margin-left:6px; vertical-align:2px; }}
.flag.bad {{ color:var(--bad); background:var(--badbg); }}
.flag.good {{ color:var(--good); background:var(--goodbg); }}
.kv {{ display:grid; grid-template-columns:auto 1fr; gap:4px 14px; font-size:14px; }}
.kv dt {{ color:var(--ink2); }} .kv dd {{ margin:0; font-family:"IBM Plex Mono",monospace; font-variant-numeric:tabular-nums; }}
ul.edge {{ margin:8px 0 0; padding-left:20px; }} ul.edge li {{ margin:5px 0; max-width:80ch; }}
.note {{ font-size:13px; color:var(--mut); max-width:90ch; }}
td, th {{ font-variant-numeric:tabular-nums; }}
.tblwrap {{ overflow-x:auto; }}
table.plain {{ border-collapse:collapse; font-size:13.5px; min-width:480px; }}
.plain th, .plain td {{ padding:5px 12px; border-bottom:1px solid var(--line); text-align:right; }}
.plain th:first-child, .plain td:first-child {{ text-align:left; }}
</style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700&family=Source+Sans+3:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<div class="wrap">
<header>
<h1>Quality &amp; Growth Factor Atlas</h1>
<p class="sub">Every number is a booked print from the Cycle Program register (entries QG-D1, QG-D2; census 1,094).
Firm panel: 1,207 US stocks, equal-weight, 1999&ndash;2019 (Coqueret&ndash;Guida, survivorship tilt declared).
Factors: FF5/FF6 1963&ndash;2020 + HXZ q-factors 1967&ndash;2019, value-weight. Paper, zero costs.</p>
<div class="prov"><span class="badge">BOOKED = ledger print</span><span class="badge">ARTIFACT = construction-dominated, not consumed</span><span class="badge">FLAGGED = registered as not-consumed</span><span class="badge">India firm data: gated on runsheet pulls</span></div>
</header>

<div class="verdicts">
<div class="v"><b>Profitability pays &mdash; modestly, value-weighted</b><div class="num">+2.8 to +6.3%/yr</div>
RMW Sharpe 0.41 &middot; q&nbsp;ROE Sharpe 0.75, 57 years. Real, slow, defensive &mdash; not a headline alpha.</div>
<div class="v"><b>Growth is not worth chasing</b><div class="num">&asymp; 0 added</div>
EPS-growth ladders flat-to-inverted; within high-ROE names, growth terciles add nothing (11.6 / 9.7 / 10.4 %/yr).</div>
<div class="v"><b>The combination is the edge</b><div class="num">Sharpe 0.49</div>
50/50 value+profitability beats value (0.32) and profitability (0.41) alone; cheap-quality beats expensive-quality by ~17pp/yr in-panel.</div>
</div>

<section class="panel">
<h2>ROE deciles: the ladder, and the trap it exposes <span class="flag bad">ARTIFACT CAUGHT</span></h2>
<p class="sub">The raw equal-weight panel ladder INVERTS (low-ROE &ldquo;wins&rdquo; +29.7 vs +11.9%/yr) &mdash; but the inversion collapses to
&minus;1.3pp inside the largest size quintile, and 33% of low-ROE names sit in the smallest quintile (vs 7% of high-ROE).
Equal-weight survivor panels manufacture junk premia. The value-weighted factor evidence (below) carries the truth.</p>
<div class="grid2">
<div><h2 style="font-size:15px">Fwd-1m return by ROE decile, %/yr (EW panel, 1999-2019)</h2>{bars(c1)}</div>
<div><h2 style="font-size:15px">Same read, largest-cap quintile only (ROE quintiles)</h2>{bars(big_row, fmt="{:+.1f}")}
<p class="note">Large caps: +7.4 (Q1) vs +6.2 (Q5) &mdash; no premium either way in this EW panel/era. The &ldquo;junk edge&rdquo; is a smallest-cap artifact.</p></div>
</div>
<dl class="kv" style="margin-top:12px">
<dt>D10 compounded (high ROE)</dt><dd>CAGR +11.6% &middot; Sharpe 0.72 &middot; maxDD &minus;50%</dd>
<dt>D1 compounded (junk)</dt><dd>CAGR +29.7% &middot; Sharpe 0.99 &middot; maxDD &minus;62% &mdash; untradeable artifact</dd>
<dt>D10&minus;D1 spread, up vs down months</dt><dd>&minus;38.1 up &middot; <b>+17.7 down</b> %/yr &mdash; quality is a down-market instrument</dd>
<dt>ROE persistence</dt><dd>12m rank-autocorr 0.69 &mdash; a quarterly signal, not a monthly one</dd>
</dl>
</section>

<section class="panel">
<h2>The cross matrices (fwd-1m EW mean, %/yr; darker = higher)</h2>
<p class="sub">Rows are ROE quintiles (Q5 = most profitable). Read WITHIN a row &mdash; absolute levels inherit the panel tilt.
Momentum and vol matrices are flagged: their within-row shapes contradict value-weighted evidence and are not consumed.</p>
<div class="grid3">
<div><h2 style="font-size:14px">&times; EPS growth <span class="flag good">THE GROWTH ANSWER</span></h2>{heat(J["c8"], cols="growth")}
<p class="note">In the Q5 (high-ROE) row the best cells are LOW/MID growth &mdash; growth adds nothing once quality is held.</p></div>
<div><h2 style="font-size:14px">&times; P/B (valuation) <span class="flag good">CHEAP-QUALITY</span></h2>{heat(J["c9"], cols="P/B")}
<p class="note">Within Q5: cheap 26.2 vs expensive 9.3 %/yr &mdash; the profitable-value corner, matching Novy-Marx.</p></div>
<div><h2 style="font-size:14px">&times; size <span class="flag bad">TILT VISIBLE</span></h2>{heat(J["c11"], cols="size")}
<p class="note">The whole left column (smallest quintile) glows &mdash; this is the artifact, made visible.</p></div>
<div><h2 style="font-size:14px">&times; leverage (SEC-D7 bridge)</h2>{heat(J["c12"], cols="leverage")}</div>
<div><h2 style="font-size:14px">&times; momentum <span class="flag bad">NOT CONSUMED</span></h2>{heat(J["c10"], cols="momentum", flag=True)}</div>
<div><h2 style="font-size:14px">&times; volatility <span class="flag bad">NOT CONSUMED</span></h2>{heat(J["c13"], cols="volatility", flag=True)}</div>
</div>
</section>

<section class="panel">
<h2>Should we focus on growth? The direct reads</h2>
<div class="grid2">
<div><h2 style="font-size:15px">Fwd-1m by EPS-growth decile, %/yr</h2>{bars(c6)}
<p class="note">Flat-to-inverted &mdash; chased growth earns nothing (LSV extrapolation, confirmed here).</p></div>
<div><h2 style="font-size:15px">Growth terciles WITHIN high-ROE names, %/yr</h2>{bars(c17, w=380)}
<p class="note">11.6 / 9.7 / 10.4 &mdash; once quality is held, more growth adds zero. Capex/sales ladder: flat (&minus;0.7pp D10&minus;D1).
Value-weighted confirmation: CMA (conservative-minus-aggressive investment) +3.0%/yr over 57y.</p></div>
</div>
</section>

<section class="panel">
<h2>The value-weighted factor evidence, 1963&ndash;2020 (growth of $1, log scale)</h2>
{factor_svg}
<div class="grid2" style="margin-top:10px">
<div class="tblwrap"><table class="plain"><thead><tr><th>Factor</th><th>CAGR</th><th>Sharpe</th><th>maxDD</th><th>Down-mo</th><th>Up-mo</th><th>Post-2013</th></tr></thead><tbody>
<tr><td>RMW (profitability)</td><td>+2.8%</td><td>0.41</td><td>&minus;41%</td><td>+9.3%/yr</td><td>&minus;1.2%/yr</td><td>+1.1%/yr</td></tr>
<tr><td>CMA (low investment)</td><td>+3.0%</td><td>0.46</td><td>&minus;21%</td><td>+12.1%/yr</td><td>&minus;2.8%/yr</td><td>&minus;2.5%/yr</td></tr>
<tr><td>q ROE (1967&ndash;2019)</td><td>+6.3%</td><td>0.75</td><td>&minus;30%</td><td colspan="2"></td><td></td></tr>
<tr><td>q EG (exp. growth) <span class="flag bad">FLAGGED</span></td><td>+10.0%</td><td>1.49</td><td>&minus;12%</td><td colspan="3">contested construction &mdash; registered as not-consumed</td></tr>
</tbody></table></div>
<div><dl class="kv">
<dt>RMW by decade, %/yr</dt><dd>{" &middot; ".join(f"{k}s {v:+.1f}" for k, v in c27.items())}</dd>
<dt>50/50 HML+RMW blend</dt><dd>Sharpe 0.49 vs HML 0.32, RMW 0.41 alone</dd>
<dt>Correlations</dt><dd>RMW&ndash;HML +0.07 &middot; RMW&ndash;Mkt &minus;0.21 &middot; RMW&ndash;UMD +0.10</dd>
</dl>
<p class="note">Down-month behavior is the real product: quality and conservatism pay when the market falls and cost a little when it rallies &mdash; the same during-crisis doctrine as SEC-D6/FUN-D3. Post-publication decay is visible (CMA negative since 2013).</p></div>
</div>
</section>

<section class="panel">
<h2>ROE &times; horizon: fwd 1y / 3y / 5y / 10y (median annualized %/yr) <span class="flag good">QG-D3</span></h2>
<p class="sub">Buy-and-hold compounding, overlapping monthly formations (flagged; ~10 independent 10y windows).
Medians collapse the mean-based junk inversion to a mild &minus;2 to &minus;4pp &mdash; the QG-D2 &ldquo;junk edge&rdquo; is skew from a few
equal-weight moonshots. The large-cap leg is the honest one, and it shows the FADE: <b>Q2 is the best column at every
horizon</b> &mdash; today&rsquo;s top-quintile ROE fades toward the mean while you hold it at a quality-premium price.</p>
<div class="grid2">
<div class="tblwrap"><h2 style="font-size:14px">All-panel deciles <span class="flag bad">EW TILT</span></h2>
{d3_all}</div>
<div class="tblwrap"><h2 style="font-size:14px">Largest-cap quintile only <span class="flag good">HONEST LEG</span></h2>
{d3_big}
<p class="note">Q5&minus;Q1 spread: +1.4pp (1y) &rarr; 0.0 (3y) &rarr; &minus;1.5 (5y) &rarr; &minus;2.1 (10y).
Attrition check: the panel has NO delisting truncation at any horizon (100% full coverage) &mdash; every absolute
level here is an upper bound, and junk legs are doubly flattered. Consumption: sort for high-but-not-extreme
profitability with persistence, never top-decile-at-any-price.</p></div>
</div>
</section>

<section class="panel">
<h2>Aggregate payout &amp; growth (QG-D1, Shiller 1871&ndash;2023)</h2>
<div class="kv">
<dt>High vs low payout &rarr; next-10y real earnings growth</dt><dd>+4.0 vs +1.8 %/yr (Arnott&ndash;Asness direction replicates)</dd>
<dt>The mechanism cell</dt><dd>high-payout months are depressed-earnings months <b>78%</b> of the time; the gap INVERTS (&minus;1.9pp) within non-depressed months</dd>
<dt>Consumption</dt><dd>aggregate payout = a repackaged earnings-state variable &mdash; no cells on payout timing</dd>
</dl>
</section>

<section class="panel">
<h2>The edge list &mdash; and what to avoid</h2>
<ul class="edge">
<li><b>Profitable-value combination</b> &mdash; the most replicated construction (blend Sharpe 0.49; cheap-quality corner). The future stock book&rsquo;s default sort. <i>Gated: as-filed India fundamentals.</i></li>
<li><b>Quality as the down-market sleeve</b> &mdash; RMW +9.3%/yr in down months; sizes the defensive tilt, never an after-crisis chase.</li>
<li><b>Never unconditional size; small + quality only</b> &mdash; junky smalls are where the artifact lives (the size matrix&rsquo;s left column).</li>
<li><b>Quality is slow</b> &mdash; ROE rank-autocorr 0.69 at 12m: quarterly rebalancing suffices; monthly turnover buys nothing.</li>
<li><b>Avoid</b>: chasing growth (ladders flat-to-inverted; CMA says conservative wins) &middot; equal-weight survivor backtests (three live demonstrations now) &middot; aggregate-payout timing &middot; the flagged q&nbsp;EG headline until independently re-verified &middot; post-2013 CMA-sized expectations.</li>
</ul>
<p class="note">Sources: ingest/vault/firm_panel + factors_us (two-pass authenticated, ~2020 vintages; two anchor
mis-specifications recorded honestly in AUTHENTICATION.md). India analogs are runsheet-gated: as-filed fundamentals,
SEBI pledge history, NSE quality-index live segments. Register: research/register/trial-ledger.md QG-D1/QG-D2.</p>
</section>
</div>
"""
open("/home/user/claude-demo/docs/learn/artifacts/quality-growth-factor-atlas.html", "w").write(html)
print("built", len(html), "bytes")
