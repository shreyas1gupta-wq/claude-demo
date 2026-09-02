# Parts D–H — calendar-as-signal (atlas 4.1 seat / 4.2 instrumented / 4.11 + 4.12 rejects)

## Part D — Econometrics: what the desk legs establish and refuse

Three trials, one pre-registration block, bars rank-based (no magic thresholds), all run
2026-09-02 on the IIMA monthly factor library (MF/SMB, 1993-10..2025-12, ~32 obs per
calendar month). Full prints: research/cycles/calendar/calendar-RESULTS.md.

**CW1 (Budget-month vol) FAIL.** February's median |MF| ranks 7 of 12 (4.27 vs 4.22
non-Feb; MW one-sided p=0.522). The pre-stated resolution caveat did the work: a 1–3 day
scheduled-reveal vol spike is diluted ~20× inside a month of ordinary variance. This is the
second time the register has measured the monthly-resolution wall (CR2 was the first), and
it now has a name in the ledger: *the resolution theorem* — an event-day phenomenon must be
tested at event-day resolution, and a monthly print can neither confirm nor kill it. The L5
budget window therefore rests on (i) the mechanism — a legally fixed reveal date with
direction unknowable, and (ii) the published daily-resolution India VIX event record, cited
in Part B — never on our monthly print. Our own daily-resolution test is data-gated (CW-D1).

**CW2 (April small-cap) PASS — and refused promotion.** April median SMB +2.47, rank 1/12,
MW one-sided p=0.020, with the month named before the print by a mechanism (FY ends Mar 31;
tax-motivated small-cap selling reverses). One test, not twelve — the family-wise trap CW3
demonstrates does not apply to a single pre-named month. What the pass buys: instrumentation
(a Tier-C flag) and a paper trade (CW-PT1) — NOT budget, because the atlas prior stands
un-refuted: the effect is a small-cap long expressed in the costliest corner of the book
(impact + 20bp STT round trip), the SMB factor is an academic long-short that no real
portfolio holds frictionlessly, and one monthly point per year means n=32 — Tier B by count,
Tier C by harvestability. The pass→refuse quadrant gets its cleanest member.

**CW3 (omnibus) null, as declared.** Kruskal-Wallis p=0.354 across 12 months of MF. The
demonstration worked in both directions: no calendar structure survives an omnibus test,
AND the two seductive rank-1 months the sweep surfaced (Nov in |MF|, Dec in median MF)
are exactly the post-hoc candidates the interpretation rule pre-committed us to ignore.

**Post-hoc observations, tagged and quarantined:** Feb (−2.36) and Mar (−1.70) are the two
most negative SMB medians — the selling leg of CW2's mechanism. Coherent, unregistered,
therefore CW2b in Part F: a future pre-registered trial, not a claim.

## Part E — The algorithm (quant/ladder/calendar_windows.py, seated)

The one module in the ladder that is a SCHEDULE, not a state. `windows()` builds explicit
Window objects — (start, end, kind, anchor) — so every flagged month carries its trail;
`calendar_schedule()` returns (in_window, n_windows, kinds) with overlap DEPTH (a February
inside an election window counts 2). Budget windows are February by construction (era-robust
at monthly resolution: last-day-of-Feb pre-2017 and Feb-1 post-2017 are the same month;
election-year July full budgets documented as a limitation, not silently flagged). Election
windows span [anchor−2, anchor+1] around supplied result months — an event list, never an
extrapolated clock: nothing is generated beyond announced calendars, and events outside the
sample are ignored. There is no directional output in the module's namespace, and a test
asserts that (`test_no_directional_output_exists`) — reduce-only is enforced structurally,
not by convention. Seven exact planted-truth tests (deterministic module, no stochastic
fixture needed); suite 80 green.

Consumption: L5 emits the mask to the risk system — leverage/vol scheduling only
(ladder.yaml `reduce_only: true`). The mandate-clarity re-lever rule (re-gross after a
decisive result) remains pre-registered-only until an election passes with the rule on
paper (HL-7's routing).

## Part F — Harvest map + pre-registered designs

Harvested now: the L5 seat machinery (above); the resolution theorem as register doctrine;
the CW2 Tier-C flag (April small-cap month, flag-only).

Designs registered, data-gated:
- **CW-D1 (daily budget-window vol):** India VIX daily (NSE, 2009-) around budget days;
  bar at registration: budget-day ±1 realized |NIFTY return| and VIX change vs matched
  non-event days, one-sided p<0.05 across the 2009-2026 set (n≈18 budgets + interims).
  Pre-2001 5pm-presentation era excluded by design (event-day definition break).
- **CW-PT1 (April paper trade):** each April, a modeled small-cap tilt (cost model from
  config/costs.yaml, aggressive book's impact schedule) held Apr-1..Apr-30, ledgered like
  HL-7; promotion discussable only after 3 Aprils AND net-of-modeled-cost positive in ≥2.
- **CW2b (the selling leg):** pre-registered now for the NEXT library refresh: Feb+Mar
  pooled median SMB < 0 with MW one-sided p<0.10 vs Apr-Jan. (Stated before any new data.)

## Part H — Knowledge ledger

**Established (our prints):** April small-cap seasonality at monthly resolution (CW2,
p=0.020, rank 1/12); no omnibus month-of-year structure in Indian market returns (CW3);
Budget-month vol invisible monthly (CW1) — the resolution theorem's second data point.
**Pooled-prior (literature, Tier B):** scheduled-announcement vol premia (Savor-Wilson
lineage); tax-loss-selling as the January-effect mechanism (Ritter/Roll/Poterba-Weisbenner),
mapped to India's April; the January effect's own post-publication decay (McLean-Pontiff) —
the standing warning on CW2's future.
**Awaits India data:** CW-D1 (daily VIX event study); CW-PT1 (paper Aprils); CW2b.
**Unknowable:** whether CW2 survives its own publication era — the effect is 30+ years old
in the US literature and decayed there; India's version gets the decay haircut BEFORE any
sizing conversation, per Contract §5.

Verdicts: 4.1 SEATED (scheduling only, mechanism + daily-resolution literature; our monthly
print abstains). 4.2 INSTRUMENTED (pass→refuse promotion; flag + paper trade). 4.11 REJECT
(omnibus-confirmed). 4.12 REJECT (priced mechanics, Elton-Gruber; no trial spent).
