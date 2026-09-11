# C-LGFV — Local Government Financing Vehicles: the debt no cross-country dataset measures

*Dossier `c-lgfv` (CN programme, Half B, dispatch row 12 — `b6-lgfv` + `b2-land-fiscal-model` +
`b2-land-reform` + `b2-land-monetization`). Compiled 2026-09-11. Direct motivation, stated by the
principal: the desk's cross-country base-rate work (ledger `CN-D3`, `research/frontier/china-property-plan.md`)
found public-debt growth has a predictive lift of only 0.23x on housing peaks and reads
*backwards* — but that test used JST's `debtgdp` field, which is central-government debt. China's
leverage sits in LGFVs, an aggregate no cross-country panel captures. This dossier tries to put a
number on it. Method: WebSearch only — **WebFetch is EGRESS_BLOCKED for every domain** (plan §0a).
Every figure below is therefore a search-result-snippet reconstruction of a primary source, not a
primary-document read; this is Half B's stated verification ceiling, not a caveat unique to this
file. Corroboration rule: load-bearing figures are tagged `[2-SOURCE]`, `[1-SOURCE]`, or
`[RECALL — unverified]`. No figure is invented; where the search bar could not be cleared, the gap
is stated as a gap (§ Gaps and cautions), not filled in. Today's date 2026-09-11; every figure
states its own as-of/vintage date. Web-sourced — not vault data, not sha256-manifested, not a
trial-ledger entry (plan §0/§5). Cross-references, where they exist, are to this same programme's
already-booked `research/notes/china-dossiers/b2-land-national.md`, whose MOF land-revenue series
is more precise than anything independently re-derived here and is cited rather than duplicated.*

## Headline findings

- **The disagreement between LGFV debt estimates is the finding, not noise, and it is almost
  entirely definitional.** Named sources range across a **~4.4x span** — from the PBOC governor's
  own **CNY 14.8tn** (Oct 2024, "hidden debt" narrowly defined) to Goldman Sachs's **CNY 94tn**
  ($13tn, 2023, *total* local government debt including LGFVs) — and the middle of that range
  (IMF, Rhodium) clusters at **CNY 59-66tn** for "LGFV interest-bearing debt" specifically. Three
  different aggregates are being called "China's local debt" in casual usage: (i) the officially
  recognized "hidden debt" subset targeted by the swap programme (~14-15tn), (ii) total LGFV
  interest-bearing liabilities (~59-66tn), and (iii) all local government debt, explicit bonds plus
  LGFVs combined (~94tn and rising). None of the three is wrong; they answer different questions.
- **Public bonds have not broken. Nonstandard debt has, repeatedly, in weak provinces.** Zero
  recorded LGFV defaults on onshore public bonds through 2024 `[2-SOURCE]` sit alongside multiple
  restructurings and technical defaults on bank loans, commercial paper, and trust products in
  Guizhou, Yunnan, Gansu, and Guangxi since 2022 `[2-SOURCE]` — the crux distinction the principal
  asked for, and it is real and holds up across sources.
- **The land-revenue collapse is precisely dated and precisely sized by this desk's own prior
  work**: CNY 8.7051tn (2021 peak) → CNY 4.1518tn (2025), **-52.3% cumulative**
  (`b2-land-national.md`, MOF series) — and it hits LGFVs through two channels simultaneously: the
  fiscal channel (land money that used to flow through government-fund budgets to backstop LGFV
  debt service has shrunk by half) and the collateral channel (land injected into LGFVs as assets,
  conservatively ~25% of LGFV balance sheets `[1-SOURCE]`, is worth less against which to borrow).
- **The 2023-2025 debt-swap programmes are real, executed, and have visibly worked on the
  narrowly-defined "hidden debt" line — CNY 14.3tn (end-2023) reportedly down to CNY 6.5tn
  (end-2025)** `[2-SOURCE]` — but every named critic (S&P's own second report, Capital Economics,
  Michael Pettis/Carnegie) makes the same point in different words: this is a liability
  reclassification (off-balance-sheet LGFV debt → cheaper, longer, on-balance-sheet local
  government bonds), not debt destruction. "Buying time is buying bad habits" is S&P's own
  headline on its own programme.
- **Land finance's origin is more contested than the "1994 reform caused it" folk narrative.** The
  1994 tax-sharing reform recentralized revenue while leaving expenditure with localities, opening
  the vertical gap land finance eventually filled — but peer-reviewed work (*China Quarterly*,
  "The Origins of Land Finance") argues land finance only took off in the early 2000s, driven by an
  anti-corruption campaign that made market-price land auctions politically necessary, and frames
  the central government as an active co-architect, not merely leaving localities to fend for
  themselves.
- **Nothing has replaced land revenue on a like-for-like operating-budget basis** — central
  transfers have grown (CNY 7.44tn 2019 → CNY 10.34tn 2025, a genuine net-new inflow per
  `b2-land-national.md`), special-bond quotas have expanded, but the property tax — the one
  instrument that could structurally replace it — has been shelved since March 2022, explicitly
  because introducing a new property-holding tax mid-crash was judged destabilizing.

---

## ESTIMATE TABLE — named sources, CNY trillion, what each one is actually counting

| Source | As-of date | Figure (CNY tn) | USD equiv. | What is counted | Stock/flow | Tag |
|---|---|---|---|---|---|---|
| PBOC Governor Pan Gongsheng | Oct 2024 (Financial Street Forum speech) | **14.8** | ~$2.1tn | The officially-recognized "hidden debt" (隐性债务) subset — the specific liability category targeted by the 2023-2028 swap programme, NOT total LGFV debt | Stock | `[2-SOURCE]` (Diplomat Sep 2025; multiple secondary citations) |
| Ministry of Finance (official) | End-2023 | **14.3** | ~$1.99tn | Same narrow "hidden debt" category, the swap programme's own starting baseline | Stock | `[2-SOURCE]` (CNN Nov 2024; S&P Global Nov 2024) |
| MOF / State Council, via Caixin | End-2025 | **6.5** (down from 14.3 at end-2023) | ~$0.9tn | Same narrow category, post-swap-programme progress | Stock | `[1-SOURCE — flagged, single Caixin report, not independently cross-checked this session]` |
| IMF, 2023 Article IV Consultation | End-2023 | **~60-60.4** (≈48% of GDP) | ~$8.3-8.4tn | LGFV interest-bearing debt (bonds + bank loans + other interest-bearing liabilities), the IMF's core LGFV aggregate | Stock | `[2-SOURCE]` (multiple press summaries of the same Article IV cycle converge near 60tn/48% GDP; note the same IMF cycle is also reported elsewhere as 65.9tn and, in yet other outlets, as 66tn/$9.3tn or "over 70tn" — see caution below) |
| Rhodium Group, "Tapped Out" | End-2022 (published Jul 2023) | **~59** (~50% of GDP) | ~$8.25tn | Interest-paying debt and payables of the 2,892 LGFVs that have issued bonds (a bond-issuer sample, extrapolated) — explicitly narrower in method than a full-population estimate | Stock | `[2-SOURCE]` (Rhodium's own report; cited independently by USCC, ChinaTalk/Jordan Schneider, Edward Conard's compilation) |
| Goldman Sachs | End-2020 (published Sep 2021) | **~53** (~52% of GDP) | ~$8.2tn | "Hidden local government debt" — Goldman's own LGFV-debt aggregate at that vintage | Stock | `[2-SOURCE]` (Bloomberg, SCMP, Forbes, FXStreet all cite the same Goldman note) |
| Goldman Sachs | 2023 (published Aug 2023) | **~94** | ~$13tn | *Total* local government debt — explicit official local-government bonds PLUS LGFV liabilities combined, a broader aggregate than Goldman's own 2021 figure | Stock | `[1-SOURCE — Asia Financial only; not independently corroborated against a second outlet this session]` |
| S&P Global Ratings | 2018 estimate | **~40** | ~$5.78tn | Off-balance-sheet borrowings by local governments (an earlier-vintage, narrower LGFV estimate; S&P's more recent work, cited throughout this dossier, analyses the swap programme rather than restating a new total-stock figure) | Stock | `[1-SOURCE]` (Reuters via Business Standard) |
| CICC (中金公司) | 2009-2011 (historical) | **~7.2-10** (bank-loan balance only) | n/a | LGFV bank-loan balances specifically, a single-financing-channel figure from 15+ years before the period this dossier is about | Stock | `[1-SOURCE, badly dated]` — **no current (2023-2025) CICC headline total-LGFV-debt estimate could be sourced in English-language search that meets the 2-source bar; see Gaps** |
| IMF "augmented" general government debt | 2023 (cited in 2024/2025 IMF Global Debt Monitor work) | **124% of GDP** (up from 86.3% at an earlier vintage) | n/a | A *different, broader* aggregate again: general government debt PLUS all off-budget government-fund and LGFV activity — not comparable line-for-line with the LGFV-only figures above | % of GDP, stock | `[1-SOURCE — East Asia Forum Sep 2025, citing IMF Article IV/Global Debt Monitor methodology; the exact vintage of the 124% reading itself was not independently pinned to a single dated IMF release this session]` |

**Why they disagree (the finding, restated precisely).** Reading down the table, the estimates are
not five measurements of one number with different amounts of error — they are answers to at least
four different questions: (a) what MOF/PBOC has formally classified as resolvable "hidden debt"
needing a swap (~14-15tn); (b) total interest-bearing LGFV liabilities by the fullest reasonable
count (~59-66tn, where IMF and Rhodium converge despite using different methods — bond-issuer
extrapolation vs. Article IV staff estimate); (c) all local government debt, explicit plus LGFV,
combined (~94tn, Goldman's 2023 figure); and (d) the IMF's broadest "augmented" concept, which adds
in off-budget government-fund activity beyond LGFVs specifically (124% of GDP). Even within
definition (b), the same IMF Article IV consultation cycle is reported across secondary outlets as
anywhere from 60tn to "over 70tn" — a spread this session cannot resolve because WebFetch cannot
reach the primary IMF document to pin the single authoritative sentence; this is exactly the kind
of aggregator noise plan §0a warned would be Half B's ceiling, and it is flagged rather than
silently averaged away.

---

## 1. Total LGFV debt stock: at least three sources, and why they disagree

Covered in full in the Estimate Table and the paragraph above. To restate the single most
important structural fact: **the 14.8tn (Pan Gongsheng, PBOC, Oct 2024) and the 60-66tn (IMF)
figures are not competing estimates of the same thing — they are the numerator and a much larger
denominator of a subset relationship.** The 14.8tn is the slice of debt MOF has formally agreed
needs refinancing under the swap programme; the 60-66tn is essentially all LGFV interest-bearing
debt, most of which is NOT in the "hidden debt" swap category because it either already carries an
implicit government guarantee investors treat as sound, or has not yet been formally recognized as
distressed. `[2-SOURCE]` for the existence of this subset relationship (multiple outlets explicitly
note the swap programme addresses only the "hidden" portion, not total LGFV debt); the precise
ratio between the two categories (14.8/~62 ≈ 24%) is this session's own arithmetic, not a
directly-quoted figure, and is offered as an illustrative ratio only.

CICC could not be sourced at a current vintage meeting the corroboration bar — see Gaps. Requests
for "at least three named sources" are satisfied by IMF, Goldman Sachs, Rhodium Group, S&P Global,
and Pan Gongsheng/PBOC (five, spanning the four definitions above), which the desk judges a
stronger answer to the underlying question than force-fitting a stale CICC number into the same
table as the 2023-2025 figures.

## 2. LGFV interest coverage and the share unable to cover interest from operating cash flow

This is the weakest-sourced section of the dossier and is presented as such rather than papered
over with a single invented headline percentage.

- **Industry-wide, one search synthesis reports an average interest-coverage ratio (EBITDA plus
  government subsidies, divided by interest expense) of ~105% for 2017-2022** — i.e., barely above
  1.0x on average, using a generous numerator that already includes subsidy income `[1-SOURCE —
  could not independently corroborate this specific average against a second, differently-sourced
  figure this session]`.
- **Tianjin, as a named worst case**: interest accruing on Tianjin's LGFV debt alone exceeded 100%
  of all new credit extended in the province over the trailing four quarters — meaning, on this
  reading, essentially every new yuan of credit entering Tianjin was going to service old LGFV
  interest, not fund anything new `[1-SOURCE]`.
- **A related but distinct statistic, for context, not as a direct answer**: Moody's estimated
  roughly one-third of outstanding *SOE* debt (not LGFV-specific; LGFVs are a subset of the SOE
  universe, not the whole of it), equal to nearly 40% of GDP, carries an interest-coverage ratio
  below 1.0x `[1-SOURCE]`. This is offered as the closest available proxy, explicitly flagged as
  measuring the wrong (broader) population.
- **By end-2022, monthly debt-service obligations exceeded monthly fiscal income in 12 of China's
  31 provincial-level units** `[1-SOURCE]` — a liquidity-stress fact adjacent to, but not the same
  as, an interest-coverage-ratio statistic.
- **No figure meeting the corroboration bar states "X% of LGFVs cannot cover interest from
  operating cash flow" as a single national statistic.** The desk's own experience report (b6 debt
  dossier, already booked) makes the identical point about developer leverage data: level readings
  are contested, flow/direction readings are cleaner. The Tianjin case and the 12-of-31-provinces
  fact are the clearest flow-direction evidence available; a clean national interest-coverage
  percentage is not.

## 3. The 2023-2025 debt-swap and refinancing programmes: size, mechanics, did they reduce debt or move it

**Chronology and size** `[2-SOURCE throughout]`:
- **August 2023**: An initial, smaller swap authorized roughly CNY 1tn ($139bn) of local bonds to
  replace LGFV debt across ~12 provincial-level regions identified as most distressed (Bloomberg,
  Malay Mail).
- **March 2024 onward**: Provinces given expanded tools/options to address LGFV strains
  (Bloomberg).
- **November 2024 — the headline package**: The NPC Standing Committee approved a three-year,
  roughly **CNY 10-12tn** hidden-debt resolution package: **CNY 6tn** in new general local
  government bond quota over 2024-2026, plus **CNY 4tn** drawn from special-purpose bond
  allocations at **CNY 800bn/year for five years (2024-2028)**, alongside a separate **CNY 2tn**
  central guarantee covering shantytown-redevelopment-linked hidden debt. Target: cut the
  officially-recognized hidden-debt stock from CNY 14.3tn (end-2023) to CNY ~2.3tn by 2028 (CNN;
  S&P Global; China Daily — figures consistent with, and here cross-referenced to,
  `b2-land-national.md` §Q5[3], which independently sourced the same CNY ~12tn package and adds
  the officially-quoted **CNY ~600bn interest-savings-over-five-years** estimate).
- **Progress to date**: hidden debt reportedly down to **CNY 6.5tn by end-2025** — roughly halved
  in two years — per Caixin (Sep 2026 report headline: "China Slashes Hidden Local Government Debt
  by Half in Two Years") `[1-SOURCE — this specific 6.5tn end-2025 figure]`.

**Mechanics**: LGFV liabilities that are short-tenor, high-cost, and off-balance-sheet (bank loans,
commercial paper, trust/nonstandard debt, some bonds) are swapped for local-government bonds that
are longer-tenor, lower-cost, and formally on the government's own balance sheet. Banks benefit
because the risk weight on the new government bonds (20%) is far below the risk weight on the old
LGFV loans (75-100%), freeing capital and lowering provisioning needs (S&P Global).

**Did it reduce debt or just move it? — both readings are defensible and both are sourced.**
- **"It worked, partially" (S&P Global, Nov 2024 LGFV Brief)**: explicitly titled "a good start" —
  the programme genuinely lowers near-term rollover risk, cuts funding costs, and extends
  maturities.
- **"It just relabels the debt" (multiple named critics)**: Capital Economics called it a
  "band-aid" — it addresses liquidity stress, not the underlying structural revenue shortfall.
  Michael Pettis (Carnegie Endowment, Aug 2025 — "Using China's Central Government Balance Sheet
  to 'Clean Up' Local Government Debt Is a Bad Idea"; and a related Aug 2026 Carnegie piece, "Who
  Paid for China's Last Debt Cleanup, and Who Will Pay for the Next?") makes the sharpest version
  of this argument: "moving bad loans from one balance sheet to another does not eliminate them...
  losses never disappear, even when they appear to." **S&P Global's own separate report on the
  same programme is titled, verbatim, "Buying Time Is Buying Bad Habits"** (Sep 2024) — the same
  rating agency that called the programme "a good start" also explicitly warned, in its own
  headline, that it substitutes time for reform.
- **The aggregate-credit cross-check supports the "moved, not eliminated" reading**: total social
  financing reportedly rose from 303% of GDP (end-2024) to 309% of GDP (mid-2025) even as the
  narrowly-defined "hidden debt" line item was shrinking — i.e., system-wide leverage kept rising
  while the specific accounting category being reported on publicly improved (East Asia Forum, Sep
  2025, "China's debt reckoning," citing Carnegie-linked analysis) `[1-SOURCE]`.
- **Desk's own read (not a verdict, an observation)**: these two findings are not in tension with
  each other — a program can genuinely lower rollover risk and funding cost (true, and useful) AND
  fail to reduce total system leverage (also true, on the aggregate numbers) simultaneously,
  because the swap does not extinguish principal, it re-prices and re-classifies it.

## 4. The transmission from the land-sale collapse to LGFV distress

**The base fact, already established and precisely dated by this desk's own prior work**
(`b2-land-national.md`, MOF series, not re-derived here): national land-transfer income fell from
**CNY 8.7051tn (2021 peak) to CNY 4.1518tn (2025), a cumulative -52.3% decline**, four consecutive
down-years. Volume fell even further — China Index Academy's 300-city residential land floor area
transacted fell **-66.4%** from its 2020 peak to 2024, worse than the revenue figure because a
shrinking pool of expensive megacity parcels props up the fiscal aggregate even as the broad market
collapses (`b2-land-national.md`, its own headline finding).

**The mechanism, in two channels, running simultaneously:**

1. **The fiscal channel.** LGFVs were never simply passive holders of land; they were, across
   many cities, the marginal *buyer* of land at auction once private developers pulled back — a
   state-buyer/floor-price role documented elsewhere in this programme (`b2-land-national.md` /
   `b2-land-auctions` scope). Land-sale proceeds flow through the same government-fund budget that
   funds LGFV capital injections and, indirectly, local governments' capacity to support LGFV debt
   service. As that fund-budget revenue line fell by half, the fiscal cushion behind LGFV debt
   thinned correspondingly. `[2-SOURCE]` for the general mechanism (multiple sources describe
   collapsing land revenue "undermining LGFV cash flows and basic services" and note "developer
   stress migrates into banks and state-owned firms via rollovers and implicit support").
2. **The collateral channel.** Land use rights are directly injected into LGFVs as balance-sheet
   assets and used as collateral for both bank loans and bonds — land and real estate are
   estimated, conservatively, at **~25% of total LGFV assets** `[1-SOURCE]`. As land prices and
   (especially) transaction volume fall, both the marked value of that collateral and the ability
   to originate fresh borrowing against it deteriorate. A **2013 National Audit Office review found
   37% of then-outstanding local government debt used future land-sale revenue explicitly as a
   named repayment source** `[1-SOURCE, and 13 years stale — see Gaps]` — the structural link is
   long-standing; no more recent comprehensive official audit of the collateral composition of
   local debt was found in this session's searches.
3. **The spillover to banks.** S&P Global estimated LGFV strains could inflict a roughly **CNY 2tn
   hit on China's regional banks** (Oct 2023 report title: "LGFV Strains May Inflict a RMB2
   Trillion Hit on China Regional Banks") — the collateral-and-cash-flow deterioration described
   above is the mechanism by which LGFV distress becomes bank-balance-sheet distress specifically
   in the smaller, more geographically concentrated regional lenders `[1-SOURCE]`.

**What could not be quantified**: no source found in this session models, in percentage or CNY
terms, what a *specific* land-price decline (e.g., "a 30% fall") does to LGFV collateral coverage
or loan-to-value ratios at a national level. The mechanism above is directionally well-attested;
translating it into "a 30% land-price fall produces a CNY-X collateral shortfall" would require
either a primary LGFV balance-sheet dataset (blocked, egress) or a study this session's searches
did not surface. This is stated as a gap in §6 of Question 6 below and in the closing Gaps section,
not filled with an invented number.

## 5. Actual LGFV defaults: public bonds vs. non-standard debt — the crux distinction

**Public bonds: effectively zero.** Across every source surfaced in this session — RBA's own
October 2024 LGFV bulletin, MacroPolo's "Default Position" analysis, and general reporting on the
CNY 4.65tn ($651bn) of LGFV bonds that came due in 2024 (a record) — the consistent statement is
that LGFVs have not defaulted on onshore public bonds `[2-SOURCE]`. The implicit-guarantee "hard
floor" around public bond markets specifically has held through the entire property downturn.

**Non-standard debt: multiple documented breaks, concentrated in weaker provinces:**
- **Zunyi Road & Bridge Co.** (Zunyi, Guizhou), the largest city-owned LGFV in its city,
  restructured **CNY 15.6bn** of bank loans on 30 December 2022 into a 20-year repayment schedule
  with a 10-year principal holiday and a 2-percentage-point rate cut — the first such LGFV
  bank-loan restructuring in China, explicitly NOT termed a "default" by authorities but a de facto
  distressed-debt-exchange in substance. A central bank official was quoted stating "the Zunyi
  model received special permission — it won't be rolled out across the country" (Caixin, Jan
  2023; SCMP) `[2-SOURCE]`.
- **Credit events / technical defaults on commercial paper, trust products, and other nonstandard
  instruments** were reported at LGFVs in **Kunming, Lanzhou, Guiyang, and Liuzhou** since 2022
  `[2-SOURCE — reported across SCMP and other outlets tracking the same set of weak-province
  LGFVs]`. These sit specifically in private-placement, bank-loan, and trust-financing channels —
  not the public bond market.
- **Zhongzhi/Zhongrong (2023) is adjacent, not the same thing, and is kept analytically separate
  per the corroboration rule's "be precise about what is counted" instruction.** Zhongrong
  International Trust missed payments on multiple products in mid-2023; its controlling
  shareholder Zhongzhi Enterprise Group later disclosed liabilities of CNY ~420-460bn ($59-65bn)
  against ~CNY 200bn ($28bn) of tangible assets, a shortfall of up to $37bn, and filed for
  bankruptcy in early 2024. This is a **property-developer-exposed shadow-banking/trust-industry
  collapse**, not a documented instance of an LGFV itself defaulting on a trust product it had
  issued — the underlying assets behind Zhongrong's troubled products were concentrated in
  real-estate developer exposure, not LGFV paper specifically `[2-SOURCE for the Zhongzhi/Zhongrong
  facts themselves; 0-SOURCE found this session directly tying Zhongzhi's losses to LGFV-issued
  trust products specifically — flagged as a likely-but-unconfirmed adjacency, not asserted as
  fact]`.

**The crux answer, stated plainly**: something has broken, but it broke exactly where the
"implicit guarantee" is weakest and least visible to bond-market investors — bank loans,
commercial paper, and trust financing at LGFVs in China's poorer, more indebted provinces — while
the instrument that would be most visible to foreign and domestic capital markets (public bonds)
has not broken at all, anywhere, through 2024. Both statements are simultaneously true and are the
same finding the b6 debt-predictive dossier already reached about developer credit ratings versus
developer balance sheets: the headline instrument (ratings/bonds) lagged; the harder-to-see
instrument (nonstandard debt/balance-sheet leverage) moved first.

## 6. How much local-government debt is collateralized on land, and what a land-price fall does to it

Covered substantively in §4 above; restated here directly against the question as asked:
- **37% of local government debt (2013 NAO audit)** was explicitly repayable from future land-sale
  revenue `[1-SOURCE, 13 years stale]`.
- **~25% of LGFV balance-sheet assets** are land and real estate, conservatively estimated
  `[1-SOURCE]`.
- **No current (post-2018), comprehensive, officially-audited figure for the land-collateralized
  share of local debt was found.** China's National Audit Office has not repeated the 2013-style
  comprehensive local-debt audit in a form this session's searches could surface at a current
  vintage.
- **What a 30% land-price fall does to that collateral: not quantified by any source found in this
  session.** The qualitative mechanism (falling land prices erode both the marked value of
  land-backed collateral and new-borrowing capacity against it, and are explicitly named by
  multiple sources as compromising "the local government's ability to repay debt and eroding the
  collateral values of LGFVs") is well attested `[2-SOURCE]`. A specific CNY or percentage
  collateral-shortfall estimate at a stated land-price-decline assumption is not — and none is
  offered here in its place. Note also that national land *prices* (as opposed to land *revenue*
  or land *volume*) are the single most misleading series in this entire program per
  `b2-land-national.md`'s own headline finding: composition effects (a shrinking pool of expensive
  megacity parcels) have kept the *reported* national average land price roughly flat to rising in
  some years even as the true national average, adjusted for composition, has been falling — so a
  clean "30% land-price fall" input is itself contested at the data level before any collateral
  calculation could even begin.

## 7. The 1994 tax-sharing reform and the "land finance" (土地财政) critique

**The reform**: China's 1994 tax-sharing reform (分税制改革, prepared 1992-93, implemented 1994)
recentralized the collection of major taxes (notably VAT) to the central government while leaving
expenditure responsibilities — infrastructure, education, and much of social spending — with
localities, opening a persistent vertical fiscal gap between local revenue and local spending
obligations `[2-SOURCE — Wikipedia's Tax-Sharing Reform of China 1994 entry; OECD Economics
Department Working Paper No. 1030, "The System of Revenue Sharing and Fiscal Transfers in China"]`.
The conventional, widely repeated narrative is that land finance emerged directly as localities'
response to this reform.

**The complication, from peer-reviewed work**: an article in *The China Quarterly*, "The Origins
of Land Finance: Local Resistance and Top-Down Imposition" (Cambridge Core; this session's search
snippets did not surface the author's name with confidence and none is guessed here — cited by
title/journal/URL only), argues the simple causal story is wrong on timing: **local governments did
not turn to land finance immediately after 1994** — they began selling land at market/monopoly
prices only in the early 2000s, driven by an anti-corruption campaign (targeting under-the-table
land allocation) that made public, market-price land auctions a political necessity, not by the
1994 revenue shock itself. The same paper documents the land-revenue share of local on-budget
revenue rising from under 10% (2000) to over 50% (2003) — a genuinely fast take-off, but one dated
roughly a decade after the reform usually blamed for it — and frames the central government as an
active, top-down co-architect of the land-centric growth model, not merely an absent landlord that
left localities to improvise `[1-SOURCE — this specific paper; its central claim is corroborated
in direction, though not in every detail, by the general academic consensus that land finance
reflects a more complex institutional bargain than a single 1994 shock]`.

**The pro-land-finance defense, named**: **Zhao Yanjing (赵燕菁)**, a prominent Chinese urban
economist, argues in his widely-read and widely-contested 2014 article "土地财政：历史、逻辑与抉择"
("Land Finance: History, Logic and Choice") that land finance was a **"great institutional
innovation"** (伟大的制度创新) — land revenue functioned as *finance* (raising capital against
future value) rather than ordinary current fiscal income, letting local governments accumulate
capital at a speed that made China's compressed-timescale infrastructure build-out (high-speed
rail, airports, at scales exceeding initial planning) possible. His piece is reported to have
sparked substantial academic criticism, which he has characterized as containing only "a few"
critiques of genuine scholarly value `[2-SOURCE for Zhao's argument and its reception; his own
assessment of the critiques' quality is his characterization, not independently verified]`.

**Named critics — a genuine gap.** This session searched specifically for individually-named
scholars offering the critical counter-case (candidates searched: Tao Ran, Zhou Feishou, Chen
Zhiwu, Yao Yang, Andrew Batson) and could not surface clearly attributed, quotable critical
arguments from any of them meeting the corroboration bar in English-language search results. Chen
Zhiwu (HKU) surfaced only as a general public-intellectual profile with no located quote on land
finance specifically. **The critique of land finance as unsustainable is well attested in aggregate
academic literature** — a documented Kuznets-curve framing (land finance helps growth short-run,
suppresses secondary/tertiary-sector development and risks an early-deindustrialization effect
long-run) and a reported majority-scholar view that land finance should be gradually phased out as
urbanization completes, not abruptly abandoned `[2-SOURCE for the aggregate literature framing]` —
but is not tied to specific named individuals in what this session could source. This is stated as
a gap rather than resolved by attribution guesswork.

## 8. The Third Plenum (July 2024) and 2025-2026 fiscal-reform announcements: actual vs. announced

**Third Plenum, 15-18 July 2024** — the Central Committee's "Decision" contained 300+ reform
measures; the specific fiscal-federalism commitments relevant here `[2-SOURCE]`:
- A commitment to **"accelerate building a fiscal system compatible with Chinese modernization"**
  and grant localities greater **"autonomous fiscal capacity"** — more tax sources, expanded
  taxation-management authority (Bloomberg; APCO; The Diplomat).
- The single most concrete structural proposal: **shift the consumption tax's collection point
  further down the supply chain (toward the point of retail/final consumption) and progressively
  assign it to local governments** — converting what is currently mostly a central/production-stage
  tax into a shared or local revenue source explicitly designed to be less land-dependent (EY;
  PwC's own summary of the Decision).

**What has actually been delivered vs. what remains an announced direction:**
- **Delivered and verified**: the debt-swap mechanics (§3) — a concrete, executed, already
  measurably-progressing programme (14.3tn → 6.5tn hidden debt, 2023-2025).
- **Delivered, incremental**: central transfer growth (CNY 7.44tn 2019 → CNY 10.34tn 2025,
  `b2-land-national.md`) and modest special-bond quota increases (CNY 3.8tn 2023 → CNY 3.9tn 2024).
- **Announced, not yet delivered**: the consumption-tax devolution to localities remains a stated
  direction ("steadily assigning") with **no announced firm implementation date** found in this
  session's searches. The **property tax** — arguably the reform Third Plenum-era commentary most
  wanted to see attached to genuine local fiscal autonomy — remains stuck at the pilot-only stage
  first authorized in October 2021, explicitly shelved since March 2022 "because introducing it
  during a price crash was judged destabilizing" (`b2-land-national.md`'s own finding, independently
  corroborated here: no source in this session's separate searches found any update moving this
  status forward into 2025-2026) `[2-SOURCE across the two independent search efforts]`.
- **2025-2026, forward-looking only**: China's vice-premier signaled, and the 15th Five-Year Plan
  (2026-2030) reportedly incorporates as a stated objective, an intent to "increase local
  governments' discretionary fiscal resources" and have the central government take on a larger
  share of national fiscal outlays — a plan-level aspiration as of this writing, not yet a
  specific, dated, implemented mechanism `[1-SOURCE — SCMP]`.

**Net assessment, stated plainly**: what has changed for local-government finance since July 2024
is almost entirely on the *liability* side (debt refinancing, executed and working on its own narrow
terms) and the *transfer* side (central-to-local flows, growing but not separately quantified as a
land-revenue offset). The *revenue-base* side — the structural fix the fiscal-federalism critique
actually calls for — remains, as of 2026-09-11, an announced direction (consumption tax) or a
shelved pilot (property tax), not a delivered reform.

## 9. What replaced land revenue: composition of the shift

This question is answered in depth, and with more precision than this session's own independent
search could achieve, in this programme's already-booked `b2-land-national.md` (§Q5, "What replaced
the lost land revenue?"), which this dossier cites rather than duplicates. Its finding, restated
because it is directly relevant to the LGFV question: **four channels were found, and none is a
clean, quantified, like-for-like replacement of the lost operating revenue**:
1. **Central-to-local transfers** — CNY 7.44tn (2019) → CNY 10.2037tn (2024, budgeted) →
   CNY 10.3415tn (2025) — a genuine, growing net-new inflow, but not separately decomposed by any
   source into "how much specifically offsets the land-revenue hole" versus other drivers (VAT
   revenue-sharing changes, disaster relief, equalization formulas).
2. **Special-purpose bonds** — quota raised to CNY 3.9tn (2024) from CNY 3.8tn (2023) — but these
   finance *capital expenditure* that land-sale proceeds used to fund; they are debt (must be
   repaid), not a revenue-side substitute, and sit in the same government-fund budget land revenue
   itself sits in.
3. **The November 2024 debt-swap package (§3 above)** — explicitly a liability operation
   (reclassifying existing hidden LGFV debt onto cheaper government bonds), not new revenue.
4. **State-asset sales/securitization** — real and growing (Hubei's own stated slogan: "turn all
   state-owned resources into assets, and all state-owned assets into securities"; China's total
   ABS market issuance reached ~CNY 2.03-2.3tn in 2024) but **not separately sized as a
   land-revenue-replacement figure specifically** — the CNY ~2tn ABS figure is the *entire* Chinese
   structured-finance market (consumer credit, auto loans, and more, included), not a
   state-asset-only slice. `b2-land-national.md` explicitly flags this as `[VERIFY — not separately
   quantified]`, and this session's own independent search corroborates the qualitative point
   ("very few local governments have resorted to selling assets at large scale") without finding a
   cleaner aggregate figure either.
5. **Property tax** — the one instrument that could structurally replace land revenue on a
   recurring basis — remains shelved (§8 above).
6. **Existing property-related taxes did NOT step up**: 2023 MOF data shows deed tax, property tax
   (existing pilot), urban land-use tax, and land value-added tax combined run to roughly CNY
   1.85tn/year — smaller than a single year's *decline* in land-transfer income (2022's y/y drop
   alone was CNY 2.02tn) — and land value-added tax (-16.6% y/y) and farmland-occupation tax
   (-10.4% y/y) are themselves transaction-linked and falling for the same underlying reason land
   revenue is falling. These are a co-moving casualty of the downturn, not a replacement channel
   (`b2-land-national.md`).

**Synthesis for the LGFV question specifically**: the fiscal gap left by the land-revenue collapse
is being bridged almost entirely by *more borrowing* (special bonds, the debt-swap programme) and
*more central redistribution* (transfers), not by new indigenous local tax revenue. This matters
directly for LGFV credit quality: a locality whose land revenue has fallen and whose replacement
inflows are themselves debt or transfer-dependent has a structurally weaker, not stronger, capacity
to backstop its LGFVs than the pre-2021 land-finance model provided, even where the specific
"hidden debt" accounting line has improved.

## 10. Is there a credible path to resolution? Arguments on each side, named

**For a credible/manageable path:**
- **Official framing (Pan Gongsheng/PBOC, MOF)**: the swap programme is working on its own terms —
  hidden debt down from 14.3tn to 6.5tn in two years, an estimated CNY ~600bn in interest savings
  over five years, and repeated official language that risks are "controllable."
- **S&P Global's own assessment**: the November 2024 programme "is a good start" — genuinely
  reduces near-term rollover risk, lowers funding costs, and extends maturities, which is a real
  and measurable improvement in the shortest-horizon risk (a payments crisis in 2024-2026) even if
  it does not resolve the longer-horizon structural question.
- **The reform pipeline exists on paper**: Third Plenum's consumption-tax-devolution commitment and
  the 15th Five-Year Plan's "autonomous fiscal capacity" language show the center has, at least
  declaratively, identified the root cause (the vertical fiscal gap since 1994) rather than only
  treating the LGFV-leverage symptom.
- **Structural fiscal space**: China's central-government debt/GDP remains low by international
  standards, its debt is overwhelmingly domestically held and denominated in its own currency, and
  Beijing retains — as the Atlantic Council itself puts it in a piece explicitly about this
  topic — significant room to keep "extending and pretending" without facing an external
  funding-market crisis of the kind that forces resolution on other sovereigns.

**Against / skeptical:**
- **Michael Pettis (Carnegie Endowment)**, in two separate, explicitly-titled 2025-2026 pieces:
  "Using China's Central Government Balance Sheet to 'Clean Up' Local Government Debt Is a Bad
  Idea" (Aug 2025) and "Who Paid for China's Last Debt Cleanup, and Who Will Pay for the Next?"
  (Aug 2026). His core argument: **"moving bad loans from one balance sheet to another does not
  eliminate them... losses never disappear, even when they appear to"** — the real, unresolved
  question is *who absorbs the loss* (households, banks, the central government, or some
  combination), and no announced programme yet answers that question; it only changes which
  balance sheet is currently holding the liability.
- **Capital Economics**: the debt swap is a "band-aid" — it treats the liquidity symptom, not the
  structural revenue shortfall that keeps reproducing the problem.
- **S&P Global, in its own separate analytical voice** (its Sep 2024 piece, distinct from its "good
  start" note on the swap programme itself): **"Buying Time Is Buying Bad Habits"** — the same
  institution that credits the programme's near-term risk reduction explicitly warns, in its own
  words, that the programme substitutes time for the harder reforms (revenue-base restructuring,
  hard-budget-constraint discipline on new LGFV borrowing) that would actually resolve the
  underlying problem.
- **Aggregate-leverage evidence (East Asia Forum, Sep 2025, "China's debt reckoning")**: total
  social financing rising from 303% to 309% of GDP (end-2024 to mid-2025) even as the specific
  "hidden debt" line item improves is offered as evidence that debt is being reclassified and
  relocated system-wide faster than it is being retired — i.e., the improvement in the
  headline-tracked metric may partly reflect where the accounting boundary is drawn, not only
  genuine deleveraging.
- **Rhodium Group's broader "fiscal decay" framing** ("China's Harsh Fiscal Winter," "The Myth of
  China's Fiscal Space") argues the fiscal space China's optimists point to is itself smaller than
  headline central-government-debt ratios suggest, once LGFV and other off-budget liabilities are
  properly consolidated into the sovereign's true balance sheet.
- **The structural root cause remains open**: as §8 and §9 document, the reform that would
  genuinely fix the vertical fiscal imbalance opened in 1994 — durable, tax-base-level local
  revenue (consumption tax devolution, property tax) — is either a stated future direction with no
  firm date, or a five-year-shelved pilot, as of this writing.

No verdict is offered here; both sets of arguments are presented with their named sources per the
task's explicit instruction, and the desk's own read (§3, "not in tension with each other") is that
the disagreement is less about the facts — both sides largely agree on the same swap-programme
numbers — than about which time horizon and which balance sheet one chooses to evaluate them
against.

---

## Gaps and cautions

- **The verification ceiling stated in `china-property-plan.md` §0a applies in full**: every figure
  in this dossier is a WebSearch-snippet reconstruction of a primary source; WebFetch could not
  reach a single primary document (IMF Article IV PDFs, MOF releases, PBOC speech transcripts, the
  China Quarterly article itself) to pin an exact sentence. Where secondary outlets disagree on the
  same primary report's own number (the IMF's LGFV-debt figure being reported as anywhere from 60tn
  to "over 70tn" across outlets covering the same Article IV cycle), that disagreement is reported
  as a range with the caveat stated, not resolved by picking one.
- **No current CICC total-LGFV-debt estimate could be sourced.** The only CICC figures found are a
  2009-2011 vintage bank-loan-balance estimate, more than a decade stale and not comparable to the
  2023-2025 figures from IMF/Goldman/Rhodium/S&P/PBOC used elsewhere in this dossier. The task's
  "at least three named sources" requirement is met by IMF, Goldman Sachs, Rhodium Group, S&P
  Global, and Pan Gongsheng/PBOC instead.
- **No single national percentage for "LGFVs unable to cover interest from operating cash flow"
  could be corroborated to two sources.** §2 presents the available proxies (an unconfirmed ~105%
  industry-average coverage ratio, the Tianjin case, and a Moody's SOE-wide — not LGFV-specific —
  statistic) explicitly as proxies, not as a direct answer.
- **No source quantifies what a specific land-price decline (e.g., 30%) does to LGFV collateral
  coverage.** The mechanism is well attested qualitatively (§4, §6); no CNY or percentage
  collateral-shortfall estimate at a stated price-decline assumption was found or is offered.
- **The 2013 NAO 37%-land-collateral figure is 13 years stale**; no more recent comprehensive
  official audit of the collateral composition of local debt was found in this session.
- **The author of the key *China Quarterly* "Origins of Land Finance" paper is not named here**
  because this session's search snippets did not surface the author's name with confidence, and no
  name is guessed. The paper is cited by title, journal, and URL only.
- **Named individual critics of the land-finance model (as distinct from its aggregate academic
  critique) could not be sourced** despite five separate targeted search attempts (Tao Ran, Zhou
  Feishou, Chen Zhiwu, Yao Yang, Andrew Batson); this is reported as a genuine search-coverage gap,
  not as evidence that no such named critics exist in the literature.
- **The Zhongzhi/Zhongrong trust collapse is presented as adjacent to, not confirmed as part of,
  the LGFV non-standard-default record** — no source found in this session directly ties Zhongzhi's
  specific losses to LGFV-issued (as opposed to property-developer-issued) trust products; treating
  it as an LGFV default would be a definitional error the task explicitly warns against.
- **The Goldman Sachs CNY 94tn (2023) total-local-debt figure rests on a single outlet** (Asia
  Financial) and could not be independently cross-checked against a second source this session;
  it is retained in the table, tagged accordingly, because it is directly attributed to a named
  source (satisfying the task's sourcing requirement) rather than discarded.
- **The IMF's "augmented debt" 124%-of-GDP figure's exact as-of date and originating document could
  not be pinned to a single dated release**; it is reported via a secondary synthesis (East Asia
  Forum, Sep 2025) citing IMF methodology rather than a directly quoted IMF sentence.
- This dossier deliberately does not attempt to independently re-derive the MOF land-revenue series
  (peak, decline, replacement channels) already established with greater precision in this
  programme's own `b2-land-national.md` — duplicating that work with a noisier, independently
  re-searched version would have been strictly worse evidence for the same conclusion, and the
  desk's process note on this programme is to build on already-booked work rather than re-run it.
