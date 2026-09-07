#!/usr/bin/env python3
"""OP-D2 combiner c03 — management adjudication per tenor (weekly vs monthly).

Inputs: research/opt_sweep/f15.json (structural greeks/stop math, CONFIRMED),
f16.json (monthly sim, CONFIRMED), f17.json (weekly sim, CONFIRMED).
No new market data touched; derives only cost/benefit ratios of numbers
already printed in the parent family JSONs (quoted verbatim below).
"""
import json, os

BASE = "/home/user/claude-demo/research/opt_sweep"
f = {i: json.load(open(os.path.join(BASE, f"{i}.json"))) for i in ("f15", "f16", "f17")}
for i in ("f15", "f16", "f17"):
    assert f[i]["id"] == i

print("== MONTHLY (F16, 41 entries 2011-23, hold: mean +0.557 %S/mo, worst -3.984, p5 -2.528) ==")
# stop-2x (registered bar: cut>=50% at cost<=30% -> MISS both edges)
s_cut, s_cost = 46.0, 32.2
print(f"stop-2x        : worst cut {s_cut}% (-3.984->-2.153), mean cost {s_cost}% "
      f"(+0.557->+0.378), 11/41 stops -> registered MISS both edges")
print(f"  cost per pp of worst-month cut: {s_cost/s_cut:.2f}")
# delta-band roll (unbarred, descriptive)
r_cut, r_cost = 35.5, 9.6
print(f"delta-band roll: |delta|>=0.30 max 3 rolls; worst cut {r_cut}% (-3.984->-2.570), "
      f"mean cost {r_cost}% (+0.557->+0.504), p5 -1.044 (best of 3) -> DESCRIPTIVE, no bar")
print(f"  cost per pp of worst-month cut: {r_cost/r_cut:.2f}")
print(f"  efficiency ratio (stop/roll cost-per-cut): {(s_cost/s_cut)/(r_cost/r_cut):.1f}x")

print()
print("== WEEKLY (F17, 231 traded wks of 611, hold: +1.89%/wk per margin, hit 80%, worst -100%) ==")
w_impr, w_cost = 7.0, 11.0  # worst -100% -> -93.3% ; mean cost 11%
print(f"daily close-stop: worst week -100%->-93.3% (+{w_impr:.0f}% impr) at {w_cost:.0f}% mean cost, "
      f"22/231 stops; stopped arm still compounds to -28.96%/yr (RUIN unstopped)")
print(f"  cost per pp of worst-week cut: {w_cost/w_impr:.2f}  (vs monthly roll {r_cost/r_cut:.2f})")

print()
print("== STRUCTURAL WHY (F15, analytic + measured storm matrix 2010-2023, 3114 days) ==")
print("stop-2x gap-through threshold m* at VIX 12/18/30: 7d 2.0/3.1/5.2% vs 30d 3.9/6.0/10.2%")
print("measured P(gap-through)/day by VIX bucket:        7d 0.57/0.55/2.01% vs 30d 0.00/0.00/0.25%")
print("when gapped (midVIX, 7d): mean 1d loss 2.9x credit (vs intended 2x), max ~8.6-9.0x credit")
print("tenor: 7d = 2.1x gamma at 0.48x vega of 30d -> weekly is gamma/gap risk a close-stop cannot see")
