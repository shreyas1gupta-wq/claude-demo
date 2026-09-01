"""Phase-space state representation — every ladder state is a TRAJECTORY, not a number.

Principal's directive (2026-09-01): a scalar state in [-1,+1] discards the path. 0.6 reached
from below (0 -> 0.2 -> 0.4 -> 0.6) and 0.6 reached from above (1 -> 0.9 -> ... -> 0.6) are
different regimes. The literature form is the business-cycle clock (Eurostat/OECD CLI practice):
(level, velocity) space, four quadrants traversed as a loop:

    recovery  = level low,  rising     boom     = level high, rising
    slowdown  = level high, falling    downturn = level low,  falling

Design rules (CONTRACT-compliant):
- Quadrant boundaries are DETERMINISTIC (level midpoint + slope sign), never fitted — no regime
  model, so the <10-transitions rule is not triggered.
- Direction carries HYSTERESIS: the sign flips only when the smoothed slope's magnitude clears a
  rank-based dead-band (an expanding percentile of |slope| history — no magic threshold), so
  noise cannot flip-flop the label.
- Everything is expanding/real-time; the no-look-ahead truncation property is tested.
- Parameters (slope horizon, smoothing, dead-band percentile) come from pre-registered grids in
  config/ladder.yaml `state_phase_convention`; defaults here are for tests only.

The scalar state remains available (level); phase is an ENRICHMENT consumed by the policy layer,
pre-registered for testing as H66-H68 before any quadrant-conditioned rule trades.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

QUADRANTS = ("recovery", "boom", "slowdown", "downturn")  # canonical rotation order


@dataclass
class PhaseResult:
    level: np.ndarray      # the input state, echoed
    velocity: np.ndarray   # smoothed slope per period (NaN during warm-up)
    direction: np.ndarray  # +1 rising / -1 falling, with hysteresis (NaN warm-up)
    quadrant: np.ndarray   # int codes: 0 recovery, 1 boom, 2 slowdown, 3 downturn (-1 warm-up)
    age: np.ndarray        # periods since the current quadrant began (NaN warm-up)


def _sma(x: np.ndarray, w: int) -> np.ndarray:
    out = np.full(len(x), np.nan)
    c = np.nancumsum(np.where(np.isnan(x), 0.0, x))
    n = np.cumsum(~np.isnan(x))
    for t in range(w - 1, len(x)):
        cnt = n[t] - (n[t - w] if t >= w else 0)
        if cnt == w:
            out[t] = (c[t] - (c[t - w] if t >= w else 0.0)) / w
    return out


def phase_state(level: np.ndarray, k_slope: int = 6, smooth: int = 3,
                deadband_pct: float = 0.25, level_mid: float = 0.0,
                min_obs: int = 24) -> PhaseResult:
    """Turn a scalar state series into its phase-space representation.

    level: the state series (e.g. the credit composite in [-1,+1], or a percentile with
      level_mid=0.5). velocity_t = (SMA(level, smooth)_t - SMA(level, smooth)_{t-k_slope}) / k_slope
      — the average slope over the trailing k_slope periods, computed from history only.
    Hysteresis: direction flips only when the NEW sign's |velocity| exceeds the dead-band, defined
      as the deadband_pct expanding percentile of all |velocity| observed so far (rank-based, no
      fixed threshold). Below the dead-band the previous direction persists.
    """
    level = np.asarray(level, float)
    n = len(level)
    sm = _sma(level, smooth)
    vel = np.full(n, np.nan)
    for t in range(k_slope, n):
        if not (np.isnan(sm[t]) or np.isnan(sm[t - k_slope])):
            vel[t] = (sm[t] - sm[t - k_slope]) / k_slope

    direction = np.full(n, np.nan)
    quadrant = np.full(n, -1, dtype=int)
    age = np.full(n, np.nan)
    prev_dir = 0.0
    prev_quad = -1
    abs_hist: list[float] = []
    started = False
    for t in range(n):
        v = vel[t]
        if np.isnan(v) or np.isnan(level[t]):
            continue
        abs_hist.append(abs(v))
        if len(abs_hist) < min_obs:
            continue
        thr = float(np.quantile(abs_hist, deadband_pct))
        cand = 1.0 if v > 0 else -1.0
        if not started:
            d = cand  # first labelled period takes the raw sign
            started = True
        elif cand != prev_dir and abs(v) > thr:
            d = cand              # a real turn: sign flipped AND magnitude clears the dead-band
        else:
            d = prev_dir          # inside the dead-band (or no flip): direction persists
        prev_dir = d
        direction[t] = d
        high = level[t] >= level_mid
        q = (1 if high else 0) if d > 0 else (2 if high else 3)
        quadrant[t] = q
        age[t] = 1.0 if q != prev_quad else age[t - 1] + 1.0 if not np.isnan(age[t - 1]) else 1.0
        prev_quad = q
    return PhaseResult(level=level, velocity=vel, direction=direction,
                       quadrant=quadrant, age=age)


def phase_label(level: float, direction: float, decimals: int = 2) -> str:
    """The principal's notation: '0.60U' / '0.60D' (NaN-safe)."""
    if np.isnan(level) or np.isnan(direction):
        return "nan"
    return f"{level:.{decimals}f}{'U' if direction > 0 else 'D'}"
