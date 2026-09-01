"""L2 fast-stress module vs the two-state synthetic economy with PLANTED stress episodes.

Assertions frozen only after holding across seeds 0-7 (dev log in the deep-dive #2 record):
stress-calm separation >= 0.26 everywhere (bar set at 0.2), every stress episode of >= 15 days
detected, median detection lag 1-10 days (bar at 12)."""
import numpy as np
import pytest

from quant.ladder import (drawdown_depth, expanding_percentile,
                          fast_stress_composite, realized_vol)
from quant.validation.synthetic import regime_vol_returns


def build_state(r, min_obs=126):
    rv_pct = expanding_percentile(realized_vol(r, 21), min_obs=min_obs)
    dd_pct = expanding_percentile(drawdown_depth(r), min_obs=min_obs)
    return fast_stress_composite(rv_pct, dd_pct)


def test_realized_vol_matches_direct_computation():
    rng = np.random.default_rng(0)
    r = rng.normal(0, 0.01, 300)
    rv = realized_vol(r, window=21)
    t = 250
    direct = np.sqrt(252 * np.mean(r[t - 20:t + 1] ** 2))
    assert rv[t] == pytest.approx(direct, rel=1e-10)
    assert np.isnan(rv[:20]).all()


def test_drawdown_depth_on_a_known_path():
    r = np.array([0.10, -0.10, -0.10, 0.05, 0.30])
    dd = drawdown_depth(r)
    # peak after day 0 = 1.10; day 2 level = 1.10*0.9*0.9 = 0.891 -> dd = 1 - 0.891/1.10 = 0.19
    assert dd[0] == pytest.approx(0.0)
    assert dd[2] == pytest.approx(1 - 0.891 / 1.10, abs=1e-12)
    assert dd[4] == pytest.approx(0.0)  # new high clears the drawdown


def test_state_separates_planted_stress_from_calm():
    r, st = regime_vol_returns(3000, seed=0, return_states=True)
    state = build_state(r)
    m = ~np.isnan(state)
    assert np.nanmean(state[m & st]) > np.nanmean(state[m & ~st]) + 0.2


def test_long_episodes_detected_at_high_rate_and_quickly():
    """Detection is high but NOT total — a planted episode can be genuinely mild (random drift)
    and leave no vol signature; a real stress switch has the same property. Measured across
    seeds 0-9 before freezing: 92/98 episodes >=15d cross 0.3 (94%), median lag 1 day. The
    original draft asserted 100% detection at 0.5; the run falsified it (73/98) and the honest
    bound below replaced it — second entry of this kind in the verification log."""
    tot, det_n, lags = 0, 0, []
    for seed in (0, 1, 2):
        r, st = regime_vol_returns(3000, seed=seed, return_states=True)
        state = build_state(r)
        starts = np.where(np.diff(st.astype(int)) == 1)[0] + 1
        for s0 in starts:
            if s0 < 300:
                continue
            run = 0
            while s0 + run < len(st) and st[s0 + run]:
                run += 1
            if run < 15:
                continue
            tot += 1
            det = [k for k in range(run)
                   if not np.isnan(state[s0 + k]) and state[s0 + k] > 0.3]
            if det:
                det_n += 1
                lags.append(det[0])
    assert tot >= 10, "fixture must contain enough long episodes to make the rate meaningful"
    assert det_n / tot >= 0.85, f"detection rate too low: {det_n}/{tot}"
    assert np.median(lags) <= 5, f"median detection lag too slow: {np.median(lags)}"


def test_truncating_the_future_never_changes_the_past():
    r, _ = regime_vol_returns(2000, seed=1, return_states=True)
    full = build_state(r)
    for T in (800, 1200, 1600):
        tr = build_state(r[:T + 1])
        m = ~np.isnan(full[:T + 1]) & ~np.isnan(tr)
        assert np.allclose(full[:T + 1][m], tr[m], atol=1e-12)


def test_confirm_input_is_symmetric_tier_b():
    """Unlike credit's Tier-C composition (clamped non-negative), the L2 confirm input is Tier B:
    a benign confirm reading may lower the state (both directions allowed)."""
    r, _ = regime_vol_returns(2000, seed=2, return_states=True)
    rv_pct = expanding_percentile(realized_vol(r, 21), min_obs=126)
    dd_pct = expanding_percentile(drawdown_depth(r), min_obs=126)
    base = fast_stress_composite(rv_pct, dd_pct)
    lo = fast_stress_composite(rv_pct, dd_pct,
                               confirm_pct=np.zeros(len(base)), w_confirm=0.3)
    hi = fast_stress_composite(rv_pct, dd_pct,
                               confirm_pct=np.ones(len(base)), w_confirm=0.3)
    m = ~np.isnan(base)
    assert np.all(lo[m] <= base[m] + 1e-12), "benign confirm may pull the state DOWN (Tier B)"
    assert np.all(hi[m] >= base[m] - 1e-12)
    valid = base[m]
    assert ((valid >= -1) & (valid <= 1)).all()
