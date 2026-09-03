"""auroc: planted-truth checks."""
import numpy as np

from quant.stats.metrics import auroc


def test_perfect_and_inverted_separation():
    score = np.array([0.1, 0.2, 0.3, 0.8, 0.9, 1.0])
    label = np.array([0, 0, 0, 1, 1, 1])
    assert auroc(score, label) == 1.0
    assert auroc(-score, label) == 0.0


def test_uninformative_is_half():
    rng = np.random.default_rng(0)
    score = rng.normal(size=4000)
    label = rng.integers(0, 2, size=4000)
    assert abs(auroc(score, label) - 0.5) < 0.03


def test_nan_pairs_dropped_and_degenerate_is_nan():
    score = np.array([1.0, np.nan, 3.0, 4.0])
    label = np.array([0, 1, np.nan, 1])
    assert auroc(score, label) == 1.0          # only rows 0 and 3 survive
    assert np.isnan(auroc(np.array([1.0, 2.0]), np.array([1, 1])))
