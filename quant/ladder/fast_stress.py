"""L2 — the fast-stress state variable (docs/cycles/02-fast-stress.md §4).

The reactive risk-off switch at the fast end of the ladder (block budget 0.25, tau_half 1-3
months pending F1). Inputs are SERIES; parameters come through the registry (grids in
config/ladder.yaml); this module holds construction logic only. Everything is expanding/
real-time; tested against the two-state synthetic economy with planted stress episodes in
tests/test_fast_stress.py.

Construction mirrors quant/ladder/credit_cycle.py deliberately: percentile-ranked inputs, a
signed composite in [-1, +1] where HIGHER = more stress = LESS risk permission. All L2 inputs
are Tier B (no Tier-C clamp needed here); the phase representation (quant/ladder/phase.py)
rides on top — stress rising (U) arms de-risking, stress falling-from-high (D) is the
candidate re-entry regime, gated by H66/F7 before any traded rule uses it.
"""
from __future__ import annotations

import numpy as np

from .credit_cycle import expanding_percentile


def realized_vol(returns: np.ndarray, window: int = 21, ann: int = 252) -> np.ndarray:
    """Trailing realized volatility (annualized), from squared returns over the window.

    Uses only r[t-window+1 .. t] at each t — real-time by construction. NaN during warm-up.
    Window comes from a pre-registered grid at call sites; 21 (one trading month) is the
    test default only."""
    r = np.asarray(returns, float)
    out = np.full(len(r), np.nan)
    sq = r * r
    c = np.cumsum(sq)
    for t in range(window - 1, len(r)):
        s = c[t] - (c[t - window] if t >= window else 0.0)
        out[t] = np.sqrt(ann * s / window)
    return out


def drawdown_depth(returns: np.ndarray) -> np.ndarray:
    """Current drawdown depth from the expanding peak of the cumulative return path.

    0 at a new high; positive fractions below it (0.12 = 12% below the running peak).
    Expanding peak => no look-ahead."""
    r = np.asarray(returns, float)
    level = np.cumprod(1.0 + r)
    peak = np.maximum.accumulate(level)
    return 1.0 - level / peak


def fast_stress_composite(rv_pct: np.ndarray, dd_pct: np.ndarray,
                          confirm_pct: np.ndarray | None = None,
                          w_rv: float = 0.5, w_dd: float = 0.5,
                          w_confirm: float = 0.0) -> np.ndarray:
    """Composite fast-stress state in [-1, +1]; higher = more stress = less risk permission.

    - rv_pct: expanding percentile of realized vol (the reactive input).
    - dd_pct: expanding percentile of drawdown depth (the "how bad is it already" input).
    - confirm_pct: optional third Tier-B confirm (India-VIX rank / funding-flow stress rank per
      the L2 registry role); symmetric weight — all L2 inputs are Tier B, so no clamp
      (contrast: the credit composite clamps its Tier-C composition input).
    Weights are registry-supplied at call sites; defaults here are for tests only.
    """
    def to_signed(p):
        return 2.0 * np.asarray(p, float) - 1.0

    state = w_rv * to_signed(rv_pct) + w_dd * to_signed(dd_pct)
    total_w = w_rv + w_dd
    if confirm_pct is not None and w_confirm > 0:
        state = state + w_confirm * to_signed(confirm_pct)
        total_w += w_confirm
    return np.clip(state / max(total_w, 1e-9), -1.0, 1.0)
