# Parts C–H — data engineering, math, algorithm, harvest, ledger (atlas 2.8; seat L9)

## Part C — Data engineering (compact, in-house; the triad's free-access reality)

| Leg | Primary (blocked here) | Free path for the desk | Cadence/lag |
|---|---|---|---|
| VIX / risk appetite | CBOE via FRED | India VIX (NSE archive — already in the L2 pull family); CBOE publishes VIX history on cboe.com [VERIFY access from principal's machine]; datahub mirror hunt at pull time | daily |
| Broad dollar | FRED DTWEXBGS | FRED blocked → principal's machine (ingest/pull_fred.py EXISTS); fallback: DXY from free mirrors (stooq) with a declared index-substitution note (DXY ≠ broad — bias stated) | daily |
| US real yields | FRED DFII10 | principal's machine via pull_fred.py; fallback: nominal 10y minus survey CPI (constructed, flagged) | daily |
| FPI flows | NSDL | ingest/pull_nsdl_fpi.py EXISTS (untested live) | daily/weekly |
| INR | RBI/FBIL reference rate | mp-cycle partC C.2's pull family — cross-ref, no duplication | daily |
| Kilian activity index | Kilian's site | updated index publicly posted [VERIFY current host]; annual re-pull | monthly |

PIT hazards: VIX methodology 2003 revision (backfilled series — vintage note); broad-dollar
index reweights (FRED publishes revisions — vintage per pull); NSDL categry reclassifications
(FPI/FII regime change 2014 — breaks registry); the DXY-vs-broad substitution bias whenever
the fallback is active (flag travels with every derived state).
Runsheet addendum 10 (steps 57-60): 57 FRED triad via pull_fred.py + vintages (~2h);
58 NSDL FPI first live run + 2014 break rules (~2-3h); 59 India-VIX archive backfill (~2h);
60 L9 state assembly + GF re-run wiring (~3-4h). Total ~9-11h.

## Part D — The mathematics

L9's state: expanding percentiles of the triad legs (dollar level+impulse, VIX level, US real
yield impulse) combined per the registered block rules; episode τ½ 3-9m makes this the ladder's
FASTEST macro seat — the state is an EPISODE detector, not an era classifier (contrast L6). The
measured base: GF1's regime change (+0.28→+0.77) grounds the pooled-Tier-A grade and creates
the STANDING CAVEAT that pre-1990 analogue evidence discounts on transfer (now cited wherever
old panels feed India claims). GF2 (+0.57) is the transfer coefficient's first in-house
estimate — the ladder's changes_if ("India factor-loading estimate") is now partially served;
the monthly-frequency loading with proper controls remains design GF-D1. GF3's fail bounds the
claim: median 69% breadth means partial insulation EXISTS ex post; the seat's job is refusing
to assume it ex ante (the decoupling trap, Part G of the theory chapter).

## Part E — The algorithm (L9, daily/weekly)

```
STEP 1  triad legs -> expanding percentiles (shared grids); Kilian-decomposed oil enters as
        the demand/supply-split conditioner (never raw price; commodity monograph D3)
STEP 2  episode state: dollar-up + VIX-up + real-yield-up co-movement percentile (the Rey
        signature); n_legs degradation when a leg's feed is stale (DXY fallback flagged)
STEP 3  consumption: global_cycle block (0.20) conditions India book size; hedge scheduling
        reads episode ARMED; sector projection reads the oil decomposition
STEP 4  FPI flows enter as CONFIRM only (flows follow returns — atlas 2.13's finding);
        never as a leading leg
MONITOR annual GF1-GF3 re-run; the May-2026 INR episode file (cases chapter) re-graded when
        NSDL/INR data is vaulted — the seat's named live test case
FAILURE MODES: fallback-index bias (flagged state); swap-line/backstop regime changes
        (2020's Fed backstop compressed episode length — regime note); decoupling narratives
        entering through the briefing layer (countermeasure: GF3's number is the ONLY
        licensed insulation sentence)
```

## Part F — Harvest map + designs

| Consumer | What it gets |
|---|---|
| global_cycle block (0.20) | the episode state (triad percentiles) |
| Hedge scheduling | episode-armed flag (τ½ 3-9m — the fastest macro input) |
| L9 oil conditioner | Kilian split (commodity monograph cross-ref) |
| Registry | the pre-1990-discount standing caveat (GF1); the licensed insulation sentence (GF3) |
| Cycle School | Lesson 22: the cycle that globalized; passes, and an honest miss |

Designs: **GF-D1** monthly India loading with world-factor + oil + INR controls (needs the
FRED triad vaulted; acceptance registered at pull). **GF-D2** episode catalog validation: L9's
armed dates vs the cases chapter's nine episodes (event-matched, registered before the look).
**GF-D3** the May-2026 test case re-grade on real data (the atlas's own live exam).

## Part H — Knowledge ledger (atlas 2.8)

**Established (our runs):** the global cycle's RISE (+0.28→+0.77 pairwise, GF1 — the register's
cleanest regime change); India inside it at +0.57 (GF2); breadth bounded at ~69% median (GF3
fail — insulation exists ex post, never assumable ex ante). **Established (record):** nine
episodes 1994-2026 with India's transfer growing as the capital account opened (cases chapter).
**Unknowable:** the next episode's trigger and the Fed's reaction function; the seat detects
episodes, refuses forecasts. **Process:** GF3's fail refined the seat's language rather than
its structure — bars that fail productively are the register working as designed.
