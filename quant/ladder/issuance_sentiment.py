"""L7 — issuance/sentiment state (docs/cycles/29-issuance.md, assembling).

The rare seat whose signal the desk expects NOT to fully decay: issuers' incentive to sell
expensive paper is structural (Baker-Wurgler; nobody arbitrages a promoter's decision not to
float). Two legs, both expanding percentiles: VOLUME (issuance value / market cap) and
RECEPTION (median first-day pop). Both high = the froth signature; volume without pops is
capital formation, pops without volume is scarcity. Consumption: the valuation_sentiment
block (with L8) + the special-sits sizing rule (froth => shrink) — reduce-only consequences.
Months with no listings leave the reception leg NaN: n_legs is first-class, as everywhere.
Evidence: designs IS1/IS2 (data-gated, trial ledger); machinery tested on planted truth.
"""
from __future__ import annotations

import numpy as np

from .credit_cycle import expanding_percentile


def issuance_sentiment_state(volume_ratio: np.ndarray, first_day_pop: np.ndarray,
                             min_obs: int = 36, w_volume: float = 1.0, w_pop: float = 1.0):
    """Two-leg froth state in [0, 1]; higher = hotter primary market.

    Returns (state, n_legs). Legs are expanding percentiles of the raw series; a no-listings
    month (NaN pop) degrades to the volume leg with n_legs=1 — flagged, never silent."""
    pv = expanding_percentile(np.asarray(volume_ratio, float), min_obs=min_obs)
    pp = expanding_percentile(np.asarray(first_day_pop, float), min_obs=min_obs)
    T = len(pv)
    num, den, n = np.zeros(T), np.zeros(T), np.zeros(T)
    for leg, w in ((pv, w_volume), (pp, w_pop)):
        ok = ~np.isnan(leg)
        num[ok] += w * leg[ok]
        den[ok] += w
        n += ok.astype(int)
    state = np.where(den > 0, num / np.where(den > 0, den, 1.0), np.nan)
    state[n == 0] = np.nan
    return state, n.astype(int)


def froth_flag(state: np.ndarray, hi: float = 0.9) -> np.ndarray:
    """The special-sits shrink flag: True where the froth state >= hi (grid-registered).

    Reduce-only consumption (sleeve sizing down, valuation-block confirm) — never a short
    signal; NaN state -> False."""
    s = np.asarray(state, float)
    return np.where(np.isnan(s), False, s >= hi)
