"""Classification metrics for state-vs-episode evaluation.

auroc() existed as a script-local helper (analyze_jst_panel.py, and a rank construction
inside the F2-index grid); third use promotes it here per process note #6 — estimation
code lives in quant/stats, scripts only call it.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def auroc(score: np.ndarray, label: np.ndarray) -> float:
    """Area under the ROC curve via the rank (Mann-Whitney) identity.

    NaNs in either input drop the pair; degenerate labels (one class absent) return NaN
    rather than a fake 0.5 — the caller must see that the evaluation was impossible.
    """
    score = np.asarray(score, float)
    label = np.asarray(label, float)
    m = ~np.isnan(score) & ~np.isnan(label)
    s, y = score[m], label[m].astype(bool)
    if y.sum() == 0 or (~y).sum() == 0:
        return float("nan")
    r = pd.Series(s).rank().to_numpy()
    n1, n0 = int(y.sum()), int((~y).sum())
    return float((r[y].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))
