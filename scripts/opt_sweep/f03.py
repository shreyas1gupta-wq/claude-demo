#!/usr/bin/env python3
"""OP-D2 family F03 (researcher f03): EWMA lambda grid vs rolling windows, 1d-ahead QLIKE.

REGISTERED (trial-ledger Entry OP-D2, 2026-09-07, before running):
  F03 EWMA lambda {0.90, 0.94, 0.97} vs rolling {10, 21, 63} 1d-ahead vol QLIKE (6 cells)
  PRIOR/BAR: EWMA .94 beats rolling-21 by >= 3% QLIKE.

Conventions (OP-D1 / cheat-sheet):
  - Data: vault NIFTY 50 daily, returns = daily LOG returns of Adj Close.
  - QLIKE(f, r2) = r2/f - ln(r2/f) - 1, f = forecast VARIANCE for day t, r2 = realized
    squared return on day t; reported as the MEAN over evaluation days (sum/n; ordering
    identical to the registered sum since all forecasters share one evaluation sample).
  - NO LOOKAHEAD: forecast f[t] for day t uses returns <= t-1 only.
      EWMA:    v initialized as mean of the FIRST 63 squared returns (data <= obs 62);
               f[t] = v_{t-1}; v_t = lam*v_{t-1} + (1-lam)*r2[t]. Recursive, forward only.
      Rolling: f[t] = mean(r2[t-w : t]) (the w squared returns ENDING at t-1).
  - min_obs / burn-in: scoring starts at return index 252 (>= every window and past the
    EWMA init block), one common evaluation sample for all six forecasters.
  - Days with r2 == 0 are dropped from evaluation (QLIKE undefined); count printed.
"""
import sys
sys.path.insert(0, '/home/user/claude-demo')
import numpy as np
import pandas as pd

CSV = '/home/user/claude-demo/ingest/vault/index/nifty50_daily_2007_2026.csv'
BURN = 252
LAMBDAS = (0.90, 0.94, 0.97)
WINDOWS = (10, 21, 63)
EWMA_INIT_N = 63

df = pd.read_csv(CSV, parse_dates=['Date']).sort_values('Date').reset_index(drop=True)
px = pd.to_numeric(df['Adj Close'], errors='coerce')
ok = px.notna()
px = px[ok].values
dates = df.loc[ok, 'Date'].values
r = np.diff(np.log(px))
r2 = r * r
n = len(r)
print(f"NIFTY daily Adj Close: {len(px)} rows {pd.Timestamp(dates[0]).date()}..{pd.Timestamp(dates[-1]).date()}; {n} returns")

fore = {}
for lam in LAMBDAS:
    f = np.full(n, np.nan)
    v = float(np.mean(r2[:EWMA_INIT_N]))          # data <= obs 62 only
    for t in range(EWMA_INIT_N, n):
        f[t] = v                                   # forecast for day t: state after t-1
        v = lam * v + (1.0 - lam) * r2[t]          # update AFTER forecasting
    fore[f'ewma_{lam:.2f}'] = f
csum = np.concatenate([[0.0], np.cumsum(r2)])
for w in WINDOWS:
    f = np.full(n, np.nan)
    for t in range(w, n):
        f[t] = (csum[t] - csum[t - w]) / w         # mean of r2[t-w .. t-1]
    fore[f'roll_{w}'] = f

names = list(fore)
mask = np.arange(n) >= BURN
for f in fore.values():
    mask &= np.isfinite(f) & (f > 0)
zeros = int(np.sum(mask & (r2 == 0)))
mask &= (r2 > 0)
neval = int(mask.sum())
print(f"burn-in {BURN}; common eval days {neval} ({pd.Timestamp(dates[1:][mask][0]).date()}..{pd.Timestamp(dates[1:][mask][-1]).date()}); zero-r2 days dropped {zeros}")

ql = {}
for name in names:
    z = r2[mask] / fore[name][mask]
    ql[name] = float(np.mean(z - np.log(z) - 1.0))
print("\nmean 1d-ahead QLIKE (lower = better):")
for name in names:
    print(f"  {name:10s} {ql[name]:.6f}")
best = min(ql, key=ql.get)
print(f"grid best: {best} ({ql[best]:.6f})")

impr = (ql['roll_21'] - ql['ewma_0.94']) / ql['roll_21'] * 100.0
print(f"\nREGISTERED BAR: EWMA .94 beats rolling-21 by >= 3% QLIKE")
print(f"  ewma_0.94 {ql['ewma_0.94']:.6f} vs roll_21 {ql['roll_21']:.6f} -> improvement {impr:+.2f}%")
verdict = 'PASS' if impr >= 3.0 else 'MISS'
print(f"  VERDICT: {verdict}")

import json, os
cells = []
for name in names:
    if name == 'ewma_0.94':
        cells.append({"name": "ewma_0.94_qlike", "value": round(ql[name], 6),
                      "bar": f"beats roll_21 by >= 3% QLIKE (printed {impr:+.2f}%)",
                      "verdict": verdict})
    else:
        cells.append({"name": f"{name}_qlike", "value": round(ql[name], 6),
                      "bar": "grid read (no registered bar)", "verdict": "DESCRIPTIVE"})
out = {
    "id": "f03",
    "headline": (f"EWMA .94 QLIKE {ql['ewma_0.94']:.4f} vs roll-21 {ql['roll_21']:.4f}: "
                 f"{impr:+.1f}% improvement vs >=3% bar -> {verdict}; grid best {best} "
                 f"({ql[best]:.4f})")[:200],
    "cells": cells,
    "caveats": f"NIFTY daily log returns, vault only; no lookahead (forecast t uses <= t-1); "
               f"burn-in 252, common eval sample n={neval}, {zeros} zero-r2 days dropped; "
               f"mean QLIKE reported (ordering identical to registered sum).",
}
os.makedirs('/home/user/claude-demo/research/opt_sweep', exist_ok=True)
with open('/home/user/claude-demo/research/opt_sweep/f03.json', 'w') as fh:
    json.dump(out, fh, indent=1)
print("\nwrote research/opt_sweep/f03.json")
