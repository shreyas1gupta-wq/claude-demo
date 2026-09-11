"""vix_vrp_v2 -- VIX-regime switch + variance-risk-premium crash filter, with a VRP-gated 1x floor in the ELEVATED regime.

Lineage: v2 of signals/vix_vrp.py (frozen, unchanged). The three-state machine, the VRP crash filter and five of the
six parameters are identical; the single structural change is rule 3 (ELEVATED regime = 1x when the variance risk
premium is rich, cash otherwise, instead of cash always). Chosen by ablation on the development window 1990-01..
2012-06 (dev_results/vix_vrp_DESIGN_NOTE.md, Part 2): a 3x CALM tier, an unconditional 1x ELEVATED floor and every
PANIC-state dissipation "burst" re-entry were tested one at a time and rejected on DEV (worse Sharpe and/or ruinous
2000-02 / 2008 behaviour; the burst re-entries fired 50-100% negative in 2008 -- the same trap that killed the pass-1
vix_dissipation model).

Rules (decided at the close of day t from data up to that close; the engine applies the target to day t+1)
--------------------------------------------------------------------------------------------------------
1. VIX regime state machine with hysteresis (three states, one shared hysteresis fraction `hyst`):
   * CALM     : entered when VIX < v_calm * (1 - hyst), left when VIX > v_calm            -> LEV_CALM  = 2x
   * PANIC    : entered when VIX > v_panic, left when VIX < v_panic * (1 - hyst)          -> LEV_PANIC = 1x
   * ELEVATED : everything in between; also the starting state                            -> rule 3
   CALM jumps straight to PANIC if the VIX gaps above v_panic; PANIC goes straight to CALM below the calm entry level.
2. Variance-risk-premium crash filter: VRP = VIX/100 - trailing realised vol (rv_win trading days, annualised).
   VRP < vrp_min (realised vol running more than 15 vol points ABOVE implied) = a shock in progress -> 100% cash in
   every state. Inside PANIC this is also the re-entry rule: the 1x long is taken only once realised vol has fallen
   back to within |vrp_min| of the still-elevated VIX.
3. NEW. ELEVATED regime: target 1x when VRP > vrp_elev (implied vol more than `vrp_elev` vol points ABOVE realised --
   the variance risk premium is rich, i.e. the market is moving less than option prices fear), else cash.
   Mechanism: a rich VRP is the known positive predictor of forward equity returns (Bollerslev-Tauchen-Zhou 2009);
   a thin or negative VRP in an elevated-VIX regime is the grinding-bear signature (2000-02: VIX 20-30 with realised
   vol 20-25%), which is where the original's cash-by-default earned its keep and where this rule stays in cash.
4. Long or cash only; leverage in {0, 1, 2}. No trend filter, no price-based input.

Parameters (6 tunables; all chosen on 1990-01..2012-06 through dev_harness.py only)
---------------------------------------------------------------------------------
v_calm 15.5, v_panic 30, hyst 0.12, rv_win 10, vrp_min -0.15: inherited from vix_vrp, re-checked by two grids
  (dev_results/vix_vrp_gridA/gridB_grid.csv, 435 combos): flat in hyst 0.08-0.20, v_calm 13-16, rv_win 7-21 and
  vrp_min -0.25..-0.05; cliffs at v_panic >= 35, v_calm 18 and rv_win 5 (all avoided).
vrp_elev: the one new parameter. Threshold x gate-form map (dev_results/vix_vrp_v2_map.csv, 42 cells) and the v2
  harness grids (dev_results/vix_vrp_v2_grid*.csv). The 2000-02 bear turns negative for vrp_elev <= 0.09 (the gate
  opens too often inside the bear) and the rule converges to the original above ~0.14 (the gate rarely opens);
  0.10-0.13 is the plateau. The default is the centre of that plateau, not its peak.

Structural constants (not tuned, with reasons)
----------------------------------------------
LEV_CALM = 2, LEV_PANIC = 1, LEV_ELEV_ON = 1: Demeter-style discrete tiers inherited from vix_vrp; 3x CALM was tested
  once on DEV and rejected (Sharpe 0.61 -> 0.55, worst month -10.7 -> -15.5%), so it is not a free constant.
Gate form = raw same-day VRP (no smoothing, no minimum hold, no extra hysteresis band): the round-3 map showed the
  smoothed / min-hold / banded forms do not improve the average Sharpe over the threshold range and worsen the
  bear and GFC outcomes, so the simplest form with no additional constant was kept.
Realised vol = close-to-close std over rv_win days (features.realized_vol), the same series for rules 2 and 3.
VIX missing prints (4 in the 1990s) are forward-filled (causal; acts on a stale print those days).

Known failure modes
-------------------
* The -28.6% daily / -19.8% monthly drawdown of the original is untouched: it is the 1x PANIC leg riding the Jan-Mar
  2009 grind with a positive VRP (realised vol fell under a VIX of 40-55 while prices kept sliding). Any prolonged
  panic that grinds lower with a normalised VRP will do the same at 1x.
* It is still a VIX-LEVEL machine (the record says Demeter was not): it never reaches 2x in a post-crash rebound
  (2009: +44-54% of SPY's +67%) and it sits out most of a bull whose VIX stays 16-30 unless the VRP is rich.
* Turnover roughly doubles versus the original (the ELEVATED gate flips on realised-vol prints); the 6 bp / 90 bp
  cost row is where that shows.
* The VIX close is struck at 16:15 ET, after the 15:59 decision time of the record; ignored, as in the literature.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

import features as F

NAME = "vix_vrp_v2"
FAMILY = "implied-volatility regimes with hysteresis + variance-risk-premium crash filter + VRP-gated 1x floor in the elevated regime"
HYPOTHESIS = (
    "Equity risk-adjusted returns are regime dependent in implied volatility: calm markets (low VIX) reward leverage, panic "
    "markets (VIX > 30) carry a large premium best harvested unlevered once realised vol has fallen back under implied, and "
    "elevated-VIX markets pay only when the variance risk premium is rich (implied well above realised) -- a thin VRP at "
    "elevated VIX is the grinding-bear signature and is sat out in cash. Realised vol running far above implied marks a "
    "shock in progress and is the trigger to be in cash in every regime."
)

LEV_CALM = 2.0
LEV_ELEV_ON = 1.0
LEV_PANIC = 1.0

DEFAULT_PARAMS = dict(v_calm=15.5, v_panic=30.0, hyst=0.12, rv_win=10, vrp_min=-0.15, vrp_elev=0.12)


def vix_regime(vix: pd.Series, v_calm: float, v_panic: float, hyst: float) -> pd.Series:
    """Causal three-state machine on the VIX close: 0 = CALM, 1 = ELEVATED (start state), 2 = PANIC.
    Identical to signals/vix_vrp.py (copied, since that file is frozen and signals/ is not a package)."""
    calm_in, calm_out = v_calm * (1.0 - hyst), v_calm
    panic_in, panic_out = v_panic, v_panic * (1.0 - hyst)
    if calm_out > panic_in:
        calm_out = panic_in
    if panic_out < calm_in:
        panic_out = calm_in
    v = vix.to_numpy(dtype=float)
    out = np.empty(len(v), dtype=np.int8)
    st = 1
    for i in range(len(v)):
        x = v[i]
        if not np.isnan(x):
            if st == 0:
                if x > panic_in:
                    st = 2
                elif x > calm_out:
                    st = 1
            elif st == 1:
                if x > panic_in:
                    st = 2
                elif x < calm_in:
                    st = 0
            else:
                if x < calm_in:
                    st = 0
                elif x < panic_out:
                    st = 1
        out[i] = st
    return pd.Series(out, index=vix.index)


def signal(df: pd.DataFrame, v_calm: float = 15.5, v_panic: float = 30.0, hyst: float = 0.12,
           rv_win: int = 10, vrp_min: float = -0.15, vrp_elev: float = 0.12) -> pd.Series:
    """Target leverage L_t in {0, 1, 2} decided at the close of day t (see module docstring)."""
    rv_win = max(int(round(rv_win)), 2)
    vix = df["vix_close"].ffill()
    reg = vix_regime(vix, v_calm, v_panic, hyst).to_numpy()
    rv = F.realized_vol(df["spx_ret"], rv_win)
    vrp = vix / 100.0 - rv
    elev_on = (reg == 1) & (vrp > vrp_elev).to_numpy()
    lev = pd.Series(np.select([reg == 0, reg == 2, elev_on], [LEV_CALM, LEV_PANIC, LEV_ELEV_ON], default=0.0),
                    index=df.index, dtype=float)
    lev[vrp < vrp_min] = 0.0
    lev[vix.isna() | rv.isna()] = 0.0
    return lev
