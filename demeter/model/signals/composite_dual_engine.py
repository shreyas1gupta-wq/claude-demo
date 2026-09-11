"""composite_dual_engine -- the inference note's section-7 composite: a shock exit protecting a dissipation
re-entry, a VIX-regime leverage tier for the ordinary state, and a minimum hold after every state change.

Rules (all decided at the close of day t from data up to that close; the engine applies them to day t+1).
Three modes -- TIER (ordinary), OUT (after a shock), REBOUND (levered burst) -- and discrete leverage {0, 1, 3}.

  1. ORDINARY TIER by implied-vol regime (VIX close, ffilled over its 4 isolated NaNs), a three-state machine with
     one shared hysteresis fraction `hyst` (the vix_vrp construction):
        CALM     entered when VIX < v_calm*(1-hyst), left when VIX > v_calm         -> LEV_CALM   = 3x
        ELEVATED everything in between (also the start state)                       -> LEV_ELEV   = 1x
        STRESSED entered when VIX > v_high, left when VIX < v_high*(1-hyst)         -> LEV_STRESS = cash
     The STRESSED = cash level is the lesson of lens 5 (vix_vrp): a 1x floor rides the grinding bears; the
     ordinary state must itself de-lever when vol is persistently elevated. The tier is not monotone in vol
     overall because rule 3 allows 3x at VIX >= 30.
  2. SHOCK EXIT -> cash (mode OUT), always allowed, from any mode. Trigger = either of
        a. two-session shock: r_t + r_{t-1} < -k * sqrt(2) * sigma, sigma = trailing 21-day daily std measured up
           to the close BEFORE both days (lens 1's cumulative form; a single -3% day at 12% vol is z = -2.8 and
           does not trip k >= 3.5, two -3% days are -5.6 and do);
        b. VIX jump on a down day: VIX > (1+J_JUMP) x its mean over the previous 10 sessions while VIX >= 20
           (lens 1's frozen trigger, borrowed as constants).
     OUT persists until `out_days` sessions have passed since the LAST shock event (a two-session shock, a
     single day below -k sigma, or a VIX jump -- each restarts the clock), then the book returns to the TIER
     (which is itself VIX-gated, so returning "into" a bear means returning to cash or 1x).
  3. DISSIPATION RE-ENTRY -> LEV_REB (mode REBOUND), from TIER or OUT, never from inside a burst. Fires when
        VIX <= (1 - VIX_FALL) x max(VIX over the trailing VIX_WIN sessions)   [vol dissipating]
        VIX >= VIX_MIN                                                       [... from an extreme]
        RSI(2) < RSI_MAX                                                     [price still being sold]
     -- lens 2's frozen strict trigger (0.25 / 30 / 30 / 20), borrowed as constants. Held HOLD_DAYS sessions,
     ended early by the burst STOP (burst equity at LEV_REB down STOP or more) or by a shock trigger. On exit ->
     OUT if a shock fired that day, else TIER. After a stop-out no new burst for HOLD_DAYS sessions.
     LEV_REB is decided by the spurious-re-entry census in DEV (see design note), not by the record's 3x.
  4. HYSTERESIS: after any change of the target leverage, no further NON-EMERGENCY change (tier up or down,
     OUT -> TIER, a new burst) for `min_hold` sessions. Emergency changes -- the shock exit and the burst stop --
     are exempt. Burst expiry after HOLD_DAYS is structural and also exempt.
  5. Before 1990 (no VIX) the signal is cash; warm-up -> 0. This is a VIX lens; dev_1950 is not applicable.

Parameters (6 tunables; development window 1990-01-01..2012-06-30 via dev_harness.py grids, see design note)
  v_calm    VIX level below which the ordinary tier is 3x (CALM exit level; entry at v_calm*(1-hyst))
  v_high    VIX level above which the ordinary tier is cash (STRESSED entry; exit at v_high*(1-hyst))
  hyst      shared hysteresis fraction of the two VIX bands
  k         two-session shock size in trailing sigmas
  out_days  sessions OUT after the last shock event before the tier is resumed
  min_hold  minimum sessions between non-emergency state changes

Structural constants (declared, NOT tuned, with the reason)
  LEV_CALM 3 / LEV_ELEV 1     the record's "3x calm / ~1x elevated" ordinary tier (inference note s7 ingredient 3)
  LEV_STRESS 0                lens 5's DEV finding: the 15-30 VIX band is sat out, that is what survives 2000-02/2008
  LEV_REB                     set from the census (3 allowed only if the two-bear entries are not mostly losses)
  SIGMA_WIN 21, SHOCK_DAYS 2  firm-wide RV21 scale; two sessions = smallest span that is a regime statement
  J_JUMP 0.30, VIX_BASE 10, VIX_FLOOR 20   lens 1's frozen VIX-jump trigger, borrowed unchanged
  VIX_FALL 0.25, VIX_WIN 30, VIX_MIN 30, RSI_MAX 20, HOLD_DAYS 10, STOP 0.10   lens 2's frozen re-entry, borrowed
  unchanged (the strict version: 4 bear firings at 50% negative; looser versions 75-83% negative)

Known failure modes: a crash from a calm base costs the first day at 3x before the exit can fire (27-Feb-2007
-3.5% = -10.5%); a grinding bear that keeps VIX in the ELEVATED band (20 < VIX < v_high) is ridden at 1x; a
V-shaped rebound with VIX making higher highs while price makes lower lows (Oct-Nov 2008) shows no dissipation
until late; the re-entry is rare (single digits in 22 years) so its contribution to a 22-year Sharpe is small
by construction; whipsaw at 3x when VIX oscillates around v_calm is the cost of the calm tier and is what
`hyst` and `min_hold` are for.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

import features as F

NAME = "composite_dual_engine"
FAMILY = "VIX-regime tier (3x/1x/cash, hysteresis) + two-session/VIX-jump shock exit + strict VIX-dissipation 3x re-entry + minimum hold"
HYPOTHESIS = (
    "Demeter's record needs four things at once: calm-regime leverage for the equity premium, a fast exit on the first "
    "statistically clean sign of a volatility regime change, a levered re-entry at capitulation lows while implied vol is "
    "still high but already dissipating, and enough hysteresis to sit out whole months. Each part alone failed in DEV "
    "(a crash exit rides grinding bears; a level gate misses rebounds; dissipation alone is a trap); the composite "
    "should keep the calm-year 3x of the tier, the bear-market cash of the VIX-stress level, and add the rare rebound."
)

# ---- structural constants (see docstring)
LEV_CALM, LEV_ELEV, LEV_STRESS = 3.0, 1.0, 0.0
LEV_REB = 3.0
SIGMA_WIN, SHOCK_DAYS = 21, 2
J_JUMP, VIX_BASE, VIX_FLOOR = 0.30, 10, 20.0
VIX_FALL, VIX_WIN, VIX_MIN, RSI_MAX, HOLD_DAYS, STOP = 0.25, 30, 30.0, 20.0, 10, 0.10

DEFAULT_PARAMS = dict(v_calm=15.5, v_high=26.0, hyst=0.12, k=4.0, out_days=15, min_hold=10)


def vix_regime(vix: pd.Series, v_calm: float, v_high: float, hyst: float) -> np.ndarray:
    """Causal three-state machine on the VIX close: 0 = CALM, 1 = ELEVATED (start), 2 = STRESSED. NaN holds state."""
    calm_in, calm_out = v_calm * (1.0 - hyst), v_calm
    hi_in, hi_out = v_high, v_high * (1.0 - hyst)
    if calm_out > hi_in:                          # degenerate perturbations: keep the machine well-ordered
        calm_out = hi_in
    if hi_out < calm_in:
        hi_out = calm_in
    v = vix.to_numpy(dtype=float)
    out = np.empty(len(v), dtype=np.int8)
    st = 1
    for i in range(len(v)):
        x = v[i]
        if not np.isnan(x):
            if st == 0:
                if x > hi_in:
                    st = 2
                elif x > calm_out:
                    st = 1
            elif st == 1:
                if x > hi_in:
                    st = 2
                elif x < calm_in:
                    st = 0
            else:
                if x < calm_in:
                    st = 0
                elif x < hi_out:
                    st = 1
        out[i] = st
    return out


def signal(df: pd.DataFrame, v_calm: float = 15.5, v_high: float = 26.0, hyst: float = 0.12, k: float = 4.0,
           out_days: int = 15, min_hold: int = 10) -> pd.Series:
    out_days = max(int(round(out_days)), 1)
    min_hold = max(int(round(min_hold)), 1)
    ret, px = df["spx_ret"], df["spx_px"]
    n = len(df)

    # ---- 1. ordinary tier by VIX regime
    vix = df["vix_close"].ffill()
    reg = vix_regime(vix, v_calm, v_high, hyst)
    tier_lev = np.array([LEV_CALM, LEV_ELEV, LEV_STRESS], dtype=float)[reg]

    # ---- 2. shock exit
    sigma_prev = ret.rolling(SIGMA_WIN, min_periods=SIGMA_WIN).std(ddof=1).shift(1)            # through t-1
    z1 = ret / sigma_prev
    z2 = ret.rolling(SHOCK_DAYS, min_periods=SHOCK_DAYS).sum() / (sigma_prev.shift(SHOCK_DAYS - 1) * np.sqrt(SHOCK_DAYS))
    shock_day = (z1 < -k).fillna(False)
    two_day = (z2 < -k).fillna(False)
    vix_base = vix.shift(1).rolling(VIX_BASE, min_periods=VIX_BASE).mean()
    vol_jump = ((vix > (1.0 + J_JUMP) * vix_base) & (vix >= VIX_FLOOR) & (ret < 0)).fillna(False)
    trigger = (two_day | vol_jump).to_numpy()
    shock_any = shock_day | two_day | vol_jump
    since_shock = F.days_since_true(shock_any).fillna(np.inf).to_numpy()

    # ---- 3. dissipation re-entry condition
    vix_max = vix.rolling(VIX_WIN, min_periods=VIX_WIN).max()
    rsi2 = F.rsi(px, 2)
    dis = ((vix <= (1.0 - VIX_FALL) * vix_max) & (vix >= VIX_MIN) & (rsi2 < RSI_MAX)).fillna(False).to_numpy()

    x_ex = (df["spx_tr_ret"] - df["rf_daily"]).fillna(0.0).to_numpy()
    warm = (vix.notna() & sigma_prev.notna()).to_numpy()

    out = np.zeros(n, dtype=float)
    mode = 0                                # 0 TIER, 1 OUT, 2 REBOUND
    cur = 0.0                               # current target leverage
    last_change = -10**9
    held, cum, block_until = 0, 1.0, -1
    for i in range(n):
        if not warm[i]:
            out[i] = 0.0
            continue
        emergency = False
        if mode == 2:                       # burst was in effect during day i
            cum *= 1.0 + LEV_REB * x_ex[i]
            held += 1
            stopped = cum <= 1.0 - STOP
            if stopped or held >= HOLD_DAYS or trigger[i]:
                mode = 1 if trigger[i] else 0
                emergency = True            # burst exit is structural / emergency: not subject to min_hold
                if stopped:
                    block_until = i + HOLD_DAYS
        if trigger[i] and mode != 1:        # shock exit always wins
            mode = 1
            emergency = True
        free = (i - last_change) >= min_hold
        if mode != 2 and dis[i] and not emergency and i >= block_until and free:
            mode, held, cum = 2, 0, 1.0
        elif mode == 1 and since_shock[i] >= out_days and free:
            mode = 0
        if mode == 2:
            target = LEV_REB
        elif mode == 1:
            target = 0.0
        else:
            target = tier_lev[i]
            if target != cur and not free and not emergency:
                target = cur                # tier change waits for the minimum hold
        if target != cur:
            cur = target
            last_change = i
        out[i] = cur
    return pd.Series(out, index=df.index).clip(0.0, 3.0)
