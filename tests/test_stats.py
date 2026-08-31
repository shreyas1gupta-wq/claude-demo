"""Estimator tests against synthetic ground truth + the no-look-ahead property test."""
import numpy as np
import pytest

from quant.stats import (ar1_ols, estimate_tau_half, hamilton_filter, kendall_corrected_rho,
                         max_drawdown, purged_kfold, stationary_bootstrap,
                         deflated_sharpe_ratio, expected_max_sharpe, min_track_record_length)
from quant.stats.cv import assert_no_leakage
from quant.validation import ar1_series, regime_vol_returns, trend_plus_cycle


# ---------------- tau_half ----------------

def test_ar1_ols_recovers_rho():
    y = ar1_series(rho=0.8, T=5000, seed=1)
    assert abs(ar1_ols(y) - 0.8) < 0.03


def test_kendall_correction_reduces_bias():
    """At India-like T (~380), the naive AR(1) rho is biased down; the correction must shrink
    the bias in expectation (Monte Carlo over 200 draws)."""
    rho, T, n = 0.9, 380, 200
    naive, corrected = [], []
    for s in range(n):
        y = ar1_series(rho, T, seed=s)
        r = ar1_ols(y)
        naive.append(r)
        corrected.append(kendall_corrected_rho(r, T))
    bias_naive = abs(np.mean(naive) - rho)
    bias_corr = abs(np.mean(corrected) - rho)
    assert bias_corr < bias_naive


def test_tau_half_flags_near_unit_root():
    y = ar1_series(0.97, 380, seed=3)
    res = estimate_tau_half(y, n_boot=100)
    assert res.near_unit_root
    assert res.ci_low < res.tau_half


# ---------------- Hamilton filter ----------------

def test_hamilton_full_recovers_cycle_direction():
    y, true_cycle = trend_plus_cycle(T=800, cycle_rho=0.9, seed=5)
    c = hamilton_filter(y, h=8, p=4, mode="full")
    m = ~np.isnan(c)
    corr = np.corrcoef(c[m], true_cycle[m])[0, 1]
    assert corr > 0.5, f"filter should track the true cycle, corr={corr:.2f}"


def test_hamilton_expanding_no_lookahead():
    """The mandatory property test (Appendix B): recomputing on data truncated at t must
    reproduce the stored value at t exactly, at every sampled t."""
    y, _ = trend_plus_cycle(T=400, seed=7)
    full = hamilton_filter(y, h=8, p=4, mode="expanding")
    rng = np.random.default_rng(0)
    for t in rng.integers(120, 400, size=12):
        trunc = hamilton_filter(y[: t + 1], h=8, p=4, mode="expanding")
        if not np.isnan(full[t]):
            assert full[t] == pytest.approx(trunc[t], abs=1e-10), f"look-ahead at t={t}"


def test_hamilton_on_white_noise_manufactures_no_persistence():
    """Slutzky guard: the filter must not create strong spurious autocorrelation from noise."""
    rng = np.random.default_rng(11)
    y = rng.normal(size=2000)
    c = hamilton_filter(y, h=8, p=4, mode="full")
    c = c[~np.isnan(c)]
    ac1 = np.corrcoef(c[:-1], c[1:])[0, 1]
    assert abs(ac1) < 0.15


# ---------------- purged CV ----------------

def test_purged_kfold_no_leakage():
    for train, test in purged_kfold(n=380, n_folds=5, label_horizon=12, embargo=24):
        assert_no_leakage(train, test, label_horizon=12, embargo=24)
        assert len(test) > 0 and len(train) > 0


def test_purged_kfold_removes_more_than_naive():
    naive_train = 380 - 380 // 5
    for train, _ in purged_kfold(380, 5, label_horizon=12, embargo=24):
        assert len(train) < naive_train


# ---------------- bootstrap / drawdown ----------------

def test_max_drawdown_known_path():
    r = np.array([0.10, -0.50, 0.20])   # nav: 1.10, 0.55, 0.66 -> maxDD = 0.50
    assert max_drawdown(r) == pytest.approx(0.50, abs=1e-12)


def test_block_bootstrap_preserves_dependence_structure():
    """What block resampling actually buys (MC3 finding, 2026-08-31): it preserves the series'
    own autocorrelation; iid resampling destroys it. (The naive claim 'iid always understates
    DD tails' was FALSIFIED by our own Monte Carlo for pure vol clustering — direction there is
    seed-dependent; see research/montecarlo/RESULTS.md.)"""
    from quant.validation import ar1_series
    r = 0.01 * ar1_series(0.15, 2500, seed=4)

    def acf1(x):
        return np.corrcoef(x[:-1], x[1:])[0, 1]

    orig = acf1(r)
    blk = stationary_bootstrap(r, 50, mean_block=40, seed=1)
    iid = stationary_bootstrap(r, 50, mean_block=1.0000001, seed=2)
    assert abs(np.mean([acf1(s) for s in blk]) - orig) < 0.05
    assert abs(np.mean([acf1(s) for s in iid])) < 0.05  # iid kills the dependence


def test_block_bootstrap_dd_tail_deeper_when_returns_autocorrelated():
    """Where theory is unambiguous — genuinely autocorrelated returns (stress regimes, trending
    declines: the episodes the ceiling is checked against) — block resampling produces the
    deeper, honest DD tail. Verified 8/8 seeds in the R6 diagnostic; pinned here on one."""
    from quant.validation import ar1_series
    r = 0.0003 + 0.01 * ar1_series(0.15, 2500, seed=4)
    dd_block = np.quantile([max_drawdown(s) for s in
                            stationary_bootstrap(r, 200, mean_block=40, seed=15)], 0.95)
    dd_iid = np.quantile([max_drawdown(s) for s in
                          stationary_bootstrap(r, 200, mean_block=1.0000001, seed=15)], 0.95)
    assert dd_block > dd_iid


def test_stationary_bootstrap_shape_and_values():
    x = np.arange(100.0)
    s = stationary_bootstrap(x, 5, mean_block=10, seed=0)
    assert s.shape == (5, 100)
    assert set(np.unique(s)).issubset(set(x))


# ---------------- DSR / MinTRL ----------------

def test_expected_max_sharpe_monotone_in_trials():
    v = 0.01
    assert expected_max_sharpe(v, 1) == 0.0
    assert expected_max_sharpe(v, 28) > expected_max_sharpe(v, 9) > 0


def test_dsr_increases_with_T_and_decreases_with_trials():
    kw = dict(sr_hat=0.3, skew=0.0, kurt=3.0, sr_var_across_trials=0.01)
    assert deflated_sharpe_ratio(T=240, n_trials=1, **kw) > deflated_sharpe_ratio(T=60, n_trials=1, **kw)
    assert deflated_sharpe_ratio(T=240, n_trials=1, **kw) > deflated_sharpe_ratio(T=240, n_trials=252, **kw)


def test_mintrl_sobering_at_realistic_sharpe():
    """The §7 capital-plan honesty check: monthly SR ~0.29 (annual ~1.0) vs zero benchmark needs
    on the order of years of monthly observations, not months."""
    t = min_track_record_length(sr_hat=0.29, sr_benchmark=0.0, skew=0.0, kurt=3.0)
    assert 20 < t < 60   # months: ~2-5 years
    assert min_track_record_length(0.29, 0.29, 0.0, 3.0) == float("inf")
