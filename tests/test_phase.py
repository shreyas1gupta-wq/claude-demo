"""Phase-space state representation (quant/ladder/phase.py) vs known trajectories.

Assertions were frozen only after holding across seeds 0-7 (see the dev log in the phase-state
decision record): sine rotation is deterministic; hysteresis flip counts and boom/turn direction
fractions were multi-seed checked before the thresholds below were written down.
"""
import numpy as np
import pytest

from quant.ladder import expanding_percentile
from quant.ladder.phase import QUADRANTS, phase_label, phase_state
from quant.validation.synthetic import boom_bust_economy


def test_same_level_different_trail_on_a_sine():
    """The principal's exact scenario: 0.6 reached from below must be labelled U (rising), 0.6
    reached from above must be labelled D (falling) — same level, different phase."""
    t = np.arange(480)
    sine = np.sin(2 * np.pi * t / 120)
    p = phase_state(sine, k_slope=6, smooth=3)
    band = np.abs(sine - 0.6) < 0.08
    up = [i for i in np.where(band)[0] if p.direction[i] == 1]
    down = [i for i in np.where(band)[0] if p.direction[i] == -1]
    assert len(up) > 0 and len(down) > 0, "0.6 must occur on both legs of the wave"
    assert phase_label(0.6, 1) == "0.60U" and phase_label(0.6, -1) == "0.60D"
    # and the quadrants differ: rising-high = boom, falling-high = slowdown
    assert {QUADRANTS[p.quadrant[i]] for i in up} == {"boom"}
    assert {QUADRANTS[p.quadrant[i]] for i in down} == {"slowdown"}


def test_sine_rotates_through_quadrants_in_canonical_order():
    t = np.arange(480)
    p = phase_state(np.sin(2 * np.pi * t / 120), k_slope=6, smooth=3)
    codes = p.quadrant[p.quadrant >= 0]
    seq = [codes[0]] + [c for i, c in enumerate(codes[1:], 1) if c != codes[i - 1]]
    assert all((b - a) % 4 == 1 for a, b in zip(seq, seq[1:])), \
        "recovery -> boom -> slowdown -> downturn -> recovery, never skipping backwards"


def test_hysteresis_suppresses_noise_flips():
    """On a noisy sine with 8 true turning points, the dead-band keeps direction changes within
    3x the true count while naive sign-of-diff flips hundreds of times. (Held on seeds 0-5:
    hysteresis 10-19 flips vs naive 302-325.)"""
    t = np.arange(480)
    sine = np.sin(2 * np.pi * t / 120)
    rng = np.random.default_rng(3)
    noisy = sine + 0.15 * rng.standard_normal(480)
    p = phase_state(noisy, k_slope=6, smooth=3)
    d = p.direction[~np.isnan(p.direction)]
    flips = int((np.diff(d) != 0).sum())
    naive = np.sign(np.diff(noisy))
    naive_flips = int((np.diff(naive) != 0).sum())
    assert flips <= 24, f"hysteresis should keep flips near the 8 true turns, got {flips}"
    assert naive_flips > 250, "sanity: the naive labelling really is that noisy"


def test_credit_cd_ratio_is_U_through_boom_and_D_after_the_turn():
    """On the boom-bust economy the CD-ratio percentile must read U through the boom and D after
    the peak. (Held at fraction 1.00/1.00 on all of seeds 0-7 before freezing the 0.9 bar.)"""
    e = boom_bust_economy()
    cp = expanding_percentile(e["credit"] / e["deposits"])
    p = phase_state(cp, level_mid=0.5)
    boom_lo, boom_hi = e["boom"]
    rising = np.nanmean(p.direction[boom_lo + 12:boom_hi - 12] == 1)
    falling = np.nanmean(p.direction[boom_hi + 10:boom_hi + 60] == -1)
    assert rising > 0.9 and falling > 0.9


def test_age_counts_periods_within_quadrant():
    t = np.arange(480)
    p = phase_state(np.sin(2 * np.pi * t / 120), k_slope=6, smooth=3)
    valid = np.where(p.quadrant >= 0)[0]
    for i in valid[1:]:
        if p.quadrant[i] == p.quadrant[i - 1] and not np.isnan(p.age[i - 1]):
            assert p.age[i] == p.age[i - 1] + 1
        elif p.quadrant[i - 1] >= 0:
            assert p.age[i] == 1


def test_truncating_the_future_never_changes_the_past():
    e = boom_bust_economy()
    cp = expanding_percentile(e["credit"] / e["deposits"])
    full = phase_state(cp, level_mid=0.5)
    for T in (200, 300, 400):
        tr = phase_state(cp[:T + 1], level_mid=0.5)
        assert (np.nan_to_num(full.direction[:T + 1], nan=9)
                == np.nan_to_num(tr.direction, nan=9)).all()
        assert (full.quadrant[:T + 1] == tr.quadrant).all()


def test_phase_label_nan_safe():
    assert phase_label(float("nan"), 1) == "nan"
    assert phase_label(0.6, float("nan")) == "nan"
