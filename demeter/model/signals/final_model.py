"""Recommended dual-engine model: trend hysteresis, volatility-tiered leverage, shock override, sticky positions.

Every decision uses only data available at that day's close and is applied to the following day.

  1. ENGINE SELECTION (trend hysteresis). Enter the market when the S&P 500 closes above its
     `ma_fast`-day average; leave when it closes below its `ma_slow`-day average. Between the two
     the previous state persists, so the position does not flip on every crossing.
  2. SHOCK OVERRIDE (volatility clustering / leverage effect). Force the cash engine for
     `shock_days` sessions after any daily loss worse than three trailing standard deviations
     (21-day realised volatility). The first large negative shock is the one that predicts the rest.
  3. LEVERAGE TIER (volatility regime). While invested: 3x when 21-day realised volatility is
     below `rv_lo`, 2x below `rv_hi`, otherwise 1x. Calm markets earn the full multiplier;
     elevated volatility is held unlevered.
  4. STICKINESS. A leverage level is held for at least `min_days` sessions before it may change,
     which roughly halves turnover at no cost to development-sample performance.

Development: parameters chosen on 1990-01-01..2012-06-30 (checked for a plateau against
1950-01-03..2012-06-30) and frozen before any out-of-sample evaluation. Selection favoured
risk-adjusted return subject to a development-sample drawdown better than -33%, then fewer trades.
"""
import numpy as np
import pandas as pd
import features as F

NAME = "final_model"
FAMILY = "trend hysteresis + volatility-tiered leverage + shock override"
HYPOTHESIS = (
    "A dual-engine system only needs three ingredients that survive out of sample: a slow trend gate to decide "
    "whether to be in the market at all, a volatility tier to decide how much leverage that state deserves, and a "
    "short forced-cash window after a volatility shock. Faster, cleverer triggers fit the recent bull market and "
    "break in earlier eras."
)
DEFAULT_PARAMS = dict(ma_fast=100, ma_slow=200, rv_lo=0.12, rv_hi=0.16, min_days=10, shock_days=5)
SHOCK_Z = 3.0  # fixed, not tuned


def min_hold_levels(lev: pd.Series, min_days: int) -> pd.Series:
    """Hold each leverage level for at least `min_days` sessions before allowing a change."""
    if not min_days:
        return lev
    out = lev.to_numpy(dtype=float).copy()
    cur, held = out[0], 0
    for i in range(1, len(out)):
        if out[i] != cur and held < min_days:
            out[i] = cur
        elif out[i] != cur:
            cur, held = out[i], 0
        held += 1
    return pd.Series(out, index=lev.index)


def core(df, ma_fast, ma_slow, rv_lo, rv_hi, min_days, shock_days, weekly=False):
    px, ret = df["spx_px"], df["spx_ret"]
    state = F.hysteresis(px > F.sma(px, ma_fast), px < F.sma(px, ma_slow), initial=False)
    rv = F.realized_vol(ret, 21)
    if shock_days:
        shock = ret < -SHOCK_Z * rv / np.sqrt(252)
        state = state & ~(shock.rolling(int(shock_days), min_periods=1).max().fillna(0) > 0)
    lev = pd.Series(0.0, index=df.index)
    lev[state] = 1.0
    lev[state & (rv < rv_hi)] = 2.0
    lev[state & (rv < rv_lo)] = 3.0
    if weekly:  # decide only on the last trading day of each week, then hold
        wk = pd.Series(df.index.isocalendar().week.values, index=df.index)
        lev = lev.where(wk.ne(wk.shift(-1))).ffill().fillna(0.0)
    return min_hold_levels(lev, int(min_days)).clip(0, 3)


def signal(df, ma_fast=100, ma_slow=200, rv_lo=0.12, rv_hi=0.16, min_days=10, shock_days=5):
    return core(df, ma_fast, ma_slow, rv_lo, rv_hi, min_days, shock_days, weekly=False)
