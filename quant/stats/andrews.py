"""Andrews (1993)-style median-unbiased AR(1) — the near-unit-root remedy.

estimate_tau_half (tau_half.py) documents its own limit: Kendall's analytic correction and
the parametric-pivot CI degrade as rho -> 1 (MC1). Andrews' exact median-unbiased idea:
the OLS estimator's MEDIAN as a function of the true rho is monotone, so invert it —
find the rho whose simulated median-OLS equals the observed OLS estimate. Implemented by
simulation (the exact tables assume Gaussian AR(1); simulation reproduces them and states
its seed), on a rho grid spanning the near-unit-root zone, with monotone interpolation.

Scope honesty: this corrects the POINT estimate's median bias; interval coverage at the
unit root remains hard everywhere (documented in Andrews' own tables) — the CI here is the
simulated central interval of the estimator at rho_mu, labeled as such. Use when
estimate_tau_half flags near_unit_root; below rho ~0.9 the Kendall path is cheaper and fine.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from quant.stats.tau_half import _tau_from_rho, ar1_ols
from quant.validation.synthetic import ar1_series


@dataclass(frozen=True)
class AndrewsResult:
    rho_mu: float          # median-unbiased rho
    tau_half: float        # periods, from rho_mu
    ci_low_rho: float      # simulated central interval of the estimator AT rho_mu
    ci_high_rho: float
    tau_ci_low: float
    tau_ci_high: float
    grid_edge: bool        # True if the inversion hit the grid boundary (report, don't trust)


def median_unbiased_rho(rho_hat: float, T: int, grid=None, n_sim: int = 300,
                        ci: float = 0.90, seed: int = 0) -> AndrewsResult:
    """Invert the simulated median function m(rho) = median(OLS rho_hat | rho, T)."""
    if grid is None:
        grid = np.concatenate([np.linspace(0.90, 0.99, 10), np.linspace(0.992, 0.9995, 8)])
    grid = np.asarray(grid, float)
    med = np.empty(len(grid))
    for j, rho in enumerate(grid):
        draws = [ar1_ols(ar1_series(rho, T, seed=seed * 7_919 + j * 104_729 + b))
                 for b in range(n_sim)]
        med[j] = float(np.median(draws))
    order = np.argsort(med)
    med_s, grid_s = med[order], grid[order]
    edge = not (med_s[0] <= rho_hat <= med_s[-1])
    rho_mu = float(np.interp(rho_hat, med_s, grid_s))
    # estimator spread AT rho_mu -> central interval mapped through the inversion
    draws = np.array([ar1_ols(ar1_series(rho_mu, T, seed=seed * 15_485_863 + b))
                      for b in range(n_sim)])
    a = (1 - ci) / 2
    lo_hat, hi_hat = np.quantile(draws, [a, 1 - a])
    rho_lo = float(np.interp(lo_hat, med_s, grid_s))
    rho_hi = float(np.interp(hi_hat, med_s, grid_s))
    return AndrewsResult(rho_mu=rho_mu, tau_half=_tau_from_rho(rho_mu),
                         ci_low_rho=rho_lo, ci_high_rho=rho_hi,
                         tau_ci_low=_tau_from_rho(rho_lo), tau_ci_high=_tau_from_rho(rho_hi),
                         grid_edge=edge)
