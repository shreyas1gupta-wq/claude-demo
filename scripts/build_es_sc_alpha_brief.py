"""Build docs/learn/artifacts/earnings-size-alpha-brief.html — the dedicated
edge/alpha brief on the principal's three metrics (2026-09-10): earnings revisions,
earnings surprises, smallcap-vs-largecap valuation & growth. SYNTHESIS ONLY: every
desk number is a booked ledger print (entry cited); literature figures carry [LIT]
with the dossier's own hedge; census unchanged (no new cells). Matrices read the
committed JSONs. House dashboard system reused."""
import json
from pathlib import Path

import numpy as np

R = Path("/home/user/claude-demo")
M = R / "research/notes/es_sc_matrices"
OUT = R / "docs/learn/artifacts/earnings-size-alpha-brief.html"
es = json.loads((M / "es_d2.json").read_text())
d4 = json.loads((M / "sc_d4.json").read_text())
d5 = json.loads((M / "sc_d5.json").read_text())


def heat(mat, rows="rows", cols="cols", rlab=None, clab=None):
    a = np.array(mat, dtype=float)
    lo, hi = a.min(), a.max()
    rlab = rlab or [f"Q{i+1}" for i in range(a.shape[0])]
    clab = clab or [f"Q{j+1}" for j in range(a.shape[1])]
    cells = ""
    for i in range(a.shape[0]):
        cells += f'<tr><th class="rl">{rows} {rlab[i]}</th>'
        for j in range(a.shape[1]):
            v = a[i][j]
            t = (v - lo) / (hi - lo or 1)
            cells += f'<td style="--t:{t:.2f}" title="{rows} {rlab[i]} x {cols} {clab[j]}: {v:+.1f}">{v:.1f}</td>'
        cells += "</tr>"
    head = "".join(f"<th>{c}</th>" for c in clab)
    return (f'<table class="hm"><thead><tr><th></th>{head}</tr></thead><tbody>{cells}</tbody></table>')


def bar_deciles(vals, lab):
    mx = max(vals)
    cells = "".join(
        f'<div class="dcol"><div class="dbar" style="height:{max(6, 84*v/mx):.0f}px"></div>'
        f'<div class="dv">{v:.0f}</div><div class="dl">D{i+1}</div></div>' for i, v in enumerate(vals))
    return f'<div class="dwrap"><div class="dlab">{lab}</div><div class="drow">{cells}</div></div>'


E1 = [17.1, 13.6, 16.2, 14.1, 20.4, 16.1, 14.5, 13.9, 12.1, 14.1]
E2 = [18.2, 15.6, 15.9, 16.2, 16.9, 20.8, 15.0, 12.2, 10.5, 11.7]

EDGES = [
    ("1", "India PEAD, event-timed (small/micro tail)", "SURPRISES",
     "~4-9% per 60d decile spread gross [LIT, VERIFY-hedged]; 40-60% concentrated at the next 1-3 prints; survives in exactly the low-coverage names arbitrage capital avoids — the Aggressive book's 500-750 habitat",
     "GATED — filed EPS + filing_date (the handoff) + NSE announcement timestamps (runsheet)",
     "kill: doesn't survive the desk's turnover-cost math or the 45-60d staggered calendar"),
    ("2", "India size valuation-spread timer", "SIZE",
     "US first gate PASSED: small-cheap terciles +28.8 vs +12.7pp next-12m (T1-T3 +16.05; Pe +16.81); corr staircase -0.26/-0.50/-0.69 at 1/12/36m [DESK SC-D1]; India analogue low-to-mid single-digit pp/yr [LIT, LOW CONF]",
     "GATED — NSE index P/E-P/B history (2021 splice named); price-only relative series is the clean fallback",
     "kill: Cohen-Polk-Vuolteenaho decomposition — if the spread forecasts realized GROWTH gaps, not mispricing, the timer dies"),
    ("3", "Monthly SUE sort (no event windows)", "SURPRISES",
     "the grind component of PEAD, harvested at monthly cadence on most-recently-known surprise; magnitude = the decile spread minus the announcement pop [LIT, qualitative discount]",
     "GATED — the handoff's filed quarterly EPS (8-quarter seasonal-random-walk history)",
     "kill: most-published anomaly corner — needs the capacity/illiquidity survival argument to hold net of costs"),
    ("4", "Large-cap value spread", "SIZE",
     "+9.95%/yr at 1m / +8.80% at 12m inside the LARGEST size quintile — the only signal that survives every construction on the panel [DESK SC-D4]; the value-growth gap is size-stable ~+5-6pp at 12m [DESK SC-D5]",
     "LIVE evidence — India form is the cheap-quality blend already in QG doctrine (Sharpe 0.49 vs 0.32/0.41 components)",
     "kill: none open — the caveat is EW/US; the India PIT version re-derives it"),
    ("5", "Post-bear smallcap avoidance (India)", "SIZE",
     "next-12m SMB -12.31% after down market years vs -0.20 after up [DESK SC-D3]; hardened -4.85pp on a panel biased the other way [DESK SC-D3a]",
     "CONSUMED — playbook rule: no smallcap adds for 12m after a bear year (Tier-C reduce-only)",
     "kill: none — double-confirmed; re-graded if PIT data contradicts"),
    ("6", "Quality-controlled size tilt (junk-filtered smallcap)", "SIZE",
     "the Asness junk-control resolution of the size premium [LIT]; India's RAW segment is -2.9pp/yr [DESK TL-D2] so any positive result must be earned on PIT data",
     "GATED — the handoff's fundamentals (ROE/leverage screens) + delisted registry",
     "kill: if junk-filtered India smallcap still loses to the market, the booked verdict stands — selection, never segment"),
    ("7", "Growth-gap / dilution short (small-growth lemons)", "SIZE+GROWTH",
     "small low-B/M high-issuance names disappoint priced-in growth [LIT]; invisible on the survivor panel BECAUSE its casualties were deleted [DESK SC-D5 branch]",
     "GATED — PIT share-issuance records (rights/QIP) via the handoff's shares_outstanding + corporate_actions",
     "kill: redundant if subsumed by the quality/junk factor already booked"),
    ("8", "Revenue-surprise confirmation (Jegadeesh-Livnat)", "SURPRISES",
     "an earnings beat confirmed by a revenue beat is the cleaner underreaction signal [LIT]; tiebreak layer on #1/#3, never standalone",
     "GATED — same handoff (revenue is in the P1 schema)",
     "kill: no incremental spread over SUE alone"),
    ("9", "The avoid corner: expensive + deteriorating", "REVISIONS",
     "+11.3%/yr vs panel ~+17-19 at 1m; +10.4 at 12m; large-cap +6.0/+6.4 [DESK ES-D2 m7/m8]",
     "AVOID-LIST line now (consistent with the moderation principle) — costs nothing to honor",
     "kill: n/a — an avoidance, not a position"),
    ("10", "Smallcap winter rebound (India)", "SIZE",
     "trailing-36m LO tercile -> +10.32%/12m [DESK SC-D3 i2] — but the survivor panel refused to corroborate [DESK SC-D3a a2]",
     "WATCH only, IIMA-single-series support; never a tilt pending PIT smallcap data",
     "kill: fails on the PIT panel when it exists"),
]
DEAD = [
    ("EPS rank-migration (fundamental momentum), standalone", "D10-D1 -3.03%/yr (3m) / -6.47 (12m); flat across horizons; junk-concentrated", "ES-D1"),
    ("Value + catalyst (cheap AND improving)", "corner increment -1.57 vs the +2.00 gate; large-cap +0.18; the improving corner LOSES to cheap alone", "ES-D2 m7/m8"),
    ("India analyst-revision signal on free data", "no free PIT consensus exists; coverage stops ~rank 500 — the Aggressive tail is unreachable even paid", "Atlas 3.5 DATA-REJECT (stands)"),
    ("US SMB momentum, imported", "+7.96%/12m pre-1981 -> -0.37 / -0.68 after — died at publication", "SC-D2 t1/t4"),
    ("US post-bear small rebound, imported to India", "US +5.15pp gap; India -12.11pp — the sign flips", "SC-D2 t3 vs SC-D3 i3"),
    ("Revision LEVEL blended with forecast DISPERSION", "opposite-signed premia (dispersion is a NEGATIVE, short-sale-constraint effect) — a construction error, pre-empted", "dossier a [LIT]"),
]


def ledger_rows(items):
    out = ""
    for rank, name, theme, ev, status, kill in items:
        st = ("good" if status.startswith(("LIVE", "CONSUMED")) else
              "warn" if status.startswith(("WATCH", "AVOID")) else "gate")
        out += (f'<tr><td class="rank">{rank}</td><td><b>{name}</b> <span class="theme">{theme}</span>'
                f'<div class="ev">{ev}</div></td>'
                f'<td><span class="st {st}">{status.split(" — ")[0]}</span>'
                f'<div class="ev">{status.split(" — ", 1)[1] if " — " in status else ""}</div>'
                f'<div class="ev kill">{kill}</div></td></tr>')
    return out


html = f"""<title>Earnings &amp; Size Alpha Brief</title>
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
.wrap {{ max-width:1080px; margin:0 auto; display:flex; flex-direction:column; gap:26px; }}
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
.grid2 {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(430px,1fr)); gap:18px; }}
table.hm {{ border-collapse:separate; border-spacing:2px; width:100%;
  font:12.5px "IBM Plex Mono",monospace; font-variant-numeric:tabular-nums; }}
.hm th {{ color:var(--mut); font-weight:500; padding:2px 4px; }}
.hm .rl {{ text-align:right; white-space:nowrap; }}
.hm td {{ text-align:center; padding:7px 4px; border-radius:4px; color:var(--ink);
  background:rgba(var(--heat), calc(.08 + .5*var(--t))); }}
.tblwrap {{ overflow-x:auto; }}
table.plain {{ border-collapse:collapse; font-size:13.5px; width:100%; min-width:540px; }}
.plain th, .plain td {{ padding:6px 10px; border-bottom:1px solid var(--line); text-align:right; vertical-align:top; }}
.plain th:first-child, .plain td:first-child {{ text-align:left; }}
.plain td.pos {{ color:var(--good); font-weight:600; }} .plain td.neg {{ color:var(--bad); font-weight:600; }}
table.ledger {{ border-collapse:collapse; font-size:13.5px; width:100%; min-width:700px; }}
.ledger td {{ padding:10px; border-bottom:1px solid var(--line); vertical-align:top; }}
.ledger tr:last-child td {{ border-bottom:none; }}
.rank {{ font:600 16px "IBM Plex Mono",monospace; color:var(--mut); width:28px; }}
.theme {{ font:600 10.5px "Archivo"; letter-spacing:.5px; color:var(--gate); background:var(--gatebg);
  border-radius:8px; padding:1px 7px; margin-left:6px; vertical-align:1px; }}
.ev {{ font-size:12.8px; color:var(--ink2); margin-top:3px; max-width:66ch; }}
.ev.kill {{ color:var(--mut); font-style:italic; }}
.st {{ display:inline-block; font:600 11px "Archivo"; letter-spacing:.4px; padding:2px 9px; border-radius:9px; white-space:nowrap; }}
.st.good {{ color:var(--good); background:var(--goodbg); }}
.st.gate {{ color:var(--gate); background:var(--gatebg); }}
.st.warn {{ color:var(--amber); background:var(--amberbg); }}
.flag {{ display:inline-block; font:600 11px "Archivo"; letter-spacing:.4px; padding:2px 8px; border-radius:9px; margin-left:6px; vertical-align:2px; }}
.flag.bad {{ color:var(--bad); background:var(--badbg); }} .flag.good {{ color:var(--good); background:var(--goodbg); }}
.note {{ font-size:13px; color:var(--mut); max-width:96ch; }}
.mono {{ font:12.5px "IBM Plex Mono",monospace; font-variant-numeric:tabular-nums; }}
.dwrap {{ margin:10px 0; }} .dlab {{ font:600 13px "Archivo"; margin-bottom:6px; }}
.drow {{ display:flex; gap:6px; align-items:flex-end; }}
.dcol {{ flex:1; display:flex; flex-direction:column; align-items:center; gap:2px; }}
.dbar {{ width:100%; max-width:44px; background:var(--s1); opacity:.9; border-radius:4px 4px 0 0; }}
.dv {{ font:11px "IBM Plex Mono",monospace; color:var(--ink2); }}
.dl {{ font:10px "IBM Plex Mono",monospace; color:var(--mut); }}
td, th {{ font-variant-numeric:tabular-nums; }}
</style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700&family=Source+Sans+3:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<div class="wrap">
<header>
<h1>Earnings &amp; Size Alpha Brief</h1>
<p class="sub">The three metrics, end to end: <b>earnings revisions · earnings surprises · smallcap-vs-largecap
valuation &amp; growth</b>. Every desk number is a booked ledger print (entry cited); literature figures carry
[LIT] with the dossier's own confidence hedge; nothing here is a new trial (census stands at 1,189).
US firm panel = 1,207 stocks EW 1999-2019, survivor-tilted (levels inflated; spreads and large-cap rows
carry the evidence). Paper, zero costs unless a cost figure is quoted.</p>
<div class="prov"><span class="badge">DESK = ledger print</span><span class="badge">[LIT] = dossier figure, hedge attached</span>
<span class="badge">GATED = registrable the day its data lands</span><span class="badge">sources: ES-D1/D2 · SC-D1..D5+D3a · TL-D2 · dossiers a/b/c</span></div>
</header>

<div class="verdicts">
<div class="v"><b>Revisions: no free path, and the free proxy is dead</b><div class="num">−3.0 / −6.5 %/yr</div>
EPS rank-migration D10−D1 on the US panel (ES-D1); no interaction rescues it (ES-D2 gate −1.57 vs +2.00);
India consensus data is paid-only and stops ~rank 500. What survives: one avoid corner + the PEAD route.</div>
<div class="v"><b>Surprises: the one live earnings edge — waiting on your data</b><div class="num">~4–9% / 60d [LIT]</div>
The PEAD decile spread, front-loaded at the next 1-3 prints; it survives precisely in low-coverage small
names — the Aggressive book's habitat AND its highest-cost segment. Two India designs are speced, both
registrable the day the handoff lands.</div>
<div class="v"><b>Size: timing exists, the segment doesn't (India)</b><div class="num">+16.1pp · −12.3%</div>
The small-vs-large valuation spread orders next-12m relative return (SC-D1); India smallcap after a bear
year loses another −12.31% to largecaps (SC-D3) while the segment itself charges −2.9pp/yr for 32 years (TL-D2).</div>
</div>

<section class="panel" style="border-left:3px solid var(--good)">
<h2>Update · 10 Sep 2026 — the 3-year re-read (H36-D1, 13 cells; census 1,202)</h2>
<p class="sub">The principal asked for the 3y layer; the whole arc was re-run at 36m forward and the map
changes: <b>the junk noise washes out and the compounding signals emerge.</b> (1) The revision proxy's
negative ladder fades to −0.84pp median at 3y — dead at every horizon, decay curve booked. (2) The avoid
corner is a 3y fact: expensive+deteriorating earns +3.9%/yr vs +8.1 for cheap in large caps, sustained
three years. (3) <b>Low-vol flips positive at 3y in mid/large caps</b> (+3.3/+4.6/+2.4 spreads) — the
moderation-principle mechanism appearing in an independent construction. (4) Large-cap value compounds:
+6.5pp/yr at 3y, <b>+4.83pp/yr still there at FIVE years</b>; the size valuation-spread's power GROWS with
horizon (T1−T3 = +16.75pp/YR at 36m). (5) <b>Both India rules extend to 3-year facts</b>: post-bear
smallcap damage runs −5.9%/yr for three years (~−16pp cumulative), and the winter rebound is monotone at
3y (LO +8.0 / MID +2.2 / HI −3.3 ann) while chasing smallcap strength is −4.1. (6) The growth-gap
conditioner does NOT survive to 3y (non-monotone) — short-horizon only. Recheck of the standing register:
QG-D3/D4 already carry the 36m quality map (Q2-ROE hump, champion moderate-ROE × low-vol); ER-D1c says 3y
index-level valuation timing is null-consistent (no 3y CAPE clock, ever); CU-D4iii is the booked 3y entry
state (+13.2 vs +6.2%/yr after currency crashes).</p>
</section>

<section class="panel">
<h2>1 · Earnings revisions <span class="flag bad">PROXY KILLED · DATA-REJECT STANDS</span></h2>
<p class="sub">Three constructs the literature says never to conflate: revision <b>LEVEL</b> (positive drift —
Stickel, Chan-Jegadeesh-Lakonishok [LIT]), revision <b>BREADTH</b> (practitioner diffusion), and forecast
<b>DISPERSION</b> (a NEGATIVE-premium short-sale-constraint effect — Diether-Malloy-Scherbina [LIT]).
India reality: no free point-in-time consensus exists (Atlas 3.5 DATA-REJECT, re-confirmed); coverage
concentrates in the top ~500 names, so the Aggressive book's 500-750 tail is unreachable even paid.
The analyst-free substitute — EPS rank-migration — was tested and killed:</p>
{bar_deciles(E1, "ES-D1 e1 · fwd-1m %/yr by Δ3m(EPS-rank) decile — D10−D1 = −3.03 (improvers LOSE)")}
{bar_deciles(E2, "ES-D1 e2 · same for Δ12m — D10−D1 = −6.47")}
<div class="grid2" style="margin-top:12px">
<div><h3>ΔEPS × P/B, fwd-1m %/yr (ES-D2 m1) — the cheap column peaks at NO-CHANGE, not improvement</h3>
{heat(es["m1"]["grid"], rows="ΔEPS", cols="P/B", clab=["cheap","Q2","Q3","Q4","exp."])}</div>
<div><h3>ΔEPS × momentum, fwd-1m (m2) — the only positive pockets sit where price hasn't moved</h3>
{heat(es["m2"]["grid"], rows="ΔEPS", cols="mom", clab=["losers","Q2","Q3","Q4","winners"])}</div>
</div>
<div class="tblwrap" style="margin-top:12px"><table class="plain">
<thead><tr><th>Corner read (EW ann.)</th><th>1m</th><th>12m</th><th>large-cap 1m</th><th>large-cap 12m</th></tr></thead>
<tbody>
<tr><td>cheap + improving</td><td>+17.9</td><td>+15.3</td><td>+12.9</td><td>+11.0</td></tr>
<tr><td>cheap alone</td><td>+19.5</td><td>+17.6</td><td>+12.7</td><td>+12.2</td></tr>
<tr><td><b>increment (the +2.00 gate)</b></td><td class="neg">−1.57</td><td class="neg">−2.35</td><td>+0.18</td><td class="neg">−1.24</td></tr>
<tr><td><b>expensive + deteriorating (the avoid corner)</b></td><td class="neg">+11.3</td><td class="neg">+10.4</td><td class="neg">+6.0</td><td class="neg">+6.4</td></tr>
</tbody></table></div>
<p class="note">What to keep: (1) the avoid corner — expensive-and-deteriorating underperforms the panel by
6-8pp/yr and large caps by ~6pp, an avoidance that costs nothing; (2) the mechanism note — improvement pays
+4-5%/yr ONLY inside low-momentum bins (the Novy-Marx nuance, recorded not consumed); (3) the honest verdict
that a real revisions signal, if the desk ever buys the data, is a refinement to the momentum seat, not a
new standalone (CJL partial-independence [LIT]).</p>
</section>

<section class="panel">
<h2>2 · Earnings surprises / PEAD <span class="flag good">THE LIVE ROUTE — TWO DESIGNS SPECED</span></h2>
<p class="sub">The mechanism is identified, not just observed: investors underreact to the KNOWN
autocorrelation of quarterly earnings (positive lags 1-3, negative lag 4 — Bernard-Thomas [LIT]), and the
drift resolves in lumps around the NEXT 1-3 announcements rather than smoothly.</p>
<div class="tblwrap"><table class="plain">
<thead><tr><th>Data point</th><th>Figure</th><th>Source / hedge</th></tr></thead><tbody>
<tr><td>Share of eventual return still unpriced at announcement</td><td>~half</td><td>Ball-Brown 1968 [LIT]</td></tr>
<tr><td>SUE decile spread over the drift window</td><td>~4-9% / 60 trading days</td><td>Bernard-Thomas [LIT, VERIFY-hedged range]</td></tr>
<tr><td>Drift concentration around the next 1-3 prints</td><td>40-60%</td><td>dossier b §2 [LIT] — the part a monthly desk struggles to capture</td></tr>
<tr><td>Drift horizon</td><td>60-180 trading days, front-loaded</td><td>Bernard-Thomas [LIT]</td></tr>
<tr><td>Where it survives post-2000</td><td>small / illiquid / low-coverage</td><td>Chordia et al., Sadka [LIT] — migrated, not dead</td></tr>
<tr><td>Where the costs bite</td><td>the same segment</td><td>Korajczyk-Sadka logic [LIT] + the desk's own cost stack</td></tr>
<tr><td>India filing calendar</td><td>staggered, 45-60d (SEBI LODR Reg. 33)</td><td>dossier b — mandates a days-since-announcement STATE variable</td></tr>
<tr><td>India academic PEAD evidence</td><td>real but thin, Tier-B directional only</td><td>dossier b §5 — short samples, quarter-label anchors, survivorship</td></tr>
</tbody></table></div>
<h3>The two India designs (registrable the day the handoff lands)</h3>
<p class="sub">(a) <b>Monthly SUE sort</b> — most-recently-known surprise (8-quarter seasonal random walk),
no event windows; captures the grind, gives up the pop; matches the desk's cadence. (b) <b>Event-timed
overlay</b> — the full drift, needs exact NSE/BSE announcement timestamps (runsheet row live); each rebalance
computes per-name days-since-announcement instead of treating the universe as uniformly fresh. Tiebreak
layer for both: revenue-surprise confirmation (Jegadeesh-Livnat [LIT]) — revenue is already in the handoff
schema. Survival argument: capacity/illiquidity — it lives where big arbitrage capital won't go, which is
the Aggressive book's habitat; the open question is net-of-cost, and that is re-derived, never assumed.</p>
</section>

<section class="panel">
<h2>3 · Smallcap vs largecap: valuation &amp; growth → predictability</h2>
<div class="tblwrap"><table class="plain">
<thead><tr><th>The level verdict first (TL-D2)</th><th>US</th><th>India</th></tr></thead><tbody>
<tr><td>Small-minus-market premium, long run</td><td class="pos">+1.5 to +2.7 pp/yr (1/5/10/20y, floor RISES at 20y)</td><td class="neg">−2.9 pp/yr over 32 years</td></tr>
<tr><td>Vol ratio / worst drawdown</td><td>1.32× / −85%</td><td>1.34× / −90% (2001-09)</td></tr>
<tr><td>The doctrine</td><td>the segment pays for its risk</td><td><b>selection inside the segment, never the segment</b></td></tr>
</tbody></table></div>

<h3>Valuation spread → relative return (SC-D1, in-sample first gate — PASSED)</h3>
<div class="tblwrap"><table class="plain">
<thead><tr><th>Signal tercile (240m, 1999-2019)</th><th>T1</th><th>T2</th><th>T3</th><th>T1−T3</th></tr></thead><tbody>
<tr><td>P/B spread (T1 = small CHEAP vs large) → next-12m S−L</td><td class="pos">+28.78</td><td>+13.06</td><td>+12.73</td><td class="pos">+16.05pp</td></tr>
<tr><td>P/E repeat</td><td class="pos">+26.40</td><td>+5.19</td><td>+9.59</td><td class="pos">+16.81pp</td></tr>
<tr><td>Growth gap (T1 = small growing SLOWER) → next-12m S−L</td><td>+14.03</td><td>+20.28</td><td class="pos">+23.39</td><td class="neg">−9.36pp</td></tr>
</tbody></table></div>
<p class="note">The correlation staircase: corr(P/B-spread, S−L) = −0.26 / −0.50 / <b>−0.69</b> at 1/12/36m —
rising with horizon, the value-spread signature [LIT]. The growth gap runs the OTHER way (+0.22 at 36m):
small out-growing large is a weak momentum-flavored conditioner, not a contrarian one. Joint corner:
cheap-small + growth-favorable months → +34.07pp next-12m (n=12) vs +11.47 (n=38). All in-sample, flagged;
the 2000-05 episode carries much of it; the India version is the tradeable one and waits on NSE index P/E-P/B.</p>

<h3>The quadrants (SC-D5) and the cap-spectrum map (SC-D4)</h3>
<div class="grid2">
<div><h3 style="margin-top:0">size × P/B, fwd-12m % — the value ladder holds in the LARGE rows</h3>
{heat(d5["j3"]["grid"], rows="size", cols="P/B", rlab=["small","Q2","Q3","Q4","large"], clab=["cheap","Q2","Q3","Q4","exp."])}</div>
<div><h3 style="margin-top:0">size × momentum, fwd-12m % — losers "win" everywhere: the EW junk bounce, a measurement limit, not a momentum verdict</h3>
{heat(d5["j5"]["grid"], rows="size", cols="mom", rlab=["small","Q2","Q3","Q4","large"], clab=["losers","Q2","Q3","Q4","winners"])}</div>
</div>
<div class="tblwrap" style="margin-top:10px"><table class="plain">
<thead><tr><th>Four corners, fwd-12m EW %</th><th>value</th><th>growth</th><th>value−growth</th></tr></thead><tbody>
<tr><td>SMALL (levels survivor-inflated — read the gap)</td><td>+21.02</td><td>+15.76</td><td class="pos">+5.26</td></tr>
<tr><td>LARGE (the honest half)</td><td>+12.04</td><td class="neg">+6.07 — worst corner</td><td class="pos">+5.97</td></tr>
</tbody></table></div>
<p class="note">The value-growth gap is SIZE-STABLE (~+5-6pp at 12m in both halves) — cheapness pays the same
whether you are small or large on this panel; and per SC-D4, value is the ONLY spread that survives every
size quintile (+9.95%/yr at 1m and +8.80% at 12m in the largest — the NIFTY-750-implementable end).
Growth never pays at any size (spreads −3.9 to −13.0 across the map), and the FF small-growth lottery corner
is invisible here precisely because the survivor panel deleted its casualties — declared at registration,
confirmed by print.</p>

<h3>Time-series: what predicts small-vs-large — US and India disagree on the sign</h3>
<div class="tblwrap"><table class="plain">
<thead><tr><th>Conditioner → next-12m SMB</th><th>US (1926-2024)</th><th>India (IIMA 1993-2025)</th></tr></thead><tbody>
<tr><td>12m SMB momentum spread</td><td>+4.49 — but +7.96 pre-1981, −0.4/−0.7 after (died at publication)</td><td>+3.99, both sides ≤0 — only says AVOID after bad smallcap years</td></tr>
<tr><td>Trailing 36m terciles (LO→HI)</td><td>−0.3 / +1.0 / +6.4 — continuation</td><td class="pos">+10.3 / −0.5 / −2.5 — REVERSAL: winters precede rebounds</td></tr>
<tr><td><b>After a DOWN market year</b></td><td class="pos">+6.18 vs +1.03 — the rebound</td><td class="neg">−12.31 vs −0.20 — the INVERSION (playbook rule)</td></tr>
<tr><td>Survivor-panel one-way check</td><td>—</td><td>gap −4.85pp on a panel biased pro-smallcap — hardened</td></tr>
</tbody></table></div>
<p class="note">India regime map (rolling-5y SMB, ann.): trough −20.4 (1999-11) · peak +9.9 (2018-07, the
categorization-unwind top) · −4.0 (2021-12) · +8.6 (2024-12, the froth SEBI stress-tested) · +3.3 latest
(2025-12). Full-period mean −2.82%/yr — matches TL-D2 on an independent construction.</p>
</section>

<section class="panel">
<h2>4 · The edge ledger for these three metrics — ranked</h2>
<div class="tblwrap"><table class="ledger"><tbody>{ledger_rows(EDGES)}</tbody></table></div>
</section>

<section class="panel">
<h2>5 · Killed on these metrics — bleed prevented <span class="flag bad">DO NOT REBUILD</span></h2>
<div class="tblwrap"><table class="ledger"><tbody>
{"".join(f'<tr><td><b>{n}</b></td><td class="ev" style="font-size:13px">{p}</td><td class="mono" style="color:var(--mut); white-space:nowrap">{r}</td></tr>' for n, p, r in DEAD)}
</tbody></table></div>
<p class="note">Sources of record: research/register/trial-ledger.md entries ES-D1/D2, SC-D1..D5, SC-D3a,
TL-D2 · research/notes/es-dossiers/a,b,c (all [LIT] hedges preserved) · research/notes/es_sc_matrices/*.json ·
india-regime-playbook.md. This brief is a SYNTHESIS — no new cells were computed for it; census 1,189.
Regenerates via scripts/build_es_sc_alpha_brief.py, never from memory.</p>
</section>
</div>
"""
OUT.write_text(html)
print(f"written {OUT} ({len(html):,} bytes)")
