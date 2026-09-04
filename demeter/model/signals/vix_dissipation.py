"""Implied-volatility dissipation with a volatility-regime leverage tier.

Rules (decided at each close, applied the next day):
  1. RISK GATE. Stay out of the market while implied volatility is *rising* relative to its own
     recent level: cash whenever VIX closes above its `vix_ma`-day average by more than
     `enter_buf` (exit trigger). Re-enter only once VIX closes below that average by `exit_buf`
     (entry trigger). The two buffers form a hysteresis band, so a single spike neither pushes
     the position out nor pulls it back in.
  2. SHOCK OVERRIDE. Regardless of the gate, force cash for `shock_days` sessions after a
     volatility shock: a daily loss worse than `shock_z` times the trailing 21-day volatility.
     This encodes the leverage effect - down-moves raise volatility faster than up-moves lower it.
  3. LEVERAGE TIER. When invested, hold 3x while 21-day realised volatility is below `rv_lo`,
     otherwise 1x. Calm markets get the full multiplier; elevated-volatility markets are held
     unlevered, matching the manager's "unleveraged or reduced exposure" description.

Development sample: 1990-01-01 to 2012-06-30 (VIX starts in 1990). Parameters frozen before
any out-of-sample evaluation.
"""
import numpy as np
import pandas as pd
import features as F

NAME = "vix_dissipation"
FAMILY = "implied-volatility dissipation + volatility-regime leverage tier"
HYPOTHESIS = (
    "The tradeable signal is the *direction* of implied volatility, not its level: equities are worth owning "
    "with leverage while VIX is falling relative to its own recent average, and are best avoided while it is rising, "
    "even when the level is high. A short forced-cash window after a volatility shock captures the leverage effect, "
    "and a realised-volatility tier decides whether the invested state is 3x or 1x."
)
DEFAULT_PARAMS = dict(vix_ma=10, enter_buf=0.02, exit_buf=0.0, shock_z=2.5, shock_days=3, rv_lo=0.18)


def signal(df, vix_ma=10, enter_buf=0.02, exit_buf=0.0, shock_z=2.5, shock_days=3, rv_lo=0.18):
    vix = df["vix_close"].ffill()
    ratio = vix / F.sma(vix, vix_ma)
    invest_trigger = ratio < (1.0 - exit_buf)
    exit_trigger = ratio > (1.0 + enter_buf)
    state = F.hysteresis(invest_trigger, exit_trigger, initial=False)

    ret = df["spx_ret"]
    rv = F.realized_vol(ret, 21)
    shock = ret < -shock_z * rv / np.sqrt(252)
    blocked = shock.rolling(int(shock_days), min_periods=1).max().fillna(0) > 0

    lev = pd.Series(0.0, index=df.index)
    invested = state & ~blocked & vix.notna()
    lev[invested] = 1.0
    lev[invested & (rv < rv_lo)] = 3.0
    return lev
