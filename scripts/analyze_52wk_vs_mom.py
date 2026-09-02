"""N4a — 12-1 momentum vs 52wk-high proximity: the structure split (pre-registered).

Ledger 2026-09-02. Survivor panel, liquid half, monthly. Spearman rank correlation,
top-decile overlap, and the stress-state dependence of the correlation.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

VAULT = Path(__file__).resolve().parents[1] / "ingest" / "vault"

A = pd.read_csv(VAULT / "panel" / "n500_adjclose_2012_2022.csv.gz", index_col=0, parse_dates=True)
V = pd.read_csv(VAULT / "panel" / "n500_value_traded_2012_2022.csv.gz", index_col=0, parse_dates=True)
nif = pd.read_csv(VAULT / "index" / "nifty50_daily_2007_2026.csv", parse_dates=["Date"]).set_index("Date")["Close"].pct_change()
rv = (nif.rolling(21).std() * np.sqrt(252)).groupby(nif.index.to_period("M")).last()

month_ends = list(A.groupby(A.index.to_period("M")).apply(lambda x: x.index.max()))
rows = []
for t0 in month_ends:
    t0 = pd.Timestamp(t0)
    m12, m1 = t0 - pd.DateOffset(months=12), t0 - pd.DateOffset(months=1)
    if m12 < A.index.min() + pd.Timedelta(days=7):
        continue
    p0 = A.loc[:t0].iloc[-1]
    p12 = A.loc[:m12].iloc[-1]
    p1 = A.loc[:m1].iloc[-1]
    hi52 = A.loc[:t0].tail(252).max()
    liq = V.loc[:t0].tail(63).median()
    valid = p0.notna() & p12.notna() & p1.notna() & hi52.notna() & liq.notna()
    names = liq[valid][liq[valid] >= liq[valid].median()].index
    if len(names) < 100:
        continue
    mom = (p1[names] / p12[names] - 1.0).rank(pct=True)
    prox = (p0[names] / hi52[names]).rank(pct=True)
    rho = stats.spearmanr(mom, prox).statistic
    ov = len(set(mom[mom > 0.9].index) & set(prox[prox > 0.9].index)) / max((mom > 0.9).sum(), 1)
    rows.append({"m": t0.to_period("M"), "rho": rho, "overlap": ov})

df = pd.DataFrame(rows).set_index("m")
j = df.join(rv.rename("rv")).dropna()
hi = j["rv"] >= j["rv"].quantile(0.9)
print(f"N4a: {len(df)} months ({df.index.min()}..{df.index.max()})")
print(f"  mean Spearman rho(12-1, 52wk-high) = {df['rho'].mean():.3f} (min {df['rho'].min():.2f}, max {df['rho'].max():.2f})")
print(f"  -> VERDICT: {'REDUNDANT (rho >= 0.8)' if df['rho'].mean() >= 0.8 else 'COMPLEMENT (rho < 0.8)'}")
print(f"  mean top-decile overlap = {df['overlap'].mean():.0%}")
print(f"  stress dependence: rho in top-decile-vol months {j.loc[hi,'rho'].mean():.3f} (n={int(hi.sum())}) "
      f"vs calm {j.loc[~hi,'rho'].mean():.3f} — prior: falls in stress")
