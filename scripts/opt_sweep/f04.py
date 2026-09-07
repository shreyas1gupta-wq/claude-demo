#!/usr/bin/env python3
"""OP-D2 family F04 (researcher f04): GARCH(1,1) MLE vs EWMA 0.94, 1d-ahead QLIKE + Mar-2020 onset lag.

REGISTERED (trial-ledger Entry OP-D2, 2026-09-07, before running):
  F04 GARCH(1,1) MLE vs EWMA .94 (3 cells)
  PRIOR/BAR: statistical tie (<2% QLIKE gap); both lag Mar-2020 by >= 20 vol pts at onset.
  Cells: c1 QLIKE gap (%) GARCH vs EWMA .94 (bar |gap| < 2% = tie);
         c2 GARCH Mar-2020 onset lag (bar >= 20 vol pts);
         c3 EWMA .94 Mar-2020 onset lag (bar >= 20 vol pts).

Conventions (OP-D1 / cheat-sheet; identical to sibling F03 where shared):
  - Data: vault NIFTY 50 daily, returns = daily LOG returns of Adj Close.
  - QLIKE(f, r2) = r2/f - ln(r2/f) - 1, f = forecast VARIANCE for day t, r2 = realized
    squared return on day t; reported as MEAN over the common evaluation days; days with
    r2 == 0 dropped (QLIKE undefined; count printed).
  - NO LOOKAHEAD:
      EWMA .94: v initialized as mean of the FIRST 63 squared returns; f[t] = v_{t-1};
                v_t = 0.94 v_{t-1} + 0.06 r2[t]. Recursive, forward only (F03 protocol).
      GARCH(1,1): normal-MLE, EXPANDING window, min_obs = 750 returns; refit on the first
                trading day of each January thereafter, fitting returns <= t-1 ONLY;
                params FIXED between refits; conditional-variance recursion
                h_t = omega + alpha*r2_{t-1} + beta*h_{t-1} (h_0 = fit-window variance)
                re-run from 0 at each refit with the new params — for forecast days
                t >= refit index this uses only returns <= t-1 (no lookahead); forward only.
  - Common evaluation sample: t >= 252 AND both forecasts finite (in practice starts at the
    first GARCH fit, ~return index 750); one shared mask, dates printed.
  - Mar-2020 onset (declared here, before running): window 2020-02-15 .. 2020-03-31.
    Realized = FORWARD 5d RV per OP-D1: RV5_t = sqrt(252/5 * sum_{s=t..t+4} r_s^2) * 100
    (annualized vol points). Forecast vol_t = sqrt(252 * f[t]) * 100 (f uses data <= t-1).
    Onset lag = max over window of (RV5_t - forecast vol_t). Bar: >= 20 vol pts, each model.
"""
import sys
sys.path.insert(0, '/home/user/claude-demo')
import numpy as np
import pandas as pd
from scipy.optimize import minimize

CSV = '/home/user/claude-demo/ingest/vault/index/nifty50_daily_2007_2026.csv'
BURN = 252
EWMA_INIT_N = 63
LAM = 0.94
MIN_OBS = 750
ONSET_LO, ONSET_HI = '2020-02-15', '2020-03-31'

df = pd.read_csv(CSV, parse_dates=['Date']).sort_values('Date').reset_index(drop=True)
px = pd.to_numeric(df['Adj Close'], errors='coerce')
ok = px.notna()
px = px[ok].values
dates = pd.DatetimeIndex(df.loc[ok, 'Date'].values)
r = np.diff(np.log(px))
r2 = r * r
rdates = dates[1:]              # date of return t
n = len(r)
print(f"NIFTY daily Adj Close: {len(px)} rows {dates[0].date()}..{dates[-1].date()}; {n} returns")

# ---------------- EWMA 0.94 (F03 protocol, verbatim recursion) ----------------
f_ewma = np.full(n, np.nan)
v = float(np.mean(r2[:EWMA_INIT_N]))
for t in range(EWMA_INIT_N, n):
    f_ewma[t] = v
    v = LAM * v + (1.0 - LAM) * r2[t]

# ---------------- GARCH(1,1) normal MLE, expanding, annual refits -------------
def garch_h(params, x, h0):
    om, al, be = params
    h = np.empty(len(x))
    h[0] = h0
    for i in range(1, len(x)):
        h[i] = om + al * x[i - 1] * x[i - 1] + be * h[i - 1]
    return h

def nll(params, x, h0):
    om, al, be = params
    if om <= 0 or al < 0 or be < 0 or al + be >= 0.9995:
        return 1e10
    h = garch_h(params, x, h0)
    if np.any(h <= 0):
        return 1e10
    return 0.5 * float(np.sum(np.log(h) + x * x / h))

def fit_garch(x):
    v0 = float(np.var(x))
    starts = [(0.05, 0.90), (0.10, 0.85), (0.02, 0.95)]
    best = None
    for a0, b0 in starts:
        p0 = np.array([v0 * (1 - a0 - b0), a0, b0])
        res = minimize(nll, p0, args=(x, v0), method='L-BFGS-B',
                       bounds=[(1e-14, 1e-2), (1e-6, 0.5), (1e-6, 0.999)])
        if best is None or res.fun < best.fun:
            best = res
    return best.x

# refit indices: first index with MIN_OBS history, then first trading day of each later January
refits = [MIN_OBS]
yr_seen = {rdates[MIN_OBS].year}
for t in range(MIN_OBS + 1, n):
    y = rdates[t].year
    if y not in yr_seen and rdates[t].month == 1:
        refits.append(t)
        yr_seen.add(y)
    elif y not in yr_seen:
        yr_seen.add(y)   # year began mid-sample without a January obs (cannot happen; guard)
refits.append(n)

f_garch = np.full(n, np.nan)
last_params = None
for k in range(len(refits) - 1):
    T, Tnext = refits[k], refits[k + 1]
    params = fit_garch(r[:T])                     # returns <= T-1 only
    last_params = (rdates[T].date(), params)
    h = garch_h(params, r, float(np.var(r[:T])))  # h[t] uses r[<t] only
    f_garch[T:Tnext] = h[T:Tnext]
om, al, be = last_params[1]
print(f"GARCH refits: {len(refits)-1} (expanding, min_obs {MIN_OBS}, annual); "
      f"last refit {last_params[0]}: omega={om:.3e} alpha={al:.4f} beta={be:.4f} persistence={al+be:.4f}")

# ---------------- common QLIKE evaluation ----------------
mask = (np.arange(n) >= BURN) & np.isfinite(f_ewma) & (f_ewma > 0) & np.isfinite(f_garch) & (f_garch > 0)
zeros = int(np.sum(mask & (r2 == 0)))
mask &= (r2 > 0)
neval = int(mask.sum())
print(f"common eval days {neval} ({rdates[mask][0].date()}..{rdates[mask][-1].date()}); zero-r2 dropped {zeros}")

ql = {}
for name, f in (('garch', f_garch), ('ewma_0.94', f_ewma)):
    z = r2[mask] / f[mask]
    ql[name] = float(np.mean(z - np.log(z) - 1.0))
gap = (ql['garch'] - ql['ewma_0.94']) / ql['ewma_0.94'] * 100.0
print(f"\nmean 1d-ahead QLIKE: garch {ql['garch']:.6f}  ewma_0.94 {ql['ewma_0.94']:.6f}")
print(f"c1 QLIKE gap (garch vs ewma, + = garch worse): {gap:+.2f}%  BAR |gap| < 2% (tie)  "
      f"VERDICT: {'PASS' if abs(gap) < 2.0 else 'MISS'}")

# ---------------- Mar-2020 onset lag ----------------
rv5 = np.full(n, np.nan)
c = np.concatenate([[0.0], np.cumsum(r2)])
for t in range(n - 4):
    rv5[t] = np.sqrt(252.0 / 5.0 * (c[t + 5] - c[t])) * 100.0
win = (rdates >= ONSET_LO) & (rdates <= ONSET_HI) & np.isfinite(rv5)
print(f"\nonset window {ONSET_LO}..{ONSET_HI}: {int(win.sum())} days with fwd-5d RV; "
      f"peak RV5 {np.nanmax(rv5[win]):.1f} pts on {rdates[win][int(np.nanargmax(rv5[win]))].date()}")
for cell, name, f in (('c2', 'garch', f_garch), ('c3', 'ewma_0.94', f_ewma)):
    fv = np.sqrt(252.0 * f[win]) * 100.0
    lag = rv5[win] - fv
    i = int(np.nanargmax(lag))
    print(f"{cell} {name:10s} max onset lag {lag[i]:+.1f} vol pts on {rdates[win][i].date()} "
          f"(RV5 {rv5[win][i]:.1f} vs forecast {fv[i]:.1f})  BAR >= 20  "
          f"VERDICT: {'PASS' if lag[i] >= 20.0 else 'MISS'}")
