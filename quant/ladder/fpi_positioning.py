"""L14 — FPI positioning extremes (docs/cycles/26-fpi-positioning.md, assembling).

The seat's defining EXCLUSION: flow momentum is rejected outright (returns lead flows —
Griffin-Nardari-Stulz; Chakrabarti; atlas §7), so this module exposes NO flow-based output of
any kind. What it computes is the surviving object: the float-scaled foreign-ownership share
as an expanding percentile, with a RISK-OFF-ONLY extreme flag — an extreme position is a
crowded exit whose unwind takes real capital and time (the capacity mechanism), and the
asymmetry is by design: high extremes condition risk DOWN; low extremes carry no flag (an
empty theater has no exit problem). Tier C, reduce-only, tierC_overlay (ladder.yaml L14).
Evidence: data-gated designs FL1/FL2 (trial ledger); machinery tested on planted truth.
"""
from __future__ import annotations

import numpy as np

from .credit_cycle import expanding_percentile


def fpi_positioning_state(ownership_float_share: np.ndarray, min_obs: int = 36) -> np.ndarray:
    """Expanding percentile of the float-scaled foreign-ownership share, in [0, 1].

    Input is ownership as a share of FREE FLOAT (never raw market cap — promoter holdings
    make raw shares misleading); NaN until min_obs ranks exist (honesty by construction)."""
    return expanding_percentile(np.asarray(ownership_float_share, float), min_obs=min_obs)


def positioning_extreme(state: np.ndarray, hi: float = 0.9) -> np.ndarray:
    """The RISK-OFF-ONLY flag: True where the positioning percentile >= hi.

    Deliberately asymmetric (no low-side flag) and deliberately the module's only consumer-
    facing signal: reduce-only conditioning per ladder.yaml. hi comes from the registered
    grid; NaN state -> False (no flag without ranks)."""
    s = np.asarray(state, float)
    return np.where(np.isnan(s), False, s >= hi)
