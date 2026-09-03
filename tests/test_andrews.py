"""Andrews median-unbiased AR(1) vs Monte Carlo truth near the unit root."""
import numpy as np

from quant.stats.andrews import median_unbiased_rho
from quant.stats.tau_half import ar1_ols, kendall_corrected_rho
from quant.validation.synthetic import ar1_series

RHO_TRUE, T = 0.985, 800
SEEDS = (0, 1, 2)   # first three, no curation (house rule)


def _estimates():
    rows = []
    for s in SEEDS:
        y = ar1_series(RHO_TRUE, T, seed=1_000 + s)
        hat = ar1_ols(y)
        rows.append((hat, kendall_corrected_rho(hat, T),
                     median_unbiased_rho(hat, T, n_sim=120, seed=s)))
    return rows


def test_median_unbiased_beats_ols_bias_near_unit_root():
    rows = _estimates()
    ols_err = np.mean([abs(h - RHO_TRUE) for h, _, _ in rows])
    and_err = np.mean([abs(r.rho_mu - RHO_TRUE) for _, _, r in rows])
    assert and_err < ols_err          # the correction must reduce, not shuffle, the bias
    assert all(r.rho_mu > h for h, _, r in rows)   # OLS biases DOWN here; correction is up


def test_interval_brackets_truth_and_edges_flagged():
    rows = _estimates()
    hits = sum(r.ci_low_rho <= RHO_TRUE <= r.ci_high_rho for _, _, r in rows)
    assert hits >= 2                  # 90% interval, 3 seeds: at least 2 must bracket
    assert all(not r.grid_edge for _, _, r in rows)


def test_grid_edge_reported_not_hidden():
    r = median_unbiased_rho(0.10, T, n_sim=60, seed=0)   # far below the grid
    assert r.grid_edge is True
