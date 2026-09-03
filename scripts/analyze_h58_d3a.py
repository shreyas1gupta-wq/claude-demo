"""H58-D3a — expiry-day noise (index partial), run exactly as registered (2026-09-03).

Monthly expiry = last trading Thursday of each month, holiday-shifted to the preceding
trading day. Control = all other trading Thursdays. Descriptive only (parent: no alpha
claim); two-sided MW p reported, nothing graded.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]

df = pd.read_csv(ROOT / "ingest/vault/index/nifty50_daily_2007_2026.csv",
                 parse_dates=["Date"]).sort_values("Date").reset_index(drop=True)
df["ret"] = df["Close"].pct_change()
df = df.dropna(subset=["ret"]).reset_index(drop=True)
tdays = set(df["Date"])

# last trading Thursday per month, holiday-shifted back
expiry = set()
for ym, g in df.groupby(df["Date"].dt.to_period("M")):
    thursdays = pd.date_range(ym.start_time, ym.end_time, freq="W-THU")
    if len(thursdays) == 0:
        continue
    last_thu = thursdays[-1]
    d = last_thu
    while d not in tdays and d >= ym.start_time:
        d -= pd.Timedelta(days=1)
    if d in tdays:
        expiry.add(d)

df["is_exp"] = df["Date"].isin(expiry)
df["is_thu"] = df["Date"].dt.weekday == 3
absr = df["ret"].abs()

def report(sub, tag):
    e = absr[sub & df.is_exp]
    o = absr[sub & df.is_thu & ~df.is_exp]
    u, p = stats.mannwhitneyu(e, o, alternative="two-sided")
    print(f"{tag}: expiry days n={len(e)} median |ret| {e.median()*100:.3f}% vs "
          f"other Thursdays n={len(o)} median {o.median()*100:.3f}% | two-sided MW p={p:.3f}")

print(f"sample {df.Date.min():%Y-%m-%d}..{df.Date.max():%Y-%m-%d}; "
      f"monthly expiry days identified: {int(df.is_exp.sum())}")
report(pd.Series(True, index=df.index), "FULL SAMPLE")
report(df.Date < "2019-01-01", "PRE-2019 (monthly-expiry era)")
report(df.Date >= "2019-01-01", "2019+ (weekly-expiry era)")
