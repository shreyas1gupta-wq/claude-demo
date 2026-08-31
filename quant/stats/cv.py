"""Purged, embargoed K-fold cross-validation (Lopez de Prado 2018, ch. 7; DESIGN §11.8).

- PURGE: drop any training observation whose LABEL WINDOW [t, t + horizon] overlaps a test
  observation's label window (forward-looking labels leak across a naive split).
- EMBARGO: additionally drop training observations within `embargo` periods AFTER each test
  fold (serial dependence leaks even without label overlap). Embargo >= 1 x tau_half of the
  signal (2x for Tier B/C) — the caller passes it from the registry; this module never chooses it.
- Fold count: 4-6 for India-only monthly series (~380 obs), NOT a textbook 10 (DESIGN §11.8).
"""
from __future__ import annotations

from typing import Iterator

import numpy as np


def purged_kfold(n: int, n_folds: int, label_horizon: int,
                 embargo: int) -> Iterator[tuple[np.ndarray, np.ndarray]]:
    """Yield (train_idx, test_idx) pairs over range(n), contiguous test folds.

    Observation i is assumed to carry a label over [i, i + label_horizon].
    """
    if n_folds < 2:
        raise ValueError("n_folds >= 2")
    bounds = np.linspace(0, n, n_folds + 1, dtype=int)
    for k in range(n_folds):
        t0, t1 = bounds[k], bounds[k + 1]          # test = [t0, t1)
        test = np.arange(t0, t1)
        train_mask = np.ones(n, dtype=bool)
        train_mask[t0:t1] = False
        # purge: train i with label window [i, i+h] overlapping [t0, t1 - 1 + h]
        purge_lo = max(0, t0 - label_horizon)
        purge_hi = min(n, t1 + label_horizon)       # labels of test reach t1 - 1 + h
        train_mask[purge_lo:purge_hi] = False
        # embargo: after the test fold
        emb_hi = min(n, t1 + label_horizon + embargo)
        train_mask[t1:emb_hi] = False
        yield np.nonzero(train_mask)[0], test


def assert_no_leakage(train_idx: np.ndarray, test_idx: np.ndarray,
                      label_horizon: int, embargo: int) -> None:
    """Property check used by the tests and by any harness embedding this CV."""
    t0, t1 = test_idx.min(), test_idx.max()
    for i in train_idx:
        assert not (i <= t1 and i + label_horizon >= t0), f"label overlap at train index {i}"
        assert not (t1 < i <= t1 + label_horizon + embargo), f"embargo violated at {i}"
