"""Market impact (square-root law), days-to-build, and the SAST position bound.

I = Y * sigma_daily * sqrt(Q / ADV)   (Gatheral/Bouchaud universality; Y in [0.5, 1.0] until the
India calibration in R3.1 narrows it). days_to_build = (Q/ADV) / participation. The golden tests
pin the corrected DESIGN §2.1 arithmetic so it cannot silently regress."""
from __future__ import annotations


def impact_bps(Y: float, sigma_daily_bps: float, q_over_adv: float) -> float:
    return Y * sigma_daily_bps * (q_over_adv ** 0.5)


def days_to_build(position_cr: float, adv_cr: float, participation: float) -> float:
    if adv_cr <= 0 or participation <= 0:
        raise ValueError("adv and participation must be positive")
    return (position_cr / adv_cr) / participation


def sast_mcap_floor_cr(position_cr: float, disclosure_threshold: float = 0.05) -> float:
    """Minimum target market cap to hold `position_cr` below the SAST disclosure threshold."""
    return position_cr / disclosure_threshold
