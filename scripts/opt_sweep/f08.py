#!/usr/bin/env python3
"""OP-D2 family F08 (researcher f08): daily mean-reversion, 5d z-score extremes -> fwd 5d.

REGISTERED (trial-ledger Entry OP-D2, 2026-09-07, BEFORE running):
  "F08 daily MR: 5d z<= -2 / >= +2 -> fwd 5d (3) — prior: decayed post-2015;
   |effect| < 0.5 sigma; two-sided."

Operationalization declared here (bars never move after this point):
  - Data: vault only, NIFTY 50 daily Adj Close 2007-09..2026-04. Daily log returns
    r_t = ln(AdjClose_t / AdjClose_{t-1}).
  - 5d return: R5_t = sum(r_{t-4}..r_t), the TRAILING cumulative log return over the 5
    trading days ending at t (uses data <= t only).
  - Z-score (NO LOOKAHEAD): z_t = (R5_t - mean(R5[<=t])) / std(R5[<=t]), an EXPANDING
    window over R5 including t itself (same convention as
    quant.ladder.credit_cycle.expanding_percentile: window is data <= t, min_obs=252 —
    the min_obs already established for daily-series expanding stats in this sweep's
    sibling families F01/F02). ddof=1. First 252 R5 observations are warm-up (NaN z).
  - Event definition: oversold_t = z_t <= -2; overbought_t = z_t >= +2 (registered bar
    thresholds, from the ledger line verbatim).
  - Forward 5d return: fwd5_t = sum(r_{t+1}..r_{t+5}), the cumulative log return over the
    5 trading days AFTER t (strictly future of t; used only for post-hoc evaluation of an
    already-fixed event day, not for the event definition itself -> no lookahead in the
    signal). Requires t+5 to exist.
  - Reversion sign convention: signed_fwd5_t = +fwd5_t for oversold events (bounce = positive
    reversion), -fwd5_t for overbought events (pullback = positive reversion) — this lets
    both tails combine into one "reversion effect" with reversion always positive-signed.
  - Effect size ("sigma" units, per the registered bar): mean(signed_fwd5 over events in a
    subsample) / std(fwd5, ALL trading days with a defined fwd5 in that same subsample) —
    i.e. the event mean-reversion return expressed in units of the unconditional 5d-return
    dispersion of that period (a Cohen's-d-style standardized effect, not a t-stat).
  - THREE registered cells = the same effect-size construction on three samples, to
    operationalize "decayed post-2015" directly:
      c1 full sample   (2007-09..2026-04, whatever the AdjClose vault covers)
      c2 pre-2015 split  (event day date < 2015-01-01)
      c3 post-2015 split (event day date >= 2015-01-01)
    Split date 2015-01-01 chosen as the plain calendar date implied by "post-2015" in the
    ledger line (declared here before reading any effect-size number).
  - Family is registered TWO-SIDED: bar is |effect| < 0.5 sigma on each cell (matches
    F02's two-sided treatment — value printed either way, no directional pass/fail).

Run: PYTHONPATH=/home/user/claude-demo python3 scripts/opt_sweep/f08.py
"""
import sys
sys.path.insert(0, "/home/user/claude-demo")
import numpy as np
import pandas as pd

CSV = "/home/user/claude-demo/ingest/vault/index/nifty50_daily_2007_2026.csv"
MIN_OBS_Z = 252
Z_LO, Z_HI = -2.0, 2.0
SPLIT_DATE = pd.Timestamp("2015-01-01")
BAR_SIGMA = 0.5

df = pd.read_csv(CSV, parse_dates=["Date"]).sort_values("Date").reset_index(drop=True)
px = pd.to_numeric(df["Adj Close"], errors="coerce")
ok = px.notna()
px = px[ok].reset_index(drop=True)
dates = df.loc[ok, "Date"].reset_index(drop=True)
n_px = len(px)
print(f"NIFTY daily Adj Close: {n_px} rows {dates.iloc[0].date()}..{dates.iloc[-1].date()}")

r = np.log(px.values[1:] / px.values[:-1])
r_dates = dates.iloc[1:].reset_index(drop=True)
n = len(r)
print(f"daily log returns: n={n}")

# trailing 5d cumulative log return, R5_t defined for t >= 4 (0-indexed on r)
R5 = pd.Series(r).rolling(5).sum().to_numpy()

# expanding z-score of R5, no lookahead: window = R5[<=t], min_obs=252, ddof=1
R5s = pd.Series(R5)
exp_mean = R5s.expanding(min_periods=MIN_OBS_Z).mean()
exp_std = R5s.expanding(min_periods=MIN_OBS_Z).std(ddof=1)
z = ((R5s - exp_mean) / exp_std).to_numpy()
n_z_defined = int(np.isfinite(z).sum())
print(f"z-score defined (min_obs={MIN_OBS_Z} on R5, expanding, data<=t): n={n_z_defined}")

# forward 5d cumulative log return, fwd5_t = sum(r_{t+1}..r_{t+5}), needs t+5 < n
fwd5 = np.full(n, np.nan)
for t in range(n - 5):
    fwd5[t] = r[t + 1:t + 6].sum()

oversold = z <= Z_LO
overbought = z >= Z_HI
event = (oversold | overbought) & np.isfinite(fwd5)
n_oversold_all = int((oversold & np.isfinite(fwd5)).sum())
n_overbought_all = int((overbought & np.isfinite(fwd5)).sum())
print(f"events with defined fwd5: oversold(z<=-2)={n_oversold_all}, overbought(z>=+2)={n_overbought_all}")

signed_fwd5 = np.where(oversold, fwd5, np.where(overbought, -fwd5, np.nan))

r5_event_dates = r_dates  # r_dates[t] is the event/signal day date for index t


def effect_cell(mask_period):
    """mask_period: boolean array over index t (len n) selecting the subsample by event date."""
    ev = event & mask_period
    n_ev = int(ev.sum())
    n_os = int((oversold & mask_period & np.isfinite(fwd5)).sum())
    n_ob = int((overbought & mask_period & np.isfinite(fwd5)).sum())
    mean_signed = float(np.nanmean(signed_fwd5[ev])) if n_ev > 0 else float("nan")
    uncond_mask = mask_period & np.isfinite(fwd5)
    uncond_std = float(np.nanstd(fwd5[uncond_mask], ddof=1)) if uncond_mask.sum() > 1 else float("nan")
    eff = mean_signed / uncond_std if uncond_std and np.isfinite(uncond_std) else float("nan")
    return n_ev, n_os, n_ob, mean_signed, uncond_std, eff


full_mask = np.ones(n, dtype=bool)
pre_mask = np.array([d < SPLIT_DATE for d in r5_event_dates])
post_mask = ~pre_mask

for label, m in [("full_sample", full_mask), ("pre_2015", pre_mask), ("post_2015", post_mask)]:
    n_ev, n_os, n_ob, mean_signed, uncond_std, eff = effect_cell(m)
    date_lo = r5_event_dates[m].min().date() if m.sum() else None
    date_hi = r5_event_dates[m].max().date() if m.sum() else None
    print(f"[{label}] range {date_lo}..{date_hi}: n_events={n_ev} (oversold={n_os}, overbought={n_ob}), "
          f"mean_signed_fwd5_logret={mean_signed:.6f}, uncond_fwd5_std={uncond_std:.6f}, "
          f"effect_sigma={eff:.4f}, |effect|<{BAR_SIGMA} -> {'within bar' if abs(eff) < BAR_SIGMA else 'exceeds bar'}")

results = {}
for label, m in [("full_sample", full_mask), ("pre_2015", pre_mask), ("post_2015", post_mask)]:
    results[label] = effect_cell(m)

full_eff = results["full_sample"][5]
pre_eff = results["pre_2015"][5]
post_eff = results["post_2015"][5]
print(f"\nSUMMARY: full={full_eff:.4f} sigma, pre2015={pre_eff:.4f} sigma, post2015={post_eff:.4f} sigma "
      f"(bar |effect|<{BAR_SIGMA}, two-sided, all three cells)")
