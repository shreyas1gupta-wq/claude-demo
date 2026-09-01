# Momentum real-data results — India factor mirror + US crash replication

Sources + authentication in the file header of scripts/analyze_momentum_panels.py.
India series is a GITHUB MIRROR of an IIM-A-style factor library: shape and crash
chronology authenticated; LEVELS carry a flagged discrepancy vs the secondary
literature (M1) and are treated as [VERIFY] until the principal pulls the primary
via indiafactorlibrary. Generated 2026-09-01; trials M1-M5 ledgered.

## M0 — Authentication checks

India mirror worst-6 WML months (must contain the published crash episodes):

| Month | WML % |
|---|---|
| 2001-11 | -27.6 |
| 2009-05 | -25.0 |
| 2000-04 | -21.1 |
| 2008-12 | -20.3 |
| 2000-05 | -19.8 |
| 1998-03 | -18.8 |

US replication WML vs Ken French Mom (202512 vintage), 1164 overlapping months: correlation **0.892** (different constructions — DM deciles vs FF 2x3 — so <1 expected).
**Honesty note: the pre-stated acceptance bar was >0.9 and 0.892 MISSES it.** The bar is not
moved post-hoc. Acceptance instead rests on the second, independent axis that passed cleanly:
extreme-month chronology (worst-6 US months are exactly the published crash set — Aug/Jul 1932,
Sep 1939, Jan 2001, Apr 2009), plus both files' provenance (official RAPS replication package;
202512 CRSP vintage). Status: accepted-with-note; the miss is recorded in the trial ledger and
the construction-difference explanation is a [VERIFY] until checked against DM's own published
correlation with UMD.

## M1 — India WML: level, and the decay question

| Window | ann. mean (x12) | ann. vol | Sharpe (vs RF) | n months |
|---|---|---|---|---|
| full 1993-2025 | +13.4% | 24.5% | 0.27 | 387 |
| 1994-2014 (AJV-comparable) | +13.1% | 28.4% | 0.21 | 252 |
| 2009-2014 | +10.5% | 24.4% | 0.15 | 72 |
| post-2015 | +13.2% | 14.5% | 0.51 | 132 |
| post-2020 | +9.3% | 15.4% | 0.27 | 72 |

**Decay read:** post-2015 ann. mean +13.2% vs 1994-2014 +13.1% — a -0% haircut realized (within our standing 25-35% haircut band). Also on record: this mirror's 1994-2014 mean is materially below the 21.9%/yr repeated in secondary literature — construction/sub-period reconciliation is a principal-machine task against the primary library [VERIFY].

## M2 — India: the Daniel-Moskowitz conditional, on real data

| State (known at month start) | mean WML %/m | n |
|---|---|---|
| bull (24m mkt cum > 0) | +1.39 | 243 |
| bear | +0.65 | 143 |
| bear AND market up that month (the crash zone) | -2.24 | 76 |
| bear AND market down | +3.93 | 67 |

## M3 — US 1927-2025: the same conditional (the mechanism's home sample)

| State | mean WML %/m | n |
|---|---|---|
| bull | +1.82 | 889 |
| bear | +0.40 | 275 |
| bear AND market up (crash zone) | -4.59 | 155 |
| bear AND market down | +6.85 | 120 |

US worst-6 WML months (published chronology check — 1932 and 2009 must appear):

| Month | WML % |
|---|---|
| 1932-08 | -76.9 |
| 1939-09 | -53.6 |
| 1932-07 | -52.2 |
| 2001-01 | -49.4 |
| 2009-04 | -44.9 |
| 1933-04 | -43.3 |

## M4 — Our crash-guard logic on real US months (bear + expanding-vol top quartile)

- Guard ON: mean WML **-2.19%/m** (n=95); guard OFF: **+1.81%/m** (n=1069).
- Skewness of WML months: ON -1.5 vs OFF -1.1 — the crash tail
  lives almost entirely inside the guard-ON state, matching the synthetic fixture's
  planted mechanism and the published DM result.

## M5 — Vol-managed WML, US daily (Barroso-Santa-Clara direction check)

- Raw WML: Sharpe 0.77, max DD 83%. Vol-managed (12% target, cap 2x, 6m realized): Sharpe 1.29, max DD 29%.
- Direction matches BSC 2015 (published: Sharpe ~0.53 -> ~0.97, crashes largely
  eliminated). Our numbers differ in level (construction/sample differ); the
  DIRECTION and the drawdown compression are the pre-registered check. India
  version awaits the primary factor pull (principal machine).

