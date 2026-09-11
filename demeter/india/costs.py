#!/usr/bin/env python3
"""Indian index-derivative cost model, and the futures-versus-options comparison it exists to answer.

Every statutory rate below is the rate in force from 1 April 2026 (Union Budget 2026 raised STT on
futures from 0.02% to 0.05% and on options from 0.10% to 0.15%). Rates are quoted as a fraction of
the base they apply to: futures charges apply to NOTIONAL turnover, option charges apply to PREMIUM.
That difference is the whole point of this file.

Sources: Union Budget 2026 (STT), NSE F&O transaction-charge schedule, state stamp-duty schedule for
derivatives, standard discount-brokerage flat fee. See PROVENANCE.md for links and caveats.

Run:  python3 costs.py       # prints the comparison tables
"""
from __future__ import annotations
import math
from dataclasses import dataclass, field

# ----------------------------------------------------------------- statutory rates (fractions)
STT_FUT_SELL = 0.0005        # 0.05% of notional, sell side only (from 2026-04-01; was 0.02%)
STT_OPT_SELL = 0.0015        # 0.15% of PREMIUM, sell side only (from 2026-04-01; was 0.10%)
STT_OPT_EXERCISE = 0.00125   # 0.125% of INTRINSIC settlement value if an ITM option is exercised at expiry
EXCH_FUT = 0.000019          # ~0.0019% of notional per side (NSE F&O futures)
EXCH_OPT = 0.000355          # ~0.0355% of PREMIUM per side (NSE F&O options)
SEBI_FEE = 0.000001          # 0.0001% (Rs 10 per crore) per side, on turnover/premium
STAMP_FUT_BUY = 0.00002      # 0.002% of notional, buy side only
STAMP_OPT_BUY = 0.00003      # 0.003% of premium, buy side only
GST = 0.18                   # on brokerage + exchange charges + SEBI fee
BROKERAGE_PER_ORDER = 20.0   # rupees, flat (discount broker)


@dataclass
class Instrument:
    """One tradeable leg and the market frictions that apply to it."""
    name: str
    lot_notional: float          # rupees of index notional per lot
    half_spread_bp_of_base: float  # half bid-ask, in bp of the base the spread is quoted on
    is_option: bool = False


def futures_round_turn(notional: float, half_spread_bp: float = 1.5) -> dict:
    """Cost of one buy-then-sell round turn in index futures, in rupees and bp of notional."""
    stt = STT_FUT_SELL * notional
    exch = EXCH_FUT * notional * 2
    sebi = SEBI_FEE * notional * 2
    stamp = STAMP_FUT_BUY * notional
    brok = BROKERAGE_PER_ORDER * 2
    gst = GST * (exch + sebi + brok)
    slip = (half_spread_bp / 1e4) * notional * 2
    total = stt + exch + sebi + stamp + brok + gst + slip
    return {"stt": stt, "exchange": exch, "sebi": sebi, "stamp": stamp, "brokerage": brok, "gst": gst,
            "slippage": slip, "total": total, "bp_of_notional": total / notional * 1e4}


def option_round_turn(premium_value: float, notional: float, n_legs: int = 1,
                      half_spread_bp_of_premium: float = 25.0, sell_first: bool = True) -> dict:
    """Cost of opening and closing an option position, in rupees and bp of the DELTA notional it carries.

    `premium_value` is the total rupee premium across all legs at entry (assumed similar at exit).
    STT hits only the sell side: once at entry for a short leg, once at exit for a long leg. Either
    way a round turn pays it exactly once per leg, which is what is charged here.
    """
    stt = STT_OPT_SELL * premium_value
    exch = EXCH_OPT * premium_value * 2
    sebi = SEBI_FEE * premium_value * 2
    stamp = STAMP_OPT_BUY * premium_value
    brok = BROKERAGE_PER_ORDER * 2 * n_legs
    gst = GST * (exch + sebi + brok)
    slip = (half_spread_bp_of_premium / 1e4) * premium_value * 2
    total = stt + exch + sebi + stamp + brok + gst + slip
    return {"stt": stt, "exchange": exch, "sebi": sebi, "stamp": stamp, "brokerage": brok, "gst": gst,
            "slippage": slip, "total": total, "bp_of_notional": total / notional * 1e4}


# ----------------------------------------------------------------- Black-Scholes (no scipy needed)
def _nd(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def bs(spot, strike, iv, years, rate=0.055, div=0.011, call=True):
    """European option price and delta."""
    if years <= 0:
        intr = max(0.0, (spot - strike) if call else (strike - spot))
        return intr, (1.0 if (call and spot > strike) else (-1.0 if (not call and spot < strike) else 0.0))
    d1 = (math.log(spot / strike) + (rate - div + 0.5 * iv * iv) * years) / (iv * math.sqrt(years))
    d2 = d1 - iv * math.sqrt(years)
    df, dq = math.exp(-rate * years), math.exp(-div * years)
    if call:
        return spot * dq * _nd(d1) - strike * df * _nd(d2), dq * _nd(d1)
    return strike * df * _nd(-d2) - spot * dq * _nd(-d1), -dq * _nd(-d1)


def cost_per_unit_exposure(spot, lots_notional, structure, iv, days, half_spread_bp_premium=25.0):
    """Cost of one round turn per 1.0 of delta-weighted index notional, in bp.

    `structure` is a list of (kind, moneyness, quantity_sign) where kind is 'C' or 'P', moneyness is
    strike/spot, and the sign is +1 for long, -1 for short. Quantities are scaled so the structure
    carries one unit of delta exposure.
    """
    years = days / 365.0
    prem_per_unit, delta_per_unit = 0.0, 0.0
    for kind, mny, sgn in structure:
        px, dl = bs(spot, spot * mny, iv, years, call=(kind == "C"))
        prem_per_unit += abs(px)      # cost base is gross premium traded, long or short
        delta_per_unit += sgn * dl
    if abs(delta_per_unit) < 1e-9:
        return None
    scale = 1.0 / abs(delta_per_unit)              # units needed for one unit of delta exposure
    notional = lots_notional
    premium_value = prem_per_unit * scale / spot * notional
    c = option_round_turn(premium_value, notional, n_legs=len(structure),
                          half_spread_bp_of_premium=half_spread_bp_premium)
    return {"bp_of_notional": c["bp_of_notional"], "premium_pct_of_notional": premium_value / notional * 100,
            "delta_per_unit": delta_per_unit, "detail": c}


def main():
    spot, notional = 24000.0, 1_500_000.0
    print(f"Index {spot:,.0f}, contract notional Rs {notional:,.0f}, statutory rates from 2026-04-01\n")

    print("=== A. Index FUTURES round turn (cost on NOTIONAL) ===")
    for name, hs in [("Nifty futures (tight)", 1.0), ("Nifty futures (normal)", 1.5), ("MIDCPNIFTY futures", 4.0)]:
        c = futures_round_turn(notional, hs)
        print(f"{name:26s} Rs {c['total']:8,.0f}  = {c['bp_of_notional']:5.2f} bp   "
              f"(STT {c['stt']/notional*1e4:.2f} + slip {c['slippage']/notional*1e4:.2f} + rest {(c['total']-c['stt']-c['slippage'])/notional*1e4:.2f})")

    print("\n=== B. OPTION structures, cost per unit of delta exposure (cost on PREMIUM) ===")
    print(f"{'structure':38s} {'days':>5} {'IV':>5} {'prem % ntl':>11} {'delta':>7} {'bp of notional':>15}")
    rows = [
        ("Synthetic long: +ATM call / -ATM put", [("C", 1.00, +1), ("P", 1.00, -1)], 30, 0.12, 25),
        ("Synthetic long, 90-day", [("C", 1.00, +1), ("P", 1.00, -1)], 90, 0.13, 35),
        ("Synthetic long, 1-year", [("C", 1.00, +1), ("P", 1.00, -1)], 365, 0.14, 120),
        ("Long ATM call only", [("C", 1.00, +1)], 30, 0.12, 25),
        ("Long 2% ITM call", [("C", 0.98, +1)], 30, 0.125, 30),
        ("Long 10% deep-ITM call", [("C", 0.90, +1)], 30, 0.16, 60),
        ("Short 10% deep-ITM put", [("P", 1.10, -1)], 30, 0.16, 60),
        ("Short ATM put", [("P", 1.00, -1)], 30, 0.12, 25),
        ("Short 5% OTM put", [("P", 0.95, -1)], 30, 0.145, 30),
        ("Bull call spread ATM/+3%", [("C", 1.00, +1), ("C", 1.03, -1)], 30, 0.12, 30),
    ]
    for label, struct, days, iv, hs in rows:
        r = cost_per_unit_exposure(spot, notional, struct, iv, days, hs)
        print(f"{label:38s} {days:5d} {iv*100:4.0f}% {r['premium_pct_of_notional']:10.2f}% "
              f"{r['delta_per_unit']:7.2f} {r['bp_of_notional']:14.2f}")

    print("\n=== C. Annual cost drag at various turnover rates (bp of capital per year) ===")
    fut = futures_round_turn(notional, 1.5)["bp_of_notional"]
    syn = cost_per_unit_exposure(spot, notional, [("C", 1.00, +1), ("P", 1.00, -1)], 0.12, 30, 25)["bp_of_notional"]
    print(f"{'round turns / year':>20} {'futures 2x':>12} {'synthetic 2x':>14} {'saving':>10}")
    for rt in [4, 9, 12, 25, 50]:
        f_ = fut * rt * 2 / 100
        s_ = syn * rt * 2 / 100
        print(f"{rt:20d} {f_:11.2f}% {s_:13.2f}% {f_-s_:9.2f}%")
    print("\nA 30-day synthetic must also be ROLLED 12 times a year even if the signal never changes:")
    print(f"  futures roll (12/yr, 2x):    {fut*12*2/100:.2f}% a year")
    print(f"  synthetic roll (12/yr, 2x):  {syn*12*2/100:.2f}% a year")
    print(f"  90-day synthetic (4 rolls):  {cost_per_unit_exposure(spot, notional, [('C',1.0,1),('P',1.0,-1)], 0.13, 90, 35)['bp_of_notional']*4*2/100:.2f}% a year")

    print("\n=== D. The expiry trap ===")
    itm = 0.10 * notional
    print(f"Letting a 10% ITM option expire instead of squaring off: STT {STT_OPT_EXERCISE*100:.3f}% of "
          f"Rs {itm:,.0f} intrinsic = Rs {STT_OPT_EXERCISE*itm:,.0f} = {STT_OPT_EXERCISE*itm/notional*1e4:.2f} bp of notional.")


if __name__ == "__main__":
    main()
