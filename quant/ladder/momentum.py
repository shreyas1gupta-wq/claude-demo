"""L3 (cross-sectional momentum composite) + L4 (time-series momentum) construction logic.

Monograph: docs/cycles/03-momentum-trend.md (assembling). Registry seats:
config/ladder.yaml L3_momentum_composite (rank blend 12-1 + 6-1 + 52wk-high) and
L4_tsmom_index_gold. Parameters flow from registry grids; defaults here are test values.
Everything uses PAST prices only at each date; no-look-ahead is tested against planted truth
(quant/validation/synthetic.py::momentum_universe) in tests/test_momentum.py — including the
planted Daniel-Moskowitz crash that the crash guard must flag.
"""
from __future__ import annotations

import numpy as np


def trailing_return(prices: np.ndarray, lookback: int, skip: int = 0) -> np.ndarray:
    """P[t-skip] / P[t-lookback] - 1 per stock. prices: (N, T). NaN during warm-up.

    skip: the convention that drops the most recent month (short-term reversal) from the
    formation window — Jegadeesh-Titman's '12-1'. Uses only information through t."""
    N, T = prices.shape
    out = np.full((N, T), np.nan)
    for t in range(lookback, T):
        out[:, t] = prices[:, t - skip] / prices[:, t - lookback] - 1.0
    return out


def pct_52wk_high(prices: np.ndarray, window: int = 252) -> np.ndarray:
    """Price relative to its trailing 52-week high (George-Hwang 2004 variant input)."""
    N, T = prices.shape
    out = np.full((N, T), np.nan)
    for t in range(window - 1, T):
        hi = prices[:, t - window + 1:t + 1].max(axis=1)
        out[:, t] = prices[:, t] / hi
    return out


def cross_rank(x: np.ndarray) -> np.ndarray:
    """Cross-sectional percentile rank per date (axis 0), NaN-safe: rank in [0,1]."""
    N, T = x.shape
    out = np.full((N, T), np.nan)
    for t in range(T):
        col = x[:, t]
        m = ~np.isnan(col)
        if m.sum() < 2:
            continue
        order = col[m].argsort().argsort().astype(float)
        out[m, t] = order / (m.sum() - 1)
    return out


def momentum_composite(prices: np.ndarray, w_12_1: float = 1 / 3, w_6_1: float = 1 / 3,
                       w_52wk: float = 1 / 3, skip: int = 21) -> np.ndarray:
    """The L3 rank blend: equal-weighted cross-sectional ranks of 12-1, 6-1, 52wk-high.

    Fixed near-equal weights per the D11 anti-optimization rule; the registry may sweep the
    blend only on pooled data. Output: composite rank in [0,1] per stock/date."""
    r12 = cross_rank(trailing_return(prices, 252, skip))
    r6 = cross_rank(trailing_return(prices, 126, skip))
    rh = cross_rank(pct_52wk_high(prices))
    num = (w_12_1 * np.nan_to_num(r12) + w_6_1 * np.nan_to_num(r6)
           + w_52wk * np.nan_to_num(rh))
    den = (w_12_1 * ~np.isnan(r12) + w_6_1 * ~np.isnan(r6) + w_52wk * ~np.isnan(rh))
    out = np.where(den > 0, num / np.where(den > 0, den, 1.0), np.nan)
    out[np.isnan(r12) & np.isnan(r6) & np.isnan(rh)] = np.nan
    return out


def wml_monthly_returns(prices: np.ndarray, score: np.ndarray, month: int = 21,
                        q: float = 0.1) -> np.ndarray:
    """Paper winners-minus-losers series for diagnostics: at each month-end, long the top-q
    fraction by score, short the bottom-q, hold one month, equal weight. Formation uses only
    information through the formation date."""
    N, T = prices.shape
    n_m = T // month - 1
    out = np.full(n_m, np.nan)
    for k in range(n_m):
        t0, t1 = (k + 1) * month - 1, (k + 2) * month - 1
        s = score[:, t0]
        m = ~np.isnan(s)
        if m.sum() < 20:
            continue
        lo_cut, hi_cut = np.nanquantile(s[m], q), np.nanquantile(s[m], 1 - q)
        ret = prices[:, t1] / prices[:, t0] - 1.0
        win, lose = ret[m & (score[:, t0] >= hi_cut)], ret[m & (score[:, t0] <= lo_cut)]
        if len(win) and len(lose):
            out[k] = float(win.mean() - lose.mean())
    return out


def tsmom_state(index_prices: np.ndarray, lookback: int = 252, skip: int = 21) -> np.ndarray:
    """L4: sign of the index's trailing 12-1 return, in {-1, +1}; NaN in warm-up.

    A STATE for the trend block (regime confirmation + hedge scheduling), consumed through the
    frozen block budgets — not a standalone trade signal here."""
    p = np.asarray(index_prices, float)
    out = np.full(len(p), np.nan)
    for t in range(lookback, len(p)):
        out[t] = 1.0 if p[t - skip] >= p[t - lookback] else -1.0
    return out


def crash_guard(market_prices: np.ndarray, vol_window: int = 63,
                dd_window: int = 504, min_obs: int = 252) -> np.ndarray:
    """Daniel-Moskowitz panic-state dummy: 1 when the MARKET is (a) in a drawdown vs its
    trailing 2y high AND (b) trailing vol is in its top expanding quartile. In panic states the
    loser leg is an embedded call option on the rebound — the sleeve's crash exposure. The guard
    is REDUCE-ONLY by contract: it may shrink WML sizing, never add.

    Both inputs are trailing/expanding: no look-ahead."""
    from quant.ladder.credit_cycle import expanding_percentile
    from quant.ladder.fast_stress import realized_vol
    p = np.asarray(market_prices, float)
    r = np.concatenate([[np.nan], p[1:] / p[:-1] - 1.0])
    vol = realized_vol(np.nan_to_num(r), window=vol_window)
    vol[:vol_window] = np.nan
    vpct = expanding_percentile(vol, min_obs=min_obs)
    dd = np.full(len(p), np.nan)
    for t in range(dd_window, len(p)):
        dd[t] = 1.0 - p[t] / p[t - dd_window:t + 1].max()
    out = np.full(len(p), np.nan)
    m = ~np.isnan(vpct) & ~np.isnan(dd)
    out[m] = ((dd[m] > 0.10) & (vpct[m] > 0.75)).astype(float)
    return out
