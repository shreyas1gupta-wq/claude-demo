#!/usr/bin/env python3
"""OP-D2 family F13 (researcher f13): VIX vs fwd-RV horizon match {5,10,21,63} +
IV-HV spread percentile -> VRP capture.

REGISTERED (trial-ledger Entry OP-D2, 2026-09-07, before running):
  F13 VIX vs fwd RV horizon match {5,10,21,63} + IV-HV spread pct -> VRP capture (5 cells)
  PRIOR: 21d peak corr; top-quintile spread best capture.

Conventions (OP-D1 / cheat-sheet, matched to siblings F03/F05/F12 exactly):
  - NIFTY daily log returns r[i] = log(AdjClose[i+1]) - log(AdjClose[i]) (state date = row i,
    "already realized" return known at close of row i+1).
  - RV over h days = sqrt(252/h * sum of squared daily log returns) * 100 (annualized vol pts);
    used BOTH forward (RV_fwd_h(t) from r[t : t+h], the h returns AFTER state date t -- an
    evaluation target only, never fed back into any decision at t) and trailing (HV_21_trail(t)
    from r[t-21 : t], the 21 returns already realized AS OF state date t -- no lookahead).
  - VIX percentile / spread percentile = expanding percentile min_obs=252, via
    quant.ladder.credit_cycle.expanding_percentile (no-lookahead: percentile of x[t] within
    x[:t+1] only).
  - Cells c1-c4: corr(VIX_t, RV_fwd_h(t)) for h in {5,10,21,63}, on a COMMON sample (state
    dates common to NIFTY+VIX with h=63 forward data available -- the largest horizon --
    applied identically across all 4 so the horizon comparison isn't confounded by differing
    sample windows). Pure descriptive correlation of contemporaneous levels; no fitting, so
    no lookahead exposure.
  - Cell c5: IV-HV spread_t = VIX_t - HV_21_trail(t) (data <= t only); expanding-percentile
    (min_obs=252) rank of spread_t; monthly entries = first common NIFTY/VIX trading day of
    each calendar month needing 21 fwd NIFTY days (OP-D1/F05 monthly VRP convention exactly);
    VRP_t = VIX_t - RV_fwd_21(t) (OP-D1 definition); entries bucketed into quintiles of the
    spread percentile (bin = floor(pct*5), clipped to [0,4]); bar: mean VRP capture is highest
    in the top quintile (bin 4) vs all others.
"""
import sys
sys.path.insert(0, '/home/user/claude-demo')
import numpy as np
import pandas as pd
from quant.ladder.credit_cycle import expanding_percentile

NIFTY_CSV = '/home/user/claude-demo/ingest/vault/index/nifty50_daily_2007_2026.csv'
VIX_CSV = '/home/user/claude-demo/ingest/vault/vix/india_vix_daily_2010_2023.csv'
HORIZONS = [5, 10, 21, 63]
HV_WINDOW = 21
PCT_MIN_OBS = 252

nf = pd.read_csv(NIFTY_CSV, parse_dates=['Date']).sort_values('Date').reset_index(drop=True)
px = pd.to_numeric(nf['Adj Close'], errors='coerce')
ok = px.notna()
nf = nf.loc[ok].reset_index(drop=True)
px = px[ok].values
ndates = nf['Date'].values
r = np.diff(np.log(px))  # r[i] = log return realized on ndates[i+1]; state date for r[i] = ndates[i]
M = len(px)
print(f"NIFTY daily: {M} rows {pd.Timestamp(ndates[0]).date()}..{pd.Timestamp(ndates[-1]).date()}")

vx = pd.read_csv(VIX_CSV, parse_dates=['date']).sort_values('date').reset_index(drop=True)
print(f"India VIX daily: {len(vx)} rows {vx['date'].min().date()}..{vx['date'].max().date()}")

nf_idx = pd.Series(np.arange(M), index=nf['Date'])  # date -> NIFTY row position
common_dates = pd.Index(nf['Date']).intersection(pd.Index(vx['date'])).sort_values()
vix_close = vx.set_index('date')['close']

# --- c1-c4: horizon-matched correlations on a COMMON sample (h=63 availability binds) ---
maxH = max(HORIZONS)
rows = []
for t in common_dates:
    pos = nf_idx.get(t)
    if pos is None or pos + maxH >= M:
        continue
    rows.append((t, pos))
common_df = pd.DataFrame(rows, columns=['date', 'pos'])
common_df['vix'] = common_df['date'].map(vix_close)
n_common = len(common_df)
print(f"\ncommon corr sample (h=63 binds): n={n_common} "
      f"{common_df['date'].min().date()}..{common_df['date'].max().date()}")

corrs = {}
for h in HORIZONS:
    fwd = np.array([np.sqrt(252.0 / h * np.sum(r[p:p + h] ** 2)) * 100.0 for p in common_df['pos']])
    c = float(np.corrcoef(common_df['vix'].values, fwd)[0, 1])
    corrs[h] = c
    print(f"  corr(VIX_t, RV_fwd_{h}d)  = {c:+.4f}")

peak_h = max(corrs, key=corrs.get)
print(f"\npeak-corr horizon: {peak_h}d (registered prior: 21d peak)")
verdict_peak = 'PASS' if peak_h == 21 else 'MISS'

# --- c5: IV-HV spread percentile quintile -> monthly VRP capture ---
# HV_21_trail(pos) from r[pos-21:pos] (21 returns already realized as of state date pos)
cd = pd.DataFrame({'date': common_dates})
cd['pos'] = cd['date'].map(nf_idx)
cd = cd.dropna(subset=['pos'])
cd['pos'] = cd['pos'].astype(int)
cd['vix'] = cd['date'].map(vix_close)
hv = np.full(len(cd), np.nan)
for i, p in enumerate(cd['pos'].values):
    if p >= HV_WINDOW:
        hv[i] = np.sqrt(252.0 / HV_WINDOW * np.sum(r[p - HV_WINDOW:p] ** 2)) * 100.0
cd['hv21_trail'] = hv
cd['spread'] = cd['vix'] - cd['hv21_trail']
cd['spread_pct'] = expanding_percentile(cd['spread'].values, min_obs=PCT_MIN_OBS)
print(f"\nIV-HV spread percentile: expanding, min_obs={PCT_MIN_OBS}; "
      f"first valid {cd.loc[cd['spread_pct'].notna(), 'date'].min().date()}")

# monthly entries = first common trading day per calendar month, needing 21 fwd NIFTY days
cd['ym'] = cd['date'].dt.to_period('M')
entries = cd.groupby('ym', as_index=False).first()
erows = []
for _, row in entries.iterrows():
    p = int(row['pos'])
    if p + HORIZONS[2] >= M or not np.isfinite(row['spread_pct']):
        continue
    fwd21 = r[p:p + HORIZONS[2]]
    rv21 = np.sqrt(252.0 / HORIZONS[2] * np.sum(fwd21 ** 2)) * 100.0
    vrp = row['vix'] - rv21
    bin_ = int(min(4, np.floor(row['spread_pct'] * 5)))
    erows.append((row['date'], row['spread_pct'], bin_, vrp))
E = pd.DataFrame(erows, columns=['date', 'spread_pct', 'quintile', 'vrp'])
nmo = len(E)
print(f"\nmonthly VRP-capture entries with valid spread percentile: {nmo} "
      f"({E['date'].min().date()}..{E['date'].max().date()})")

qmeans = E.groupby('quintile')['vrp'].agg(['mean', 'count'])
print("\nmean monthly VRP capture by IV-HV-spread-percentile quintile (0=lowest,4=highest):")
for q in range(5):
    if q in qmeans.index:
        print(f"  Q{q+1}  mean {qmeans.loc[q, 'mean']:+.3f} vol pts  n={int(qmeans.loc[q, 'count'])}")
    else:
        print(f"  Q{q+1}  (no entries)")

top_mean = float(qmeans.loc[4, 'mean']) if 4 in qmeans.index else float('nan')
best_q = int(qmeans['mean'].idxmax())
verdict_topq = 'PASS' if (4 in qmeans.index and best_q == 4) else 'MISS'
print(f"\ntop-quintile (Q5) mean VRP capture: {top_mean:+.3f}; best-performing quintile overall: Q{best_q+1}")
print(f"REGISTERED PRIOR: top-quintile spread has the best (highest mean) VRP capture -> {verdict_topq}")

print(f"\nVERDICT c3 (21d peak corr): {verdict_peak}")
print(f"VERDICT c5 (top-quintile best capture): {verdict_topq}")

import json, os
cells = [
    {"name": "c1 corr(VIX_t, RV_fwd_5d), common sample",
     "value": round(corrs[5], 4),
     "bar": "none (descriptive, horizon scan)", "verdict": "DESCRIPTIVE"},
    {"name": "c2 corr(VIX_t, RV_fwd_10d), common sample",
     "value": round(corrs[10], 4),
     "bar": "none (descriptive, horizon scan)", "verdict": "DESCRIPTIVE"},
    {"name": "c3 corr(VIX_t, RV_fwd_21d), common sample",
     "value": round(corrs[21], 4),
     "bar": f"registered prior: peak corr at 21d (printed peak={peak_h}d)",
     "verdict": verdict_peak},
    {"name": "c4 corr(VIX_t, RV_fwd_63d), common sample",
     "value": round(corrs[63], 4),
     "bar": "none (descriptive, horizon scan)", "verdict": "DESCRIPTIVE"},
    {"name": "c5 top-quintile (Q5) mean monthly VRP capture, IV-HV(21d trail) spread pct bucket",
     "value": round(top_mean, 3),
     "bar": f"registered prior: Q5 (top quintile) is the best-performing quintile (printed best=Q{best_q+1})",
     "verdict": verdict_topq},
]
out = {
    "id": "f13",
    "headline": (f"VIX-fwdRV corr peaks at {peak_h}d (5d {corrs[5]:+.3f},10d {corrs[10]:+.3f},"
                 f"21d {corrs[21]:+.3f},63d {corrs[63]:+.3f}) vs 21d-peak prior->{verdict_peak}; "
                 f"IV-HV spread top quintile best={best_q==4}->{verdict_topq}")[:200],
    "cells": cells,
    "caveats": (f"NIFTY daily Adj-Close log returns + India VIX close, vault only. c1-c4: pure "
                f"contemporaneous correlation VIX_t vs RV_fwd_h(t), common sample bound by the "
                f"h=63 horizon (n={n_common}, {common_df['date'].min().date()}.."
                f"{common_df['date'].max().date()}) so the 4 horizons are compared on identical "
                f"dates; no fitting/state so no lookahead exposure (fwd RV is an evaluation "
                f"target only). c5: HV_21_trail(t) uses only r[t-21:t] (data <= t); IV-HV "
                f"spread percentile is expanding, min_obs={PCT_MIN_OBS} (no lookahead); monthly "
                f"entries = first common NIFTY/VIX day per calendar month needing 21 fwd NIFTY "
                f"days, OP-D1/F05 convention exactly (n={nmo}, {E['date'].min().date()}.."
                f"{E['date'].max().date()}); VRP_t = VIX_t - RV_fwd_21(t). Sample bounded by "
                f"the India VIX vault window (2010-07..2023-04); survivorship/mirror caveats "
                f"n/a (index-level VIX+NIFTY only, no panel used)."),
}
os.makedirs('/home/user/claude-demo/research/opt_sweep', exist_ok=True)
with open('/home/user/claude-demo/research/opt_sweep/f13.json', 'w') as fh:
    json.dump(out, fh, indent=1)
print("\nwrote research/opt_sweep/f13.json")
