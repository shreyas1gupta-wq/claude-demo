"""H58 — calendar-mechanics ops pack (docs/cycles/34-calendar-mechanics.md, assembling).

EXECUTION rules, not signals: three mechanical calendars that other modules must NOT
mistake for information. No alpha claim exists anywhere in this module (the pre-stated
framing of the H58 block, trial ledger 2026-09-02):

1. STATUTORY DRAIN DATES — system liquidity drains on dates fixed by statute, so funding
   rates spike MECHANICALLY there: advance-tax instalments (Income-tax Act s.211: Jun 15,
   Sep 15, Dec 15, Mar 15) and the monthly GSTR-3B due date (the 20th). L2's funding-stress
   triggers must ignore fires inside these windows (H58-D1 grades the rule once L2 daily
   history exists).
2. RESULTS-DATE PAUSE — staged-entry tranches crossing a holding's results date buy gap
   risk for free; the pause helper flags tranche dates inside a supplied results calendar.
   The calendar is SUPPLIED (exchange results announcements), never scraped here.
3. EXPIRY-DAY AVOIDANCE — rebalance tranches avoid derivative-expiry days (pinning and
   rollover flows distort closes). The expiry WEEKDAY IS A PARAMETER: SEBI's 2024-25 curbs
   and the 2025 exchange moves (weekly expiries consolidated; NSE/BSE weekday reshuffles)
   make any hardcoded weekday a latent bug. Callers pass the weekday per (exchange, era)
   from config; this module only does the date arithmetic.

Everything here is deterministic date mechanics — exact planted-truth tests, no fixtures.
Windows use BUSINESS days via numpy busday (Mon-Fri; exchange holiday lists are a supplied
refinement, not assumed).
"""
from __future__ import annotations

import numpy as np
import pandas as pd

ADVANCE_TAX = ((6, 15), (9, 15), (12, 15), (3, 15))  # s.211 instalment dates (month, day)
GST_DUE_DAY = 20                                      # GSTR-3B monthly due date


def statutory_drain_dates(year: int) -> list[pd.Timestamp]:
    """All statutory drain dates falling in calendar `year`: 4 advance-tax + 12 GST."""
    out = [pd.Timestamp(year, m, d) for (m, d) in ADVANCE_TAX]
    out += [pd.Timestamp(year, m, GST_DUE_DAY) for m in range(1, 13)]
    return sorted(out)


def _window_mask(dates: pd.DatetimeIndex, anchors: list[pd.Timestamp],
                 pre_bd: int, post_bd: int, holidays=None) -> np.ndarray:
    hol = [] if holidays is None else [np.datetime64(pd.Timestamp(h).date()) for h in holidays]
    d64 = np.array([np.datetime64(pd.Timestamp(x).date()) for x in dates])
    mask = np.zeros(len(d64), dtype=bool)
    for a in anchors:
        a64 = np.datetime64(pd.Timestamp(a).date())
        lo = np.busday_offset(a64, -pre_bd, roll="backward", holidays=hol)
        hi = np.busday_offset(a64, post_bd, roll="forward", holidays=hol)
        mask |= (d64 >= lo) & (d64 <= hi)
    return mask


def drain_window_mask(dates, pre_bd: int = 2, post_bd: int = 1, holidays=None) -> np.ndarray:
    """True where a date sits inside a statutory drain window (advance tax ±, GST due ±).

    Consumption: L2 funding-stress fires inside the mask are quarantined as mechanical
    (flagged, not acted on) pending H58-D1's grading. Reduce-only in spirit: the mask can
    only SUPPRESS a trigger, never create one."""
    idx = pd.DatetimeIndex(pd.to_datetime(pd.Index(dates)))
    years = range(idx.min().year, idx.max().year + 1)
    anchors = [d for y in years for d in statutory_drain_dates(y)]
    return _window_mask(idx, anchors, pre_bd, post_bd, holidays)


def results_pause_mask(tranche_dates, results_dates, pre_bd: int = 1, post_bd: int = 1,
                       holidays=None) -> np.ndarray:
    """True where a staged-entry tranche date crosses a supplied results date (±window).

    A True means: defer the tranche past the window (gap risk is not paid for). The results
    calendar is per-holding and supplied by the caller."""
    idx = pd.DatetimeIndex(pd.to_datetime(pd.Index(tranche_dates)))
    anchors = list(pd.to_datetime(pd.Index(results_dates)))
    if not anchors:
        return np.zeros(len(idx), dtype=bool)
    return _window_mask(idx, anchors, pre_bd, post_bd, holidays)


def expiry_days(dates, weekday: int, which: str = "last") -> np.ndarray:
    """True on the expiry day of each month present in `dates`.

    weekday: 0=Mon..4=Fri, passed from config per (exchange, era) — NEVER hardcoded here
    (see module docstring). which='last' (monthly expiry = last such weekday of the month)
    is the only supported convention; weekly expiries are just `dates.weekday == weekday`
    and need no helper. If the calendar weekday falls on a supplied holiday the exchange
    moves expiry to the PRIOR session — pass exchange holidays via `holidays` in the
    consuming layer; this helper flags the calendar day."""
    if which != "last":
        raise ValueError("only 'last' is supported")
    if not 0 <= int(weekday) <= 4:
        raise ValueError("weekday must be 0..4 (Mon..Fri)")
    idx = pd.DatetimeIndex(pd.to_datetime(pd.Index(dates)))
    out = np.zeros(len(idx), dtype=bool)
    for (y, m) in sorted({(d.year, d.month) for d in idx}):
        last = pd.Timestamp(y, m, 1) + pd.offsets.MonthEnd(0)
        back = (last.weekday() - int(weekday)) % 7
        exp = last - pd.Timedelta(days=back)
        out |= np.asarray(idx.normalize() == exp.normalize())
    return out
