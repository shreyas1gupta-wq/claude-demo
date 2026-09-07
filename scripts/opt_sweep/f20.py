#!/usr/bin/env python3
"""OP-D2 family F20 (researcher f20): L2-style stress flag x VRP capture vs VIX-pct alone.

REGISTERED (trial-ledger Entry OP-D2, 2026-09-07, before running):
  F20 L2-style stress flag x VRP capture vs VIX-pct alone (3 cells) -- prior: overlay trims
  left tail >= 20% with <= 10% mean cost; two-sided.

Construction (matches OP-D1/F05 monthly-VRP-capture conventions; adds a stand-down overlay):
  - Monthly seller proxy P&L, same as F05: 1 entry/calendar month (first common NIFTY/VIX
    trading day), VRP_t = VIX_t - RV21_fwd (RV21_fwd = sqrt(252/21 * sum sq daily log ret)*100
    over t+1..t+21), fixed_pnl_t = VRP_t (sell always, size=1, the no-overlay baseline).
  - L2-STYLE STRESS FLAG (house rule #6: quant/ladder machinery, never re-implemented inline):
      rv_state  = quant.ladder.fast_stress.realized_vol(daily log returns, window=21)
      dd_state  = quant.ladder.fast_stress.drawdown_depth(daily simple returns)
      rv_pct, dd_pct = quant.ladder.credit_cycle.expanding_percentile(., min_obs=252) each
      composite = quant.ladder.fast_stress.fast_stress_composite(rv_pct, dd_pct,
                  w_rv=0.5, w_dd=0.5)  -- the module's own stated default weights; no other
                  OP-D2 registry entry overrides them, so the shipped default is used and
                  cited here, not invented for this cell.
      l2_pct = expanding_percentile(composite, min_obs=252) -- puts the composite on the
               same own-history-percentile footing as the VIX-pct baseline (apples to apples).
  - VIX-PCT BASELINE: vix_pct = expanding_percentile(VIX close, min_obs=252)
    (OP-D1 / OP-D2-F14 convention, identical call).
  - STAND-DOWN GRID: stress pctile {0.80, 0.90, 0.95} -- ALREADY REGISTERED, not invented for
    this cell (docs/cycles/02-fast-stress.md F2 de-risk grid; config/ladder.yaml L2_fast_stress
    role). Primary reported threshold = 0.90 (grid midpoint; also the threshold OP-D2/F14 used
    for spike-episode definition). Full grid printed for robustness.
  - OVERLAY RULE (both flags, applied identically): at entry date t, if pct[t] >= threshold the
    seller STANDS DOWN that month (overlay_pnl_t = 0); else overlay_pnl_t = VRP_t (sell as
    usual). NO LOOKAHEAD: pct[t] is an expanding percentile using data <= t only; VRP_t's
    forward-realized leg is the same already-realized-after-the-fact payoff convention as
    OP-D1/F05 (it is the measured outcome/label, not an input to the flag).
  - LEFT TAIL = mean of the bottom decile (worst 10%, by count, rounded down, floor 1) of
    monthly fixed_pnl prints -- more robust than a single worst month (deliberately a
    different metric from F05's single worst-month cell, since "trims left tail" in the
    F20 registration reads as a tail-mass claim, not a single-print claim).
      trim_pct = (|left_tail_fixed| - |left_tail_overlay|) / |left_tail_fixed| * 100
      cost_pct = (mean_fixed - mean_overlay) / |mean_fixed| * 100
  - COMMON COMPARISON SAMPLE: entries where BOTH l2_pct and vix_pct are warmed up (VIX-pct
    warms up later -- min_obs=252 trading days after the 2010-07 VIX start, ~2011-07) so the
    L2-style and VIX-pct-alone overlays are scored on the IDENTICAL set of months and against
    the IDENTICAL fixed-pnl baseline (recomputed on that common sample).
"""
import sys
sys.path.insert(0, '/home/user/claude-demo')
import numpy as np
import pandas as pd
from quant.ladder.fast_stress import realized_vol, drawdown_depth, fast_stress_composite
from quant.ladder.credit_cycle import expanding_percentile

NIFTY_CSV = '/home/user/claude-demo/ingest/vault/index/nifty50_daily_2007_2026.csv'
VIX_CSV = '/home/user/claude-demo/ingest/vault/vix/india_vix_daily_2010_2023.csv'
H = 21                       # RV horizon, OP-D1 convention
MIN_OBS = 252                # OP-D1/F14 expanding-percentile warm-up
GRID = [0.80, 0.90, 0.95]    # already-registered L2 de-risk grid (02-fast-stress.md F2)
PRIMARY = 0.90

nf = pd.read_csv(NIFTY_CSV, parse_dates=['Date']).sort_values('Date').reset_index(drop=True)
px = pd.to_numeric(nf['Adj Close'], errors='coerce')
ok = px.notna()
nf = nf.loc[ok].reset_index(drop=True)
px = px[ok].values
ndates = nf['Date'].values
logret = np.diff(np.log(px))              # logret[i] -> ndates[i+1]
simret = px[1:] / px[:-1] - 1.0            # simret[i] -> ndates[i+1]
n = len(logret)
print(f"NIFTY daily: {len(px)} rows {pd.Timestamp(ndates[0]).date()}..{pd.Timestamp(ndates[-1]).date()}; {n} returns")

# --- L2-style stress composite (quant/ladder machinery only) ---
rv_state = realized_vol(logret, window=H)             # unscaled vol level; percentile-invariant to *100
dd_state = drawdown_depth(simret)
rv_pct = expanding_percentile(rv_state, min_obs=MIN_OBS)
dd_pct = expanding_percentile(dd_state, min_obs=MIN_OBS)
composite = fast_stress_composite(rv_pct, dd_pct, w_rv=0.5, w_dd=0.5)
l2_pct = expanding_percentile(composite, min_obs=MIN_OBS)
state_date = pd.Series(ndates[1:])
state = pd.DataFrame({'date': state_date, 'l2_pct': l2_pct}).set_index('date')
print(f"L2-style composite warm-up ends {pd.Timestamp(ndates[MIN_OBS]).date()} (pre-VIX; fast_stress_composite w_rv=w_dd=0.5, module default)")

vx = pd.read_csv(VIX_CSV, parse_dates=['date']).sort_values('date').reset_index(drop=True)
vix_pct_arr = expanding_percentile(vx['close'].values, min_obs=MIN_OBS)
vx = vx.assign(vix_pct=vix_pct_arr).set_index('date')
print(f"India VIX daily: {len(vx)} rows {vx.index.min().date()}..{vx.index.max().date()}; vix_pct warm-up ends {vx.index[MIN_OBS-1].date()}")

nf_idx = pd.Series(np.arange(len(nf)), index=nf['Date'])
common_dates = pd.Index(nf['Date']).intersection(pd.Index(vx.index)).sort_values()
cd = pd.DataFrame({'date': common_dates})
cd['ym'] = cd['date'].dt.to_period('M')
entries = cd.groupby('ym', as_index=False).first()['date']

rows = []
for t in entries:
    pos = nf_idx.get(t)
    if pos is None or pos + H >= len(px):
        continue
    if t not in state.index or not np.isfinite(state.loc[t, 'l2_pct']):
        continue
    fwd_r = np.log(px[pos + 1: pos + H + 1]) - np.log(px[pos: pos + H])
    rv21 = np.sqrt(252.0 / H * np.sum(fwd_r ** 2)) * 100.0
    vix_t = float(vx.loc[t, 'close'])
    vpct = vx.loc[t, 'vix_pct']
    vrp = vix_t - rv21
    rows.append((t, vix_t, float(vpct) if np.isfinite(vpct) else np.nan, float(state.loc[t, 'l2_pct']), vrp))

R = pd.DataFrame(rows, columns=['date', 'vix', 'vix_pct', 'l2_pct', 'vrp'])
print(f"\nusable monthly entries (L2-pct warmed up): {len(R)} ({R['date'].min().date()}..{R['date'].max().date()})")

# common sample: both percentiles warmed up (VIX-pct is the later-warming one)
C = R.dropna(subset=['vix_pct']).reset_index(drop=True)
print(f"common comparison sample (both l2_pct and vix_pct warmed up): {len(C)} months "
      f"({C['date'].min().date()}..{C['date'].max().date()})")


def tail_cost(df, pct_col, thresh):
    fixed = df['vrp'].values
    overlay = np.where(df[pct_col].values >= thresh, 0.0, fixed)
    k = max(1, int(np.floor(0.10 * len(fixed))))
    order = np.argsort(fixed)  # ascending: worst first
    tail_idx = order[:k]
    left_tail_fixed = float(np.mean(fixed[tail_idx]))
    left_tail_overlay = float(np.mean(overlay[tail_idx]))
    mean_fixed = float(np.mean(fixed))
    mean_overlay = float(np.mean(overlay))
    trim_pct = (abs(left_tail_fixed) - abs(left_tail_overlay)) / abs(left_tail_fixed) * 100.0
    cost_pct = (mean_fixed - mean_overlay) / abs(mean_fixed) * 100.0
    return dict(k=k, left_tail_fixed=left_tail_fixed, left_tail_overlay=left_tail_overlay,
                mean_fixed=mean_fixed, mean_overlay=mean_overlay,
                trim_pct=trim_pct, cost_pct=cost_pct,
                n_flagged=int(np.sum(df[pct_col].values >= thresh)))


print(f"\n--- grid sensitivity (common sample, n={len(C)}) ---")
for g in GRID:
    l2r = tail_cost(C, 'l2_pct', g)
    vxr = tail_cost(C, 'vix_pct', g)
    print(f"pct>={g:.2f}: L2-style  trim={l2r['trim_pct']:+7.2f}% cost={l2r['cost_pct']:+7.2f}% "
          f"flagged={l2r['n_flagged']:3d}mo  |  VIX-pct  trim={vxr['trim_pct']:+7.2f}% "
          f"cost={vxr['cost_pct']:+7.2f}% flagged={vxr['n_flagged']:3d}mo")

l2_primary = tail_cost(C, 'l2_pct', PRIMARY)
vx_primary = tail_cost(C, 'vix_pct', PRIMARY)

print(f"\n=== PRIMARY (pct >= {PRIMARY}) ===")
print(f"no-overlay (sell always): mean {l2_primary['mean_fixed']:+.3f} vol pts, "
      f"bottom-decile(k={l2_primary['k']}) mean {l2_primary['left_tail_fixed']:+.3f}")
print(f"L2-style overlay:  mean {l2_primary['mean_overlay']:+.3f}, "
      f"bottom-decile mean {l2_primary['left_tail_overlay']:+.3f}, "
      f"flagged {l2_primary['n_flagged']}/{len(C)} months")
print(f"VIX-pct overlay:   mean {vx_primary['mean_overlay']:+.3f}, "
      f"bottom-decile mean {vx_primary['left_tail_overlay']:+.3f}, "
      f"flagged {vx_primary['n_flagged']}/{len(C)} months")

trim_pct = l2_primary['trim_pct']
cost_pct = l2_primary['cost_pct']
edge_pp = l2_primary['trim_pct'] - vx_primary['trim_pct']
cost_edge_pp = l2_primary['cost_pct'] - vx_primary['cost_pct']

print(f"\nCELL1 l2_style_left_tail_trim_pct = {trim_pct:+.2f}%  (BAR: >= 20%)")
print(f"CELL2 l2_style_mean_cost_pct      = {cost_pct:+.2f}%  (BAR: <= 10%)")
print(f"CELL3 l2_vs_vixpct_trim_edge_pp   = {edge_pp:+.2f}pp  "
      f"(L2-style trim {l2_primary['trim_pct']:+.2f}% vs VIX-pct trim {vx_primary['trim_pct']:+.2f}%; "
      f"cost edge {cost_edge_pp:+.2f}pp -- L2-style cost {l2_primary['cost_pct']:+.2f}% vs "
      f"VIX-pct cost {vx_primary['cost_pct']:+.2f}%)")

v1 = 'PASS' if trim_pct >= 20.0 else 'MISS'
v2 = 'PASS' if cost_pct <= 10.0 else 'MISS'
v3 = 'TWO-SIDED'
print(f"\nVERDICT l2_style_left_tail_trim_pct: {v1}")
print(f"VERDICT l2_style_mean_cost_pct: {v2}")
print(f"VERDICT l2_vs_vixpct_trim_edge_pp: {v3} (edge {'favors L2-style' if edge_pp > 0 else 'favors VIX-pct alone' if edge_pp < 0 else 'ties'})")
