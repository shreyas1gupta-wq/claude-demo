"""Registry loader + cost-engine golden tests.

The golden numbers here are the AUDIT-CORRECTED figures (consistency audit, 2026-08-31); these
tests exist so the corrected arithmetic cannot silently regress (red-team requirement)."""
import pytest

from quant.costs import days_to_build, impact_bps, round_trip_bps, sast_mcap_floor_cr
from quant.registry import load_registry


@pytest.fixture(scope="module")
def reg():
    return load_registry(validate=True)


def test_registry_validates_and_loads(reg):
    assert reg["mandate"]["frozen"]["gross_leverage_cap"] == 1.5
    assert reg.param("mandate", "drawdown_violation_test", "K_days") == 15


def test_statutory_cash_delivery_golden(reg):
    # 0.1% + 0.1% STT + 0.015% stamp + 2*0.00317%*1.18 + 2*0.0001%*1.18 = 22.31 bps
    assert round_trip_bps(reg, "cash_delivery") == pytest.approx(22.31, abs=0.05)


def test_statutory_index_futures_golden_corrected(reg):
    # CORRECTED figure (audit): 5.66 bps, NOT the dossier's 7.7
    assert round_trip_bps(reg, "index_futures") == pytest.approx(5.66, abs=0.05)


def test_futures_vs_cash_ratio_about_4x(reg):
    ratio = round_trip_bps(reg, "cash_delivery") / round_trip_bps(reg, "index_futures")
    assert 3.5 < ratio < 4.5


def test_days_to_build_conservative_rank300_corrected():
    """DESIGN §2.1 corrected: Rs1,375cr at ADV 20-40cr, 10%/day -> 344-688 trading days."""
    assert days_to_build(1375, 40, 0.10) == pytest.approx(343.75)
    assert days_to_build(1375, 20, 0.10) == pytest.approx(687.5)


def test_days_to_build_rank100_150_corrected():
    """Rs1,375cr at ADV 80-150cr, 10%/day -> ~92-172 days (18-34 weeks)."""
    assert 91 < days_to_build(1375, 150, 0.10) < 92
    assert 171 < days_to_build(1375, 80, 0.10) < 172


def test_sast_floor_corrected_range():
    """Audit-corrected: Rs11,000cr at the book floor, Rs30,000cr at the top."""
    assert sast_mcap_floor_cr(10000 * 0.055) == pytest.approx(11000)
    assert sast_mcap_floor_cr(25000 * 0.06) == pytest.approx(30000)


def test_impact_scaling_is_square_root():
    one = impact_bps(0.75, 200, 0.01)
    four = impact_bps(0.75, 200, 0.04)
    assert four == pytest.approx(2 * one)


def test_r4_worst_case_matches_validator(reg):
    """Reproduce validator.py's ceiling check from registry values (single source of truth)."""
    eb = reg["risk"]["effective_beta_identity"]
    rb = reg["risk"]["regime_buckets"]["R4_crisis"]
    beta = eb["downside_beta_tilt"]["value"][1]
    lev = rb["leverage_range"][1]
    hedge = rb["hedge_ratio_range"][0]
    he = eb["hedge_effectiveness_fast_crash"]["value"][0]
    fall = eb["worst_case_fall_while_in_R4"]["value"]
    gap = eb["gap_floor"]["value"][1]
    worst = beta * lev * (1 - hedge * he) * fall + gap
    assert worst <= reg["mandate"]["frozen"]["drawdown_absolute_ceiling"][1]
