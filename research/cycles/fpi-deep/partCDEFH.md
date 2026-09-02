# Parts C–H — data engineering, math, algorithm, harvest, ledger (atlas 2.13; seat L14)

## Part C — Data engineering (compact, in-house)

| Leg | Source | Cadence / lag | Notes |
|---|---|---|---|
| FPI flows (equity/debt) | NSDL FPI monitor (ingest/pull_nsdl_fpi.py EXISTS, untested live) | daily / T+1 | the 2014 FII→FPI regime change is a breaks-registry entry; category recuts never spliced silently |
| Stock-level foreign ownership | quarterly shareholding patterns (NSE/BSE filings) | quarterly / ~3-6w | THE seat's series after float-scaling; heavy engineering (entity mapping, float calc) |
| Free float | index provider factsheets + filings | quarterly | the denominator; promoter+locked shares excluded — the float rule pinned in the registry |
| FPI derivatives positioning | NSE daily participant-wise OI | daily / T+1 | the FAST SHADOW — a different object (leveraged, expiring); briefing only, never the seat's state |
| DII flows (the counterweight) | AMFI/SEBI + exchange dailies | daily-monthly | context for the unwind arithmetic; not a leg |

PIT hazards: shareholding-pattern refiling revisions; float redefinitions (SEBI 2021 norms);
the FII→FPI recut; survivorship in stock-level panels (delistings kept).
Runsheet addendum 12 (steps 65-69): 65 NSDL first live pull + 2014 break rules (~2-3h, shared
with addendum 10 step 58 — dedup noted); 66 shareholding-pattern scraper pilot (NSE500,
8 quarters back) ~6-8h; 67 float table assembly + the float rule registration ~3-4h; 68 FL1
run + acceptance fill (two-pass) ~2h; 69 FL2 run after ≥20y of ownership ranks assembled from
archives ~3-4h. Total ~16-21h.

## Part D — The mathematics

The seat computes ONE series: pct_t = ExpandingPercentile(ownership_t / float_t), and ONE
signal: extreme_t = 1[pct_t ≥ 0.9] (grid-registered threshold), consumed reduce-only in the
tierC overlay. The exclusion is structural: the module exposes no flow-named API (tested) —
a §7 REJECT enforced in the interface, not just the register. The capacity mechanism's
asymmetry justifies risk-off-only: a crowded theater has an exit problem; an empty one does
not (a LOW extreme is information about ownership, not about forced selling). The fixture
plants the causal direction at +0.97 (flows chase lagged returns) with lead-corr ~0 — the
machinery demonstrably cannot mistake the planted direction. Evidence tier C; FL1/FL2 are the
data-gated tests, bars shaped at registration, filled at the data (two-pass).

## Part E — The algorithm (L14, quarterly with daily confirms)

```
STEP 1  quarterly: stock-level foreign ownership / float -> aggregate + sector percentiles
        (expanding, min_obs per the shared grids)
STEP 2  extreme flag at the registered threshold -> tierC overlay consumption (reduce-only,
        risk-off only); sector-level extremes flag concentration (financials-heavy caution)
STEP 3  daily NSDL flows + derivatives OI feed the BRIEFING shadow only — labeled as such;
        no state, no score path
STEP 4  the DII-counterweight annotation travels with every extreme flag (the unwind
        arithmetic changed post-2014 — the flag's consequence sizing notes it)
MONITOR quarterly refiling revisions; float-rule drift; FL1/FL2 at data-landing; the
        structural-change question (does DII depth blunt the capacity mechanism?) re-read
        against each new unwind episode
FAILURE MODES: float mis-measurement (the denominator IS the seat); shareholding lag making
        extremes stale at quarter-ends (the daily shadow flags divergence); flow-momentum
        re-entering through the briefing (countermeasure: the structural API exclusion +
        the §7 print)
```

## Part F — Harvest + designs

| Consumer | What it gets |
|---|---|
| tierC overlay | the extreme flag (reduce-only, risk-off only) |
| Hedge scheduling | extreme-and-aging positioning joins the watch context |
| Stage-2 briefings | the flow/derivatives shadow, labeled non-signal |
| Cycle School | Lesson 26: the seat defined by what it refuses |

Designs: **FL1** (registered) the flows-follow-returns quantification; **FL2** (registered)
the extreme→drawdown conditioning; **FL-D3** the DII-counterweight test: unwind-episode
depth vs DII absorption share (design only; needs both sides' flow vaults).

## Part H — Knowledge ledger (atlas 2.13)

**Established (fixture-verified machinery + record):** the module cannot express flow
momentum (structural exclusion, tested); the planted causal direction is recovered at +0.97.
**Established (record, cases chapter):** five positioning eras with returns leading flows in
both directions; the FY22 exodus absorbed by DIIs as the structural-change exhibit.
**Awaits India data [C]:** FL1/FL2 — the seat's own numbers; ~20y of quarterly ownership
ranks needed for honest extremes. **Unknowable:** whether DII depth permanently blunts the
capacity mechanism — each unwind episode is one more observation, arriving on the market's
schedule. **Process:** a red test briefly reached the branch when a piped exit code was
masked; caught next run, fixed forward, gate discipline corrected (PIPESTATUS) — logged here
because process notes belong in the ledger, not just the fix commit.
