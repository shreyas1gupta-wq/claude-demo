#!/usr/bin/env python3
"""OP-D2 family F05 (researcher f05): vol-target sizing of the OP-D1 monthly VRP capture
(target/EWMA, cap 2x) vs fixed sizing.

REGISTERED (trial-ledger Entry OP-D2, 2026-09-07, before running):
  F05 vol-target sizing of the OP-D1 monthly VRP capture (target/EWMA, cap 2x) vs fixed
  (3 cells) — BAR: worst-month improves >= 30% at <= 20% mean cost.

Conventions (OP-D1 / cheat-sheet, matched exactly):
  - NIFTY daily log returns from Adj Close (vault: ingest/vault/index/nifty50_daily_2007_2026.csv).
  - RV over h=21 days = sqrt(252/21 * sum of squared daily log returns over the window) * 100
    (annualized vol points).
  - VRP_t = VIX_t - RV_{t+1..t+21}; monthly seller proxy P&L = VRP_t.
  - Monthly sampling: ONE entry per calendar month = the first common NIFTY/VIX trading day
    of that month (non-overlapping monthly VRP capture, matching the "monthly" cadence of
    OP-D1/F16). Entry month m needs the next 21 NIFTY trading days after entry to exist
    (else dropped, e.g. the final partial month).
  - NO LOOKAHEAD, state at entry date t uses only data <= t:
      Sizing signal = EWMA realized vol (lambda=0.94, the OP-D2/F03-registered EWMA choice),
      recursive on squared daily NIFTY log returns, v_0 = mean of first 63 sq. returns
      (min_obs=63 trading days, ~1 quarter warm-up, entirely pre-VIX i.e. pre-2010-07 so it
      never touches an evaluation month), vol_pts[t] = sqrt(252*v_t)*100, v updated AFTER
      each day using only that day's own (already-realized, close-of-day) return.
      Target vol_t = EXPANDING mean of vol_pts over all days <= t since warm-up ends (a
      no-magic-number target: the sample's own history, not a picked level).
      size_t = min(target_t / vol_pts[t], 2.0)   (cap 2x; no floor -- ratio of two positive
      vol levels is always > 0, so sizing shrinks smoothly in high-vol regimes).
  - fixed_pnl_t      = VRP_t                 (size == 1 always)
  - voltarget_pnl_t  = size_t * VRP_t
  - worst-month improvement % = (|worst_fixed| - |worst_voltarget|) / |worst_fixed| * 100
    (positive = vol-targeting shrinks the worst monthly loss)
  - mean cost %      = (mean_fixed - mean_voltarget) / |mean_fixed| * 100
    (positive = vol-targeting gives up average monthly VRP income)
  - Data window is bounded by India VIX vault (2010-07..2023-04); usable entry months need
    21 NIFTY trading days of forward RV, so the last few months are dropped.
"""
import sys
sys.path.insert(0, '/home/user/claude-demo')
import numpy as np
import pandas as pd

NIFTY_CSV = '/home/user/claude-demo/ingest/vault/index/nifty50_daily_2007_2026.csv'
VIX_CSV = '/home/user/claude-demo/ingest/vault/vix/india_vix_daily_2010_2023.csv'
LAMBDA = 0.94          # OP-D2/F03-registered EWMA choice
EWMA_INIT_N = 63       # ~1 quarter warm-up, entirely pre-2010 (pre-VIX)
H = 21                 # RV horizon, OP-D1 convention
CAP = 2.0

nf = pd.read_csv(NIFTY_CSV, parse_dates=['Date']).sort_values('Date').reset_index(drop=True)
px = pd.to_numeric(nf['Adj Close'], errors='coerce')
ok = px.notna()
nf = nf.loc[ok].reset_index(drop=True)
px = px[ok].values
ndates = nf['Date'].values
r = np.diff(np.log(px))          # r[i] = log return on ndates[i+1]
r2 = r * r
n = len(r)
print(f"NIFTY daily: {len(px)} rows {pd.Timestamp(ndates[0]).date()}..{pd.Timestamp(ndates[-1]).date()}; {n} log returns")

# --- EWMA sizing signal, computed on the return series (index i -> date ndates[i+1]) ---
vol_pts = np.full(n, np.nan)
v = float(np.mean(r2[:EWMA_INIT_N]))
for t in range(EWMA_INIT_N, n):
    v = LAMBDA * v + (1.0 - LAMBDA) * r2[t]   # update with day t's own (already realized) return
    vol_pts[t] = np.sqrt(252.0 * v) * 100.0    # state AFTER day t, usable for sizing at t (data <= t)
# expanding target = running mean of vol_pts since warm-up ended (no-lookahead, no magic number)
target = np.full(n, np.nan)
csum, cnt = 0.0, 0
for t in range(EWMA_INIT_N, n):
    csum += vol_pts[t]; cnt += 1
    target[t] = csum / cnt
sizing_date = pd.Series(ndates[1:])          # date for r[t]/vol_pts[t]/target[t]
sizing = pd.DataFrame({'date': sizing_date, 'vol_pts': vol_pts, 'target': target})
print(f"EWMA lambda={LAMBDA}, init_n={EWMA_INIT_N} (warm-up ends {pd.Timestamp(ndates[EWMA_INIT_N]).date()}, pre-VIX)")

vx = pd.read_csv(VIX_CSV, parse_dates=['date']).sort_values('date').reset_index(drop=True)
print(f"India VIX daily: {len(vx)} rows {vx['date'].min().date()}..{vx['date'].max().date()}")

nf_idx = pd.Series(np.arange(len(nf)), index=nf['Date'])  # date -> row position in nf/px
common_dates = pd.Index(nf['Date']).intersection(pd.Index(vx['date'])).sort_values()

# monthly entry = first common trading day of each calendar month
cd = pd.DataFrame({'date': common_dates})
cd['ym'] = cd['date'].dt.to_period('M')
entries = cd.groupby('ym', as_index=False).first()['date']

vx_close = vx.set_index('date')['close']
sizing_close = sizing.set_index('date')

rows = []
for t in entries:
    pos = nf_idx.get(t)
    if pos is None or pos + H >= len(px):
        continue  # not enough forward NIFTY days for RV_21 -> drop (final partial month)
    if t not in sizing_close.index or not np.isfinite(sizing_close.loc[t, 'vol_pts']) or not np.isfinite(sizing_close.loc[t, 'target']):
        continue  # sizing signal not yet warmed up at this date
    fwd_r = np.log(px[pos + 1: pos + H + 1]) - np.log(px[pos: pos + H])
    rv21 = np.sqrt(252.0 / H * np.sum(fwd_r ** 2)) * 100.0
    vix_t = float(vx_close.loc[t])
    vrp = vix_t - rv21
    vp = float(sizing_close.loc[t, 'vol_pts'])
    tg = float(sizing_close.loc[t, 'target'])
    size = min(tg / vp, CAP)
    rows.append((t, vix_t, rv21, vrp, vp, tg, size))

R = pd.DataFrame(rows, columns=['date', 'vix', 'rv21', 'vrp', 'vol_pts', 'target', 'size'])
R['fixed_pnl'] = R['vrp']
R['vt_pnl'] = R['size'] * R['vrp']
nmo = len(R)
ncap = int((R['size'] >= CAP - 1e-9).sum())
print(f"\nusable monthly entries: {nmo} ({R['date'].min().date()}..{R['date'].max().date()}); "
      f"months at the {CAP}x cap: {ncap}")

worst_fixed = float(R['fixed_pnl'].min())
worst_vt = float(R.loc[R['fixed_pnl'].idxmin(), 'vt_pnl'])  # same calendar month, vol-target P&L
worst_vt_own = float(R['vt_pnl'].min())  # the vol-target series' own worst month (may differ)
mean_fixed = float(R['fixed_pnl'].mean())
mean_vt = float(R['vt_pnl'].mean())

worst_month_improvement_pct = (abs(worst_fixed) - abs(worst_vt_own)) / abs(worst_fixed) * 100.0
mean_cost_pct = (mean_fixed - mean_vt) / abs(mean_fixed) * 100.0

print(f"\nfixed-size (1x) monthly VRP capture: mean {mean_fixed:+.3f} vol pts, worst month {worst_fixed:+.3f}")
print(f"vol-target (target/EWMA, cap {CAP}x): mean {mean_vt:+.3f} vol pts, worst month {worst_vt_own:+.3f}")
print(f"\nworst-month improvement: {worst_month_improvement_pct:+.2f}%  (BAR: >= 30%)")
print(f"mean cost: {mean_cost_pct:+.2f}%  (BAR: <= 20%)")

v1 = 'PASS' if worst_month_improvement_pct >= 30.0 else 'MISS'
v2 = 'PASS' if mean_cost_pct <= 20.0 else 'MISS'
v3 = 'PASS' if (v1 == 'PASS' and v2 == 'PASS') else 'MISS'
print(f"\nVERDICT worst_month_improvement: {v1}")
print(f"VERDICT mean_cost: {v2}")
print(f"VERDICT combined (registered BAR, both conditions): {v3}")
