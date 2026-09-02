"""L5 calendar-window scheduler vs exact planted truth.

Deterministic module — the truth is planted by construction (a hand-built monthly index
with known elections), so assertions are exact; no stochastic fixture or seed sweep."""
import numpy as np
import pandas as pd
import pytest

from quant.ladder import calendar_schedule, windows

MONTHS = pd.period_range("2003-01", "2005-12", freq="M").to_timestamp()
ELECTION = ["2004-05"]  # the 2004 result month — the canonical direction-surprise case


def test_budget_windows_are_every_february_and_only_february():
    in_w, n, kinds = calendar_schedule(MONTHS)
    flagged = {str(pd.Period(m, freq="M")) for m, f in zip(MONTHS, in_w) if f}
    assert flagged == {"2003-02", "2004-02", "2005-02"}
    assert all(k == ("budget",) for m, k in zip(MONTHS, kinds) if pd.Timestamp(m).month == 2)
    assert n.max() == 1


def test_election_window_spans_pre2_post1_with_trail():
    in_w, n, kinds = calendar_schedule(MONTHS, ELECTION)
    flagged = {str(pd.Period(m, freq="M")) for m, f in zip(MONTHS, in_w)
               if f and pd.Timestamp(m).month != 2}
    assert flagged == {"2004-03", "2004-04", "2004-05", "2004-06"}
    i_may = list(pd.PeriodIndex(MONTHS, freq="M").astype(str)).index("2004-05")
    assert kinds[i_may] == ("election",)


def test_overlap_counts_depth_not_just_flag():
    in_w, n, kinds = calendar_schedule(MONTHS, ["2003-03"])  # window covers Jan-Apr 2003
    i_feb = 1  # 2003-02
    assert in_w[i_feb] and n[i_feb] == 2 and set(kinds[i_feb]) == {"budget", "election"}


def test_events_outside_range_ignored_nothing_extrapolated():
    in_w, n, _ = calendar_schedule(MONTHS, ["1999-10", "2009-05"])
    assert n.sum() == 3  # only the three Februaries — no invented future/past elections


def test_window_objects_carry_trail():
    ws = windows(MONTHS, ELECTION)
    kinds = [w.kind for w in ws]
    assert kinds.count("budget") == 3 and kinds.count("election") == 1
    e = [w for w in ws if w.kind == "election"][0]
    assert str(e.anchor) == "2004-05" and str(e.start) == "2004-03" and str(e.end) == "2004-06"


def test_unsorted_months_rejected():
    bad = list(MONTHS[::-1])
    with pytest.raises(ValueError):
        calendar_schedule(bad)


def test_no_directional_output_exists():
    import quant.ladder.calendar_windows as m
    banned = [a for a in dir(m) if any(t in a.lower() for t in ("direction", "signal", "tilt"))]
    assert banned == []  # the seat schedules; it never points
