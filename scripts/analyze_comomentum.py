"""CR-D2a — comomentum calibration on the survivor panel (pre-registered shape checks).

Ledger 2026-09-02. Lou-Polk comomentum with a documented deviation (market-adjusted weekly
returns, not FF3 residuals): monthly, within the liquid half, rank by 12-2 momentum;
comomentum(t) = mean pairwise correlation of trailing-52-week market-adjusted weekly
returns within the LOSER decile.
"""
from pathlib import Path

import numpy as np
import pandas as pd

VAULT = Path(__file__).resolve().parents[1] / "ingest" / "vault"

A = pd.read_csv(VAULT / "panel" / "n500_adjclose_2012_2022.csv.gz", index_col=0, parse_dates=True)
V = pd.read_csv(VAULT / "panel" / "n500_value_traded_2012_2022.csv.gz", index_col=0, parse_dates=True)

wk = A.resample("W-FRI").last()
wret = wk.pct_change(fill_method=None)
mkt = wret.mean(axis=1)
abn = wret.sub(mkt, axis=0)

month_ends = list(A.groupby(A.index.to_period("M")).apply(lambda x: x.index.max()))
out = []
for t0 in month_ends:
    t0 = pd.Timestamp(t0)
    m12, m1 = t0 - pd.DateOffset(months=12), t0 - pd.DateOffset(months=1)
    if m12 < A.index.min() + pd.Timedelta(days=7):
        continue
    px = A.loc[:t0]
    def at(ts):
        s = px.loc[:ts]
        return s.iloc[-1] if len(s) else None
    p0, p12, p1 = A.loc[:t0].iloc[-1], A.loc[:m12].iloc[-1], A.loc[:m1].iloc[-1]
    liq = V.loc[:t0].tail(63).median()
    valid = p0.notna() & p12.notna() & p1.notna() & liq.notna()
    liq_ok = liq[valid] >= liq[valid].median()
    names = liq_ok[liq_ok].index
    if len(names) < 100:
        continue
    mom = (p1[names] / p12[names] - 1.0)          # 12-2 momentum
    losers = mom[mom.rank(pct=True) <= 0.10].index
    W = abn.loc[abn.index <= t0].tail(52)[losers].dropna(axis=1, thresh=40)
    if W.shape[1] < 10:
        continue
    C = W.corr().values
    iu = np.triu_indices_from(C, k=1)
    out.append({"date": t0, "comom": float(np.nanmean(C[iu])), "n_losers": W.shape[1]})

s = pd.DataFrame(out).set_index("date")["comom"]
print(f"Comomentum series: {len(s)} months ({s.index.min():%Y-%m}..{s.index.max():%Y-%m}); "
      f"median {s.median():.3f}, min {s.min():.3f}, max {s.max():.3f}")
ac1 = s.autocorr(1)
print(f"P1 (slow state): lag-1 AC = {ac1:.2f} -> BAR >0.5: {'PASS' if ac1 > 0.5 else 'FAIL'}")
win = s.loc["2017-12-01":"2018-06-30"]
p2 = win.mean() > s.median()
print(f"P2 (2018 accumulation): 2017-12..2018-06 mean {win.mean():.3f} vs sample median {s.median():.3f} "
      f"-> {'PASS' if p2 else 'FAIL'}")
print(f"2020 COVID print (no bar): 2020-03..2020-06 mean {s.loc['2020-03-01':'2020-06-30'].mean():.3f}; "
      f"2020 peak {s.loc['2020'].max():.3f} in {s.loc['2020'].idxmax():%Y-%m}")
print("\nAnnual means (the monitor's path):")
print(s.groupby(s.index.year).mean().round(3).to_string())
