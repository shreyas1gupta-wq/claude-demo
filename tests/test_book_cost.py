"""The per-book turnover-cost curve vs hand-computed truth + the registry's own range."""
import pytest

from quant.costs.book import turnover_cost_bps
from quant.costs.impact import impact_bps
from quant.costs.statutory import round_trip_bps
from quant.registry.loader import load_registry

REG = load_registry(validate=False)


def test_single_bucket_exact_arithmetic():
    stat = round_trip_bps(REG, "cash_delivery")
    got = turnover_cost_bps(REG, {"r1_50": 1.0}, trade_size_cr=10.0, sigma_daily_bps=150.0)
    lo_want = stat + 2 * 1.0 + 2 * impact_bps(0.5, 150.0, 10.0 / 800)
    hi_want = stat + 2 * 5.0 + 2 * impact_bps(1.0, 150.0, 10.0 / 500)
    assert got.lo_bps == pytest.approx(lo_want, abs=1e-9)
    assert got.hi_bps == pytest.approx(hi_want, abs=1e-9)
    assert got.statutory_bps == pytest.approx(stat)


def test_reproduces_registry_liquid_range():
    # the registry's own at_100pct_liquid grid is [35, 70] bps round trip — the executable
    # curve at a liquid mix / ~10cr clip must land in that neighborhood, not another world
    lo_r, hi_r = REG["costs"]["turnover_cost_curve"]["at_100pct_liquid"]["value"]
    got = turnover_cost_bps(REG, {"r1_50": 1.0}, trade_size_cr=10.0)
    assert lo_r * 1e4 * 0.7 <= got.lo_bps <= hi_r * 1e4 * 1.3
    assert lo_r * 1e4 * 0.7 <= got.hi_bps <= hi_r * 1e4 * 1.3


def test_tail_bucket_costs_dominate():
    liquid = turnover_cost_bps(REG, {"r1_50": 1.0}, trade_size_cr=5.0)
    tail = turnover_cost_bps(REG, {"r501_750": 1.0}, trade_size_cr=5.0)
    assert tail.hi_bps > 3 * liquid.hi_bps      # the thin bucket is where cost lives


def test_mix_must_sum_to_one_and_provisional_surfaces():
    with pytest.raises(ValueError):
        turnover_cost_bps(REG, {"r1_50": 0.5}, trade_size_cr=5.0)
    got = turnover_cost_bps(REG, {"r1_50": 0.5, "r301_500": 0.5}, trade_size_cr=5.0)
    assert got.adv_status == "PROVISIONAL"      # the warning travels with every number
