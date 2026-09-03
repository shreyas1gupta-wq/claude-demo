"""Strictly causal feature helpers for dual-engine signals (rolling / shifted only; nothing centered, nothing full-sample)."""
from __future__ import annotations
import numpy as np
import pandas as pd

ANN = np.sqrt(252)


def realized_vol(ret: pd.Series, window: int = 21) -> pd.Series:
    """Annualised close-to-close realised volatility over the trailing window (in vol points, e.g. 0.16)."""
    return ret.rolling(window, min_periods=window).std(ddof=1) * ANN


def ewma_vol(ret: pd.Series, halflife: float = 10.0, min_periods: int = 20) -> pd.Series:
    return ret.ewm(halflife=halflife, min_periods=min_periods).std() * ANN


def sma(px: pd.Series, n: int) -> pd.Series:
    return px.rolling(n, min_periods=n).mean()


def ema(px: pd.Series, n: int) -> pd.Series:
    return px.ewm(span=n, min_periods=n, adjust=False).mean()


def momentum(px: pd.Series, n: int, skip: int = 0) -> pd.Series:
    """Trailing total return over n days, optionally skipping the most recent `skip` days."""
    return px.shift(skip) / px.shift(n + skip) - 1


def rsi(px: pd.Series, n: int = 2) -> pd.Series:
    d = px.diff()
    up = d.clip(lower=0).ewm(alpha=1 / n, min_periods=n, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1 / n, min_periods=n, adjust=False).mean()
    rs = up / dn.replace(0, np.nan)
    return 100 - 100 / (1 + rs)


def drawdown_from_high(px: pd.Series, n: int | None = None) -> pd.Series:
    hi = px.cummax() if n is None else px.rolling(n, min_periods=1).max()
    return px / hi - 1


def zscore(x: pd.Series, n: int) -> pd.Series:
    r = x.rolling(n, min_periods=n)
    return (x - r.mean()) / r.std(ddof=1)


def pct_rank(x: pd.Series, n: int) -> pd.Series:
    """Trailing percentile rank of the latest value within the last n observations (0..1)."""
    return x.rolling(n, min_periods=n).apply(lambda a: (a[:-1] < a[-1]).mean(), raw=True)


def vrp(vix_close: pd.Series, ret: pd.Series, window: int = 21) -> pd.Series:
    """Variance-risk-premium proxy: implied (VIX/100) minus trailing realised vol."""
    return vix_close / 100.0 - realized_vol(ret, window)


def vix_term_proxy(vix_close: pd.Series, n: int = 10) -> pd.Series:
    """VIX relative to its trailing mean (>1 = spot vol elevated vs recent norm; proxy for backwardation)."""
    return vix_close / sma(vix_close, n)


def days_since_true(mask: pd.Series) -> pd.Series:
    """Trading days since the condition was last true (0 on the day it is true; NaN before the first true)."""
    idx = pd.Series(np.where(mask.values, np.arange(len(mask)), np.nan), index=mask.index).ffill()
    return pd.Series(np.arange(len(mask)), index=mask.index) - idx


def hysteresis(enter: pd.Series, exit_: pd.Series, initial: bool = False) -> pd.Series:
    """Two-threshold state machine: turn ON when `enter` is true, OFF when `exit_` is true, else hold.
    Both inputs are boolean Series aligned to the same index. Returns a boolean Series (state after each close)."""
    e, x = enter.fillna(False).values, exit_.fillna(False).values
    out = np.empty(len(e), dtype=bool)
    state = initial
    for i in range(len(e)):
        if x[i]:
            state = False
        elif e[i]:
            state = True
        out[i] = state
    return pd.Series(out, index=enter.index)


def min_holding(state: pd.Series, min_days: int) -> pd.Series:
    """Suppress state flips that occur fewer than `min_days` after the previous flip (reduces trade count)."""
    v = state.values.astype(float)
    out = v.copy()
    last_flip = -10**9
    cur = out[0]
    for i in range(1, len(v)):
        if v[i] != cur:
            if i - last_flip >= min_days:
                cur = v[i]; last_flip = i
        out[i] = cur
    return pd.Series(out, index=state.index)
