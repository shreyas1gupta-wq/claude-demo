"""L12 financial-cycle module vs the planted credit-property economy.

Bounds frozen after a 10-seed dev sweep (2026-09-01): planted co-movement recovered at
0.96-0.99; the combined state fires in the early boom (9/10 seeds; one marginal miss kept
honest) and collapses at the turn with -0.88..-0.97 readings (10/10). Both legs are expanding
gaps, so the state is IMPULSE-like — the Lesson-1 dynamic, now on two legs; the level job in
production is carried elsewhere in the macro block (de-duplication rule §4.2)."""
import numpy as np

from quant.ladder import (credit_gap, expanding_percentile,
                          financial_cycle_state, real_house_price_gap)
from quant.validation.synthetic import financial_cycle_economy

SEEDS = (31, 0, 1)


def legs(e, min_obs=36):
    gc = expanding_percentile(credit_gap(e["credit"], e["income"], h=24), min_obs=min_obs)
    gh = expanding_percentile(real_house_price_gap(e["hp"], e["cpi"], h=24), min_obs=min_obs)
    return gc, gh


def test_planted_comovement_is_recovered():
    e = financial_cycle_economy()
    r = e["credit"] / e["income"]
    rh = e["hp"] / e["cpi"]
    d5c = r[60:] - r[:-60]
    d5h = np.log(rh[60:]) - np.log(rh[:-60])
    assert np.corrcoef(d5c, d5h)[0, 1] > 0.9


def test_state_fires_early_and_collapses_at_the_turn():
    early_all, turn_all = [], []
    for s in SEEDS:
        e = financial_cycle_economy(seed=s)
        st, _ = financial_cycle_state(*legs(e))
        b0, b1 = e["boom"]
        early_all.append(np.nanmean(st[b0 + 6:b0 + 48]))
        turn_all.append(np.nanmean(st[b1:b1 + 30]))
    assert np.mean(early_all) > 0.25, f"early-boom firing too weak: {np.mean(early_all):.2f}"
    assert np.mean(turn_all) < np.mean(early_all) - 0.5, "the turn must collapse the state"
    assert max(turn_all) < -0.5


def test_degrades_gracefully_when_the_property_leg_is_short():
    """India reality: HPI starts ~2010. A late-starting hp leg must yield n_legs=1 (credit-only,
    equal to the credit leg) early and n_legs=2 later — never NaN spillover, never silence."""
    e = financial_cycle_economy()
    gc, gh = legs(e)
    gh_short = gh.copy()
    gh_short[:300] = np.nan
    st, n = financial_cycle_state(gc, gh_short)
    early = ~np.isnan(gc[:300])
    assert (n[:300][early] == 1).all()
    assert np.allclose(st[:300][early], 2 * gc[:300][early] - 1, atol=1e-12)
    late = ~np.isnan(gc[320:]) & ~np.isnan(gh_short[320:])
    assert (n[320:][late] == 2).all()


def test_no_lookahead_truncation():
    e = financial_cycle_economy()
    st_full, _ = financial_cycle_state(*legs(e))
    T = 350
    e_tr = {k: (v[:T] if isinstance(v, np.ndarray) else v) for k, v in e.items()}
    st_tr, _ = financial_cycle_state(*legs(e_tr))
    m = ~np.isnan(st_full[:T]) & ~np.isnan(st_tr)
    assert np.allclose(st_full[:T][m], st_tr[m], atol=1e-12)
