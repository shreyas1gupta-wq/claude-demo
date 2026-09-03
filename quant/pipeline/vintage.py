"""Vintage-stamped series — the anti-lookahead primitive the pipeline design requires.

Macro and fundamental data get REVISED; a backtest that reads today's revised history has
already cheated. A VintageSeries stores (obs_date, as_of_date, value) triples and serves
only what was knowable at a given view date. The pipeline-v2 digest's rule ("weld
vintage-stamping into the final Transform") starts here.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


class VintageSeries:
    def __init__(self):
        self._rows: list[tuple[pd.Timestamp, pd.Timestamp, float]] = []

    def record(self, obs_date, as_of, value: float) -> None:
        """Append one vintage observation: `value` for `obs_date`, published at `as_of`."""
        self._rows.append((pd.Timestamp(obs_date), pd.Timestamp(as_of), float(value)))

    def asof(self, view_date) -> pd.Series:
        """The series as an observer on `view_date` would have seen it.

        For each obs_date, the LATEST value whose as_of <= view_date; obs_dates with no
        publication yet are absent entirely.
        """
        view = pd.Timestamp(view_date)
        best: dict[pd.Timestamp, tuple[pd.Timestamp, float]] = {}
        for obs, aso, val in self._rows:
            if aso <= view and (obs not in best or aso >= best[obs][0]):
                best[obs] = (aso, val)
        if not best:
            return pd.Series(dtype=float)
        idx = sorted(best)
        return pd.Series([best[d][1] for d in idx], index=pd.DatetimeIndex(idx))

    def final(self) -> pd.Series:
        """The fully-revised series (backtest use FORBIDDEN by convention; for diagnostics)."""
        return self.asof(pd.Timestamp.max)
