#!/usr/bin/env python3
"""Registry CI validator — CONTRACT §10 / DESIGN §0.

A registry violating its own budgets must FAIL TO LOAD: this script exits non-zero on any
violation. Checks: frozen-mandate integrity, evidence-tier rules (Tier-C reduce-only), per-block
budget containment, worst-case (3-sigma-style) aggregation inside mandate caps, turnover budgets,
provenance completeness on every parameter, DAG acyclicity, provisional-data tier caps.
"""
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
ERRORS: list[str] = []
WARNINGS: list[str] = []


def err(msg: str) -> None:
    ERRORS.append(msg)


def warn(msg: str) -> None:
    WARNINGS.append(msg)


def load(name: str) -> dict:
    with open(ROOT / name) as f:
        return yaml.safe_load(f)


def lo(x):
    return x[0] if isinstance(x, list) else x


def hi(x):
    return x[1] if isinstance(x, list) else x


PROVENANCE_KEYS = {"source", "tier", "confidence"}


def check_provenance(node, path: str) -> None:
    """Every dict carrying a 'value' key is a parameter and must carry provenance."""
    if isinstance(node, dict):
        # a node is a parameter iff it carries a scalar/list 'value' (dict-valued 'value' keys are
        # sub-sections, e.g. the factor book's value sleeve)
        if "value" in node and not isinstance(node["value"], dict):
            missing = PROVENANCE_KEYS - node.keys()
            if missing:
                err(f"provenance missing {sorted(missing)} at {path}")
            if "changes_if" not in node:
                warn(f"no 'changes_if' (what would change it) at {path}")
        for k, v in node.items():
            check_provenance(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            check_provenance(v, f"{path}[{i}]")


def main() -> int:
    mandate = load("mandate.yaml")
    books = load("books.yaml")
    ladder = load("ladder.yaml")
    risk = load("risk.yaml")
    sleeves = load("sleeves.yaml")
    costs = load("costs.yaml")

    # ---- 1. Frozen mandate integrity ------------------------------------------------
    frozen = mandate["frozen"]
    expected = {
        "gross_leverage_cap": 1.50, "debt_weight_cap": 0.70, "gold_weight_cap": 0.50,
        "name_entry_cap": 0.06, "name_drift_cap": 0.10, "in_progress_aggregate_cap": 0.20,
        "options_notional_cap_directional": 0.50, "options_notional_cap_tail": 0.75,
    }
    for k, v in expected.items():
        if frozen.get(k) != v:
            err(f"frozen mandate cap changed: {k}={frozen.get(k)} != {v} (needs principal sign-off)")
    if frozen["hedge_ratio_grid"] != [0.0, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50]:
        err("hedge grid altered from frozen 7-point sweep")

    # ---- 2. Ladder: tiers, reduce-only, block budgets, DAG --------------------------
    budgets = ladder["budgets"]["regime_score_blocks"]
    if sum(budgets.values()) > 1.0 + 1e-9:
        err(f"regime-score block budgets sum to {sum(budgets.values()):.2f} > 1.0")
    if ladder["budgets"]["tierC_overlay_cap"] > 0.10:
        err("Tier-C overlay cap exceeds 0.10")
    valid_blocks = set(budgets) | {"tierC_overlay", "long_wave", "context_only"}
    ids = set()
    for e in ladder["entries"]:
        eid = e["id"]
        ids.add(eid)
        if e["tier"] not in ("A", "B", "C"):
            err(f"{eid}: invalid tier {e['tier']}")
        if e["tier"] == "C" and not e.get("reduce_only", False):
            err(f"{eid}: Tier C must be reduce_only")
        if e["block"] not in valid_blocks:
            err(f"{eid}: unknown block {e['block']}")
        if e["block"] == "tierC_overlay" and e["tier"] != "C":
            err(f"{eid}: only Tier-C entries may draw from the tierC_overlay budget")
        if e["tier"] == "C" and e["block"] in budgets and not e.get("reduce_only", False):
            err(f"{eid}: Tier-C entry inside additive budget without reduce_only")
        if e["tier"] == "C" and e["block"] in budgets and e.get("contribution_clamp") != "non_positive":
            err(f"{eid}: Tier-C entry inside an ADDITIVE block must carry contribution_clamp: "
                "non_positive (else a positive reading adds regime score through the shared "
                "block average - Contract §4 violation the reduce_only flag alone cannot catch)")
    # DAG acyclicity
    graph = {e["id"]: e.get("inputs", []) for e in ladder["entries"]}
    for eid, deps in graph.items():
        for d in deps:
            if d not in ids:
                err(f"{eid}: unknown dependency {d}")
    state: dict[str, int] = {}

    def dfs(n: str, stack: tuple) -> None:
        if state.get(n) == 1:
            err(f"dependency cycle: {' -> '.join(stack + (n,))}")
            return
        if state.get(n) == 2:
            return
        state[n] = 1
        for d in graph.get(n, []):
            dfs(d, stack + (n,))
        state[n] = 2

    for n in graph:
        dfs(n, ())

    # long-wave block must have no regime-score seat
    for e in ladder["entries"]:
        if e["block"] == "long_wave" and e["tier"] != "C":
            err(f"{e['id']}: long-wave entries must be Tier C (reduce-only expression)")

    # ---- 3. Books: turnover budgets, leverage, name counts --------------------------
    for bname, b in books["books"].items():
        if hi(b["turnover_design_point"]["value"]) > b["turnover_cap_oneway"] + 1e-9:
            err(f"{bname}: design-point turnover exceeds its cap")
        if hi(b["leverage_avg_target"]) > frozen["gross_leverage_cap"]:
            err(f"{bname}: leverage average target exceeds gross cap")
        if lo(b["name_count_floor"]) > hi(b["name_count_ceiling"]):
            err(f"{bname}: name-count floor exceeds ceiling")
        if hi(b["net_cagr_band"]) > 0.30:
            warn(f"{bname}: CAGR band upper end {hi(b['net_cagr_band'])} looks like a stretch case, not a design target")

    # ---- 4. Risk: bucket monotonicity + worst-case aggregation ----------------------
    rb = risk["regime_buckets"]
    order = ["R1_benign", "R2_watch", "R3_slow_bear", "R4_crisis"]
    for a, b in zip(order, order[1:]):
        if hi(rb[b]["leverage_range"]) > hi(rb[a]["leverage_range"]) + 1e-9:
            err(f"regime leverage not monotone: {b} max > {a} max")
        if hi(rb[b]["hedge_ratio_range"]) < hi(rb[a]["hedge_ratio_range"]) - 1e-9:
            err(f"regime hedge ratio not monotone: {b} max < {a} max")
    for name, bucket in rb.items():
        if hi(bucket["leverage_range"]) > frozen["gross_leverage_cap"]:
            err(f"{name}: leverage range breaches 1.5x gross cap")
        if hi(bucket["hedge_ratio_range"]) > max(frozen["hedge_ratio_grid"]):
            err(f"{name}: hedge range outside frozen grid")
    gf = risk["effective_beta_identity"]["gap_floor"]["value"]
    ceiling = frozen["drawdown_absolute_ceiling"]
    # worst-case check: R4 effective beta * the provenanced worst fast fall + gap floor <= ceiling
    beta = hi(risk["effective_beta_identity"]["downside_beta_tilt"]["value"])
    lev = hi(rb["R4_crisis"]["leverage_range"])
    hedge = lo(rb["R4_crisis"]["hedge_ratio_range"])
    he = lo(risk["effective_beta_identity"]["hedge_effectiveness_fast_crash"]["value"])
    fall = risk["effective_beta_identity"]["worst_case_fall_while_in_R4"]["value"]
    eff_beta_r4 = beta * lev * (1 - hedge * he)
    worst = eff_beta_r4 * fall + hi(gf)
    if worst > hi(ceiling):
        err(f"worst-case R4 arithmetic {worst:.2f} breaches absolute ceiling {hi(ceiling)} "
            f"(effBeta={eff_beta_r4:.2f} x {fall:.0%} fall + gap {hi(gf)})")
    if risk["leverage_function"]["funding_rate"]["value"] is None:
        warn("funding_rate unset - PRINCIPAL INPUT REQUIRED before leverage feature is enabled")
    if not risk["leverage_function"]["rule_no_debt_while_levered"]:
        err("no-debt-while-levered rule disabled (negative-carry violation)")

    # ---- 5. Sleeves: gold caps, factor weights, stage-2 ladder ----------------------
    gold = sleeves["gold"]
    for book, ceil in gold["ceilings_total"].items():
        if hi(ceil) > frozen["gold_weight_cap"]:
            err(f"gold ceiling {book} breaches 50% mandate cap")
        if lo(gold["floors"][book]) > hi(ceil):
            err(f"gold floor > ceiling for {book}")
    w_min = sum(lo(v["weight"]) for v in gold["score_inputs"].values())
    w_max = sum(hi(v["weight"]) for v in gold["score_inputs"].values())
    if not (w_min <= 1.0 <= w_max):
        err(f"gold score weights not normalizable: min {w_min:.2f}, max {w_max:.2f}")
    fb = sleeves["factor_book"]
    f_min = sum(lo(fb[s]["weight_range"]) for s in ("value", "quality", "low_vol", "size_quality_controlled"))
    f_max = sum(hi(fb[s]["weight_range"]) for s in ("value", "quality", "low_vol", "size_quality_controlled"))
    if not (f_min <= 1.0 <= f_max):
        err(f"factor-book weights not normalizable: min {f_min:.2f}, max {f_max:.2f}")
    if fb["size_quality_controlled"]["tier"] == "C" and not fb["size_quality_controlled"].get("satellite_only"):
        err("Tier-C size sleeve must be satellite_only")
    if sleeves["stage2"]["inception_rung"] != -1:
        err("Stage-2 must start at rung -1 (advisory-only) per Decision Q7")
    if sleeves["special_situations"]["sleeve_cap_nav"]["value"] > 0.15:
        err("special-sits sleeve cap unreasonably high vs D12 placeholder")
    if hi(risk["tactical_short_sleeve"]["cap_share_of_short_side"]["value"] if isinstance(
            risk["tactical_short_sleeve"]["cap_share_of_short_side"]["value"], list) else
          risk["tactical_short_sleeve"]["cap_share_of_short_side"]["value"]) > 0.25 + 1e-9:
        err("tactical single-name shorts exceed 25% of short-side sleeve (Decision Q2)")

    # ---- 6. Costs: provisional data cannot claim high tiers -------------------------
    if costs["adv_by_rank_bucket_cr"]["verify_status"] == "PROVISIONAL":
        warn("ADV table PROVISIONAL - every downstream capacity number inherits this; replace in Phase 0")
        for key in ("at_500pct_throttled", "incremental_hurdle_500_vs_100"):
            if costs["turnover_cost_curve"][key]["tier"] == "A":
                err(f"{key} claims Tier A while resting on provisional ADV data")

    # ---- 7. Provenance completeness --------------------------------------------------
    for fname, doc in [("mandate", mandate), ("books", books), ("ladder", ladder),
                       ("risk", risk), ("sleeves", sleeves), ("costs", costs)]:
        check_provenance(doc, fname)
    # bare-numeric sections (lists/scalars without a 'value' wrapper) must carry a section-level
    # provenance stanza - red-team finding: the walker alone missed ~38 load-bearing numbers
    required_section_provenance = [
        (ladder, "budgets", "regime_score_blocks_provenance", "ladder.budgets"),
        (risk, None, "regime_buckets_provenance", "risk"),
        (sleeves["gold"], None, "floors_ceilings_provenance", "sleeves.gold"),
        (books, None, "numeric_fields_provenance", "books"),
    ]
    for doc, sub, key, label in required_section_provenance:
        container = doc[sub] if sub else doc
        stanza = container.get(key)
        if not isinstance(stanza, dict) or PROVENANCE_KEYS - stanza.keys():
            err(f"{label}: missing or incomplete section-level provenance stanza '{key}' "
                f"(must carry {sorted(PROVENANCE_KEYS)})")

    # ---- report ----------------------------------------------------------------------
    for w in WARNINGS:
        print(f"WARN  {w}")
    for e in ERRORS:
        print(f"ERROR {e}")
    print(f"\n{len(ERRORS)} error(s), {len(WARNINGS)} warning(s) across 6 registry files.")
    if ERRORS:
        print("REGISTRY REFUSED TO LOAD.")
        return 1
    print("Registry loads clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
