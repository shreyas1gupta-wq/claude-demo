"""OP-D2 / f14 -- VIX spike decay half-life.

Registered cells (research/register/trial-ledger.md, Entry OP-D2, family F14):
  "VIX spike decay: half-life from >=90th pct; days to re-enter <60th (3)
   -- prior: half-life 15-40 trading days (the sleeve-A holding window)."

Method (no-lookahead, expanding percentile, min_obs=252, per CONTRACT.md / OP-D2 header):
  1. pct[t] = expanding_percentile(VIX_close, min_obs=252) -- uses only data <= t by
     construction (quant.ladder.credit_cycle.expanding_percentile).
  2. A "spike episode" = a maximal run of consecutive trading days with pct >= 0.90.
     Within each episode the PEAK day is the day of max VIX close.
  3. pre-spike baseline = VIX close on the trading day immediately before the episode
     started (the last day with pct < 0.90 before the run began).
  4. half-life (trading days) = first day AFTER the peak (peak, ...] where
     close <= peak - 0.5*(peak - pre_spike_baseline). Purely forward-looking from the
     peak date (peak itself is already known at that point) -- no fit uses future data.
  5. days-to-reentry-below-60th = first day after the peak where pct[t] < 0.60.
     pct[t] itself only uses data <= t (expanding), so this is real-time computable at t.
  6. Episodes that never resolve before the data ends are right-censored and EXCLUDED
     from the median (counted separately) -- never invented.

Data: ingest/vault/vix/india_vix_daily_2010_2023.csv (vault only).
Run: PYTHONPATH=/home/user/claude-demo python3 scripts/opt_sweep/f14.py
"""
import sys
sys.path.insert(0, "/home/user/claude-demo")

import numpy as np
import pandas as pd

from quant.ladder.credit_cycle import expanding_percentile

VIX_PATH = "/home/user/claude-demo/ingest/vault/vix/india_vix_daily_2010_2023.csv"
MIN_OBS = 252
SPIKE_PCT = 0.90
REENTRY_PCT = 0.60

df = pd.read_csv(VIX_PATH, parse_dates=["date"]).sort_values("date").reset_index(drop=True)
close = df["close"].to_numpy(float)
dates = df["date"].to_numpy()
n = len(close)

pct = expanding_percentile(close, min_obs=MIN_OBS)

# --- identify spike episodes: maximal runs of pct >= SPIKE_PCT ---
is_spike = pct >= SPIKE_PCT
episodes = []  # (start_idx, end_idx) inclusive
i = 0
while i < n:
    if is_spike[i]:
        j = i
        while j + 1 < n and is_spike[j + 1]:
            j += 1
        episodes.append((i, j))
        i = j + 1
    else:
        i += 1

half_lives = []
reentries = []
n_total_episodes = len(episodes)
n_half_life_censored = 0
n_reentry_censored = 0
n_no_pre_baseline = 0

for (start, end) in episodes:
    if start == 0:
        # no pre-spike baseline available (episode runs from the very first obs) -- skip
        n_no_pre_baseline += 1
        continue
    pre_baseline = close[start - 1]
    seg = close[start:end + 1]
    peak_offset = int(np.argmax(seg))
    peak_idx = start + peak_offset
    peak_val = close[peak_idx]
    target = peak_val - 0.5 * (peak_val - pre_baseline)

    # half-life: first day after peak with close <= target
    hl = None
    for t in range(peak_idx + 1, n):
        if close[t] <= target:
            hl = t - peak_idx
            break
    if hl is None:
        n_half_life_censored += 1
    else:
        half_lives.append(hl)

    # days to re-enter below REENTRY_PCT (pct[t] already real-time / expanding)
    re = None
    for t in range(peak_idx + 1, n):
        if not np.isnan(pct[t]) and pct[t] < REENTRY_PCT:
            re = t - peak_idx
            break
    if re is None:
        n_reentry_censored += 1
    else:
        reentries.append(re)

median_half_life = float(np.median(half_lives)) if half_lives else float("nan")
median_reentry = float(np.median(reentries)) if reentries else float("nan")

print("=== OP-D2 / f14 -- VIX spike decay half-life ===")
print(f"vault file: {VIX_PATH}")
print(f"n obs: {n}, expanding percentile min_obs={MIN_OBS}")
print(f"spike threshold: pct >= {SPIKE_PCT}, reentry threshold: pct < {REENTRY_PCT}")
print(f"n spike episodes identified (maximal runs): {n_total_episodes}")
print(f"  excluded (no pre-spike baseline, episode at series start): {n_no_pre_baseline}")
usable = n_total_episodes - n_no_pre_baseline
print(f"  usable episodes: {usable}")
print(f"  half-life resolved: {len(half_lives)}, right-censored (never decayed to target): {n_half_life_censored}")
print(f"  reentry resolved: {len(reentries)}, right-censored (never < {REENTRY_PCT} pct): {n_reentry_censored}")
print(f"individual half-lives (trading days): {half_lives}")
print(f"individual days-to-reentry<60th (trading days): {reentries}")
print(f"MEDIAN half-life (trading days): {median_half_life}")
print(f"MEDIAN days-to-reentry-below-60th (trading days): {median_reentry}")
bar_lo, bar_hi = 15, 40
bar_pass = (not np.isnan(median_half_life)) and (bar_lo <= median_half_life <= bar_hi)
print(f"BAR (pre-registered): half-life in [{bar_lo},{bar_hi}] trading days -> {'PASS' if bar_pass else 'MISS'}")
print(f"CELL3 n_usable_spike_episodes: {usable} (half-life n={len(half_lives)}, reentry n={len(reentries)})")
