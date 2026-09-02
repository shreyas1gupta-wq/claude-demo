"""MR1-S — the survivor-panel reversal preliminary (pre-registered, one-way).

Ledger 2026-09-02. Data: vaulted NIFTY500 survivor panel (2012-2021). Monthly 1-month-
return deciles within the liquid half; long D1 / short D10; costs 28bps per side on actual
turnover (config/costs.yaml cash_delivery grid midpoint). One-way rule: can corroborate the
L1 freeze, can never unfreeze (survivorship upper bound).
"""
from pathlib import Path

import numpy as np
import pandas as pd

VAULT = Path(__file__).resolve().parents[1] / "ingest" / "vault"
COST_PER_SIDE = 0.0028  # 28bps: cash_delivery all-in per-side grid [24,32] midpoint

A = pd.read_csv(VAULT / "panel" / "n500_adjclose_2012_2022.csv.gz", index_col=0, parse_dates=True)
V = pd.read_csv(VAULT / "panel" / "n500_value_traded_2012_2022.csv.gz", index_col=0, parse_dates=True)

month_ends = A.groupby(A.index.to_period("M")).apply(lambda x: x.index.max())
me = list(month_ends)
rows = []
prev_long, prev_short = set(), set()
for k in range(3, len(me) - 1):  # need trailing 63d liquidity + 1m signal; hold to next ME
    t0, t1 = me[k], me[k + 1]
    sig_start = me[k - 1]
    liq = V.loc[:t0].tail(63).median()
    px_t0, px_sig = A.loc[t0], A.loc[sig_start]
    valid = px_t0.notna() & px_sig.notna() & liq.notna()
    liq_ok = liq[valid] >= liq[valid].median()
    names = liq_ok[liq_ok].index
    if len(names) < 100:
        continue
    sig = (px_t0[names] / px_sig[names] - 1.0)
    q = sig.rank(pct=True)
    longs = set(q[q <= 0.10].index)
    shorts = set(q[q > 0.90].index)
    fwd = (A.loc[t1] / A.loc[t0] - 1.0)
    lr = fwd[list(longs)].dropna().mean()
    sr = fwd[list(shorts)].dropna().mean()
    gross = lr - sr
    to_l = 1.0 if not prev_long else 1.0 - len(longs & prev_long) / max(len(longs), 1)
    to_s = 1.0 if not prev_short else 1.0 - len(shorts & prev_short) / max(len(shorts), 1)
    # each side: turnover fraction replaced => sell+buy = 2 trades on that fraction
    cost = COST_PER_SIDE * 2 * (to_l + to_s) / 2 * 2  # avg turnover x 2 sides x 2 trades
    rows.append({"date": t1, "gross": gross, "net": gross - cost,
                 "to": (to_l + to_s) / 2, "n": len(names)})
    prev_long, prev_short = longs, shorts

df = pd.DataFrame(rows).set_index("date")
print(f"Months: {len(df)} ({df.index.min():%Y-%m}..{df.index.max():%Y-%m}); "
      f"median universe {int(df['n'].median())}; median monthly one-side turnover {df['to'].median():.0%}")
print(f"GROSS L-S: mean {df['gross'].mean()*100:+.2f}%/mo, median {df['gross'].median()*100:+.2f}%/mo, "
      f"t={df['gross'].mean()/df['gross'].std()*np.sqrt(len(df)):.2f}")
print(f"NET L-S:   mean {df['net'].mean()*100:+.2f}%/mo (cost drag {100*(df['gross']-df['net']).mean():.2f}%/mo)")
h1 = df.loc[:"2016-12-31", "net"]
h2 = df.loc["2017-01-01":, "net"]
print(f"Half 1 (2012-2016): net mean {h1.mean()*100:+.2f}%/mo (n={len(h1)})")
print(f"Half 2 (2017-2021): net mean {h2.mean()*100:+.2f}%/mo (n={len(h2)})")
corroborated = (h1.mean() <= 0) or (h2.mean() <= 0)
print("MR1-S one-way verdict:",
      "FREEZE CORROBORATED (net <= 0 in a half-sample)" if corroborated
      else "upper-bound-positive in both halves — freeze UNCHANGED (one-way rule)")

# Nagel-style stress conditionality (measurement, no bar)
nif = pd.read_csv(VAULT / "index" / "nifty50_daily_2007_2026.csv", parse_dates=["Date"]).set_index("Date")["Close"].pct_change()
rv = nif.rolling(21).std() * np.sqrt(252)
rv_m = rv.groupby(rv.index.to_period("M")).last()
g = df["gross"].copy()
g.index = g.index.to_period("M")
join = pd.concat([g, rv_m.rename("rv")], axis=1, join="inner").dropna()
hi = join["rv"] >= join["rv"].quantile(0.9)
print(f"Stress conditionality (gross): top-decile-vol months mean {join.loc[hi,'gross'].mean()*100:+.2f}%/mo "
      f"vs other months {join.loc[~hi,'gross'].mean()*100:+.2f}%/mo [measurement]")
