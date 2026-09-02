"""L5 — calendar-window scheduler (docs/cycles/33-calendar-signal.md, assembling).

The one seat that is a SCHEDULE, not a state: leverage/vol scheduling into windows whose
TIMING is fixed by law while their DIRECTION is pure surprise (PL1: pre-window sign predicts
the result month 3/8 — at/below coin flip; 2004 −15.5% / 2009 +10.7% halt / 2024 −5.9%).
Consequently the seat is reduce-only by contract: it may only shrink exposure into a window,
never place a directional bet on one (ladder.yaml L5 reduce_only: true, D08).

Two window families, monthly resolution:
- BUDGET: February, every year. Era-robust at this resolution — the Union Budget moved from
  the last day of February (pre-2017) to February 1 (2017-) and both live inside the same
  month. Election-year July full budgets are NOT flagged (documented limitation; CW1).
- ELECTION: general-election result months, supplied as dates (n=8-9 since 1991 — an event
  list, not a clock; the 5-year rhythm shifts with early dissolutions, so no extrapolated
  schedule is ever generated beyond announced calendars).

Windows carry their trail: `windows()` returns explicit (start, end, kind) objects so any
consumer can say WHY a month is flagged. Deterministic module — planted-truth tests are
exact assertions, no stochastic fixture (tests/test_calendar_windows.py).

Desk evidence: CW1 FAIL (Feb |MF| rank 7/12 monthly — the budget-day spike is a daily
phenomenon, invisible monthly; the seat's vol claim rests on the daily-resolution VIX
record + the fixed-reveal mechanism, and the monograph says so). CW3 omnibus null (no
month-of-year structure) is exactly why this seat schedules and never forecasts.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

BUDGET_MONTH = 2  # February — see docstring for the era-robustness argument


@dataclass(frozen=True)
class Window:
    """One scheduling window, with its trail."""
    start: pd.Period   # first flagged month (inclusive)
    end: pd.Period     # last flagged month (inclusive)
    kind: str          # "budget" | "election"
    anchor: pd.Period  # the event month the window is built around


def _to_periods(months) -> pd.PeriodIndex:
    idx = pd.PeriodIndex(pd.to_datetime(pd.Index(months)), freq="M")
    if len(idx) > 1 and not (idx[1:] > idx[:-1]).all():
        raise ValueError("months must be strictly increasing")
    return idx


def windows(months, election_result_months=(), pre: int = 2, post: int = 1,
            budget_pre: int = 0, budget_post: int = 0) -> list[Window]:
    """Build the window list over `months` (monthly timestamps, strictly increasing).

    Election windows span [anchor - pre, anchor + post] months around each supplied result
    month (defaults from the FP1/PL1 designs: 2 months of pre-election positioning noise +
    the settling month). Budget windows default to February alone (budget_pre/post widen it
    if a pre-registered design ever earns that). Events outside `months` are ignored;
    nothing is extrapolated."""
    idx = _to_periods(months)
    lo, hi = idx[0], idx[-1]
    out: list[Window] = []
    for y in range(lo.year, hi.year + 1):
        anchor = pd.Period(f"{y}-{BUDGET_MONTH:02d}", freq="M")
        w = Window(anchor - budget_pre, anchor + budget_post, "budget", anchor)
        if w.end >= lo and w.start <= hi:
            out.append(w)
    for em in election_result_months:
        anchor = pd.Period(pd.Timestamp(em), freq="M")
        w = Window(anchor - pre, anchor + post, "election", anchor)
        if w.end >= lo and w.start <= hi:
            out.append(w)
    return sorted(out, key=lambda w: (w.start, w.kind))


def calendar_schedule(months, election_result_months=(), pre: int = 2, post: int = 1):
    """The seat's output: (in_window, n_windows, kinds) aligned to `months`.

    in_window — boolean scheduling mask (True = a reduce-only window is active);
    n_windows — how many windows overlap each month (int; overlaps are real: a February
    inside an election window counts 2 — the consumer sees depth, not just a flag);
    kinds — per-month tuple of window kinds, the trail ("why is this month flagged?").
    No directional output exists on purpose."""
    idx = _to_periods(months)
    ws = windows(months, election_result_months, pre=pre, post=post)
    n = np.zeros(len(idx), dtype=int)
    kinds: list[tuple[str, ...]] = [() for _ in idx]
    for w in ws:
        hit = (idx >= w.start) & (idx <= w.end)
        n += hit.astype(int)
        for i in np.flatnonzero(hit):
            kinds[i] = kinds[i] + (w.kind,)
    return n > 0, n, kinds
