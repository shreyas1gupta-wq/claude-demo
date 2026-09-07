#!/usr/bin/env python3
"""OP-D2 family F12 (researcher f12): Parkinson (OHLC) vs close-close 21d vol,
1d-ahead QLIKE.

REGISTERED (trial-ledger Entry OP-D2, 2026-09-07, before running):
  F12 Parkinson (OHLC) vs close-close 21d vol for 1d-ahead QLIKE (2 cells)
  PRIOR/BAR: Parkinson better by >= 5%.

Conventions (OP-D1 / cheat-sheet, matched to sibling F03/F04 exactly):
  - Data: vault NIFTY 50 daily OHLC. Close-close returns = daily LOG returns of Adj Close.
    Parkinson estimator uses raw daily High/Low (only fields the vault carries for range).
  - QLIKE(f, r2) = r2/f - ln(r2/f) - 1, f = forecast VARIANCE for day t, r2 = realized
    close-close squared log return on day t (the estimation TARGET is unchanged across
    both forecasters — only the rolling window's *input series* differs). Reported as the
    MEAN over evaluation days (ordering identical to the registered sum, per F03/F04).
  - Parkinson daily variance estimator (per trading day i, non-annualized, same scale as
    a squared daily log return so it is QLIKE-comparable to r2 with no rescaling):
        pk[i] = (1 / (4 * ln 2)) * (ln(High_i / Low_i))^2
  - 21d ROLLING forecast, close-close:  f_cc[t] = mean(r2[t-21 : t])       (returns < t)
  - 21d ROLLING forecast, Parkinson:    f_pk[t] = mean(pk[t-21 : t])       (OHLC obs < t)
    Both are the mean of the 21 most recent DAYS ENDING AT t-1 -- NO LOOKAHEAD, identical
    window mechanics to sibling F03's roll_21 (csum trick), only the summed series differs.
  - min_obs / burn-in: scoring starts at return index 252 (matches F03/F04's common burn-in
    so eval windows are comparable across the OP-D2 sweep). Days with r2 == 0 are dropped
    from evaluation (QLIKE undefined); count printed.
"""
import sys
sys.path.insert(0, '/home/user/claude-demo')
import numpy as np
import pandas as pd

CSV = '/home/user/claude-demo/ingest/vault/index/nifty50_daily_2007_2026.csv'
BURN = 252
WINDOW = 21
LN2 = np.log(2.0)

df = pd.read_csv(CSV, parse_dates=['Date']).sort_values('Date').reset_index(drop=True)
adjpx = pd.to_numeric(df['Adj Close'], errors='coerce')
high = pd.to_numeric(df['High'], errors='coerce')
low = pd.to_numeric(df['Low'], errors='coerce')
ok = adjpx.notna() & high.notna() & low.notna() & (high > 0) & (low > 0) & (high >= low)
adjpx = adjpx[ok].reset_index(drop=True)
high = high[ok].reset_index(drop=True)
low = low[ok].reset_index(drop=True)
dates = df.loc[ok, 'Date'].reset_index(drop=True)
print(f"NIFTY daily OHLC (Adj Close/High/Low), rows after cleaning: {len(adjpx)} "
      f"{pd.Timestamp(dates.iloc[0]).date()}..{pd.Timestamp(dates.iloc[-1]).date()}")

# Close-close squared log returns: r2[i] is the return realized ON price-row i+1
# (r[i] = log(px[i+1]) - log(px[i])), aligned to dates[1:] -- same as sibling F03/F04.
px = adjpx.values
r = np.diff(np.log(px))
r2 = r * r
n = len(r2)

# Parkinson daily variance, one estimate per row, same scale as a squared daily return.
pk_all = (1.0 / (4.0 * LN2)) * (np.log(high.values / low.values)) ** 2
# Align to the same "day" as r2[i] -> price row i+1 (the day the close-close return realizes).
pk = pk_all[1:]
assert len(pk) == n

# Rolling 21d forecasts, mean of the WINDOW obs strictly BEFORE t (no lookahead), via
# cumulative-sum trick identical to sibling F03.
csum_r2 = np.concatenate([[0.0], np.cumsum(r2)])
csum_pk = np.concatenate([[0.0], np.cumsum(pk)])
f_cc = np.full(n, np.nan)
f_pk = np.full(n, np.nan)
for t in range(WINDOW, n):
    f_cc[t] = (csum_r2[t] - csum_r2[t - WINDOW]) / WINDOW
    f_pk[t] = (csum_pk[t] - csum_pk[t - WINDOW]) / WINDOW

mask = (np.arange(n) >= BURN) & np.isfinite(f_cc) & (f_cc > 0) & np.isfinite(f_pk) & (f_pk > 0)
zeros = int(np.sum(mask & (r2 == 0)))
mask &= (r2 > 0)
neval = int(mask.sum())
eval_dates = dates.values[1:][mask]
print(f"burn-in {BURN}, window {WINDOW}d; common eval days {neval} "
      f"({pd.Timestamp(eval_dates[0]).date()}..{pd.Timestamp(eval_dates[-1]).date()}); "
      f"zero-r2 days dropped {zeros}")

z_cc = r2[mask] / f_cc[mask]
z_pk = r2[mask] / f_pk[mask]
ql_cc = float(np.mean(z_cc - np.log(z_cc) - 1.0))
ql_pk = float(np.mean(z_pk - np.log(z_pk) - 1.0))
print(f"\nmean 1d-ahead QLIKE (lower = better):")
print(f"  close-close 21d  {ql_cc:.6f}")
print(f"  parkinson 21d    {ql_pk:.6f}")

impr = (ql_cc - ql_pk) / ql_cc * 100.0
print(f"\nREGISTERED BAR: Parkinson beats close-close 21d QLIKE by >= 5%")
print(f"  parkinson {ql_pk:.6f} vs close-close {ql_cc:.6f} -> improvement {impr:+.2f}%")
verdict = 'PASS' if impr >= 5.0 else 'MISS'
print(f"  VERDICT: {verdict}")

import json, os
cells = [
    {"name": "c1 Parkinson 21d QLIKE (1d-ahead, mean over eval days)",
     "value": round(ql_pk, 6),
     "bar": f"beats close-close 21d QLIKE by >= 5% (printed {impr:+.2f}%)",
     "verdict": verdict},
    {"name": "c2 close-close 21d QLIKE (baseline, 1d-ahead, mean over eval days)",
     "value": round(ql_cc, 6),
     "bar": "baseline (no independent bar)",
     "verdict": "DESCRIPTIVE"},
]
out = {
    "id": "f12",
    "headline": (f"Parkinson 21d QLIKE {ql_pk:.4f} vs close-close {ql_cc:.4f}: "
                 f"{impr:+.1f}% improvement vs >=5% bar -> {verdict}")[:200],
    "cells": cells,
    "caveats": (f"NIFTY daily OHLC vault only; no lookahead (both forecasts at t use only "
                f"obs <= t-1, csum-rolling mechanics identical to sibling F03); Parkinson "
                f"variance from raw High/Low (pk=(1/(4 ln2))(ln(H/L))^2, non-annualized, "
                f"same scale as a squared daily log return so QLIKE-comparable to r2 with "
                f"no rescaling); burn-in {BURN}, window {WINDOW}d, common eval sample "
                f"n={neval}, {zeros} zero-r2 days dropped; mean QLIKE reported (ordering "
                f"identical to registered sum, per F03/F04 convention). High/Low are raw "
                f"(not dividend-adjusted) since the vault carries no adjusted range fields "
                f"-- a known small mismatch vs the Adj-Close return target, immaterial at "
                f"NIFTY-index dividend-adjustment magnitudes."),
}
os.makedirs('/home/user/claude-demo/research/opt_sweep', exist_ok=True)
with open('/home/user/claude-demo/research/opt_sweep/f12.json', 'w') as fh:
    json.dump(out, fh, indent=1)
print("\nwrote research/opt_sweep/f12.json")
