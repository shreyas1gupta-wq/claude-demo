"""Low-turnover trend and volatility model: weekly decisions, wide hysteresis, minimum holding.

Rules (evaluated only on the last trading day of each week, then held):
  1. DIRECTION. Price above its `ma_fast`-day average enters; price below its `ma_slow`-day
     average exits. The gap between the two averages is the hysteresis band, so the position
     changes only on a decisive move rather than on every crossing.
  2. LEVERAGE. When invested, 3x while 21-day realised volatility is below `rv_lo`, 2x while it
     is below `rv_hi`, 1x above that.
  3. STICKINESS. Any state is held for at least `min_days` sessions.
  Uses no implied-volatility data, so it runs on the full 1950-2026 history.

Development sample: 1950-01-03 to 2012-06-30. Parameters frozen before out-of-sample evaluation.
"""
import pandas as pd
import features as F

NAME = "trend_vol_fewtrades"
FAMILY = "trend + volatility tier, deliberately low turnover"
HYPOTHESIS = (
    "Most of the dual-engine benefit survives at a fraction of the trading: a weekly decision with a wide "
    "moving-average hysteresis band and a minimum holding period keeps the position changes near twenty a year "
    "while retaining the cash engine's drawdown protection."
)
DEFAULT_PARAMS = dict(ma_fast=100, ma_slow=200, rv_lo=0.13, rv_hi=0.20, min_days=15)


def signal(df, ma_fast=100, ma_slow=200, rv_lo=0.13, rv_hi=0.20, min_days=15):
    px = df["spx_px"]
    rv = F.realized_vol(df["spx_ret"], 21)
    enter = px > F.sma(px, ma_fast)
    exit_ = px < F.sma(px, ma_slow)
    state = F.hysteresis(enter, exit_, initial=False)

    week_end = pd.Series(df.index.isocalendar().week.values, index=df.index).ne(
        pd.Series(df.index.isocalendar().week.values, index=df.index).shift(-1))
    weekly = state.where(week_end).ffill().fillna(False).astype(bool)
    weekly = F.min_holding(weekly, int(min_days)).astype(bool)

    lev = pd.Series(0.0, index=df.index)
    lev[weekly] = 1.0
    lev[weekly & (rv < rv_hi)] = 2.0
    lev[weekly & (rv < rv_lo)] = 3.0
    return lev
