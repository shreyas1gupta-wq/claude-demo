"""QG-D1 — payout vs subsequent aggregate earnings growth (Arnott-Asness 2003 re-run
on Shiller 1871-2023). Registered 2026-09-08 BEFORE this run. Payout = D/E nominal,
6m availability lag; real-E>0 and real-D>0 guards; growth = annualized log real-E
growth; monthly overlapping obs FLAGGED — direction/magnitude only. Prints only.
"""
import numpy as np
import pandas as pd
from scipy import stats

V = "/home/user/claude-demo/ingest/vault"
sh = pd.read_csv(f"{V}/us_index/sp500_shiller_monthly_1871.csv", parse_dates=["Date"])
sh = sh[sh["Real Price"] > 0].set_index("Date")
RE = sh["Real Earnings"]
RE = RE[RE > 0]
RD = sh["Real Dividend"]
RD = RD[RD > 0]
E, D = sh["Earnings"], sh["Dividend"]

payout = (D / E).where((E > 0) & (D > 0)).shift(6)  # 6m availability lag
g10 = (np.log(RE.shift(-120)) - np.log(RE)) / 10
g5 = (np.log(RE.shift(-60)) - np.log(RE)) / 5
trend10 = RE.shift(6).rolling(120).median()
depressed = (RE.shift(6) < trend10)

df = pd.DataFrame({"po": payout, "g10": g10, "g5": g5, "dep": depressed}).dropna(subset=["po"])
med = df.po.expanding(120).median()
hi = df.po > med

print(f"QG-D1 — payout vs subsequent real-E growth, {df.index[0].date()}..{df.index[-1].date()} "
      "(monthly overlapping — direction/magnitude only, FLAGGED):")

v = df.dropna(subset=["g10"])
rho = stats.spearmanr(v.po, v.g10)[0]
print(f"  q1 rank-corr(payout, next-10y real-E growth) = {rho:+.2f} (n={len(v)} overlapping months)")

h_, l_ = v[hi.reindex(v.index).fillna(False)], v[~hi.reindex(v.index).fillna(False)]
print(f"  q2 next-10y real-E growth: HIGH payout {100*h_.g10.median():+.2f}%/yr vs "
      f"LOW payout {100*l_.g10.median():+.2f}%/yr (gap {100*(h_.g10.median()-l_.g10.median()):+.2f}pp)")

v5 = df.dropna(subset=["g5"])
h5, l5 = v5[hi.reindex(v5.index).fillna(False)], v5[~hi.reindex(v5.index).fillna(False)]
print(f"  q3 next-5y: HIGH {100*h5.g5.median():+.2f}%/yr vs LOW {100*l5.g5.median():+.2f}%/yr")

p = v[v.index >= "1950-01-01"]
hp, lp = p[hi.reindex(p.index).fillna(False)], p[~hi.reindex(p.index).fillna(False)]
print(f"  q4 post-1950 10y: HIGH {100*hp.g10.median():+.2f}%/yr vs LOW {100*lp.g10.median():+.2f}%/yr")

# q5 mechanism: is high payout just the depressed-earnings state?
vd = v.dropna(subset=["dep"])
share_dep_hi = vd[hi.reindex(vd.index).fillna(False)].dep.mean()
share_dep_lo = vd[~hi.reindex(vd.index).fillna(False)].dep.mean()
# and the split within non-depressed months (the clean read)
nd = vd[vd.dep == False]  # noqa: E712
hn, ln_ = nd[hi.reindex(nd.index).fillna(False)], nd[~hi.reindex(nd.index).fillna(False)]
print(f"  q5 mechanism: high-payout months are depressed-E {100*share_dep_hi:.0f}% of the time "
      f"vs {100*share_dep_lo:.0f}% for low-payout; WITHIN non-depressed months the gap is "
      f"{100*(hn.g10.median()-ln_.g10.median()):+.2f}pp (HIGH {100*hn.g10.median():+.2f} vs "
      f"LOW {100*ln_.g10.median():+.2f})")
