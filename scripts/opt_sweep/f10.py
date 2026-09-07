"""
OP-D2 family F10 -- "candle patterns graveyard test"
Registered cell (research/register/trial-ledger.md, Entry OP-D2, line F10):
  "F10 candles: doji/engulf/hammer/3-down on index OHLC -> fwd 1d/5d (8) --
   PRIOR: ALL NULL (graveyard registration; any |t|>2 cell is a recorded
   surprise, not a signal)."
8 registered cells = 4 patterns x 2 forward horizons {1d, 5d}.

Data: ingest/vault/index/nifty50_daily_2007_2026.csv (vault only).
Pattern flag at day t uses ONLY OHLC data with index <= t (raw Open/High/
Low/Close, standard candle shape). Forward return target uses Adj Close at
t+1 (1d) and t+5 (5d) -- this is the forward-looking label being tested,
not a lookahead in the feature. No fitted/estimated parameters anywhere in
this script (pure fixed geometric definitions below) -> no fold structure
needed; still, everything is computed once, top-to-bottom, no re-fitting.

Pattern definitions (declared, fixed, no magic-number search -- these are
the standard textbook candle-shape thresholds, not fit to this sample):
  body  = |Close_t - Open_t| ;  rng = High_t - Low_t  (rng>0 required)
  doji   : body <= 0.10 * rng                          (indecision; no
           directional prior -> raw fwd return tested, two-sided)
  hammer : lower_shadow = min(Open,Close) - Low >= 2*body  AND
           upper_shadow = High - max(Open,Close) <= 0.10*rng  AND body>0
           (textbook bullish-reversal shape; aligned return = +1 * raw fwd
           return, i.e. testing the traditional bullish claim)
  engulf : bullish: Close_{t-1}<Open_{t-1} (red t-1), Close_t>Open_t (green
           t), Open_t<=Close_{t-1}, Close_t>=Open_{t-1} (body engulfs).
           bearish: mirror image. direction = +1 bullish / -1 bearish;
           aligned return = direction * raw fwd return (textbook claim:
           bullish engulf -> up, bearish engulf -> down)
  3-down : Close_t<Close_{t-1}<Close_{t-2}<Close_{t-3} (three strictly
           lower closes ending at t). Textbook trader lore = short-term
           bullish reversal -> aligned return = +1 * raw fwd return.

Test: one-sample t-test of aligned forward return vs 0 (scipy.stats
ttest_1samp -- standard-library stat test, not project machinery per
process note #6 which governs regime/preprocess/CV tooling).
Bar (registered): PRIOR ALL NULL -> verdict PASS if |t|<=2 (null holds as
registered); verdict TWO-SIDED if |t|>2 (a recorded surprise -- NOT a
promoted signal per the graveyard registration).
"""
import sys
sys.path.insert(0, "/home/user/claude-demo")
import numpy as np
import pandas as pd
from scipy.stats import ttest_1samp

CSV = "ingest/vault/index/nifty50_daily_2007_2026.csv"

df = pd.read_csv(CSV, parse_dates=["Date"]).sort_values("Date").reset_index(drop=True)
n_rows = len(df)
O, H, L, C = df["Open"].to_numpy(), df["High"].to_numpy(), df["Low"].to_numpy(), df["Close"].to_numpy()
AC = df["Adj Close"].to_numpy()

body = np.abs(C - O)
rng = H - L
valid_rng = rng > 0

# forward returns off Adj Close (registered convention)
fwd1 = np.full(n_rows, np.nan)
fwd5 = np.full(n_rows, np.nan)
fwd1[:-1] = AC[1:] / AC[:-1] - 1.0
fwd5[:-5] = AC[5:] / AC[:-5] - 1.0

# --- pattern flags (all use only data at index <= t) ---
doji = valid_rng & (body <= 0.10 * rng)

lower_shadow = np.minimum(O, C) - L
upper_shadow = H - np.maximum(O, C)
hammer = valid_rng & (body > 0) & (lower_shadow >= 2 * body) & (upper_shadow <= 0.10 * rng)

prev_O = np.roll(O, 1); prev_C = np.roll(C, 1)
bull_engulf = (prev_C < prev_O) & (C > O) & (O <= prev_C) & (C >= prev_O)
bear_engulf = (prev_C > prev_O) & (C < O) & (O >= prev_C) & (C <= prev_O)
bull_engulf[0] = False; bear_engulf[0] = False
engulf_flag = bull_engulf | bear_engulf
engulf_dir = np.where(bull_engulf, 1.0, np.where(bear_engulf, -1.0, 0.0))

c1 = np.roll(C, 1); c2 = np.roll(C, 2); c3 = np.roll(C, 3)
three_down = (C < c1) & (c1 < c2) & (c2 < c3)
three_down[:3] = False

PATTERNS = {
    "doji":   (doji,        np.ones(n_rows)),
    "hammer": (hammer,      np.ones(n_rows)),
    "engulf": (engulf_flag, engulf_dir),
    "3down":  (three_down,  np.ones(n_rows)),
}
HORIZONS = {"1d": fwd1, "5d": fwd5}

print(f"vault rows: {n_rows}  span: {df['Date'].min().date()} .. {df['Date'].max().date()}")
print(f"{'cell':16s} {'n':>6s} {'mean_aligned_ret%':>18s} {'t_stat':>9s} {'p':>9s}  verdict")

cells = []
for pname, (flag, direction) in PATTERNS.items():
    n_pat = int(flag.sum())
    for hname, fwd in HORIZONS.items():
        mask = flag & ~np.isnan(fwd)
        n = int(mask.sum())
        aligned = fwd[mask] * direction[mask]
        if n >= 2:
            mean_ret = float(np.mean(aligned)) * 100.0
            t_stat, p_val = ttest_1samp(aligned, 0.0)
            t_stat = float(t_stat); p_val = float(p_val)
        else:
            mean_ret, t_stat, p_val = float("nan"), float("nan"), float("nan")
        verdict = "MISS" if n < 30 else ("TWO-SIDED" if abs(t_stat) > 2 else "PASS")
        cell_name = f"{pname}_fwd{hname}"
        print(f"{cell_name:16s} {n:6d} {mean_ret:18.4f} {t_stat:9.3f} {p_val:9.4f}  {verdict}")
        cells.append({
            "name": cell_name, "n_occurrences_pattern": n_pat, "n_obs_used": n,
            "mean_aligned_fwd_ret_pct": round(mean_ret, 4) if n >= 2 else None,
            "t_stat": round(t_stat, 3) if n >= 2 else None,
            "p_value": round(p_val, 4) if n >= 2 else None,
            "verdict": verdict,
        })

n_surprise = sum(1 for c in cells if c["verdict"] == "TWO-SIDED")
n_miss = sum(1 for c in cells if c["verdict"] == "MISS")
print(f"\nsummary: {len(cells)} cells, {n_surprise} surprises (|t|>2), {n_miss} MISS (n<30)")

import json
print("\n--- JSON_CELLS ---")
print(json.dumps(cells))
