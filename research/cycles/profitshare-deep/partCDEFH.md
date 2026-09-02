# Parts C–H — data engineering, math, algorithm, harvest, ledger (atlas 2.15; candidate H56)

## Part C — Data engineering (compact, in-house)

| Leg | Source | Status |
|---|---|---|
| Macro capital share (1−labsh), 180+ countries 1950-2019 | PWT 10.0 | VAULTED + authenticated (PA1; the PA1c marginal miss recorded) |
| India LISTED corporate profits/GDP (the H56 series proper) | aggregate filings (exchange disclosures) ÷ MoSPI nominal GDP | runsheet — the fundamentals-puller gap capex-partC already flagged; annual, FY basis |
| Corporate tax collections (the cross-check leg) | CGA monthly / Budget docs | shared with fiscal pulls — dedup noted |
| Household/govt saving (the Kalecki decomposition legs) | MoSPI NAS institutional accounts | runsheet; ~18m lag on the split |

PIT hazards: PWT vintage revisions (10.0 → 10.01 → 11 re-state labsh history — vintage-named
files, WORM); the listed-universe drift (new listings mechanically raise listed-profits/GDP —
the H56 series needs a constant-universe variant printed alongside); GDP rebasing (the
Feb-2026 rebase splice discipline, buscycle Part B).
Runsheet addendum 14 (steps 74-77): 74 listed-profits aggregation pipeline (8-10h — the
band's largest single build, shared with the optimizer's fundamentals needs); 75 NAS saving
legs (~2h); 76 constant-universe variant (~2h); 77 H56 acceptance registration (BEFORE the
look): percentile-conditioned extrapolation test with L8, purged (~2h).

## Part D — The mathematics

Kalecki's identity is the entry's spine (the chapter derives it); the desk's measured
contribution is the PS1/PS2 pair: within-country reversion at 85% breadth AND no decline
prediction at extremes (+6pp vs the +15pp bar) — formally, the capital share s_t behaves like
s_{t+10} − s_t = α_c − β·(s_t − trend) + ε with β>0 (PS1) but trend drift α large enough that
even top-quintile s_t rarely yields negative changes (PS2). The licensed sentence: HIGH SHARE
⇒ SMALLER FURTHER RISES, never "must fall". H56's conditioner is therefore an EXTRAPOLATION
GOVERNOR on the valuation block: at high percentiles, the earnings-growth term attributable
to share expansion is haircut toward zero (grid-registered haircut), jointly read with L8's
value spread (high share + expensive market = the double-count to refuse). The macro-vs-
listed caveat is structural: PWT calibrates the QUESTION; the seat's own series is the listed
one (runsheet), and the two are never spliced.

## Part E — The algorithm (H56 candidate, annual with quarterly updates)

```
STEP 1  listed-profits/GDP (FY, constant-universe variant alongside) -> expanding percentile
STEP 2  Kalecki decomposition table (investment, fiscal, saving, external legs) printed with
        every annual update — WHY the share moved decides WHICH reversion forces apply
STEP 3  consumption (Tier C, reduce-only): at high percentiles the valuation block's
        earnings-extrapolation input is haircut (the governor); joint read with L8 flags the
        double-count; NO decline forecast exists in the interface (PS2's fail is the reason)
STEP 4  quarterly earnings seasons update a nowcast shadow (briefing only)
MONITOR annual PS1-PS3 re-run on new PWT vintages; the listed-universe drift check; the
        Smolyansky-style tailwind ledger for India (tax cuts, rate declines — exhaustible
        tailwinds enumerated, each with its remaining runway stated honestly)
FAILURE MODES: universe drift masquerading as share expansion (the constant-universe
        variant); GDP rebase splices; the macro-listed conflation (structurally separated)
```

## Part F — Harvest + designs

| Consumer | What it gets |
|---|---|
| valuation_sentiment block (with L8) | the extrapolation governor at high percentiles (Tier C, reduce-only) |
| Stage-2 briefings | the Kalecki decomposition table + the tailwind ledger |
| Registry | the "reversion around a rising trend" print — cited whenever mean-reversion language appears |
| Cycle School | Lesson 28: what goes up rises slower — Band 2's closing lesson |

Designs: **PS-D1** H56's promotion test (runsheet step 77, registered before the look).
**PS-D2** the listed-vs-macro share wedge as its own diagnostic (design only).

## Part H — Knowledge ledger (atlas 2.15; BAND 2 CLOSES)

**Established (our runs):** relative capital-share reversion at 85%/114-country breadth (PS1);
NO decline-prediction at extremes (PS2's fail — the design-sharpening result); India's macro
share already at its 81st percentile in 2019, pre-tripling (PS3). **Candidate [H56]:** the
extrapolation governor, instrumented, awaiting its listed series. **Unknowable:** whether
India's 2019-24 tripling extends — the seat governs the extrapolation instead of answering
the question. **Band-2 process ledger:** thirteen entries, zero unplanned seats, five labels
retired with prints (Juglar, Kitchin's clock, the dollar cycle, the Fed cycle, the oil
cycle), three candidates instrumented (H54/H55/H56), one seat calibrated (L6), two modules
shipped (L14 here; L11 in Band 1's finale), the frequency sweep closed, and the ENSO control
group sealing the doctrine: states and bands, never dates.
