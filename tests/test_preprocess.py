"""Planted-truth tests: winsorization bounds come from train only (process note #8)."""
import numpy as np
import pandas as pd

from quant.stats.preprocess import winsor_bounds, winsorize


def test_bounds_come_from_train_only():
    train = pd.Series(np.linspace(0.0, 1.0, 101))          # 1%/99% at 0.01 / 0.99
    bounds = winsor_bounds(train)
    assert abs(bounds[0] - 0.01) < 1e-9 and abs(bounds[1] - 0.99) < 1e-9
    # a test set with a huge outlier: clipped at TRAIN's bound, not its own quantile
    test = pd.Series([0.5, 50.0, -50.0])
    out = winsorize(test, bounds)
    assert out.iloc[1] == bounds[1] and out.iloc[2] == bounds[0]
    assert out.iloc[0] == 0.5                                # interior values untouched


def test_apply_never_reestimates():
    bounds = (-1.0, 1.0)
    s = pd.Series([-5.0, 0.0, 5.0])
    assert list(winsorize(s, bounds)) == [-1.0, 0.0, 1.0]
