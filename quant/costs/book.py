"""Per-book turnover cost — the registry's turnover_cost_curve form, executable.

cost(mix) = sum_bucket[ turnover_share * (statutory + brokerage + impact(Y, sigma, size/ADV)) ]
(config/costs.yaml turnover_cost_curve: "cost depends on WHERE turnover is spent, never a
single scalar"). Everything comes from the registry — no rate, Y, ADV or brokerage number
lives in code; the ADV table's PROVISIONAL status therefore flows through every result and
is surfaced on the output object so no consumer can quietly forget it.

The consumers this was built for: full F2's book-level drag leg, MR1's cost stack, and the
paper-ledger gradings (PT-2's "modeled cost" column). Grid endpoints [lo, hi] are honored:
`turnover_cost_bps` returns the (lo, hi) pair, never a midpoint invented in code — the
caller decides which end its design registered.
"""
from __future__ import annotations

from dataclasses import dataclass

from quant.costs.impact import impact_bps
from quant.costs.statutory import round_trip_bps


@dataclass(frozen=True)
class BookCost:
    lo_bps: float          # optimistic end (Y lo, ADV hi, brokerage lo)
    hi_bps: float          # pessimistic end (Y hi, ADV lo, brokerage hi)
    statutory_bps: float   # the fixed statutory round-trip component
    adv_status: str        # PROVISIONAL until the live bhavcopy medians land (Phase 0)


def _pair(x):
    return (x[0], x[1]) if isinstance(x, list) else (float(x), float(x))


def turnover_cost_bps(reg, mix: dict, trade_size_cr: float,
                      sigma_daily_bps: float = 150.0,
                      instrument: str = "cash_delivery") -> BookCost:
    """Round-trip cost in bps of traded notional for a turnover MIX across ADV buckets.

    mix: {rank_bucket: share} over config's adv_by_rank_bucket_cr keys (shares sum to 1);
    trade_size_cr: per-name round-trip notional in Rs crore (the size that hits the book);
    sigma_daily_bps: daily vol assumption for the impact law (caller-supplied; a design
    that registered a different sigma passes it — 150bps/day ~ 24% annualized default [A]).
    Returns the (lo, hi) grid pair per the registry's own ranges."""
    costs = reg["costs"]
    adv_table = costs["adv_by_rank_bucket_cr"]
    y_lo, y_hi = _pair(costs["impact_model"]["Y"]["value"])
    br_lo, br_hi = _pair(costs["brokerage_per_side_bps"]["value"])
    stat = round_trip_bps(reg, instrument)

    shares = {k: v for k, v in mix.items() if v}
    if abs(sum(shares.values()) - 1.0) > 1e-9:
        raise ValueError(f"mix shares must sum to 1, got {sum(shares.values())}")
    lo = hi = 0.0
    for bucket, share in shares.items():
        adv_lo, adv_hi = _pair(adv_table[bucket])
        lo += share * (stat + 2 * br_lo
                       + 2 * impact_bps(y_lo, sigma_daily_bps, trade_size_cr / adv_hi))
        hi += share * (stat + 2 * br_hi
                       + 2 * impact_bps(y_hi, sigma_daily_bps, trade_size_cr / adv_lo))
    return BookCost(lo_bps=lo, hi_bps=hi, statutory_bps=stat,
                    adv_status=str(adv_table.get("verify_status", "unknown")))
