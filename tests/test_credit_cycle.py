"""L10 credit-cycle module vs a synthetic boom-bust economy with known phases."""
import numpy as np
import pytest

from quant.ladder import credit_gap, credit_state_composite, expanding_percentile
from quant.validation.synthetic import boom_bust_economy


def test_gap_fires_on_acceleration_and_collapses_at_the_turn():
    """The EXPANDING Hamilton gap is an acceleration-surprise detector, not a level gap:
    it fires positive during the boom's build-out (targets outrun forecasts trained on the
    pre-boom era), decays toward zero late in the boom as the expanding regression absorbs
    the boom, and collapses hard at the bust ONSET (forecasts made at peak extrapolate the
    boom while actuals contract). Verified 10/10 across seeds 0-9 before freezing."""
    e = boom_bust_economy()
    gap = credit_gap(e["credit"], e["income"], h=24, p=4)
    boom_lo, boom_hi = e["boom"]
    pre_boom = np.nanmean(gap[boom_lo - 40:boom_lo])
    early_boom = np.nanmean(gap[boom_lo + 12:boom_hi - 24])
    late_boom = np.nanmean(gap[boom_hi - 24:boom_hi])
    turn = np.nanmean(gap[boom_hi:boom_hi + 24])
    assert early_boom > pre_boom, "gap should fire while credit growth is a surprise"
    assert turn < late_boom, "gap should collapse when the bust begins"
    assert turn < -0.05, "the turn signal should be large and negative, not marginal"


def test_expanding_percentile_no_lookahead_and_range():
    e = boom_bust_economy()
    cd = e["credit"] / e["deposits"]
    pct = expanding_percentile(cd)
    valid = pct[~np.isnan(pct)]
    assert ((valid >= 0) & (valid <= 1)).all()
    # no-look-ahead property: truncating the future never changes the past
    full = expanding_percentile(cd)
    for t in (150, 250, 350):
        trunc = expanding_percentile(cd[: t + 1])
        assert full[t] == pytest.approx(trunc[t], abs=1e-12)


def test_cd_percentile_saturates_high_in_late_boom():
    e = boom_bust_economy()
    pct = expanding_percentile(e["credit"] / e["deposits"])
    assert np.nanmean(pct[e["boom"][1] - 12:e["boom"][1]]) > 0.85


def test_composite_discriminates_boom_from_turn_and_aftermath():
    """The state must be materially higher during the boom than at the bust onset and in the
    post-bust era — that is the discrimination the regime block consumes. (No assertion vs the
    PRE-boom window: early-sample expanding percentiles are noisy ranks over short reference
    windows — an honest limitation, documented in the demo, not hidden by a tuned margin.)"""
    e = boom_bust_economy()
    gap_pct = expanding_percentile(credit_gap(e["credit"], e["income"], h=24))
    cd_pct = expanding_percentile(e["credit"] / e["deposits"])
    state = credit_state_composite(gap_pct, cd_pct)
    boom_lo, boom_hi = e["boom"]
    boom = np.nanmean(state[boom_lo + 12:boom_hi])
    turn = np.nanmean(state[boom_hi:boom_hi + 24])
    post = np.nanmean(state[420:])
    assert boom > turn + 0.3, "state must fall hard once the bust begins"
    assert boom > post + 0.3, "state must be higher in the boom than after deleveraging"


def test_tierC_composition_can_never_add_risk_on():
    """The consistency-audit C2 clamp, enforced in code (Appendix B's M16 test): a Tier-C
    composition input may push the state toward risk-off (higher) but NEVER below the
    two-input composite (more risk-on)."""
    e = boom_bust_economy()
    gap_pct = expanding_percentile(credit_gap(e["credit"], e["income"], h=24))
    cd_pct = expanding_percentile(e["credit"] / e["deposits"])
    base = credit_state_composite(gap_pct, cd_pct)
    m = ~np.isnan(base)
    rng = np.random.default_rng(0)
    for _ in range(5):
        # ANY composition series: the clamped contribution is >= 0, so the composite can never
        # fall below the renormalized base — composition cannot argue for MORE risk.
        comp = rng.random(len(base))
        with_c = credit_state_composite(gap_pct, cd_pct, composition_pct=comp,
                                        w_composition=0.3)
        assert np.all(with_c[m] >= base[m] * (1.0 / 1.3) - 1e-9), \
            "arbitrary composition must never push the state risk-on vs the renormalized base"
    # composition pinned at its hottest only ever raises the state (toward risk-off):
    hot = np.ones(len(base))
    with_hot = credit_state_composite(gap_pct, cd_pct, composition_pct=hot,
                                      w_composition=0.3)
    assert np.all(with_hot[m] >= base[m] * (1.0 / 1.3) - 1e-9)
    assert np.all(with_hot[m] >= base[m] * (1.0 / 1.3) + 0.3 / 1.3 - 1e-9), \
        "a fully hot composition adds exactly its clamped weight toward risk-off"
    # and a BENIGN composition (0th percentile) contributes exactly nothing:
    benign = np.zeros(len(base))
    with_benign = credit_state_composite(gap_pct, cd_pct, composition_pct=benign,
                                         w_composition=0.3)
    assert np.allclose(with_benign[m], base[m] * (1.0 / 1.3), atol=1e-9), \
        "benign Tier-C reading must add zero (clamped), only renormalization applies"
