"""Low-turnover variant of the recommended model: weekly decisions, wider tiers, longer minimum hold.

Identical logic to `final_model` (trend hysteresis, shock override, volatility-tiered leverage) with
three changes that cut trading to roughly seven position changes a year:
  * the leverage level is read only on the last trading day of each week and then held,
  * the volatility tiers are wider (3x below `rv_lo`, 2x below `rv_hi`, else 1x),
  * a level must be held for `min_days` sessions before it may change.

Development: chosen on 1990-01-01..2012-06-30 (plateau-checked against 1950-01-03..2012-06-30)
among variants whose development drawdown stayed better than -33%, then ranked by fewest trades.
"""
from signals.final_model import core

NAME = "final_model_fewtrades"
FAMILY = "trend hysteresis + volatility tier, weekly decisions (low turnover)"
HYPOTHESIS = (
    "Most of the dual-engine benefit is available at a fraction of the trading. Deciding weekly instead of daily, "
    "with wider volatility tiers and a twenty-day minimum hold, keeps the drawdown protection while cutting position "
    "changes to about seven a year."
)
DEFAULT_PARAMS = dict(ma_fast=100, ma_slow=200, rv_lo=0.10, rv_hi=0.15, min_days=20, shock_days=5)


def signal(df, ma_fast=100, ma_slow=200, rv_lo=0.10, rv_hi=0.15, min_days=20, shock_days=5):
    return core(df, ma_fast, ma_slow, rv_lo, rv_hi, min_days, shock_days, weekly=True)
