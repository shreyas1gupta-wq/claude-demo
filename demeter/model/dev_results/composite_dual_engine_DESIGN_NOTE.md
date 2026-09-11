# composite_dual_engine — design note (lens 6: the inference note's §7 composite)

Written incrementally; the Mechanism section below was banked BEFORE the first harness run (2026-09-10).
Everything here is DEVELOPMENT-window only (data hard-truncated at 2012-06-30 by `dev_harness.py`); no
out-of-sample file was read or written.

## Mechanism (written before any run)

The record (inference note §7) says a daily rule had to do four things at once, and the other five lenses
have each shown in DEV what happens when one of them is taken alone:

1. **Shock exit** (§7 ingredient 1): a two-session multi-sigma loss or an implied-vol jump from an already
   elevated base is the earliest clean observation of a volatility regime change; de-levering to cash on it
   removes the clustered aftermath (the Feb-2020 pattern: two −3% days, then −4.5%). Lens 1 (`crash_exit_dual`)
   showed in DEV that this ingredient ALONE is not enough: a default-IN book with a 1x floor rides the 2000-02
   and 2007-09 grinds (maxDD −52.8%) because grinding bears produce no sigma-normalised shock.
2. **Dissipation re-entry** (§7 ingredient 2): at a capitulation low implied vol peaks before price does; a
   fresh price low (RSI(2) < 20) with the VIX still extreme (≥ 30) but well off its 30-day peak (≥ 25% below) is
   the 23-Mar-2020 signature. Lens 2 (`dissipation_reentry`) showed in DEV that this fires 7 times in 22 years,
   4 of them inside the two bears at 50% negative (looser versions 75-83% negative) — so it must be STRICT and
   bounded (10-session hold, 10% burst stop), and its leverage is decided by the spurious-re-entry census, not
   by the record's 3x.
3. **Leverage tier by vol regime in the ORDINARY state** (§7 ingredient 3): 3x when implied vol is calm, 1x when
   elevated. Learned from lens 5 (`vix_vrp`, the DEV leader at Sharpe 0.61 / −19.8%): the thing that saved it in
   2000-02 and 2008 was that its ELEVATED VIX state was CASH, not 1x. So the ordinary tier here has a third
   level: **cash when VIX is persistently above a stress threshold** (the "de-lever when vol is persistently
   elevated" the brief demands). The tier is therefore 3x / 1x / 0 by VIX level with hysteresis — and it is
   NOT monotone in vol overall, because the re-entry state (2) is allowed 3x at VIX ≥ 30.
4. **Hysteresis** (§7 ingredient 4): a minimum hold after every non-emergency state change so that cash spells
   last weeks and the 3x tier is not flipped by a day's VIX noise. Emergency transitions (the shock exit, the
   burst stop) are exempt — protection must never wait.

Why the composite should be at least as good as its parts in 1990-2012: the tier carries the equity premium at
3x in calm years (1993-95, 2005-06, parts of 2010-11) and goes to cash in the grinds (2000-02 VIX 20-35, 2008),
which is exactly vix_vrp's mechanism; the shock exit protects the 3x tier from the calm-regime crashes that a
VIX-level tier reaches late (27-Feb-2007, Oct-1997, Aug-2011 from VIX ~17); the re-entry is the only component
that can take a V-shaped rebound while VIX is still > 30 (Mar-2009 low: VIX 49 off its 81 peak).

Why it may NOT beat vix_vrp — the pre-registered risk: (a) vix_vrp found the 15-30 VIX band has Sharpe ~0 in DEV,
so a 1x ELEVATED tier dilutes rather than adds; (b) 3x in calm carries 3x the single-day gap risk before the
exit can fire (a −3.5% day from VIX 11 costs −10.5% at 3x); (c) the strict re-entry fires so rarely that it
cannot move a 22-year Sharpe, while any loosening re-creates the trap. If the DEV grid drives v_high down to
v_calm (ELEVATED band empty) the honest reading is "the composite collapses into vix_vrp"; if it cannot beat
Sharpe 0.61 / −19.8% at all, the finding is that the extra complexity does not pay in DEV.

Bar: dev_1990 Sharpe 0.61 / maxDD −19.8% (vix_vrp, 3/60). Gates: PREREG G1-G7.

## Parameter budget (declared before the first run)

Tunables (6): `v_calm`, `v_high`, `hyst` (VIX regime bands), `k` (two-session shock size), `out_days`
(sessions out after the last shock), `min_hold` (hysteresis).
Structural constants (not tuned): LEV_CALM 3, LEV_ELEV 1, LEV_STRESS 0, LEV_REB (3 pending census);
J_JUMP 0.30 / VIX_BASE 10 / VIX_FLOOR 20 (lens 1's frozen VIX-jump trigger); SIGMA_WIN 21, SHOCK_DAYS 2;
the whole re-entry trigger borrowed from lens 2's frozen point: VIX_FALL 0.25, VIX_WIN 30, VIX_MIN 30,
RSI_MAX 20, HOLD_DAYS 10, STOP 0.10; cash before 1990 (VIX lens).

## Planned ablations (before any run)

On dev_1990 at 3/60: (A) tier only; (B) tier + shock exit; (C) B + dissipation re-entry at 3x; (D) C +
hysteresis (= the model); (E/F) D with re-entry at 2x / 1x; (G) D with the ELEVATED tier at cash (vix_vrp-like).
Columns: Sharpe, CAGR, maxDD, chg/yr, cash %, 2000-02, GFC, 2009 recovery, avg leverage when invested,
up-capture, census (n entries / share negative in the two bears).
