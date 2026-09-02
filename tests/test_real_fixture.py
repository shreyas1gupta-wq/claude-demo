"""The real-data regression fixture: the L2 chain vs a frozen slice of actual history.

tests/fixtures/nifty_slice_2019_2020.csv is a 491-row cut of the authenticated NIFTY vault
(2019-01..2020-12 — calm, crash, recovery). Golden values were computed ONCE at freeze time
(2026-09-02) on the slice alone (self-contained code path, min_obs=252) and must reproduce
byte-stably forever: any change to realized_vol / drawdown_depth / expanding_percentile /
fast_stress_composite that moves these numbers is a behavior change and must say so.
Synthetic tests prove the machinery on planted truth; this one pins it to the real world:
COVID's floor prints a near-max stress state, mid-recovery prints ~neutral-high, and the
year-end melt-up prints negative (calm) — the shape a human would draw."""
from pathlib import Path

import numpy as np
import pandas as pd

from quant.ladder import expanding_percentile
from quant.ladder.fast_stress import drawdown_depth, fast_stress_composite, realized_vol

FIX = Path(__file__).parent / "fixtures" / "nifty_slice_2019_2020.csv"
GOLDEN = {"2020-03-23": 0.9930228883297475, "2020-06-30": 0.5080611288811347,
          "2020-12-30": -0.4733475479744137}


def _state():
    sl = pd.read_csv(FIX, parse_dates=["Date"])
    r = sl["Close"].pct_change().dropna().values
    rv_p = expanding_percentile(realized_vol(r, 21), min_obs=252)
    dd_p = expanding_percentile(drawdown_depth(r), min_obs=252)
    return sl["Date"].iloc[1:].reset_index(drop=True), fast_stress_composite(rv_p, dd_p)


def test_golden_states_reproduce():
    d, st = _state()
    for day, want in GOLDEN.items():
        i = d[d == day].index[0]
        assert abs(float(st[i]) - want) < 1e-9, f"{day}: {st[i]} != {want}"


def test_real_world_shape():
    d, st = _state()
    covid = float(st[d[d == "2020-03-23"].index[0]])
    yearend = float(st[d[d == "2020-12-30"].index[0]])
    assert covid > 0.9 and yearend < 0    # crash near max stress; melt-up calm
