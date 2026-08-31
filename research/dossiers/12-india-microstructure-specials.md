# Dossier 12 — India Microstructure and Special Situations

Workstream owner: research analyst · Phase: research-only, no data/code/backtests.
Complies with `research/CONTRACT.md` v0.1 and assumes all `OPEN_QUESTIONS.md` defaults — notably
**Q2** (hedge-only: long-only cash equities, shorts only via index futures/options — no single-stock
shorts, which rules out the classic US "short into lockup expiry / short the index-deletion" trades
as directly implementable), **Q3** (index-futures leverage overlay only), **Q4** (index options +
futures hedge set only, no single-stock options), and **Q10** (special situations = a **capped Tier-B
satellite sleeve in the aggressive book only**, rules frozen at inception).

**Session constraint, stated up front, per the disclosure convention already established by sibling
Workstreams 01/05/08 in this program.** This workstream's `WebSearch` allocation was drawn from a
program-wide shared budget of 200 calls; by the time this workstream ran, **the budget was already at
200/200 — zero searches executed, not even one.** `WebFetch` was tested against eleven domains
(sebi.gov.in, nseindia.com, en.wikipedia.org, papers.ssrn.com, arxiv.org, rbi.org.in, moneycontrol.com,
duckduckgo.com, bing.com, google.com) and returned `EGRESS_BLOCKED` or an equivalent failure on
**every single one** — a stricter block than Workstream 05 encountered (05 got several fetches through
before its own budget ran out). **No live source was verified in this session.** Consistent with the
contract's fallback protocol ("if you cannot verify, keep the finding and tag it `[VERIFY]`"), every
citation below drawn purely from pre-cutoff (Jan 2026) trained knowledge is tagged `[VERIFY]` even
where confidence is high (classic, decades-old, extremely well-cited papers). Two mitigations were
used instead of a fresh search: (1) cross-referencing overlapping facts that **sibling dossiers did
verify earlier in this session's shared budget** (Workstream 01 on ASM/GSM cadence, MWPL/F&O-ban
mechanics, and a specific Indian index-inclusion citation; Workstream 05 on STT/exercise-STT/T+1
figures; Workstream 02 on promoter-pledge papers) — these are marked "cross-verified via WS0x" and
carry that dossier's verification status, not a fresh one; (2) explicit, conservative haircuts and
wide ranges wherever a point figure could not be confirmed. **Recommend a follow-up verification pass
once search budget is available** — flagged again in §7.

---

## 1. Findings and literature

**F1. IPO underpricing / listing-day pop, India, long-run academic base.** Madhusoodanan &
Thiripalraju (1997), *"Underpricing in Initial Public Offerings: The Indian Evidence,"* Vikalpa
22(4) — one of the earliest systematic India studies, covering the pre-book-building, fixed-price-era
IPO regime (roughly 1992–1995); reports average first-day underpricing in a high double-digit to
triple-digit range, an order of magnitude larger than developed-market averages of the same period,
attributed to fixed-price allotment mechanics that left almost no price-discovery role for the
market. `[VERIFY: exact %, exact sample window]`. Marisetty & Subrahmanyam (2010), *"Group affiliation
and the performance of IPOs in the Indian stock market,"* Journal of Financial Markets 13(1) —
larger, more recent sample (into the 2000s book-building era); central finding is that
business-group-affiliated IPOs are underpriced **less** than standalone-firm IPOs (group affiliation
functions as a certification/reputation mechanism reducing the information asymmetry that underpricing
compensates for), and post-listing long-run performance differs by affiliation status. `[VERIFY]`.
Jay Ritter's (University of Florida) international IPO-underpricing country table, widely cited in
the IPO literature, lists India among the highest average-initial-return countries globally in
its pooled sample spanning the fixed-price era — a figure on the order of **80–90% average initial
return**, which is a fixed-price-era artifact, not representative of the 2000s–2020s book-built
regime. `[VERIFY: precise figure and sample years — this is drawn from memory of a frequently-cited
table, not confirmed this session]`. Net read: India's headline "IPO pop is huge" reputation is
**partly a stale artifact of the pre-1999 fixed-price allotment regime**; the modern book-built
regime (SEBI ICDR Regulations, price band + anchor-investor mechanism) shows materially smaller,
though still economically large and highly right-skewed, listing-day gains — order of magnitude
20–40% average with a long right tail (some SME and small mainboard names >100%) and a left tail of
large, "marquee" IPOs listing flat or below issue price (e.g., mega-IPOs where anchor demand was
driven by index-inclusion expectations rather than genuine scarcity). `[VERIFY: current-regime
average]`.

**F2. Long-run IPO underperformance — the global base result and why it likely doesn't transfer
cleanly.** Ritter (1991), *"The Long-Run Performance of Initial Public Offerings,"* Journal of
Finance 46(1):3–27 — finds US IPOs underperform matched non-issuing firms by roughly **15–30% over a
3-year buy-and-hold window**, concentrated in "hot issue" periods and growth/small-cap names.
`[VERIFY: exact %]`. Brav & Gompers (1997), *"Myth or Reality? The Long-Run Underperformance of
Initial Public Offerings,"* Journal of Finance 52(5) — important qualifier: once returns are
benchmarked against size- and book-to-market-matched portfolios (rather than the market index), most
of the "IPO underperformance" anomaly is subsumed by the well-known small-growth-stock
underperformance pattern; it is **not a clean, IPO-specific anomaly** but largely a restatement of the
value/growth and size effects applied to a sample that happens to be issuer-heavy. `[VERIFY]`.
**Design implication, stated explicitly per the contract's "why does this survive being known"
test**: a standalone "short IPOs 6–36 months out" rule has a **weak, contested survival argument** —
it looks like it is mostly value/quality doing the work, which is already a planned core sleeve in
the moderate/factor book (Workstream 02). Treating "recently listed, no profitability history, high
valuation" as an *input to* the existing value/quality composite (a fresh-issuance / newly-listed
flag lowering quality-composite score until a track record accrues) is defensible; a dedicated
"IPO short" sleeve is not, and in any case is foreclosed by the hedge-only mandate (Q2) since India
single-stock shorting requires SLB borrow that is thin-to-absent for most recent small/mid IPOs.

**F3. SEBI study on retail/anchor IPO "flipping" behaviour.** Widely reported in Indian financial
media (approx. 2023–2024 vintage) is a SEBI analysis of allotment-to-exit trading patterns finding
that a large share of individual (retail/HNI) investors who receive IPO allotment **sell within a
short window of listing — commonly cited as roughly 50% exiting within one week and a majority within
one month**, and a separate finding that anchor investors, once their lock-in tranche opens, sell a
material share of their allotment promptly rather than holding as "long-term" institutional capital
the anchor mechanism was designed to signal. `[VERIFY: exact SEBI report title, publication date, and
percentages — this is recalled as a well-covered media story, likely a SEBI DERA working paper or a
SEBI board-memo-linked study, but the citation could not be run down without search this session.
This is the single most important verification item in this dossier — flagged again in §7]`. The
mechanism this implies for design purposes does not depend on the exact percentage: **IPO allotment
itself is a lottery for oversubscribed issues** (retail category allotment is by proportionate draw,
not by order size), so "buy the IPO pop" is **not a controllable, scalable institutional strategy** —
a proprietary book cannot reliably obtain allotment at will, and size obtained (when it happens) is
capped by category-wise reservation limits, not by capital deployed. This is a hard **capacity/
implementability constraint**, not a decay argument: the edge may be real but the entry mechanism is
structurally lottery-gated, so it cannot be sized as an institutional sleeve. What *can* be
implemented at institutional size is trading the **secondary-market drift after listing** (buying or
avoiding in the weeks following listing, once shares are freely tradeable) — this is a momentum/
quality-composite question, not an "IPO allotment" strategy, and should be folded into the existing
momentum and quality sleeves' universe-inclusion rules rather than built as a separate module.

**F4. SEBI anchor-investor lock-in structure (30/90-day split).** SEBI's ICDR Regulations amendment
(recalled as a 2022 circular) split the anchor-investor lock-in from a single 90-day block into
**two tranches: 50% of anchor allotment released after 30 days, the remaining 50% after 90 days** —
explicitly designed to reduce the "cliff" selling pressure that a single 90-day unlock date used to
create, by spreading it across two dates. `[VERIFY: exact circular date/number — recalled with high
confidence on substance, not on citation precision]`. Mechanism: this is a textbook example of a
**regulator directly defusing a known market-microstructure edge** (a predictable, calendar-scheduled
supply event) *before* a systematic strategy could be built around it at scale — the two-tranche
design is explicitly a decay-inducing regulatory change, dated after the single-cliff version had
presumably already been observed and discussed in practitioner circles. Net effect for us: the
30-day and 90-day anchor-unlock dates remain **known, public, mechanical supply-event dates** (every
mainboard IPO's anchor allocation and lock-in dates are disclosed in the prospectus / RHP), so they
remain usable as a **risk-reduction, not return-generating, input**: reduce/avoid new entry into a
recently-listed name in the days bracketing its 30-day and 90-day anchor unlock, rather than try to
harvest a short around it (foreclosed by Q2 in any case for single stocks).

**F5. Mainboard vs. SME IPO — a two-tier market, and the SME tier is not institutionally investable.**
SME IPOs list on the NSE Emerge / BSE SME platforms under a lighter-touch disclosure and eligibility
regime (smaller minimum-lot sizes but a high per-lot value — typically ₹1–2 lakh minimum application,
deliberately restricting the investor base to HNI/wealthy-retail rather than mass retail), thinner
free float, and materially thinner post-listing secondary liquidity than mainboard names. SEBI's own
2024 regulatory actions are the most important evidence point here: the board tightened SME-IPO norms
in 2024 — recalled measures include capping/tightening the "general corporate purposes" use of
proceeds, restricting the use of IPO proceeds to repay promoter/related-party loans, tightening
related-party-transaction disclosure, and (in a further Dec-2024-vintage consultation) proposing
additional profitability/track-record eligibility thresholds — **explicitly in response to observed
price manipulation, circular trading, and fund diversion in specific SME-listed names** (multiple
SEBI show-cause/investigation orders against individual SME issuers were reported through 2024).
`[VERIFY: exact circular dates and company names]`. **Design implication (stated plainly, feeding the
exclusion list in §6)**: SME IPOs are **excluded from the universe entirely, for both the factor book
and the special-situations sleeve** — not merely deprioritized. The reasons compound rather than
merely add: (i) free float and liquidity are too thin to exit a proprietary-book-sized position
without moving the price by multiples of the square-root-law estimate in Workstream 05; (ii)
SEBI's own 2024 enforcement pattern is direct evidence that a meaningful share of SME-tier listing
gains reflect promoter-linked manipulation rather than a real repricing a systematic strategy should
want exposure to; (iii) the NIFTY 750 (Nifty 500 + Nifty Microcap 250) universe as defined in the
mandate does not include the SME platforms at all — they sit outside both index families — so
including them would be an explicit, unargued departure from the frozen universe definition.

**F6. Lockup expiry — the classic US result.** Field & Hanka (2001), *"The Expiration of IPO Share
Lockups,"* Journal of Finance 56(2):471–500 — studies the mechanical, contractually-scheduled
(typically 180-day) VC/insider lockup expiration common to US IPOs; finds an abnormal return around
the expiration date on the order of **−1.5% to −3% in a narrow (multi-day) window**, materially larger
for venture-backed issuers than non-VC-backed, accompanied by a **volume spike (recalled magnitude
roughly +40%)** and an increase in short interest **in the days leading up to** expiration — i.e., the
effect is partially anticipated by sophisticated participants rather than a pure post-hoc surprise.
`[VERIFY: exact %, exact window, exact volume figure]`. **India-specific evidence**: no India-specific
academic citation for this exact mechanism could be produced with confidence this session
`[VERIFY: search for an India lockup-expiry study]`. The mechanism, however, transfers cleanly by
analogy and is *reinforced*, not weakened, in the Indian institutional setting for two reasons: (a)
India's promoter/anchor lock-in schedule is itself calendar-mandated and public (F4 above, plus
standard 6-month/1-year promoter lock-ins under ICDR), so the "known mechanical supply date" setup
Field-Hanka document is structurally present; (b) **SLB (Securities Lending & Borrowing) liquidity on
NSE is thin outside roughly the top 150–200 names**, meaning the "short into the unlock" trade Field-
Hanka implicitly assume is arbitrageable in the deep-borrow US market is **frequently not
implementable in India even for a book that were allowed single-stock shorts** — an institutional
constraint that should, if anything, **preserve** more of the pre-unlock drift in India than in the
US, because fewer participants can express the short. Since our mandate forecloses single-stock
shorts regardless (Q2), the actionable form is again risk-reduction only: treat scheduled
promoter/anchor lock-in expiry dates (public, from the RHP) as a reason to trim or avoid adding to
a held position, not a source of new alpha.

**F7. Index inclusion/exclusion — the foundational US debate.** Shleifer (1986), *"Do Demand Curves
for Stocks Slope Down?"* Journal of Finance 41(3):579–590 — S&P 500 addition sample; finds an
average abnormal return around **+3%** at announcement that is largely **permanent** (does not fully
reverse), interpreted as evidence against a flat, perfectly-elastic demand curve for a stock's shares
— i.e., evidence that index-fund and benchmark-hugging demand is itself price-relevant, not merely
a re-labeling of existing demand. `[VERIFY: exact %]`. Harris & Gurel (1986), *"Price and Volume
Effects Associated with Changes in the S&P 500 List,"* Journal of Finance 41(4):815–829 — same broad
event, opposite interpretation: finds a similarly sized (~3%) price jump on the addition's effective
date, but one that **substantially reverses within about two weeks**, consistent with a temporary
**price-pressure** story (index funds must transact on the effective date regardless of price, and
arbitrageurs who supply the liquidity are compensated by the subsequent reversal) rather than a
permanent demand-curve shift. `[VERIFY]`. Chen, Noronha & Singal (2004), *"The Price Response to S&P
500 Index Additions and Deletions: Evidence of Asymmetry and a New Explanation,"* Journal of Finance
59(4):1901–1929 — reconciles the two 1980s results with a longer, more careful sample: **additions
show a permanent price increase; deletions show only a temporary price decrease that reverses.** The
proposed explanation is "investor awareness" (a Merton-1987-style investor-recognition mechanism):
addition to a widely-followed index permanently raises analyst coverage and institutional ownership
(the stock becomes "known" to a wider investor base), while deletion does not symmetrically destroy
that awareness, so the deletion-side price effect is transient supply/demand noise rather than a
permanent re-rating. `[VERIFY: precise citation]`. Separately, the broader "index effect has decayed
over time in developed markets as arbitrage capital anticipates it" finding (associated with authors
including Petajisto, and consistent with the contract's general McLean-Pontiff framing) is directly
relevant: in the US, the 1990s S&P-inclusion premium of several percent has been documented to have
fallen toward roughly zero by the 2000s–2010s as index-arbitrage capital grew to anticipate and
pre-position ahead of announced changes. `[VERIFY: specific decay citation/authors — recalled as a
real, well-known finding, not confirmed by search this session]`.

**F8. Index inclusion/exclusion — India-specific evidence (cross-verified via Workstream 01).**
Workstream 01 (momentum/reversal) reports, from its own session-time search: **Selvam, Indhumathi &
Lydia (2012)** and related Indian studies of Nifty index reconstitution find that abnormal
**inclusion gains fade within roughly 60 days**, while abnormal **exclusion losses fade within roughly
10 days** — a materially *shorter-lived, more asymmetric-in-the-other-direction* pattern than the
Chen-Noronha-Singal US asymmetry (in the Indian sample, it is the *inclusion* effect that persists
longer, and the *exclusion* effect that decays fastest, opposite emphasis from the US "additions are
permanent" framing, though both studies agree the effects are transient/semi-transient rather than
purely permanent). This citation is treated as WS01's verification status (searched within this
session's shared budget before it was exhausted), not re-verified independently here. **MSCI India
rebalance flows** are the larger, more institutionally consequential India-specific version of this
same mechanism: India's weight within the MSCI Emerging Markets index has risen materially over
2020–2025 (falling China weight, rising India weight, plus foreign-ownership-limit and
free-float-adjustment mechanics specific to certain large caps), such that a single semi-annual or
quarterly MSCI review can now move **hundreds of millions to low billions of USD** of passive flow
into or out of an individual large-cap Indian name — well-publicized examples include large flow
estimates around Adani-group inclusions (2020, later reversed/adjusted post the 2023 short-seller
report) and Zomato/other new-economy inclusions post-IPO (2024). `[VERIFY: specific flow-size
figures]`. **Net read for design**: the India index-effect edge should be treated as **Tier B**
(multiple decades of semi-annual Nifty reconstitutions plus MSCI/FTSE reviews comfortably exceeds the
4-observation floor, likely exceeds 30 if pooled across index families — arguably borderline Tier A on
observation count, but the effect-size literature is thin enough in India specifically, and the
"decays with arbitrage capital" mechanism is well-established enough elsewhere, that Tier B with a
stated decay haircut is the honest call), with an explicit, **rising** decay assumption over the
design's 2026–2036 horizon as India's own passive/index-arb AUM continues to grow from its still-low
base (this is the mirror image of the US 1990s→2000s decay Petajisto-style evidence documents — India
today looks more like the US did in the 1990s on this dimension, meaning **some** edge should still be
extractable now, decaying over the coming decade as domestic passive AUM keeps compounding).

**F9. Promoter share pledging and crash risk (cross-verified via Workstream 02).** Workstream 02
already cites, from its own session search, "**Promoter Share Pledging and Downside Risk: Evidence
from Indian Listed Firms**" (recalled as a 2023–2025-vintage India paper, `[VERIFY: exact
author/venue]`) finding pledging positively associated with future crash risk and negatively with
financial performance, with pledging firms showing worse CVaR/left-tail outcomes. This dossier adds
the **event-driven framing** on top of WS02's factor-book framing: pledging is disclosed under SEBI's
SAST (Takeover Code) Regulation 31 encumbrance-disclosure rules **within a short, regulator-mandated
window of any pledge creation, invocation, or release** — a free, point-in-time, per-stock exchange
filing. The crash mechanism is mechanical and well-documented by case history rather than merely
statistical: when a promoter has pledged a large share of their holding against a personal/company
loan and the stock falls far enough to breach the lender's loan-to-value covenant, the lender can
**invoke the pledge and force-sell the collateral shares on the open market**, which pushes the price
down further, which can trigger further margin calls on any remaining pledged collateral — a
self-reinforcing cascade. Prominent, widely reported Indian cases fitting this exact mechanism include
Zee Entertainment (2019), Café Coffee Day / Coffee Day Enterprises (2019, following the founder's
death), Dish TV, Reliance Capital/Reliance Infrastructure/Reliance Communications (multiple episodes,
2018–2020), Cox & Kings (2019), Manpasand Beverages (2019), and Vakrangee (2018) — a working count of
roughly **10–15+ distinct, dated, promoter-pledge-driven crash episodes across 2015–2023** is
plausible from public reporting, which would clear the Tier-B observation floor (4–30) on its own,
independent of WS02's cross-country framing. `[VERIFY: exact count and dates — recalled from general
financial-press familiarity, not tallied from a source this session]`.

**F10. Insider (PIT) disclosure and bulk/block-deal signals.** SEBI's PIT (Prohibition of Insider
Trading) Regulations, 2015 require "designated persons" (promoters, KMP, and other insiders) to
disclose trades above a threshold, with the listed company obligated to disclose the trade to the
exchanges within a short window (recalled as within 2 trading days) — a free, per-stock, dated
disclosure feed. Separately, exchanges publish **daily bulk-deal and block-deal reports** (any single
trade or same-day-aggregated trades by one client crossing roughly 0.5% of a company's equity on the
bulk-deal definition, or meeting the larger block-deal negotiated-window threshold) — same-day, free,
per-stock, per-counterparty-category (where disclosed) data. International insider-trading-signal
literature (e.g., work associated with Seyhun in the 1980s, and Jeng-Metrick-Zeckhauser-era studies in
the 2000s) generally finds a modest but persistent abnormal return to following disclosed insider
*buying* (materially weaker or absent for insider selling, which has many liquidity-driven, non-
informative reasons). `[VERIFY: specific citations — recalled generically, not confirmed this
session]`. **Survival argument for India specifically**: (i) a genuine information/attention
asymmetry — the raw disclosure feeds are free and public but require scraping and per-stock
aggregation that most retail participants do not do systematically, though this is weaker for
large-caps where financial media and momentum-chasing retail apps already push bulk-deal
notifications; (ii) a **capacity argument that maps directly onto this book's own structure**: any
edge that survives is most likely to survive in the **rank 500–750 tail**, where financial-media and
crowd attention is thinnest and where the aggressive book (the only book mandated to hold this rank
range) is also the only book small enough in AUM (₹100–250cr) to size a position off a single bulk/
block disclosure without moving the name itself. This is a clean fit to the special-situations
sleeve's aggressive-book-only default (Q10).

**F11. Buyback / open-offer / delisting arbitrage — capacity is the whole story.** SEBI moved to
phase out the open-market (stock-exchange-route) buyback method in favour of **tender-offer-only**
buybacks (board decision recalled as announced November 2023, with a transition completing around
2025) — a transparency-motivated reform that also **caps how much stock any single tender buyback can
absorb** (small-shareholder reservation categories exist, and total buyback size is itself capped as a
percentage of net worth/reserves under the Companies Act). `[VERIFY: exact transition date]`. Buyback-
tender arbitrage (tendering shares at a premium to prevailing market price, historically favourable
tax treatment for the shareholder since the Finance Act 2020 shifted buyback tax liability to the
company) is a genuine, small, largely mechanical risk premium (compensation for proration
uncertainty and tender-timeline risk) — but individual buyback sizes (commonly ₹100–3,000cr) and
per-participant proration caps mean the **entire strategy is capacity-limited by design**, appropriate
only for the aggressive book's satellite allocation, never scalable to the moderate or conservative
books. **Open-offer arbitrage**: mandatory open offers are triggered under SEBI's SAST Regulations
when an acquirer's stake crosses the 25% trigger threshold (or on any change of control), requiring a
minimum 26% public open offer at a regulator-defined offer price; the spread between prevailing market
price and the announced/likely open-offer price is arbitrageable but carries **SEBI-approval-timeline
risk and competing-offer risk**. **Delisting arbitrage**: under SEBI's Delisting Regulations (2021
amendment), a voluntary delisting requires reverse book-building price discovery **and** (post-2021)
approval by a majority of public (non-promoter) shareholders, with a minimum 90% post-offer promoter
stake required for the delisting to succeed — this creates genuine binary/fat-tail risk (a well-known
recent example is Vedanta's failed delisting attempt), so the "spread to expected reverse-book-build
price" is compensation for real event risk, not free money. `[VERIFY: exact regulatory dates and
Vedanta timeline]`. All three (buyback/open-offer/delisting) share the same design conclusion: **small,
real, capacity-capped risk premia that fit only the aggressive book's satellite sleeve.**

**F12. Demergers and spin-offs.** Cusatis, Miles & Woolridge (1993), *"Restructuring Through
Spinoffs: The Stock Market Evidence,"* Journal of Financial Economics 33(3):293–311 — finds spun-off
units and their former parents, combined, earn statistically significant positive abnormal returns
over the **following ~3 years** (a figure on the order of a few tens of percent cumulative,
`[VERIFY: exact %]`), and traces most of this to a **much higher subsequent takeover/acquisition rate**
for spun-off units and parents versus size/industry-matched control firms (recalled as roughly 1-in-3
being acquired within several years, versus a much lower base rate for the control sample)
`[VERIFY: exact rate]`. The proposed mechanisms — forced index-fund/institutional selling of a newly
small, low-float spinoff that no longer meets the parent index's inclusion criteria (a structural,
non-informational selling pressure creating temporary undervaluation), plus improved managerial
incentive alignment and capital-allocation clarity once a business unit is separately managed and
separately valued — are structural, not merely "it backtests well," so the mechanism itself clears the
survival-argument bar. **India-specific evidence is thin at the academic level**: no dedicated
India demerger-event-study citation could be produced with confidence this session
`[VERIFY: search needed]`, though India has a large, well-documented population of candidate events
across two decades — the Reliance Industries 2005–06 demerger (into Reliance Industries, Reliance
Communications, Reliance Infrastructure, Reliance Power, Reliance Capital), Bajaj Auto's 2008 three-
way split (Bajaj Auto / Bajaj Finserv / Bajaj Holdings), L&T Finance Holdings and L&T Technology
Services carve-outs, Raymond's real-estate/lifestyle demerger (2024–25 vintage), ITC's hotels-business
demerger (2025), and the broader Adani Group's sequential listed-entity separations, among many
others. This gives a **plausible Tier-B-sized event population (20–40+ mainboard demergers over
2000–2025)** for a data-phase event study, but the tier assignment here is provisional pending that
study, not yet earned by existing literature.

---

## 2. India-specific evidence

This section consolidates the India-specific institutional detail threaded through §1 and adds the
pure-microstructure items the workstream brief calls out directly (ASM/GSM, circuit bands, derivative
bans, T+1/peak-margin, the 2024–25 index-derivatives regime, STT-on-exercise).

**ASM/GSM surveillance — mechanics and consequence for implementability.** Two overlapping but
distinct SEBI/exchange surveillance frameworks apply to individual stocks showing abnormal price/
volume behaviour without a commensurate fundamental trigger. **ASM (Additional Surveillance Measure)**
has short-term and long-term variants triggered by criteria such as high-low price variation,
client concentration, and volatility over rolling windows; consequences escalate through stages and
can include additional margin requirements up to 100% of trade value and tightened price bands.
**GSM (Graded Surveillance Measure)** is the more severe framework (originally targeted at suspected
shell/pump-and-dump companies), escalating through multiple stages that can include: trading permitted
only once a week (rather than daily), mandatory **trade-for-trade settlement** (every trade must
result in actual delivery — no same-day intraday squaring-off), an **Additional Surveillance Deposit**
held by the exchange, and a periodic call-auction mechanism replacing continuous trading entirely at
the most severe stage. Workstream 01 (cross-verified) reports that **ASM/GSM list reviews are now
monthly, tightened from a prior quarterly cadence** — the surveillance net is being tightened over
time, not loosened, which matters for how conservatively the exclusion rule (§6) should be set: a
name that is clean today in the rank 500–750 tail can be added to GSM with only a month's lag once its
price/volume pattern trips the criteria, so a static "exclude only names currently on the list" rule
is insufficient; the rule needs a forward-looking buffer (proximity-to-trigger monitoring), which is a
data-phase design task, not something resolvable in this research-only pass.

**Circuit limits / price bands — the 5/10/20% tiers and why they are a discontinuity, not a cost.**
NSE/BSE apply daily price bands to individual securities: for the most liquid, F&O-eligible large caps,
bands have moved toward **dynamic, wider, or no fixed daily band** in recent years (large caps trade
essentially unconstrained intraday); for the broad non-derivative mid/small/microcap universe —
precisely the rank 500–750 tail this book must hold in the aggressive book — **static daily bands of
5%, 10%, or 20%** (assigned per-stock by the exchange based on volatility/liquidity classification)
remain the norm, and ASM/GSM-flagged names can have these bands tightened further (to as low as 2–5%
per Workstream 05's cross-verified finding). The critical point for the factor/momentum book (echoing
Workstream 05's framing) is that this is **not a smooth cost to be added to a square-root-law impact
estimate — it is a discontinuity**: once a stock hits its lower band with no buyers at that price, the
stock **simply stops trading** at any price below the band for the rest of the session (and potentially
consecutive sessions, in a cascading decline). A momentum strategy holding a rank-600 name that
reverses sharply (the exact scenario the momentum-crash literature, e.g. Daniel-Moskowitz, warns
about) can find itself **unable to exit at all** on the worst days — precisely when exiting matters
most. **Quantified consequence, framed for the data phase (this is a measurement-method proposal, not
a completed measurement, per the research-only scope of this pass)**: build, from free NSE/BSE
bhavcopy data (closing price = band limit, zero or near-zero traded volume beyond the band-touching
trade), a per-stock, per-month **"band-lock frequency"** statistic — the fraction of trading days a
stock closed at or within a small tolerance of its price band with unfilled residual demand on the
book (approximable from bhavcopy's closing-price-vs-band-limit fields plus the exchange's published
circuit-limit master list) — and use its trailing 6–12 month value as (a) a **hard exclusion filter**
for any name whose band-lock frequency exceeds a data-phase-determined percentile of its own investable
universe (a quantile rule, not a fixed number, per the contract's no-magic-numbers principle), and (b)
an input to a **liquidity-adjusted position-sizing haircut** distinct from the pure ADV-based sizing
already used elsewhere, since a name can have perfectly normal average daily volume most days and still
carry a fat-tailed, band-triggered "cannot exit" risk concentrated in exactly the drawdown states the
mandate's drawdown constraint cares about most.

**Derivative (F&O) ban periods.** Cross-verified via Workstream 01: a stock enters an F&O trading ban
once open interest reaches 95% of its Market-Wide Position Limit (MWPL — defined, per WS01's
Oct-2025-vintage methodology note, as the lesser of 15% of free float or 65× average daily delivery
value, using a delta-based futures-equivalent OI calculation); the ban blocks **new** derivative
positions only (existing positions may be unwound, cash-equity trading is entirely unaffected). Given
this book's mandate (index-futures leverage overlay only, index options+futures hedge only — Q3/Q4
defaults, no single-stock derivatives), **F&O ban periods have no direct mechanical effect on this
book's own tradeability** — they matter only as a **contrarian positioning signal**: a stock repeatedly
entering ban (OI persistently pinned near the 95% MWPL threshold) is, by construction, a name with
unusually crowded speculative derivative positioning relative to its own free float, which is
plausible tail-risk information for a name the equity book might also hold. No rigorous published
study of this specific "repeated-ban as a contrarian/risk signal" mechanism could be produced with
confidence this session — **Tier C, narrative only, reduce-risk-only per the contract's Tier-C rule**,
until a data-phase event study is run.

**T+1 settlement and peak-margin rules as turnover mechanics.** Cross-verified via Workstream 05:
India completed cash-market T+1 settlement in January 2023 (with an optional T+0 pilot for a subset of
large caps beginning March 2024), shortening settlement float versus most developed markets — a
modest positive for capital recycling speed, not a cost-model change. Separately, SEBI's phased
**"peak margin"** framework (recalled as phased through 2020–2021, moving from 25% to 100% of
exchange-mandated margin collected upfront across four stages) ended the practice of brokers
extending intraday leverage well beyond exchange margin requirements; this raises the **effective
capital required per unit of gross exposure** for any high-turnover or short-holding-period strategy,
and imposes a short-collection penalty (recalled roughly 0.5%/day for shortfalls up to 1%, higher above
that) for any margin shortfall — a real, quantifiable cost that belongs in Workstream 05's cost-stack
model, not duplicated here, but flagged because it directly bears on the special-situations sleeve's
implementability: any event-driven trade held through a volatile window (a lockup-expiry-adjacent
trim, a bulk-deal-triggered entry) must be margin-funded at the full exchange rate from day one, with
no intraday-leverage cushion the pre-2021 market used to offer. `[VERIFY: exact phased dates/
percentages, not re-confirmed this session — cross-referencing Workstream 05's framing rather than
independently verifying]`.

**Index-options expiry regime after the SEBI 2024–25 curbs — best available read for 2026.** SEBI's
October 2024 circular (recalled title along the lines of *"Measures to strengthen equity index
derivatives framework for increased investor protection and market stability"*) introduced, in
phases through late 2024 and 2025: (a) rationalizing weekly index-options expiries so that **each
exchange offers only one weekly-expiring benchmark index product** (NSE retaining its flagship Nifty
weekly; BSE retaining Sensex weekly; the other index products — Bank Nifty, Fin Nifty, Nifty
Midcap Select, Bankex, etc. — moved to monthly-only expiry), sharply reducing the number of
weekly-expiry events per week market-wide; (b) an increase in minimum contract size (recalled roughly
₹5–10 lakh notional moving toward ₹15 lakh); (c) **upfront collection of the full options premium**
from option buyers (removing a source of intraday leverage in options buying); (d) removal of the
calendar-spread margin benefit specifically on the expiry day itself (raising margin, hence cost, for
calendar-spread positions that used to roll cheaply through expiry); (e) intraday (rather than only
end-of-day) monitoring of position limits. `[VERIFY: circular date/number and exact phase-in dates]`.
Separately recalled (with lower confidence): **exchanges were required to each pick a single weekly-
expiry weekday from a constrained set (Tuesday/Thursday), avoiding Monday/Wednesday/Friday**, spreading
market-wide expiry-day risk rather than concentrating it — with NSE's Nifty weekly and BSE's Sensex
weekly landing on different weekdays after this change (recalled as an implementation sometime in
2025). `[VERIFY: this specific weekday-assignment detail is the least confident recollection in this
dossier and should be checked first in any follow-up pass]`. **As of the current date (31 Aug 2026,
per system context), this regime should be the settled state** — no further major structural change to
the weekly-expiry framework is recalled as pending, though SEBI's F&O framework has been in a period of
frequent revision (2020 peak-margin, 2024 index-derivatives curbs, 2026 STT hike per Workstream 05's
verified finding) and a further tightening cannot be ruled out. **Relevance to this book**: none of this
changes the mandate's own hedge-instrument set (index options + futures only, Q4), but it is important
context for sizing the hedge-ratio sweep's cost assumptions (fewer weekly-expiry windows per month for
non-Nifty/Sensex products means a Bank-Nifty-beta hedge, if ever used, now rolls monthly rather than
weekly, changing its cost/convexity profile) and for interpreting the SEBI retail F&O loss studies
below.

**SEBI retail F&O loss studies — context for why "harvest options premium" is not a proposed edge
here.** SEBI published a widely reported study (recalled as January 2023, covering FY22, with a
follow-up update recalled as September 2024 covering FY24) finding that a large majority of individual
traders in the equity F&O segment **lose money in aggregate** — recalled headline figures on the
order of **~90% of individual traders showing net losses**, with **aggregate net losses in the tens of
thousands of crores of rupees per year**, growing across the update years. `[VERIFY: exact percentages,
exact rupee figures, exact report titles/dates — recalled as a well-covered story, not confirmed by
search this session]`. This is presented as **context, not a proposed signal**: the losing side of
this trade is overwhelmingly retail directional option-buying and naive short-premium selling; the
winning side is dominated by proprietary/FII derivatives desks already running sophisticated,
well-capitalized market-making and volatility-arbitrage books. There is no credible "capacity limit
keeps competitors out" or "structural mechanism" argument for a two-person team to extract this
specific retail-loss edge systematically — it is exactly the kind of "it backtests well because
retail loses money" claim the contract's governing principle (§5) treats as inadmissible without a
survival argument, and no such argument is offered here. **Design conclusion: the options book stays
hedge-only per Q4's default; this dossier does not propose an options-premium-harvesting sleeve.**

**STT-on-exercise trap (cross-verified via Workstream 05, extended here).** Workstream 05 verified
this session (via its own search) that under the live FY2026-27 schedule (effective 1 April 2026),
STT on the automatic exercise of an in-the-money index option at expiry is **0.15% of intrinsic
value**, charged to the option buyer; the prior schedule (effective 1 October 2024 through 31 March
2026) charged **0.125%** on the same intrinsic-value base. The trap WS05 identifies — and this dossier
extends to the special-situations sleeve's own hedge overlays — is that **letting a deep-ITM option
run to automatic exercise, rather than actively selling it before the close on expiry day, taxes the
full intrinsic value at expiry**, which can be many multiples of the original premium paid for an
option that has moved deep into the money; institutional desks in India routinely close ITM positions
before expiry specifically to avoid this. **Operating rule for this book's own hedge book (not a
special-situations finding per se, but recorded here since it directly affects any tail-hedge payoff
path)**: any modeled hedge-ratio sweep (0/25/50/75/100/125/150%, per Contract §3) must assume active
close-out of ITM index options before the final expiry session in the crash-scenario payoff path, and
must cost that payoff path at the exercise-STT rate only in the (presumably rare, forced) case where
close-out was not possible — modeling "STT on premium only" for the tail-hedge payoff, as WS05 notes,
understates realized cost exactly when the hedge is doing its job.

---

## 3. Decay and crowding assessment

Per finding, stated as the contract requires: mechanism (survives crowding) or numeric haircut.

| Edge/signal | Survival argument | Verdict |
|---|---|---|
| IPO listing-day pop (buying the pop) | None viable — allotment is a lottery, not a scalable entry (capacity/institutional constraint on the *entry* side, not a market-efficiency argument) | **Not implementable at institutional size.** Exclude as a strategy; the mechanism is real but uncontrollable. |
| Post-listing secondary drift (weeks post-listing) | Largely subsumed by size/growth/quality factors already priced elsewhere (Brav-Gompers 1997) — weak standalone survival argument | Fold into existing quality/value composite as a "newly-listed" flag (lower quality score pending track record); apply full McLean-Pontiff 26%/58% haircut to any standalone version. |
| Anchor/promoter lock-in expiry drift | (iv) Institutional constraint — the event is calendar-mandated and public, so it persists as a *risk fact* even though it is anticipated; regulator has already halved the "cliff" (30/90 split) precisely because it was becoming known | Risk-reduction input only (trim/avoid around known unlock dates); not a return source, and foreclosed as a short by Q2 in any case. |
| Mainboard index inclusion/exclusion (Nifty, MSCI, FTSE) | (ii) Capacity limit temporarily — India's own passive/index-arb AUM is still small relative to developed markets, so the "US 1990s" analogy implies a currently-extractable but **actively decaying** edge as domestic passive AUM compounds | Tier B, with an explicit **rising** decay haircut over the 2026–2036 design horizon — treat current effect size as an upper bound that shrinks year over year; re-estimate periodically in the data phase, do not freeze a single number for a decade. |
| Promoter share pledging as crash-risk flag | (iii)/(iv) Genuine mechanical risk (forced collateral liquidation cascades) plus institutional-disclosure-based information asymmetry — not a "backtests well" pattern, a structural leverage/margin-call mechanism | Durable; a mechanism-based signal survives crowding almost by definition (more capital watching for pledge-driven cascades does not remove the lender's contractual right to force-sell). No haircut proposed beyond ordinary estimation uncertainty; Tier B on cross-country + Indian case-count grounds. |
| Bulk/block-deal following, PIT insider-disclosure following (large-cap names) | Weak — large-cap bulk deals already receive heavy media/retail-app attention; likely substantially arbitraged already | Apply a large haircut (treat as close to McLean-Pontiff's 58% post-publication figure) for ranks 1–500; do not size meaningfully outside the rank 500–750 tail. |
| Bulk/block-deal following, PIT insider-disclosure following (rank 500–750 tail) | (ii) Capacity limit — thin attention + small absolute position sizes needed, matching exactly the aggressive book's own size ceiling | Tier B candidate for the aggressive-book satellite only; moderate haircut, not full McLean-Pontiff, since the "who else is big enough to bother" argument is a real capacity wall, not just an assumption. |
| Buyback-tender / open-offer / delisting arbitrage | (ii) Hard capacity limit by regulatory/structural design (tender sizes, proration caps, net-worth-linked buyback ceilings) | Durable but tiny; capacity-capped by construction, not crowding-decayed — appropriate only for the aggressive-book satellite, sized to available deal flow, never scaled up. |
| Demerger/spinoff long-run outperformance | (i)/(iv) Structural — forced index-fund selling of low-float spinoffs plus incentive-realignment and elevated takeover-rate mechanisms, replicated in multiple markets (though not yet in a dedicated India study) | Provisional Tier B (event count plausible, effect size unconfirmed for India) pending a data-phase event study; treat current sizing as a placeholder, not a frozen parameter. |
| F&O-ban-repetition as contrarian signal | None demonstrated — narrative only, no cited study | Tier C, reduce-risk-only per the contract's Tier-C rule; may not be used to add exposure. |
| Options-premium harvesting (retail-loss-driven) | None — no capacity, structural, or risk-premium argument distinguishes this book from the many already-professionalized desks on the other side of that trade | **Rejected outright.** Not proposed as a sleeve. |

---

## 4. Proposed parameters

| Name | Value/range | Source | Tier | Confidence | Decay assumption | What would change it |
|---|---|---|---|---|---|---|
| SME IPO universe inclusion | **0% — hard exclusion**, all books, all sleeves | F5; NIFTY 750 universe definition excludes SME platforms by construction | A (definitional) / B (liquidity+manipulation argument) | High | N/A — a scope rule | SEBI SME-tier reform materially improving disclosure/liquidity AND the mandate's universe definition being explicitly amended |
| Special-situations sleeve — book eligibility | **Aggressive book only** (₹100–250cr); 0% in moderate/conservative | Q10 default; F11 (capacity-capped by construction) | B (by mandate default) | High | N/A — a scope rule | Principal override of Q10 |
| Special-situations sleeve — capital cap | Provisional **≤10% of aggressive-book NAV**, satellite, aggregated across all special-situations sub-strategies | Analogy to Contract's other satellite caps (e.g., size sleeve 0–15% in WS02); no India-specific capacity study run this session | C (placeholder) | Low | Full re-derivation required | A data-phase capacity study sizing actual India deal flow (buybacks/open-offers/delistings/demergers per year) against this cap |
| Anchor/promoter lock-in trim window | Reduce or avoid adding to a position in the **±5–10 trading days around each disclosed 30-day and 90-day anchor unlock date**, and around disclosed promoter lock-in expiry dates | F4, F6 (Field-Hanka mechanism, adapted; exact window not India-tested) | C (narrative, mechanism-based) | Low-Medium | Reduce-risk-only, no haircut needed since it never adds exposure | An India-specific event study of the actual pre/post-unlock return pattern |
| Index-inclusion/exclusion positioning window | Trade only in the **announcement-to-effective-date window** for confirmed Nifty/MSCI/FTSE reconstitutions, sized by free-float-adjusted flow estimate, not a fixed % | F7, F8 | B | Medium | Rising haircut — treat as **shrinking year over year** as India passive AUM grows (no single frozen % given, per the no-magic-numbers rule); re-estimate each data-phase cycle | Direct measurement of India passive/index-tracking AUM growth rate and re-estimated effect size per reconstitution cycle |
| Promoter-pledge crash-risk flag | Any name with **pledge >X% of promoter holding** (X a data-phase-determined quantile of the pledge distribution, not a fixed number) triggers a quality-composite penalty and/or position-size haircut; a **new pledge invocation** disclosure triggers immediate review/exit consideration | F9; cross-ref WS02 | B | Medium-High | None proposed — mechanism-based, durable | A completed India event study quantifying the actual return pattern around pledge-invocation disclosures |
| Bulk/block-deal / PIT-disclosure signal | Rank 500–750 only; direction and size a data-phase design question (sign-rule/quantile-rank form only, no fixed threshold) | F10 | B (narrative + capacity argument), pending data-phase test | Low-Medium | Large haircut for ranks 1–500 (near-zero weight); moderate haircut for 500–750 | A purged/embargoed India backtest isolating rank-500–750 large-owner-disclosure events from rank 1–500 events |
| Buyback/open-offer/delisting arb allocation | Capacity-sized to **actual live deal flow**, not a fixed % — proposed as a residual "opportunistic" bucket inside the special-situations cap, sized deal-by-deal against available spread and proration-adjusted expected size | F11 | B | Medium | None beyond ordinary event risk (delisting-failure binary risk priced per-deal) | A tallied multi-year India deal-flow census (frequency, size, realized spread) from free exchange filings |
| Demerger/spinoff holding rule | Hold parent + spun-off entity through the first 3–12 months post-listing of the new entity by default (no forced sale on technical index-exclusion of the small spinoff), reassessed via the standard quality/value composite thereafter | F12 (Cusatis-Miles-Woolridge mechanism) | C, provisional B pending India study | Low-Medium | Full re-derivation pending India event study | Completed India demerger event-study registry (see §6) |
| ASM/GSM/band-lock exclusion filter (factor book, ranks 500–750) | Exclude any name whose trailing 6–12m **band-lock frequency** exceeds a percentile of its own universe's distribution (quantile rule, no fixed %); hard-exclude any name currently on GSM stage ≥2 or under trade-for-trade settlement | §2 (ASM/GSM), cross-ref WS01 (monthly review cadence), WS05 (band discontinuity) | B (mechanism + regulatory-published thresholds), C (specific percentile untested) | Medium | N/A — a construction/exclusion rule, not a return premium | A completed band-lock-frequency data build from free bhavcopy data (§6) |
| F&O-ban-repetition contrarian flag | Not proposed for sizing; monitor-only | §2 | C | Low | Reduce-only if ever adopted | A dedicated event study — none exists today |
| Options-premium-harvesting sleeve | **Not proposed** | §2, §3 | N/A | N/A | N/A | A demonstrated structural/capacity argument distinguishing this book from professionalized desks — none offered here |

---

## 5. Evidence-tier recommendations

- **Index inclusion/exclusion (India, pooled Nifty + MSCI + FTSE reconstitutions)**: **Tier B**,
  borderline Tier A on raw observation count (semi-annual/quarterly reconstitutions across three
  index families over 15–25 years plausibly exceeds 30 events), held at B because the India-specific
  effect-size literature is thin (one cross-verified citation, F8) and the mechanism is explicitly
  time-varying (decaying/rising with domestic passive AUM), which argues for treating parameters as
  provisional even at high observation counts, per the contract's spirit if not its letter.
- **Promoter pledging as crash-risk signal**: **Tier B**, roughly 10–15+ dated Indian case events
  identified from public reporting (F9), comfortably inside the 4–30 Tier-B band; a genuine mechanical
  (not merely statistical) forced-selling mechanism, one of the stronger survival arguments in this
  dossier.
- **Anchor/promoter lock-in expiry drift**: **Tier C**, narrative/mechanism-based only — no India-
  specific quantified study produced this session; reduce-risk-only per the contract's Tier-C rule,
  which is exactly the intended use here (it was never proposed as a return source).
- **IPO listing pop / post-listing drift**: **Tier C for any standalone version** (uncontrollable entry
  mechanism, weak/contested US literature once matched-benchmark corrections are applied); the
  *quality-composite flag* version inherits the moderate book's existing Tier-B factor tiering rather
  than standing alone.
- **Bulk/block-deal and PIT-disclosure following**: **Tier C→B split by rank bucket** — Tier C
  (effectively excluded) for ranks 1–500, provisional Tier B for ranks 500–750 pending a dedicated
  data-phase test; zero India-specific quantified citation available this session.
- **Buyback/open-offer/delisting arbitrage**: **Tier B**, moderate observation count (India buyback/
  open-offer/delisting activity plausibly yields 10–30+ events per year pooled, though per-book
  capacity, not signal quality, is the true binding constraint here).
- **Demerger/spinoff holding rule**: **Tier C, provisional B** — strong structural mechanism from
  non-India literature (F12), zero India-specific citation verified this session; the tier should be
  earned by a data-phase event study, not assumed from the US analogy alone.
- **ASM/GSM/circuit-band exclusion rule**: **Tier B/A by construction** — this is a regulatory-
  published, rule-based filter, not an estimated effect; its "observation count" framing does not
  apply in the usual sense, but its evidentiary basis (published SEBI/exchange surveillance criteria,
  cross-verified by two sibling dossiers) is as solid as anything in this dossier.
- **F&O-ban repetition as contrarian signal**: **Tier C**, narrative only, no citation; explicitly
  monitor-only, never sizing-eligible under the contract's Tier-C rule.
- **Options-premium harvesting**: **not tiered — rejected**, no survival argument offered.

---

## 6. Research method for the data phase

Honoring the Estimation Standards (Contract §9): pre-register each hypothesis below before running it;
purge/embargo cross-validation with an embargo scaled to each signal's own half-life; judge
out-of-sample performance against the historical-mean benchmark; correct for Stambaugh bias wherever a
persistent predictor (e.g., pledge %, band-lock frequency) is used; count every sweep (including any
quantile-threshold sweep for the band-lock filter) in the deflated-Sharpe trial count.

1. **India demerger/spinoff event registry** — build from free BSE/NSE corporate-action filings (no
   paid data required): date of demerger record date, parent and spun-off entity identifiers, relative
   size (spun-off market cap ÷ parent market cap pre-demerger), and subsequent 3/6/12/24/36-month
   returns for both entities vs. a size/sector-matched benchmark. This is the single highest-value new
   data-build in this dossier — it directly tests F12's untested India-transfer question and can be
   built entirely from free, point-in-time exchange filings.
2. **India index-reconstitution effect, pooled and re-estimated** — extend WS01's Selvam et al.
   citation (F8) with a full-sample rebuild (Nifty 50/Next 50/Midcap 150 semi-annual changes plus MSCI
   India semi-annual/quarterly reviews, from free NSE bhavcopy plus published index-provider
   reconstitution announcements) segmented by **calendar era** (pre-2015 vs. post-2020) to directly
   test the proposed "rising decay as passive AUM grows" hypothesis rather than assuming it.
3. **Promoter-pledge event study** — build a point-in-time pledge-disclosure panel from free SAST
   Regulation 31 exchange filings (encumbrance creation/invocation/release, per stock, dated), and
   test both (a) the crash-risk quality-composite overlay (WS02's framing) and (b) this dossier's
   event-driven framing (abnormal return in the days following a **pledge-invocation** disclosure
   specifically, as distinct from steady-state high-pledge levels).
4. **Band-lock frequency build** — from free NSE/BSE bhavcopy (closing price vs. the exchange's
   published circuit-band master), construct the per-stock, per-month band-lock-frequency statistic
   proposed in §2, and validate it as an exclusion filter by testing whether it predicts (i) realized
   slippage vs. modeled square-root-law impact (Workstream 05) and (ii) forward drawdown severity
   conditional on being held into a broad market selloff — the exact scenario the mandate's drawdown
   constraint is measured against.
5. **Bulk/block-deal and PIT-disclosure signal, rank-segmented** — from free exchange bulk/block-deal
   and insider-disclosure feeds, pre-register a single test design (event window, direction rule,
   rank-bucket split) *before* looking at ranks 500–750 returns, to avoid exactly the "re-test a
   rejected idea with tweaked parameters" trap the contract forbids.
6. **Buyback/open-offer/delisting deal-flow census** — tally, from free exchange filings, every
   mainboard buyback, mandatory open offer, and delisting attempt over a multi-year window (deal size,
   realized spread, outcome, time-to-resolution) to convert F11's qualitative "small but real" claim
   into an actual capacity number for the aggressive-book satellite cap.
7. **Anchor/promoter lock-in window test** — using RHP-disclosed anchor allocation and lock-in dates
   (free, per-IPO, public prospectus data) plus post-listing bhavcopy prices, directly test whether an
   India-specific pre/post-unlock abnormal-return pattern exists at all, rather than assuming the
   Field-Hanka (US, VC-backed) mechanism transfers unchanged.
8. **SME-tier liquidity confirmation** — even though SME names are excluded from the universe, a brief
   data-phase check (free NSE Emerge/BSE SME bhavcopy) of typical free-float and traded-value figures
   would convert F5's qualitative exclusion argument into a quantified one, useful if the exclusion is
   ever challenged or revisited.

---

## 7. Open questions and [VERIFY] items

**Tooling/session-level, stated first because it governs everything else in this dossier**: this
workstream executed **zero** web searches (shared program budget was already exhausted at 200/200
before the first call) and had **WebFetch blocked on every domain tested**, a stricter failure than
the sibling dossiers that ran earlier in the program's shared budget. Every citation not explicitly
marked "cross-verified via WS0x" in this dossier rests on pre-cutoff trained knowledge alone and
should be treated as unverified until a follow-up pass with search access confirms it. If a follow-up
verification pass is possible, the priority order should be:

1. **The SEBI IPO-flipping/anchor-selling study (F3)** — the single most load-bearing citation in this
   dossier for the "why buying the IPO pop doesn't scale" argument; exact title, publication venue
   (SEBI DERA working paper vs. board memo vs. press-only), date, and percentages are all unconfirmed.
2. **The SEBI 2022 anchor lock-in 30/90-day split circular (F4)** — exact circular number/date.
3. **The 2024–25 index-derivatives-curbs weekday-assignment detail (§2)** — the specific claim that
   NSE and BSE were pushed to different weekly-expiry weekdays is the lowest-confidence recollection in
   this dossier and should be checked first among the microstructure items.
4. **An India-specific lockup-expiry event study (F6)** and **an India-specific demerger event study
   (F12)** — both currently rest entirely on US literature by analogy; neither citation exists yet.
5. **Exact figures for Field-Hanka (2001), Shleifer (1986), Harris-Gurel (1986), Chen-Noronha-Singal
   (2004), and Cusatis-Miles-Woolridge (1993)** (F6, F7, F12) — high confidence on substance and
   mechanism (these are foundational, decades-old, extremely well-known papers), but exact percentages,
   page numbers, and sample windows were not re-confirmed this session and are recalled from training
   only.
6. **Exact SEBI retail F&O loss study figures (§2)** — the qualitative "most retail traders lose money"
   conclusion is very likely directionally correct (this is one of the most widely reported SEBI
   findings of the mid-2020s), but exact percentages and rupee figures need confirmation.
7. **Promoter-pledge Indian paper's exact author/venue (F9)** — WS02 cited this with the same caveat;
   worth a joint follow-up since both dossiers rely on it.
8. **The exact SME-IPO 2024 SEBI tightening measures and company names (F5)** — the exclusion
   conclusion does not depend on getting these exactly right (the universe-definition argument alone
   is sufficient), but the manipulation-evidence framing would be strengthened by confirmed citations.
9. **Design question left genuinely open (not a citation gap)**: the special-situations sleeve's
   capital cap (§4, proposed placeholder ≤10% of aggressive-book NAV) is not derived from any source —
   it is an analogy to other satellite-sleeve caps proposed elsewhere in this research program. This
   should be treated as the least-defended number in this entire dossier and must be re-derived from
   an actual India deal-flow census (§6, item 6) before it is allowed to bind anything.
