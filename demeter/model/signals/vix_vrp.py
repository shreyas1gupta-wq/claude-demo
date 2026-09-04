"""vix_vrp -- implied-volatility regime switch with a variance-risk-premium crash filter.

Rules (all decided at the close of day t from data up to that close; the engine applies them to day t+1)
--------------------------------------------------------------------------------------------------------
1. VIX regime state machine with hysteresis (three states, one shared hysteresis fraction `hyst`):
   * CALM     : entered when VIX < v_calm * (1 - hyst)  (default 15.5 * 0.88 = 13.6),
                left when VIX > v_calm (15.5).                             -> target leverage 2x (LEV_CALM)
   * PANIC    : entered when VIX > v_panic (30),
                left when VIX < v_panic * (1 - hyst) (26.4).                -> target leverage 1x (LEV_PANIC)
   * ELEVATED : everything in between (the state is also the starting state) -> 100% cash (LEV_ELEV = 0)
   CALM jumps straight to PANIC if VIX gaps above v_panic; PANIC goes straight to CALM if VIX falls below the
   calm entry level (never happens in practice).
2. Variance-risk-premium crash filter: VRP = VIX/100 - trailing realised vol (rv_win = 10 trading days).
   If VRP < vrp_min (default -0.15, i.e. realised vol running more than 15 vol points ABOVE implied) the market
   is moving more than option prices had priced -> a shock is in progress -> 100% cash regardless of regime.
   In the PANIC state this is the re-entry rule: the 1x long is only taken once realised vol has fallen back
   towards (within 15 points of) the still-elevated VIX, i.e. once the variance risk premium has normalised.
3. Long or cash only; leverage in {0, 1, 2}. Nothing else: no trend filter, no price-based signals.

Why these rules (development sample 1990-01..2012-06 only)
----------------------------------------------------------
Conditional sorts of next-day excess returns on the development sample show three volatility regimes:
calm VIX (12-18): Sharpe ~0.5-0.6 at 10-12% vol (leverage pays); elevated VIX (18-30): Sharpe ~0 (cash);
panic VIX (>30): Sharpe 0.8-1.2 but at 30-55% vol (unlevered participation), and catastrophic returns when
realised vol exceeds implied by >20 points (Sharpe -4 to -7).  Hysteresis keeps position changes to ~8/yr.
Parameters were chosen on the development window for Sharpe, drawdown and trade count (plateaus, not peaks);
the OOS window 2012-07..2026-02 was looked at only through the final evaluate.py runs.

Known caveats: the CBOE VIX close is struck at 4:15 pm ET, 16 minutes after Demeter's 3:59 pm decision; the
intraday difference is typically a few tenths of a point and is ignored here (the whole literature does the same).
"""
from __future__ import annotations

import numpy as np
import pandas as pd

import features as F

NAME = "vix_vrp"
FAMILY = "implied volatility (VIX level regimes with hysteresis) + variance-risk-premium crash filter"
HYPOTHESIS = (
    "Equity risk-adjusted returns are regime dependent in implied volatility: calm markets (low VIX) reward leverage, "
    "elevated-VIX markets carry little premium per unit of risk and should be sat out in cash, and panic markets "
    "(VIX > 30) carry a large premium that is best harvested unlevered. Within any regime, realised volatility running "
    "far above implied (a collapsed variance risk premium) marks a shock in progress and is the trigger to be in cash; "
    "re-entry happens when the VRP normalises, not when the VIX level falls."
)

# Leverage tiers are structural constants (Demeter-style discrete steps), not tunables.
LEV_CALM = 2.0
LEV_ELEV = 0.0
LEV_PANIC = 1.0

DEFAULT_PARAMS = dict(v_calm=15.5, v_panic=30.0, hyst=0.12, rv_win=10, vrp_min=-0.15)


def vix_regime(vix: pd.Series, v_calm: float, v_panic: float, hyst: float) -> pd.Series:
    """Causal three-state machine on the VIX close: 0 = CALM, 1 = ELEVATED (start state), 2 = PANIC.
    Hysteresis: calm is entered below v_calm*(1-hyst) and left above v_calm; panic is entered above v_panic
    and left below v_panic*(1-hyst).  NaN VIX values leave the state unchanged."""
    calm_in, calm_out = v_calm * (1.0 - hyst), v_calm
    panic_in, panic_out = v_panic, v_panic * (1.0 - hyst)
    if calm_out > panic_in:                      # degenerate perturbations: keep the machine well-ordered
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
           rv_win: int = 10, vrp_min: float = -0.15) -> pd.Series:
    """Target leverage L_t in {0, 1, 2} decided at the close of day t (see module docstring)."""
    rv_win = max(int(round(rv_win)), 2)
    vix = df["vix_close"].ffill()                                   # 4 isolated missing prints in the 1990s
    reg = vix_regime(vix, v_calm, v_panic, hyst)
    rv = F.realized_vol(df["spx_ret"], rv_win)                       # annualised trailing realised vol
    vrp = vix / 100.0 - rv                                           # variance-risk-premium proxy (vol points)
    lev = pd.Series(np.select([reg.values == 0, reg.values == 2], [LEV_CALM, LEV_PANIC], default=LEV_ELEV),
                    index=df.index, dtype=float)
    lev[vrp < vrp_min] = 0.0                                         # shock in progress -> cash
    lev[vix.isna() | rv.isna()] = 0.0                                # no VIX / warm-up -> cash
    return lev
