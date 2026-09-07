#!/usr/bin/env python3
"""OP-D2 family F22 (researcher f22): INR 21d momentum x VRP capture (the one-axis overlay
at option frequency).

REGISTERED (trial-ledger Entry OP-D2, 2026-09-07, before running):
  F22 INR 21d momentum x VRP capture (the one-axis overlay at option frequency) (3 cells) --
  two-sided (CU coupling cited). No directional bar registered for any cell (CU-D1..D7's
  India-coupling prior -0.69/-0.79 on EQUITY returns is the motivation, not a transferred
  numeric bar for option-seller VRP capture -- a distinct outcome variable).

DATA CONSTRAINT (stated up front, drives the construction): the vaulted INR series
(ingest/vault/fx/inr_usd_monthly_1973_2026.csv) is MONTHLY -- one INR_per_USD print per
calendar month, no daily FX in the vault. A literal 21-TRADING-DAY momentum cannot be
computed from vaulted data (no daily FX series exists to sum/return over 21 sessions).
Consecutive vaulted monthly prints are ~30 calendar days apart (~21 trading days), so the
closest available proxy -- and the one used here, not invented data -- is the MONTH-OVER-
MONTH INR_per_USD change: mom_i = INR_i / INR_{i-1} - 1. This is flagged DESCRIPTIVE in the
JSON caveats: it is a monthly-frequency proxy for the registered "21d" construct, not a
literal 21-trading-day return.

NO LOOKAHEAD: the momentum used to condition month M's VRP entry is the COMPLETED PRIOR
month's change, mom_prior(M) = INR(M-1)/INR(M-2) - 1 -- computed entirely from INR prints
dated strictly before month M, then applied to the VRP outcome realized during/after month M.
No same-month INR value is used as a predictor of that month's own VRP print.

Construction (matches OP-D1/F05 / OP-D2-F20 monthly-VRP-capture conventions):
  - Monthly seller proxy P&L: 1 entry/calendar month (first common NIFTY/VIX trading day),
    VRP_t = VIX_t - RV21_fwd, RV21_fwd = sqrt(252/21 * sum sq daily log ret)*100 over
    t+1..t+21 (forward-realized outcome, computed after the entry date by construction).
  - No expanding-percentile transform is used here (unlike F13/F14/F20's VIX-pct/L2-pct
    baselines) -- INR momentum sign is a "one-axis" construct straight from the vaulted
    monthly series, so the sample is bounded only by VIX vault coverage (2010-07..2023-04),
    not by an additional percentile warm-up.
  - WEAK-INR flag = mom_prior(M) > 0 (INR_per_USD rose month-on-month = rupee depreciated).
    A sign split, not an invented percentile threshold (no magic-number grid registered for
    F22, unlike F20's already-registered L2 grid).

Three registered cells:
  1. inr_mom_vrp_corr: Pearson corr(mom_prior, VRP) over the common sample -- descriptive,
     two-sided.
  2. weak_vs_strong_inr_vrp_diff: mean VRP in weak-INR months (mom_prior>0) minus mean VRP
     in strong/flat-INR months (mom_prior<=0) -- descriptive, two-sided.
  3. inr_overlay_trim_cost: stand-down overlay (stand down -- overlay_pnl=0 -- in weak-INR
     months, sell as usual otherwise) vs the fixed (sell-always) baseline, reported as
     bottom-decile left-tail trim% and mean cost%, same metric definitions as F20's
     tail_cost() (trim_pct = shrink in |bottom-decile mean VRP|; cost_pct = give-up in mean
     VRP) -- descriptive, two-sided (reported as a single cell per the 3-cell registration;
     both numbers carried in one string value).
"""
import sys
sys.path.insert(0, '/home/user/claude-demo')
import numpy as np
import pandas as pd
from scipy import stats

NIFTY_CSV = '/home/user/claude-demo/ingest/vault/index/nifty50_daily_2007_2026.csv'
VIX_CSV = '/home/user/claude-demo/ingest/vault/vix/india_vix_daily_2010_2023.csv'
INR_CSV = '/home/user/claude-demo/ingest/vault/fx/inr_usd_monthly_1973_2026.csv'
H = 21  # RV horizon, OP-D1 convention

nf = pd.read_csv(NIFTY_CSV, parse_dates=['Date']).sort_values('Date').reset_index(drop=True)
px = pd.to_numeric(nf['Adj Close'], errors='coerce')
ok = px.notna()
nf = nf.loc[ok].reset_index(drop=True)
px = px[ok].values
ndates = nf['Date'].values
n = len(px)
print(f"NIFTY daily: {n} rows {pd.Timestamp(ndates[0]).date()}..{pd.Timestamp(ndates[-1]).date()}")

vx = pd.read_csv(VIX_CSV, parse_dates=['date']).sort_values('date').reset_index(drop=True)
print(f"India VIX daily: {len(vx)} rows {vx['date'].min().date()}..{vx['date'].max().date()}")

inr = pd.read_csv(INR_CSV, parse_dates=['Date']).sort_values('Date').reset_index(drop=True)
inr['ym'] = inr['Date'].dt.to_period('M')
inr = inr.drop_duplicates('ym', keep='last').set_index('ym')
inr['mom'] = inr['INR_per_USD'].pct_change()  # month-over-month change, monthly-freq proxy for "21d"
print(f"INR monthly: {len(inr)} rows {inr['Date'].min().date()}..{inr['Date'].max().date()} "
      f"(monthly-only vault -- 21d momentum literally unavailable, see script header)")

nf_idx = pd.Series(np.arange(len(nf)), index=nf['Date'])
common_dates = pd.Index(nf['Date']).intersection(pd.Index(vx['date'])).sort_values()
cd = pd.DataFrame({'date': common_dates})
cd['ym'] = cd['date'].dt.to_period('M')
entries = cd.groupby('ym', as_index=False).first()['date']
vx_close = vx.set_index('date')['close']

rows = []
for t in entries:
    pos = nf_idx.get(t)
    if pos is None or pos + H >= len(px):
        continue
    ym = pd.Period(t, freq='M')
    prior_ym = ym - 1
    if prior_ym not in inr.index:
        continue
    mom_prior = inr.loc[prior_ym, 'mom']
    if not np.isfinite(mom_prior):
        continue
    fwd_r = np.log(px[pos + 1: pos + H + 1]) - np.log(px[pos: pos + H])
    rv21 = np.sqrt(252.0 / H * np.sum(fwd_r ** 2)) * 100.0
    vix_t = float(vx_close.loc[t])
    vrp = vix_t - rv21
    rows.append((t, float(mom_prior), vrp))

R = pd.DataFrame(rows, columns=['date', 'mom_prior', 'vrp']).reset_index(drop=True)
n_common = len(R)
print(f"\ncommon sample (VIX-window entries with a completed-prior-month INR mom): {n_common} months "
      f"({R['date'].min().date()}..{R['date'].max().date()})")

# --- cell 1: correlation ---
r1, p1 = stats.pearsonr(R['mom_prior'].values, R['vrp'].values)
print(f"\nCELL1 inr_mom_vrp_corr: pearson r={r1:+.4f}  n={n_common}  two_sided_p={p1:.4f}")

# --- cell 2: weak vs strong/flat INR split ---
weak = R['mom_prior'].values > 0.0
n_weak, n_strong = int(weak.sum()), int((~weak).sum())
mean_weak = float(R.loc[weak, 'vrp'].mean())
mean_strong = float(R.loc[~weak, 'vrp'].mean())
diff = mean_weak - mean_strong
t2, p2 = stats.ttest_ind(R.loc[weak, 'vrp'], R.loc[~weak, 'vrp'], equal_var=False)
print(f"\nCELL2 weak_vs_strong_inr_vrp_diff: weak-INR(mom>0) n={n_weak} mean_vrp={mean_weak:+.3f}; "
      f"strong/flat-INR(mom<=0) n={n_strong} mean_vrp={mean_strong:+.3f}; diff={diff:+.3f}; "
      f"welch_t={t2:.3f} p={p2:.4f}")

# --- cell 3: stand-down overlay (weak-INR flag) vs fixed (sell-always), F20 tail_cost metric ---
fixed = R['vrp'].values
overlay = np.where(weak, 0.0, fixed)  # stand down when weak-INR flag is on
k = max(1, int(np.floor(0.10 * len(fixed))))
order = np.argsort(fixed)  # ascending: worst first
tail_idx = order[:k]
left_tail_fixed = float(np.mean(fixed[tail_idx]))
left_tail_overlay = float(np.mean(overlay[tail_idx]))
mean_fixed = float(np.mean(fixed))
mean_overlay = float(np.mean(overlay))
trim_pct = (abs(left_tail_fixed) - abs(left_tail_overlay)) / abs(left_tail_fixed) * 100.0
cost_pct = (mean_fixed - mean_overlay) / abs(mean_fixed) * 100.0
n_flagged = int(weak.sum())
print(f"\nCELL3 inr_overlay_trim_cost: k={k} bottom-decile; no-overlay mean={mean_fixed:+.3f} "
      f"bottom-decile-mean={left_tail_fixed:+.3f}; weak-INR-standdown mean={mean_overlay:+.3f} "
      f"bottom-decile-mean={left_tail_overlay:+.3f}; flagged={n_flagged}/{n_common} months; "
      f"trim_pct={trim_pct:+.2f}%  cost_pct={cost_pct:+.2f}%")

print(f"\nVERDICT inr_mom_vrp_corr: TWO-SIDED (r={r1:+.4f}, p={p1:.4f})")
print(f"VERDICT weak_vs_strong_inr_vrp_diff: TWO-SIDED (diff={diff:+.3f}, p={p2:.4f})")
print(f"VERDICT inr_overlay_trim_cost: TWO-SIDED (trim={trim_pct:+.2f}%, cost={cost_pct:+.2f}%)")
