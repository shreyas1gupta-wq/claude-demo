"""Build docs/learn/artifacts/red-flag-horizon-map.html — cross-arc synthesis:
every red flag this desk has evidence on, sorted by the forward horizon at which it
actually shows up (not by which arc produced it). Zero new cells — every number here
is quoted from an already-booked ledger print (EQ-D1, QG-D3/D4, VAL-D1/D5, H36-D1,
SC-D3, TECH-D2/D3/D4, DB-D1/D3/D5/D6/D9, CI-D1/D3/D4, MOM-D1, RATIO-D1) or from
eq-dossiers/a. Ledger entry of record: SYNTHESIS-RF1. House dashboard system."""
from pathlib import Path

R = Path("/home/user/claude-demo")
OUT = R / "docs/learn/artifacts/red-flag-horizon-map.html"

html = """<title>Red Flag Horizon Map</title>
<style>
:root {
  --bg:#f6f5f1; --panel:#fdfdfb; --ink:#212528; --ink2:#5a5f63; --mut:#8a8f93;
  --line:#e2e0d8; --s1:#2a78d6; --heat:42,120,214;
  --bad:#b3352b; --badbg:#f9e9e7; --good:#1f7a4d; --goodbg:#e7f3ec;
  --amber:#9a6a00; --amberbg:#f6eed7; --gate:#5b6b8c; --gatebg:#e9edf4;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg:#15181c; --panel:#1d2126; --ink:#e8eaec; --ink2:#aab0b5; --mut:#7d838a;
  --line:#30353b; --s1:#3987e5; --heat:57,135,229;
  --bad:#e0736a; --badbg:#3a2422; --good:#5fbe8e; --goodbg:#1e3328;
  --amber:#d9a83c; --amberbg:#32290f; --gate:#8fa2c4; --gatebg:#20262f;
} }
:root[data-theme="dark"] {
  --bg:#15181c; --panel:#1d2126; --ink:#e8eaec; --ink2:#aab0b5; --mut:#7d838a;
  --line:#30353b; --s1:#3987e5; --heat:57,135,229;
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
.flag { display:inline-block; font:600 11px "Archivo"; letter-spacing:.4px; padding:2px 8px; border-radius:9px; margin-left:6px; vertical-align:2px; }
.flag.bad { color:var(--bad); background:var(--badbg); } .flag.good { color:var(--good); background:var(--goodbg); }
.flag.gate { color:var(--gate); background:var(--gatebg); } .flag.amber { color:var(--amber); background:var(--amberbg); }
.warn { background:var(--amberbg); color:var(--amber); border-radius:8px; padding:12px 16px; margin:12px 0 0; font-size:13.5px; max-width:104ch; }
.note { font-size:13px; color:var(--mut); max-width:100ch; }
.st { display:inline-block; font:600 11px "Archivo"; padding:2px 8px; border-radius:9px; }
.st.decay { color:var(--bad); background:var(--badbg); } .st.grow { color:var(--gate); background:var(--gatebg); }
.st.regime { color:var(--amber); background:var(--amberbg); } .st.gate { color:var(--mut); background:var(--line); }
ul.q { margin:8px 0 0; padding-left:20px; } ul.q li { margin:6px 0; max-width:92ch; }
td, th { font-variant-numeric:tabular-nums; }
</style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700&family=Source+Sans+3:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<div class="wrap">
<header>
<h1>Red Flag Horizon Map</h1>
<p class="sub">Every red flag this desk has evidence on — accrual/earnings-quality, governance,
valuation-trap, quality/growth, momentum, and macro-debt/credit — sorted not by which arc produced it
but by the forward horizon at which it actually shows up. Some flags are loudest immediately and fade;
some are invisible at 12 months and only become real by year three to five; some are never a fixed-
horizon signal at all, only a regime or a probability shift. Zero new cells: every number below is
quoted from an already-booked ledger print.</p>
<div class="prov"><span class="badge">DESK = ledger print, entry ID cited per row</span>
<span class="badge">quoted: EQ-D1 · QG-D3/D4 · VAL-D1/D5 · H36-D1 · SC-D3 · TECH-D2/D3/D4 · DB-D1/D3/D5/D6/D9 · CI-D1/D3/D4 · MOM-D1 · RATIO-D1</span>
<span class="badge">lit: eq-dossiers/a</span></div>
</header>

<div class="verdicts">
<div class="v"><b>DECAYING flags — act within the year or not at all</b><div class="num">−11.9 → −4.4</div>
The accrual/TATA proxy and the India post-bear-smallcap avoid are both strongest at 12m and roughly
half their per-year size by 36m — same direction, shrinking bite.</div>
<div class="v"><b>GROWING flags — invisible at 12m, real by 3-5y</b><div class="num">+1.4 → −2.1</div>
Peak-ROE-at-any-price and the glamour-quality corner are wrong-signed or flat at 12m and only turn
into genuine drags from 36-60m onward — buying today's winner-at-any-price looks fine for a year.</div>
<div class="v"><b>REGIME flags — no fixed horizon is the right frame</b><div class="num">+0.16 @ 5-10y</div>
Sovereign debt LEVEL never hurts equities even at 10y (it hurts bonds); credit BOOMS don't lower 5y
equity returns at all — they raise crisis odds on a 3-year clock instead. Different question entirely.</div>
</div>

<section class="panel">
<h2>0 · Immediate / event-triggered — not a horizon at all</h2>
<p class="sub">These fire on discovery, not on a countdown. Treat as an avoid/reduce trigger the day the
flag is seen, regardless of what horizon you're otherwise underwriting.</p>
<div class="tblwrap"><table class="plain">
<thead><tr><th>Red flag</th><th>What happens</th><th>Source</th></tr></thead><tbody>
<tr><td>Promoter share pledge acceleration + falling price (India)</td><td>reflexive spiral: pledge → price fall → margin call → forced sale → further fall, independent of the underlying business</td><td class="mut">[LIT, mechanism only] eq-dossiers/a §5a</td></tr>
<tr><td>Restatement announcement</td><td>significant NEGATIVE abnormal return AT disclosure (event-study evidence, not an ex-ante horizon claim)</td><td class="mut">[LIT, LOW CONFIDENCE] eq-dossiers/a §4</td></tr>
<tr><td>Auditor going-concern opinion / sudden auditor change</td><td>elevated distress/delisting risk; no evidence it predicts returns beyond what's already visible in the fundamentals</td><td class="mut">[LIT, LOW CONFIDENCE] eq-dossiers/a §4</td></tr>
<tr><td>Crisis event itself (t0)</td><td class="neg">real equity <b>−14.1%</b> in the crisis year — but recovery arrives already at t+1 (+9.7%) and t+2 (+13.9%)</td><td class="mut">DESK, CI-D4 (88 crisis-years, JST)</td></tr>
<tr><td>No-skip short lookback (3-1, 6-1 formation)</td><td>the WORST formation window in both US and India cuts, every cut — this is short-term reversal, not momentum</td><td class="mut">DESK, MOM-D1</td></tr>
</tbody></table></div>
</section>

<section class="panel">
<h2>1 · 12-month horizon — where most earnings-quality and technical red flags live</h2>
<p class="sub">The standard "annual" test window. This is where the accrual anomaly, momentum crash-states,
and valuation-cluster transitions are validated on this desk's own data.</p>
<div class="tblwrap"><table class="plain">
<thead><tr><th>Red flag</th><th>Fwd-12m print</th><th>Status</th><th>Source</th></tr></thead><tbody>
<tr><td>TATA_proxy (earnings-rank vs cash-flow-rank divergence)</td><td class="neg">panel −11.88%/yr · large-cap −4.76</td><td><span class="st decay">PEAK HERE, decays after</span></td><td>DESK, EQ-D1 e1</td></tr>
<tr><td>Cash conversion (good conversion = green flag, mirror check)</td><td class="pos">+7.77%/yr</td><td><span class="st decay">confirms e1's story</span></td><td>DESK, EQ-D1 e4</td></tr>
<tr><td>Momentum crash-state (post-bear + top-vol tercile)</td><td class="neg">US −22.48%/yr (n=44) · India −27.46%/yr (n=15)</td><td><span class="st gate">Tier-C stand-down</span></td><td>DESK, TECH-D3</td></tr>
<tr><td>India post-bear smallcap re-entry</td><td class="neg">−12.31% vs −0.20% (gap −12.11pp)</td><td><span class="st decay">PEAK HERE, decays after</span></td><td>DESK, SC-D3 i3</td></tr>
<tr><td>Downtrend FROM an expensive valuation (vs from cheap)</td><td class="neg">expensive +0.27% real vs cheap +14.65%</td><td><span class="st gate">don't fear the high, fear this</span></td><td>DESK, TECH-D2 (Shiller)</td></tr>
<tr><td>Exiting an expensive valuation cluster (de-rating)</td><td class="neg">−7.21% real vs +8.57% unconditional</td><td><span class="st gate">transitions carry the damage</span></td><td>DESK, TECH-D4</td></tr>
<tr><td>High + RISING inflation (the killer 2x2 cell)</td><td class="neg">same-year −3.0% (median −4.0%)</td><td><span class="st amber">contemporaneous, not forward — fwd-1y after acceleration is only muted (+2.1/+0.1%)</span></td><td>DESK, CI-D1 i2/i5</td></tr>
<tr><td>Margin decline (Beneish GMI-style, as coded)</td><td class="pos">+5.27%/yr — WRONG SIGN</td><td><span class="st gate">MISS — do not use raw</span></td><td>DESK, EQ-D1 e2</td></tr>
<tr><td>Leverage increase (Beneish LVGI-style, as coded)</td><td class="pos">+2.22%/yr — WRONG SIGN</td><td><span class="st gate">MISS — do not use raw</span></td><td>DESK, EQ-D1 e3</td></tr>
</tbody></table></div>
<p class="note">The two Beneish-style misses are not noise: DGLS's own classify-vs-predict-returns
distinction (eq-dossiers/a §2) says these components were built to flag manipulation, not to time
returns — expecting them to work as raw 12m return signals was always the weaker claim.</p>
</section>

<section class="panel" style="border-left:3px solid var(--gate)">
<h2>2 · 3-year horizon — where flags either decay to their true size or first appear</h2>
<p class="sub">The pivotal horizon: some 12m flags are already burning out here; other flags that were
flat, wrong-signed, or invisible at 12m first show their real color.</p>
<h3>Decaying (were strong at 12m, weaker but same-signed by 3y)</h3>
<div class="tblwrap"><table class="plain">
<thead><tr><th>Red flag</th><th>12m</th><th>36m</th><th>Source</th></tr></thead><tbody>
<tr><td>TATA_proxy accrual divergence</td><td class="neg">−11.88 (panel)</td><td class="neg">−4.43</td><td>EQ-D1 e1</td></tr>
<tr><td>India post-bear smallcap avoid</td><td class="neg">−12.31</td><td class="neg">−5.93</td><td>SC-D3 i3 / H36-D1 h11</td></tr>
<tr><td>Fundamental-momentum proxy (d3(Eps), reversal artifact)</td><td class="mut">−3.03 (1m)</td><td class="neg">−0.84</td><td>ES-D1 / H36-D1 h1</td></tr>
</tbody></table></div>
<h3>Growing (flat, wrong-signed, or invisible at 12m — real by 3y)</h3>
<div class="tblwrap"><table class="plain">
<thead><tr><th>Red flag</th><th>12m</th><th>36m</th><th>60-120m</th><th>Source</th></tr></thead><tbody>
<tr><td>Peak-ROE-at-any-price (large-cap Q5-Q1)</td><td class="pos">+1.4pp (wrong sign)</td><td class="mut">0.0</td><td class="neg">−1.5 @60m / −2.1 @120m</td><td>QG-D3 h10</td></tr>
<tr><td>Glamour-quality corner (ROE Q5 × growth Q5)</td><td class="mut">+6.5%/yr</td><td class="mut">—</td><td class="neg">+2.9%/yr @120m (worst corner)</td><td>QG-D4</td></tr>
<tr><td>Volatile "quality" (ROE Q5 × vol Q5, large-cap)</td><td class="mut">flattered (junk-bounce artifact)</td><td class="mut">still positive</td><td class="neg">−0.7 @60m</td><td>QG-D4 / H36-D1 h3</td></tr>
<tr><td>szQ5 value spread (protective, the mirror image)</td><td class="pos">+8.80 (VAL-D1)</td><td class="pos">+6.5pp/yr</td><td class="pos">+4.83pp/yr @60m</td><td>H36-D1 h4/h5, VAL-D5 quoted</td></tr>
<tr><td>Low-vol as protective (mid/large caps)</td><td class="neg">buried by junk-bounce artifact</td><td class="pos">FLIPS positive (+3.29/+4.58/+2.41)</td><td class="mut">—</td><td>H36-D1 h3</td></tr>
</tbody></table></div>
<p class="note">Same mechanism runs both directions: the EW no-delisting panel's junk-bounce artifact
(QG-D2) hides quality/low-vol's true protective value AND hides peak-ROE/glamour's true damage for
about a year — it dies out by 36m, and the honest picture only appears from there.</p>
</section>

<section class="panel">
<h2>3 · 5-year+ / structural horizon — regime facts, not point forecasts</h2>
<div class="tblwrap"><table class="plain">
<thead><tr><th>Red flag / read</th><th>Print</th><th>Read</th><th>Source</th></tr></thead><tbody>
<tr><td>CAPE valuation floor (cheap vs expensive p10)</td><td class="pos">+2.92pp/yr floor gap (cheap p10 −2.00 vs expensive p10 −4.92)</td><td>a genuinely 5-year read; at 12m valuation is a STATE (P(stay) 0.97-0.98/mo), never a forecast</td><td>DESK, VAL-D5, next-5y</td></tr>
<tr><td>Public debt LEVEL (sovereign)</td><td class="mut">+0.16 (5y) / +0.17 (10y) — ~zero, POSITIVE sign</td><td>has NEVER predicted bad equity returns at 5-10y in 150 years of JST data; the real casualty is BONDS (US ≥90%-debt cohort: next-10y bonds −1.0%, 1/7 positive)</td><td>DESK, DB-D1 / DB-D4</td></tr>
<tr><td>Debt ≥120% tail</td><td class="neg">FX leaks +3.7%/yr faster · r−g most negative at −1.3%</td><td>structural, decade-scale regime facts — not a return forecast at any single horizon</td><td>DESK, DB-D9 c2 / DB-D6 f6</td></tr>
<tr><td>Credit BOOM (not level)</td><td class="mut">null on 5y equity returns (+0.01)</td><td class="neg">but crisis-in-3y jumps to 15-19% vs 5-6% calm</td><td>DESK, DB-D3 / DB-D5 / CI-D3 j2</td></tr>
<tr><td>Debt-era regime (pre- vs post-1980)</td><td class="pos">pre-1980 +0.19</td><td class="neg">post-1980 −0.05 — the "debt helps equities" pattern is a dead, pre-1980-only phenomenon</td><td>DESK, DB-D9 c5</td></tr>
</tbody></table></div>
<p class="note"><b>The debt lesson, stated plainly (the user's own example):</b> "high debt" is NOT a
red flag for equities at any horizon this desk can measure — 5y, 10y, or by era, the correlation is
flat-to-positive. It IS a red flag for BONDS at long horizons, and separately, credit BOOMS (not debt
levels) are a red flag for CRISIS PROBABILITY on a 3-year clock rather than for return size at any
fixed horizon. Three different claims that "debt is bad" routinely blur together.</p>
</section>

<section class="panel">
<h2>4 · Governance / mechanism-only gates — no desk-quantified horizon</h2>
<p class="sub">These carry a real mechanism but no return-horizon evidence, desk or literature-strong
enough to size. Read as always-on avoid-list gates, not timed signals.</p>
<div class="tblwrap"><table class="plain">
<thead><tr><th>Flag</th><th>Why no horizon</th><th>Source</th></tr></thead><tbody>
<tr><td>Promoter share pledging level + acceleration</td><td>event-driven trigger (see Tier 0), not a horizon-return statistic; India's cleanest genuinely point-in-time marker regardless</td><td>eq-dossiers/a §5a; P5 buildable</td></tr>
<tr><td>Related-party transactions</td><td>plausible mechanism [LIT], magnitudes thin and jurisdiction-varying — a qualitative screen, not a sized factor</td><td>eq-dossiers/a §4</td></tr>
<tr><td>Beneish M-Score / DGLS F-Score (raw)</td><td>literature-validated to CLASSIFY manipulation (a label), only secondarily and weakly to predict returns — never presented as a horizon signal in the source papers themselves</td><td>eq-dossiers/a §2</td></tr>
<tr><td>Off-balance-sheet financing, auditor flags, restatement history</td><td>risk-avoidance / due-diligence screens with thin-to-absent standalone return evidence at any horizon</td><td>eq-dossiers/a §4</td></tr>
</tbody></table></div>
</section>

<section class="panel">
<h2>5 · How to use this map</h2>
<ul class="q">
<li><b>Before underwriting a position, ask which horizon you're actually holding for</b> — a red flag
that's a 12m-peak-then-decay signal (accrual divergence, India post-bear smallcap) is the wrong tool
for a 3-5y hold, and a flag that only shows up at 3-5y (glamour-quality, peak-ROE) will look like
nothing at all in a 12m backtest.</li>
<li><b>Never treat "high debt" as an equity red flag</b> — the desk's own 150-year record says the
opposite at every horizon tested; treat elevated sovereign debt as a BOND concern and a decade-scale
regime marker, and treat CREDIT BOOMS (not debt levels) as the crisis-probability flag on its own
3-year clock.</li>
<li><b>Don't composite red flags blindly across horizons</b> — EQ-D1's own composite backfired by
averaging a peaking-at-12m ingredient (accrual) with two ingredients that are simply wrong-signed at
12m (margin-decline, leverage-increase); the fix there generalizes here: check each flag's OWN
horizon-of-validity before combining anything.</li>
<li><b>India-registrable on the fundamentals handoff:</b> every accrual/leverage/margin flag above
re-runs with true dollar values and real deaths in the data (P1-P6); the India-specific horizon
ladder (does TATA_proxy also decay 12m→36m in India, does peak-ROE also invert-then-bite) is an
open, registrable design once the handoff lands.</li>
</ul>
<p class="note">Sources of record: trial-ledger entry SYNTHESIS-RF1 (cross-arc synthesis, zero new
cells, every number quoted from EQ-D1, QG-D3/D4, VAL-D1/D5, H36-D1, SC-D3, TECH-D2/D3/D4,
DB-D1/D3/D5/D6/D9, CI-D1/D3/D4, MOM-D1, RATIO-D1) · eq-dossiers/a-earnings-quality-red-flags.md.
Regenerates via scripts/build_rf_horizon_atlas.py, never from memory.</p>
</section>
</div>
"""
OUT.write_text(html)
print(f"written {OUT} ({len(html):,} bytes)")
