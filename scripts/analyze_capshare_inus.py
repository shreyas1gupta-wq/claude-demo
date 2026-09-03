"""Capital share (1 - labsh, PWT 10.0) for India & USA + link to next-10y equity returns.

CONTEXT NOTE computation (descriptive; unregistered, no bar, no census consumption — any
design use requires registration). Equity outcome = next-10y annualized EXCESS return
(equity total return minus bills/RF), avoiding CPI: USA from JST R6 (1950-2010 starts),
India from IIMA monthly factors (market = MF + RF, excess = MF; starts 1994-2015).
"""
import numpy as np
import pandas as pd
from scipy import stats

ROOT = "/home/user/claude-demo"
pwt = pd.read_csv(f"{ROOT}/ingest/vault/macro/pwt100.csv")
lab = [c for c in pwt.columns if "labour compensation" in c][0]
pwt = pwt.rename(columns={"Entity": "countrycode", "Year": "year"})
pwt["capsh"] = 1 - pwt[lab].astype(float) / 100.0
pwt = pwt[["countrycode", "year", "capsh"]].dropna()

print("CAPITAL SHARE BY DECADE (mean, PWT 10.0):")
print(f"{'decade':>7} {'India':>7} {'USA':>7}")
for dec in range(1950, 2020, 10):
    row = []
    for cc in ["India", "United States"]:
        g = pwt[(pwt.countrycode == cc) & (pwt.year >= dec) & (pwt.year < dec + 10)]
        row.append(f"{100*g.capsh.mean():6.1f}" if len(g) else "   n/a")
    print(f"{dec:>6}s {row[0]:>7} {row[1]:>7}")
for cc in ["India", "United States"]:
    g = pwt[pwt.countrycode == cc].sort_values("year")
    print(f"{cc} latest: {int(g.year.iloc[-1])} capsh {100*g.capsh.iloc[-1]:.1f}%  "
          f"(own-history percentile {100*(g.capsh.rank(pct=True).iloc[-1]):.0f}th)")

# USA: capsh level (year t) vs next-10y annualized equity excess return, JST R6
jst = pd.ExcelFile(f"{ROOT}/ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
us = jst[jst.country == "USA"].set_index("year")
exc = ((1 + us.eq_tr) / (1 + us.bill_rate) - 1).dropna()
cap_us = pwt[pwt.countrycode == "United States"].set_index("year").capsh
pairs = []
for t in range(1950, 2011):
    w = exc.loc[t + 1:t + 10]
    if len(w) == 10 and t in cap_us.index:
        pairs.append((cap_us[t], float(np.exp(np.log1p(w).mean()) - 1)))
x, y = np.array(pairs).T
pr, pp = stats.pearsonr(x, y)
sr, sp = stats.spearmanr(x, y)
print(f"\nUSA capsh level -> next-10y equity excess (n={len(pairs)} overlapping starts):")
print(f"  Pearson {pr:+.2f} (p={pp:.3f}, overlap-inflated)   Spearman {sr:+.2f}")
lo, hi = x <= np.median(x), x > np.median(x)
print(f"  below-median capsh -> next-10y excess {100*y[lo].mean():+.1f}%/yr;"
      f" above-median -> {100*y[hi].mean():+.1f}%/yr")

# India: IIMA market excess (MF, monthly %) vs capsh level
iima = pd.read_csv(f"{ROOT}/ingest/vault/factors/iima_monthly_factors.csv")
iima["year"] = iima.Date.str[:4].astype(int)
mf = iima.set_index("Date").MF / 100
cap_in = pwt[pwt.countrycode == "India"].set_index("year").capsh
pairs_in = []
for t in range(1994, 2016):
    w = mf[(iima.set_index("Date").year > t) & (iima.set_index("Date").year <= t + 10)]
    if len(w) == 120 and t in cap_in.index:
        pairs_in.append((cap_in[t], float(np.exp(np.log1p(w).mean() * 12) - 1)))
xi, yi = np.array(pairs_in).T
pri, ppi = stats.pearsonr(xi, yi)
sri, _ = stats.spearmanr(xi, yi)
print(f"\nIndia capsh level -> next-10y equity excess (n={len(pairs_in)} starts, IIMA MF):")
print(f"  Pearson {pri:+.2f} (p={ppi:.3f}, overlap-inflated)   Spearman {sri:+.2f}")
lo, hi = xi <= np.median(xi), xi > np.median(xi)
print(f"  below-median capsh -> {100*yi[lo].mean():+.1f}%/yr; above-median -> {100*yi[hi].mean():+.1f}%/yr")
