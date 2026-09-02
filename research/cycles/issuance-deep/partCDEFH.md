# Parts C–H — data engineering, math, algorithm, harvest, ledger (atlas 3.2; seat L7, Tier B)

## Part C — Data engineering (compact, in-house)

| Leg | Source | Cadence / notes |
|---|---|---|
| Issue calendar + sizes (mainboard/SME/QIP/OFS/rights) | NSE/BSE public issue pages; SEBI monthly bulletins; prime-database-style aggregates are PAID — the free build is exchange-first | per-issue; monthly aggregation |
| Subscription books (QIB/HNI/retail) | exchange live-bid archives + red-herring outcomes | per-issue; the free RECEPTION variable |
| First-day pops | bhavcopy (listing-day open/close vs issue price) — the existing puller family | per-issue |
| Market cap denominator | index factsheets/bhavcopy aggregates | monthly |
| SEBI actions (the institutional thermometer) | SEBI orders/circulars | event registry entries |

PIT hazards: SME-board survivorship (delisted/migrated issues retained); issue-price
restatements (anchor allotments vs final); the mainboard/SME split kept as SEPARATE series
(microstructure differs — the psychology chapter's SME caution is structural here); calendar
lag between filing, open, and listing (state timestamps on LISTING date, declared).
Runsheet addendum 15 (steps 78-81): 78 exchange issue-calendar scraper (mainboard+SME,
2000s→) ~5-6h; 79 subscription-book backfill ~3-4h; 80 listing-day pop assembly from bhavcopy
~2-3h; 81 IS1/IS2 acceptance fill + first India two-leg state (two-pass) ~2-3h.

## Part D — The mathematics

state_t = availability-weighted mean of {pct(volume/mcap), pct(median pop)} with n_legs
(no-listing months degrade to the volume leg — tested). Why the persistent-incentive argument
changes the decay prior: most seats assume alpha decays (Contract); L7's edge is an incentive
equilibrium — issuers CANNOT be arbitraged out of timing their own sales — so the desk's
haircut applies to the MAGNITUDE, not the existence, of the effect (the ladder's Tier-B
confidence with the Schultz pseudo-timing critique carried as the honest counter). The froth
signature needs BOTH legs high (volume alone = capital formation; pops alone = scarcity);
the flag threshold sits on the registered grid. Consumption is reduce-only twice over:
valuation_sentiment block confirm (with L8's spread — expensive market + hot primary = the
double-confirm) and the special-sits sleeve sizing (froth => shrink).

## Part E — The algorithm (L7, monthly)

```
STEP 1  monthly aggregation: issuance value / mcap; median listing pop; subscription medians
        (mainboard and SME as SEPARATE series; the state reads mainboard, SME is a satellite
        briefing line — the 2023-25 frenzy showed why)
STEP 2  expanding percentiles (shared grids) -> two-leg state + n_legs
STEP 3  consumption: valuation_sentiment block (0.10, with L8); special-sits sleeve sizing
        rule (froth_flag => shrink per the registered schedule); NO short-signal path exists
STEP 4  SEBI-action registry entries annotate the state (a regulator acting IS a reading)
MONITOR quarterly re-aggregation; the SME/mainboard divergence watch; IS1/IS2 at data-landing
FAILURE MODES: SME microstructure polluting the pop leg (separated by design); QIP/OFS
        classification drift; the wave arriving through NEW vehicles (REIT/InvIT waves —
        the calendar scraper's category audit is annual)
```

## Part F — Harvest + designs

| Consumer | What it gets |
|---|---|
| valuation_sentiment block | the froth state (with L8 — the double-confirm) |
| Special-sits sleeve | the sizing rule (froth => shrink) per L7's role line |
| Stage-2 briefings | the SME satellite line + the SEBI-action annotations |
| Cycle School | Lesson 29: the signal that shouldn't decay, and why |

Designs: **IS1** (registered, prior stated) the Baker-Wurgler India test; **IS2** (registered)
the 2018/2023-24 episode shape check — the ladder's own changes_if; **IS-D3** promoter/PE OFS
selling as a third leg candidate (design only; classification work first).

## Part H — Knowledge ledger (atlas 3.2)

**Established (fixture-verified machinery + record):** the two-leg state separates planted
froth from winter (0.9 vs 0.2) and degrades honestly through no-listing months; the module
exposes no short-signal path. **Established (record, cases chapter):** India's issuance waves
top-tick markets with regularity (1994-96, 2007-08, 2021, 2024) and regulators confirm froth
institutionally (SEBI 2024 — the ladder's own citation). **Awaits India data [B]:** IS1/IS2 —
the seat's numbers; the primary-market vault is runsheet addendum 15. **Unknowable:** which
VEHICLE carries the next wave (the category-audit exists because the fragile node moves here
too). **Tier note:** L7 stays Tier B on the strength of the incentive argument + the global
evidence; the India-specific coefficients wait for their test, as the ladder's changes_if
already says.
