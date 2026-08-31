"""Stationary block bootstrap (Politis & Romano 1994) and drawdown distributions.

Why blocks (DESIGN §11.7): an iid bootstrap of daily returns destroys volatility clustering and
therefore cannot generate runs of consecutive bad days at the empirically observed rate — it
systematically UNDERSTATES tail drawdowns. Mean block length: 2-4 x tau_half of the return
series (registry-supplied), Politis-White plug-in when the sample permits. The 30-35% ceiling is
checked against the 95th/99th percentile of this distribution, never against the point-estimate
historical max.
"""
from __future__ import annotations

import numpy as np


def max_drawdown(returns: np.ndarray) -> float:
    """Max peak-to-trough drawdown of the cumulative (compounded) NAV path. Positive number."""
    nav = np.cumprod(1.0 + np.asarray(returns, dtype=float))
    peak = np.maximum.accumulate(nav)
    return float(np.max(1.0 - nav / peak))


def stationary_bootstrap(x: np.ndarray, n_samples: int, mean_block: float,
                         seed: int = 0) -> np.ndarray:
    """Politis-Romano: geometric block lengths with mean `mean_block`, wrap-around indexing.

    Returns an (n_samples, len(x)) array of resampled series."""
    x = np.asarray(x, dtype=float)
    n = len(x)
    p = 1.0 / mean_block
    rng = np.random.default_rng(seed)
    out = np.empty((n_samples, n))
    for s in range(n_samples):
        idx = np.empty(n, dtype=int)
        t = 0
        while t < n:
            start = rng.integers(0, n)
            length = rng.geometric(p)
            take = min(length, n - t)
            idx[t:t + take] = (start + np.arange(take)) % n
            t += take
        out[s] = x[idx]
    return out


def drawdown_distribution(returns: np.ndarray, n_samples: int = 2000,
                          mean_block: float = 20.0, seed: int = 0) -> np.ndarray:
    """Distribution of max drawdowns across stationary-bootstrap resamples."""
    samples = stationary_bootstrap(returns, n_samples, mean_block, seed)
    return np.array([max_drawdown(s) for s in samples])
