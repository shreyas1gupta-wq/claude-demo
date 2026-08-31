"""Seeded synthetic generators with KNOWN ground truth — the estimator-validation fixtures.

Purpose (Track R6): before any estimator touches Indian data, it must demonstrably recover known
parameters on synthetic data at India-like sample sizes (~380 monthly obs). These generators are
the ground truth for tests/ and scripts/run_estimator_validation.py.
"""
from __future__ import annotations

import numpy as np


def ar1_series(rho: float, T: int, sigma: float = 1.0, seed: int = 0,
               burn: int = 200) -> np.ndarray:
    """Stationary AR(1) with known rho (true tau_half = ln(.5)/ln(rho)).

    Vectorized via scipy.signal.lfilter with a burn-in for stationarity — the parametric
    bootstrap in quant.stats.tau_half simulates thousands of these."""
    from scipy.signal import lfilter
    rng = np.random.default_rng(seed)
    eps = rng.normal(0.0, sigma, T + burn)
    y = lfilter([1.0], [1.0, -rho], eps)
    return y[burn:]


def regime_vol_returns(T: int, seed: int = 0, p_calm_to_stress: float = 0.02,
                       p_stress_to_calm: float = 0.10, mu: float = 0.0004,
                       sigma_calm: float = 0.008, sigma_stress: float = 0.028,
                       stress_drift: float = -0.002) -> np.ndarray:
    """Two-state volatility-clustered daily returns (calm/stress persistence) — used to
    demonstrate that iid bootstrap understates drawdown tails vs the block bootstrap.
    Ground truth: stress episodes have mean length 1/p_stress_to_calm days."""
    rng = np.random.default_rng(seed)
    r = np.empty(T)
    stress = False
    for t in range(T):
        if stress:
            r[t] = rng.normal(stress_drift, sigma_stress)
            stress = rng.random() > p_stress_to_calm
        else:
            r[t] = rng.normal(mu, sigma_calm)
            stress = rng.random() < p_calm_to_stress
    return r


def trend_plus_cycle(T: int, cycle_rho: float = 0.9, trend: float = 0.01,
                     sigma_cycle: float = 1.0, seed: int = 0):
    """Random-walk-with-drift trend + known AR(1) cycle; returns (y, true_cycle) for
    Hamilton-filter recovery tests."""
    rng = np.random.default_rng(seed)
    cyc = ar1_series(cycle_rho, T, sigma_cycle, seed=seed + 1)
    tr = np.cumsum(trend + rng.normal(0, 0.2, T))
    return tr + cyc, cyc


def boom_bust_economy(T: int = 480, seed: int = 7) -> dict:
    """Monthly synthetic economy with a KNOWN credit boom and bust (the L10 fixture).

    Income grows steadily; credit grows WITH income except a boom (months 200-320: credit
    outgrows income by 60bps/mo) then a bust (320-400: credit growth 70bps/mo below income).
    Deposits track income, so the credit-deposit ratio rises through the boom and unwinds
    after it. Ground truth: boom=(200, 320), bust=(320, 400), returned alongside the series."""
    rng = np.random.default_rng(seed)
    g_income = 0.005 + 0.002 * rng.standard_normal(T)
    income = 100 * np.cumprod(1 + g_income)
    g_credit = g_income.copy()
    g_credit[200:320] += 0.006            # boom: credit outgrows income
    g_credit[320:400] -= 0.007            # bust: credit contracts vs income
    credit = 80 * np.cumprod(1 + g_credit + 0.001 * rng.standard_normal(T))
    deposits = 110 * np.cumprod(1 + g_income + 0.0005 * rng.standard_normal(T))
    return dict(income=income, credit=credit, deposits=deposits,
                boom=(200, 320), bust=(320, 400))
