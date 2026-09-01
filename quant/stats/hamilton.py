"""Hamilton (2018) regression filter — the CONTRACT-mandated replacement for the banned HP filter.

Hamilton, "Why You Should Never Use the Hodrick-Prescott Filter", REStat 100(5), 2018:
regress y_{t+h} on a constant and the p most recent values of y as of date t; the residual is the
cyclical component. Two modes:

- mode="full":       one OLS fit on the whole sample (Hamilton's own illustration). Fine for
                     historical characterization; NOT usable as a live signal (coefficients see
                     the future).
- mode="expanding":  at each date t the regression is re-fit using only data available through t.
                     This is the only mode admissible inside a tradable state variable — it is
                     what the no-look-ahead property test (tests/test_noleak.py) certifies.

h and p come from config/ladder.yaml band settings via the registry — never hardcoded by callers.
"""
from __future__ import annotations

import numpy as np


def _design(y: np.ndarray, h: int, p: int):
    """Rows: t index such that y[t+h] is the target and y[t], y[t-1], ..., y[t-p+1] regressors."""
    n = len(y)
    t_idx = np.arange(p - 1, n - h)          # t where all lags and the target exist
    X = np.column_stack([np.ones(len(t_idx))] +
                        [y[t_idx - j] for j in range(p)])
    target = y[t_idx + h]
    return t_idx, X, target


def hamilton_filter(y, h: int, p: int, mode: str = "expanding",
                    min_obs: int | None = None) -> np.ndarray:
    """Return the cyclical component aligned to the TARGET date (t+h).

    Output c has len(y); c[s] is the cycle estimate for date s (= y[s] - forecast made at s-h),
    NaN where undefined. min_obs: minimum regression observations before an expanding-mode
    estimate is emitted (default: 5 * (p + 1) — a coefficient-stability floor, not a tuning knob).
    """
    y = np.asarray(y, dtype=float)
    n = len(y)
    if min_obs is None:
        min_obs = 5 * (p + 1)
    t_idx, X, target = _design(y, h, p)
    cycle = np.full(n, np.nan)
    # NaN robustness (real series have leading gaps and war holes): a regression row is usable
    # only when its target and all its regressors are finite; unusable rows are excluded from
    # every fit and get NaN cycle values. Discovered the hard way on the JST panel (2026-09-01).
    row_ok = np.isfinite(target) & np.all(np.isfinite(X), axis=1)

    if mode == "full":
        if row_ok.sum() >= min_obs:
            beta, *_ = np.linalg.lstsq(X[row_ok], target[row_ok], rcond=None)
            cycle[t_idx[row_ok] + h] = target[row_ok] - X[row_ok] @ beta
        return cycle

    if mode != "expanding":
        raise ValueError(f"unknown mode {mode!r}")

    n_ok = np.cumsum(row_ok)
    for i in range(len(t_idx)):
        # fit on regressions whose TARGET date is <= current target date (info through s = t+h)
        if not row_ok[i] or n_ok[i] < min_obs:
            continue
        sel = row_ok[: i + 1]
        beta, *_ = np.linalg.lstsq(X[: i + 1][sel], target[: i + 1][sel], rcond=None)
        s = t_idx[i] + h
        cycle[s] = target[i] - X[i] @ beta
    return cycle
