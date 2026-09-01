"""Value + quality sleeve construction (monograph: docs/cycles/04-value-quality.md, assembling).

Registry seats: the value/quality sleeves of the factor book plus the value-spread state feeding
the valuation_sentiment block (0.10). Parameters come from registry grids; defaults are test
values. PIT discipline is built into the API: book/fundamental inputs enter through a REPORTING
LAG argument, and the test suite demonstrates that ignoring it (lag=0, the classic backtest
cheat) inflates the measured premium — the trap is executable, not prose.
"""
from __future__ import annotations

import numpy as np

from .momentum import cross_rank


def lagged(x: np.ndarray, lag: int) -> np.ndarray:
    """Shift a (N,T) panel right by `lag` periods: at time t you may use x[:, t-lag]."""
    out = np.full_like(np.asarray(x, float), np.nan)
    if lag == 0:
        return np.asarray(x, float).copy()
    out[:, lag:] = x[:, :-lag]
    return out


def value_score(book: np.ndarray, prices: np.ndarray, report_lag: int = 3) -> np.ndarray:
    """Book-to-price rank with the reporting lag respected (PIT rule).

    report_lag: periods between a fiscal snapshot and its public availability (India quarterly
    results lag; grid at call sites). Higher rank = cheaper."""
    bp = lagged(book, report_lag) / np.asarray(prices, float)
    return cross_rank(bp)


def quality_score(profit_obs: np.ndarray, report_lag: int = 3) -> np.ndarray:
    """Profitability rank (the Novy-Marx direction), reporting lag respected."""
    return cross_rank(lagged(profit_obs, report_lag))


def vq_composite(v_rank: np.ndarray, q_rank: np.ndarray,
                 w_value: float = 0.5, w_quality: float = 0.5) -> np.ndarray:
    """Fixed near-equal blend (D11 anti-optimization rule) of value and quality ranks."""
    num = w_value * np.nan_to_num(v_rank) + w_quality * np.nan_to_num(q_rank)
    den = w_value * ~np.isnan(v_rank) + w_quality * ~np.isnan(q_rank)
    out = np.where(den > 0, num / np.where(den > 0, den, 1.0), np.nan)
    out[np.isnan(v_rank) & np.isnan(q_rank)] = np.nan
    return out


def value_spread(book: np.ndarray, prices: np.ndarray, report_lag: int = 3,
                 q: float = 0.2) -> np.ndarray:
    """The value-spread STATE: log(B/P of the cheap quintile / B/P of the expensive quintile)
    per date. A dispersion gauge for the valuation_sentiment block — wide spread = the market is
    paying up for glamour = historically value's best forward years (Cohen-Polk-Vuolteenaho).
    Consumed as an expanding percentile at the call site; NEVER a standalone timing trade."""
    bp = lagged(book, report_lag) / np.asarray(prices, float)
    N, T = bp.shape
    out = np.full(T, np.nan)
    for t in range(T):
        col = bp[:, t]
        col = col[~np.isnan(col) & (col > 0)]
        if len(col) < 25:
            continue
        cheap = np.quantile(col, 1 - q)
        rich = np.quantile(col, q)
        if rich > 0:
            out[t] = float(np.log(cheap / rich))
    return out
