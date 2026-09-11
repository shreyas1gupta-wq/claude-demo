"""sticky_tier -- the whipsaw minimiser: discrete {0,1,2,3} leverage tiers from a trailing EWMA volatility regime,
with wide hysteresis, a persistence requirement, a re-levering cooling-off period and a weekly re-levering cadence.

Rules (decided at the close of day t from data up to that close; the engine applies the level to day t+1)
--------------------------------------------------------------------------------------------------------
1. VOL REGIME. sigma_t = max( EWMA-vol(halflife hl), EWMA-vol(halflife hl*long_mult) ) of daily S&P 500 price
   returns, annualised (features.ewma_vol, 20-session warm-up; pre-warm-up = cash). The slow leg is the regime
   memory: after a shock the fast leg decays in weeks but the slow leg keeps the regime "high-vol" for months, so a
   lull inside a bear does not re-lever (grid A, plain EWMA, re-levered to 1x on every lull of 2000-02 -- Aug-00,
   Jul-01, Jan/Apr-02 -- each followed by a -6% month). Trailing only. No VIX, so the rule runs from 1950.
2. TIER BOUNDARIES (Moreira-Muir inverse-variance shape, one scale parameter). Tier k is warranted when
   (target_vol/sigma)^2 >= k, i.e. v_k = target_vol / sqrt(k): v1 = target_vol, v2 = target_vol/1.414,
   v3 = target_vol/1.732. Raw tier T(sigma) = number of boundaries sigma is below: 3x below v3, 2x in [v3, v2),
   1x in [v2, v1), cash at or above v1. This is the continuous volmanaged target rounded DOWN to an integer
   ("hold k times only when the evidence warrants at least k times"). Grid A's free two-parameter geometric ladder
   (v_lo, gap) found no gate-feasible point (384 combos, all maxDD < -22%) and is replaced by this theory-given shape.
3. HYSTERESIS. The held level c changes only when the evidence leaves a band around it:
   * UP: raw tier T(sigma) > c, i.e. sigma has fallen below the next boundary.
   * DOWN: T_h(sigma) < c, where T_h uses every boundary inflated by (1+h); i.e. sigma has risen more than h above
     the boundary of the CURRENT tier. Level c is therefore held for all sigma in [v_{c+1}, v_c*(1+h)].
   A down move goes straight to T_h(sigma) (can drop several tiers in one session); an up move goes to T(sigma).
4. PERSISTENCE (up only). An up move requires the UP condition to have held for P consecutive sessions.
   Down moves act on the first session the DOWN condition holds (P_DN = 1, structural -- see below).
5. COOLING-OFF + WEEKLY CADENCE (up only). An up move is allowed only if at least M_COOL sessions have passed since
   the last change of level AND the session is the first trading session of an ISO week (causal: the session's
   ISO week differs from the previous row's). Down moves are never blocked by M_COOL or by the calendar.
6. Long or cash only; leverage in {FLOOR..3}. FLOOR = 0 (cash tier exists) -- the 1x-floor alternative was tested in
   DEV and is reported in the design note.

Parameters (5 tunables; chosen on 1990-01..2012-06, cross-checked on 1950-2012; grids in dev_results/sticky_tier_*
-- grid A 384 combos (free geometric ladder, plain EWMA, floor 0/1), grid B 135, grid C1 144, grid C2 64)
-------------------------------------------------------------------------------------------------------------------
target_vol = 0.14 : the vol at which exactly 1x is warranted (annualised); sets every boundary via v_k = target_vol/sqrt(k)
             (v1 = 14.0%, v2 = 9.9%, v3 = 8.1%). Grid 0.12-0.20. Sharpe is flat 0.46-0.54 (marginal mean) from 0.12 to
             0.15 and every point at 0.16+ breaks the 1950-69 / 1970-89 era drawdown gate (1962 and 1973-74 taken at
             2-3x). 0.14 is the centre of the feasible band.
h = 0.20   : hysteresis width -- a tier is left only when sigma exceeds its boundary by this fraction (1x is left at
             16.8%). Grid 0.15-0.60; Sharpe flat 0.57-0.61 across 0.15-0.50 at the frozen hl / long_mult; 0.20 has
             the largest era-drawdown margin (-33.9% vs -38.9% at 0.30 and -40.0% at 0.40 -- the 1962 exit timing).
hl = 20    : fast EWMA halflife in sessions. Grid 5-26; Sharpe rises from 0.39 (hl 8) to 0.53 (hl 20-26) and is flat
             from 20; at the frozen point the neighbours are 0.51 (16) and 0.62 (26).
long_mult = 8 : slow halflife = hl * long_mult = 160 sessions (regime memory). Grid 1-12; marginal Sharpe 0.39 (1),
             0.45 (4), 0.52 (6), 0.53 (8), 0.52 (12); 8 is the centre of the 6-12 plateau. long_mult = 1 (no memory)
             re-levers into every lull of the 2000-02 grind and roughly doubles the trade count.
P = 5      : persistence -- consecutive sessions the UP condition must hold before leverage is raised. Grid 1-10;
             P = 1 re-enters 2x one week too early in 1962 and breaks the 1950-69 gate (-40.5%); P = 3 and 5 are
             identical; P = 10 costs ~0.04 Sharpe. 5 is interior.

Structural constants (not tuned): MAX_LEV = 3 (mandate); the {0,1,2,3} grid (Demeter's); FLOOR = 0 (a 1x floor
fails the -30% drawdown gate in every one of 192 grid-A combos, best -53.6%, because 2000-02 is taken at 1x; re-run
at the frozen point in the note); M_COOL = 10 sessions (the re-levering cooling-off; grid C2 showed IDENTICAL results
for M in {0, 5, 10, 21} at this operating point because the slow leg keeps sigma above the re-entry boundary for
months after any exit -- a dead tunable would only inflate the plateau share, so it is a constant safety rail);
P_DN = 1 (de-levering is never delayed: the hysteresis margin IS the evidence and the leverage effect makes delay
at 2-3x expensive); WEEKLY_UP = True (re-levering cadence); MIN_PERIODS = 20 (EWMA warm-up); the inverse-variance
ladder shape v_k = target_vol/sqrt(k) with round-DOWN (a theory-given shape, not a tuned one; the rounding
convention is a conservatism choice -- round-to-nearest would hold 1x up to 1.41*target_vol).

Known failure modes: (i) a one-day crash from a calm regime (1987) is taken at the full held tier -- the rule has no
intraday or price-based exit; (ii) recoveries begin while vol is still high, so their first leg is taken at cash/1x
(2009); (iii) a bear at moderate vol (2000-02) is held at 1-2x until the vol boundary is crossed; (iv) a regime where
vol and return are positively related (a levered melt-up on rising vol) is the regime that breaks the mechanism.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

import features as F

NAME = "sticky_tier"
FAMILY = "discrete {0,1,2,3} leverage tiers from a trailing EWMA vol regime; wide hysteresis, persistence, cooling-off, weekly re-levering"
HYPOTHESIS = (
    "Realised equity volatility clusters and the conditional mean excess return is roughly flat in the vol level, so "
    "the mean/variance ratio of the S&P 500 is highest in calm regimes: a position levered in calm regimes and cut in "
    "high-vol regimes raises the Sharpe ratio and avoids the long high-variance drawdowns (1973-74, 2000-02, 2007-09). "
    "Because every change made on noise is reversed on noise, a DISCRETE tier changed only on persistent evidence, with "
    "wide hysteresis and a cooling-off before re-levering, should keep most of the vol-timing benefit while trading a "
    "handful of times a year and holding 2-3x through whole calm years -- the exposure that continuous scaling and the "
    "incumbent's trend gate both give up."
)

# ---- structural constants (see docstring) -----------------------------------------------------------------------
MAX_LEV = 3
FLOOR = 0            # lowest tier: 0 = cash tier exists; 1 = never below 1x (tested in DEV, see note)
P_DN = 1             # sessions the DOWN condition must persist before de-levering (1 = act at once)
WEEKLY_UP = True     # up moves only on the first trading session of an ISO week
MIN_PERIODS = 20     # EWMA warm-up sessions (pre-warm-up = cash)
M_COOL = 10          # sessions after any change before leverage may be raised again (no effect in DEV grid C2)

DEFAULT_PARAMS = dict(target_vol=0.14, h=0.20, hl=20.0, long_mult=8.0, P=5)   # frozen after DEV grids A, B, C1, C2


def _core(df: pd.DataFrame, target_vol: float, h: float, hl: float, long_mult: float, P: int, M: int = M_COOL,
          floor: int = FLOOR, p_dn: int = P_DN, weekly_up: bool = WEEKLY_UP) -> pd.Series:
    ret = df["spx_ret"].astype(float)
    hl = max(float(hl), 1.0)
    fast = F.ewma_vol(ret, halflife=hl, min_periods=MIN_PERIODS)
    slow = F.ewma_vol(ret, halflife=hl * max(float(long_mult), 1.0), min_periods=MIN_PERIODS)
    sig = pd.concat([fast, slow], axis=1).max(axis=1).to_numpy(dtype=float)
    v1 = float(target_vol); v2 = v1 / np.sqrt(2.0); v3 = v1 / np.sqrt(3.0)    # v3 < v2 < v1
    hh = 1.0 + max(float(h), 0.0)
    v3h, v2h, v1h = v3 * hh, v2 * hh, v1 * hh
    M = max(int(round(M)), 0); P = max(int(round(P)), 1); p_dn = max(int(round(p_dn)), 1)
    floor = int(min(max(int(round(floor)), 0), MAX_LEV))

    if weekly_up:   # first session of a new ISO week: causal (compares this row's week with the previous row's only)
        wk = pd.Series(df.index.isocalendar().week.to_numpy(), index=df.index)
        decide = wk.ne(wk.shift(1)).to_numpy()
    else:
        decide = np.ones(len(df), dtype=bool)

    n = len(sig)
    out = np.zeros(n, dtype=float)
    cur = -1                      # unset until warm-up ends
    last_change = -10 ** 9
    up_run = dn_run = 0
    for i in range(n):
        s = sig[i]
        if np.isnan(s):
            out[i] = 0.0
            continue
        T = int(s < v1) + int(s < v2) + int(s < v3)              # raw tier at plain boundaries
        Th = int(s < v1h) + int(s < v2h) + int(s < v3h)          # raw tier at inflated (exit) boundaries; Th >= T
        if cur < 0:
            cur = max(T, floor); last_change = i
            out[i] = cur
            continue
        tgt_dn = max(Th, floor)
        if tgt_dn < cur:
            dn_run += 1; up_run = 0
            if dn_run >= p_dn:
                cur = tgt_dn; last_change = i; dn_run = 0
        else:
            dn_run = 0
            if T > cur:
                up_run += 1
                if up_run >= P and decide[i] and (i - last_change) >= M:
                    cur = T; last_change = i; up_run = 0
            else:
                up_run = 0
        out[i] = cur
    return pd.Series(out, index=df.index).clip(0.0, float(MAX_LEV))


def signal(df: pd.DataFrame, target_vol: float = 0.14, h: float = 0.20, hl: float = 20.0, long_mult: float = 8.0,
           P: int = 5, **structural) -> pd.Series:
    """Target leverage L_t in {FLOOR..3} decided at the close of day t (see module docstring).
    `structural` may carry M / floor / p_dn / weekly_up overrides -- used only for the DEV diagnostics named in the note."""
    return _core(df, target_vol, h, hl, long_mult, P, **structural)
