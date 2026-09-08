# Track FUN — the fundamentals program (opened 2026-09-08, business cycle first)

Principal directive: "move to fundamentals, start with business cycle — layers, sectoral
level, data points; global research then India-specific." This brief is the track map:
what each layer is, what ran today on vault data (FUN-D1/D2/D3, booked), and what each
remaining layer needs. It builds ON the booked doctrine — Atlas 2.3 (business cycle
CONTEXT: GDP leads credit at home 16/18; band real), the GDP/ER arcs (market leads GDP
1y; growth-negative within-country, median −0.41), the CI arc (crises belong to credit,
returns to inflation), and SEC-D1..D7 (crisis safety = balance sheet > demand > revenue
currency) — none of which is re-run here.

## The layers

| # | Layer | Global leg | India leg | Status |
|---|---|---|---|---|
| 1 | **Phase identification** (growth quadrants: recovery/expansion/slowdown/contraction) | JST annual, 17 countries — **FUN-D1 RUN** | needs IIP + PMI (+GST/OBICUS nowcast) — monthly, vintage-stamped | India = runsheet |
| 2 | **Assets by phase** | **FUN-D1 RUN** (eq/bond/housing/bill, next-year, honest lag) | FUN-D4 after the pulls | India gated |
| 3 | **Sector rotation by phase** | US needs Ken French 12-industry (SEC-D5, frozen pull) | market-proxy partial **FUN-D3 RUN** (one-way); the full version needs NSE sectoral TR indices | both gated for the full version |
| 4 | **Earnings cycle** | Shiller 1871-2023 — **FUN-D2 RUN** | FUN-D7: needs NIFTY aggregate EPS/PE history | India gated |
| 5 | **Credit × sector** | booked at country level (CI arc) | FUN-D6: RBI sectoral credit deployment × sector returns | gated |
| 6 | **Leading indicators** | booked: yield curve = recession-odds only (MG); market leads GDP 1y and no further (ER-D8) | GST/PMI/OBICUS composite nowcast (FUN-D5) | gated |
| 7 | **Valuation × cycle** | booked doctrine (ER arc): states for expectations, never point forecasts; FUN-D2 e5 adds the cheap×depressed-earnings corner | inherits ER doctrine; India EPS needed to localize | partially done |

## What today's three prints established (the track's opening doctrine)

**One inversion, three scales.** All three legs, registered independently, printed the
same law:

1. **Global phases (FUN-D1):** next-year equity is best after RECOVERY (+8.4%) and
   CONTRACTION (+7.1%), worst after EXPANSION (+5.0%) and SLOWDOWN (+2.5%) — post-1950
   the spread widens (CONT +12.0 vs SLOW +1.2). Same-year returns show the opposite
   ordering — the phase pays concurrently, but a phase you can already identify is
   priced. Contraction WITH a financial crisis is the strongest entry (+13.8% next
   year). Inflation regime cuts through every quadrant (high inflation ≈ halves
   next-year equity in all four) — the cycle you must respect FIRST is inflation, then
   the growth quadrant.
2. **Earnings cycle (FUN-D2):** below-trend and falling earnings predict HIGHER
   next-12m returns (+5.4/+5.6 vs +3.2/+2.9), concentrated in the cheap-PE10 half
   (+8.8%) — the mechanism is earnings anti-persistence (annual AR(1) −0.11). Price
   bottoms ~10 months BEFORE the earnings trough in 75% of the 16 episodes since 1871 —
   never wait for earnings to confirm a bottom. Honest decay: the above/below-trend
   signal fades post-1950.
3. **India sectors (FUN-D3, one-way):** once a risk-off state is identifiable,
   defensives (pharma/FMCG/IT) LAG the next 21 days and beaten-down cyclicals/
   financials lead — in both halves. Defensives are DURING-crisis instruments
   (SEC-D6's episode fact stands); they are not an after-crisis trade. Two forward
   trades killed one-way: buy-defensives-on-risk-off, IT-as-21d-USD-hedge.

**Consumption for the books:** phases and earnings states are STATE INPUTS for
expectations (like valuation in the ER arc) — the tradeable content is contrarian and
slow (6m-1y post-stress entries, already expressed in the book's post-spike/stand-down
machinery), never chase-the-phase rotation.

## India-specific data points (all principal-machine; runsheet rows added 2026-09-08)

IIP monthly · PMI mfg+services · GST collections · RBI OBICUS capacity utilization ·
RBI consumer confidence · RBI sectoral bank-credit deployment · NSE sectoral TR indices
(survivorship-free — retires the panel for rotation uses) · NIFTY aggregate EPS/PE
(NSE monthly reports or Damodaran). Free sources exist for all eight; pullers follow
the `ingest/pull_*.py` skeleton convention with vintage stamping (Track P machinery).

## Registered-next queue (designs to write when data lands)

- **FUN-D4** India phase atlas (IIP/PMI quadrants → asset & sector conditioning,
  publication-lag stamped) — the FUN-D1 analog.
- **FUN-D5** nowcast composite (GST+PMI+OBICUS) — judged ONLY against the booked bar
  that market leads GDP, so a nowcast must beat the market's own signal to matter.
- **FUN-D6** credit-by-sector × sector returns (the CI arc at sector level).
- **FUN-D7** India earnings cycle (the FUN-D2 analog: census, lead/lag, trend states).
- **SEC-D5** (already frozen) unblocks the US sector-rotation-by-phase leg on Ken
  French industries; FUN-D1's quadrants become its conditioning variable.

Census cost of the opening leg: 32 cells (10+12+10), booked. Total register: 1,045.
