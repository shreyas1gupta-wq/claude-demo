# H02 — Post-2015 PIT momentum premium vs the AJV 1994–2014 benchmark

STATUS: **registered 2026-08-31, NOT RUN** (awaiting Phase-0 fixtures; fixture vintage and code
commit to be pinned here before execution).

## Registered
- **Hypothesis** (directional, falsifiable): the post-2015 point-in-time momentum premium
  (rank-blend 12-1 + 6-1 + 52wk-high, skip-month, NSE-hygiene exclusions) is materially below the
  1994–2014 Agarwalla-Jacob-Varma WML benchmark of 21.9%/yr — "materially" = sub-sample point
  estimate < ~2/3 of AJV's, with non-overlapping block-bootstrap CIs.
- **Mechanism at stake**: (i) behavioural diffusion; this is the design's own stated falsifier
  for the 25–35% haircut (DESIGN §10 momentum row).
- **Sample**: bhavcopy PIT price panel, full universe with hygiene exclusions, split at 2015-01;
  monthly rebalanced decile spread.
- **Primary metric**: sub-sample mean long-short spread (net of rank-bucket costs) vs full-sample.
- **Minimum economic effect**: the fast sleeve must clear the 3.0–6.0pp/yr incremental hurdle at
  design-point turnover after the resulting haircut (D05 §4h) — if the post-2015 premium implies
  it cannot, the haircut escalates regardless of statistical significance.
- **Procedure**: Chow-type break test + block bootstrap CIs (mean block 2–4×τ½); purged 4–6-fold
  CV for the net-IR restatement; Stambaugh correction on persistent sizing inputs; trial-ledger
  entry #10 covers the construct family — no variant beyond the registered blend is tested.
- **Stop rule**: one run on the registered spec. Confirmed weak → `sleeves.yaml momentum.haircut`
  escalates toward 0.58 (registry PR). Not weak → haircut stays 0.25–0.35. Either way, no re-cut.
- **Decision rule**: pre-registered thresholds above; result appended below after the run.

## Result
*(pending)*

## Registry action
*(pending)*
