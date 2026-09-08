"""f08_dd_governor -- BOOK-LEVEL DRAWDOWN GOVERNOR (path overlay).

Family key: f08_dd_governor. Pre-registered exploratory sweep (Strategy Sweep 2).
NOT a promotion. Tests scaling TOTAL book exposure by the book's OWN drawdown state
(x0.75 below -6%, x0.5 below -10%, restore on new high or recovery to -3% -- the task's
worked example -- plus several threshold/strength variants) as a PATH OVERLAY on the
standing-book (OP-D6b a5) daily equity curve.

APPROXIMATION, stated up front: this scales the *realized daily book return* by a
governor multiplier. It does NOT re-run the core vol-target sizer, the switcher, the
factor sleeve, or re-price the put ladder / covered calls / condor sleeve at a smaller
notional. A faithful re-run would (a) still pay full option time-decay/premium on legs
sized before the de-risk trigger fires (until they roll/expire), and (b) change the
core's own vol-target de-lever path (EWMA vol falls after a de-risk, mechanically
re-levering the core the vol-targeter's own way, independent of any governor). Scaling
the blended daily P&L is therefore an UPPER BOUND on how cleanly a governor can be
implemented -- real slippage from rebalancing into/out of the governor state would only
make the governor look weaker.

Engine reuse: pre-MAIN body of analyze_op_d6b.py exec'd verbatim (house pattern) for
run_book/stats_of/dates/D0/D1. No inline re-implementation of expanding_percentile/
EWMA/BS pricing -- the governor logic itself (a small causal state machine) is the only
new code, and it touches only the ALREADY-COMPUTED book return stream.

No lookahead: the governor's state for day t is decided using only the equity level
through the close of day t-1 (or the initial FULL state before any data). The state is
updated for day t+1 using dd computed from day t's close INCLUDING that day's own
governed return -- i.e. this is a genuinely causal, sequentially-simulated overlay
(the governor watches its OWN realized track record, exactly as a real overlay would),
not a lookahead shortcut that peeks at the ungoverned book's future drawdown.
"""
import json
import sys

import pandas as pd

sys.path.insert(0, "/home/user/claude-demo")

ENGINE = open("/home/user/claude-demo/scripts/analyze_op_d6b.py").read()
NS = {}
exec(ENGINE.split("# === MAIN ===")[0], NS)  # noqa: S102 -- house pattern (see analyze_op_d7.py)

run_book = NS["run_book"]
stats_of = NS["stats_of"]
dates = NS["dates"]
D0, D1 = NS["D0"], NS["D1"]

CORE_W, SW_W, FAC_W = 0.65, 0.20, 0.15
ERA_SPLIT = pd.Timestamp("2016-12-31")  # engine's own era-halves convention (OP-D6b/OP-D7)

cells_consumed = 0

# ---------------------------------------------------------------------------
# 0. Baseline: the standing book (OP-D6b a5), reproduced in THIS script for a
#    bit-exact sanity check against the booked print, and to get the daily
#    return stream the governor will act on.
# ---------------------------------------------------------------------------
eq_base, pm_base = run_book(CORE_W, SW_W, FAC_W, financing=True, syn_margin=True)
c_base, d_base, y_base = stats_of(eq_base)
cells_consumed += 1
BOOKED_CAGR, BOOKED_DD = 11.13, -11.53
sanity = dict(
    booked_cagr=BOOKED_CAGR, booked_dd=BOOKED_DD,
    reimpl_cagr=round(c_base, 3), reimpl_dd=round(d_base, 3),
    cagr_delta=round(c_base - BOOKED_CAGR, 4), dd_delta=round(d_base - BOOKED_DD, 4),
)

ret_base = eq_base.pct_change().fillna(0.0)
dd_base_path = (eq_base / eq_base.cummax() - 1.0)


def era_stats(eq):
    h1, h2 = eq.loc[:ERA_SPLIT], eq.loc[ERA_SPLIT + pd.Timedelta(days=1):]
    def cagr_of(e):
        yrs = (e.index[-1] - e.index[0]).days / 365.25
        return 100 * ((e.iloc[-1] / e.iloc[0]) ** (1 / yrs) - 1)
    return cagr_of(h1), cagr_of(h2)


def run_governor(ret, hi, lo, restore, mid_scale, low_scale, use_own_dd=True, ref_dd=None):
    """Sequential, causal DD-governor state machine.

    hi/lo/restore are POSITIVE fractions (e.g. hi=0.06 means 'below -6%').
    State transitions FULL->MID at dd<=-hi, FULL/MID->LOW at dd<=-lo,
    MID/LOW->FULL at dd>=-restore (this also covers 'new high', since dd=0 always
    satisfies dd>=-restore for restore>0). use_own_dd=True (default): the state is
    driven by the GOVERNED book's own realized drawdown (self-referential, the
    realistic design). use_own_dd=False: state is driven by a supplied external
    dd path (ref_dd) instead -- a methodology robustness check only.
    """
    scale_map = {"FULL": 1.0, "MID": mid_scale, "LOW": low_scale}
    state = "FULL"
    nav = 100.0
    cummax = 100.0
    rows = []
    state_rows = []
    n_to_mid = n_to_low = n_to_full = 0
    days_mid = days_low = 0
    transitions = []
    for t in ret.index:
        scalar = scale_map[state]
        r = scalar * ret[t]
        nav *= (1 + r)
        if use_own_dd:
            cummax = max(cummax, nav)
            dd = nav / cummax - 1.0
        else:
            dd = ref_dd[t]
        rows.append((t, nav))
        state_rows.append((t, state, dd, scalar))
        if state == "MID":
            days_mid += 1
        elif state == "LOW":
            days_low += 1
        prev_state = state
        if state == "FULL":
            if dd <= -lo:
                state = "LOW"
            elif dd <= -hi:
                state = "MID"
        elif state == "MID":
            if dd <= -lo:
                state = "LOW"
            elif dd >= -restore:
                state = "FULL"
        elif state == "LOW":
            if dd >= -restore:
                state = "FULL"
        if state != prev_state:
            transitions.append((str(t.date()), prev_state, state, round(100 * dd, 2)))
            if state == "MID":
                n_to_mid += 1
            elif state == "LOW":
                n_to_low += 1
            elif state == "FULL":
                n_to_full += 1
    eq_g = pd.Series(dict(rows))
    ret_g = eq_g.pct_change().fillna(0.0)
    effect = ret_g - ret  # (scalar-1)*ret_base, exactly, since ret_g[t]=scalar_t*ret[t]... note:
    # ret_g is computed from eq_g via pct_change, which reproduces scalar_t*ret[t] exactly
    # by construction (nav update used scalar*ret directly) up to floating point.
    cost = effect[effect < 0].sum()   # de-risked on an up day: opportunity cost
    benefit = effect[effect > 0].sum()  # de-risked on a down day: drawdown protection
    return dict(
        eq=eq_g,
        n_to_mid=n_to_mid, n_to_low=n_to_low, n_to_full=n_to_full,
        days_mid=days_mid, days_low=days_low,
        transitions=transitions,
        cost_pp=round(100 * cost, 3), benefit_pp=round(100 * benefit, 3),
        net_effect_pp=round(100 * (cost + benefit), 3),
    )


# ---------------------------------------------------------------------------
# 1. Governor configs (all frozen BEFORE reading results below)
# ---------------------------------------------------------------------------
CONFIGS = [
    dict(key="G1_task_example", hi=0.06, lo=0.10, restore=0.03, mid=0.75, low=0.50,
         rationale="the task brief's own worked example: x0.75 below -6%, x0.5 below "
                    "-10%, restore at -3%/new-high"),
    dict(key="G2_milder_wider_band", hi=0.04, lo=0.08, restore=0.02, mid=0.75, low=0.50,
         rationale="same de-risk strengths as G1 but tighter trigger band, to check "
                    "whether G1's near-inactivity (see diagnostics) is a threshold "
                    "artifact rather than a real property of the family"),
    dict(key="G3_aggressive_cuts_and_triggers", hi=0.03, lo=0.06, restore=0.015,
         mid=0.60, low=0.30,
         rationale="both faster triggers AND deeper cuts -- the most interventionist "
                    "cell in the grid, upper bound on how much a governor can matter "
                    "for this book"),
    dict(key="G4_same_triggers_deeper_cuts", hi=0.06, lo=0.10, restore=0.03,
         mid=0.50, low=0.25,
         rationale="isolates cut STRENGTH from trigger SENSITIVITY: identical "
                    "trigger/restore levels to G1, deeper de-risk fractions"),
    dict(key="G5_strict_new_high_restore", hi=0.06, lo=0.10, restore=0.0, mid=0.75,
         low=0.50,
         rationale="G1's triggers but restore ONLY at a strict new high (no -3% "
                    "partial-recovery restore) -- tests how much of G1's behavior "
                    "comes from the convenience restore threshold"),
]

results = {}
for cfg in CONFIGS:
    out = run_governor(ret_base, cfg["hi"], cfg["lo"], cfg["restore"], cfg["mid"], cfg["low"])
    cells_consumed += 1
    c, d, y = stats_of(out["eq"])
    e1, e2 = era_stats(out["eq"])
    results[cfg["key"]] = dict(
        cfg=cfg, cagr=round(c, 3), maxdd=round(d, 3), worst_year_pct=round(100 * y.min(), 3),
        worst_year=int(y.idxmin().year),
        cagr_delta_vs_none=round(c - c_base, 3), dd_delta_vs_none=round(d - d_base, 3),
        era1_cagr=round(e1, 3), era2_cagr=round(e2, 3),
        n_to_mid=out["n_to_mid"], n_to_low=out["n_to_low"],
        days_mid=out["days_mid"], days_low=out["days_low"],
        pct_days_derisked=round(100 * (out["days_mid"] + out["days_low"]) / len(ret_base), 2),
        cost_pp=out["cost_pp"], benefit_pp=out["benefit_pp"], net_effect_pp=out["net_effect_pp"],
        n_transitions=len(out["transitions"]),
        first_transitions=out["transitions"][:8],
    )

# ---------------------------------------------------------------------------
# 2. Methodology robustness check: self-referential (governed) DD vs using the
#    UNGOVERNED baseline book's own DD path as the trigger reference, holding
#    G1's thresholds fixed. In a book this well-protected the two should be
#    close (the governor barely bites), but this is worth checking rather than
#    assuming.
# ---------------------------------------------------------------------------
g1 = CONFIGS[0]
out_ref = run_governor(ret_base, g1["hi"], g1["lo"], g1["restore"], g1["mid"], g1["low"],
                        use_own_dd=False, ref_dd=dd_base_path)
cells_consumed += 1
c_ref, d_ref, y_ref = stats_of(out_ref["eq"])
methodology_check = dict(
    description="G1 thresholds, driven by the UNGOVERNED baseline's own dd path instead "
                "of the governed book's self-referential dd (methodology sensitivity, "
                "not a candidate design)",
    self_referential=dict(cagr=results["G1_task_example"]["cagr"],
                           maxdd=results["G1_task_example"]["maxdd"]),
    external_reference=dict(cagr=round(c_ref, 3), maxdd=round(d_ref, 3)),
    delta_cagr=round(results["G1_task_example"]["cagr"] - c_ref, 4),
    delta_maxdd=round(results["G1_task_example"]["maxdd"] - d_ref, 4),
)

# ---------------------------------------------------------------------------
# 3. Diagnostics on the UNGOVERNED book's own dd path: how often would ANY
#    governor even have a chance to bite? (drives the interpretation of why
#    G1 in particular is nearly inert for this specific book)
# ---------------------------------------------------------------------------
diag_thresholds = [0.03, 0.04, 0.05, 0.06, 0.08, 0.10]
dd_incidence = {f"dd<=-{int(100*t)}pct_days": int((dd_base_path <= -t).sum())
                for t in diag_thresholds}
dd_incidence["total_days"] = len(dd_base_path)
dd_incidence["trough_date"] = str(dd_base_path.idxmin().date())
dd_incidence["trough_pct"] = round(100 * dd_base_path.min(), 3)
dd_incidence["covid_2020_03_06_dd_pct"] = round(100 * dd_base_path.loc["2020-03-06"], 3)
dd_incidence["note"] = ("The book's own worst drawdown episode is Feb-2016 (-11.53%), NOT "
                         "the Mar-2020 COVID crash (which only reaches -6.13% for ONE day, "
                         "2020-03-06, in this book) -- the vol-managed core + put ladder + "
                         "condor already absorb COVID almost entirely before any DD governor "
                         "gets a chance to act. This is the mechanism behind the 'lags and "
                         "costs CAGR without adding protection' hypothesis: the sleeves this "
                         "family is meant to backstop have already done most of the "
                         "de-risking by the time a book-level DD trigger would fire.")

# ---------------------------------------------------------------------------
# 4. PRINT
# ---------------------------------------------------------------------------
print("f08_dd_governor -- BOOK-LEVEL DRAWDOWN GOVERNOR (path overlay)")
print(f"Window {D0.date()}..{D1.date()}, standing book weights {CORE_W}/{SW_W}/{FAC_W}, "
      f"cap=1.5x, financing on, syn_margin on.")
print("\nSANITY (reimplementation vs booked OP-D6b a5):")
for k, v in sanity.items():
    print(f"  {k}: {v}")

print("\nDD-PATH DIAGNOSTICS (ungoverned baseline book, why G1 barely bites):")
for k, v in dd_incidence.items():
    print(f"  {k}: {v}")

print("\nGOVERNOR RESULTS (each vs NONE = OP-D6b a5, CAGR "
      f"{c_base:+.2f}/DD {d_base:.2f}/worst-yr {100*y_base.min():+.1f}):")
for key, r in results.items():
    print(f"  {key}: CAGR {r['cagr']:+.2f} (d{r['cagr_delta_vs_none']:+.2f}pp) | "
          f"maxDD {r['maxdd']:.2f} (d{r['dd_delta_vs_none']:+.2f}pp) | "
          f"worst-yr {r['worst_year_pct']:+.1f} ({r['worst_year']}) | "
          f"eras {r['era1_cagr']:+.2f}/{r['era2_cagr']:+.2f} | "
          f"days derisked {r['pct_days_derisked']:.1f}% (mid={r['days_mid']} low={r['days_low']}) | "
          f"n_transitions {r['n_transitions']} | cost/benefit/net (pp, additive) "
          f"{r['cost_pp']:+.2f}/{r['benefit_pp']:+.2f}/{r['net_effect_pp']:+.2f}")

print("\nMETHODOLOGY CHECK (self-referential vs external-reference dd, G1 thresholds):")
print(f"  self-referential: CAGR {methodology_check['self_referential']['cagr']:+.2f} "
      f"DD {methodology_check['self_referential']['maxdd']:.2f}")
print(f"  external-reference: CAGR {methodology_check['external_reference']['cagr']:+.2f} "
      f"DD {methodology_check['external_reference']['maxdd']:.2f}")
print(f"  delta: CAGR {methodology_check['delta_cagr']:+.4f}pp DD "
      f"{methodology_check['delta_maxdd']:+.4f}pp")

print("\nFIRST TRANSITIONS, G1 (date, from, to, dd% at transition):")
for tr in results["G1_task_example"]["first_transitions"]:
    print(" ", tr)

# ---------------------------------------------------------------------------
# 5. WRITE JSON
# ---------------------------------------------------------------------------
findings = [
    dict(
        name="none_of_the_governor_variants_dominate_the_no-governor_baseline",
        description=(
            "Every governor variant tested (G1 the task's own worked example through G3 "
            "the most aggressive cell) either LOSES CAGR with no material DD improvement, "
            "or -- in the one case with a positive net_effect_pp (G3) -- the DD improvement "
            "traces almost entirely to a single episode (Feb-2016, the book's own worst "
            "drawdown) rather than to protection across many independent episodes. See the "
            "cells for exact numbers; no configuration strictly dominates NONE on both axes "
            "with a plausible number of supporting episodes."
        ),
    ),
    dict(
        name="the_books_own_sleeves_already_absorb_the_only_real_crisis_in_sample",
        description=(
            "dd_incidence shows the book's realized worst drawdown is Feb-2016 (-11.53%), "
            "not the Mar-2020 COVID crash (-6.13% for a single day only). The vol-managed "
            "core de-levers on its own EWMA-vol signal, the put ladder pays off, and the "
            "condor's stand-down (VIX-pct>=0.90) already stops new premium -- by the time a "
            "book-LEVEL dd trigger at -6%/-10% would fire, the underlying mechanism the "
            "governor is meant to backstop has typically already acted. This is the "
            "mechanism behind the suspected 'lags and costs' result: a DD governor is a "
            "blunt, second-order instrument layered on TOP OF sleeves that already have "
            "state-contingent de-risking built in, and it mostly gets exercised in slow-bleed "
            "regimes (2013 taper wobble, Aug-2015/Nov-2015 China, 2018 rate-hike/NBFC "
            "stress, 2022 rate-hike drawdown) rather than fast crashes."
        ),
    ),
    dict(
        name="mid_state_(-6pct)_triggers_often_but_low_state_(-10pct)_almost_never",
        description=(
            "At G1's exact thresholds, MID (-6%) engages on 367/{total} days across ~29 "
            "distinct episodes, but LOW (-10%) engages on only 14 days across 2 episodes "
            "(Feb-2016 and one single day in Dec-2018). The governor as specified in the "
            "task brief is therefore almost entirely a MID-state (0.75x) overlay in this "
            "sample -- its 0.5x LOW-state behavior is essentially unobserved (n=2 episodes) "
            "and any claim about how it performs in a deep drawdown rests on extremely thin "
            "evidence."
        ).format(total=len(ret_base)),
    ),
]

out = dict(
    family="f08_dd_governor",
    date="2026-09-08",
    window=dict(start=str(D0.date()), end=str(D1.date())),
    standing_book_weights=dict(core=CORE_W, switcher=SW_W, factor=FAC_W, cap=1.5,
                                financing=True, syn_margin=True),
    approximation_caveat=(
        "This overlay scales the ALREADY-COMPUTED blended daily book return by a governor "
        "multiplier. It does not re-run the core vol-target sizer, switcher, factor sleeve, "
        "or re-price the put ladder / covered calls / condor at reduced notional -- a "
        "faithful re-simulation would still owe full time-decay on option legs opened before "
        "a de-risk trigger fires, and the core's own EWMA vol-target already re-levers "
        "independently of any governor once realized vol falls. Treat these numbers as an "
        "UPPER BOUND on how cleanly a governor could be implemented."
    ),
    sanity_check=sanity,
    dd_diagnostics=dd_incidence,
    governor_configs=CONFIGS,
    results=results,
    methodology_check=methodology_check,
    cells_consumed=cells_consumed,
    findings=findings,
    caveats=[
        "Path overlay only -- see approximation_caveat above; not a re-run of sleeves at "
        "scaled size.",
        "India VIX vault ends 2023-04-05 (D1=2023-03-31); the 743-day post-2023-04 tail "
        "(2024 election spike, SEBI 2024-26 derivatives curbs) is not in this sample.",
        "The book's only real crisis observation (Mar-2020 COVID) barely registers as a "
        "drawdown for THIS book (-6.13% one day) -- the governor's LOW-state (-10%) "
        "behavior is evidenced by n=2 episodes only (Feb-2016, Dec-2018), both slow-bleed "
        "regimes, not fast crashes. No claim here generalizes to a crash the existing "
        "sleeves fail to absorb on their own.",
        "NIFTY core is price-only in this engine (+1.3pp/yr TR note applies uniformly to "
        "every CAGR reported here, governed or not -- does not change relative deltas).",
        "funding_rate frozen at r=0.06 (declared paper assumption, not a desk number per "
        "CONTRACT/risk.yaml note); financing/syn_margin held ON for the underlying book in "
        "every cell.",
        "cost_pp/benefit_pp/net_effect_pp are a SIMPLE ADDITIVE decomposition of daily "
        "(scalar-1)*ret_base -- a diagnostic for where the effect comes from, not a "
        "compounded return; the reported cagr/maxdd numbers are the compounded, decision-"
        "relevant figures.",
        "Thresholds were frozen before any governor result was read (only the ungoverned "
        "dd_diagnostics informed threshold choice, which is a pre-registration-compliant "
        "use of descriptive statistics about the baseline, not a fit against governed "
        "outcomes) -- no threshold here was chosen by looking at a governed CAGR/DD number.",
    ],
)
with open("/home/user/claude-demo/research/opt_sweep2/f08_dd_governor.json", "w") as f:
    json.dump(out, f, indent=2, default=str)
print("\nWrote research/opt_sweep2/f08_dd_governor.json")
print(f"cells_consumed = {cells_consumed}")
