"""F4a — correlation-spike increment (survivor partial), run exactly as registered.

Top-50 by previous-year median value traded (annually refreshed); mean pairwise correlation
over {21,63}d; expanding percentile min_obs 252; RV leg = index 21d RV percentile (F5a
construction); bars: redundant if Spearman>=0.80, adds if AUROC >= RV+0.03; 6 frozen
episodes 2012-2021. One-way reading declared at registration.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from quant.ladder import expanding_percentile
from quant.ladder.fast_stress import realized_vol
from quant.stats.metrics import auroc

ROOT = Path(__file__).resolve().parents[1]
V = ROOT / "ingest" / "vault"

EPISODES = [  # frozen §3, in-span subset for 2012-2021
    ("Taper tantrum", "2013-05-01", "2013-09-30"),
    ("China deval 2015", "2015-08-01", "2015-09-30"),
    ("Demonetization", "2016-11-08", "2016-11-30"),
    ("Feb-2018 vol+LTCG", "2018-02-01", "2018-03-31"),
    ("IL&FS", "2018-09-01", "2018-10-31"),
    ("COVID crash", "2020-02-20", "2020-04-30"),
]

px = pd.read_csv(V / "panel/n500_adjclose_2012_2022.csv.gz", index_col=0, parse_dates=True)
vt = pd.read_csv(V / "panel/n500_value_traded_2012_2022.csv.gz", index_col=0, parse_dates=True)
rets = px.pct_change()
print(f"panel: {px.shape[1]} names, {px.index.min():%Y-%m-%d}..{px.index.max():%Y-%m-%d}")

# top-50 by previous-year median value traded, refreshed each January
years = sorted(set(px.index.year))
top50 = {}
for y in years[1:]:
    med = vt[vt.index.year == y - 1].median()
    top50[y] = med.dropna().sort_values(ascending=False).head(50).index
print(f"selection years: {years[1]}..{years[-1]} (prior-year value-traded medians)")

# daily mean pairwise correlation over trailing windows, per registered grid
dates = rets.index[rets.index.year >= years[1]]
out = {21: pd.Series(index=dates, dtype=float), 63: pd.Series(index=dates, dtype=float)}
pos = {d: i for i, d in enumerate(rets.index)}
for d in dates:
    names = top50[d.year]
    i = pos[d]
    for w in (21, 63):
        if i - w + 1 < 0:
            continue
        blk = rets.iloc[i - w + 1: i + 1][names].dropna(axis=1, thresh=int(w * 0.9))
        if blk.shape[1] < 30:
            continue
        c = np.corrcoef(blk.T.fillna(0.0))
        out[w][d] = float(c[np.triu_indices_from(c, k=1)].mean())

# RV leg from the index vault (F5a construction, verbatim)
nifty = pd.read_csv(V / "index/nifty50_daily_2007_2026.csv",
                    parse_dates=["Date"]).sort_values("Date").reset_index(drop=True)
nifty["ret"] = nifty["Close"].pct_change()
nifty = nifty.dropna(subset=["ret"]).reset_index(drop=True)
rv_p = pd.Series(expanding_percentile(realized_vol(nifty["ret"].to_numpy(), 21), min_obs=252),
                 index=nifty["Date"])

for w in (21, 63):
    sig = out[w].dropna()
    sig_p = pd.Series(expanding_percentile(sig.to_numpy(), min_obs=252), index=sig.index)
    j = pd.concat([sig_p, rv_p], axis=1, keys=["c", "r"], sort=True).dropna()
    label = np.zeros(len(j))
    covered = []
    for name, s0, s1 in EPISODES:
        m = (j.index >= s0) & (j.index <= s1)
        if m.any():
            label[m] = 1
            covered.append(f"{name}({int(m.sum())}d)")
    rho, _ = stats.spearmanr(j["c"], j["r"])
    a_c, a_r = auroc(j["c"].to_numpy(), label), auroc(j["r"].to_numpy(), label)
    redundant = rho >= 0.80
    adds = a_c >= a_r + 0.03
    print(f"\nF4a-{w}d: joint days {len(j)} ({j.index.min():%Y-%m}..{j.index.max():%Y-%m}); "
          f"episodes {covered}")
    print(f"  Spearman(corr_p, rv_p) = {rho:.3f} -> {'REDUNDANT (>=0.80)' if redundant else 'not redundant'}")
    print(f"  AUROC corr {a_c:.3f} vs RV {a_r:.3f} (bar +0.03) -> "
          f"{'ADDS [caps at VERIFY-PIT]' if adds else 'does not add'}")
