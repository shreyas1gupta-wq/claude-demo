"""tau_half estimation — the ladder's ordering statistic (CONTRACT §4).

tau_half = ln(0.5) / ln(rho) in the sampling frequency's periods, from an AR(1) fit with the
classical first-order small-sample bias correction:

    E[rho_hat] - rho ~= -(1 + 3*rho)/T        (Kendall 1954; Marriott & Pope 1954)
    => rho_corrected = rho_hat + (1 + 3*rho_hat)/T   (plug-in form)

Near the unit root (rho_hat > 0.9) the first-order correction under-corrects — flagged in the
result; the data phase substitutes Andrews (1993) exact median-unbiased estimation there
(DESIGN §11.2). Confidence intervals via a moving-block bootstrap over the series itself.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np


def ar1_ols(y: np.ndarray) -> float:
    """OLS AR(1) coefficient with intercept."""
    y = np.asarray(y, dtype=float)
    x, target = y[:-1], y[1:]
    X = np.column_stack([np.ones(len(x)), x])
    beta, *_ = np.linalg.lstsq(X, target, rcond=None)
    return float(beta[1])


def kendall_corrected_rho(rho_hat: float, T: int) -> float:
    return rho_hat + (1.0 + 3.0 * rho_hat) / T


def _tau_from_rho(rho: float) -> float:
    if rho <= 0.0:
        return 0.0
    if rho >= 1.0:
        return np.inf
    return float(np.log(0.5) / np.log(rho))


@dataclass
class TauHalfResult:
    rho_naive: float
    rho_corrected: float
    tau_half: float                 # periods, corrected
    tau_half_naive: float
    ci_low: float
    ci_high: float
    n_obs: int
    near_unit_root: bool            # rho_corrected > 0.9 -> Andrews method required (data phase)


def estimate_tau_half(y, n_boot: int = 400, ci: float = 0.90, seed: int = 0) -> TauHalfResult:
    """Bias-corrected tau_half with a PARAMETRIC pivot-bootstrap CI.

    METHOD HISTORY (Track R6 Monte Carlo, 2026-08-31): the first implementation used a
    moving-block bootstrap of the observed series for the CI; MC1 showed its 90% intervals
    covering the truth as little as 0-7% of the time at rho >= 0.9 (block resampling of LEVELS
    chops persistence at block joins, biasing resampled rho down and centering the interval
    wrong). Replaced with the standard parametric pivot: simulate AR(1) at rho_corrected,
    re-estimate with the same corrected estimator, and reflect the estimator's simulated
    deviations around rho_corrected. Near the unit root coverage still degrades (documented in
    research/montecarlo/RESULTS.md) — Andrews (1993) exact median-unbiased estimation remains
    the data-phase substitute there (DESIGN §11.2)."""
    from quant.validation.synthetic import ar1_series

    y = np.asarray(y, dtype=float)
    T = len(y)
    rho_hat = ar1_ols(y)
    rho_c = min(kendall_corrected_rho(rho_hat, T), 0.9999)
    draws = np.empty(n_boot)
    for b in range(n_boot):
        sim = ar1_series(max(rho_c, 0.0), T, seed=seed * 1_000_003 + b)
        draws[b] = min(kendall_corrected_rho(ar1_ols(sim), T), 0.9999)
    alpha = (1 - ci) / 2
    lo_star, hi_star = np.quantile(draws, [alpha, 1 - alpha])
    rho_lo = float(np.clip(2 * rho_c - hi_star, 1e-6, 0.9999))
    rho_hi = float(np.clip(2 * rho_c - lo_star, 1e-6, 0.9999))
    return TauHalfResult(
        rho_naive=rho_hat,
        rho_corrected=rho_c,
        tau_half=_tau_from_rho(rho_c),
        tau_half_naive=_tau_from_rho(max(rho_hat, 1e-6)),
        ci_low=_tau_from_rho(rho_lo), ci_high=_tau_from_rho(rho_hi),
        n_obs=T,
        near_unit_root=rho_c > 0.9,
    )
