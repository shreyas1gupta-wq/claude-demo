"""The Stage-1 regime-score assembler — the spine that turns ladder states into R.

DESIGN §4 / risk.yaml: seat states (each in [-1, +1], HIGHER = more stress = less risk
permission) are averaged within their block, blocks are combined by the registry's
block budgets, and the score is availability-weighted — a missing seat or an empty block
never silently reads as calm; it shrinks the denominator and is named in the trail.

Rules enforced structurally (each carries a test):
- TIER-C SEATS NEVER ENTER THE SCORE. They act only through the negative-only overlay:
  overlay = min(tierC_overlay_cap, cap * max over available Tier-C states clamped to >= 0),
  added ON TOP of R (pushing toward risk-off). A calm Tier-C seat contributes nothing;
  a stressed one can only reduce permission (CONTRACT §4).
- REDUCE-ONLY Tier-A/B seats are clamped to max(state, 0) — they may push R up (toward
  risk-off), never pull it down (L5's scheduling, L13's household-debt lens).
- The result is a phase-style object with its trail: per-block states, per-block seat
  availability, the available budget, and n_blocks — states carry their trail (principal
  directive 2026-09-01).
- Bucket boundaries are QUANTILE RULES on R's own expanding history (risk.yaml
  bucket_boundaries: no fixed numeric thresholds): `bucket_path` percentile-ranks the score
  series with the house expanding_percentile and cuts at a pre-registered grid.

Consumption: the R1..R4 bucket drives leverage/hedge ranges (risk.yaml regime_buckets);
this module computes and explains — it never maps to positions (Stage 3's job).
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from quant.ladder import expanding_percentile


@dataclass
class RegimeResult:
    score: float                      # R in [-1, +1] (+ overlay may push above the mean)
    bucket_inputs_pctile: float | None  # filled by bucket_path, None for a single assembly
    available_budget: float           # sum of budgets of blocks with >= 1 available seat
    n_blocks: int                     # blocks that contributed
    overlay: float                    # the Tier-C negative-only shift actually applied
    block_states: dict = field(default_factory=dict)   # block -> availability-weighted state
    block_avail: dict = field(default_factory=dict)    # block -> [seat ids that reported]
    missing: list = field(default_factory=list)        # seats passed as NaN / absent


def assemble_regime(states: dict, ladder: dict) -> RegimeResult:
    """Combine seat states into the regime score R with its trail.

    states: {seat_id: float in [-1, +1] or NaN}; seats not passed are treated as NaN.
    ladder: the registry's ladder document (load_registry()['ladder'])."""
    budgets = ladder["budgets"]["regime_score_blocks"]
    cap = float(ladder["budgets"]["tierC_overlay_cap"])
    entries = {e["id"]: e for e in ladder["entries"]}

    block_num: dict = {b: 0.0 for b in budgets}
    block_cnt: dict = {b: 0 for b in budgets}
    block_avail: dict = {b: [] for b in budgets}
    missing: list = []
    tierC_states: list = []

    for sid, e in entries.items():
        v = states.get(sid, np.nan)
        v = float(v) if v is not None else np.nan
        if np.isnan(v):
            missing.append(sid)
            continue
        if not -1.0 <= v <= 1.0:
            raise ValueError(f"{sid}: state {v} outside [-1, 1]")
        if e["tier"] == "C":
            tierC_states.append(max(v, 0.0))   # calm Tier-C is silent; stress accumulates
            continue
        if e["block"] not in budgets:
            continue                           # non-scored block (defensive)
        if e.get("reduce_only"):
            v = max(v, 0.0)                    # may add stress, never subtract it
        block_num[e["block"]] += v
        block_cnt[e["block"]] += 1
        block_avail[e["block"]].append(sid)

    block_states = {b: block_num[b] / block_cnt[b] for b in budgets if block_cnt[b] > 0}
    avail_budget = sum(budgets[b] for b in block_states)
    if avail_budget == 0:
        return RegimeResult(score=float("nan"), bucket_inputs_pctile=None,
                            available_budget=0.0, n_blocks=0, overlay=0.0,
                            block_states={}, block_avail=block_avail, missing=missing)
    score = sum(budgets[b] * s for b, s in block_states.items()) / avail_budget
    overlay = min(cap, cap * max(tierC_states)) if tierC_states else 0.0
    return RegimeResult(score=score + overlay, bucket_inputs_pctile=None,
                        available_budget=avail_budget, n_blocks=len(block_states),
                        overlay=overlay, block_states=block_states,
                        block_avail={b: v for b, v in block_avail.items() if v},
                        missing=missing)


def bucket_path(scores: np.ndarray, grid=(0.5, 0.8, 0.95), min_obs: int = 252) -> np.ndarray:
    """Map a score SERIES to buckets 1..4 by quantile rules on its own expanding history.

    grid: pre-registered percentile cuts (R1 below grid[0]; R4 at/above grid[2]).
    Warm-up (< min_obs) returns 0 = no bucket, never a default-calm 1."""
    p = expanding_percentile(np.asarray(scores, float), min_obs=min_obs)
    out = np.zeros(len(p), dtype=int)
    ok = ~np.isnan(p)
    out[ok] = 1
    for k, g in enumerate(grid, start=2):
        out[ok & (p >= g)] = k
    return out
