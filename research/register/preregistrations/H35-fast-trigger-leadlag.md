# H35 — Fast-trigger lead-lag across the full episode set

STATUS: **registered 2026-08-31, NOT RUN** (awaiting Phase-0 fixtures; vintage + commit pinned
here before execution).

## Registered
- **Hypothesis**: the L2 fast triggers (realized-vol top-decile rank, India-VIX term-structure
  inversion, CCIL/NSDL funding-stress rank) LEAD realized crash acceleration by ≥1–2 trading days
  (enough for the de-gross priority list to execute) at a low false-fire rate, across the full
  episode set 2008→2026 — not merely in the single documented Mar-2020 case.
- **Mechanism**: reactive information (vol clustering, funding stress) — no predictive claim.
- **Sample**: India-VIX archive (2008→), bhavcopy realized vol, CCIL spreads, NSDL FPI flows;
  the R2.1 episode table (including May-2026 as the L9/currency test case, which this hypothesis
  does NOT count as an equity episode).
- **Primary metric**: median lead time in trading days; false-fire count per calendar year,
  frequency-counted. NO regression or Markov fitting (<10 transitions — CONTRACT §8).
- **Minimum economic effect**: median lead ≥1 day AND false fires ≤ a rate whose whipsaw cost
  (from the R3.4 cost curves) stays inside the risk-system drag budget of DESIGN §1.1.
- **Stop rule / decision rule**: lead ≈0 or negative in most episodes → widen the honest
  fast-crash floor (`risk.yaml gap_floor`) and say so; high single-trigger false-fire rate →
  registry PR changing R4 arming from "any one trigger" to "two-channel confirmation always".
  One run on the registered spec; results appended below.

## Result
*(pending)*

## Registry action
*(pending)*
