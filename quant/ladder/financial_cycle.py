"""L12 — the medium-term financial-cycle state (docs/cycles/12-financial-cycle.md, assembling).

Borio's object: credit and property prices amplifying each other. Construction: the credit/GDP
gap leg (shared machinery with L10 — the §4.2 de-duplication rule means L12 adds the PROPERTY
leg, never a second credit seat) plus a REAL house-price Hamilton gap leg, each expanding-
percentile ranked, combined as a signed mean. India reality baked into the API: the house-price
series is SHORT (RBI HPI from ~2010), so the combined state must degrade gracefully to the
available leg with the degradation FLAGGED — tested against the planted joint-boom fixture
(quant/validation/synthetic.py::financial_cycle_economy) in tests/test_financial_cycle.py.
"""
from __future__ import annotations

import numpy as np

from quant.stats.hamilton import hamilton_filter

from .credit_cycle import expanding_percentile


def real_house_price_gap(hp_nominal: np.ndarray, cpi: np.ndarray, h: int,
                         p: int = 4) -> np.ndarray:
    """Expanding Hamilton gap of the REAL house-price level (nominal ÷ CPI).

    Same estimator family as the credit gap; the property leg's h comes from the same
    pre-registered 16-24q grid (registry). NaN-robust (short/holed series supported)."""
    real_hp = np.asarray(hp_nominal, float) / np.asarray(cpi, float)
    return hamilton_filter(real_hp, h=h, p=p, mode="expanding")


def financial_cycle_state(credit_gap_pct: np.ndarray, hp_gap_pct: np.ndarray,
                          w_credit: float = 0.5, w_hp: float = 0.5):
    """Combined L12 state in [-1, +1]; higher = joint boom more mature = less risk permission.

    Returns (state, n_legs): n_legs marks how many legs carried each date (2 = full; 1 = the
    other leg was missing — the India short-HPI reality; 0 = NaN). Consumers must treat
    n_legs==1 dates as DEGRADED (the sentinel flags them); the state never silently pretends
    both legs existed."""
    def signed(p):
        return 2.0 * np.asarray(p, float) - 1.0

    c, h = signed(credit_gap_pct), signed(hp_gap_pct)
    n = np.zeros(len(c))
    num = np.zeros(len(c))
    den = np.zeros(len(c))
    for leg, w in ((c, w_credit), (h, w_hp)):
        ok = ~np.isnan(leg)
        num[ok] += w * leg[ok]
        den[ok] += w
        n += ok.astype(int)
    state = np.where(den > 0, num / np.where(den > 0, den, 1.0), np.nan)
    state = np.clip(state, -1.0, 1.0)
    state[n == 0] = np.nan
    return state, n.astype(int)
