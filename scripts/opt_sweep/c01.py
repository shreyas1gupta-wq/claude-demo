#!/usr/bin/env python3
"""OP-D2 combiner C01: entry-state stack VIX-pct x IV-HV spread (F13) x 200d-MA trend (F06)
-> monthly VRP capture, vs each single filter alone.

NOT pre-registered with a numeric bar (Entry OP-D2's combiner cells are "booked at
completion", descriptive/two-sided, feeds H60-VRP design brief only, no promotion) --
this script reports the stack vs singles descriptively and lets the numbers answer
"does stacking add anything over VIX-pct alone".

Reuses ONLY already-registered constructions/thresholds from this OP-D2 batch -- no new
magic numbers:
  - monthly VRP capture convention: OP-D1/F05/F13 (first common NIFTY/VIX trading day per
    calendar month, needing 21 fwd NIFTY days; VRP_t = VIX_t - RV_fwd_21(t)).
  - VIX-pct / IV-HV spread-pct: expanding_percentile (quant.ladder.credit_cycle), min_obs=252
    (F01/F06/F11/F13 convention). "High" = top quintile, pct>=0.8 (F06's Q5 corner, F13's
    c5 top-quintile bin -- both already-registered quintile cuts, not invented here).
  - trend: 200d trailing MA (F06 convention, MIN_OBS_MA=200), state = px_t > ma200_t.

KNOWN BUG FIXED (not repeated here): F13's combiner-audit found cd.groupby('ym').first()
silently frankensteins rows (per-column first-non-null, not first-row) at the warmup
boundary month. Here entries are built with sort_values('date') + drop_duplicates('ym',
keep='first'), which is provably row-wise-correct (whole row from the true first date).

NO LOOKAHEAD: MA200 trailing (px[t-199:t+1]); vix_pct/spread_pct expanding rank of x[t]
within x[:t+1] only; HV21_trail(t) from r[t-21:t]; VRP's RV_fwd_21 is the forward
EVALUATION target only (never fed into any state/filter). Vault only, prints only.
"""
import sys
sys.path.insert(0, '/home/user/claude-demo')
import numpy as np
import pandas as pd
from quant.ladder.credit_cycle import expanding_percentile

NIFTY_CSV = '/home/user/claude-demo/ingest/vault/index/nifty50_daily_2007_2026.csv'
VIX_CSV = '/home/user/claude-demo/ingest/vault/vix/india_vix_daily_2010_2023.csv'
MIN_OBS_MA = 200      # F06 convention
MIN_OBS_PCT = 252     # F01/F06/F11/F13 convention
HV_WINDOW = 21        # F13 convention
FWD_H = 21            # OP-D1/F05/F13 monthly VRP convention
HI_CUT = 0.8          # top quintile, F06 Q5 / F13 c5 bin==4 convention

nf = pd.read_csv(NIFTY_CSV, parse_dates=['Date']).sort_values('Date').reset_index(drop=True)
px = pd.to_numeric(nf['Adj Close'], errors='coerce')
ok = px.notna()
nf = nf.loc[ok].reset_index(drop=True)
px = px.values[ok.values] if False else nf['Adj Close'].astype(float).values
M = len(px)
r = np.diff(np.log(px))  # r[i] realized on nf.Date[i+1]; state date for r[i] = nf.Date[i]
print(f"NIFTY daily: {M} rows {nf['Date'].iloc[0].date()}..{nf['Date'].iloc[-1].date()}")

ma200 = pd.Series(px).rolling(MIN_OBS_MA, min_periods=MIN_OBS_MA).mean().values
trend_above = np.where(np.isnan(ma200), np.nan, (px > ma200).astype(float))

vx = pd.read_csv(VIX_CSV, parse_dates=['date']).sort_values('date').reset_index(drop=True)
print(f"India VIX daily: {len(vx)} rows {vx['date'].min().date()}..{vx['date'].max().date()}")
vix_close = vx.set_index('date')['close']

nf_idx = pd.Series(np.arange(M), index=nf['Date'])
common_dates = pd.Index(nf['Date']).intersection(pd.Index(vx['date'])).sort_values()

cd = pd.DataFrame({'date': common_dates})
cd['pos'] = cd['date'].map(nf_idx).astype(int)
cd['vix'] = cd['date'].map(vix_close)
cd['trend_above'] = cd['pos'].map(lambda p: trend_above[p])

hv = np.full(len(cd), np.nan)
for i, p in enumerate(cd['pos'].values):
    if p >= HV_WINDOW:
        hv[i] = np.sqrt(252.0 / HV_WINDOW * np.sum(r[p - HV_WINDOW:p] ** 2)) * 100.0
cd['hv21_trail'] = hv
cd['spread'] = cd['vix'] - cd['hv21_trail']

cd['vix_pct'] = expanding_percentile(cd['vix'].values, min_obs=MIN_OBS_PCT)
cd['spread_pct'] = expanding_percentile(cd['spread'].values, min_obs=MIN_OBS_PCT)
print(f"vix_pct first valid: {cd.loc[cd['vix_pct'].notna(),'date'].min().date()}; "
      f"spread_pct first valid: {cd.loc[cd['spread_pct'].notna(),'date'].min().date()}")

# monthly entries: row-wise first trading day per calendar month (BUG-FIX vs F13's .first())
cd = cd.sort_values('date').reset_index(drop=True)
cd['ym'] = cd['date'].dt.to_period('M')
entries = cd.drop_duplicates('ym', keep='first').reset_index(drop=True)

erows = []
for _, row in entries.iterrows():
    p = int(row['pos'])
    if p + FWD_H >= M:
        continue
    if not (np.isfinite(row['vix_pct']) and np.isfinite(row['spread_pct']) and np.isfinite(row['trend_above'])):
        continue
    fwd21 = r[p:p + FWD_H]
    rv21 = np.sqrt(252.0 / FWD_H * np.sum(fwd21 ** 2)) * 100.0
    vrp = row['vix'] - rv21
    erows.append((row['date'], row['vix_pct'], row['spread_pct'], row['trend_above'], vrp))
E = pd.DataFrame(erows, columns=['date', 'vix_pct', 'spread_pct', 'trend_above', 'vrp'])
n_all = len(E)
print(f"\nmonthly VRP entries (all 3 states valid): n={n_all} "
      f"({E['date'].min().date()}..{E['date'].max().date()})")

base_mean = E['vrp'].mean()
print(f"\nUNCONDITIONAL baseline: mean VRP capture = {base_mean:+.3f} vol pts, n={n_all}")

vix_hi = E['vix_pct'] >= HI_CUT
spread_hi = E['spread_pct'] >= HI_CUT
above = E['trend_above'] == 1.0

def report(name, mask):
    n = int(mask.sum())
    m = E.loc[mask, 'vrp'].mean() if n > 0 else float('nan')
    print(f"  {name:<38s} n={n:>4d}  mean_vrp={m:+7.3f}  (delta_vs_base={m - base_mean:+6.3f})")
    return n, m

print("\n--- SINGLE FILTERS (each alone, top quintile pct>=0.8; trend both directions) ---")
n_v, m_v = report("VIX-pct HIGH (>=Q5) alone", vix_hi)
n_s, m_s = report("IV-HV spread HIGH (>=Q5) alone", spread_hi)
n_ta, m_ta = report("trend: ABOVE 200dMA alone", above)
n_tb, m_tb = report("trend: BELOW 200dMA alone", ~above)

print("\n--- PAIRWISE STACKS ---")
report("VIX-hi x spread-hi", vix_hi & spread_hi)
report("VIX-hi x aboveMA", vix_hi & above)
report("VIX-hi x belowMA", vix_hi & ~above)
report("spread-hi x aboveMA", spread_hi & above)
report("spread-hi x belowMA", spread_hi & ~above)

print("\n--- FULL 3-WAY STACK (both trend directions) ---")
n_stack_up, m_stack_up = report("VIX-hi x spread-hi x aboveMA", vix_hi & spread_hi & above)
n_stack_dn, m_stack_dn = report("VIX-hi x spread-hi x belowMA", vix_hi & spread_hi & ~above)

# Pick by LARGER n, not larger deviation (picking the bigger-|delta| side would be a
# look-ahead-selection / data-mining move -- trend has no directional prior here, F06
# registered only a dispersion finding, so the fair, non-cherry-picked choice is whichever
# trend side keeps more usable months).
best_stack_n, best_stack_m, best_stack_name = (
    (n_stack_up, m_stack_up, "VIX-hi x spread-hi x aboveMA")
    if n_stack_up >= n_stack_dn
    else (n_stack_dn, m_stack_dn, "VIX-hi x spread-hi x belowMA")
)

print("\n--- VERDICT INPUTS ---")
print(f"VIX-pct alone:            n={n_v:4d}  mean={m_v:+.3f}  lift_vs_base={m_v-base_mean:+.3f}")
print(f"Best full 3-way stack:    n={best_stack_n:4d}  mean={best_stack_m:+.3f}  "
      f"lift_vs_base={best_stack_m-base_mean:+.3f}  ({best_stack_name})")
incr_lift = best_stack_m - m_v
n_shrink_pct = 100.0 * (1 - best_stack_n / n_v) if n_v else float('nan')
print(f"incremental lift of stack OVER VIX-pct-alone: {incr_lift:+.3f} vol pts, "
      f"at an n-shrink of {n_shrink_pct:.1f}% ({n_v}->{best_stack_n})")

verdict = "STACK_WORTH_IT" if (incr_lift >= 1.0 and best_stack_n >= 20) else "VIX_PCT_ALONE_CARRIES_IT"
print(f"\nCOMBINER VERDICT (descriptive, no registered bar): {verdict}")

import json, os
cells = [
    {"name": "unconditional monthly VRP capture", "value": round(float(base_mean), 3),
     "bar": "none (descriptive baseline)", "verdict": "DESCRIPTIVE", "n": n_all},
    {"name": "VIX-pct HIGH (Q5) alone", "value": round(float(m_v), 3),
     "bar": "none (descriptive single filter)", "verdict": "DESCRIPTIVE", "n": n_v},
    {"name": "IV-HV spread HIGH (Q5) alone [F13 c5 leg, re-derived, bug-fixed aggregation]",
     "value": round(float(m_s), 3), "bar": "none (descriptive single filter)",
     "verdict": "DESCRIPTIVE", "n": n_s},
    {"name": "trend ABOVE 200dMA alone", "value": round(float(m_ta), 3),
     "bar": "none (descriptive single filter)", "verdict": "DESCRIPTIVE", "n": n_ta},
    {"name": "trend BELOW 200dMA alone", "value": round(float(m_tb), 3),
     "bar": "none (descriptive single filter)", "verdict": "DESCRIPTIVE", "n": n_tb},
    {"name": f"best full 3-way stack ({best_stack_name})", "value": round(float(best_stack_m), 3),
     "bar": "none (descriptive stack)", "verdict": "DESCRIPTIVE", "n": int(best_stack_n)},
    {"name": "incremental lift: stack minus VIX-pct-alone", "value": round(float(incr_lift), 3),
     "bar": "none (descriptive comparison)", "verdict": verdict, "n_shrink_pct": round(n_shrink_pct, 1)},
]
out = {
    "id": "c01",
    "headline": (f"Stack (VIXhi x spreadhi x {best_stack_name.split('x')[-1].strip()}) mean VRP "
                 f"{best_stack_m:+.2f} (n={best_stack_n}) vs VIX-pct alone {m_v:+.2f} (n={n_v}): "
                 f"incr {incr_lift:+.2f} at {n_shrink_pct:.0f}% n-shrink -> {verdict}"),
    "cells": cells,
    "caveats": (
        f"Monthly VRP entries n={n_all} ({E['date'].min().date()}..{E['date'].max().date()}), "
        "OP-D1/F05/F13 convention (first common NIFTY/VIX day per month needing 21 fwd NIFTY "
        "days), all three states (vix_pct, spread_pct, trend_above) required valid "
        "(min_obs=252/252/200 respectively) -> n is a strict subset of F05/F13's own n=142/154 "
        "monthly samples (fewer usable months here because trend needs MA200 warmup too). "
        "F13's known groupby('ym').first() row-frankenstein bug (combiner audit on f13) is "
        "NOT repeated: entries built via sort_values+drop_duplicates(keep='first'), verified "
        "row-wise correct. IV-HV spread state and VIX-pct state are mechanically correlated "
        "(spread = VIX - HV21_trail, so spread inherits VIX's own level) -- stacking them is "
        "not adding two independent signals, it is asking whether the SPREAD component nets "
        "out any residual signal beyond VIX alone. Trend (200d-MA) is registered elsewhere "
        "(F06) as a dead standalone signal (T-CTRL1, 0/10) and is used here only as a "
        "regime-conditioning corner per F06's own registered dispersion finding, never as a "
        "return-predictive claim. Single-index NIFTY50 + single India-VIX construction "
        "(index-level, no survivorship exposure). No PASS/MISS bar was pre-registered for "
        "this combiner cell (Entry OP-D2 combiners are booked descriptively, feed the "
        "H60-VRP design brief only, no promotion) -- the STACK_WORTH_IT/VIX_PCT_ALONE_CARRIES_IT "
        "verdict above is this script's own descriptive threshold (incremental lift >= 1.0 vol "
        "pt at n>=20), stated plainly, not a registered bar."
    ),
}
os.makedirs('/home/user/claude-demo/research/opt_sweep', exist_ok=True)
with open('/home/user/claude-demo/research/opt_sweep/c01.json', 'w') as fh:
    json.dump(out, fh, indent=1)
print("\nwrote research/opt_sweep/c01.json")
