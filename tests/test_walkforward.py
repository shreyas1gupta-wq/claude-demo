"""M4 walk-forward harness vs exact planted truth (deterministic)."""
import pytest

from quant.validation.walkforward import Fold, evaluate_walkforward, walkforward_folds


def test_fold_boundaries_exact():
    folds = walkforward_folds(n=100, n_folds=4, min_train=20, embargo=0)
    assert [(f.test_start, f.test_end) for f in folds] == [(20, 40), (40, 60), (60, 80), (80, 100)]
    assert [f.train_end for f in folds] == [20, 40, 60, 80]  # expanding


def test_embargo_gap_enforced():
    folds = walkforward_folds(n=120, n_folds=3, min_train=30, embargo=5)
    for f in folds:
        assert f.test_start - f.train_end == 5 or f.train_end == 0
    assert folds[0] == Fold(train_end=25, test_start=30, test_end=60)


def test_test_eras_disjoint_and_cover_tail():
    folds = walkforward_folds(n=97, n_folds=3, min_train=10, embargo=0)
    spans = [(f.test_start, f.test_end) for f in folds]
    for (a0, a1), (b0, b1) in zip(spans, spans[1:]):
        assert a1 == b0                       # contiguous, no overlap
    assert spans[-1][1] == 97                 # remainder folds into the last era


def test_rejects_impossible_requests():
    with pytest.raises(ValueError):
        walkforward_folds(n=50, n_folds=10, min_train=45, embargo=0)
    with pytest.raises(ValueError):
        walkforward_folds(n=100, n_folds=4, min_train=20, embargo=30)


def test_evaluate_attaches_boundaries_and_orders():
    folds = walkforward_folds(n=40, n_folds=2, min_train=10)
    res = evaluate_walkforward(folds, lambda f: {"width": f.test_end - f.test_start})
    assert [r["width"] for r in res] == [15, 15]
    assert res[0]["test_start"] == 10 and res[1]["test_end"] == 40
