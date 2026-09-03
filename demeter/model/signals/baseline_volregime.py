"""Baseline reference signal: trend filter + realised-vol regime (used to smoke-test the evaluator)."""
import pandas as pd
import features as F

NAME = "baseline_volregime"
FAMILY = "volatility-regime + trend (reference baseline)"
HYPOTHESIS = "Lever up only when the trend is up and realised vol is low; unlevered when vol is moderate; cash otherwise."
DEFAULT_PARAMS = dict(vol_win=21, lo=0.15, hi=0.25, ma=200)


def signal(df, vol_win=21, lo=0.15, hi=0.25, ma=200):
    rv = F.realized_vol(df["spx_ret"], vol_win)
    trend = df["spx_px"] > F.sma(df["spx_px"], ma)
    lev = pd.Series(0.0, index=df.index)
    lev[(rv < hi) & trend] = 1.0
    lev[(rv < lo) & trend] = 3.0
    return lev
