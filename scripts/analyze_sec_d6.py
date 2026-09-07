"""SEC-D6 — the characteristic decomposition of crisis safety (India panel).

Registered 2026-09-07 BEFORE this run; axis scores, composite definition and bars live in
the ledger. Reuses the SEC-D1 basket/REL machinery verbatim. Prints only.
"""
import sys

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, "/home/user/claude-demo")
from scripts.analyze_sec_battery import BASKETS, EPISODES, rel, cum_rel  # noqa: E402

STRESS = ["E1 TAPER (ccy)", "E3 NBFC (credit)", "E4 COVID (crisis)", "E5 INR+OIL (ccy)"]
RECOV = "E4b RECOVERY"
AXES = {
    "EXPORT": {"IT": 2, "PHARMA": 2, "METALS": 1},
    "CYCLICALITY": {"FMCG": 0, "PHARMA": 0, "UTILITIES": 0, "IT": 1, "ENERGY": 1,
                    "AUTO": 2, "DURABLES": 2, "CAPGOODS": 2, "METALS": 2, "CEMENT": 2,
                    "REALTY": 2, "PVTBANK": 2, "PSUBANK": 2, "NBFC": 2},
    "LEVERAGE": {"IT": 0, "FMCG": 0, "PHARMA": 0, "DURABLES": 0, "AUTO": 1, "CEMENT": 1,
                 "ENERGY": 1, "CAPGOODS": 1, "METALS": 2, "REALTY": 2, "UTILITIES": 2,
                 "PVTBANK": 2, "PSUBANK": 2, "NBFC": 2},
    "DURABILITY": {"FMCG": 0, "PHARMA": 0, "ENERGY": 0, "METALS": 1, "CEMENT": 1,
                   "AUTO": 2, "DURABLES": 2, "CAPGOODS": 2, "REALTY": 2},
}
ep = {lab: {k: cum_rel(k, a, b) for k in BASKETS} for lab, a, b in EPISODES}
comp = {k: float(np.mean([ep[e][k] for e in STRESS])) for k in BASKETS}
worst = {k: min(ep[e][k] for e in STRESS) for k in BASKETS}

print("SEC-D6 — stress composite (mean cum REL over E1/E3/E4/E5, pp) and worst episode:")
for k in sorted(comp, key=comp.get, reverse=True):
    sc = " ".join(f"{a[:3]}={AXES[a].get(k, 0) if a != 'DURABILITY' else AXES[a].get(k, 'na')}"
                  for a in AXES)
    print(f"  {k:>9}: comp {100*comp[k]:+6.1f} | worst {100*worst[k]:+6.1f} | {sc}")

print("\nc1 — rank-corr(stress composite, axis score):")
for a, scores in AXES.items():
    ks = list(scores) if a == "DURABILITY" else list(BASKETS)
    x = [scores.get(k, 0) for k in ks]
    y = [comp[k] for k in ks]
    print(f"  {a:12}: rho {stats.spearmanr(x, y)[0]:+.2f} (n={len(ks)})")

print("\nc2 — clean pairwise contrasts (stress composite, pp):")
for i, (m, s, lab) in enumerate([
        ("FMCG", "DURABLES", "non-cyclicality effect (leverage ~held)"),
        ("IT", "FMCG", "export hedge vs domestic defensive (two-sided)"),
        ("IT", "METALS", "exporter-margin vs global-priced+leveraged (bar >= +15)"),
        ("FMCG", "UTILITIES", "leverage penalty, cyclicality held at 0")], 1):
    print(f"  (i{'i'*(i-1)}) {m} - {s} = {100*(comp[m]-comp[s]):+.1f}pp  [{lab}]")

print("\nc3 — the same axis rank-corrs on E4b RECOVERY:")
for a, scores in AXES.items():
    ks = list(scores) if a == "DURABILITY" else list(BASKETS)
    x = [scores.get(k, 0) for k in ks]
    y = [ep[RECOV][k] for k in ks]
    print(f"  {a:12}: rho {stats.spearmanr(x, y)[0]:+.2f}")

qual = [k for k in BASKETS if worst[k] >= -0.05]
print(f"\nc4 — SAFEST SEATS (worst stress episode >= -5pp): {qual if qual else 'NONE'}")
print("   full worst-episode order: " + ", ".join(
    f"{k} {100*worst[k]:+.1f}" for k in sorted(worst, key=worst.get, reverse=True)))
