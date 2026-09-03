"""Triple-barrier labeling and meta-labels (López de Prado, Advances in Financial ML ch.3).

The label a supervised model should learn is path-aware: which of {profit-take, stop-loss,
time-out} a position hits first. Meta-labeling then asks the second question — given a
primary signal already took a side, was it RIGHT — turning a directional model into a
bet-sizing filter (the pipeline-v2 design's chosen consumption for ML).
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class BarrierEvent:
    t0: int          # entry index
    t1: int          # exit index (barrier hit or vertical)
    label: int       # +1 profit-take first, -1 stop-loss first, 0 vertical timeout
    ret: float       # log return over [t0, t1]


def triple_barrier(close: np.ndarray, events: np.ndarray, vol: np.ndarray,
                   pt_mult: float, sl_mult: float, max_hold: int,
                   side: np.ndarray | None = None) -> list[BarrierEvent]:
    """Label each event bar by the first barrier its forward path touches.

    - close: price series; events: entry indices; vol: per-bar vol estimate (same units as
      log returns) sizing the horizontal barriers; pt_mult/sl_mult scale them (a 0 mult
      disables that barrier); max_hold: the vertical barrier in bars.
    - side: optional +1/-1 per event (from a primary model). Barriers are applied to
      side * path so a short's profit-take is a fall. With side given, label=0 still means
      timeout; the SIGN of a horizontal hit is in profit/stop terms.
    Real-time by construction: uses only the path AFTER t0; vol must be computed by the
    caller from data through t0 (that contract is the caller's, tested at call sites).
    """
    close = np.asarray(close, float)
    logp = np.log(close)
    out = []
    n = len(close)
    for k, t0 in enumerate(np.asarray(events, int)):
        s = 1.0 if side is None else float(side[k])
        up = pt_mult * vol[t0] if pt_mult > 0 else np.inf
        dn = -sl_mult * vol[t0] if sl_mult > 0 else -np.inf
        t_end = min(t0 + max_hold, n - 1)
        label, t1 = 0, t_end
        for t in range(t0 + 1, t_end + 1):
            path = s * (logp[t] - logp[t0])
            if path >= up:
                label, t1 = 1, t
                break
            if path <= dn:
                label, t1 = -1, t
                break
        out.append(BarrierEvent(t0=int(t0), t1=int(t1), label=label,
                                ret=float(s * (logp[t1] - logp[t0]))))
    return out


def meta_labels(events: list[BarrierEvent]) -> np.ndarray:
    """Meta-label per event: 1 if the (side-adjusted) position ended profitable, else 0.

    The meta-model learns WHEN to trust the primary signal; size = P(meta=1) downstream.
    Timeouts count by their realized sign — a timeout that made money is still a good bet.
    """
    return np.array([1 if e.ret > 0 else 0 for e in events], dtype=int)
