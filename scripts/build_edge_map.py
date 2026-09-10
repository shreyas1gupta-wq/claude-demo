"""Build docs/learn/artifacts/edge-map.html — THE EDGE MAP: every measured edge in
the register, ranked by consumption status, with the ES-D2/SC-D4/SC-D5 matrices.
Every number is a booked ledger print (entry named per row); matrices read the
committed JSONs in research/notes/es_sc_matrices/. House dashboard system
(palette validated in the QG atlas session) reused unchanged."""
import json
from pathlib import Path

import numpy as np

R = Path("/home/user/claude-demo")
M = R / "research/notes/es_sc_matrices"
OUT = R / "docs/learn/artifacts/edge-map.html"

es = json.loads((M / "es_d2.json").read_text())
d4 = json.loads((M / "sc_d4.json").read_text())
d5 = json.loads((M / "sc_d5.json").read_text())


def heat(mat, rows="rows", cols="cols", rlab=None, clab=None, flag=False):
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
            cells += (f'<td style="--t:{t:.2f}" title="{rows} {rlab[i]} x {cols} {clab[j]}: {v:+.1f}">{v:.1f}</td>')
        cells += "</tr>"
    head = "".join(f"<th>{c}</th>" for c in clab)
    return (f'<table class="hm{" suspect" if flag else ""}"><thead><tr><th></th>{head}</tr></thead>'
            f'<tbody>{cells}</tbody></table>')


def spread_table(block, unit):
    sigs = [("Pb", "Value (cheap−exp)"), ("Mom", "Momentum (W−L)"), ("Vol", "Low-vol (lo−hi)"),
            ("Roe", "ROE (hi−lo)"), ("Gr", "EPS growth (hi−lo)"), ("d3", "EPS Δrank (up−dn)")]
    head = "".join(f"<th>size Q{i+1}</th>" for i in range(5))
    rows = ""
    for k, lab in sigs:
        v = block[k]
        cells = "".join(
            f'<td class="{"pos" if x > 0.5 else ("neg" if x < -0.5 else "")}">{x:+.1f}</td>' for x in v)
        surv = "✓ survives Q5" if abs(v[4]) >= 1.0 and np.sign(v[4]) == np.sign(sum(np.sign(v))) else ""
        rows += f"<tr><td>{lab}</td>{cells}<td>{surv}</td></tr>"
    return (f'<div class="tblwrap"><table class="plain"><thead><tr><th>signal spread ({unit})</th>{head}'
            f'<th></th></tr></thead><tbody>{rows}</tbody></table></div>')


# ---- booked edge rows (every number = a ledger print; entry cited) ----
CONSUMED = [
    ("The standing book (structure over leverage)", "+11.46 CAGR (TR ~+12.76) / −11.36 maxDD",
     "65/20/15 collar-stacked; condors gated at VIX-pct ≥0.60; two grids + sweep 2 REFUSED their train winners OOS", "SW2-A1 · OP-D3..D7"),
    ("Overnight execution", "overnight +24.0%/yr vs intraday −12.6 (gap t=+7.6)",
     "no harvest (STT-capped, registered before the run); staged deployment defaults to buy-at-close on calm days", "T1 · T1b"),
    ("Budget-day vol scheduling", "|ΔlogVIX| 2.1x (p=2.7e-06); day-0 crush −8.9%",
     "L5 schedules vol both sides of the event; never picks direction; condor exclusion window", "CW1 · CW-D1v"),
    ("The post-bear smallcap rule (India)", "next-12m SMB −12.31% after down years vs −0.20 (US: +6.18)",
     "no smallcap adds for 12m after a bear year; hardened by the survivor-panel one-way check (−4.85pp on a panel biased the other way)", "SC-D3 · SC-D3a"),
    ("The killer inflation cell", "HIGH+RISING: equity −3.0%/yr vs +4.4 falling-from-high; gold +9.6 > housing +6.8 >> bonds −5.6",
     "the L9 2x2; asset ranking inside the cell drives the gold sleeve's crash premium (+6-9pp)", "CI-D1..D5"),
    ("Monetary avoid-state", "hiking-into-slowdown −5.2%/yr; falling-rate years +8.0 vs +3.3",
     "STATE for risk budget, never a forecast; slope return-RANKING flag hardened (medians flat at US monthly); recession-odds channel survives (26/28/14)", "FUN-D8 · FUN-D9a"),
    ("Entry-state discipline", "stress-percentile rebound zone; re-entry below the 60th pct (median wait 29td)",
     "converts crashes into the entry state; Tier-C reduce-only overlays", "F2 · OP-D2"),
    ("The moderation principle", "champion cell moderate ROE x low vol; glamour-quality 2.9%/yr at 10y",
     "quality consumed at moderate rank with a vol screen; growth never pays at any horizon", "QG-D2..D5"),
]
FLAGS = [
    ("April SMB tilt", "Apr rank 1/12, p=0.020", "promotion refused on costs; paper trade PT-2 grades Apr-2027", "CW2"),
    ("q-EG expected growth", "+8.3%/yr unspanned alpha, 100% in-sample", "adjudicated by QG-D6 (frozen) on the India PIT data", "QG-D5"),
    ("Size valuation-spread timing", "US first gate: T1−T3 +16.05pp next-12m; corr −0.69 at 36m",
     "in-sample existence test PASSED; India version waits on NSE index P/E-P/B (2021 splice named)", "SC-D1"),
    ("Smallcap winter rebound (India)", "trailing-36m LO tercile → +10.32%/12m",
     "IIMA-only support after the panel cross-check refused to corroborate — a watch, never a tilt", "SC-D3 · SC-D3a"),
    ("VRP harvesting at scale", "in-state capture +5.58 vs +2.96 unconditional",
     "H60-VRP registration deferred until real chains + post-2023 VIX land", "OP-D2 · F16"),
    ("dp x inflation corner", "+5.1pp real-time corner spread, no OOS forecast value",
     "expectations qualifier only", "ER-D7"),
]
GRAVE = [
    ("Fundamental momentum (EPS Δrank)", "D10−D1 −3.03%/yr; gate +0.42 vs +2.00", "ES-D1"),
    ("Repo-direction factor conditioning", "RMW better in FALLING; market split reverses post-1990", "FUN-D10"),
    ("US SMB momentum post-publication", "+7.96 pre-1981 → −0.4/−0.7 after", "SC-D2"),
    ("Unconditional India smallcap beta", "−2.9pp/yr for 32y, deeper DDs, more vol", "TL-D2"),
    ("Mean reversion, all frequencies", "net −0.80%/mo at 89% turnover", "MR1-S · MR-D1"),
    ("Weekly option sells", "in-sample ruin at full margin; dead OOS at earmark", "OP-D2 F17 · OP-D7"),
    ("IV-confirmation of the stress spine", "India VIX a WORSE classifier (AUROC 0.770 vs 0.786)", "F5a · FS-D3"),
    ("Growth as a stock signal", "never pays at any horizon, panel or large-cap", "QG-D2/D4"),
]
GATED = [
    ("India PEAD event study", "filed EPS + filing_date (both in the handoff schema)", "the data drop"),
    ("India size valuation-spread timer", "NSE index P/E-P/B daily history", "niftyindices pull"),
    ("Dilution-adjusted small-growth", "shares_outstanding history", "the data drop"),
    ("QG-D6 India q-EG (frozen)", "the full authenticated vault", "the data drop"),
    ("H60-VRP registration", "real option chains + post-2023 India VIX", "Priority-1 pulls"),
    ("Full F2 / true MR1 / CR-D2", "PIT bhavcopy", "Priority-1 pulls"),
]


def rows3(items, cls=""):
    out = ""
    for name, num, note, ref in items:
        out += (f'<tr><td><b>{name}</b></td><td class="mono">{num}</td>'
                f'<td>{note}</td><td class="mono ref">{ref}</td></tr>')
    return out


m7, m8 = es["m7"], es["m8"]
gate_pass = m7["corner_increment_1m"] >= 2.0 and m8["corner_increment_1m"] > 0
gate_lab = ('<span class="flag good">GATE MET — flag registrable</span>' if gate_pass
            else '<span class="flag bad">GATE FAILED — value+catalyst dead on this panel</span>')

html = f"""<title>The Edge Map</title>
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
.wrap {{ max-width:1080px; margin:0 auto; display:flex; flex-direction:column; gap:26px; }}
h1 {{ font:700 30px/1.15 "Archivo",system-ui,sans-serif; letter-spacing:-.3px; margin:0; text-wrap:balance; }}
h2 {{ font:650 19px/1.2 "Archivo",system-ui,sans-serif; margin:0 0 4px; }}
.sub {{ color:var(--ink2); max-width:76ch; margin:6px 0 0; }}
.prov {{ display:flex; gap:14px; flex-wrap:wrap; font:12px "IBM Plex Mono",monospace; color:var(--mut); }}
.badge {{ padding:1px 8px; border:1px solid var(--line); border-radius:10px; }}
.panel {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:18px 20px; }}
.grid2 {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(430px,1fr)); gap:18px; }}
.grid3 {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:18px; }}
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
.tblwrap {{ overflow-x:auto; }}
table.plain {{ border-collapse:collapse; font-size:13.5px; width:100%; min-width:560px; }}
.plain th, .plain td {{ padding:6px 10px; border-bottom:1px solid var(--line); text-align:right;
  vertical-align:top; }}
.plain th:first-child, .plain td:first-child {{ text-align:left; }}
table.ledger {{ border-collapse:collapse; font-size:13.5px; width:100%; min-width:720px; }}
.ledger td {{ padding:8px 10px; border-bottom:1px solid var(--line); vertical-align:top; }}
.ledger tr:last-child td {{ border-bottom:none; }}
.mono {{ font:12.5px "IBM Plex Mono",monospace; font-variant-numeric:tabular-nums; white-space:normal; }}
.ref {{ color:var(--mut); white-space:nowrap; }}
.pos {{ color:var(--good); font-weight:600; }} .neg {{ color:var(--bad); font-weight:600; }}
.note {{ font-size:13px; color:var(--mut); max-width:96ch; }}
td, th {{ font-variant-numeric:tabular-nums; }}
</style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700&family=Source+Sans+3:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<div class="wrap">
<header>
<h1>The Edge Map</h1>
<p class="sub">Every measured edge in the Cycle Program register on one page, ranked by what the desk actually
does with it — consumed, flagged, buried, or waiting on data — plus the ES-D2 / SC-D4 / SC-D5 matrix
batteries that ask WHERE each edge lives in the cap spectrum. Every number is a booked ledger print
(entry cited per row); paper, zero costs unless a cost print is quoted. Census 1,189.</p>
<div class="prov"><span class="badge">CONSUMED = in the book/playbook today</span>
<span class="badge">FLAG/WATCH = registered, not consumed</span>
<span class="badge">GRAVEYARD = a kill that prevents bleed</span>
<span class="badge">GATED = registrable the day its data lands</span></div>
</header>

<section class="panel">
<h2>1 · Consumed — the edges the book runs on <span class="flag good">IN PRODUCTION DOCTRINE</span></h2>
<div class="tblwrap"><table class="ledger"><tbody>{rows3(CONSUMED)}</tbody></table></div>
</section>

<section class="panel">
<h2>2 · Flags &amp; watches — real prints, deliberately unconsumed</h2>
<div class="tblwrap"><table class="ledger"><tbody>{rows3(FLAGS)}</tbody></table></div>
</section>

<section class="panel">
<h2>3 · Where the signals live in the cap spectrum — the SC-D4 edge map</h2>
<p class="sub">Within each size quintile, the Q-spread of six signals (EW, US firm panel 1999-2019,
survivor-tilted — the LARGE end is the honest, NIFTY-750-implementable read). Positive = the signal's
long side wins. {d4.get("convention", "")}</p>
<h2 style="font-size:15px">Forward 1 month, %/yr</h2>
{spread_table(d4["h1m"], "%/yr")}
<h2 style="font-size:15px; margin-top:14px">Forward 12 months, %</h2>
{spread_table(d4["h12m"], "%")}
</section>

<section class="panel">
<h2>4 · Size &times; value and size &times; momentum — the quadrants (SC-D5)</h2>
<div class="grid2">
<div><h2 style="font-size:14px">size &times; P/B, fwd 1m %/yr</h2>{heat(d5["j1"]["grid"], rows="size", cols="P/B", clab=["cheap","Q2","Q3","Q4","exp."])}</div>
<div><h2 style="font-size:14px">size &times; P/B, fwd 12m %</h2>{heat(d5["j3"]["grid"], rows="size", cols="P/B", clab=["cheap","Q2","Q3","Q4","exp."])}</div>
<div><h2 style="font-size:14px">size &times; momentum, fwd 1m %/yr</h2>{heat(d5["j4"]["grid"], rows="size", cols="mom", clab=["losers","Q2","Q3","Q4","winners"])}</div>
<div><h2 style="font-size:14px">size &times; momentum, fwd 12m %</h2>{heat(d5["j5"]["grid"], rows="size", cols="mom", clab=["losers","Q2","Q3","Q4","winners"])}</div>
</div>
<p class="note">Four corners at 12m (EW, %): small-value {d5["j6"]["small_value"]:+.1f} ·
small-growth {d5["j6"]["small_growth"]:+.1f} · large-value {d5["j6"]["large_value"]:+.1f} ·
large-growth {d5["j6"]["large_growth"]:+.1f}. Size rows Q1 = smallest. EW-survivor caveat: the small
rows are level-inflated; read the SHAPE, and weight the large rows.</p>
</section>

<section class="panel">
<h2>5 · The revision-proxy interactions (ES-D2) {gate_lab}</h2>
<p class="sub">EPS Δrank (3m) crossed with everything. The main effect is NEGATIVE on this panel (ES-D1);
the registered question was whether a cheap+improving corner rescues it. Corner reads (EW ann):
cheap+improving {m7["cheap_improving_1m"]:+.1f} vs cheap-alone {m7["cheap_alone_1m"]:+.1f} at 1m
(increment {m7["corner_increment_1m"]:+.2f}; gate ≥ +2.00) · at 12m {m7["cheap_improving_12m"]:+.1f}
vs {m7["cheap_alone_12m"]:+.1f}; large-cap corner increment {m8["corner_increment_1m"]:+.2f} at 1m.
Expensive+deteriorating — the avoid corner: {m7["expensive_deteriorating_1m"]:+.1f} /
{m7["expensive_deteriorating_12m"]:+.1f} (large-cap {m8["expensive_deteriorating_1m"]:+.1f} /
{m8["expensive_deteriorating_12m"]:+.1f}).</p>
<div class="grid2">
<div><h2 style="font-size:14px">&Delta;EPS &times; P/B, fwd 1m</h2>{heat(es["m1"]["grid"], rows="&Delta;EPS", cols="P/B", clab=["cheap","Q2","Q3","Q4","exp."])}</div>
<div><h2 style="font-size:14px">&Delta;EPS &times; momentum, fwd 1m</h2>{heat(es["m2"]["grid"], rows="&Delta;EPS", cols="mom", clab=["losers","Q2","Q3","Q4","winners"])}</div>
<div><h2 style="font-size:14px">&Delta;EPS &times; size, fwd 1m</h2>{heat(es["m3"]["grid"], rows="&Delta;EPS", cols="size", clab=["small","Q2","Q3","Q4","large"])}</div>
<div><h2 style="font-size:14px">&Delta;EPS &times; ROE, fwd 1m</h2>{heat(es["m4"]["grid"], rows="&Delta;EPS", cols="ROE", clab=["junk","Q2","Q3","Q4","best"])}</div>
<div><h2 style="font-size:14px">&Delta;EPS &times; volatility, fwd 1m</h2>{heat(es["m5"]["grid"], rows="&Delta;EPS", cols="vol", clab=["calm","Q2","Q3","Q4","wild"])}</div>
<div><h2 style="font-size:14px">&Delta;EPS &times; P/B, fwd 12m</h2>{heat(es["m6"]["grid"], rows="&Delta;EPS", cols="P/B", clab=["cheap","Q2","Q3","Q4","exp."])}</div>
</div>
</section>

<section class="panel">
<h2>6 · The graveyard — negative edge avoided <span class="flag bad">EVERY KILL IS ALPHA</span></h2>
<div class="tblwrap"><table class="ledger"><tbody>
{"".join(f'<tr><td><b>{n}</b></td><td class="mono">{p}</td><td class="mono ref">{r}</td></tr>' for n, p, r in GRAVE)}
</tbody></table></div>
</section>

<section class="panel">
<h2>7 · Gated — registrable the day the data lands</h2>
<div class="tblwrap"><table class="ledger"><tbody>
{"".join(f'<tr><td><b>{n}</b></td><td>{d}</td><td class="mono ref">{u}</td></tr>' for n, d, u in GATED)}
</tbody></table></div>
<p class="note">Sources of record: research/register/trial-ledger.md (entries cited per row) ·
research/register/trial-count.md (census) · research/notes/es_sc_matrices/*.json (grids) ·
india-regime-playbook.md. The EW-survivor firm panel flatters small caps and deletes failures —
matrix SHAPES and large-cap rows carry the evidence; levels do not. This page regenerates from the
repo via scripts/build_edge_map.py, never from memory.</p>
</section>
</div>
"""
OUT.write_text(html)
print(f"written {OUT} ({len(html):,} bytes); gate_pass={gate_pass}")
