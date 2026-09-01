"""L11 — the capex/investment-cycle state (docs/cycles/16-capex-cycle.md, assembling).

Three legs per ladder.yaml (OBICUS utilization, IIP capital goods, GFCF share), each an
expanding-percentile rank, combined as an availability-weighted signed mean — the L12 pattern
with THREE legs, because India's legs start decades apart (GFCF ~1950s annual, IIP-capgoods
1994+, OBICUS 2008+): n_legs is a first-class output and the sentinel flags degradation.

CLAMP SEMANTICS (ladder.yaml: contribution_clamp: non_positive): the RAW state is exposed by
capex_cycle_state — sector-tilt consumers read it in full — and the macro-block contribution
applies clamp_non_positive at CONSUMPTION, so a hot capex print can never ADD regime score
through the shared budget (consistency-audit finding; IN3's non-monotone analogue read backs
the design). Evidence tier is C (IN1 failed its sign-consistency bar; the module is machinery,
not an evidence claim — see the trial ledger).
"""
from __future__ import annotations

import numpy as np


def capex_cycle_state(util_pct: np.ndarray, capgoods_pct: np.ndarray, gfcf_pct: np.ndarray,
                      w_util: float = 1.0, w_capgoods: float = 1.0, w_gfcf: float = 1.0):
    """Combined L11 state in [-1, +1]; higher = hotter capex conditions.

    Inputs are expanding-percentile ranks in [0, 1] (NaN where a leg does not exist yet).
    Returns (state, n_legs): n_legs in {0,1,2,3} marks how many legs carried each date;
    consumers must treat n_legs < 3 as DEGRADED. state is NaN where n_legs == 0."""
    legs = [(np.asarray(util_pct, float), w_util),
            (np.asarray(capgoods_pct, float), w_capgoods),
            (np.asarray(gfcf_pct, float), w_gfcf)]
    T = len(legs[0][0])
    num, den, n = np.zeros(T), np.zeros(T), np.zeros(T)
    for p, w in legs:
        signed = 2.0 * p - 1.0
        ok = ~np.isnan(signed)
        num[ok] += w * signed[ok]
        den[ok] += w
        n += ok.astype(int)
    state = np.where(den > 0, num / np.where(den > 0, den, 1.0), np.nan)
    state = np.clip(state, -1.0, 1.0)
    state[n == 0] = np.nan
    return state, n.astype(int)


def clamp_non_positive(state: np.ndarray) -> np.ndarray:
    """The macro-block consumption clamp: min(0, state), NaN-preserving.

    Applied at block aggregation, never inside the state itself — the raw state stays
    available to sector-tilt consumers (partC C.6 ordering argument)."""
    s = np.asarray(state, float)
    return np.where(np.isnan(s), np.nan, np.minimum(s, 0.0))
