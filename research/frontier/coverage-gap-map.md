# COVERAGE GAP MAP — what this program has NOT looked at yet
Written 2026-09-11 on principal request ("we have done macro funda and technical — what else is
left which can give us edge and alpha in Indian markets"). Method: enumerate the alpha-source
space, subtract everything already booked in `trial-ledger.md`, subtract everything already
queued in `RUNSHEET.md`, and report only the residual. Nothing here is a finding; this is an
agenda document in the `manager-frontier-sweep.md` tradition — every row is a candidate that
still owes its own pre-registration before any number is computed.

---

## 0. What is already covered (subtracted, not re-listed)

**Booked arcs:** macro (ER/GDP/FISH/CU/DB/CI/FUN monetary seasons), fundamentals (QG/VAL/ES/EQ,
earnings-cycle phase inversion), technicals (TECH ATH/stages/momentum-conditions/valuation
clustering, MOM lookbacks, RATIO ratios+leverage-timing, T-series overnight/intraday/ToM/MA
control), factors (size/value/momentum/low-vol/quality/growth), the option program (OP/VRP/
budget-day IV crush/expiry mechanics), calendar (L5/H58), and the machinery (regime assembler,
walk-forward, DSR/census, cost stack, challenger law, Track P triple-barrier/meta-labels).

**Already on the runsheet** (so NOT gaps, just unlanded): PIT bhavcopy, India VIX tail +
option-chain IV, CCIL money-market (TREPS/call/CP) + RBI LAF, NSDL FPI flows, AMFI SIP/AUM,
primary-market listings/issue sizes, demat counts + retail F&O turnover share, index
reconstitution announcements, results calendars, NSE index P/E-P/B-yield history, NSE sectoral
TR indices, India CPI, India IIP/PMI/GST/OBICUS/consumer-confidence, RBI sectoral bank credit,
India aggregate EPS/PE, as-filed quarterly fundamentals, SEBI shareholding pattern + promoter
pledge history, Ken French industries + RMW/CMA/QMJ, NSE quality indices, Damodaran datasets,
BIS India credit/GDP + RBI/NHB house prices, Shiller/Damodaran US, China TSF, WSTS, DJIA daily.

Everything below is what survives BOTH subtractions.

---

## 1. RUNNABLE TODAY — needs no new data at all

The only genuinely free lunch left. The option-program sweeps already established that the
return gap to the 15/15 target is alpha/data-gated while **the risk side has headroom**
(OP-D6: two stacks in a row moved drawdown, not CAGR). That makes construction mechanics —
not another factor hunt — the place where marginal effort most plausibly pays on vaulted data.

| # | Candidate | What it asks | Data (all vaulted) |
|---|---|---|---|
| G1 | **Rebalance-band / frequency grid** | the desk holds static blends (T3's 50/50 equity-gold beat active rotation) but has NEVER tested the rebalancing RULE itself — calendar (M/Q/A) vs threshold bands (±3/5/10pp) vs hybrid, on after-cost, after-tax terms | NIFTY daily + gold monthly + IIMA factors |
| G2 | **Concentration curve** | how many names before diversification stops paying in India — the marginal-Sharpe curve by portfolio size; informs whether a 25-name or 60-name stock book is right | NIFTY500 survivor panel (one-way) |
| G3 | **Cross-sectional dispersion as a STATE** | is stock-picking conditionally worth more when dispersion is high? A state variable the desk has never built, and the natural gate on whether to run a stock book at all in a given regime | survivor panel + IIMA |
| G4 | **The India LTCG-threshold turnover asymmetry** | India's 1-year holding line creates a real, mechanical after-tax kink no US-derived study captures: the same gross signal has different net value either side of it. Directly prices whether 6-2 momentum (MOM-D1's winner) survives its own tax bill | any vaulted return series + the tax schedule |
| G5 | **Vol-target vs fixed-weight, at BOOK level** | F3a tested vol-managing the index; nobody has tested vol-targeting the whole three-book stack (the interaction with the collar overlay is unexamined) | vaulted series + the standing-book engine |

**Recommendation: G1 and G4 first.** Both are cheap, both attack real money (rebalancing drag
and tax drag are certain costs, unlike hypothetical alpha), and G4 is genuinely India-specific —
no imported study can answer it.

---

## 2. NOT EVEN ON THE RUNSHEET — the real blind spots

All India-specific, all public/free in principle, all blocked at this proxy (principal-machine
pulls), and all — as far as this program's own reading goes — under-researched by the systematic
crowd precisely because they require exchange-disclosure plumbing rather than a factor library.

### 2a. The exchange-microstructure disclosure suite ← **top new-pull priority**
Daily, public, point-in-time by construction, and almost nobody builds it systematically. Same
durability logic as promoter pledge (SYNTHESIS-LH1): the moat is *doing the data work*, not
information asymmetry.

| Signal | Why it might carry information | Design sketch (unregistered) |
|---|---|---|
| **Delivery percentage** (delivered qty / traded qty, per scrip per day) | separates conviction ownership transfer from intraday churn — a free, direct read on whether a move is being *bought* or *traded* | delivery-% terciles x forward returns; delivery-% spike as a confirmation gate on the 6-2 momentum sleeve |
| **F&O ban list** (scrips where market-wide OI breaches 95% of limit) | a hard, exchange-declared marker of extreme crowding in a single name — the crowding measure India's factor book kept failing to find the American way (CR1a/CR2/CR-D2a all no-showed) | ban-entry as an event; forward returns and vol around entry/exit; test as the missing stock-level crowding flag |
| **ASM / GSM surveillance lists** | exchange-imposed additional margin / graded surveillance — a regulator-declared distress-and-froth marker with forced deleveraging attached | list-addition event study; overlap with the promoter-pledge and accrual red-flag sets |
| **Circuit / price-band hits** | forced-halt mechanics create measurable next-day continuation or reversal | upper/lower circuit event study, split by band width and market cap |
| **Bulk & block deal disclosures** | ≥0.5% of equity traded in a day must be disclosed same-day, with counterparty names — genuine informed-flow observation | deal direction x forward returns; repeat-buyer identity as a signal |
| **F&O rollover % and OI build** (monthly expiry) | India-specific positioning gauge; the desk's derivatives work has all been on synthetic/paper chains, never real OI | rollover-% state x next-month index returns; OI-buildup-with-price-direction 2x2 |

### 2b. The corporate-event suite beyond results ← **second new-pull priority**
The runsheet has results calendars and reconstitution. It has NOTHING on the rest of India's very
active corporate-action calendar, and event-driven is the classic home of uncrowded, capacity-
limited alpha.

| Event | Why India specifically | Note |
|---|---|---|
| **IPO lock-in expiry** (anchor 30d; pre-IPO 6m/18m tranches) | a *dated, pre-announced, mechanical* supply shock — the cleanest event structure on this list, and India's IPO pipeline has been heavy | the runsheet's issuance row covers listings/first-day closes, NOT lock-in dates |
| **Buybacks** (tender vs open-market) | acceptance-ratio arbitrage in tender offers is a real retail-accessible edge; and the Oct-2024 tax change (see §3) is a live structural break | needs offer terms + acceptance ratios |
| **Demergers / spinoffs** | the US spinoff anomaly is well documented; India has had a run of large ones, and index-exclusion mechanics force indiscriminate selling of the stub | needs the corporate-action feed |
| **Open offers (SEBI takeover code)** | merger-arb spreads, with India-specific regulatory timelines | |
| **Delisting offers (reverse book building)** | a genuinely India-unique price-discovery mechanism with documented squeeze dynamics | |
| **Rights issues, bonus, splits** | mechanical, dated, retail-behaviour-heavy | |
| **Promoter preferential allotments / warrant conversions** | a governance-and-flow signal simultaneously (insider willingness to fund at a struck price) | pairs with the pledge work |

### 2c. India rates term structure ← **closes an already-named gap**
FUN-D8's slope-ranks-returns finding was flagged as needing **India verification** and that
verification has been owed since 2026-09-08; FUN-D9a then hardened the flag on US monthly data.
The CCIL runsheet row covers the money-market end (TREPS/call/CP) and RBI LAF — but **the G-sec
curve itself (2y/5y/10y/30y) is nowhere on the runsheet.** Without it the India slope leg cannot
run at all.

### 2d. India credit spreads and rating migrations
| Gap | Unblocks |
|---|---|
| Corporate bond spreads (AAA/AA/A over G-sec, by tenor) | the equity-relevant credit-stress state India's own NBFC episode (2018-19) proves matters; the CI/DB batteries are all JST/global, never India-live |
| CRISIL/ICRA rating-action history | downgrade-cluster event study; the migration signal the EQ arc's red-flag work has no India instrument for |

### 2e. Basis and relative-price instruments
| Gap | Why |
|---|---|
| **GIFT Nifty basis** (offshore vs onshore) | an overnight-sentiment and flow-pressure read that pairs directly with T1's overnight discovery — arguably the most natural extension of the desk's single best execution finding |
| ADR/GDR premia on India names | a second offshore-demand gauge, independent of FPI flow reporting lags |

### 2f. Text and filing-language analysis
Flagged in `eq-dossiers/b` §5 as a real frontier technique and explicitly NOT run. Two designs:
YoY **language-diff** on annual reports (the "what changed in the filing" anomaly), and
earnings-call transcript sentiment/hedging markers. India's transcripts are widely public, which
makes this the most obtainable of the alternative-data family.

### 2g. Fund and manager selection ← directly relevant to the operating business
The program studies *markets*; it has never studied *the funds sold into them*. AMFI scheme-level
NAV history is public. Open questions with real money attached: India MF alpha persistence, decay
with AUM (capacity), the flow-performance loop (does retail flow arrive after alpha ends?), and
active-vs-passive crossover by category. The runsheet's AMFI row asks for SIP/AUM *flows* only —
not scheme NAV history.

---

## 3. A CHEAP FIX AVAILABLE NOW — the breaks registry is missing its TAX dimension

`breaks-registry.md` carries BR1-BR6 (OPEC eras, India inflation targeting, weekly expiry, SEBI
2024-26 retail-derivatives curbs, T+1, SIP era). It has **nothing on tax-regime changes**, which
structurally rewrite which strategies work in India — most obviously for dividend-yield, buyback
and turnover-sensitive designs. Three dated entries are owed (added this session as BR7-BR9, each
with a pin-the-notification [VERIFY] in the BR4/BR6 tradition):

- **LTCG on listed equity reintroduced** (Budget 2018) — re-priced every long-hold strategy and
  created the 1-year threshold G4 above exploits.
- **DDT abolished / dividends taxed in the recipient's hands** (Budget 2020) — the single biggest
  break for dividend-yield strategies; VAL-D1's Div_Yld split should never be read across it.
- **Buyback taxation changed twice** (listed-buyback distribution tax 2019; buyback proceeds
  treated as deemed dividend from Oct 2024) + the same-budget STT increase on derivatives — binds
  any buyback or high-turnover design, and compounds BR4.

---

## 4. Ranked recommendation

1. **BR7-BR9 tax breaks into the registry** — free, immediate, and binds every future dividend/
   buyback/turnover design. Done this session.
2. **G1 + G4 (rebalance bands + the LTCG-threshold turnover asymmetry)** — runnable today on
   vaulted data; both attack certain costs rather than hypothetical alpha, which is where the
   option-program sweeps say the headroom actually is.
3. **The microstructure disclosure suite (2a)** — the top NEW pull: most uncovered, most
   India-specific, lowest crowding, and delivery-% plus the F&O ban list may finally give the
   stock-level crowding instrument India's factor book has failed three times to find.
4. **The corporate-event suite (2b)**, led by IPO lock-in expiry — the cleanest dated-supply-shock
   structure available.
5. **The G-sec curve (2c)** — smallest pull on this page and it discharges an explicitly owed
   verification (FUN-D8's India leg).
6. Then 2d/2e/2f/2g as capacity allows; 2g is the one with the most direct bearing on the
   operating business rather than the model.

## 5. What this map does NOT claim

No row above has a registered bar, a prior, or a single computed number. Every one of them is a
candidate in exactly the sense H53-H61 were: it earns its bars BEFORE its data, or it does not
run. Nothing here changes any booked verdict, and nothing here is consumed by any book.
