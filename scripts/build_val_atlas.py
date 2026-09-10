"""Build docs/learn/artifacts/valuation-edge-atlas.html — the VAL arc dashboard:
measure ladder, complementarity matrix (with the artifact diagnosis), trap anatomy,
factor blends, the CAPE floor test, the register recheck, and the India design queue.
Every desk number is a booked ledger print (VAL-D1..D5 + quoted entries); house style."""
import json
from pathlib import Path

R = Path("/home/user/claude-demo")
J = json.loads((R / "research/notes/es_sc_matrices/val.json").read_text())
D6 = json.loads((R / "research/notes/es_sc_matrices/val_d6.json").read_text())
OUT = R / "docs/learn/artifacts/valuation-edge-atlas.html"

d1, d2, d3, d4, d5 = J["val_d1"], J["val_d2"], J["val_d3"], J["val_d4"], J["val_d5"]


def cls(x, th=0.5):
    return "pos" if x > th else ("neg" if x < -th else "")


meas_rows = ""
NAMES = {"Pb": "P/B (low)", "Pe": "P/E (low)", "Ev_Ebitda": "EV/EBITDA (low)", "Fcf_Yld": "FCF yield (high)",
         "Div_Yld": "Dividend yield (high)", "Bb_Yld": "Buyback yield (high)", "COMPOSITE": "COMPOSITE (Pb+EV+FCF ranks)"}
for k in ["COMPOSITE", "Pb", "Div_Yld", "Ev_Ebitda", "Fcf_Yld", "Pe", "Bb_Yld"]:
    v = d1[k]
    hl = ' style="font-weight:600"' if k in ("COMPOSITE", "Pb") else ""
    meas_rows += (f'<tr{hl}><td>{NAMES[k]}</td>'
                  + "".join(f'<td class="{cls(x)}">{x:+.2f}</td>' for x in v) + "</tr>")

CNAMES = {"Roe": "ROE (high)", "Mom_11M_Usd": "Momentum (winners)", "Vol1Y_Usd": "Low volatility",
          "Debtequity": "Low leverage", "Share_Turn_12M": "Low turnover", "Eps_Basic_Gr": "EPS growth (high)",
          "Bb_Yld": "Buyback yield (high)", "d3": "EPS Δrank (improving)"}
comp_rows = ""
for k, nm in CNAMES.items():
    r = d2[k]
    v = r["verdict"]
    vc = "gate" if "REDUND" in v else "bad"
    comp_rows += (f'<tr><td>{nm}</td><td class="{cls(r["wcs"])}">{r["wcs"]:+.2f}</td>'
                  f'<td class="pos">{r["vsc"]:+.2f}</td><td class="{cls(r["szQ5_wcs"])}">{r["szQ5_wcs"]:+.2f}</td>'
                  f'<td><span class="st {vc}">{v}</span></td></tr>')

TNAMES = {"Debtequity": "Low leverage", "d12e": "Rising EPS (12m)", "Vol1Y_Usd": "Low volatility",
          "Roe": "High ROE", "Share_Turn_12M": "Low turnover"}
trap_rows = "".join(f'<tr><td>{TNAMES[k]}</td><td class="{cls(v[0])}">{v[0]:+.2f}</td>'
                    f'<td class="{cls(v[1])}">{v[1]:+.2f}</td></tr>' for k, v in d3.items())

corr_chips = " ".join(f'<span class="chip">{k} <b>{v:+.2f}</b></span>' for k, v in d4["corr"].items())
blend_rows = ""
for x, (sh_h, sh_x, sh_b) in d4["blends"].items():
    tag = ('<span class="st good">THE COMPLEMENT</span>' if x == "UMD"
           else '<span class="st bad">REDUNDANT</span>' if x == "CMA" else '<span class="st gate">CRUMBS</span>')
    blend_rows += (f'<tr><td>50/50 HML + {x}</td><td>{sh_h:+.2f}</td><td>{sh_x:+.2f}</td>'
                   f'<td class="pos"><b>{sh_b:+.2f}</b></td><td>{tag}</td></tr>')

def half_rows(block, order, names):
    rows = ""
    for k in order:
        v = block[k]
        s, l = v["small"], v["large"]
        rows += (f'<tr><td>{names.get(k, k)}</td>'
                 + "".join(f'<td class="{cls(x)}">{x:+.2f}</td>' for x in s)
                 + "".join(f'<td class="{cls(x)}">{x:+.2f}</td>' for x in l) + "</tr>")
    return rows


D6M_NAMES = {"Pb": "P/B", "Pe": "P/E", "Ev_Ebitda": "EV/EBITDA", "Fcf_Yld": "FCF yield",
             "Div_Yld": "Dividend yield", "Bb_Yld": "Buyback yield", "Ebit_Bv": "EBIT/book (hybrid — flagged)"}
D6X_NAMES = {"VAL2": "VAL2 · P/B+P/E", "VAL3": "VAL3 · P/B+EV+FCF", "VAL4": "VAL4 · +Div yield",
             "CQ": "Cheap-quality (P/B+ROE)", "VM": "Value-momentum (P/B+Mom)", "VLV": "Value-low-vol"}
d6_meas = half_rows(D6["measures"], ["Pb", "Pe", "Ev_Ebitda", "Fcf_Yld", "Div_Yld", "Bb_Yld", "Ebit_Bv"], D6M_NAMES)
d6_mix = half_rows(D6["mixes"], ["VAL2", "VAL3", "VAL4", "CQ", "VM", "VLV"], D6X_NAMES)

floor_rows = "".join(
    f'<tr><td>{lab}</td><td class="{cls(d5[lab][0], 0.1)}">{d5[lab][0]:+.2f}</td>'
    f'<td>{d5[lab][1]:+.2f}</td><td>{d5[lab][2]:+.2f}</td><td class="mut">{d5[lab][3]}</td></tr>'
    for lab in ["CHEAP", "MID", "EXPENSIVE"])

html = f"""<title>Valuation Edge Atlas</title>
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
.sub {{ color:var(--ink2); max-width:78ch; margin:6px 0 0; }}
.prov {{ display:flex; gap:14px; flex-wrap:wrap; font:12px "IBM Plex Mono",monospace; color:var(--mut); }}
.badge {{ padding:1px 8px; border:1px solid var(--line); border-radius:10px; }}
.panel {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:18px 20px; }}
.verdicts {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(290px,1fr)); gap:12px; }}
.v {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:14px 16px; }}
.v b {{ font-family:"Archivo"; font-size:15.5px; }}
.v .num {{ font:600 24px/1.25 "IBM Plex Mono",monospace; font-variant-numeric:tabular-nums; margin:4px 0; }}
.tblwrap {{ overflow-x:auto; }}
table.plain {{ border-collapse:collapse; font-size:13.5px; width:100%; min-width:560px; }}
.plain th, .plain td {{ padding:6px 10px; border-bottom:1px solid var(--line); text-align:right; vertical-align:top; }}
.plain th:first-child, .plain td:first-child {{ text-align:left; }}
.plain td.pos {{ color:var(--good); font-weight:600; }} .plain td.neg {{ color:var(--bad); font-weight:600; }}
.plain td.mut {{ color:var(--mut); }}
.st {{ display:inline-block; font:600 10.5px "Archivo"; letter-spacing:.4px; padding:2px 8px; border-radius:9px; white-space:nowrap; }}
.st.good {{ color:var(--good); background:var(--goodbg); }} .st.bad {{ color:var(--bad); background:var(--badbg); }}
.st.gate {{ color:var(--gate); background:var(--gatebg); }}
.flag {{ display:inline-block; font:600 11px "Archivo"; letter-spacing:.4px; padding:2px 8px; border-radius:9px; margin-left:6px; vertical-align:2px; }}
.flag.bad {{ color:var(--bad); background:var(--badbg); }} .flag.good {{ color:var(--good); background:var(--goodbg); }}
.warn {{ background:var(--amberbg); color:var(--amber); border-radius:8px; padding:12px 16px; margin:12px 0 0; font-size:13.5px; max-width:100ch; }}
.chip {{ display:inline-block; font:12.5px "IBM Plex Mono",monospace; border:1px solid var(--line);
  border-radius:9px; padding:2px 9px; margin:2px 4px 2px 0; }}
.note {{ font-size:13px; color:var(--mut); max-width:96ch; }}
ul.q {{ margin:8px 0 0; padding-left:20px; }} ul.q li {{ margin:6px 0; max-width:86ch; }}
td, th {{ font-variant-numeric:tabular-nums; }}
</style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700&family=Source+Sans+3:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<div class="wrap">
<header>
<h1>Valuation Edge Atlas</h1>
<p class="sub">Valuation as edge, measured at every level the vaults allow: which MEASURE carries the
cross-section, which companion metrics are complementary vs redundant vs artifact, what filters value
traps (and why this panel cannot say), the factor-level pairing doctrine on value-weighted data, and
whether valuation prices the downside floor at the index level. Every number is a booked ledger print
(VAL-D1..D6, 43 cells, census 1,245; quoted entries named). US firm panel = EW, survivor-tilted, no
delistings — large-cap columns carry the honest weight.</p>
<div class="prov"><span class="badge">DESK = ledger print</span><span class="badge">quoted: ER-D1c · QG-D2 c9 · SC-D1/D4 · H36 · CU-D1/D4</span>
<span class="badge">India designs: gated on the fundamentals handoff + NSE valuations</span></div>
</header>

<div class="verdicts">
<div class="v"><b>The complement is momentum</b><div class="num">Sharpe 0.70</div>
50/50 HML+UMD vs 0.32 / 0.54 alone (corr −0.21, VW 1963-2020). With the booked cheap-quality 0.49,
the pairing doctrine is value × momentum × moderate quality.</div>
<div class="v"><b>Valuation prices the floor</b><div class="num">+2.92pp/yr</div>
Cheap-CAPE p10 of next-5y real returns (−2.00) vs expensive (−4.92) — the band role gets numeric
content; the mean stays null-consistent (ER-D1c stands).</div>
<div class="v"><b>The value spread is unsubsumed</b><div class="num">+12.5 to +14.8</div>
The Pb Q1−Q5 spread survives WITHIN every companion family tested (quality, momentum, vol, leverage,
turnover, growth, payout, revisions) — the single most robust cross-sectional fact on the panel.</div>
</div>

<section class="panel">
<h2>1 · The measure ladder (VAL-D1) — which valuation ratio carries the edge</h2>
<div class="tblwrap"><table class="plain">
<thead><tr><th>Measure (cheap side)</th><th>fwd-1m %/yr</th><th>fwd-12m %</th><th>fwd-36m %/yr</th><th>LARGE-CAP 12m %</th></tr></thead>
<tbody>{meas_rows}</tbody></table></div>
<p class="note">The large-cap column is the implementable rank: <b>COMPOSITE ≈ P/B &gt; dividend yield &gt;
EV/EBITDA &gt; FCF yield &gt; P/E &gt; buyback yield</b>. Priors graded honestly: the FCF-yield and
EV≥P/B claims MISSED here; the composite TIES P/B rather than beating it. The teaching print is the
dividend-yield split: −4.6% at panel (in small caps high yield = distress — the QG-D1 payout-state
confound live) but +5.10 in large caps, where yield means discipline. P/B's panel dominance partly
rides the junk bounce — hence the large-cap column as the verdict column.</p>
</section>

<section class="panel">
<h2>2 · The complementarity matrix (VAL-D2) <span class="flag bad">THE WCS SIDE IS THE PANEL TALKING</span></h2>
<div class="tblwrap"><table class="plain">
<thead><tr><th>Companion (good side)</th><th>WCS · adds within cheap?</th><th>VSC · value survives it?</th><th>large-cap WCS</th><th>rule verdict</th></tr></thead>
<tbody>{comp_rows}</tbody></table></div>
<div class="warn"><b>Read this table the way the ledger does.</b> The VSC column is clean and loud:
value is not subsumed by anything tested. The WCS column — every companion's good side "hurting"
among cheap stocks — is the no-delisting artifact at full strength: on a panel where failures were
deleted, the deep-distress corner of the cheap bucket mechanically outperforms, so any filter that
removes distress removes the survivor bounce. Same mechanism, third sighting (QG-D2, SC-D3a, now
here). The within-cheap complementarity question is UNMEASURABLE on this data and moves to the India
PIT panel — whose delisted_registry and promoter-pledge fields exist precisely for this. The
value-weighted factor evidence below is the artifact-free read, and it says the opposite of the WCS
column: momentum and profitability DO complement value.</div>
<h2 style="font-size:15px; margin-top:14px">Value-trap anatomy (VAL-D3) — every filter prints negative, and that is the finding</h2>
<div class="tblwrap"><table class="plain">
<thead><tr><th>Trap filter (good half)</th><th>12m good−bad, pp</th><th>36m, pp/yr</th></tr></thead>
<tbody>{trap_rows}</tbody></table></div>
<p class="note">Prior (Piotroski-flavored: leverage and falling EPS mark traps) MISSED wholesale — because
traps cannot spring on a panel with no deaths. Booked as the measured demonstration that trap-filter
research REQUIRES delisting data; the India design (value + pledge + leverage filters on PIT data with
the delisted registry) is the real test.</p>
</section>

<section class="panel" style="border-left:3px solid var(--good)">
<h2>Update · VAL-D6 — the measure × size × horizon atlas, plus the mixes (14 cells; census 1,245)</h2>
<p class="sub">Every measure and six mix constructions, re-ranked WITHIN the small half (size Q1-2) and
the large half (Q4-5) at 1m / 12m / 3y. P/S is recorded as NOT constructible on this panel (uniformized
ranks — it joins the India design set, where PIT P/S is buildable from the handoff). Columns:
small 1m · 12m · 36m | large 1m · 12m · 36m (%/yr, EW, cheap-minus-expensive or mix Q5−Q1).</p>
<div class="tblwrap"><table class="plain">
<thead><tr><th>Measure</th><th>S 1m</th><th>S 12m</th><th>S 36m</th><th>L 1m</th><th>L 12m</th><th>L 36m</th></tr></thead>
<tbody>{d6_meas}</tbody></table></div>
<div class="tblwrap" style="margin-top:10px"><table class="plain">
<thead><tr><th>Mix</th><th>S 1m</th><th>S 12m</th><th>S 36m</th><th>L 1m</th><th>L 12m</th><th>L 36m</th></tr></thead>
<tbody>{d6_mix}</tbody></table></div>
<p class="note"><b>The which-works-where verdict:</b> P/B owns both halves among single measures; in the
LARGE half the pure-valuation composite VAL3 (P/B+EV+FCF) beats P/B at every horizon (+8.76/+7.80/+5.88
vs +7.15/+7.30/+5.39) — the composite premium exists where measure noise can be averaged. In the SMALL
half every yield measure INVERTS (Div yield −11.6, EBIT/book −19.5 at 12m): the no-delisting bounce pays
distress, so small-cap "value" here is only the low-price side. And the registered key question split:
CQ and VM mixes do NOT beat P/B in large — stock-level rank-mixing fails when an ingredient (this
panel's momentum leg) is artifact-broken. The pairing lesson is level-specific: <b>blend at the sleeve
level (factor portfolios, where HML+UMD prints 0.70), never rank-mix signals at the stock level</b> —
until the India PIT panel can measure the ingredients cleanly. EBIT/book graded weak-hybrid as flagged.</p>
</section>

<section class="panel">
<h2>3 · Factor-level pairing doctrine (VAL-D4, value-weighted — artifact-free)</h2>
<p class="sub">corr(HML, ·) monthly 1963-2020: {corr_chips}</p>
<div class="tblwrap"><table class="plain">
<thead><tr><th>Blend</th><th>HML Sharpe</th><th>partner Sharpe</th><th>blend Sharpe</th><th>verdict</th></tr></thead>
<tbody>{blend_rows}
<tr><td>50/50 value + profitability</td><td>+0.32</td><td>+0.41</td><td class="pos"><b>+0.49</b></td><td><span class="st good">BOOKED (QG-D2 c9)</span></td></tr>
</tbody></table></div>
<p class="note">One honest miss booked: the blend does NOT truncate the tail — worst-12m of HML+UMD is
−37.4% vs HML's own −35.1% (momentum crashes are the blend's own tail event). Complementarity is a
Sharpe fact, not crash protection: sizing and the drawdown governor own the tail, never the blend.
CMA at corr +0.68 with no blend gain is value in drag — never hold both as separate sleeves.</p>
</section>

<section class="panel">
<h2>4 · Does valuation price the floor? (VAL-D5, Shiller 1881-2023) <span class="flag good">BAR PASSED +2.92 ≥ +2.00</span></h2>
<div class="tblwrap"><table class="plain">
<thead><tr><th>CAPE tercile (expanding, lagged)</th><th>p10 next-5y real TR ann</th><th>p50</th><th>p90</th><th>n (overlap)</th></tr></thead>
<tbody>{floor_rows}</tbody></table></div>
<p class="note">The whole distribution shifts — floor, median, and ceiling — from cheap starts. The claim
consumed is deliberately narrow: valuation is a STATE that sets the expected BAND (the floor included)
for expectations and risk budgets. It is still not a timing signal: ER-D1c's persistent-regressor
demotion is quoted, not overturned, and a quantile-level null test is a named future design.</p>
</section>

<section class="panel">
<h2>5 · The register recheck — where valuation already earns its keep</h2>
<ul class="q">
<li><b>Cross-section, every size, every horizon:</b> the value spread survives all five size quintiles
(+9.95%/yr large-cap at 1m, +8.80 at 12m, +6.5pp/yr at 3y, +4.83 at 5y — SC-D4/H36) and orders
size rotation (+16.75pp/yr at 36m — SC-D1/H36 h12).</li>
<li><b>Index level:</b> the dp/CAPE staircase is null-consistent through 10y — only the 20y relation
beats the persistent-regressor null (ER-D1/D1c); the dp × inflation corner is an expectations
qualifier (+5.1pp real-time, no OOS value — ER-D7). No CAPE clock, ever.</li>
<li><b>Currencies:</b> valuation WORKS as a slow anchor where equity indices refuse it — PPP +0.94,
RER → next-5y USD −0.36, crash years are entry states (+13.2 vs +6.2 next-3y) — CU-D1/D3/D4.</li>
<li><b>Quality interaction:</b> cheap-quality beats expensive-quality ~17pp/yr in-panel; blend Sharpe
0.49 (QG-D2 c9) — and the moderation principle bounds it: never extreme-ROE at any price (QG-D3 fade).</li>
<li><b>India:</b> nothing PIT exists yet — Tobin's-q (QG-D6) is frozen and ready; the NSE index
P/E-P/B state and the pledge trap filter are the two named pulls.</li>
</ul>
</section>

<section class="panel">
<h2>6 · What moves to India (design briefs, registrable on data arrival)</h2>
<ul class="q">
<li><b>Within-industry value composite</b> (P1 fields: Pb-proxy from total_equity + Ev-proxy from
debt/cash/mcap) — the measure-ladder re-run where sector mix can't masquerade as cheapness.</li>
<li><b>Value + pledge trap filter</b> (P5 shareholding_pledge) — the trap test this panel could not run,
on data where failure exists (P3 delisted_registry).</li>
<li><b>Value × momentum double sort on PIT membership</b> — the 0.70 pairing tested where it will trade.</li>
<li><b>QG-D6 Tobin's-q expected-growth</b> — frozen, runs on arrival, adjudicates the R_EG flag.</li>
<li><b>The NSE index valuation state</b> — the floor test and the size-spread timer, India form
(2021 consolidated-splice caveat named in advance).</li>
</ul>
<p class="note">Sources of record: trial-ledger entries VAL-D1..D5 (registrations committed before the
run) · es_sc_matrices/val.json · dossiers in research/notes/val-dossiers/ · quoted entries as named.
This page regenerates via scripts/build_val_atlas.py, never from memory.</p>
</section>
</div>
"""
OUT.write_text(html)
print(f"written {OUT} ({len(html):,} bytes)")
