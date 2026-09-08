# The Indian Business Cycle — Literature Synthesis (Track FUN dossier B)

*2026-09-08; Sonnet research agent B, adversarially consumed by the desk. Knowledge
synthesis only — every quantitative claim [LIT] with approximate source; a prior to be
re-argued once vault data lands. Does not duplicate booked doctrine (Atlas 2.3, GDP/ER
arcs, CI arc, FUN-D1/D2/D3 — referenced, not re-derived).*

## 1. The Indian cycle's character

**Monsoon and the agricultural share.** Agriculture ~half of GDP at Independence [LIT,
CSO historical]; ~15-18% of GVA by the 2020s [LIT, MOSPI] while still employing ~40-45%
of the workforce [LIT]. Through the 1950s-80s a bad monsoon was near-sufficient for a
slowdown; today the channel is second-order, working through rural demand and food-CPI
(food ~40% of the CPI basket [LIT, MOSPI]). A pre-1991 monsoon indicator has little
read-through to a post-2010 book.

**The pre/post-1991 break.** License-Raj era = the "Hindu rate of growth" (Raj Krishna,
~1978 [LIT]): trend ~3.5%/yr vs population +2.2%. The 1991 BoP crisis (reserves at weeks
of imports) forced liberalization; post-1991 trend growth usually cited 5.5-7%/yr [LIT,
e.g. Ahluwalia ~2002] — a genuine trend break. Any series spanning 1991 needs a
structural-break treatment; Hamilton's regression filter (CONTRACT §8, never HP) is far
more robust to this one-time shift.

**The post-2000 investment cycle and the twin balance sheet.** 2003-08 corporate capex
boom financed by bank credit into infra/power/steel; interrupted by the GFC, revived
2009-11 on stimulus, then curdled into the "twin balance sheet problem" (Economic Survey
~2015-16, Subramanian; RBI AQR under Rajan ~2013-16 [LIT]) — over-leveraged corporates +
NPA-laden PSU banks. India's clearest domestically generated credit cycle: boom, then a
2011-2018/19 deleveraging bust — the natural candidate cycle for FUN-D6.

**Informality and measurement.** ~80-90% of the workforce informal [LIT, ILO/NSSO-based,
approximate]; informal output is proxy-extrapolated in GDP. Consequences: (i)
formalization shocks — demonetization (Nov 2016), GST (Jul 2017) — created LEVEL SHIFTS
in measured formal activity easily mistaken for cyclical turns, exactly when the
GST/e-way/UPI indicator era begins (their early years carry a formalization trend, not a
clean cycle); (ii) informal-sector distress can run counter to the formal-sector cycle
the official indicators track.

**Why classical recessions are rare.** Negative real-GDP years: FY1957-58, FY1965-66,
FY1972-73/1979-80, and FY2020-21 (COVID, ~−6 to −7% [LIT, MOSPI]) — the first clean
modern-era contraction. The EM pattern per Aguiar & Gopinath (~2007) "The Cycle Is the
Trend" [LIT]: EM cycles are dominated by shocks to trend growth. India's object of study
is the GROWTH CYCLE — the FUN-D1 quadrant template is the right one; a literal
level-contraction is the rare tail.

**Slowdown episodes** [LIT, one-line drivers]: 1957-58 (Second-Plan BoP/import
compression); 1965-67 (double monsoon failure + Indo-Pak war + PL-480 suspension);
1972-73/1979-80 (oil shocks on drought years); 1991 (BoP crisis + Gulf-War oil +
politics); 2000-02 (dot-com/US recession via IT/trade + 2002 drought); 2008-09 (GFC via
trade and flows; banks insulated from subprime); 2011-13 (twin-balance-sheet unwind,
policy paralysis, taper tantrum, wide CAD); 2019-20 (NBFC/IL&FS stress + real-estate
distress + weak consumption, then COVID).

## 2. Who dates the Indian cycle

**There is no standing official dating authority** — a first-order fact: every "the cycle
turned in month X" claim is an academic/RBI-research construction (Tier B/C).
- **RBI**: CLI work since the late 1990s; Mall's RBI Occasional Paper (~1999) the
  foundational CLI against IIP [LIT]; MPR output-gap/Markov-switching estimates used
  internally, no published chronology.
- **NCAER**: Business Expectations Survey since the 1950s-60s [LIT, LOW CONFIDENCE on
  start] — one of the longest Indian sentiment series.
- **Dua & Banerji** (DSE + ECRI): classical NBER/ECRI-methodology leading/coincident
  composites for India (late 1990s-2000s [LIT]); leading index leads the reference cycle
  by several months (ECRI tradition ~half a year [LIT, LOW CONFIDENCE]); growth-rate
  slowdowns dominate.
- **Pandey, Patnaik & Shah** (NIPFP, ~2016 [LIT]): Bry-Boschan dating of Indian GROWTH
  cycles — classical recessions essentially absent; full-cycle lengths cluster ~4-6y
  peak-to-peak [LIT, LOW CONFIDENCE]; amplitude moderation post-1991 (contested, few
  cycles in sample — India alone fails the CONTRACT ≥4-periods clock bar, which is why
  the program pools on JST).
- **OECD CLI for India**: live, free, IIP-referenced; India-specific lead/hit-rate not
  quotable from memory [LIT, LOW CONFIDENCE].

## 3. The Indian indicator set (lags approximate; check each series' docs at pull time)

| Indicator | Freq | Pub lag | Free source | Leads/identifies | Quirks |
|---|---|---|---|---|---|
| IIP (headline) | M | ~6w | MOSPI | The classical reference series | Base-year breaks (2004-05→2011-12); heavy revisions |
| Core-sector IIP (8 industries) | M | ~3-4w | OEA/DPIIT (PIB) | Early IIP read; capex/infra proxy | ~40% of IIP from 8 industries — concentration |
| PMI mfg/services | M | ~1-3d | S&P Global release | Fastest sentiment; diffusion not level | Private small panel; methodology rebrands |
| GST collections | M | ~1d | GSTN/PIB | Consumption + formalization | **Jul 2017+ only**; rate changes confound YoY |
| E-way bills | M | near-RT | GSTN | Freight/goods movement | **Apr 2018+ only** |
| Rail freight | M | ~2-4w | Ministry of Railways/PIB | Bulk goods | Decades of history; administered prices decouple |
| Port cargo | M | ~3-4w | IPA | Physical trade | Major ports only; private-port share grows |
| Electricity demand | D/M | ~1d | POSOCO/CEA | High-frequency nowcast | Weather noise; renewables change composition |
| Petroleum products (diesel) | M | ~2-3w | PPAC | Transport/industrial | Pre/post-2010 decontrol breaks comparability |
| Auto: 2W / PV / tractor | M | ~1-2w | SIAM (wholesale); Vahan/FADA (retail) | Rural / urban / farm splits | Wholesale vs retail diverge (channel stuffing) |
| Credit growth + sectoral deployment | F/M | ~1m | RBI DBIE | The credit cycle by sector | SCBs only (no NBFCs); HDFC-merger break 2023 |
| OBICUS | Q | ~2-3m | RBI | Capacity utilization / capex turns | Small panel, revised |
| RBI consumer confidence + inflation expectations | 2M | at MPC | RBI | Household sentiment | Urban-skewed; expectations upward-biased |
| CPI | M | ~2w | MOSPI | Inflation cycle; food ~40% | Base revisions |
| WPI | M | ~2w | OEA | Producer prices; longer history | No longer the target (CPI since 2016 FIT) |
| Trade data | M | ~2-4w | DGCIS/RBI | External demand; IT decoupling | Provisional vs final; services lag goods |
| FII/DII flows | D | T+1 | NSDL; NSE/BSE | Flow cycle | Coincident/lagging more than leading |
| Naukri JobSpeak | M | ~1w | Info Edge | White-collar hiring | IT-skewed (US-cycle) |
| Cement / steel production | M | ~3-6w | OEA/JPC | Construction/infra | Regional mismatch; duty-driven supply moves |
| Air passenger traffic | M | ~3-4w | DGCA/AAI | Discretionary consumption | COVID structural break |
| UPI volumes | M | days | NPCI | Digital consumption | Meaningful ~2019+; P2P vs P2M mix |
| CMIE (unemployment, CPHS) | M/W | varies | **PAID** | Household cycle | Literature reference only — not vaultable per free-only rule |

**Cross-cutting quirks:** the 2015 GDP methodology controversy (2011-12 base, GVA
switch; Subramanian ~2019 working paper alleging ~2-2.5pp/yr overstatement [LIT],
disputed) is live uncertainty on the REFERENCE SERIES itself; repeated rebasings mean
long-history backtests must stitch explicitly, never splice naively.

## 4. Transmission to NIFTY earnings

- **Bank-credit channel**: capex/working capital run through banks (thin bond market);
  RBI sectoral deployment reads straight into industrials/capital-goods/cement/steel
  earnings (Atlas 2.3's GDP-leads-credit 16/18 is the booked direction; FUN-D6 localizes).
- **Rural-demand channel**: monsoon → farm income (crops, MSP) → rural wages (MGNREGA
  buffer) → 2W/tractor sales → rural FMCG/durables volumes. Largely decoupled from the
  urban/industrial cycle — hence the separate 2W/PV/tractor lines.
- **Government-capex channel**: union/state capex (roads, rail, defence, PLI) is large
  and deliberately counter-cyclical since ~2014; pre-announced in the Budget; execution
  slippage is the recurring gap.
- **Export/IT channel — a US-cycle exposure, NOT an India-cycle one**: IT (and partly
  pharma) demand is US/global corporate budgets; NIFTY IT is a global-cycle exposure in
  an India-listed wrapper. Consistent with FUN-D3's kill of IT-as-forward-hedge. Any
  sector-rotation-by-India-phase design must not classify IT as a domestic-cycle sector.
- **Oil-import channel**: ~85% import dependence [LIT, PPAC]; a spike hits CAD/INR, CPI,
  and crude-input margins simultaneously — the SIGN is opposite to exporter-economy
  commodity literature (already booked: the global factor owns the commodity link).

## 5. Indian asset behavior across the domestic cycle — what is known

The India-specific academic literature on cycle-conditioned asset/sector behavior is
THIN TO ABSENT — the absence is the finding [LIT, LOW CONFIDENCE].
- Sector rotation: no rigorous India-specific phase-conditioned academic study known
  outside this program's own FUN-D3 (one-way: defensives lag once risk-off is
  identifiable); qualitative EM-practitioner consensus agrees.
- Small-vs-large across phases: brokerage "wealth creation" studies (e.g. Motilal Oswal
  [LIT, Tier C]) — small/midcaps outperform off troughs, draw down harder in slowdowns;
  no peer-reviewed formal dating study known. FUN-D4 fills this once NSE size/sector
  indices land.
- Earnings cyclicality by sector (sell-side/RBI qualitative consensus, Tier C
  throughout): capital goods/infra/cement/steel = early-cycle high-operating-leverage;
  banks/NBFCs = credit-coincident with a LAGGED counter-running asset-quality cycle
  (2011-18); autos split by the rural/urban channel; FMCG/pharma = low growth-beta,
  rural-income and input-cost beta; IT = US-beta, near-zero domestic beta.

**Bottom line:** the dating literature converges ("growth cycles, moderate amplitude
post-1991, no official chronology"); the cycle-conditioned ASSET literature barely
exists — FUN-D4/D7 will likely CONSTITUTE the primary literature, not confirm one.
