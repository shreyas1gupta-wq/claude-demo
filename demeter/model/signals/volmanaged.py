"""volmanaged -- volatility-managed leverage (Moreira & Muir 2017) with a two-horizon variance forecast and an
asymmetric no-trade band.

Rules (decided at the close of day t from data up to that close; the engine applies the level to day t+1)
--------------------------------------------------------------------------------------------------------
1. VARIANCE FORECAST. sigma_t = max( EWMA-vol(halflife hl), EWMA-vol(halflife hl * long_mult) ) of daily S&P 500
   price returns, annualised (features.ewma_vol, 20-session warm-up). Taking the max of a fast and a slow horizon
   makes the forecast rise as fast as the fast leg (de-lever quickly after a shock) and fall only as fast as the
   slow leg (re-lever slowly once a high-vol regime has been established). Trailing only.
2. RAW TARGET. T_t = clip( (target_vol / sigma_t) ** 2 , 0, 3 ): exposure inversely proportional to forecast
   VARIANCE (the Moreira-Muir form; the inverse-VOL form, POWER = 1, was rejected in DEV, see design note).
3. ASYMMETRIC NO-TRADE BAND. Held level H_t = H_{t-1} unless T_t - H_{t-1} > band_up (target has risen) or
   H_{t-1} - T_t > band_dn (target has fallen); then H_t = T_t. band_dn < band_up means the rule acts on
   de-levering signals sooner than on re-levering signals (leverage effect). The band is the turnover control.
4. Long or cash only, leverage continuous in [0, 3]. No VIX (runs from 1950), no trend filter, no price signal,
   no shock override (tested in DEV and rejected: -3 sigma days are followed by reversals more often than by
   continuation, so forced cash after them cost ~0.09 Sharpe).

Parameters (5 tunables; each chosen on the development window 1990-01..2012-06, cross-checked on 1950-2012;
coarse grid 540 combos + refinement grid 216 combos, see dev_results/volmanaged_DESIGN_NOTE.md)
-----------------------------------------------------------------------------------------------------------
target_vol = 0.14 : the volatility at which the rule is exactly 1x. Grid 0.12-0.16. The dev_1990 Sharpe is flat
             0.44-0.49 across 0.12-0.15; 0.15-0.16 breaks the 1970-89 era drawdown gate (-40%), 0.12 gives up
             participation. 0.14 is the centre of the region that clears every era with ~5 points of margin.
hl = 13    : fast EWMA halflife in sessions. Grid 6-20; Sharpe rises 0.43 -> 0.51 from 6 to 20 and is flat from 13.
             13 is interior of the 10-20 plateau so the +-30% perturbations (9-17) stay on it.
long_mult = 8 : slow halflife = hl * long_mult = 104 sessions. Grid 3-12; flat 0.46-0.51 from 5 to 12; 8 is the centre.
band_up = 0.75, band_dn = 0.30 : no-trade bands (leverage units) for upward / downward target moves. Grids 0.5-1.0
             and 0.15-0.45; Sharpe is flat (0.48-0.50) across both; the bands set the trade count (1-8/yr).

Structural constants (not tuned): MAX_LEV = 3 (mandate); POWER = 2 (MM form; DEV comparison in the note);
DISCRETE = False (rounding to {0,1,2,3} cost ~0.05 Sharpe and doubled trades in DEV); WEEKLY = False (a weekly
band check was no better than the daily one in DEV); EST = "max2" (plain EWMA and downside semi-vol were
tested and are reported in the note); the 20-session EWMA warm-up (pre-warm-up level = 0 = cash). The shock
override knobs in _core are kept at "off" for reproducibility of the DEV comparisons only.

Known failure modes: (i) leverage effect -- vol rises AFTER the first down move, so the first shock day is taken
at the pre-shock leverage; (ii) a bear market at moderate volatility (1969-70, 2000-02) is taken at 0.5-1.5x
the whole way down because the rule has no directional input; (iii) recoveries start while vol is still high,
so the first leg is taken at low leverage (2009); (iv) calm months with a few -1..-2% days pay band-crossing
costs for nothing.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

import features as F

NAME = "volmanaged"
FAMILY = "volatility-managed leverage (inverse trailing variance, Moreira-Muir 2017), two-horizon vol, asymmetric band"
HYPOTHESIS = (
    "Realised equity volatility is highly predictable at horizons of days to a month while the conditional mean "
    "excess return is roughly flat in volatility, so scaling exposure inversely to forecast variance raises the "
    "Sharpe ratio (Moreira & Muir 2017) and mechanically holds little exposure through the long high-variance "
    "drawdowns of 1973-74, 2000-02 and 2007-09 while running up to 3x in calm bull markets. A two-horizon forecast "
    "(fast up, slow down) and an asymmetric no-trade band keep the daily rule's whipsaw and turnover inside budget."
)

# ---- structural constants (decided in DEV, see design note; not tunables) -------------------------------------
MAX_LEV = 3.0
POWER = 2            # exponent on target_vol / sigma: 2 = Moreira-Muir (inverse variance), 1 = inverse vol
DISCRETE = False     # round held levels to {0,1,2,3}
WEEKLY = False       # band check only on the first session of each ISO week
MIN_PERIODS = 20     # EWMA warm-up sessions (pre-warm-up = cash)
EST = "max2"         # "ewma" (plain), "max2" (max of fast and slow EWMA), "semi" (downside semi-vol)
SHOCK_Z, SHOCK_DAYS = 0.0, 0   # shock override OFF (rejected in DEV)

DEFAULT_PARAMS = dict(target_vol=0.14, hl=13.0, long_mult=8.0, band_up=0.75, band_dn=0.30)   # frozen after DEV grids


def _sigma(ret: pd.Series, hl: float, est: str, long_mult: float) -> pd.Series:
    if est == "ewma":
        return F.ewma_vol(ret, halflife=hl, min_periods=MIN_PERIODS)
    if est == "max2":
        a = F.ewma_vol(ret, halflife=hl, min_periods=MIN_PERIODS)
        b = F.ewma_vol(ret, halflife=hl * max(float(long_mult), 1.0), min_periods=MIN_PERIODS)
        return pd.concat([a, b], axis=1).max(axis=1)
    if est == "semi":
        neg2 = ret.clip(upper=0.0) ** 2
        return np.sqrt(2.0 * neg2.ewm(halflife=hl, min_periods=MIN_PERIODS).mean()) * F.ANN
    raise ValueError(est)


def _core(df: pd.DataFrame, target_vol: float, hl: float, long_mult: float, band_up: float, band_dn: float,
          power: int = POWER, discrete: bool = DISCRETE, weekly: bool = WEEKLY, est: str = EST,
          shock_z: float = SHOCK_Z, shock_days: int = SHOCK_DAYS) -> pd.Series:
    ret = df["spx_ret"].astype(float)
    hl = max(float(hl), 1.0)
    sig = _sigma(ret, hl, est, long_mult)                                   # annualised, trailing
    tgt = ((float(target_vol) / sig) ** int(power)).clip(lower=0.0, upper=MAX_LEV)

    n_shock = int(round(shock_days)) if shock_days else 0
    if n_shock > 0 and shock_z > 0:
        sig_d = sig.shift(1) / np.sqrt(252)
        shock = (ret < -float(shock_z) * sig_d).fillna(False)
        blocked = (shock.rolling(n_shock, min_periods=1).max().fillna(0) > 0).to_numpy()
    else:
        blocked = np.zeros(len(df), dtype=bool)

    if weekly:  # first session of a new ISO week: causal (compares with the PREVIOUS row only)
        wk = pd.Series(df.index.isocalendar().week.values, index=df.index)
        decide = wk.ne(wk.shift(1)).to_numpy()
    else:
        decide = np.ones(len(df), dtype=bool)

    t = tgt.to_numpy(dtype=float)
    out = np.zeros(len(t), dtype=float)
    cur = np.nan
    bu, bd = float(band_up), float(band_dn)
    for i in range(len(t)):
        if np.isnan(t[i]):                      # warm-up -> cash
            out[i] = 0.0
            continue
        if blocked[i]:
            cur = 0.0
        elif np.isnan(cur) or (decide[i] and ((t[i] - cur) > bu or (cur - t[i]) > bd)):
            cur = float(np.rint(t[i])) if discrete else t[i]
        out[i] = cur
    return pd.Series(out, index=df.index).clip(0.0, MAX_LEV)


def signal(df: pd.DataFrame, target_vol: float = 0.14, hl: float = 13.0, long_mult: float = 8.0,
           band_up: float = 0.75, band_dn: float = 0.30) -> pd.Series:
    """Target leverage L_t in [0, 3] decided at the close of day t (see module docstring)."""
    return _core(df, target_vol, hl, long_mult, band_up, band_dn)
