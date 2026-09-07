"""
OP-D2 family f07: 12-1 momentum sign -> fwd 1m/3m ret+vol.
Registered (trial-ledger.md, Entry OP-D2, F07), 3 cells:
  prior: weak positive tilt (T3 cited).

Registered cells (3), matching the "(3)" cell count = 2 return horizons + 1 vol comparison:
  1. mom-sign -> fwd 1m (21d) return spread (pos-momentum mean minus neg-momentum mean)
  2. mom-sign -> fwd 3m (63d) return spread
  3. mom-sign -> fwd 1m (21d) realized-vol spread (fwd 3m vol printed as descriptive context
     only -- not a registered cell, same convention as f06's full-matrix-vs-corners split)

Interpretation criterion for the "weak positive tilt" prior, stated BEFORE computing (process
note #5 -- partial/soft bars quote the parent design; here the parent design gives a directional
prior with no numeric threshold, so the operational test is fixed up front): PASS if the spread
mean is positive (consistent with the direction of the prior); MISS if the spread mean is
<= 0 (contradicts direction). "Weak" (vs a stronger, highly significant tilt) is reported
separately via the two-sample t-stat -- not part of the PASS/MISS criterion, to avoid a second,
post-hoc goalpost on top of the registered direction.

NO LOOKAHEAD:
  - 12-1 momentum at t = Px[t-21] / Px[t-252] - 1: trailing 12m return skipping the most
    recent 1m, using only Adj Close observed at/before t (min_obs=253: needs t-252 to exist).
  - Sign of momentum at t is the state; it is fixed using data <= t only.
  - Forward 1m (21d) / 3m (63d) simple return and realized vol use Adj Close / daily log
    returns strictly AFTER t (t+1 .. t+21 or t+63) -- these are the forward OUTCOME variables
    being tabulated by the state at t, never inputs to the state.
Vault only. Prints only.
"""
import sys
sys.path.insert(0, "/home/user/claude-demo")
import numpy as np
import pandas as pd
from scipy import stats as sstats

NIFTY_CSV = "ingest/vault/index/nifty50_daily_2007_2026.csv"
MOM_LOOKBACK = 252   # ~12 months trading days
MOM_SKIP = 21        # ~1 month trading days, skipped (12-1 momentum)
MIN_OBS_MOM = MOM_LOOKBACK + 1  # need t-252 to exist
H1, H3 = 21, 63      # forward horizons, trading days (1m, 3m)
MIN_CELL_N = 30      # minimum obs per state for an evaluable mean/std (precedent: f06)

nifty = pd.read_csv(NIFTY_CSV, parse_dates=["Date"]).sort_values("Date").reset_index(drop=True)
px = nifty["Adj Close"].astype(float).values
logret = np.r_[np.nan, np.diff(np.log(px))]
n = len(px)

# 12-1 momentum sign at t, no lookahead (uses px[t-252] and px[t-21] only, both <= t)
mom = np.full(n, np.nan)
for t in range(MIN_OBS_MOM, n):
    mom[t] = px[t - MOM_SKIP] / px[t - MOM_LOOKBACK] - 1.0

mom_sign = np.where(np.isnan(mom), np.nan, np.where(mom > 0, 1.0, 0.0))

# forward return (%) and forward realized vol (annualized pts, OP-D1 convention) at both horizons
fwd_ret = {H1: np.full(n, np.nan), H3: np.full(n, np.nan)}
fwd_vol = {H1: np.full(n, np.nan), H3: np.full(n, np.nan)}
for H in (H1, H3):
    for t in range(n - H):
        fwd_ret[H][t] = (px[t + H] / px[t] - 1.0) * 100.0
        window = logret[t + 1: t + H + 1]
        if np.all(~np.isnan(window)):
            fwd_vol[H][t] = np.sqrt(252.0 / H * np.sum(window ** 2)) * 100.0

nifty["mom_sign"] = mom_sign
nifty["fwd_ret21"] = fwd_ret[H1]
nifty["fwd_ret63"] = fwd_ret[H3]
nifty["fwd_vol21"] = fwd_vol[H1]
nifty["fwd_vol63"] = fwd_vol[H3]

print("=== f07: 12-1 momentum sign -> fwd 1m/3m ret+vol ===")
print(f"vault file: {NIFTY_CSV}")
print(f"min_obs: momentum lookback={MOM_LOOKBACK}d skip={MOM_SKIP}d (needs {MIN_OBS_MOM} trailing obs)")

def spread_test(df, col, min_n):
    sub = df.dropna(subset=["mom_sign", col])
    pos = sub.loc[sub["mom_sign"] == 1.0, col]
    neg = sub.loc[sub["mom_sign"] == 0.0, col]
    n_pos, n_neg = len(pos), len(neg)
    if n_pos < min_n or n_neg < min_n:
        return dict(n_pos=n_pos, n_neg=n_neg, evaluable=False)
    mean_pos, mean_neg = pos.mean(), neg.mean()
    spread = mean_pos - mean_neg
    tstat, pval = sstats.ttest_ind(pos, neg, equal_var=False)
    return dict(n_pos=n_pos, n_neg=n_neg, mean_pos=mean_pos, mean_neg=mean_neg,
                spread=spread, tstat=tstat, pval=pval, evaluable=True)

print()
print(f"sample: n={len(nifty)} dates {nifty['Date'].min().date()}..{nifty['Date'].max().date()}")
print(f"momentum-sign defined n={int((~np.isnan(mom_sign)).sum())}  "
      f"pos={int((mom_sign==1.0).sum())}  neg={int((mom_sign==0.0).sum())}")
print()

r1 = spread_test(nifty, "fwd_ret21", MIN_CELL_N)
r3 = spread_test(nifty, "fwd_ret63", MIN_CELL_N)
v1 = spread_test(nifty, "fwd_vol21", MIN_CELL_N)
v3 = spread_test(nifty, "fwd_vol63", MIN_CELL_N)  # descriptive context only, not registered

print("Cell 1 -- mom-sign -> fwd 1m (21d) return spread:")
if r1["evaluable"]:
    print(f"  n_pos={r1['n_pos']} n_neg={r1['n_neg']} mean_pos={r1['mean_pos']:.4f}% "
          f"mean_neg={r1['mean_neg']:.4f}% spread={r1['spread']:.4f}% "
          f"t={r1['tstat']:.3f} p={r1['pval']:.4f}")
    verdict1 = "PASS" if r1["spread"] > 0 else "MISS"
    print(f"  direction test (spread>0, weak-positive prior): {verdict1}")
else:
    print(f"  MISS: n_pos={r1['n_pos']} n_neg={r1['n_neg']} below MIN_CELL_N={MIN_CELL_N}, not evaluable")
    verdict1 = "MISS"

print()
print("Cell 2 -- mom-sign -> fwd 3m (63d) return spread:")
if r3["evaluable"]:
    print(f"  n_pos={r3['n_pos']} n_neg={r3['n_neg']} mean_pos={r3['mean_pos']:.4f}% "
          f"mean_neg={r3['mean_neg']:.4f}% spread={r3['spread']:.4f}% "
          f"t={r3['tstat']:.3f} p={r3['pval']:.4f}")
    verdict3 = "PASS" if r3["spread"] > 0 else "MISS"
    print(f"  direction test (spread>0, weak-positive prior): {verdict3}")
else:
    print(f"  MISS: n_pos={r3['n_pos']} n_neg={r3['n_neg']} below MIN_CELL_N={MIN_CELL_N}, not evaluable")
    verdict3 = "MISS"

print()
print("Cell 3 -- mom-sign -> fwd 1m (21d) realized-vol spread (registered):")
if v1["evaluable"]:
    print(f"  n_pos={v1['n_pos']} n_neg={v1['n_neg']} mean_pos={v1['mean_pos']:.4f}pts "
          f"mean_neg={v1['mean_neg']:.4f}pts spread={v1['spread']:.4f}pts "
          f"t={v1['tstat']:.3f} p={v1['pval']:.4f}")
    print("  no directional prior registered for vol -- DESCRIPTIVE")
else:
    print(f"  MISS: n_pos={v1['n_pos']} n_neg={v1['n_neg']} below MIN_CELL_N={MIN_CELL_N}, not evaluable")

print()
print("Context only (not a registered cell) -- mom-sign -> fwd 3m (63d) realized-vol spread:")
if v3["evaluable"]:
    print(f"  n_pos={v3['n_pos']} n_neg={v3['n_neg']} mean_pos={v3['mean_pos']:.4f}pts "
          f"mean_neg={v3['mean_neg']:.4f}pts spread={v3['spread']:.4f}pts "
          f"t={v3['tstat']:.3f} p={v3['pval']:.4f}")
else:
    print(f"  n_pos={v3['n_pos']} n_neg={v3['n_neg']} below MIN_CELL_N={MIN_CELL_N}, not evaluable")
