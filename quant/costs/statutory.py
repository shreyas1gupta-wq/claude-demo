"""Statutory cost engine — computes round-trip costs FROM config/costs.yaml rates.

Never hardcodes a rate: the FY2026-27 schedule lives in the registry with its expiry date
(re-verify every Budget — statutory cost has been hiked twice in 18 months)."""
from __future__ import annotations

from quant.registry import Registry


def round_trip_bps(reg: Registry, instrument: str) -> float:
    """Statutory-only round trip in bps of notional (before brokerage/spread/impact).

    instrument: 'cash_delivery' | 'index_futures'."""
    s = reg["costs"]["statutory_fy2026_27"]
    gst = None
    if instrument == "cash_delivery":
        r = s["cash_delivery"]
        gst = r["gst_on_fees"]
        frac = (r["stt_buy"] + r["stt_sell"] + r["stamp_buy"]
                + 2 * r["exch_per_side"] * (1 + gst)
                + 2 * r["sebi_per_side"] * (1 + gst))
    elif instrument == "index_futures":
        r = s["index_futures"]
        gst = r["gst_on_fees"]
        frac = (r["stt_sell"] + r["stamp_buy"]
                + 2 * r["exch_per_side"] * (1 + gst)
                + 2 * r["sebi_per_side"] * (1 + gst))
    else:
        raise ValueError(instrument)
    return frac * 1e4
