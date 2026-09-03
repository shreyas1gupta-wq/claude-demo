"""The regime assembler vs exact planted truth + the vaulted real series (deterministic)."""
import numpy as np
import pandas as pd
import pytest

from quant.regime import assemble_regime, bucket_path
from quant.registry.loader import load_registry

LADDER = load_registry(validate=False)["ladder"]


def test_two_seat_exact_score_and_trail():
    # L2 (fast_stress, 0.25) at +0.8 and L10 (macro_credit_block, 0.20) at -0.4
    r = assemble_regime({"L2_fast_stress": 0.8, "L10_credit_block": -0.4}, LADDER)
    want = (0.25 * 0.8 + 0.20 * -0.4) / 0.45
    assert abs(r.score - want) < 1e-12
    assert r.available_budget == pytest.approx(0.45) and r.n_blocks == 2
    assert r.block_avail == {"fast_stress": ["L2_fast_stress"],
                             "macro_credit_block": ["L10_credit_block"]}
    assert "L9_global_financial_cycle" in r.missing


def test_availability_weighting_never_reads_missing_as_calm():
    lone = assemble_regime({"L2_fast_stress": 0.8}, LADDER)
    assert lone.score == pytest.approx(0.8)      # not diluted by absent blocks
    assert lone.available_budget == pytest.approx(0.25)


def test_reduce_only_seat_adds_stress_never_calm():
    calm = assemble_regime({"L5_calendar_windows": -0.9}, LADDER)
    assert np.isnan(calm.score) or calm.n_blocks == 0 or calm.score == 0.0
    stressed = assemble_regime({"L5_calendar_windows": 0.6}, LADDER)
    assert stressed.score == pytest.approx(0.6)


def test_tierC_never_enters_score_only_negative_overlay():
    # L1 is Tier C: calm state contributes NOTHING; stressed adds capped overlay only
    base = assemble_regime({"L2_fast_stress": 0.4}, LADDER)
    with_calm_c = assemble_regime({"L2_fast_stress": 0.4, "L1_reversal_1m": -1.0}, LADDER)
    assert with_calm_c.score == pytest.approx(base.score) and with_calm_c.overlay == 0.0
    with_hot_c = assemble_regime({"L2_fast_stress": 0.4, "L1_reversal_1m": 1.0}, LADDER)
    assert with_hot_c.overlay == pytest.approx(0.10)      # tierC_overlay_cap
    assert with_hot_c.score == pytest.approx(base.score + 0.10)
    assert "tierC_overlay" not in with_hot_c.block_states


def test_empty_input_is_nan_never_default_calm():
    r = assemble_regime({}, LADDER)
    assert np.isnan(r.score) and r.n_blocks == 0


def test_out_of_range_state_rejected():
    with pytest.raises(ValueError):
        assemble_regime({"L2_fast_stress": 1.7}, LADDER)


def test_bucket_path_quantile_rules_and_warmup():
    rng = np.random.default_rng(0)
    s = rng.normal(0, 1, 2000)
    b = bucket_path(s, grid=(0.5, 0.8, 0.95), min_obs=252)
    assert (b[:251] == 0).all()                 # warm-up is NO bucket, not calm
    ok = b[252:]
    frac4 = (ok == 4).mean()
    assert 0.02 <= frac4 <= 0.10                # ~5% of days at/above the 0.95 cut
    assert set(np.unique(ok)) <= {1, 2, 3, 4}


def test_real_series_l2_only_assembly():
    # Real vaulted slice: L2 alone drives R; COVID floor must sit in the top bucket zone
    from quant.ladder import expanding_percentile
    from quant.ladder.fast_stress import drawdown_depth, fast_stress_composite, realized_vol
    sl = pd.read_csv("tests/fixtures/nifty_slice_2019_2020.csv", parse_dates=["Date"])
    r = sl["Close"].pct_change().dropna().values
    st = fast_stress_composite(expanding_percentile(realized_vol(r, 21), min_obs=252),
                               expanding_percentile(drawdown_depth(r), min_obs=252))
    d = sl["Date"].iloc[1:].reset_index(drop=True)
    i = d[d == "2020-03-23"].index[0]
    res = assemble_regime({"L2_fast_stress": float(st[i])}, LADDER)
    assert res.score > 0.9 and res.n_blocks == 1 and res.available_budget == pytest.approx(0.25)
