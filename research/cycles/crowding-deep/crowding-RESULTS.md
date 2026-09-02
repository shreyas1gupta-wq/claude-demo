# Atlas 3.3/3.4 — crowding: crash asymmetry on India factors (CR1-CR2, pre-registered)

| Factor | monthly skew | worst month (own σ) | worst month (date, %) |
|---|---|---|---|
| WML | +0.05 | -4.1σ | 2001-11 (-27.6%) |
| SMB | +0.04 | -2.9σ | 2020-03 (-14.1%) |
| HML | +0.60 | -3.4σ | 2000-01 (-19.0%) |

- CR1a (skew(WML) ≤ −0.5 AND most negative): **FAIL**.
- CR1b (WML worst ≤ −4σ AND most extreme): **PASS**.

## CR2 — 2025 WML months at ≤ −2σ (the named mid-2025 unwind, measurement)

- NO 2025 month reaches −2σ in India's WML.

- 2025 monthly WML z-scores: [-1.1, -0.0, -0.1, -0.6, -1.0, 0.0, 0.1, -0.1, -0.5, 0.1, 0.5, 0.0]

## Honest read (written AFTER the print)

- **CR1a FAILS, and it's the BC2 lesson again — an imported stylized fact dying on transfer.**
  The US literature's "momentum is negatively skewed" does NOT hold unconditionally on India's
  33-year factor library (WML skew +0.05, indistinguishable from SMB's +0.04; HML is the
  POSITIVELY skewed one at +0.60). Consistency check against monograph 03: no contradiction —
  its crash finding was CONDITIONAL (bear-market-then-rally windows), and a conditional crash
  tail can coexist with ~zero unconditional skew when normal-times momentum is right-skewed.
  The refined sentence: India's momentum danger is REGIME-LOCAL, not a standing distributional
  feature — which is precisely what the seated crash_guard (conditional, not permanent)
  already implements. Design vindicated by the fail.
- **CR1b PASSES: crash CONCENTRATION is real.** WML's worst month sits at −4.1σ of its own
  distribution, more extreme than SMB's (−2.9σ) and HML's (−3.4σ) — the synchronized-exit
  signature shows in the tail's depth even where it doesn't show in the third moment.
- **CR2: the named mid-2025 quant unwind left NO trace in India's monthly WML** (no 2025
  month at −2σ). Two readings, both recorded: the episode was US/global-implementation-
  specific, and/or unwind episodes live at daily/intramonth granularity invisible to monthly
  academic factors. Either way the consequence for the 3.4 candidate is structural: MONTHLY
  FACTOR RETURNS CANNOT BE THE MONITOR — the AUM-growth and comomentum legs (runsheet) are
  necessary, not decorative, and the candidate's design says so from its first day.
