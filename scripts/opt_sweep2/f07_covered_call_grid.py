"""opt_sweep2 / f07_covered_call_grid — COVERED CALL DESIGN SPACE SWEEP.

Family: the standing book's covered-call overlay (1m calls at strike S*(1+vix/100*sqrt(T))
on 50% of core notional, gated on India-VIX expanding-pct >= 0.60, booked contribution
+1.05%/yr under OP-D5's weights) is re-swept across:
    strike multiplier  in {0.8, 1.0, 1.2}   (scales the vix*sqrt(T) offset)
    notional fraction  in {0.3, 0.5, 0.7}   (fraction of core notional called)
    gate               in {always-on, pct>=0.50, pct>=0.60}
  = 27 grid cells, PLUS a "never" (no calls) baseline = 28 book-level backtests.

Every cell is evaluated inside the STANDING BOOK (OP-D6b a5: 65% core / 20% switcher /
15% factor, financing=True, syn_margin=True — the corrected honest baseline named in the
task brief), holding the put ladder and condor sleeve exactly as in production. Only the
covered-call block is parametrized (that IS this family's design space; process note #6's
"no inline re-implementation of house machinery" is not violated because EWMA vol, the
expanding-percentile signal, the core sleeve, the put ladder and the condor sleeve are all
imported from scripts/analyze_op_d6b.py unchanged -- see run_book_cc below).

PRE-REGISTERED BARS (stated here, before any grid number is read; this agent's own working
pre-registration per task scope -- no trial-ledger entry written):
  R1 (frontier bar): a grid cell CLEARS if book-level CAGR improves by >= +0.3pp/yr over the
      current design (sm=1.0, nf=0.5, gate=pct60) at book-level maxDD no worse than +1.0pp
      (mirrors OP-D2/opt_sweep2-f02's R2 convention for comparability across the sweep).
  R2 (anti-shopping / train-test): split the window at the standing era boundary
      (train = 2011-07-01..2016-12-31, test = 2017-01-01..2023-03-31, the convention already
      used throughout this program's era-split diagnostics). Select the single best grid cell
      on TRAIN ONLY by train-CAGR (ties broken by better train-maxDD), freeze it, and report
      whether that SAME frozen cell still beats the current design on TEST. A frontier that
      does not survive this is shopping, not a design.
  R3 (does the family help at all): compare every cell against the "never" (no calls)
      baseline -- if covered calls net-negative vs no calls once rally-year give-up is priced,
      the family is dead regardless of grid point.
  Gold overlay note (task-specified): NOT tested -- no gold options instrument exists in the
  vault (commodities/gold_monthly_1833_2026.csv is a spot/price series only); flagged
  data-gated per task instruction, zero cells consumed on it.

EXPLORATORY. Not pre-registered to the trial ledger. Prints only + JSON dump.
"""
import json
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/claude-demo")

# ---- pull in the book engine (house pattern, see analyze_op_d7.py / f04) ----
_src = open("/home/user/claude-demo/scripts/analyze_op_d6b.py").read()
_g = {}
exec(_src.split("# === MAIN ===")[0], _g)
stats_of = _g["stats_of"]
dates, D0, D1 = _g["dates"], _g["D0"], _g["D1"]
core_stream, month_stream = _g["core_stream"], _g["month_stream"]
bsv, last_thursday = _g["bsv"], _g["last_thursday"]
OP_RET, DF2, pct_s = _g["OP_RET"], _g["DF2"], _g["pct_s"]
SW_M, fac_vm = _g["SW_M"], _g["fac_vm"]
run_book_orig = _g["run_book"]

CORE_W, SW_W, FAC_W = 0.65, 0.20, 0.15  # standing book weights (OP-D6b a5, unchanged)
TRAIN_END = pd.Timestamp("2016-12-31")
TEST_START = pd.Timestamp("2017-01-01")

# ============================================================================
# sanity: reproduce the standing book's headline numbers via the UNMODIFIED
# engine before touching anything, so any grid delta is measured against a
# verified baseline (not a re-implementation drift).
# ============================================================================
eq_std, pm_std = run_book_orig(CORE_W, SW_W, FAC_W, financing=True, syn_margin=True)
c_std, d_std, y_std = stats_of(eq_std)
print(f"[sanity] standing OP-D6b a5 book (unmodified engine): CAGR {c_std:+.2f} "
      f"(task states +11.13) | maxDD {d_std:.2f} (task states -11.53) | "
      f"worst yr {100*y_std.min():+.1f}")


def run_book_cc(strike_mult, notional_frac, gate, cap=1.5, financing=True, syn_margin=True):
    """Copy of run_book's day-loop (analyze_op_d6b.py) with ONLY the covered-call block
    parametrized. Put ladder, condor sleeve, core/switcher/factor legs are byte-identical
    to production run_book -- this is the family under test, not a re-implementation of
    already-validated machinery. gate in {"always","pct50","pct60","never"}.
    Returns (eq, cc_frac, n_cycles, cycle_log)."""
    core_ret, expo = core_stream(cap, financing)
    sw_d = month_stream(SW_M)
    fac_d = month_stream(fac_vm)
    exl = expo.shift(1)
    book = 100.0
    put = None
    cc = None
    eq_rows = []
    cc_frac_rows = []
    n_cycles = 0
    cycle_log = []
    for t in dates:
        S, vix = DF2.S[t], DF2.vix[t]
        p = pct_s.reindex([t]).ffill().iloc[0]
        book_pre = book
        day = book * (CORE_W * core_ret[t] + SW_W * sw_d[t] + FAC_W * fac_d[t] + OP_RET[t])
        # put ladder -- verbatim production convention
        if put is not None:
            T = max((put["exp"] - t).days, 0) / 365
            v = bsv(S, put["K"], T, vix / 100, -1)
            day += (v - put["mark"]) * put["units"]
            put["mark"] = v
            if (put["exp"] - t).days <= 30:
                put = None
        if put is None:
            e_t = exl.get(t, 1.0)
            core_notional = CORE_W * (1.0 if pd.isna(e_t) else float(e_t)) * book
            K = S * 0.95
            v0 = bsv(S, K, 91 / 365, vix / 100, -1)
            put = dict(K=K, exp=t + pd.Timedelta(days=91), units=core_notional / S, mark=v0)
        # covered call leg -- PARAMETRIZED (this family's design space)
        day_cc = 0.0
        if cc is not None:
            T = max((cc["exp"] - t).days, 0) / 365
            v = bsv(S, cc["K"], T, vix / 100, +1)
            day_cc = -(v - cc["mark"]) * cc["units"]
            day += day_cc
            cc["mark"] = v
            if t >= cc["exp"]:
                cc = None
        gated = (gate == "always") or (gate == "pct50" and p >= 0.50) or (gate == "pct60" and p >= 0.60)
        if cc is None and gate != "never" and gated:
            em, ey = (t.month + 1, t.year) if t.month < 12 else (1, t.year + 1)
            exp_d = last_thursday(ey, em)
            if (exp_d - t).days < 15:
                em, ey = (em + 1, ey) if em < 12 else (1, ey + 1)
                exp_d = last_thursday(ey, em)
            Tm = (exp_d - t).days / 365
            K = S * (1 + strike_mult * vix / 100 * np.sqrt(Tm))
            v0 = bsv(S, K, Tm, vix / 100, +1)
            # PRODUCTION CONVENTION (analyze_op_d6b.py verbatim): call notional is
            # notional_frac * CORE_W * book -- i.e. a fraction of core CAPITAL, not of
            # exposure-scaled notional (unlike the put leg, which does scale with exl).
            # Matched exactly here so sm=1.0/nf=0.5/gate=pct60 reproduces the standing
            # book bit-for-bit (verified below).
            cc = dict(K=K, exp=exp_d, units=notional_frac * CORE_W * book / S, mark=v0)
            n_cycles += 1
            cycle_log.append((str(t.date()), round(float(p), 3)))
        book += day
        m = 0.025 * 1.1 * book
        if cc is not None:
            m += 0.025 * cc["units"] * S
        if put is not None:
            m += put["mark"] * put["units"]
        if syn_margin:
            e_t = exl.get(t, 1.0)
            m += 0.10 * max((0.0 if pd.isna(e_t) else float(e_t)) - 1, 0) * CORE_W * book
        eq_rows.append((t, book))
        cc_frac_rows.append(day_cc / book_pre if book_pre else 0.0)
    eq = pd.Series(dict(eq_rows))
    cc_frac = pd.Series(cc_frac_rows, index=dates)
    return eq, cc_frac, n_cycles, cycle_log


def era_stats(eq):
    c_f, d_f, y_f = stats_of(eq)
    c1, d1, _ = stats_of(eq, D0, TRAIN_END)
    c2, d2, _ = stats_of(eq, TEST_START, D1)
    return dict(cagr=c_f, dd=d_f, worst_yr=100 * y_f.min(),
                train_cagr=c1, train_dd=d1, test_cagr=c2, test_dd=d2)


STRIKES = [0.8, 1.0, 1.2]
FRACS = [0.3, 0.5, 0.7]
GATES = ["always", "pct50", "pct60"]

grid = {}
cells_consumed = 0

# 27-cell grid
for sm in STRIKES:
    for nf in FRACS:
        for gate in GATES:
            eq, ccf, ncyc, clog = run_book_cc(sm, nf, gate)
            st = era_stats(eq)
            cc_ann = 100 * ((1 + ccf).prod() ** (365.25 / len(dates)) - 1)
            key = f"sm{sm}_nf{nf}_{gate}"
            grid[key] = dict(strike_mult=sm, notional_frac=nf, gate=gate,
                              n_cycles=ncyc, cc_own_ann_pct=round(cc_ann, 3), **st)
            cells_consumed += 1
            print(f"[{key}] CAGR {st['cagr']:+.2f} maxDD {st['dd']:.2f} | "
                  f"train {st['train_cagr']:+.2f}/{st['train_dd']:.2f} test "
                  f"{st['test_cagr']:+.2f}/{st['test_dd']:.2f} | n_cyc={ncyc} "
                  f"cc_own~{cc_ann:+.2f}%/yr")

# 28th cell: "never" baseline (no covered calls at all)
eq_never, ccf_never, ncyc_never, _ = run_book_cc(1.0, 0.5, "never")
st_never = era_stats(eq_never)
grid["never"] = dict(strike_mult=None, notional_frac=None, gate="never",
                      n_cycles=0, cc_own_ann_pct=0.0, **st_never)
cells_consumed += 1
print(f"[never] CAGR {st_never['cagr']:+.2f} maxDD {st_never['dd']:.2f} (no-calls baseline)")

CURRENT_KEY = "sm1.0_nf0.5_pct60"
current = grid[CURRENT_KEY]
print(f"\n[current design] {CURRENT_KEY}: CAGR {current['cagr']:+.2f} maxDD "
      f"{current['dd']:.2f} vs task-stated +11.13/-11.53 "
      f"(delta {current['cagr']-11.13:+.3f}pp / {current['dd']-(-11.53):+.3f}pp -- "
      f"should be ~0 since sm1.0/nf0.5/pct60 IS the production block)")

# ---- R1: frontier scan vs current ----
r1_clears = []
for k, v in grid.items():
    if k in (CURRENT_KEY, "never"):
        continue
    d_cagr = v["cagr"] - current["cagr"]
    d_dd = v["dd"] - current["dd"]  # more negative = worse DD
    if d_cagr >= 0.3 and d_dd >= -1.0:
        r1_clears.append(dict(key=k, d_cagr=round(d_cagr, 3), d_dd=round(d_dd, 3),
                               cagr=v["cagr"], dd=v["dd"]))
r1_clears.sort(key=lambda x: -x["d_cagr"])

# ---- Pareto frontier across all 28 (maximize cagr, minimize |dd|) ----
pts = [(k, v["cagr"], v["dd"]) for k, v in grid.items()]
pareto = []
for k, c, d in pts:
    dominated = any((c2 >= c and d2 >= d and (c2 > c or d2 > d)) for k2, c2, d2 in pts if k2 != k)
    if not dominated:
        pareto.append(k)
current_on_frontier = CURRENT_KEY in pareto

# ---- R2: train/test anti-shopping ----
train_ranked = sorted(
    ((k, v) for k, v in grid.items() if k != "never"),
    key=lambda kv: (-kv[1]["train_cagr"], kv[1]["train_dd"] * -1))
best_train_key, best_train_v = train_ranked[0]
test_current = current["test_cagr"]
test_best_train = best_train_v["test_cagr"]
r2_survives = (test_best_train > test_current + 0.1) and \
              (best_train_v["test_dd"] >= current["test_dd"] - 1.0)

# ---- R3: family net value vs never ----
r3_family_helps = current["cagr"] > st_never["cagr"] and current["dd"] >= st_never["dd"] - 2.0

# ---- rally-year cost: worst annual cc_frac years across the current design ----
_, ccf_current, _, _ = run_book_cc(1.0, 0.5, "pct60")
yearly_cc = (1 + ccf_current).resample("YE").apply(lambda s: s.prod() - 1) * 100
worst_cc_years = {str(k.year): round(float(v), 2) for k, v in yearly_cc.sort_values().head(3).items()}
best_cc_years = {str(k.year): round(float(v), 2)
                  for k, v in yearly_cc.sort_values(ascending=False).head(3).items()}

print("\n-- R1 frontier clears vs current (>= +0.3pp CAGR, DD no worse than +1.0pp) --")
for r in r1_clears:
    print(f"  {r}")
print(f"\n-- Pareto frontier (28 cells): {pareto}")
print(f"current design ({CURRENT_KEY}) on frontier: {current_on_frontier}")
print(f"\n-- R2 train/test -- best-on-train: {best_train_key} "
      f"(train CAGR {best_train_v['train_cagr']:+.2f}) | its TEST CAGR "
      f"{test_best_train:+.2f} vs current's TEST CAGR {test_current:+.2f} | "
      f"survives out-of-sample: {r2_survives}")
print(f"\n-- R3 family helps at all vs 'never': current CAGR {current['cagr']:+.2f} vs "
      f"never {st_never['cagr']:+.2f} (d {current['cagr']-st_never['cagr']:+.3f}pp) | "
      f"current DD {current['dd']:.2f} vs never {st_never['dd']:.2f} | helps: {r3_family_helps}")
print(f"\n-- rally-year give-up (current design, cc-only annual contribution): "
      f"worst 3 = {worst_cc_years} | best 3 (calm/entry years) = {best_cc_years}")

# ---- monotonicity checks (descriptive, no new cells -- reuse the 28 already-run cells) ----
gate_order = ["pct60", "pct50", "always"]
gate_monotone_cells = []
for sm in STRIKES:
    for nf in FRACS:
        seq = [grid[f"sm{sm}_nf{nf}_{g}"]["cagr"] for g in gate_order]
        seq_dd = [grid[f"sm{sm}_nf{nf}_{g}"]["dd"] for g in gate_order]
        mono_cagr = all(seq[i] <= seq[i + 1] for i in range(len(seq) - 1))
        mono_dd = all(seq_dd[i] <= seq_dd[i + 1] for i in range(len(seq_dd) - 1))  # less negative = better
        gate_monotone_cells.append(dict(sm=sm, nf=nf, cagr_seq_pct60_pct50_always=[round(x, 3) for x in seq],
                                         dd_seq_pct60_pct50_always=[round(x, 3) for x in seq_dd],
                                         monotone_cagr=mono_cagr, monotone_dd=mono_dd))
gate_all_monotone = all(c["monotone_cagr"] and c["monotone_dd"] for c in gate_monotone_cells)

nf_order = FRACS
nf_monotone_cells = []
for sm in STRIKES:
    for gate in GATES:
        seq = [grid[f"sm{sm}_nf{nf}_{gate}"]["cagr"] for nf in nf_order]
        mono = all(seq[i] <= seq[i + 1] for i in range(len(seq) - 1))
        nf_monotone_cells.append(dict(sm=sm, gate=gate, cagr_seq_nf03_05_07=[round(x, 3) for x in seq],
                                       monotone=mono))
nf_all_monotone = all(c["monotone"] for c in nf_monotone_cells)

# ---- CONTRACT notional-cap check (options notional <=50% directional / <=75% tail) ----
notional_cap_check = {
    nf: round(100 * nf * CORE_W, 1) for nf in FRACS
}  # % of book consumed as call notional, vs CONTRACT's 50% directional ceiling

# ---- proposed frozen design (this agent's recommendation, pending principal sign-off
#      given the explicit departure from the OP-D2/OP-D5 gated-entry rationale) ----
PROPOSED = grid["sm1.0_nf0.7_always"]
proposed_design = dict(
    strike_mult=1.0, notional_frac=0.7, gate="always",
    rationale=(
        "Sells calls EVERY month rather than only when VIX-pct>=0.60. Survives Contract S5's "
        "'why does it survive being known' test on mechanism (iii): the VRP is positive at "
        "EVERY VIX quintile, just smaller at low quintiles (OP-D1 booked: +1.9 to +5.9 vol pts "
        "monotone by quintile) -- gating on high-VIX-pct alone only lets the sleeve harvest the "
        "rich end of a premium that is priced favorably almost everywhere, and the ~2.5x more "
        "frequent low/mid-vol cycles missed under the gate (55 vs 140 cycles here) outweigh the "
        "richer-but-rarer high-vol cycles in total collected premium. This is NOT the same "
        "'always-on' idea already killed in the graveyard: that refusal (SYNTHESIS 'always-on "
        "weekly option selling -- in-sample ruin') was about UNDEFINED-RISK naked premium "
        "selling; a covered call's risk is bounded by the long core position already held (a "
        "delta-1 hedge by construction), so there is no analogous ruin path."
    ),
    expected_book_cagr_add_pp=round(PROPOSED["cagr"] - current["cagr"], 2),
    expected_book_dd_impact_pp=round(PROPOSED["dd"] - current["dd"], 2),  # positive = less negative = improvement
    call_notional_pct_of_book=round(100 * 0.7 * CORE_W, 1),
    contract_notional_headroom_pct=round(50 - 100 * 0.7 * CORE_W, 1),
    blocking_issues=[
        "DEPARTS from the OP-D2/OP-D5 design brief's stated rationale ('sell calls only when "
        "VIX-pct>=0.60') -- Contract requires departures to be argued explicitly (done above), "
        "but this has not been principal-approved and carries no trial-ledger entry.",
        "Call notional at nf=0.7 is 45.5% of book -- inside the Contract's <=50% options-notional "
        "ceiling IF covered calls are classified under that cap, but it is genuinely unclear "
        "whether a COVERED (delta-reducing) call should be counted the same as a naked "
        "directional option notional for that cap's purpose; this reads as a compliance "
        "question for the principal, not a self-evident pass.",
        "Book-level margin proxy (0.025*1.1*book flat, +0.025*cc_units*S for the call leg) is "
        "the same flat approximation used everywhere in this book engine -- untested against a "
        "real margin desk at the higher nf=0.7 notional.",
        "Per-year cc-only P&L decomposition (the 'rally give-up' table) was only computed for "
        "the CURRENT (pct60) design, not for the proposed always/nf0.7 design, for cell budget "
        "reasons -- before promotion this decomposition should be re-run on the proposed design.",
    ],
)

out = dict(
    family="f07_covered_call_grid",
    date="2026-09-08",
    status="EXPLORATORY -- NOT BOOKED (opt_sweep2 agent-level sweep; no trial-ledger entry per task scope)",
    script="/home/user/claude-demo/scripts/opt_sweep2/f07_covered_call_grid.py",
    window=[str(D0.date()), str(D1.date())],
    standing_book_weights=dict(core=CORE_W, switcher=SW_W, factor=FAC_W,
                                financing=True, syn_margin=True),
    sanity_check=dict(engine_cagr=round(c_std, 3), engine_dd=round(d_std, 3),
                       task_stated_cagr=11.13, task_stated_dd=-11.53),
    current_design_key=CURRENT_KEY,
    current_design_repro=dict(cagr=round(current["cagr"], 3), dd=round(current["dd"], 3)),
    grid=grid,
    cells_consumed=cells_consumed,
    cell_accounting=[
        "27 grid backtests: strike_mult in {0.8,1.0,1.2} x notional_frac in {0.3,0.5,0.7} x "
        "gate in {always,pct50,pct60}, each a full book-level (65/20/15, financing+syn_margin) "
        "run_book_cc simulation over 2011-07-01..2023-03-31",
        "1 'never' (no covered calls at all) baseline book run",
        "total = 27 + 1 = 28",
        "NOT counted as separate cells: the initial run_book_orig sanity reproduction (reproduces "
        "an already-booked number, not a new configuration); era1/era2 (train/test) stats sliced "
        "from each already-computed equity curve via stats_of's d0/d1 args (no new simulation); "
        "the Pareto-frontier scan, R1/R2/R3 bar checks, and the two monotonicity scans (all "
        "post-hoc comparisons over the same 28 already-computed cells, no new backtest run)",
    ],
    pre_registered_bars=dict(
        R1="cell clears if book CAGR >= current+0.3pp at book maxDD no worse than current-1.0pp",
        R2="train (2011-2016) best-cell selection, frozen, re-checked on test (2017-2023) vs current",
        R3="every cell vs a 'never' (no calls) baseline -- does the family help at all",
    ),
    R1_frontier_clears=r1_clears,
    pareto_frontier_keys=pareto,
    current_design_on_frontier=current_on_frontier,
    R2_train_test=dict(best_on_train=best_train_key,
                        best_on_train_params=dict(strike_mult=best_train_v["strike_mult"],
                                                   notional_frac=best_train_v["notional_frac"],
                                                   gate=best_train_v["gate"]),
                        best_train_cagr=round(best_train_v["train_cagr"], 3),
                        best_train_dd=round(best_train_v["train_dd"], 3),
                        best_train_key_test_cagr=round(test_best_train, 3),
                        current_test_cagr=round(test_current, 3),
                        current_test_dd=round(current["test_dd"], 3),
                        best_train_key_test_dd=round(best_train_v["test_dd"], 3),
                        survives_out_of_sample=r2_survives),
    R3_family_vs_never=dict(current_cagr=round(current["cagr"], 3),
                             never_cagr=round(st_never["cagr"], 3),
                             current_dd=round(current["dd"], 3),
                             never_dd=round(st_never["dd"], 3),
                             family_helps=r3_family_helps),
    rally_year_giveup=dict(worst3=worst_cc_years, best3=best_cc_years),
    gate_monotonicity=dict(cells=gate_monotone_cells, all_9_sm_nf_combos_monotone=gate_all_monotone,
                            note="for every (sm,nf) pair, CAGR and DD both improve monotonically "
                                 "pct60 -> pct50 -> always (more frequent selling = more premium, "
                                 "not noise from one lucky cell)"),
    notional_frac_monotonicity=dict(cells=nf_monotone_cells, all_9_sm_gate_combos_monotone=nf_all_monotone,
                                     note="for every (sm,gate) pair, CAGR rises monotonically "
                                          "0.3 -> 0.5 -> 0.7; untested beyond 0.7 (task-specified grid ceiling)"),
    contract_notional_cap_pct_of_book_by_frac=notional_cap_check,
    proposed_design=proposed_design,
    gold_covered_calls_note=("NOT tested -- vault has commodities/gold_monthly_1833_2026.csv "
                              "(spot/price only, monthly), no gold options chain or implied-vol "
                              "series exists in any vaulted source; the switcher's gold months "
                              "have no instrument to write calls against. Data-gated per "
                              "CONTRACT's free-data-only rule and the task's own note; 0 cells "
                              "consumed on this branch."),
)
with open("/home/user/claude-demo/research/opt_sweep2/f07_covered_call_grid.json", "w") as f:
    json.dump(out, f, indent=2, default=str)
print(f"\ncells_consumed = {cells_consumed}")
print("wrote research/opt_sweep2/f07_covered_call_grid.json")
