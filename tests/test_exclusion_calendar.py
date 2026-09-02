"""H58 ops-pack calendars vs exact planted truth (deterministic — no fixtures)."""
import numpy as np
import pandas as pd
import pytest

from quant.ladder import (drain_window_mask, expiry_days, results_pause_mask,
                          statutory_drain_dates)


def test_statutory_dates_are_4_plus_12():
    d = statutory_drain_dates(2024)
    assert len(d) == 16
    assert pd.Timestamp(2024, 6, 15) in d and pd.Timestamp(2024, 3, 15) in d
    assert sum(1 for x in d if x.day == 20) == 12


def test_drain_window_flags_around_advance_tax_date():
    # Jun 15 2023 is a Thursday; pre 2bd = Tue Jun 13, post 1bd = Fri Jun 16
    days = pd.date_range("2023-06-09", "2023-06-23", freq="B")
    m = drain_window_mask(days, pre_bd=2, post_bd=1)
    flagged = {str(d.date()) for d, f in zip(days, m) if f}
    assert {"2023-06-13", "2023-06-14", "2023-06-15", "2023-06-16"} <= flagged
    assert "2023-06-09" not in flagged
    # Jun 20 (GST due, Tuesday) opens its own window: 2bd back = Fri Jun 16
    assert "2023-06-19" in flagged and "2023-06-20" in flagged


def test_drain_mask_never_creates_only_suppresses():
    days = pd.date_range("2023-07-03", "2023-07-07", freq="B")  # no statutory date ±2bd
    assert not drain_window_mask(days).any()


def test_results_pause_flags_crossing_tranches():
    tranches = pd.to_datetime(["2024-01-10", "2024-01-15", "2024-01-25"])
    results = ["2024-01-15"]
    m = results_pause_mask(tranches, results, pre_bd=1, post_bd=1)
    assert list(m) == [False, True, False]
    assert not results_pause_mask(tranches, []).any()


def test_expiry_last_thursday_and_configurable_weekday():
    days = pd.date_range("2024-01-01", "2024-02-29", freq="D")
    thu = expiry_days(days, weekday=3)  # last Thursdays: Jan 25, Feb 29 2024
    got = {str(d.date()) for d, f in zip(days, thu) if f}
    assert got == {"2024-01-25", "2024-02-29"}
    tue = expiry_days(days, weekday=1)  # last Tuesdays: Jan 30, Feb 27 2024
    got_t = {str(d.date()) for d, f in zip(days, tue) if f}
    assert got_t == {"2024-01-30", "2024-02-27"}


def test_expiry_weekday_must_come_from_config():
    days = pd.date_range("2024-01-01", "2024-01-31", freq="D")
    with pytest.raises(TypeError):
        expiry_days(days)  # no default — the 2025 weekday flux makes a default a bug
    with pytest.raises(ValueError):
        expiry_days(days, weekday=6)


def test_no_alpha_surface():
    import quant.ladder.exclusion_calendar as m
    banned = [a for a in dir(m) if any(t in a.lower()
              for t in ("signal", "alpha", "tilt", "direction", "score"))]
    assert banned == []  # ops pack: it excludes and defers; it never recommends
