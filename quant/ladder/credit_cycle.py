"""L10 — the credit-cycle state variable (docs/cycles/01-credit-cycle.md §4).

Inputs are SERIES, parameters come through the registry; this module holds construction logic
only. Everything is expanding/real-time (no look-ahead), tested against a synthetic boom-bust
economy in tests/test_credit_cycle.py.
"""
from __future__ import annotations

import numpy as np

from quant.stats.hamilton import hamilton_filter


def credit_gap(credit: np.ndarray, income: np.ndarray, h: int, p: int = 4) -> np.ndarray:
    """Hamilton-filtered credit-to-income gap, EXPANDING mode (real-time honest).

    credit, income: level series (same frequency). Returns the cyclical component of the
    credit/income ratio aligned to date; NaN during warm-up. NEVER the HP filter; the BIS
    HP-based gap is an external cross-check only (CONTRACT §8)."""
    ratio = np.asarray(credit, float) / np.asarray(income, float)
    return hamilton_filter(ratio, h=h, p=p, mode="expanding")


def expanding_percentile(x: np.ndarray, min_obs: int = 24) -> np.ndarray:
    """Percentile rank of x[t] within x[:t+1] (expanding window — no look-ahead by construction).

    The no-magic-numbers workhorse: levels become self-referenced ranks."""
    x = np.asarray(x, float)
    out = np.full(len(x), np.nan)
    for t in range(min_obs - 1, len(x)):
        window = x[: t + 1]
        window = window[~np.isnan(window)]
        if len(window) >= min_obs:
            out[t] = (window < x[t]).mean() if not np.isnan(x[t]) else np.nan
    return out


def credit_state_composite(gap_pct: np.ndarray, cd_pct: np.ndarray,
                           composition_pct: np.ndarray | None = None,
                           w_gap: float = 0.5, w_cd: float = 0.5,
                           w_composition: float = 0.0) -> np.ndarray:
    """Composite credit state in [-1, +1]; higher = boom more mature = LESS risk permission.

    - gap_pct, cd_pct: percentile series in [0,1] (Tier-B inputs).
    - composition_pct: Tier-C issuance-quality percentile — CLAMPED to non-positive contribution
      per Contract §4 / ladder.yaml L11-style rule: a hot composition reading can only push the
      state toward risk-off, never add risk-on. (Consistency-audit finding C2, enforced in code;
      the mirror test lives in tests/test_credit_cycle.py.)
    Weights are registry-supplied at call sites; defaults here are for tests only.
    """
    def to_signed(p):
        return 2.0 * np.asarray(p, float) - 1.0     # [0,1] -> [-1,+1]

    state = w_gap * to_signed(gap_pct) + w_cd * to_signed(cd_pct)
    if composition_pct is not None and w_composition > 0:
        contrib = w_composition * to_signed(composition_pct)
        state = state + np.maximum(contrib, 0.0)    # only ADDS toward +1 (risk-off direction)
    total_w = w_gap + w_cd + (w_composition if composition_pct is not None else 0.0)
    return np.clip(state / max(total_w, 1e-9), -1.0, 1.0)
