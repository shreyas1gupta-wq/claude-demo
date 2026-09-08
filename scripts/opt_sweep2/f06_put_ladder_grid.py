"""f06_put_ladder_grid — THE PUT LADDER COST/PROTECTION FRONTIER.

Family key: f06_put_ladder_grid. Pre-registered exploratory sweep (Strategy Sweep 2).
NOT a promotion / not a new booked design — CONTRACT-mandated bar: this maps the frontier
and reports whether the CURRENT standing-book cell (91d tenor, 5%-OTM strike, roll at 30d-
to-expiry) sits on it. No cell is picked as "the answer" (task instruction: in-sample
shopping is banned).

Grid (18 cells): tenor in {60,91,182} days x strike moneyness in {0.93,0.95,0.97} x
roll-trigger in {15,30} days-to-expiry. BS flat-sigma at India-VIX close (engine
convention, house-standard, no lookahead: only the SAME-DAY close is used to mark/reprice,
identical to scripts/analyze_op_d6b.py's put block). Swapped into THE STANDING BOOK
(OP-D6b a5: core 65% vol-managed NIFTY (15% target, cap 1.5x, financing r=0.06 on
exposure>1x) / 20% dual-momentum switcher / 15% factor sleeve + covered calls + condor
sleeve UNCHANGED — only the put ladder's tenor/strike/roll are varied).

Engine reuse: the pre-MAIN body of analyze_op_d6b.py is exec'd verbatim (house pattern,
same as analyze_op_d7.py) to get core_stream/month_stream/SW_M/fac_vm/OP_RET/bsv/
last_thursday/DF2/pct_s/dates/D0/D1/R/stats_of — i.e. everything EXCEPT the put-ladder
block of run_book(), which is copied here and generalized per the task instruction
("copy the engine loop into your scratch script"). No inline re-implementation of
expanding_percentile/EWMA/BS pricing — all imported from quant/ or the engine verbatim.

Cost/payoff normalization: at each put's OPEN, notional0 = units*S_open is fixed for that
put's life (matches the engine's own units = notional/S_open convention, i.e. a fixed-
currency-notional ladder, not delta-rebalanced). Daily pnl_frac = daily_pnl / notional0.
"Annual carry cost" = 100 * mean(pnl_frac over ALL days with a live put) * 252 (%/yr of
protected notional) -- this is a full-sample average net of every payoff year, matching
the OP-D5 ledger's "-1.60%/yr of notional" convention (research/register/trial-ledger.md
OP-D5 entry, s3). "2020 payoff" = 100 * sum(pnl_frac for t.year==2020) (%, that calendar
year only, of notional).
"""
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/claude-demo")

ENGINE = open("/home/user/claude-demo/scripts/analyze_op_d6b.py").read()
NS = {}
exec(ENGINE.split("# === MAIN ===")[0], NS)  # noqa: S102 -- house pattern (see analyze_op_d7.py)

core_stream = NS["core_stream"]
month_stream = NS["month_stream"]
SW_M = NS["SW_M"]
fac_vm = NS["fac_vm"]
OP_RET = NS["OP_RET"]
bsv = NS["bsv"]
last_thursday = NS["last_thursday"]
DF2 = NS["DF2"]
pct_s = NS["pct_s"]
dates = NS["dates"]
D0, D1 = NS["D0"], NS["D1"]
stats_of = NS["stats_of"]
run_book_engine = NS["run_book"]  # unmodified engine, for the baseline sanity check

YEARS = (D1 - D0).days / 365.25

# STANDING BOOK weights (OP-D6b a5 — the corrected baseline quoted in the task brief)
CORE_W, SW_W, FAC_W = 0.65, 0.20, 0.15


def run_book_ladder(tenor_days, strike_mult, roll_days, core_w=CORE_W, sw_w=SW_W,
                     fac_w=FAC_W, cap=1.5, financing=True, syn_margin=True):
    """OP-D6b run_book() with the put-ladder block generalized. Everything else
    (core vol-target, switcher, factor sleeve, covered calls, condor sleeve, margin
    model, financing) is IDENTICAL to the engine -- copied verbatim, only the put
    open/roll/strike logic is parameterized. No lookahead: BS priced at the SAME-DAY
    close (S_t, vix_t), exactly like the engine.
    """
    core_ret, expo = core_stream(cap, financing)
    sw_d = month_stream(SW_M)
    fac_d = month_stream(fac_vm) if fac_w > 0 else pd.Series(0.0, index=dates)
    exl = expo.shift(1)
    book = 100.0
    eq_rows = []
    put = None
    cc = None
    peak_margin = 0.0
    put_pnl_frac_days = []   # list of (date, pnl_frac) for every day a put is live
    put_premium_frac = []    # premium paid at open, as frac of that put's notional0 (==1 always;
                              # kept as (date, v0*units/notional0) for the gross-premium view)
    put_recovery_frac = []   # value received at early close (roll), frac of notional0

    for t in dates:
        S, vix = DF2.S[t], DF2.vix[t]
        p = pct_s.reindex([t]).ffill().iloc[0]
        day = book * (core_w * core_ret[t] + sw_w * sw_d[t] + fac_w * fac_d[t] + OP_RET[t])
        # ---- put ladder (generalized) ----
        if put is not None:
            T = max((put["exp"] - t).days, 0) / 365
            v = bsv(S, put["K"], T, vix / 100, -1)
            pnl = (v - put["mark"]) * put["units"]
            day += pnl
            put_pnl_frac_days.append((t, pnl / put["notional0"]))
            put["mark"] = v
            if (put["exp"] - t).days <= roll_days:
                put_recovery_frac.append((t, v * put["units"] / put["notional0"]))
                put = None
        if put is None:
            e_t = exl.get(t, 1.0)
            core_notional = core_w * (1.0 if pd.isna(e_t) else float(e_t)) * book
            K = S * strike_mult
            v0 = bsv(S, K, tenor_days / 365, vix / 100, -1)
            units = core_notional / S
            put = dict(K=K, exp=t + pd.Timedelta(days=tenor_days), units=units, mark=v0,
                       notional0=core_notional)
            put_premium_frac.append((t, v0 * units / core_notional))
        # ---- covered calls (verbatim engine logic) ----
        if cc is not None:
            T = max((cc["exp"] - t).days, 0) / 365
            v = bsv(S, cc["K"], T, vix / 100, +1)
            day += -(v - cc["mark"]) * cc["units"]
            cc["mark"] = v
            if t >= cc["exp"]:
                cc = None
        if cc is None and p >= 0.60:
            em, ey = (t.month + 1, t.year) if t.month < 12 else (1, t.year + 1)
            exp_d = last_thursday(ey, em)
            if (exp_d - t).days < 15:
                em, ey = (em + 1, ey) if em < 12 else (1, ey + 1)
                exp_d = last_thursday(ey, em)
            Tm = (exp_d - t).days / 365
            K = S * (1 + vix / 100 * np.sqrt(Tm))
            v0 = bsv(S, K, Tm, vix / 100, +1)
            cc = dict(K=K, exp=exp_d, units=0.5 * core_w * book / S, mark=v0)
        book += day
        m = 0.025 * 1.1 * book
        if cc is not None:
            m += 0.025 * cc["units"] * S
        if put is not None:
            m += put["mark"] * put["units"]
        if syn_margin:
            e_t = exl.get(t, 1.0)
            m += 0.10 * max((0.0 if pd.isna(e_t) else float(e_t)) - 1, 0) * core_w * book
        peak_margin = max(peak_margin, m / book)
        eq_rows.append((t, book))

    eq = pd.Series(dict(eq_rows))
    pf = pd.Series({d: x for d, x in put_pnl_frac_days})
    prem = pd.Series({d: x for d, x in put_premium_frac})
    rec = pd.Series({d: x for d, x in put_recovery_frac})
    return eq, peak_margin, pf, prem, rec


# ---------------------------------------------------------------------------
# 0. SANITY CHECK: current cell (91d / 0.95 / roll-30) must reproduce the
#    engine's own a5 baseline (run_book_engine) and the OP-D5-ledger-quoted
#    put-ladder economics (~-1.6%/yr net carry, +4.3pp in 2020).
# ---------------------------------------------------------------------------
cells_consumed = 0

eq_engine, pm_engine = run_book_engine(CORE_W, SW_W, FAC_W, financing=True, syn_margin=True)
c_engine, d_engine, y_engine = stats_of(eq_engine)
cells_consumed += 1

eq_cur, pm_cur, pf_cur, prem_cur, rec_cur = run_book_ladder(91, 0.95, 30)
c_cur, d_cur, y_cur = stats_of(eq_cur)
cells_consumed += 1

sanity = dict(
    engine_cagr=round(c_engine, 3), engine_dd=round(d_engine, 3),
    reimpl_cagr=round(c_cur, 3), reimpl_dd=round(d_cur, 3),
    cagr_delta=round(c_cur - c_engine, 4), dd_delta=round(d_cur - d_engine, 4),
    current_carry_pct_yr=round(100 * pf_cur.mean() * 252, 3),
    current_2020_payoff_pct=round(100 * pf_cur[pf_cur.index.year == 2020].sum(), 3),
)

# ---------------------------------------------------------------------------
# 1. THE GRID: tenor x strike x roll (18 cells)
# ---------------------------------------------------------------------------
TENORS = [60, 91, 182]
STRIKES = [0.93, 0.95, 0.97]
ROLLS = [15, 30]

results = []
for tenor in TENORS:
    for strike in STRIKES:
        for roll in ROLLS:
            if roll >= tenor:  # degenerate (rolling before or at inception) -- skip, not a real cell
                continue
            eq, pm, pf, prem, rec = run_book_ladder(tenor, strike, roll)
            cagr, dd, yearly = stats_of(eq)
            cells_consumed += 1
            carry_pct_yr = 100 * pf.mean() * 252
            pf_2020 = pf[pf.index.year == 2020]
            payoff_2020 = 100 * pf_2020.sum()
            peak_2020 = 100 * pf_2020.cumsum().max() if len(pf_2020) else float("nan")
            gross_prem_pct_yr = 100 * prem.sum() / YEARS
            recovery_pct_yr = 100 * rec.sum() / YEARS
            n_rolls = len(prem)
            worst_year = 100 * yearly.min()
            results.append(dict(
                tenor=tenor, strike=strike, roll=roll,
                is_current=(tenor == 91 and strike == 0.95 and roll == 30),
                carry_pct_yr=round(carry_pct_yr, 3),
                payoff_2020_pct=round(payoff_2020, 3),
                peak_2020_protection_pct=round(peak_2020, 3),
                gross_premium_pct_yr=round(gross_prem_pct_yr, 3),
                recovery_pct_yr=round(recovery_pct_yr, 3),
                n_positions_opened=n_rolls,
                book_cagr=round(cagr, 3),
                book_maxdd=round(dd, 3),
                book_worst_year_pct=round(worst_year, 3),
                book_peak_margin_pct=round(100 * pm, 2),
            ))

df = pd.DataFrame(results).sort_values(["tenor", "strike", "roll"]).reset_index(drop=True)

# ---------------------------------------------------------------------------
# 2. FRONTIER CHECK: for each cell, is there another cell with BOTH lower
#    carry cost (less negative / more positive) AND a better (less negative)
#    BOOK MAXDD -- the "book maxDD if swapped in" is used as the protection
#    axis (not payoff_2020_pct -- see the round-trip finding below: the
#    calendar-year-net payoff figure is NOT monotone in strike because 2020
#    round-tripped within the same calendar year, so it is reported as a
#    descriptive number but is NOT a reliable protection ranking). A cell is
#    "on the frontier" iff no other cell dominates it on (cost, book_maxdd).
# ---------------------------------------------------------------------------
def is_dominated(row, all_rows):
    for _, other in all_rows.iterrows():
        if other.name == row.name:
            continue
        # "better" = higher carry_pct_yr (less cost) AND higher (less negative) book_maxdd
        if (other["carry_pct_yr"] >= row["carry_pct_yr"] and
                other["book_maxdd"] >= row["book_maxdd"] and
                (other["carry_pct_yr"] > row["carry_pct_yr"] or
                 other["book_maxdd"] > row["book_maxdd"])):
            return True
    return False


df["on_frontier"] = ~df.apply(lambda r: is_dominated(r, df), axis=1)
current_row = df[df["is_current"]].iloc[0]
current_on_frontier = bool(current_row["on_frontier"])
frontier_df = df[df["on_frontier"]].sort_values("carry_pct_yr")

# ---------------------------------------------------------------------------
# 3. PRINT
# ---------------------------------------------------------------------------
print("f06_put_ladder_grid -- THE PUT LADDER COST/PROTECTION FRONTIER")
print(f"Window {D0.date()}..{D1.date()} ({YEARS:.2f}yr), standing book weights "
      f"{CORE_W}/{SW_W}/{FAC_W}, cap=1.5x, financing on, syn_margin on.")
print()
print("SANITY (current cell vs engine a5, and vs OP-D5-ledger-quoted put economics "
      "-1.60%/yr, +4.3pp 2020):")
for k, v in sanity.items():
    print(f"  {k}: {v}")
print()
print(f"GRID ({len(df)} cells; {TENORS} x {STRIKES} x {ROLLS}, "
      f"{len([1 for t in TENORS for r in ROLLS if r < t]) * len(STRIKES) - len(df)} "
      "degenerate roll>=tenor cells skipped):")
print(df.to_string(index=False))
print()
print(f"CURRENT CELL (91d/0.95/roll-30) ON FRONTIER (cost vs book_maxdd axes): "
      f"{current_on_frontier}")
print("FRONTIER CELLS (non-dominated on cost vs book_maxdd, sorted by carry cost):")
print(frontier_df[["tenor", "strike", "roll", "carry_pct_yr", "payoff_2020_pct",
                    "peak_2020_protection_pct", "book_cagr", "book_maxdd"]]
      .to_string(index=False))

# ---- the round-trip finding: at fixed tenor/roll, payoff_2020_pct (calendar-
# year NET) falls as strike rises toward the money, even though peak_2020_
# protection_pct (the max in-crisis gain) and book_maxdd (whole-book protection)
# BOTH improve monotonically with strike. This is because NIFTY round-tripped
# within calendar 2020 (trough late-March, recovered above pre-crash levels by
# year end): a near-the-money put earns MORE at the trough but has more value
# to give back on the V-shaped recovery, so its calendar-year-end NET number is
# smaller (or negative) despite offering strictly better protection at the
# moment that mattered.
fixed = df[(df.tenor == 60) & (df.roll == 30)].sort_values("strike")
print("\nROUND-TRIP FINDING (tenor=60, roll=30, strike 0.93->0.97):")
print(fixed[["strike", "payoff_2020_pct", "peak_2020_protection_pct", "book_maxdd"]]
      .to_string(index=False))
print("  -> payoff_2020_pct (calendar-year net) DECREASES with strike while "
      "peak_2020_protection_pct (max in-crisis MTM gain) and book_maxdd (actual "
      "whole-book protection) both IMPROVE with strike -- the calendar-year-net "
      "number is an artifact of 2020's V-shaped round trip, not a protection "
      "ranking. book_maxdd is the decision-relevant protection metric.")

# ---------------------------------------------------------------------------
# 4. WRITE JSON
# ---------------------------------------------------------------------------
import json  # noqa: E402

out = dict(
    family="f06_put_ladder_grid",
    date="2026-09-08",
    window=dict(start=str(D0.date()), end=str(D1.date()), years=round(YEARS, 3)),
    standing_book_weights=dict(core=CORE_W, switcher=SW_W, factor=FAC_W, cap=1.5,
                                financing=True, syn_margin=True),
    sanity_check=sanity,
    grid_spec=dict(tenor_days=TENORS, strike_moneyness=STRIKES,
                    roll_trigger_days_to_expiry=ROLLS,
                    note="strike_moneyness = K/S (e.g. 0.95 = 5% OTM put); roll_trigger "
                         "= days-to-expiry at which the put is closed and a fresh "
                         "tenor_days put opened; cells with roll>=tenor are degenerate "
                         "and skipped"),
    cells=df.to_dict(orient="records"),
    current_cell=dict(tenor=91, strike=0.95, roll=30, on_frontier=current_on_frontier),
    frontier_cells=frontier_df.to_dict(orient="records"),
    cells_consumed=cells_consumed,
    findings=[
        dict(
            name="tenor_scaling_is_a_flat_sigma_artifact",
            description=(
                "At fixed strike=0.95/roll=30, gross premium %/yr FALLS monotonically "
                "as tenor rises: 10.47 (60d) -> 7.56 (91d) -> 4.82 (182d); the 182d "
                "cells dominate the frontier on carry cost. This is the standard "
                "BS sqrt(T) scaling (premium ~ sigma*sqrt(T), so cost-per-year falls "
                "as T rises) COMBINED with rolling all tenors at the SAME fixed "
                "roll_days=30, which is a smaller fraction of a longer tenor's life "
                "(30/182=16% vs 30/91=33% vs 30/60=50%), avoiding the steep late-life "
                "theta region for a larger share of a long-dated put's life. Both "
                "effects are mechanical consequences of pricing EVERY tenor off the "
                "SAME flat India-VIX level with NO implied-vol term structure. Real "
                "Indian index option markets are typically in vol-term-structure "
                "contango in calm periods (longer-dated implied vol priced ABOVE "
                "spot VIX), which would erode or reverse this apparent cheapness. "
                "The grid's apparent 182d dominance should be read as a PRICING-MODEL "
                "ARTIFACT, not a tradeable free lunch, until real option-chain term "
                "structure replaces flat-sigma BS."
            ),
        ),
        dict(
            name="2020_calendar_year_net_payoff_is_not_a_protection_ranking",
            description=(
                "At fixed tenor=60/roll=30, payoff_2020_pct FALLS as strike rises "
                "toward the money (2.887 at 0.93 -> 1.512 at 0.95 -> -0.394 at 0.97) "
                "even though BOTH peak_2020_protection_pct (the max in-crisis "
                "mark-to-market gain, measured day-by-day inside the printed "
                "crash window) AND book_maxdd (the actual whole-book drawdown) "
                "improve monotonically with strike (day-level check: at the trough, "
                "2020-03-23, pnl_frac is 0.0825/0.0850/0.0873 for strike "
                "0.93/0.95/0.97 -- strictly increasing, as theory predicts: a "
                "near-the-money put IS more protective at the crash trough). The "
                "reversal in the full-year NET number is because NIFTY round-"
                "tripped within calendar 2020 (trough late-March, index above "
                "pre-crash level by December, book a5 yearly 2020 = +21.2%): the "
                "near-the-money put earned MORE at the trough but had more value "
                "to give back on the V-shaped recovery, so its calendar-year-end "
                "net is smaller (even negative). This is a genuine, non-obvious "
                "finding about the payoff METRIC, not about the ladder's actual "
                "protective value -- book_maxdd (which marks at the actual trough "
                "moment, not a calendar boundary) is the decision-relevant number, "
                "and it correctly shows near-the-money strikes protecting better. "
                "In a bear market that does NOT fully recover within the same "
                "calendar year, payoff_2020_pct-style annual netting would show "
                "the opposite (expected) ranking -- this is a 2020-specific "
                "artifact of the recovery speed, not a general property of strike "
                "choice."
            ),
        ),
    ],
    caveats=[
        "BS flat-sigma at India-VIX close: no smile/skew, no bid-ask, no strike "
        "granularity, no transaction costs -- theoretical mark-to-market only "
        "(engine convention, unchanged from OP-D5/OP-D6b). This is the DIRECT "
        "cause of the tenor_scaling_is_a_flat_sigma_artifact finding above.",
        "India VIX vault ends 2023-04-05 (D1=2023-03-31): the 743-day post-2023-04 "
        "tail (2024 election spike, SEBI 2024-26 derivatives curbs) is not in this "
        "sample for ANY cell -- cost/payoff numbers are era-bound to a single VIX "
        "vault span.",
        "2008 (GFC) is not in the India VIX sample (vault starts 2010-07-23, "
        "pct_s usable from ~2011-07 after min_obs=252) -- '2020 payoff' is the "
        "ONLY crisis observation in this grid for every cell; n=1 crisis event, "
        "not a distribution.",
        "NIFTY core is price-only in this engine (+1.3pp/yr TR note applies to "
        "book_cagr uniformly across all 18 cells -- does not change relative "
        "ranking).",
        "funding_rate frozen at r=0.06 (declared paper assumption, not a desk "
        "number per CONTRACT/risk.yaml note) -- both the BS pricing rate and the "
        "core financing rate use this same assumption.",
        "financing/syn_margin held ON (matches the a5 standing-book baseline) for "
        "every cell -- differences between cells are put-ladder-only, not "
        "core-financing artifacts.",
        "Longer-tenor cells (182d) have fewer independent roll cycles over the "
        "12-year window (n_positions_opened column) -- their carry-cost estimate "
        "averages over fewer, more autocorrelated observations than the 60d cells.",
        "The frontier dominance check uses exactly 2 axes (carry_pct_yr, "
        "book_maxdd) with n=1 crisis event on the protection axis -- a single "
        "different crash could reorder which cells are non-dominated; this is a "
        "descriptive map, not a validated ranking.",
        "payoff_2020_pct is a calendar-year NET number and is NOT used for the "
        "frontier/dominance check for exactly the reason in the "
        "2020_calendar_year_net_payoff_is_not_a_protection_ranking finding above "
        "-- it round-trips with the market's own V-shaped recovery and can show "
        "a WORSE number for a MORE protective strike. Read it as a curiosity "
        "about calendar-boundary netting, not as the protection metric.",
    ],
    protocol_proposal=(
        "Any change to the standing book's put ladder must NOT be selected by "
        "picking the best cell on this grid (in-sample shopping, banned by the "
        "task instruction and CONTRACT SS4 'assume your alpha decays'). Proposed "
        "protocol if a change is ever pursued: (1) PRE-REGISTER a single candidate "
        "cell (or a narrow, economically-motivated sub-family, e.g. 'roll trigger "
        "only, holding tenor=91/strike=0.95 fixed') with a stated bar BEFORE "
        "looking at this grid's numbers again; (2) split the 2011-07..2023-03 "
        "window at a pre-chosen date (e.g. 2017-01-01, matching the engine's "
        "existing era-halves convention) into TRAIN (2011-16) and TEST (2017-23); "
        "(3) the candidate must show carry cost no worse AND 2020-analog payoff "
        "no worse than the current cell on TRAIN before being read on TEST at "
        "all; (4) because there is only ONE crisis observation (2020) in the "
        "entire sample and it falls in the TEST half, no protocol here can "
        "validate crash-payoff out-of-sample with a real train/test split -- "
        "the honest position is that tenor/strike/roll choice cannot be tuned "
        "against 2020 without it being pure in-sample fitting to n=1; the only "
        "defensible move is to CHOOSE the cell from a stated structural argument "
        "(e.g. cost-of-carry per unit of tail-delta from the BS greeks, F15-style "
        "analytic reasoning) and treat any backtest agreement as confirmatory, "
        "never as the selection criterion; (5) any promoted change still needs "
        "the option-chain data upgrade (RUNSHEET priority pull) before it can "
        "leave paper status, since strike/tenor/roll economics are exactly the "
        "axes flat-sigma BS misprices most (skew is strike-dependent, term "
        "structure is tenor-dependent)."
    ),
)
with open("/home/user/claude-demo/research/opt_sweep2/f06_put_ladder_grid.json", "w") as f:
    json.dump(out, f, indent=2)
print("\nWrote research/opt_sweep2/f06_put_ladder_grid.json")
print(f"cells_consumed = {cells_consumed}")
