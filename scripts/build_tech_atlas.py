"""Build docs/learn/artifacts/technical-states-atlas.html — Track TECH: ATH &
drawdown states, stage quadrants, the momentum condition map, valuation-regime
persistence. Every number is a booked print (TECH-D1..D4; quoted entries named).
House dashboard system."""
import json
from pathlib import Path

R = Path("/home/user/claude-demo")
J = json.loads((R / "research/notes/es_sc_matrices/tech.json").read_text())
OUT = R / "docs/learn/artifacts/technical-states-atlas.html"


def cls(x, th=0.5):
    return "pos" if x > th else ("neg" if x < -th else "")


html = f"""<title>Technical States Atlas</title>
<style>
:root {{
  --bg:#f6f5f1; --panel:#fdfdfb; --ink:#212528; --ink2:#5a5f63; --mut:#8a8f93;
  --line:#e2e0d8; --s1:#2a78d6; --heat:42,120,214;
  --bad:#b3352b; --badbg:#f9e9e7; --good:#1f7a4d; --goodbg:#e7f3ec;
  --amber:#9a6a00; --amberbg:#f6eed7; --gate:#5b6b8c; --gatebg:#e9edf4;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg:#15181c; --panel:#1d2126; --ink:#e8eaec; --ink2:#aab0b5; --mut:#7d838a;
  --line:#30353b; --s1:#3987e5; --heat:57,135,229;
  --bad:#e0736a; --badbg:#3a2422; --good:#5fbe8e; --goodbg:#1e3328;
  --amber:#d9a83c; --amberbg:#32290f; --gate:#8fa2c4; --gatebg:#20262f;
}} }}
:root[data-theme="dark"] {{
  --bg:#15181c; --panel:#1d2126; --ink:#e8eaec; --ink2:#aab0b5; --mut:#7d838a;
  --line:#30353b; --s1:#3987e5; --heat:57,135,229;
  --bad:#e0736a; --badbg:#3a2422; --good:#5fbe8e; --goodbg:#1e3328;
  --amber:#d9a83c; --amberbg:#32290f; --gate:#8fa2c4; --gatebg:#20262f;
}}
body {{ background:var(--bg); color:var(--ink); font:15px/1.55 "Source Sans 3",system-ui,sans-serif;
  margin:0; padding:28px 20px 60px; }}
.wrap {{ max-width:1060px; margin:0 auto; display:flex; flex-direction:column; gap:26px; }}
h1 {{ font:700 30px/1.15 "Archivo",system-ui,sans-serif; letter-spacing:-.3px; margin:0; text-wrap:balance; }}
h2 {{ font:650 19px/1.2 "Archivo",system-ui,sans-serif; margin:0 0 4px; }}
h3 {{ font:600 15px/1.25 "Archivo",system-ui,sans-serif; margin:14px 0 4px; }}
.sub {{ color:var(--ink2); max-width:78ch; margin:6px 0 0; }}
.prov {{ display:flex; gap:14px; flex-wrap:wrap; font:12px "IBM Plex Mono",monospace; color:var(--mut); }}
.badge {{ padding:1px 8px; border:1px solid var(--line); border-radius:10px; }}
.panel {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:18px 20px; }}
.verdicts {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(290px,1fr)); gap:12px; }}
.v {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:14px 16px; }}
.v b {{ font-family:"Archivo"; font-size:15.5px; }}
.v .num {{ font:600 23px/1.25 "IBM Plex Mono",monospace; font-variant-numeric:tabular-nums; margin:4px 0; }}
.tblwrap {{ overflow-x:auto; }}
table.plain {{ border-collapse:collapse; font-size:13.5px; width:100%; min-width:520px; }}
.plain th, .plain td {{ padding:6px 10px; border-bottom:1px solid var(--line); text-align:right; vertical-align:top; }}
.plain th:first-child, .plain td:first-child {{ text-align:left; }}
.plain td.pos {{ color:var(--good); font-weight:600; }} .plain td.neg {{ color:var(--bad); font-weight:600; }}
.plain td.mut {{ color:var(--mut); }}
.flag {{ display:inline-block; font:600 11px "Archivo"; letter-spacing:.4px; padding:2px 8px; border-radius:9px; margin-left:6px; vertical-align:2px; }}
.flag.bad {{ color:var(--bad); background:var(--badbg); }} .flag.good {{ color:var(--good); background:var(--goodbg); }}
.warn {{ background:var(--amberbg); color:var(--amber); border-radius:8px; padding:12px 16px; margin:12px 0 0; font-size:13.5px; max-width:100ch; }}
.note {{ font-size:13px; color:var(--mut); max-width:96ch; }}
ul.q {{ margin:8px 0 0; padding-left:20px; }} ul.q li {{ margin:6px 0; max-width:86ch; }}
td, th {{ font-variant-numeric:tabular-nums; }}
</style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700&family=Source+Sans+3:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<div class="wrap">
<header>
<h1>Technical States Atlas</h1>
<p class="sub">Track TECH: all-time highs and drawdown states, Weinstein-style stage quadrants
(as STATES — the desk's own graveyard of MA trading rules is quoted, not contradicted), the momentum
condition map on 98 years of US and 32 years of India factor data, and the persistence anatomy of
market valuation regimes, plus MOM-D1's stock-level lookback anatomy across regimes. Every number is a
booked ledger print (TECH-D1..D4 + MOM-D1, 43 cells, census 1,288; registrations committed before the
run; the runner's prints desk-verified). Sector RS is data-gated
on the NSE sectoral TR pull; leverage and index-ratio verdicts are quoted from booked entries.</p>
<div class="prov"><span class="badge">DESK = ledger print</span>
<span class="badge">quoted: TS1 · T-CTRL1 · T2 · T3 · F2 · CU-D4 · VAL-D5 · SC-D4</span>
<span class="badge">states, never rules — Tier-C consumption only</span></div>
</header>

<div class="verdicts">
<div class="v"><b>Don't fear the high — fear the expensive downtrend</b><div class="num">+9.5 vs +0.3</div>
New-ATH months earn slightly MORE than average next-12m (Shiller, 1871-); the dead state is a
downtrend from EXPENSIVE valuations (+0.27% next-12m real, vs +14.65% from cheap ones).</div>
<div class="v"><b>The momentum stand-down gate FIRED</b><div class="num">−22.5 / −27.5 %/yr</div>
Post-bear + top-vol-tercile momentum in the US (n=44) and India (n=15) vs +8.6/+15.1 baselines —
the switch state is real in both markets; a Tier-C stand-down monitor is now registrable.</div>
<div class="v"><b>Valuation clusters for years</b><div class="num">P(stay) 0.97-0.98</div>
Cheap and expensive regimes persist (spells: mean 37-43 months); the damage lives in de-rating
transitions (first year after exiting expensive: −7.2% real vs +8.6 unconditional).</div>
</div>

<section class="panel">
<h2>1 · ATH &amp; drawdown states (TECH-D1)</h2>
<div class="tblwrap"><table class="plain">
<thead><tr><th>State</th><th>Print (next-12m unless noted)</th><th>Read</th></tr></thead><tbody>
<tr><td>Shiller NEW-ATH months (1871-2023)</td><td class="pos">+9.46% vs +8.29 others · P(neg) 28% vs 32%</td><td>ATHs are slightly BETTER than average — don't fear the high</td></tr>
<tr><td>NIFTY drawdown terciles → 12m</td><td>LOW +9.16 · MID +14.41 · <span class="pos">DEEP +33.66</span></td><td>the entry state, third asset class running</td></tr>
<tr><td>NIFTY drawdown terciles → 36m ann</td><td>LOW +10.42 · MID +14.66 · <span class="pos">DEEP +21.54</span></td><td>the entry premium compounds at 3y</td></tr>
<tr><td>NIFTY 52w-high proximity terciles</td><td>FAR +21.53 · MID +13.63 · NEAR +10.00</td><td>index-level proximity ranks INVERSELY (this is not the cross-sectional 52w-high effect, which stays untested)</td></tr>
<tr><td>Gold new-ATH months (1833-2026)</td><td>+3.80 vs +3.78</td><td>nothing</td></tr>
<tr><td>Shiller breakouts (first ATH after ≥24m base)</td><td>+9.34 vs +8.57 unconditional (n=15)</td><td>the folk breakout edge does not show at index level</td></tr>
</tbody></table></div>
</section>

<section class="panel">
<h2>2 · Stage quadrants — a risk state, not a return rule <span class="flag bad">T-CTRL1 / T2 STAND</span></h2>
<p class="sub">Quadrants = (price vs MA) × (MA slope), 200d/10m conventions, lagged. S2≈uptrend, S4≈downtrend.</p>
<div class="tblwrap"><table class="plain">
<thead><tr><th></th><th>S1 (below, rising)</th><th>S2 (above, rising)</th><th>S3 (above, falling)</th><th>S4 (below, falling)</th></tr></thead><tbody>
<tr><td>NIFTY fwd-1m ann / fwd vol</td><td>+21.3 / 18.2%</td><td>+6.8 / <b>13.7%</b></td><td>+27.9 / 18.6%</td><td>+18.4 / <b>26.3%</b></td></tr>
<tr><td>NIFTY fwd-12m</td><td>+11.0</td><td>+9.2</td><td>+26.4</td><td class="pos">+32.2</td></tr>
<tr><td>Shiller fwd-12m real</td><td>+2.6</td><td>+7.9</td><td>+13.6</td><td>+10.6</td></tr>
<tr><td>GOLD fwd-12m</td><td>+1.9</td><td class="pos">+11.3</td><td>+5.3</td><td class="neg">+0.55</td></tr>
</tbody></table></div>
<p class="note"><b>Three verdicts:</b> (1) stages rank VOL exactly as registered — S2 is the calm regime
(13.7%), S4 the wild one (26.3%): consumed as a risk state. (2) For EQUITY indices the "buy stage 2"
folk claim INVERTS — stage 4 clusters at bottoms and carries the rebound (+32.2 NIFTY): equities
mean-revert at index level. (3) GOLD is the opposite animal — stage 2 works (+11.3), stage 4 is dead
(+0.55): gold trends, equities rebound — the TS1 doctrine (3m fast rules for NIFTY drawdown control,
12m slow trend for gold) re-derived from an independent construction.</p>
<h3>The keeper: stage × valuation corners (Shiller, 1881-2023, fwd-12m real)</h3>
<div class="tblwrap"><table class="plain">
<thead><tr><th></th><th>CHEAP CAPE tercile</th><th>EXPENSIVE CAPE tercile</th></tr></thead><tbody>
<tr><td>S2 uptrend</td><td class="pos">+10.91 (n=269)</td><td>+6.22 (n=503)</td></tr>
<tr><td>S4 downtrend</td><td class="pos">+14.65 (n=216) — the entry</td><td class="neg">+0.27 (n=110) — the falling knife</td></tr>
</tbody></table></div>
</section>

<section class="panel" style="border-left:3px solid var(--good)">
<h2>Update · 10 Sep 2026 — MOM-D1: the stock-level lookback anatomy (18 cells; census 1,288)</h2>
<p class="sub">TECH-D3's m9 could only read the panel's pre-baked momentum columns and found the artifact
made the question ungradeable. MOM-D1 rebuilds the lookback windows from raw formation returns — five
windows (3-1, 6-1, 6-2, 12-2, 12-7 [Novy-Marx intermediate, LIT]) crossed with market-state and
volatility regimes, on BOTH markets, with the one-way rule sharpened: a bias that DEPRESSES momentum
spreads makes a POSITIVE print admissible evidence, so India's survivor panel — despite the same
no-delisting flattery — can answer this cleanly where the US panel cannot.</p>
<div class="tblwrap"><table class="plain">
<thead><tr><th>Window</th><th>US panel</th><th>US large</th><th>India full</th><th>India top-ADV</th></tr></thead><tbody>
<tr><td>3-1 (no skip)</td><td class="neg">−11.00</td><td class="neg">−7.40</td><td class="pos">+9.65</td><td class="neg">−1.41</td></tr>
<tr><td>6-1 (no skip)</td><td class="neg">−14.41 (worst)</td><td class="neg">−13.71 (worst)</td><td class="pos">+14.70</td><td class="pos">+5.59</td></tr>
<tr><td><b>6-2 (skip-month)</b></td><td class="neg">−13.60</td><td class="neg">−9.54</td><td class="pos"><b>+15.59 — peak</b></td><td class="pos"><b>+5.87 — peak</b></td></tr>
<tr><td>12-2</td><td class="neg">−19.02 (worst)</td><td class="neg">−12.82</td><td class="pos">+14.38</td><td class="pos">+5.51</td></tr>
<tr><td>12-7 (Novy-Marx)</td><td class="neg">−12.61</td><td class="neg">−5.68</td><td class="pos">+10.74</td><td class="pos">+5.20</td></tr>
</tbody></table></div>
<p class="note"><b>US: the artifact closes the question a third time</b> (SC-D4, TECH-D3 m9, now this
independent construction) — every window inverts on the EW no-delisting panel; ungradeable as ordering
evidence. One mechanistic note survives regardless of sign: the no-skip 6-1 window is the WORST in
both cuts — the skip-month convention [LIT] is corroborated even inside the artifact. <b>India: a
clean, admissible verdict</b> — 6-2 (six-month formation, one-month skip) is the outright peak in BOTH
the full universe and the liquid top-ADV tercile, and the ONLY window that stays positive across every
India-VIX tercile (LO +26.60 / MID +9.87 / HI +5.68) while 12-7 FLIPS NEGATIVE under vol stress
(LO +27.57 / MID +7.09 / HI <b>−9.74</b>). The 3-1 window flips negative in liquid names too — short-term
reversal, not momentum [Jegadeesh 1990]. By NIFTY market state, 6-2 prints −7.51 (down) vs
<b>+20.99</b> (up) — a third independent confirmation of Cooper-Gutierrez-Hameed's up-market-only
momentum, now at the individual-stock level.</p>
<div class="warn"><b>Consumption:</b> the India momentum sleeve defaults to 6-2 formation; in rising
India-VIX, SHORTEN toward 6-2 rather than lengthening (a refinement alongside the TECH-D3 stand-down
monitor, not a replacement for it) — the 12-month window is the one that breaks under stress, the
6-month one degrades but survives; never use a no-skip short window in liquid names.</div>
</section>

<section class="panel">
<h2>3 · The momentum condition map (TECH-D3) <span class="flag good">STAND-DOWN GATE FIRED — MONITOR REGISTRABLE</span></h2>
<div class="tblwrap"><table class="plain">
<thead><tr><th>Condition</th><th>US UMD (1927-2024)</th><th>India WML (1993-2025)</th></tr></thead><tbody>
<tr><td>Baseline (all other months)</td><td>+8.55%/yr</td><td>+15.06%/yr</td></tr>
<tr><td>Post-bear (trailing-24m mkt &lt; 0)</td><td class="neg">−9.30 vs +10.64</td><td>+9.81 vs +14.49 (degraded, still +)</td></tr>
<tr><td>Vol tercile LOW / MID / HIGH</td><td>+6.7 / +10.0 / <span class="neg">−9.7</span> (VIX)</td><td class="pos">+20.0</span> / +2.4 / <span class="neg">−7.2</span> (realized)</td></tr>
<tr><td><b>CRASH STATE: post-bear AND top-vol</b></td><td class="neg">−22.48 (n=44)</td><td class="neg">−27.46 (n=15)</td></tr>
<tr><td>Own-factor momentum (chase strength?)</td><td>+6.9 after strong vs +8.4 after weak — no</td><td>+12.5 vs <b>+23.5 after weak</b> — inverted: never chase WML strength</td></tr>
<tr><td>Worst months (state flags)</td><td>1932-07/08, 2009-04 — all post-bear</td><td>2001-11, 2009-05, 2000-04</td></tr>
</tbody></table></div>
<p class="note"><b>When momentum works:</b> calm, post-up markets — India low-vol state +20%/yr.
<b>When it doesn't:</b> the year after a bear inside a vol spike — that is when the loser leg becomes
a call option on the rebound (Daniel-Moskowitz [LIT], reproduced here on both markets). <b>The switch:</b>
the registered gate fired in both markets, so the stand-down monitor (post-bear + top-vol tercile,
Tier-C reduce-only) is now registrable for the India factor sleeve; vol-scaling mitigates but does not
immunize (panel: −15.9 vs −17.6 — sign unflipped). <b>Lookbacks:</b> the 3-6 vs 6-12 stock-level
question is unanswerable on the EW panel (the reversal artifact punishes longer formation harder —
SC-D4 quoted); at index level the booked answer stands: 3m for NIFTY drawdown control, 12m for gold
(TS1). Stock-level lookbacks re-run on India PIT data.</p>
</section>

<section class="panel">
<h2>4 · Valuation clustering (TECH-D4) — slow states, violent transitions</h2>
<div class="tblwrap"><table class="plain">
<thead><tr><th>CAPE tercile</th><th>P(stay) monthly</th><th>P(same, 12m later)</th><th>spell median / mean (months)</th></tr></thead><tbody>
<tr><td>CHEAP</td><td>0.97</td><td>0.84</td><td>7 / 37.1</td></tr>
<tr><td>MID</td><td>0.87</td><td>0.36</td><td>5.5 / 7.5 — a corridor, not a state</td></tr>
<tr><td>EXPENSIVE</td><td>0.98</td><td>0.85</td><td>16.5 / 42.9</td></tr>
</tbody></table></div>
<p class="note">Transitions carry the returns: the first 12m after flipping OUT of expensive averages
<b>−7.21% real</b> (exits happen BY falling, and keep falling); out of cheap, <b>+16.51%</b> (re-rating
rallies continue); unconditional +8.57 (n=15 events each, overlap flagged). This is WHY valuation can
never be a clock (states last years) and CAN be a band/floor instrument (VAL-D5's +2.92pp/yr floor gap;
ER-D1c's null stands).</p>
</section>

<section class="panel">
<h2>5 · Quoted &amp; gated — the rest of the technical menu</h2>
<ul class="q">
<li><b>Sector RS / rotation — GATED:</b> needs the Priority-1 NSE sectoral TR pull; the design brief is in
research/notes/tech-dossiers/a (industry momentum per Moskowitz-Grinblatt [LIT], with FUN-D3's booked
warning: buying defensives once risk-off is identifiable is the measured mistake in India).</li>
<li><b>Index ratios:</b> equity/gold rotation lost to the static 50/50 blend (T3, both lookbacks);
small/large ratio conditioning is booked in the SC series (winter rebound a watch; never chase).</li>
<li><b>Leverage:</b> stock-level leverage is booked (QG-D2 c12; DB battery at the macro level);
margin-debt-as-timing has the weakest evidence in the canon [LIT] and no free India series — not pursued.</li>
<li><b>MA trading rules:</b> dead and staying dead (T-CTRL1: 0/10 net; T2: trend-on-states adds nothing) —
everything on this page is a STATE read consistent with those kills.</li>
</ul>
<p class="note">Sources of record: trial-ledger entries TECH-D1..D4 + MOM-D1 (registrations committed
before-run; results desk-verified) · es_sc_matrices/tech.json · tech-dossiers a/b ·
india-regime-playbook.md (the 2026-09-10 Track TECH + MOM-D1 addenda). Regenerates via
scripts/build_tech_atlas.py, never from memory.</p>
</section>
</div>
"""
OUT.write_text(html)
print(f"written {OUT} ({len(html):,} bytes)")
