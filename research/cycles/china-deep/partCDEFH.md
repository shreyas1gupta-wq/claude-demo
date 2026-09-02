# Parts C–H — data engineering, math, algorithm, harvest, ledger (atlas 2.11; candidate H54)

## Part C — Data engineering (compact, in-house)

The real object needs TSF (AFRE) monthly + nominal GDP quarterly from PBoC/NBS — both hosts
untested from the desk's proxy [VERIFY at pull]; no GitHub mirror found (commodity partC C.6's
finding stands). Runsheet addendum 11 (steps 61-64): 61 PBoC TSF monthly backfill (2002→) +
component table with the migration-breaks registry (shadow suppression 2017-18, LGFV swaps,
the 2019 aggregate redefinitions) ~4-6h; 62 NBS quarterly nominal GDP + the impulse assembly
(Δ12m of 12m-flow/GDP — the Bloomberg-lineage construction, parameters registered) ~2-3h;
63 China customs iron-ore/copper import volumes (monthly, free) as the DEMAND cross-check
~2-3h; 64 H54's acceptance registration (incremental loading inside L9, pooled, purged)
BEFORE any look ~2h. Meanwhile the desk computes TODAY: the metals-vs-ags relative state
(CI1's construction) from the existing vault — monthly to 2017-06 on the IMF mirror, extended
at the edge by Brent-adjusted metals proxies only if a newer mirror vintage lands (WORM).
PIT hazards: TSF component redefinitions (never spliced silently); NBS GDP revisions; the
proxy's own confound list travels with every derived state.

## Part D — The mathematics

The impulse is a SECOND-derivative object: I_t = Δ(F_t/Y_t) where F is the 12m flow of new
credit — deliberately faster machinery than L10's stock-gap (pulses, not supercycles). The
proxy: rel_t = mean log(metals) − mean log(ags), consumed as expanding percentile + impulse.
CI1a (2.19x variance shift) and CI1b (2/2 signs, confounds named) ground candidacy; the
identification gap is stated as algebra: rel responds to {China demand, global IP, dollar,
energy costs, metals supply} — the proxy cannot invert one term. H54's real test (registered
at runsheet step 64): does the TSF impulse add incremental loading inside L9's factor, pooled,
purged? Until then the proxy enriches, capped at Tier C, reduce-only per the lane rules.

## Part E — The algorithm (candidate mode)

```
STEP 1  rel state monthly (IMF vintage) -> expanding percentile + impulse (shared grids)
STEP 2  consumption: L9 enrichment CANDIDATE input under tierC caps (reduce-only); briefing
        line in Stage-2 ("China-pulse shadow: <state>, confounds unresolved")
STEP 3  when TSF lands: the real impulse replaces the proxy as the CANDIDATE; the proxy
        remains as a cross-check leg (two independent shadows beat one)
STEP 4  validation calendar: the cases chapter's pulse table = the event dates H54's test
        is graded against
MONITOR annual CI re-run; the cadence question (property-era end weakening the metals
        transmission — the cases chapter's honest read) re-asked with each vintage
FAILURE MODES: proxy confounds spiking (dollar/energy shocks masquerading as pulses — the
        briefing line carries the confound flag); TSF redefinitions; the structural-change
        scenario (manufacturing-export China transmits by COMPETITION not commodities — the
        India sign may flip; noted, watched, never assumed)
```

## Part F — Harvest + designs

| Consumer | What it gets |
|---|---|
| L9 enrichment (H54 lane) | the metals-vs-ags relative state (candidate, Tier C) |
| Sector projection | the same state as a metals/mining conditioner cross-check (with H53) |
| Stage-2 briefings | the China-pulse shadow line with confound flag |
| Cycle School | Lesson 24: measuring a neighbor through the commodity window |

Designs: **CN-D1** the real TSF impulse + H54 acceptance (runsheet step 64, registered before
any look). **CN-D2** customs-volume cross-check (iron-ore/copper import volumes vs the proxy —
demand-side identification's first leg). **CN-D3** the structural-change watch: the
export-competition channel's India sign (design only; needs trade-share data).

## Part H — Knowledge ledger (atlas 2.11)

**Established (our runs):** the China era structurally changed metals-vs-ags dynamics (2.19x);
the named 2009/2016 pulses printed the predicted sign (2/2, confounds recorded). **Candidate
[H54]:** the impulse concept is sound machinery awaiting its data; the proxy is a licensed
shadow, never a signal. **Unknowable:** whether the post-property China still pulses through
commodities at all — the 2022-26 record (cases chapter) suggests weakening; the watch is
annual and the India sign under the export-competition regime is an open question with a
registered design. **Process:** a candidate entry ran honest trials on a PROXY with confounds
declared at registration — the pattern for every future data-blocked candidate.
