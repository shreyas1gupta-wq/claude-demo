"""Build docs/learn/artifacts/construction-mechanics-atlas.html — the G1-G4 battery:
the rebalance grid, the concentration curve, dispersion-as-a-state, and the India
LTCG-threshold holding ladder. Every number is a booked print (ledger entry G1-G4,
desk-verified on two cells). House dashboard system."""
from pathlib import Path

R = Path("/home/user/claude-demo")
OUT = R / "docs/learn/artifacts/construction-mechanics-atlas.html"

html = """<title>Construction Mechanics Atlas</title>
<style>
:root {
  --bg:#f6f5f1; --panel:#fdfdfb; --ink:#212528; --ink2:#5a5f63; --mut:#8a8f93;
  --line:#e2e0d8; --s1:#2a78d6;
  --bad:#b3352b; --badbg:#f9e9e7; --good:#1f7a4d; --goodbg:#e7f3ec;
  --amber:#9a6a00; --amberbg:#f6eed7; --gate:#5b6b8c; --gatebg:#e9edf4;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg:#15181c; --panel:#1d2126; --ink:#e8eaec; --ink2:#aab0b5; --mut:#7d838a;
  --line:#30353b; --s1:#3987e5;
  --bad:#e0736a; --badbg:#3a2422; --good:#5fbe8e; --goodbg:#1e3328;
  --amber:#d9a83c; --amberbg:#32290f; --gate:#8fa2c4; --gatebg:#20262f;
} }
:root[data-theme="dark"] {
  --bg:#15181c; --panel:#1d2126; --ink:#e8eaec; --ink2:#aab0b5; --mut:#7d838a;
  --line:#30353b; --s1:#3987e5;
  --bad:#e0736a; --badbg:#3a2422; --good:#5fbe8e; --goodbg:#1e3328;
  --amber:#d9a83c; --amberbg:#32290f; --gate:#8fa2c4; --gatebg:#20262f;
}
body { background:var(--bg); color:var(--ink); font:15px/1.55 "Source Sans 3",system-ui,sans-serif;
  margin:0; padding:28px 20px 60px; }
.wrap { max-width:1100px; margin:0 auto; display:flex; flex-direction:column; gap:26px; }
h1 { font:700 30px/1.15 "Archivo",system-ui,sans-serif; letter-spacing:-.3px; margin:0; text-wrap:balance; }
h2 { font:650 19px/1.2 "Archivo",system-ui,sans-serif; margin:0 0 4px; }
h3 { font:600 15px/1.25 "Archivo",system-ui,sans-serif; margin:14px 0 4px; }
.sub { color:var(--ink2); max-width:82ch; margin:6px 0 0; }
.prov { display:flex; gap:14px; flex-wrap:wrap; font:12px "IBM Plex Mono",monospace; color:var(--mut); }
.badge { padding:1px 8px; border:1px solid var(--line); border-radius:10px; }
.panel { background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:18px 20px; }
.verdicts { display:grid; grid-template-columns:repeat(auto-fit,minmax(290px,1fr)); gap:12px; }
.v { background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:14px 16px; }
.v b { font-family:"Archivo"; font-size:15.5px; }
.v .num { font:600 21px/1.25 "IBM Plex Mono",monospace; font-variant-numeric:tabular-nums; margin:4px 0; }
.tblwrap { overflow-x:auto; }
table.plain { border-collapse:collapse; font-size:13.5px; width:100%; min-width:560px; }
.plain th, .plain td { padding:6px 10px; border-bottom:1px solid var(--line); text-align:right; vertical-align:top; }
.plain th:first-child, .plain td:first-child { text-align:left; }
.plain td.pos { color:var(--good); font-weight:600; } .plain td.neg { color:var(--bad); font-weight:600; }
.plain td.mut { color:var(--mut); }
.plain tr.hl td { background:var(--goodbg); }
.flag { display:inline-block; font:600 11px "Archivo"; letter-spacing:.4px; padding:2px 8px; border-radius:9px; margin-left:6px; vertical-align:2px; }
.flag.bad { color:var(--bad); background:var(--badbg); } .flag.good { color:var(--good); background:var(--goodbg); }
.flag.gate { color:var(--gate); background:var(--gatebg); } .flag.amber { color:var(--amber); background:var(--amberbg); }
.warn { background:var(--amberbg); color:var(--amber); border-radius:8px; padding:12px 16px; margin:12px 0 0; font-size:13.5px; max-width:104ch; }
.note { font-size:13px; color:var(--mut); max-width:100ch; }
ul.q { margin:8px 0 0; padding-left:20px; } ul.q li { margin:6px 0; max-width:92ch; }
td, th { font-variant-numeric:tabular-nums; }
</style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700&family=Source+Sans+3:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<div class="wrap">
<header>
<h1>Construction Mechanics Atlas</h1>
<p class="sub">The gap map's Tier-1 battery — the only alpha-space residual that needed no new data
pull. Rationale: the option sweeps had already shown the return gap is alpha-gated while the RISK side
has headroom, so construction mechanics (which attack <i>certain</i> costs — rebalancing drag, tax
drag — rather than hypothetical alpha) is where marginal effort on vaulted data most plausibly pays.
Four designs, 31 cells, all pre-registered before any number was computed; two cells desk-verified
independently.</p>
<div class="prov"><span class="badge">DESK = ledger entry G1-G4</span>
<span class="badge">census 1,305 → 1,336</span>
<span class="badge">costs + tax rates read from the registry, never typed</span>
<span class="badge">quoted: T3 · F6a · MOM-D1 · QG-D2 · SEC-D7 · TECH-D3</span></div>
</header>

<div class="verdicts">
<div class="v"><b>Rebalancing ADDED drawdown</b><div class="num">−20.6% vs −24 to −25%</div>
Pure drift beat every rebalanced rule on both risk-adjusted return and maxDD — an outcome nothing in
the registration anticipated. Monthly rebalancing is the one clearly dominated choice.</div>
<div class="v"><b>Diversification keeps paying past 20 names</b><div class="num">7.39x → 8.21x p10</div>
The tail bar cleared (+11.08%), and the prior's "flattens at 15-20" MISSED — the curve climbs to ~100
names. Concentration loses even though the survivor bias flatters it.</div>
<div class="v"><b>The LTCG line is real but sub-decisive</b><div class="num">−3.85 → −2.71pp/yr</div>
Short holds still win after tax under both rate regimes — but Jul-2024 narrowed their advantage by
~1.14pp/yr, leaving only ~10% of gross edge as margin.</div>
</div>

<section class="panel">
<h2>1 · G1 — the rebalance grid <span class="flag amber">BAR MET: winner named, but the risk winner is a different rule</span></h2>
<p class="sub">50/50 NIFTY / gold-INR, 2007-10..2026-04 (n=223 months). Statutory round trip 22.27bps
read from <span class="mono">quant/costs/statutory</span>. The desk held static blends (T3) but had
never tested the rebalancing RULE itself.</p>
<div class="tblwrap"><table class="plain">
<thead><tr><th>Rule</th><th>Net CAGR</th><th>Gross</th><th>Vol</th><th>maxDD</th><th>Turnover/yr</th><th>Events</th><th>CAGR/vol</th></tr></thead><tbody>
<tr><td>monthly</td><td class="neg">13.19</td><td>13.23</td><td>11.17</td><td>−24.43</td><td class="neg">16.31</td><td>223</td><td>1.184</td></tr>
<tr><td>quarterly</td><td>13.39</td><td>13.42</td><td>11.21</td><td>−25.16</td><td>10.32</td><td>74</td><td>1.197</td></tr>
<tr class="hl"><td><b>semi-annual</b></td><td class="pos"><b>13.55</b></td><td>13.57</td><td>11.28</td><td>−25.10</td><td>7.98</td><td>37</td><td>1.204</td></tr>
<tr><td>annual</td><td>13.43</td><td>13.44</td><td>10.94</td><td>−23.87</td><td>4.83</td><td>18</td><td>1.228</td></tr>
<tr class="hl"><td><b>never (pure drift)</b></td><td>13.24</td><td>13.24</td><td class="pos">10.39</td><td class="pos"><b>−20.62</b></td><td>0.00</td><td>0</td><td class="pos"><b>1.275</b></td></tr>
<tr><td>band ±3pp</td><td>13.36</td><td>13.39</td><td>11.16</td><td>−23.98</td><td>10.20</td><td>43</td><td>1.200</td></tr>
<tr><td>band ±5pp</td><td>13.24</td><td>13.26</td><td>11.15</td><td>−25.02</td><td>6.93</td><td>21</td><td>1.189</td></tr>
<tr><td>band ±10pp</td><td>13.21</td><td>13.22</td><td>11.27</td><td>−23.94</td><td>3.67</td><td>6</td><td>1.173</td></tr>
</tbody></table></div>
<p class="note"><b>Grading, bar by bar:</b> the kill branch did NOT fire — net spread 0.364pp/yr ≥ the
0.20 bar, so the winner is named (semi-annual on net CAGR). Prior (a) "gross CAGR/vol spread &lt; 0.10"
<b>MISSED by 0.002</b> (actual 0.102) — recorded as a boundary miss, not rounded into a pass, because
bars are never moved. Prior (b) HIT on the annual limb (+0.24pp over monthly), MISSED on the ±10pp
limb (+0.02pp). Prior (c) turnover monotone in band width — HIT.</p>
<div class="warn"><b>The unregistered surprise, and the headline:</b> pure drift delivered the best
risk-adjusted return of the whole grid AND the shallowest drawdown. Nothing in the registration
anticipated that rebalancing would <i>add</i> drawdown. Mechanism offered as interpretation, not claim:
both legs trended up across this window, so periodic rebalancing repeatedly sold the runner into the
laggard. <b>Consumption:</b> the CAGR winner and the risk winner are different rules and the entire
net-CAGR range is 0.36pp — small beside the 3-4pp maxDD differences. The one clearly DOMINATED choice
is monthly (worst net CAGR, 16.3%/yr turnover, no risk benefit). Default: semi-annual or annual.
"Never" is not adoptable as a rule — unbounded drift eventually breaches the mandate's own weight
bands, a constraint stated here rather than measured.</div>
</section>

<section class="panel">
<h2>2 · G2 — the concentration curve <span class="flag good">TAIL BAR CLEARED · admissible one-way</span></h2>
<p class="sub">Survivor panel, 418 names with ≥60 monthly observations, 2012-01..2021-12; 200 equal-weight
random draws per N, seed fixed at 20260911, monthly rebalance to equal weight.</p>
<div class="tblwrap"><table class="plain">
<thead><tr><th>N</th><th>Median CAGR</th><th>Median vol</th><th>CAGR/vol</th><th>p10 terminal wealth</th></tr></thead><tbody>
<tr><td>5</td><td>25.56</td><td class="neg">26.58</td><td class="neg">0.962</td><td class="neg">4.596x</td></tr>
<tr><td>10</td><td>26.62</td><td>23.92</td><td>1.113</td><td>5.951x</td></tr>
<tr><td>15</td><td>26.45</td><td>23.03</td><td>1.149</td><td>5.977x</td></tr>
<tr class="hl"><td><b>20</b></td><td>27.06</td><td>22.52</td><td>1.201</td><td><b>7.393x</b></td></tr>
<tr><td>30</td><td>26.79</td><td>22.04</td><td>1.215</td><td>7.459x</td></tr>
<tr class="hl"><td><b>50</b></td><td>27.40</td><td>21.46</td><td>1.276</td><td><b>8.213x</b></td></tr>
<tr><td>100</td><td>27.27</td><td>21.23</td><td>1.285</td><td>9.397x</td></tr>
<tr><td>200</td><td>27.48</td><td>21.10</td><td>1.302</td><td>10.005x</td></tr>
<tr><td>all 418</td><td>27.37</td><td class="pos">21.00</td><td class="pos">1.304</td><td class="pos">11.012x</td></tr>
</tbody></table></div>
<p class="note"><b>BAR:</b> p10 terminal wealth from N=20 → N=50 is <b>+11.08%</b>, clearing the +10%
bar — the tail argument holds and the stock book's floor sits above 20 names. <b>PRIOR MISSED on the
flattening:</b> the registration said CAGR/vol "rises steeply to N~15-20 then flattens"; it actually
keeps climbing well past 20 and only settles after ~100 — diversification kept paying in the median
too, not just the tail. <b>One-way rule applied as declared:</b> the panel deletes failures and so
flatters CONCENTRATED draws more (a 5-name draw from survivors is five survivors) — concentration
nonetheless loses on both median and tail, making this admissible evidence in the declared direction,
the strongest form available here. Absolute levels (25-27%/yr) are survivor-absurd and are NOT
evidence; only the shape across N is. <b>Stated limit:</b> this is a zero-skill random-draw curve — a
skilled selector's optimal N is a different question this design does not answer.</p>
</section>

<section class="panel">
<h2>3 · G3 — dispersion as a state <span class="flag gate">DISTINCT BUT UNUSABLE</span></h2>
<p class="sub">Cross-sectional dispersion, expanding terciles (min 36 months, lagged 1 month — real-time
by construction). n=84 months after warm-up: LOW 28 / MID 30 / HIGH 26.</p>
<div class="tblwrap"><table class="plain">
<thead><tr><th>Conditioned spread</th><th>LOW</th><th>MID</th><th>HIGH</th><th>HIGH−LOW</th><th>Bar (≥+5 AND monotone)</th></tr></thead><tbody>
<tr><td>6-2 momentum, fwd-1m</td><td class="neg">+3.14</td><td>+15.21</td><td>+13.36</td><td class="pos">+10.22</td><td class="mut">gap yes, <b>monotone NO</b> → partial</td></tr>
<tr><td>6-2 momentum, fwd-12m</td><td>+5.29</td><td>+10.17</td><td>+9.49</td><td>+4.20</td><td class="neg">fails both</td></tr>
<tr><td>low-vol, fwd-1m</td><td class="mut">−1.13</td><td class="mut">−10.09</td><td class="mut">−21.45</td><td class="mut">−20.32</td><td class="mut">artifact — not interpreted</td></tr>
<tr><td>low-vol, fwd-12m</td><td class="mut">−9.07</td><td class="mut">−13.23</td><td class="mut">−17.09</td><td class="mut">−8.01</td><td class="mut">artifact — not interpreted</td></tr>
</tbody></table></div>
<p class="note"><b>The redundancy branch did NOT fire:</b> corr(dispersion, panel realized vol) =
<b>0.453</b>, well under the 0.70 threshold — so dispersion is genuinely NOT repackaged volatility.
Combined with the failed monotonicity, the verdict is the precise one: <b>distinct but unusable</b> —
the read kills the "it's just vol in disguise" objection and simultaneously refuses promotion. The one
piece of real content, recorded as printed rather than as a ladder: the LOW-dispersion tercile is where
India momentum is weakest (+3.14 vs +13-15 in MID/HIGH) — a floor observation, not a monotone state.
<b>The low-vol rows are negative at every tercile</b> and most negative in HIGH dispersion: this
reproduces the known EW-survivor junk artifact (QG-D2's inversion; SEC-D7 a6's vol-CAGR cell is
already permanently survivorship-flagged), is NOT evidence about low-vol, and is deliberately left
uninterpreted.</p>
</section>

<section class="panel">
<h2>4 · G4 — the India LTCG-threshold turnover asymmetry <span class="flag amber">TAX LINE IS SECOND-ORDER</span></h2>
<p class="sub">6-2 momentum long leg (top decile), non-overlapping holds. Rates read from
<span class="mono">config/costs.yaml capital_gains_tax_india</span> (press-sourced, BR7/BR9 pin-flags
attached) — no rate typed into the script. Tax applied at each realization, after-tax proceeds
compounded.</p>
<div class="tblwrap"><table class="plain">
<thead><tr><th>Hold</th><th>n</th><th>Per-period</th><th>Gross ann.</th><th>After-tax pre-Jul2024</th><th>After-tax post-Jul2024</th></tr></thead><tbody>
<tr class="hl"><td><b>1m</b></td><td>83</td><td>2.39%</td><td>32.84</td><td class="pos"><b>27.35</b></td><td class="pos"><b>25.57</b></td></tr>
<tr><td>3m</td><td>27</td><td>8.09%</td><td class="pos"><b>36.52</b></td><td class="pos">30.49</td><td class="pos">28.53</td></tr>
<tr><td>6m</td><td>13</td><td>15.53%</td><td>33.48</td><td>28.15</td><td>26.40</td></tr>
<tr><td>12m (on boundary)</td><td class="neg">6</td><td>24.10%</td><td>24.10</td><td>21.69 <span class="mut">(as-STCG 20.49)</span></td><td>21.09 <span class="mut">(as-STCG 19.28)</span></td></tr>
<tr><td>13m</td><td class="neg">6</td><td>28.55%</td><td>26.09</td><td>23.50</td><td>22.86</td></tr>
</tbody></table></div>
<p class="note"><b>BAR:</b> the 13-month hold does NOT beat the 1-month hold after tax under either
regime — pre-Jul2024 23.50 vs 27.35 (gap −3.85pp/yr), post-Jul2024 22.86 vs 25.57 (gap −2.71pp/yr).
The registered branch is taken cleanly: <b>the tax line is second-order for India momentum and the 6-2
short-hold construction stands.</b> <b>The quantified nuance</b> is the useful output: Jul-2024
narrowed the short-hold advantage by ~1.14pp/yr without flipping the ranking. Break-even: a 1m hold
needs 2.088%/month gross (pre) or 2.163%/month (post) to match the 13m hold after tax, against an
actual 2.394% — so the post-2024 margin is only ~0.23pp/month, roughly <b>10% of the gross edge</b>: a
degradation-risk flag, since a ~10% decay in gross momentum would flip the after-tax ranking.</p>
<div class="warn"><b>Prior partial miss + an unregistered finding:</b> "gross return falls as H rises"
is wrong — it's a HUMP peaking at 3 months (32.84 → <b>36.52</b> → 33.48 → 24.10 → 26.09). Flowing
from that: within the STCG zone, a <b>3-month hold dominated the 1-month hold on every metric printed</b>
(gross 36.52 vs 32.84; after-tax 30.49/28.53 vs 27.35/25.57) at the same tax rate and a third of the
turnover — and turnover cost is not even modelled here, which can only widen the gap. Recorded as a
candidate refinement to the momentum sleeve's holding period, NOT consumed: it is an unregistered
comparison inside a registered design.<br><br><b>The binding caveat, stated first among limitations:</b>
non-overlapping periods leave n = 83 / 27 / 13 / <b>6</b> / <b>6</b>. The 12m and 13m cells rest on SIX
observations across a ten-year panel — direction only, no significance claimed or computable. Survivor
caveat carried: the ~33%/yr gross long-leg levels are survivor-absurd per MOM-D1's own flag; only the
cross-holding-period comparison is evidence.</div>
</section>

<section class="panel">
<h2>5 · What this battery changed</h2>
<ul class="q">
<li><b>Two construction defaults now have prints behind them:</b> rebalance the equity-gold blend
semi-annually or annually (never monthly), and floor the stock book at 50-100 names rather than
20-30.</li>
<li><b>One folk belief inverted:</b> rebalancing is not free risk reduction — on this window it
<i>added</i> 3-4pp of drawdown versus leaving the blend alone.</li>
<li><b>One candidate state refused:</b> dispersion is real and distinct from volatility, but its
conditioning is non-monotone, so it is not promoted to an instrument.</li>
<li><b>One tax question answered and one opened:</b> the LTCG line does not overturn short-hold
momentum (so the 6-2 construction stands), but the 3-month hold beating the 1-month hold on every
metric is an unregistered result that deserves its own design.</li>
<li><b>G5 stays registered-unrun</b> with its spec frozen — book-level vol-targeting needs the
standing-book engine plus a margin/collar interaction model, and registering bars that cannot be
evaluated would be a fake registration.</li>
</ul>
<p class="note">Sources of record: trial-ledger entry G1-G4 (registration committed before the run;
results desk-verified on two cells, with the verification-pass error recorded honestly) ·
scripts/analyze_gap_tier1.py · config/costs.yaml (statutory + the new capital_gains_tax_india block) ·
research/frontier/coverage-gap-map.md (the Tier-1 rationale). Regenerates via
scripts/build_construction_atlas.py, never from memory.</p>
</section>
</div>
"""
OUT.write_text(html)
print(f"written {OUT} ({len(html):,} bytes)")
