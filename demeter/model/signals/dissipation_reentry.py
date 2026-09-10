"""dissipation_reentry -- a levered re-entry on implied-vol DIVERGENCE (not a trend filter), behind a simple stress exit.

Rules (decided at the close of day t from data up to that close; the engine applies them to day t+1).
Three states; the leverage is discrete {0, 1, 2, 3}.

  1. DEFAULT engine: FLAT 1x (structural, LEV_TIER = (1, 1, 1)). Not cash-by-default: calm markets are held unlevered.
     The incumbent's 3x/2x/1x RV tier (thresholds 0.10 / 0.15) was the other structural default the brief allows; it
     was tested on DEV at the frozen trigger parameters and REJECTED because, with no trend filter, it levers into the
     1962 and 1973-74 bears: era maxDD -46.9% (1950-69) and -43.7% (1970-89), failing gate G4, while flat 1x gives
     -19.6% / -13.8% at the same dev_1990 Sharpe (0.447 vs 0.445). The tier code path is kept (all levels 1.0) so the
     diagnostic script dev_results/dissipation_reentry_flat1x.py can still reproduce the comparison.
  2. STRESS exit -> cash. Trigger = RV21 > `rv_exit` OR two consecutive days each below -Z sigma, where sigma is the
     PREVIOUS day's RV21 / sqrt(252) (so a shock cannot inflate its own yardstick) and Z = 2 (structural).
     Leaves STRESS back to DEFAULT only once RV21 < HYST x rv_exit (HYST = 0.8, structural hysteresis).
  3. REBOUND re-entry -> 3x, WITHOUT any trend condition. Fires (from STRESS or DEFAULT) on a day when all three hold:
        VIX <= (1 - `vix_fall`) x max(VIX over the trailing `vix_win` sessions, today included)   [vol dissipating]
        VIX >= `vix_min`                                                                          [... from an extreme]
        RSI(2) < 20                                                                               [price still being sold]
     i.e. a bullish implied-vol divergence: price at a fresh low while implied vol has already come off its peak
     (the 23-Mar-2020 profile: VIX 61.6, 25% below its 16-Mar peak, RSI(2) = 8). Holds `hold_days` sessions, ended
     early by (a) a fresh two-sigma double shock or (b) the burst STOP: the burst's own cumulative 3x excess return
     falling to -`stop_loss` or worse at a close (a burst is a bet; a bet has a stop). On exit -> DEFAULT if
     RV21 < HYST x rv_exit, else STRESS. After a natural expiry a new burst needs the trigger on a LATER day; after a
     stop-out no new burst is allowed for `hold_days` sessions (a stopped thesis is not re-tried the next morning).
  4. Before 1990 (no VIX) REBOUND never occurs: the model is the default tier + stress exit only. Warm-up -> 0.

Parameters (6 tunables) -- development window 1990-01-01..2012-06-30 (dev_1950 for the non-VIX part), chosen from a
plateau of the coarse grid documented in dev_results/dissipation_reentry_DESIGN_NOTE.md:
  rv_exit   annualised RV21 above which the model is in cash (stress).
  vix_fall  required fall of VIX from its trailing maximum (fraction).
  vix_win   trailing window (sessions) for that maximum.
  vix_min   absolute VIX floor for a re-entry (the "still an extreme" leg).
  hold_days sessions a burst is held (also the re-entry block after a stop-out).
  stop_loss burst stop as a fraction of burst equity at 3x (0.10 = exit once the burst has lost 10%); >= 1 disables.
  The stop slot was reserved in the design note before the first run and filled after the first grid corners showed
  that the Nov-2008 and Feb-2009 bursts were straight-line losses of 40-47% that the bounded hold alone could not cap.

Structural constants (declared, never varied): RV window 21 (scale only); default leverage flat 1x (see rule 1 for the
rejected tier alternative); RSI(2) < 20 (the brief's oversold definition); Z = 2 (two consecutive 2-sigma days happen
~once per 8 years by chance under iid normality; Feb-2020's two -3% days at 10% vol were ~4.7 sigma); HYST = 0.8;
rebound leverage 3x (the record's Apr-2020 tier).

What the frozen model IS, said plainly: 1x while RV21 < 15% (resuming below 12%), cash above, a 3x burst of up to 10
sessions on an implied-vol divergence with a 10% burst stop. About half of all days are cash. The default engine is a
realised-vol LEVEL gate -- the inference note rules that ingredient out for reproducing Demeter's 2020; it is here because
the lens forbids a trend filter and nothing else kept the model out of the 2000-02 bear in DEV (see design note).

Known failure modes (pre-registered in the design note): a crash whose VIX makes successive higher highs while price
makes lower lows (Oct-Nov 2008) shows no divergence until far too late; a grinding bear without a VIX spike (2000-01)
never fires, so the rule is safe there by silence, not skill; inside a crash a 2-sigma day is -7% and the double-shock
exit cannot fire, so the only protection on a burst is the bounded hold; the default 1x/cash flip near rv_exit carries
most of the turnover.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

import features as F

NAME = "dissipation_reentry"
FAMILY = "implied-vol divergence re-entry (VIX off its peak, still extreme, price oversold) behind an RV / double-shock stress exit; incumbent's RV tier as default"
HYPOTHESIS = (
    "At a genuine capitulation low the marginal buyer of protection is exhausted before the last seller of stock, so implied "
    "vol puts in its high days before price does: a fresh price low with VIX well below its recent peak but still extreme is "
    "a bottom signature (23-Mar-2020) that a trend filter cannot see. Conditioning the 3x re-entry on that divergence -- rather "
    "than on VIX merely being below its 10-day average -- should remove most of the spurious 2000-02 / 2007-09 entries of the "
    "pass-1 trap while keeping the crisis-rebound leverage. Whether it is non-ruinous without a trend filter is the test."
)

# ---- structural constants (not tuned; see docstring)
RV_WIN = 21
TIER_RV_LO, TIER_RV_HI = 0.10, 0.15          # thresholds of the REJECTED incumbent tier (kept for the diagnostic script)
LEV_TIER = (1.0, 1.0, 1.0)                   # FLAT 1x default (RV<lo, RV<hi, else); the tier variant is (3, 2, 1)
LEV_REBOUND = 3.0
RSI_MAX = 20.0
Z_SHOCK = 2.0
HYST = 0.8

DEFAULT_PARAMS = dict(rv_exit=0.15, vix_fall=0.25, vix_win=30, vix_min=30.0, hold_days=10, stop_loss=0.10)


def signal(df: pd.DataFrame, rv_exit: float = 0.15, vix_fall: float = 0.25, vix_win: int = 30,
           vix_min: float = 30.0, hold_days: int = 10, stop_loss: float = 0.10) -> pd.Series:
    vix_win = max(int(round(vix_win)), 2)
    hold_days = max(int(round(hold_days)), 1)

    ret, px = df["spx_ret"], df["spx_px"]
    x_ex = (df["spx_tr_ret"] - df["rf_daily"]).fillna(0.0).to_numpy()   # excess return, for the burst's own P&L
    rv = F.realized_vol(ret, RV_WIN)
    sigma_prev = (rv / np.sqrt(252)).shift(1)                        # yesterday's vol as today's yardstick
    shock_day = ret < -Z_SHOCK * sigma_prev
    double_shock = (shock_day & shock_day.shift(1).fillna(False)).fillna(False)
    stress_on = ((rv > rv_exit) | double_shock).fillna(False)
    stress_off = (rv < HYST * rv_exit).fillna(False)

    vix = df["vix_close"].ffill()
    vix_max = vix.rolling(vix_win, min_periods=vix_win).max()
    rsi2 = F.rsi(px, 2)
    dissip = ((vix <= (1.0 - vix_fall) * vix_max) & (vix >= vix_min) & (rsi2 < RSI_MAX) & vix.notna()).fillna(False)

    tier = pd.Series(LEV_TIER[2], index=df.index, dtype=float)
    tier[rv < TIER_RV_HI] = LEV_TIER[1]
    tier[rv < TIER_RV_LO] = LEV_TIER[0]

    warm = rv.notna().to_numpy()
    s_on, s_off, dis, dbl = stress_on.to_numpy(), stress_off.to_numpy(), dissip.to_numpy(), double_shock.to_numpy()
    tier_v = tier.to_numpy()
    out = np.zeros(len(df), dtype=float)
    state, held, cum, block_until = 0, 0, 1.0, -1                    # 0 DEFAULT, 1 STRESS, 2 REBOUND
    for i in range(len(df)):
        if not warm[i]:
            out[i] = 0.0
            continue
        exited = False
        if state == 2:                                               # burst was in effect during day i
            cum *= 1.0 + LEV_REBOUND * x_ex[i]
            held += 1
            stopped = cum <= 1.0 - stop_loss
            if stopped or held >= hold_days or dbl[i]:
                state = 0 if s_off[i] else 1
                exited = True
                if stopped:
                    block_until = i + hold_days                      # no re-try for hold_days sessions
        if state != 2 and dis[i] and not exited and i >= block_until:
            state, held, cum = 2, 0, 1.0
        elif state == 0 and s_on[i]:
            state = 1
        elif state == 1 and s_off[i]:
            state = 0
        out[i] = LEV_REBOUND if state == 2 else (0.0 if state == 1 else tier_v[i])
    return pd.Series(out, index=df.index).clip(0.0, 3.0)
