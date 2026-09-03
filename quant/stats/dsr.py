"""Deflated Sharpe Ratio and Minimum Track Record Length (Bailey & Lopez de Prado 2014/2012).

[VERIFY] STATUS (DESIGN §15 item 7, open): the constants below follow the structure recorded in
DESIGN §11.6 / D09 §4, recalled with moderate confidence and NOT yet pinned against the primary
paper. The Monte Carlo calibration study (scripts/run_estimator_validation.py) checks the
implementation empirically: under a true-zero-Sharpe null with N trials, DSR should reject at
~the nominal rate. Until the formula is pinned to the source, treat DSR outputs as a
selection-bias-aware screen, not a precision p-value.

Conventions: SR inputs are per-period (e.g. monthly) Sharpe ratios; T = number of return
observations; skew/kurt are the sample skewness and RAW kurtosis (normal = 3) of the strategy's
per-period returns; N = the CUMULATIVE trial count from research/register/trial-ledger.md —
programmatically supplied, never typed by hand (DESIGN §10 protocol).
"""
from __future__ import annotations

import numpy as np
from scipy.stats import norm

EULER_GAMMA = 0.5772156649015329


def expected_max_sharpe(sr_var_across_trials: float, n_trials: int) -> float:
    """E[max SR] over n_trials zero-true-Sharpe strategies (EVT order-statistic approximation).

    sr_var_across_trials: variance of the estimated SRs across the trials actually run (the
    simplifying approximation used when trials are correlated)."""
    if n_trials <= 1:
        return 0.0
    sd = np.sqrt(max(sr_var_across_trials, 0.0))
    z1 = norm.ppf(1.0 - 1.0 / n_trials)
    z2 = norm.ppf(1.0 - 1.0 / (n_trials * np.e))
    return float(sd * ((1.0 - EULER_GAMMA) * z1 + EULER_GAMMA * z2))


def _sr_std_error(sr: float, T: int, skew: float, kurt: float) -> float:
    """Std error of the estimated SR under non-normal returns (Mertens-style adjustment)."""
    var = (1.0 - skew * sr + (kurt - 1.0) / 4.0 * sr ** 2) / (T - 1)
    return float(np.sqrt(max(var, 1e-12)))


def deflated_sharpe_ratio(sr_hat: float, T: int, skew: float, kurt: float,
                          n_trials: int, sr_var_across_trials: float) -> float:
    """P(true SR > SR*), SR* = expected max SR from selection over n_trials.

    Returns a probability; promotion to Tier A requires t>3 AND DSR>0.5-equivalent evidence
    per DESIGN §11.6 (the operating threshold is pre-registered there, not chosen here)."""
    sr_star = expected_max_sharpe(sr_var_across_trials, n_trials)
    se = _sr_std_error(sr_hat, T, skew, kurt)
    return float(norm.cdf((sr_hat - sr_star) / se))


def min_track_record_length(sr_hat: float, sr_benchmark: float, skew: float, kurt: float,
                            confidence: float = 0.95) -> float:
    """Observations needed before asserting true SR > sr_benchmark at `confidence`.

    Solves T from the SR standard-error formula; returns np.inf when sr_hat <= benchmark."""
    if sr_hat <= sr_benchmark:
        return float("inf")
    z = norm.ppf(confidence)
    num = 1.0 - skew * sr_hat + (kurt - 1.0) / 4.0 * sr_hat ** 2
    return float(1.0 + num * (z / (sr_hat - sr_benchmark)) ** 2)


def census_n(register_path=None) -> int:
    """The trial census's RUNNING TOTAL, read from the register (never hardcoded).

    trial-count.md's contract: any Sharpe-like claim must call deflated_sharpe_ratio with
    n_trials >= this number at claim time (plus the strategy's own sweep cells). This helper
    makes that rule mechanical — callers read the census, they don't remember it.
    """
    import re
    from pathlib import Path
    if register_path is None:
        register_path = Path(__file__).resolve().parents[2] / \
            "research" / "register" / "trial-count.md"
    text = Path(register_path).read_text()
    m = re.search(r"RUNNING TOTAL \(run cells\)\*\* \| \| \*\*(\d+)\*\*", text)
    if not m:
        raise ValueError(f"census RUNNING TOTAL not found in {register_path}")
    return int(m.group(1))
