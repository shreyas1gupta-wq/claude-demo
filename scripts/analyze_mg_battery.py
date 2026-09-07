"""MG-D1..D4 — the macro gap-closer (yield curve, twin deficits, disaster census,
demographics/fiscal). Registered 2026-09-07 BEFORE this run. Prints only."""
import sys

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile  # noqa: E402

ROOT = "/home/user/claude-demo/ingest/vault"
df = pd.ExcelFile(f"{ROOT}/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
df = df[["country", "year", "cpi", "eq_tr", "bond_tr", "housing_tr", "stir", "ltrate",
         "ca", "gdp", "pop", "revenue", "expenditure", "xrusd",
         "rgdpmad"]].sort_values(["country", "year"])

frames = []
for c, g in df.groupby("country"):
    g = g.set_index("year").copy()
    g["infl"] = g.cpi.pct_change()
    g["req"] = (1 + g.eq_tr) / (1 + g.infl) - 1
    g["rbond"] = (1 + g.bond_tr) / (1 + g.infl) - 1
    g["rhouse"] = (1 + g.housing_tr) / (1 + g.infl) - 1
    g["grw"] = np.log(g.rgdpmad).diff()
    g["slope"] = g.ltrate - g.stir
    g["cagdp"] = g.ca / g.gdp
    g["ca_pct"] = expanding_percentile(g.cagdp.to_numpy(), min_obs=20)
    g["fis"] = (g.revenue - g.expenditure) / g.gdp
    g["fis_pct"] = expanding_percentile(g.fis.to_numpy(), min_obs=20)
    g["pop10"] = np.log(g["pop"]).diff().rolling(10).mean()
    g["feq10"] = np.log1p(g.req).rolling(10).mean().shift(-10).apply(np.expm1)
    g["feq5"] = np.log1p(g.req).rolling(5).mean().shift(-5).apply(np.expm1)
    g["fbd5"] = np.log1p(g.rbond).rolling(5).mean().shift(-5).apply(np.expm1)
    g["g_next"] = g.grw.shift(-1)
    g["req_next"] = g.req.shift(-1)
    g["rbd_next"] = g.rbond.shift(-1)
    g["dep_next"] = (np.log(g.xrusd).diff().shift(-1)) if c != "USA" else np.nan
    g["country"] = c
    frames.append(g.reset_index())
p = pd.concat(frames, ignore_index=True)
pw = p[(p.year >= 1950) & (p.year <= 2020)]

print("MG-D1 — THE YIELD CURVE (1950-2020):")
j = pw[["slope", "g_next"]].dropna()
print(f"  d1 corr(slope, next-1y growth) = {stats.spearmanr(j.slope, j.g_next)[0]:+.2f} (n={len(j)})")
inv = pw[pw.slope < 0].dropna(subset=["slope"])
nrm = pw[pw.slope >= 0].dropna(subset=["slope"])
print(f"  d2 INVERTED years (n={len(inv)}): next-1y growth {100*inv.g_next.mean():+.1f}% vs "
      f"normal {100*nrm.g_next.mean():+.1f}%; negative-growth freq {100*(inv.g_next<0).mean():.0f}% "
      f"vs {100*(nrm.g_next<0).mean():.0f}%")
j = pw[["slope", "req_next"]].dropna()
print(f"  d3 corr(slope, next-1y real equity) = {stats.spearmanr(j.slope, j.req_next)[0]:+.2f} (n={len(j)})")
print(f"  d4 next-1y real BOND after inversion: {100*inv.rbd_next.mean():+.1f}% vs normal "
      f"{100*nrm.rbd_next.mean():+.1f}%")

print("\nMG-D2 — TWIN DEFICITS (1950-2020):")
cad = pw[pw.ca_pct <= 0.2]
oth = pw[(pw.ca_pct > 0.2) & pw.ca_pct.notna()]
print(f"  d1 worst-CAD years (n={len(cad)}): next-1y depreciation {100*cad.dep_next.mean():+.1f}% "
      f"vs others {100*oth.dep_next.mean():+.1f}%")
print(f"  d2 next-1y local real equity: CAD {100*cad.req_next.mean():+.1f}% vs others "
      f"{100*oth.req_next.mean():+.1f}%")
j = pw[["cagdp", "req"]].dropna()
print(f"  d3 corr(ca/gdp, same-yr real equity) = {stats.spearmanr(j.cagdp, j.req)[0]:+.2f} (n={len(j)})")
pos = tot = 0
for c, g in pw[pw.country != "USA"].groupby("country"):
    a = g[g.ca_pct <= 0.2].dep_next.mean()
    b = g[(g.ca_pct > 0.2) & g.ca_pct.notna()].dep_next.mean()
    if not (np.isnan(a) or np.isnan(b)):
        tot += 1
        pos += (a > b)
print(f"  d4 sign census: CAD years depreciate more in {pos}/{tot} countries")

print("\nMG-D3 — THE RARE-DISASTER CENSUS (full span, real total-return indices):")


def disaster(g, col):
    s = g.set_index("year")[col].dropna()
    if len(s) < 40:
        return None
    idx = np.log1p(s).cumsum()
    peak = idx.cummax()
    dd = idx - peak
    t = dd.idxmin()
    depth = 100 * (1 - np.exp(dd.min()))
    peak_lvl = peak.loc[t]
    after = idx.loc[t:]
    rec = after[after >= peak_lvl]
    yrs = (rec.index[0] - idx.loc[:t][idx.loc[:t] == peak_lvl].index[-1]) if len(rec) else None
    return depth, int(t), (int(yrs) if yrs is not None else None)


eq_d, ho_d = [], []
print(f"  {'country':>12} {'eq worst':>9} {'trough':>7} {'recov yrs':>10} | {'housing worst':>14} {'recov':>6}")
for c, g in p.groupby("country"):
    e = disaster(g, "req")
    h = disaster(g, "rhouse")
    if e:
        eq_d.append(e)
    if h:
        ho_d.append(h)
    if e:
        hh = f"{h[0]:>13.0f}% {str(h[2]) if h and h[2] else '>':>6}" if h else " " * 20
        print(f"  {c:>12} {e[0]:>8.0f}% {e[1]:>7} {str(e[2]) if e[2] else '>span':>10} | {hh}")
print(f"  d2 EQUITY medians: depth {np.median([d[0] for d in eq_d]):.0f}%, recovery "
      f"{np.median([d[2] for d in eq_d if d[2]]):.0f}y (n={len(eq_d)})")
print(f"  d3 HOUSING medians: depth {np.median([d[0] for d in ho_d]):.0f}%, recovery "
      f"{np.median([d[2] for d in ho_d if d[2]]):.0f}y (n={len(ho_d)})")

print("\nMG-D4 — DEMOGRAPHICS + FISCAL (1950-2020):")
j = pw[["pop10", "feq10"]].dropna()
print(f"  d1 corr(trail-10y pop growth, next-10y real equity) = "
      f"{stats.spearmanr(j.pop10, j.feq10)[0]:+.2f} (n={len(j)})")
j = pw[["fis_pct", "feq5"]].dropna()
k = pw[["fis_pct", "fbd5"]].dropna()
print(f"  d2 fiscal-balance pct -> next-5y equity rho {stats.spearmanr(j.fis_pct, j.feq5)[0]:+.2f} "
      f"(n={len(j)}) | -> bonds rho {stats.spearmanr(k.fis_pct, k.fbd5)[0]:+.2f} (n={len(k)})")
