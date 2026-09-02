# Parts C–H — data engineering, math, algorithm, harvest, ledger (atlas 2.14; candidate H55)

## Part C — Data engineering (compact, in-house)

| Leg | Source | Status |
|---|---|---|
| SST anomalies 1950-2010 | statsmodels vendored series | VAULTED + authenticated (EA1a-c) |
| ONI/Niño3.4 current + post-2010 | NOAA CPC/PSL | BLOCKED here; runsheet pull on the principal's machine; the official episode chronology enters the cases chapter from the public record meanwhile |
| Official ENSO forecasts | IRI/CPC plume | free public; consumed as-is (the desk never re-forecasts) — runsheet monthly save |
| IMD all-India + subdivision rainfall | IMD (mausam.imd.gov.in / data portal) | runsheet; the % - of-LPA table 1901- is public [VERIFY access] |
| Food CPI (weights, sub-indices) | MoSPI | shared with the mp-cycle deflator pulls — dedup noted |
| Sector returns (FMCG, two-wheelers, agri-inputs) | NSE indices + bhavcopy | shared with commodity partC's harvest spec |

PIT hazards: ONI base-period updates (the 30y climatology window rolls every 5y — anomaly
values are re-stated historically! a REAL vintage trap, registry entry); IMD LPA redefinitions
(the LPA base updates, e.g. 89cm→87cm era [VERIFY]); monsoon forecast revisions (Apr vs Jun
issues kept as separate vintages).
Runsheet addendum 13 (steps 70-73): 70 ONI/Nino3.4 pull + climatology-vintage registry ~2h;
71 IMD rainfall backfill (all-India + met subdivisions) ~3-4h; 72 monthly forecast-plume save
~1h setup; 73 H55 acceptance registration (sector conditional returns + food-CPI watch,
purged; bars BEFORE the look) ~2h.

## Part D — The mathematics

The register's control-group logic, formalized: EN1's bar was the same SHAPE as every
financial clock bar (median in-band AND ≥70% in-band), applied to the one object with a
genuine oscillator mechanism. Result: 62% — the best in-band share ever printed here (RE1
45%, KJ1 0%) and still a fail. Two theorems-by-measurement follow: (i) the in-band share is
an ORDERING of clock-likeness (ENSO > property > commodity ≥ Kitchin ≈ K-wave ≈ 0), exactly
matching the mechanism ordering (physical oscillator > capacity echo > none) — the machinery
measures what it should; (ii) the 70% bar is unpassable even for physics under simple
real-time rules — so a financial "pass" (DL1, n=4) carries a presumption of noise, and the
states-never-dates doctrine now rests on a measured ceiling, not taste. ENSO's OWN
consumption is state-shaped: episode phase (El Niño / neutral / La Niña + age) + the official
forecast, with EN3's 92% persistence as the state's justification.

## Part E — The algorithm (H55 candidate, monthly/seasonal)

```
STEP 1  ENSO state from official ONI (once pulled): phase + age + official forecast plume
STEP 2  the CHAIN, each link separately monitored (the base-rate discipline): ENSO state ->
        IMD forecast/realized rainfall -> food-CPI momentum -> RBI language; a conditioner
        may fire ONLY on realized links, never on the event alone
STEP 3  consumption (Tier C, reduce-only, under L5/L6 context): rural-basket sector
        conditioner (FMCG/two-wheelers/agri-inputs/tractors) + the food-CPI->policy watch
        feeding L6's briefing; NO index-level signal exists (EN2 + mechanism)
STEP 4  seasonal cadence: the June-September window gets the weekly rainfall-deviation
        briefing line (L5's calendar machinery hosts the schedule)
MONITOR annual EN1-EN3 re-run when ONI lands; the ENSO-monsoon-link instability literature
        (the correlation itself drifts — the H55 test must be era-split by design)
FAILURE MODES: ONI climatology re-basing (vintage registry); IOD confounding (the 1997
        save — the conditioner reads rainfall, not ENSO, precisely for this); trading the
        June panic (the psychology chapter's counter)
```

## Part F — Harvest + designs

| Consumer | What it gets |
|---|---|
| Sector projection | the rural-basket conditioner candidate (H55, Tier C, reduce-only) |
| L6 briefing | the food-CPI→policy watch line in monsoon season |
| L5 calendar | the monsoon-window scheduling entry |
| Registry | the clock-likeness ordering + the 70%-ceiling lesson (EN1) |
| Cycle School | Lesson 27: the only real oscillator, and why even it isn't a calendar |

Designs: **EN-D1** H55's promotion test (sector conditional returns on REALIZED rainfall
deficits + food-CPI spikes, purged, era-split; bars at registration — runsheet step 73).
**EN-D2** the chain contingency table maintained live (cases chapter's base-rate exhibit,
re-printed annually).

## Part H — Knowledge ledger (atlas 2.14)

**Established (our runs):** ENSO is the register's most clock-like object (median 4.0y
dead-center, 62% in-band) AND still fails a strict bar — the measured ceiling that seals the
states-never-dates doctrine; no India equity-level transfer (EN2, n=6); 92% monthly
persistence (EN3). **Established (record):** the ENSO→monsoon→CPI chain fires link-by-link
with real base rates (the 1997 IOD save; 2009's drought-with-GDP-shrug) — conditioners read
REALIZED links. **Awaits India data [C]:** H55's sector test (runsheet). **Unknowable:** any
given year's monsoon from the ENSO state alone — the chain has two more links and the desk
reads them in order. **Process:** the control-group entry did exactly what it was designed
for — calibrating every other funeral in the sweep.
