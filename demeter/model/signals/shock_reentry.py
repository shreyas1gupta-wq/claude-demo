"""Volatility-shock exit with an oversold / volatility-peak re-entry.

Rules (decided at each close, applied the next day):
  1. EXIT. Leave the market for at least `cool_days` sessions when trailing 21-day realised
     volatility rises above `rv_exit`, or on any daily loss worse than `shock_z` trailing
     standard deviations.
  2. RE-ENTRY. Come back at full leverage while the market is *recovering from* stress rather
     than waiting for calm: VIX at least `vix_fall` below its `vix_win`-day maximum (fear
     dissipating) and short-term oversold, RSI(2) below `rsi_max` or price back above its
     20-day average.
  3. CALM REGIME. Independently of the crisis logic, hold 3x whenever realised volatility is
     below `rv_calm` and price is above its 100-day average - the low-volatility bull state.
  Invested exposure is 3x in the calm regime and after a confirmed re-entry, 1x otherwise.

Development sample: 1990-01-01 to 2012-06-30. Parameters frozen before out-of-sample evaluation.
"""
import numpy as np
import pandas as pd
import features as F

NAME = "shock_reentry"
FAMILY = "volatility-shock exit + mean-reversion re-entry"
HYPOTHESIS = (
    "Two mechanisms drive the record: a fast exit when volatility clusters, and an aggressive re-entry into the "
    "recovery while implied volatility is still high but falling from its peak. Waiting for volatility to normalise "
    "forfeits the rebound; re-entering on the fall from the peak captures it."
)
DEFAULT_PARAMS = dict(rv_exit=0.22, shock_z=2.5, cool_days=5, vix_fall=0.30, vix_win=20, rv_calm=0.16)


def signal(df, rv_exit=0.22, shock_z=2.5, cool_days=5, vix_fall=0.30, vix_win=20, rv_calm=0.16):
    ret, px = df["spx_ret"], df["spx_px"]
    rv = F.realized_vol(ret, 21)
    vix = df["vix_close"].ffill()

    shock = (ret < -shock_z * rv / np.sqrt(252)) | (rv > rv_exit)
    cooling = shock.rolling(int(cool_days), min_periods=1).max().fillna(0) > 0

    vix_max = vix.rolling(int(vix_win), min_periods=5).max()
    fear_falling = vix < vix_max * (1.0 - vix_fall)
    oversold = (F.rsi(px, 2) < 20) | (px > F.sma(px, 20))
    rebound = fear_falling & oversold

    calm = (rv < rv_calm) & (px > F.sma(px, 100))

    lev = pd.Series(0.0, index=df.index)
    lev[calm & ~cooling] = 3.0
    lev[rebound] = 3.0
    lev[~calm & ~cooling & ~rebound & (px > F.sma(px, 100))] = 1.0
    return lev.clip(0, 3)
