# CN PROGRAMME — the China land & property crash, end to end
Opened 2026-09-11 by principal directive: "land price in china crash, cover tier 1 tier 2 3 and
capital city and land vs appartment vs houses vs shops vs buildings in key centres on business rent
etc, rental yield pre crash post crash, avg crash velocity and pre crash rising velocity, debt no.
that were predicting a crash is upcoming, other interesting facts, reits of china and much more...
keep it as a larger task... 3 parallel agents at a time, 200+ agents, 500+ tasks... final output a
dashboard."

## 0. The one decision that shapes everything
Egress was TESTED before planning, not assumed: **WebSearch/WebFetch work in this session**
(NSE/RBI/FRED remain blocked — unchanged). So this is a genuinely SOURCED research programme, not a
recall exercise. Two consequences, both binding:
1. Every number in the final dashboard carries a source URL or is tagged `[RECALL]` /
   `[VERIFY]`. No unsourced figure is presented as fact — the EQ/VAL arc precedent.
2. Web-sourced figures are NOT vault data. They are not sha256-manifested and do not enter
   `ingest/vault/`. They live in `research/notes/china-dossiers/` as cited dossiers. Anything the
   desk later wants to TRADE on must go through a proper runsheet pull first.

## 1. Why this is worth a large task for THIS desk (not just interesting)
Three existing desk positions bear directly on it and none was built with China in view:
- **CI-D1..D5** booked that crises belong to CREDIT and returns to INFLATION, and that housing
  "slows but never negative" in the JST crisis event study. China is the largest live test of
  that claim in history.
- **DB-D1..D9** booked that high public debt kills BONDS not equities — but China's debt is
  LGFV/quasi-fiscal, the exact category JST's `debtgdp` does not measure. Named as a limit.
- **H54 (China credit impulse)** is already an Atlas monograph and a booked candidate. The
  property bust is the mechanism by which the credit impulse transmits — or fails to.
Plus the India read-across the desk actually trades: steel/cement/commodity demand, FPI rotation,
and the L12/L13 real-estate-cycle monographs' 18-year folk cycle.

## 2. Structure: two halves that answer different questions
### HALF A — THE BASE RATE (vault-computable TODAY, pre-registered, desk-grade)
`ingest/vault/jst/JSTdatasetR6.xlsx` — 18 countries, 1870-2020, with `hpnom` (nominal house
prices), `cpi`, `rent_ipolated`, **`housing_rent_yd` (rental yield)**, `tmort` (mortgage debt),
`thh`, `debtgdp`, `eq_tr`, `crisisJST`. China is NOT in JST and that is the point: the panel
supplies the distribution of what property crashes DO, against which China's web-sourced numbers
are placed. Five designs (CN-D1..CN-D5), pre-registered in the trial ledger BEFORE any number is
computed, answering the principal's quantitative questions as BASE RATES:
- CN-D1 crash anatomy: every real drawdown >=20%, its depth, duration, and DECLINE velocity, plus
  the pre-peak APPRECIATION velocity (the principal's "avg crash velocity vs pre crash rising
  velocity", made a distribution instead of an anecdote).
- CN-D2 rental yield through the cycle: yield at peak-5y / peak / trough (the principal's
  "rental yield pre crash post crash").
- CN-D3 what actually predicted it: 5y mortgage-credit run-up ahead of peaks, as a contingency
  table (the principal's "debt no. that were predicting a crash is upcoming").
- CN-D4 does a bigger boom crash faster, or only further?
- CN-D5 the investable leg: equity total return 1y/3y/5y after a housing peak.

### HALF B — CHINA ITSELF (agent research, sourced, on disk)
Ten blocks, ~560 discrete questions, dispatched to Sonnet/Opus subagents **3 concurrent**
(CLAUDE.md rule 6). Each agent writes a cited dossier to
`research/notes/china-dossiers/<slug>.md` and returns <=200 words — content lives on disk, never
in the orchestrator's context (token-wise discipline). Blocks:
- B1 price levels & declines by geography (tier-1 individually, 20 tier-2, tier-3/4 + the
  notorious busts, provincial capitals as a class)
- B2 the LAND market specifically (transfer income, auction failure rates, floor-price share,
  LGFV/state-buyer share, premium rates, centralized auctions, land-vs-house price ratio)
- B3 asset-class splits (land / apartment / villa-house / shop-retail / office / industrial-
  logistics / hotel / 类住宅) by key centre
- B4 rental yields and business rent pre- vs post-crash (residential gross yield, Grade-A office
  cap rates and vacancy, high-street vs mall rent, logistics)
- B5 velocity & anatomy (monthly decline rates, peak-to-trough by city, time-to-trough, the
  2015-16 destocking boom, and the Japan/US/Spain/Ireland/HK comparisons)
- B6 debt & the predictive indicators (developer-by-developer, Three Red Lines, presale escrow,
  LGFV and hidden debt, BIS credit-to-GDP gap, property share of GDP, inventory months,
  unfinished units, vacancy surveys, starts vs completions)
- B7 REITs and listed vehicles (C-REITs pilot and expansion, each listed C-REIT's yield and
  performance, HK/Singapore China-asset REITs, the offshore USD developer bond market and
  recovery values, the property equity indices)
- B8 policy, mechanism and demographics (the full 2020-2026 policy sequence, property tax
  pilots, PSL and state purchase, hukou, births and household formation, Rogoff-Yang)
- B9 comparative history & the genuinely interesting facts (Hainan 1993 and Beihai — China's own
  precedents; Wenzhou 2011; ghost cities; price-to-income by city; the six-pockets phenomenon;
  the 2022 mortgage strike)
- B10 the India read-across — what this means for the book the desk actually runs.

## 3. Honest scope statement on the agent count
The principal asked for 200+ agents / 500+ tasks. The task COUNT is deliverable and is the real
target: ~560 discrete sourced questions. The AGENT count is a means, and the binding constraint is
token budget, not willingness: a research agent that actually searches, fetches and writes a cited
dossier costs materially more than a thin one. The programme is therefore sized at **~120-150
agents carrying ~4-6 questions each**, run 3 at a time, extendable toward 200+ if budget allows
after the first blocks land. Stated here rather than discovered later, and the trade is deliberate:
560 well-sourced answers across 130 agents beats 560 thin ones across 200.

## 4. Deliverables
1. `research/notes/china-dossiers/*.md` — every cited dossier (the archive of record).
2. Trial-ledger entries CN-D1..CN-D5 (registration BEFORE the run) + their RESULT entry.
3. `scripts/analyze_china_baserate.py` — the JST base-rate runner.
4. A published dashboard artifact + committed copy in `docs/learn/artifacts/` + a README row
   (preservation rule), with China placed on every base-rate distribution.
5. RUNSHEET rows for whatever turns out to be tradeable-but-unpulled.

## 5. Discipline that applies unchanged
Pre-register before running; interpretation after the print; bars never moved; census append-only;
both commit gates; commit and push everything; `[LIT]`/`[RECALL]`/`[VERIFY]` tagging on every
non-computed claim; agents may cite only what they can source, and may NOT invent figures.
