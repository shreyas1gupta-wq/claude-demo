"""L11 capex module vs the planted accelerator economy.

Bounds frozen after a 10-seed dev sweep (2026-09-01, post-retune: boom force 0.008, reversion
0.10): early-boom pooled firing +0.05..+0.75 (mean +0.39), turn collapse -0.50..-0.77 (10/10).
SEEDS are the first three of the sweep, not a curated subset. All three legs are ranks; the
gap legs are IMPULSE-like (the Lesson-1 dynamic), so the test windows are early-boom and the
turn — never the late plateau. The non_positive clamp is consumption-side (ladder.yaml)."""
import numpy as np

from quant.ladder import capex_cycle_state, clamp_non_positive, expanding_percentile
from quant.stats.hamilton import hamilton_filter
from quant.validation.synthetic import capex_economy

SEEDS = (0, 1, 2)


def legs(e, min_obs=36):
    pu = expanding_percentile(e["util"], min_obs=min_obs)
    pc = expanding_percentile(
        hamilton_filter(np.log(e["capgoods"]), h=24, p=4, mode="expanding"), min_obs=min_obs)
    pg = expanding_percentile(
        hamilton_filter(e["gfcf_share"], h=24, p=4, mode="expanding"), min_obs=min_obs)
    return pu, pc, pg


def test_state_fires_early_and_collapses_at_the_turn():
    early_all, turn_all = [], []
    for s in SEEDS:
        e = capex_economy(seed=s)
        st, _ = capex_cycle_state(*legs(e))
        b0, _ = e["boom"]
        c0, _ = e["bust"]
        early_all.append(np.nanmean(st[b0 + 12:b0 + 72]))
        turn_all.append(np.nanmean(st[c0 + 6:c0 + 42]))
    assert np.mean(early_all) > 0.2, f"early firing too weak: {np.mean(early_all):.2f}"
    assert np.mean(turn_all) < np.mean(early_all) - 0.5, "the turn must collapse the state"
    assert max(turn_all) < -0.45


def test_degrades_gracefully_when_legs_start_late():
    """India reality: GFCF is decades long, IIP-capgoods starts 1994, OBICUS 2008 — the state
    must carry n_legs and equal the available-leg mean, never NaN-spill or stay silent."""
    e = capex_economy()
    pu, pc, pg = legs(e)
    pu_short = pu.copy()
    pu_short[:300] = np.nan
    st, n = capex_cycle_state(pu_short, pc, pg)
    both = ~np.isnan(pc[:300]) & ~np.isnan(pg[:300])
    assert (n[:300][both] == 2).all()
    expect = ((2 * pc - 1) + (2 * pg - 1)) / 2
    assert np.allclose(st[:300][both], np.clip(expect[:300][both], -1, 1), atol=1e-12)
    late = ~np.isnan(pu_short[320:]) & ~np.isnan(pc[320:]) & ~np.isnan(pg[320:])
    assert (n[320:][late] == 3).all()


def test_clamp_is_non_positive_and_nan_preserving():
    e = capex_economy()
    st, _ = capex_cycle_state(*legs(e))
    c = clamp_non_positive(st)
    ok = ~np.isnan(st)
    assert (c[ok] <= 0).all()
    neg = ok & (st < 0)
    assert np.allclose(c[neg], st[neg])
    assert np.isnan(c[~ok]).all()


def test_no_lookahead_truncation():
    e = capex_economy()
    st_full, _ = capex_cycle_state(*legs(e))
    T = 350
    e_tr = {k: (v[:T] if isinstance(v, np.ndarray) else v) for k, v in e.items()}
    st_tr, _ = capex_cycle_state(*legs(e_tr))
    m = ~np.isnan(st_full[:T]) & ~np.isnan(st_tr)
    assert np.allclose(st_full[:T][m], st_tr[m], atol=1e-12)
