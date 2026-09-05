"""Train-only preprocessing — the anti-lookahead helpers PROCESS NOTE #8 mandates.

Winsorization (and any fitted preprocessing) must estimate its parameters on the TRAINING
information set only and apply them unchanged to test data. The 2026-09-05 ER-battery
audit found full-sample clip bounds inside legs labeled "no-lookahead"; this module makes
the honest pattern the easy pattern.
"""
from __future__ import annotations

import pandas as pd


def winsor_bounds(train: pd.Series, lo: float = 0.01, hi: float = 0.99) -> tuple[float, float]:
    """Clip bounds estimated from `train` ONLY."""
    return float(train.quantile(lo)), float(train.quantile(hi))


def winsorize(s: pd.Series, bounds: tuple[float, float]) -> pd.Series:
    """Apply pre-fitted bounds; never re-estimates from `s`."""
    return s.clip(bounds[0], bounds[1])
