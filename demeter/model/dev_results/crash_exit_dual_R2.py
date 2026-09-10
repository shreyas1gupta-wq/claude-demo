"""SCRATCH VARIANT R2 of crash_exit_dual (DEV comparison only; not a candidate file).
Identical to signals/crash_exit_dual.py except the re-entry condition 2b: instead of "vol proxy below its n_dis-day
mean", re-enter when the vol proxy is below the level it had at the FIRST exit close of the current OUT spell times
(1 - f). f < 0 allows re-entry while vol is still above the exit level; f > 0 demands it fall below it.
Tunables: k, j, min_out, f, rv_lo, rv_hi (6)."""
from __future__ import annotations
import numpy as np
import pandas as pd
import features as F

NAME = "crash_exit_dual_R2"
FAMILY = "scratch: crash exit + exit-level re-entry"
HYPOTHESIS = "As crash_exit_dual, with re-entry keyed to the exit-day vol level instead of a trailing mean."
DEFAULT_PARAMS = dict(k=3.5, j=0.25, min_out=21, f=0.0, rv_lo=0.10, rv_hi=0.16)
SIGMA_WIN = 21; SHOCK_DAYS = 2; VIX_BASE = 10; VIX_FLOOR = 20.0; TIER_HOLD = 5; PROXY_WIN = 10


def _min_hold(levels, min_days):
    out = levels.astype(float).copy(); cur, held = np.nan, 0
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


def _state(trigger, since_shock, proxy, min_out, f):
    trig, ss, v = trigger.values, since_shock.values, proxy.values
    out = np.empty(len(trig), dtype=bool); state, level = True, np.nan
    for i in range(len(trig)):
        if trig[i]:
            if state or np.isnan(level):          # first exit of the spell fixes the reference level
                level = v[i]
            state = False
        elif (not state) and (not np.isnan(ss[i])) and ss[i] >= min_out and (not np.isnan(v[i])) \
                and (np.isnan(level) or v[i] < level * (1.0 - f)):
            state = True; level = np.nan
        out[i] = state
    return pd.Series(out, index=trigger.index)


def signal(df, k=3.5, j=0.25, min_out=21, f=0.0, rv_lo=0.10, rv_hi=0.16):
    min_out = max(int(round(min_out)), 1)
    ret = df["spx_ret"]; idx = df.index
    sigma_prev = ret.rolling(SIGMA_WIN, min_periods=SIGMA_WIN).std(ddof=1).shift(1)
    z1 = ret / sigma_prev
    z2 = ret.rolling(SHOCK_DAYS, min_periods=SHOCK_DAYS).sum() / (sigma_prev.shift(SHOCK_DAYS - 1) * np.sqrt(SHOCK_DAYS))
    shock_day = (z1 < -k).fillna(False); two_day = (z2 < -k).fillna(False)
    vix = df["vix_close"].ffill()
    vix_base = vix.shift(1).rolling(VIX_BASE, min_periods=VIX_BASE).mean()
    vix_jump = ((vix > (1.0 + j) * vix_base) & (vix >= VIX_FLOOR)).fillna(False)
    trigger = two_day | vix_jump
    since_shock = F.days_since_true(shock_day | two_day | vix_jump)
    rv_proxy = F.realized_vol(ret, PROXY_WIN) * 100.0
    proxy = vix.where(vix.notna(), rv_proxy)
    in_market = _state(trigger, since_shock, proxy, min_out, f)
    rv = F.realized_vol(ret, SIGMA_WIN)
    tier = np.where(rv < rv_lo, 3.0, np.where(rv < rv_hi, 2.0, 1.0)).astype(float)
    tier[rv.isna().values] = np.nan
    tier = _min_hold(tier, TIER_HOLD)
    lev = pd.Series(np.where(in_market.values, tier, 0.0), index=idx)
    lev[np.isnan(tier)] = np.nan
    return lev.clip(0.0, 3.0)
