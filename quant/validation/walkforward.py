"""M4 walk-forward harness (DESIGN M4; CONTRACT §9 purged/embargoed evaluation).

The registered adjudicator for de-risk value ("judged in the M4 walk-forward, never
standalone Sharpe") gets its machinery: expanding-train folds over disjoint test eras with
an embargo gap between train end and test start (embargo scaled to signal half-life by the
caller, per §9). Two deliberate design points:

1. RULES HERE ARE EVALUATED, NEVER FITTED. The ladder's states are expanding/real-time by
   construction and the grids are pre-registered, so a "fold" is a disjoint ERA whose job is
   consistency: does the rule's value hold across independent segments, or was it one
   episode's gift? A rule with fitted parameters must fit on [0, train_end) only — the
   harness hands it that boundary and the embargo enforces the gap.
2. FOLD BOUNDARIES ARE DETERMINISTIC from (n, n_folds, min_train, embargo) — nothing about
   fold placement can be tuned toward a result without the ledger seeing new parameters.

Tests: tests/test_walkforward.py (exact boundary assertions, embargo/overlap properties).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Fold:
    train_end: int    # exclusive: train/history = [0, train_end)
    test_start: int   # inclusive; test_start = train_end + embargo
    test_end: int     # exclusive


def walkforward_folds(n: int, n_folds: int, min_train: int, embargo: int = 0) -> list[Fold]:
    """Split [0, n) into `n_folds` equal disjoint test eras after a burn-in of `min_train`.

    Train is EXPANDING: fold k's history is everything before its test era minus the
    embargo. Raises if the request cannot produce non-empty folds."""
    if n_folds < 1 or min_train < 0 or embargo < 0:
        raise ValueError("n_folds >= 1, min_train >= 0, embargo >= 0 required")
    test_span = n - min_train
    width = test_span // n_folds
    if width <= embargo:
        raise ValueError(f"cannot fit {n_folds} folds of width > embargo={embargo} "
                         f"into {test_span} periods after min_train={min_train}")
    folds = []
    for k in range(n_folds):
        t0 = min_train + k * width
        t1 = n if k == n_folds - 1 else t0 + width
        folds.append(Fold(train_end=t0 - embargo if t0 - embargo > 0 else 0,
                          test_start=t0, test_end=t1))
    return folds


def evaluate_walkforward(folds: list[Fold], metric_fn) -> list[dict]:
    """Run metric_fn(fold) per fold; each result dict gains the fold boundaries.

    metric_fn receives the Fold and returns a dict of metrics for the TEST era only —
    the caller is responsible for using only [0, fold.train_end) information in any
    fitted component (the ladder's expanding states satisfy this by construction)."""
    out = []
    for f in folds:
        m = dict(metric_fn(f))
        m.update(train_end=f.train_end, test_start=f.test_start, test_end=f.test_end)
        out.append(m)
    return out
