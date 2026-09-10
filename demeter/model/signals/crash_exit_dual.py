"""crash_exit_dual -- two separate decisions: a crash-triggered IN/OUT state machine (default IN) and an
independent realised-vol leverage tier.

Rules (all decided at the close of day t from data up to that close; the engine applies them to day t+1)
--------------------------------------------------------------------------------------------------------
DECISION A -- "am I in the market?"  A state machine whose default (and initial) state is IN.
  1. EXIT trigger (either of):
     a. TWO-SESSION SHOCK: the two-day return r_t + r_{t-1} is below -k * sqrt(2) * sigma, where sigma is the
        trailing 21-day daily standard deviation measured up to the close BEFORE both days (so the shock does not
        dilute its own z-score). One -3% day in a 12%-vol regime (sigma 0.76%) is a 2-day z of -2.8 and does not
        trip it at k >= 3; two -3% days are -5.6 and do; -3% followed by -1.5% is -4.2. The cumulative form was
        chosen over "each day below -k sigma" after the first DEV run: 14/15-Oct-1987 were -2.36 sigma and
        -1.72 sigma (the second day measured on a sigma already inflated by the first), so an individual-day
        pair can never fire before Black Monday at any k that avoids calm-year noise, whereas the 2-day z was
        -2.99 on 15-Oct and -3.91 on 16-Oct.
     b. VOL JUMP on a down day: the vol proxy (VIX close from 1990; 10-day realised vol x100 before that) closes
        more than j above its own mean over the previous 10 sessions, while the proxy is >= 20 (absolute floor: a
        jump from a calm base is normal-regime noise) and the day's return is negative (a realised-vol proxy also
        jumps on a big UP day; that is not a crash). Because of the floor this trigger is regime-dependent by
        construction: it is silent in calm years and active only once vol is already elevated.
  2. OUT persists until BOTH hold:
     a. at least `min_out` sessions have passed since the LAST shock event (a two-session shock, a single day
        below -k sigma, or a vol jump -- any of these restarts the clock: a crash is over when shocks stop
        arriving, not when a calendar expires);
     b. vol is DISSIPATING: the vol proxy (VIX close; before 1990 the 10-day realised vol) is below its own
        trailing `n_dis`-day mean. Dissipation, not calm: the re-entry may happen while vol is still very high.
  3. No trend filter anywhere; an exit trigger always wins over a re-entry on the same close.
DECISION B -- "how much leverage?"  Independent of A, slower.
  4. Tier by trailing 21-day realised vol: 3x below `rv_lo`, 2x below `rv_hi`, else 1x. Each tier is held for at
     least 5 sessions before it may change (anti-churn). The tier never goes to 0 -- cash is Decision A's job.
  Target leverage = tier if IN, 0 if OUT. Leverage grid {0, 1, 2, 3}.

Parameters (6 tunables; all chosen on the development window 1990-01-01..2012-06-30 via dev_harness.py grids,
plateau-checked against 1950-01-03..2012-06-30; grids and reasons in dev_results/crash_exit_dual_DESIGN_NOTE.md)
  k       two-session shock size in trailing sigmas     (grids 3.0 .. 5.0)   frozen 4.0
  j       vol-jump fraction over the 10-day mean        (grids 0.10 .. 0.40)  frozen 0.30
  min_out minimum sessions OUT after the last shock     (grids 10 .. 63)      frozen 21
  n_dis   window of the dissipation mean                (grids 10 .. 63)      frozen 10 (inert: +-0.01 Sharpe)
  rv_lo   RV21 below which the tier is 3x               (grids 0.09 .. 0.12)  frozen 0.10
  rv_hi   RV21 below which the tier is 2x               (grids 0.13 .. 0.18)  frozen 0.14
  The frozen point is the centre of the max-Sharpe plateau on dev_1990 (Sharpe 0.40-0.45 for k 4-5, j 0.3-0.4,
  min_out 15-30, rv_hi 0.13-0.14). DEV VERDICT (see design note): this lens does NOT pass the pre-registered gates
  -- no configuration among 1,200+ evaluated clears G3 (-30% DD) and G2 (Sharpe 0.4253) together, and none clears
  G4, because the 2000-02 and 2007-09 bears (and 1973-74) were grinds that produce no sigma-normalised shock and a
  default-IN book with a 1x floor rides them. The file is frozen for the record, not proposed for an OOS look.

Structural constants (declared, NOT tuned, with the reason):
  SIGMA_WIN = 21    one trading month of daily returns for sigma; the standard RV21 scale used firm-wide
  SHOCK_DAYS = 2    "two sessions" is the smallest span that is a regime statement rather than a bad day
  VIX_BASE  = 10    two trading weeks as the vol-proxy reference level for the jump
  VIX_FLOOR = 20    the record's own bins and the CBOE long-run median (~18-19) put "elevated" at 20+; applied to
                    the realised-vol proxy on the same scale (20% annualised) before 1990
  TIER_HOLD = 5     one trading week; keeps daily RV21 noise from churning the tier
  PROXY_WIN = 10    pre-1990 vol proxy = 10-day realised vol (the shortest window with a usable std estimate);
                    the jump and dissipation tests are computed on VIX and on the proxy separately and the
                    proxy result is used only on dates without a VIX print

Known failure modes: a grinding bear with no two-session shock and no VIX jump is ridden at 1x (the tier floor);
once vol is already high, sigma-normalised moves look small, so the price trigger goes quiet deep in a crash and
the OUT clock relies on VIX jumps and the dissipation condition; a V-shaped rebound that begins while shocks are
still arriving (Mar-2020 style) is re-entered late, at 1x; a single large down day from a very calm base
(27-Feb-2007, 13-Oct-1989) fires the two-session trigger and costs `min_out` sessions of missed 3x drift.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

import features as F

NAME = "crash_exit_dual"
FAMILY = "crash-triggered IN/OUT state machine (default IN) + independent realised-vol leverage tier"
HYPOTHESIS = (
    "Crash losses at leverage come from the first two or three days of a volatility regime change, which trailing-vol "
    "and trend gates see only weeks later. A two-session multi-sigma loss (or an implied-vol jump from an elevated "
    "base) is the earliest statistically clean observation of that change, so exiting on it and staying out until "
    "shocks stop arriving and vol is falling removes the clustered aftermath, while a default-IN state and a "
    "realised-vol tier keep the book levered in the calm regimes where the equity premium at 3x is earned."
)

DEFAULT_PARAMS = dict(k=4.0, j=0.30, min_out=21, n_dis=10, rv_lo=0.10, rv_hi=0.14)

SIGMA_WIN = 21
SHOCK_DAYS = 2
VIX_BASE = 10
VIX_FLOOR = 20.0
TIER_HOLD = 5
PROXY_WIN = 10


def _min_hold(levels: np.ndarray, min_days: int) -> np.ndarray:
    """Hold each level for at least `min_days` sessions before allowing a change (NaN passes through)."""
    out = levels.astype(float).copy()
    cur, held = np.nan, 0
    for i in range(len(out)):
        v = out[i]
        if np.isnan(v):
            continue
        if np.isnan(cur):
            cur, held = v, 0
        elif v != cur:
            if held >= min_days:
                cur, held = v, 0
            else:
                out[i] = cur
        held += 1
    return out


def signal(df: pd.DataFrame, k: float = 3.5, j: float = 0.25, min_out: int = 21, n_dis: int = 21,
           rv_lo: float = 0.10, rv_hi: float = 0.16) -> pd.Series:
    min_out = max(int(round(min_out)), 1)
    n_dis = max(int(round(n_dis)), 2)
    ret = df["spx_ret"]
    idx = df.index

    # ---------------- Decision A: crash exit state machine (default IN)
    sigma_prev = ret.rolling(SIGMA_WIN, min_periods=SIGMA_WIN).std(ddof=1).shift(1)          # through t-1
    z1 = ret / sigma_prev
    r2 = ret.rolling(SHOCK_DAYS, min_periods=SHOCK_DAYS).sum()
    z2 = r2 / (sigma_prev.shift(SHOCK_DAYS - 1) * np.sqrt(SHOCK_DAYS))                        # sigma before both days
    shock_day = (z1 < -k).fillna(False)
    two_day = (z2 < -k).fillna(False)

    vix = df["vix_close"].ffill()                                           # 4 isolated NaNs in the 1990s
    rv_proxy = F.realized_vol(ret, PROXY_WIN) * 100.0                       # pre-1990 stand-in for VIX
    has_vix = vix.notna().values

    def _jump(p: pd.Series) -> np.ndarray:
        base = p.shift(1).rolling(VIX_BASE, min_periods=VIX_BASE).mean()
        return ((p > (1.0 + j) * base) & (p >= VIX_FLOOR)).fillna(False).values

    vol_jump = pd.Series(np.where(has_vix, _jump(vix), _jump(rv_proxy)), index=idx) & (ret < 0).fillna(False)

    trigger = two_day | vol_jump                                            # leaves the market
    shock_any = shock_day | two_day | vol_jump                              # restarts the OUT clock
    since_shock = F.days_since_true(shock_any)                              # NaN before the first shock

    dis_vix = (vix < F.sma(vix, n_dis)).fillna(False)
    dis_rv = (rv_proxy < F.sma(rv_proxy, n_dis)).fillna(False)
    dissipating = pd.Series(np.where(has_vix, dis_vix.values, dis_rv.values), index=idx)

    reentry = (since_shock >= min_out).fillna(False) & dissipating
    in_market = F.hysteresis(reentry, trigger, initial=True)               # exit wins on the same close

    # ---------------- Decision B: realised-vol leverage tier, held >= TIER_HOLD sessions
    rv = F.realized_vol(ret, SIGMA_WIN)
    tier = np.where(rv < rv_lo, 3.0, np.where(rv < rv_hi, 2.0, 1.0)).astype(float)
    tier[rv.isna().values] = np.nan
    tier = _min_hold(tier, TIER_HOLD)

    lev = pd.Series(np.where(in_market.values, tier, 0.0), index=idx)
    lev[np.isnan(tier)] = np.nan                                            # warm-up
    return lev.clip(0.0, 3.0)
