# Parts D–H — calendar mechanics (atlas 4.3/4.4/4.5 = H58 ops pack; 4.6 = RC1 edge + exclusion)

## Part D — Econometrics of an entry with no trials, on purpose

This entry runs ZERO trials and that is its design, stated before any data lands: every claim
here is about MECHANICS — flows forced by statute, settlement, or index rules — and mechanics
are graded by frequency counts, not hypothesis tests. The four registered designs (trial
ledger, 2026-09-02) are counting exercises with their acceptance shapes fixed now:

- **H58-D1** is the only one with a bar, because it must EARN a suppression rule: quarantining
  L2 funding fires inside drain windows is justified only if drain-window fires are ≥2x the
  base rate (the calendar actually attracts fires) AND ≥80% of them mean-revert within 5
  business days (they are mechanical, not stress). The formal point: a stress classifier's
  precision is degraded by scheduled spikes exactly in proportion to their rate ratio — but a
  suppression rule that fires during a REAL crisis that happens to straddle Sep 15 is the
  catastrophic failure mode, which is why the rule QUARANTINES (flags for confirmation by the
  other two L2 legs) and never vetoes alone. The two-of-three confirmation architecture in
  L2's role already provides the override path; the ladder.yaml role text now carries it.
- **H58-D2/D3** are frequency reports with no bar: prudence rules whose cost (a tranche
  deferred a day or two) is bounded and whose benefit (a gap or a pinned close not bought)
  needs measuring, not proving.
- **RC1** is the entry's only alpha-adjacent object and it points AWAY from the ladder: the
  reconstitution pop is a special-sits sleeve question (Tier B, capped, aggressive book only,
  per CONTRACT §10) plus a HYGIENE rule for everyone else — an add's pre-effective pop is a
  one-time demand-curve level shift (Shleifer lineage) and must be excluded from L3/L4
  momentum lookbacks, or the trend legs buy a flow artifact. The exclusion needs no trial:
  it follows from what the pop IS; RC1 measures its size for the sleeve, not its existence.

## Part E — The algorithm (quant/ladder/exclusion_calendar.py, seated as ops)

Three deterministic calendars, seven exact tests, suite 87 green:
`statutory_drain_dates(year)` — the sixteen statutory dates (four s.211 advance-tax
instalments + twelve GSTR-3B due-20ths); `drain_window_mask(dates, pre_bd=2, post_bd=1)` —
business-day windows around them (numpy busday; exchange holiday lists a supplied
refinement); `results_pause_mask(tranches, results_dates)` — flags staged-entry tranche
dates crossing a SUPPLIED results calendar (never scraped); `expiry_days(dates, weekday)` —
last-weekday-of-month arithmetic where the weekday is a REQUIRED argument with no default:
the 2024-25 SEBI curbs and exchange weekday reshuffles make any hardcoded expiry day a
latent bug, so config owns it per (exchange, era) and a test enforces that a bare call
raises. The namespace contains no signal/alpha/tilt surface and `test_no_alpha_surface`
asserts it stays that way — the pack excludes and defers; it never recommends.

Consumption: L2's funding leg (quarantine, two-of-three override); the staged-entry
executor (defer past results windows); the rebalance scheduler (skip expiry days). All three
are execution-layer; none touches a budget block.

## Part F — Harvest map

Harvested now: the H58 ops rules (above) wired into L2's role text with provenance; the
momentum-hygiene exclusion stated as a rule for the L3/L4 build (reconstitution pops out of
lookbacks — implementation lands with the equity cross-section, where the add/drop lists
live). Registered, data-gated: H58-D1/D2/D3 counting designs; RC1 event study for the
special-sits sleeve. Nothing else — this entry's honest yield is plumbing-awareness, and the
budget it touches is zero.

## Part H — Knowledge ledger

**Established (mechanics, not measured by us):** the drain calendar itself (statute); expiry
and reconstitution dates (exchange/index rules) — these are facts of the plumbing, not
hypotheses. **Pooled-prior (literature, Tier B):** scheduled liquidity drains spike funding
rates (RBI's own liquidity commentary; the US Sep-2019 repo episode as the canonical
extreme); index-inclusion demand effects large in the 1990s-2000s US and DECAYING
post-2010 (Patel-Welch lineage) — the decay prior applies to India's version before RC1
prints. **Awaits India data:** all four designs. **Unknowable:** whether the next real
funding crisis straddles a drain date — which is exactly why the quarantine flags and the
two-of-three architecture decides, never the calendar alone.

Verdicts: 4.3/4.4/4.5 EXECUTION rules seated (ops pack, no alpha claim, tests enforce the
framing). 4.6 split: special-sits EDGE design registered (RC1, sleeve-side) + momentum
exclusion adopted as hygiene. No seat, no budget, no new ladder row — the entry's product
is that the fast layer stops lying to itself on sixteen known dates a year.
