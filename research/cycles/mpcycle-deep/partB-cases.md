# PART B — India's monetary-policy cycle case record

*Monetary-policy-cycle monograph (Atlas 2.6; ladder seat `L6_monetary_stance`, `config/ladder.yaml`,
Tier B, `tau_half` 12–24 months) · Part B · v1.0 · 2026-09-02 · Author: Claude (research agent) for
Ionic quant desk (principal: gaurav@ionic.in)*

*Governed by `research/CONTRACT.md`. Every figure below is search-verified as of September 2026
unless tagged `[VERIFY: ...]`. Scope, stated once: this Part owns the **policy-cycle side** of every
episode — rate/liquidity path, RBI's stated rationale, what transmission (lending/deposit rates,
credit growth) actually did. The **macro/activity side** of several windows (GDP, IIP, exports, the
dating problem itself) is already covered by `docs/cycles/18-business-cycle.md` Part B (Atlas 2.3) —
cited by episode, never re-derived. The **NBFC/shadow-credit side** of 2013 and 2018 is already
covered by `research/cycles/shadow-deep/partB-cases.md` — cited, not re-derived. The **credit-side**
mechanics of the 2003–2018 twin-balance-sheet decade (GNPA masking, the AQR, the restructuring
alphabet) are already covered by `research/cycles/credit-deep/partB-cross-country.md` case #10 —
cited, not re-derived. This chapter's sibling files carry the theory
(`partA-theory-psychology.md`), the pre-registered JST-analogue trials MP1–MP3 (`mp-RESULTS.md`), the
data engineering (`partC-data.md`), and the algorithm/harvest ledger
(`partDEFH-math-algo-harvest-ledger.md`) — this Part closes that ledger's two outstanding designs:
**MP-D2** (pass-through asymmetry, hikes vs cuts, deposit-war conditioning — §B.4 below) and
**MP-D3** (the completed round-trip count against the ladder's own `changes_if: "6th completed round
trip"` — §B.3 below). Style follows `research/cycles/fincycle-deep/partB-cases.md` (house style):
numbers-forward, every figure sourced, `[VERIFY]` where a search pass could not pin the primary
release.*

*A note on "L6's lagged-regime read," used after every episode below: per `partC-data.md` §C.1, L6
consumes an `effective_rate` — the operating policy rate under whatever framework governed at the
time (Bank Rate → LAF repo → the single-repo corridor from May 2011 → the 2020–22 reverse-repo-floor
interlude → the SDF-floor era from April 2022) — read as a real rate against its own expanding
percentile, paired with the liquidity sign (surplus/deficit), classified loose/neutral/tight, and
consumed **lagged ~1 year** (the MP2 calibration: contemporaneous correlation with credit growth is
mildly **positive**, +0.07 — central banks tighten *into* booms, the reaction-function face — before
flipping to a **negative** peak of −0.06 at +1 year, per `mp-RESULTS.md`). L6 never trades the
announcement itself; the read below is what the lagged, classified state would say a year after each
episode's own rate action, not a same-day call.*

---

## B.1 The eight campaigns

### 1. 1997–2003 — the Jalan easing era

**The rate path.** Governor Bimal Jalan (22 Nov 1997 – 4 Sep 2003) inherited a Bank-Rate-era
framework — the modern repo-based Liquidity Adjustment Facility (LAF) did not exist yet; it was
introduced only in June 2000, with the single-repo operating corridor arriving even later, in May
2011 (`partC-data.md`'s own "effective-rate migration" point, first instance). The single sharpest
move of the entire 1997–2003 window came almost immediately: following the July 1997 Asian financial
crisis, contagion pressure on the rupee forced RBI to **raise the Bank Rate from 9% to 11%,
effective 17 January 1998** — a defensive spike, alongside a 1-percentage-point CRR increase in
December 1997/January 1998 and a temporary, very short-dated repo-style instrument pushed as high as
9% in the same defense. **[Verified — the 11% Bank Rate level and its 17 Jan 1998 effective date;
the accompanying CRR hike and short-dated repo spike are corroborated in the same search pass but
carry lower confidence on the exact repo figure `[VERIFY: the pre-LAF "repo" instrument's precise
January 1998 level and duration]`.]** The defense worked fast: the rupee stabilised at roughly
₹38.9/USD by late January 1998 and traded in a narrow ₹39.5 band by March 1998 — a shock, not a
regime, in the ladder's own vocabulary (`tau_half` 12–24 months; a two-month spike does not clear
even the low end of that band). The Bank Rate was then cut steadily across the rest of the Jalan
governorship; the CRR's own decline is the cleanest continuously-dated series available for this
era: **15.00% (8 Oct 1992) → 14.00% (May 1993) → 15.00% (Aug 1994, a brief re-hike) → 11.00% (Nov
1996) → 10.00% (Jan 1997) → 10.00%→11.00%→10.00% (a further 1997–98 wobble around the Asian-crisis
defense) → 9.00% (Nov 1999) → 8.00% (Apr 2000) → 8.50% (Aug 2000, a brief re-hike) → 7.50% (May 2001)
→ 5.50% (Dec 2001) → 4.75% (Nov 2002) → 4.50% (Jun 2003)** — a near-monotonic decline from the
15%-era ceiling to single digits, exactly the "CRR's long decline from 15% (1991)" the desk's own
brief names, verified date-by-date. **[Verified — the CRR chronology, cross-checked across the
allbankingsolutions.com and Business Standard timeline sources; the exact 1996–99 sub-path around
the Asian-crisis wobble carries `[VERIFY: primary RBI notification cross-check]`.]** On the operating-
rate side, once the June-2000 LAF gave RBI a genuine short-term policy instrument, the repo rate
itself eased from **9% (Mar 2001) → 8.75% (Apr 2001) → 8.5% (Jun 2001) → 8% (Mar 2002) → 7.5% (Nov
2002) → 7.1% (Mar 2003)**, converging toward the **~6% trough that the Reddy tightening campaign
would use as its own starting point in March 2004** `[VERIFY: the exact 2003→2004 sub-path from
7.1% to 6%]` — the Bank Rate itself, meanwhile, having been the pre-LAF era's headline instrument,
settled near 6% as the LAF regime took over, consistent with dossier 08's own "trough near 6%
(2003–04)" framing.

**Stated rationale.** The Jan-1998 spike was an explicit, public exchange-rate defense — arresting
contagion from the Asian crisis, not a domestic-inflation-targeting move (India had no formal
inflation target of any kind until 2015). The subsequent multi-year easing was framed around
supporting growth and financial-sector reform following the 1991–92 liberalization, deepening the
LAF's own operating-rate architecture, and progressively lowering the reserve-requirement burden on
a banking system still working through the post-1991 NPA legacy (cross-ref `docs/cycles/
18-business-cycle.md` Part B case 1, the 1991 BoP crisis's own credit-side legacy, not re-derived
here).

**What transmission actually did.** Bank lending rates in this era were still governed by the
administered Prime Lending Rate (PLR) system — a pre-Base-Rate, pre-MCLR regime (`partC-data.md`
§C.3's own four-regime taxonomy: BPLR → Base Rate (Jul 2010) → MCLR (Apr 2016) → EBLR (Oct 2019)) —
under which pass-through was notoriously incomplete and administratively sticky in both directions;
directionally, PLRs eased through the late 1990s alongside the Bank Rate and CRR cuts, but the
magnitude of pass-through relative to the policy-rate decline is `[VERIFY: no primary PLR-vs-Bank-Rate
spread series located this pass]`. Credit growth recovered through the late 1990s deceleration
(`18-business-cycle.md` Part B case 2, the 1997–2002 "long deceleration") into the 2003–2008 boom
this same easing regime fed directly into.

**Duration.** Treating the Jan-1998 spike as a shock inside a single multi-year LOOSE regime (per
the ladder's own tau_half band, a two-month spike cannot itself register as a distinct regime): the
Jalan era is one long easing arc, roughly **1998–2003/04, on the order of 5–6 years** — among the
longest single-direction regimes in this entire record, second only to the 2020–22 COVID floor in
duration once that episode's own hold is counted (§7 below).

**L6's lagged-regime read.** For most of 1998–2003, a lagged L6 reading the effective rate (Bank
Rate, then repo from 2001) against its own expanding percentile would have classified the regime
**LOOSE and aging** throughout — the multi-year monotonic decline gives L6 no ambiguous signal here,
unlike several later episodes with within-regime wobbles (§4, §5 below). The one moment L6 would
have registered a **transient TIGHT flag** is the 1998 Q1 spike itself — but on the ~1-year lag
convention, by the time that flag would have entered the regime score, the Bank Rate had already
reversed and eased again, meaning L6's own lag discipline (never a same-day event trade,
`partDEFH...` Part E Step 4) would have naturally filtered out a shock this short-lived, exactly the
design behavior the seat is built to produce.

---

### 2. 2004–2008 — the Reddy tightening campaign

**The rate path.** Governor Y.V. Reddy (6 Sep 2003 – 5 Sep 2008) inherited the ~6% repo trough and
tightened steadily as growth accelerated and inflation pressure built: **repo 6.00% (31 Mar 2004) →
6.50% (24 Jan 2006) → 7.00% (25 Jul 2006) → 7.25% (30 Oct 2006) → 7.50% (31 Jan 2007) → 7.75% (30 Mar
2007) → 8.00% (12 Jun 2008) → 8.50% (25 Jun 2008) → 9.00% (30 Jul 2008)** — the cycle's own peak, a
**300bp climb over roughly four years and four months**, the bulk of it (150bp) compressed into the
final six weeks before the July-2008 peak as oil and food inflation spiked ahead of the Lehman
collapse. **[Verified — the full repo date/level chronology, cross-checked across multiple aggregator
sources with consistent dates.]** The CRR moved in the same direction across the same window, rising
from its ~4.5–4.75% 2003 floor toward a pre-crisis peak of **9% by August 2008** — the same 9% level
the crisis-response chapter below (§3) documents being unwound in four months flat
`[VERIFY: the complete CRR step-path 2004→2008; the 9% August-2008 peak level itself is corroborated
by the symmetric "CRR cut from 9% to 5%" crisis-era sourcing, which requires a 9% starting point]`.

**Stated rationale.** RBI's own contemporaneous framing was containing an overheating economy running
at 9%+/yr growth with rising headline and asset-price inflation, alongside a second, structurally
distinct problem the tightening campaign had to solve *simultaneously*: **large, persistent capital
inflows** that would otherwise have driven unwanted rupee appreciation if RBI's dollar purchases went
unsterilized. The **Market Stabilisation Scheme (MSS)** — formalised via a Memorandum of Understanding
between the Government of India and RBI signed **25 March 2004** and operationalised from **April
2004** — was the instrument built specifically to solve this: RBI issues government bonds whose
proceeds are impounded in a separate account (never funding the fiscal deficit), sterilising the rupee
liquidity that dollar-purchase intervention would otherwise inject, at a scale that continuous
open-market sales of RBI's own limited G-sec stock could not have sustained. **[Verified — the MSS's
2004 origin, its March 2004 MoU date, and its sterilization mechanism.]** This is the clean illustration
of the **overheating/capital-inflows dilemma** the desk's own brief names: a single tightening campaign
simultaneously fighting domestic demand *and* absorbing external liquidity, using two different tools
(the repo/CRR path for the former, MSS for the latter) rather than one.

**Macroprudential tightening, before the term was fashionable.** Running alongside the rate campaign,
RBI used **risk-weight and provisioning tools on real-estate and consumer-credit exposures** — the
same countercyclical macroprudential logic BIS and the FSB would only formalize globally after 2009 —
to lean specifically against the credit-fuelled real-estate boom the fincycle monograph's own India
case (`research/cycles/fincycle-deep/partB-cases.md` §B3) dates to 2002–03 onward. RBI's general
direction across 2005–2007 raised risk weights on commercial real estate exposure and consumer credit
well above the standard 100% baseline, and lifted standard-asset provisioning requirements on the same
sensitive-sector book from a low base to multiples of it — a direct, administrative credit-supply lean
against the property boom's collateral channel, the same *class* of tool (though a different mechanism)
Japan's MOF used in 1990 and China's "three red lines" used in 2020 (both documented in the fincycle
monograph's own case record) `[VERIFY: the exact RBI circular dates and precise risk-weight/provisioning
percentage points for 2005–2007 — this pass could confirm the general direction and today's risk-weight
levels (commercial real estate: 100% standard / 150% non-standard) but not independently re-pull the
specific 2005–2007 circulars themselves]`. **Cross-reference discipline**: the fincycle monograph's own
India case (`fincycle-deep/partB-cases.md` §B3) already documents the 2003–2013 property boom's
price-side magnitude (Delhi/Bengaluru city indices near-tripling 2003–2007) and the RERA/GST structural
reset that followed the 2013–2020 stagnation; this Part's own contribution is narrower — the *policy
tool* RBI used mid-boom, not the boom's own price or credit chronology, which belongs to the fincycle
and credit monographs respectively.

**What transmission actually did.** Bank lending rates (still BPLR-regime, per `partC-data.md`'s
taxonomy) rose alongside the repo/CRR campaign, and credit growth — already running at a multi-year
high through the 2003–2008 boom (`docs/cycles/18-business-cycle.md` Part B case 3: GFCF growth
8.2%→17.5%, 2002→2004, capital-goods output roughly tripling 2005–2008) — decelerated only mildly
ahead of the 2008 global crisis itself, with manufacturing and construction growth easing by roughly
2.5 percentage points in 2007–08 from a 12% 2006–07 base (per the same cross-referenced chapter) —
a soft early warning that arrived *before* Lehman, not clearly separable from the tightening
campaign's own bite `[VERIFY: an India-specific bank-credit-growth series isolating the tightening
campaign's own effect from the simultaneous global deceleration]`.

**Duration.** A single, essentially uninterrupted TIGHT regime, **March 2004 – July 2008, roughly
four years and four months**.

**L6's lagged-regime read.** Reading the effective repo rate a year behind, L6 would classify this
campaign **TIGHT and aging** from roughly early 2005 onward — long and monotonic enough that the lag
costs little precision, except at the very end: L6's own 1-year-lagged read would still carry
**TIGHT** into mid-2009, a full year *after* the crisis-response easing (§3) had already cut the repo
rate by more than half — the stale read the ladder's design accepts as the cost of never trading a
same-day event, and why L6 is a REGIME input inside a shared macro block, never a timing trigger.

---

### 3. 2008–2010 — the crisis easing, and the 2010–2011 normalization

**The rate path — the speed record.** As the Lehman collapse hit India's own funding markets, RBI
reversed the entire 2004–2008 tightening campaign in a matter of months: the **repo rate fell from
its 9.00% (30 Jul 2008) peak to 4.75% by April 2009** — essentially the same magnitude of move the
prior campaign took over four years to build, unwound in under nine months. The **CRR fell from 9% to
5% over four months, October 2008 to January 2009** — a **400bp reduction released roughly USD 32.7
billion** into the banking system, according to contemporaneous IMF commentary praising the response
as "quick" and "fully warranted." **[Verified — the repo trough level and approximate date, and the
CRR's magnitude/timing and IMF characterization.]** SLR was trimmed one point, **25%→24%, in November
2008**. This combination — repo, CRR, and SLR all easing simultaneously and fast — is, on the ladder's
own evidentiary standard, the single cleanest "speed record" in this entire chronology: no other
easing campaign in the 1997–2026 record moves this much distance this fast. **The 2010–2011
normalization then reversed it just as sharply, if not as fast**: RBI raised the repo rate **13 times
between March 2010 and October 2011, a cumulative 375bp, from the 4.75% trough to 8.50%** — the
granular early path runs **5.00% (19 Mar 2010) → 5.25% (20 Apr 2010) → 5.50% (2 Jul 2010) → 5.75% (27
Jul 2010) → 6.00% (16 Sep 2010) → 6.25% (2 Nov 2010) → 6.50% (25 Jan 2011) → 6.75% (17 Mar 2011)**,
continuing in the same 25bp cadence through the remainder of 2011 to the 8.50% October peak.
**[Verified — the "13 hikes, 375bp cumulative, 4.75%→8.5%, Mar2010–Oct2011" aggregate figure and the
early 2010 date-by-date path; the complete month-by-month 2011 leg carries `[VERIFY: full primary
DBIE table]`.]**

**Stated rationale.** The 2008–09 easing was an explicit, unambiguous crisis response to a global
funding shock transmitted through India's export and capital-flow channels — the fastest, most
export/IIP-visible transmission episode in this entire record (`docs/cycles/18-business-cycle.md`
Part B case 4: IIP registering its first negative print in fifteen years in October 2008, exports
turning outright negative the same month, averaging roughly a 20% contraction through September 2009,
cross-referenced not re-derived here). The 2010–11 reversal was explicitly framed as reining in
inflation once the crisis-response stimulus had done its job and growth had recovered sharply (the
same cross-referenced chapter's own "fast V": growth recovering to 7.4% FY10, with Q4 FY10 alone
printing 8.6%).

**What transmission actually did.** Base-Rate-era (from Jul 2010) bank lending rates cut alongside the
crisis-era repo/CRR reduction, though — consistent with the chronic "sticky lending rate" complaint
RBI itself would keep making through the 2010s (RBI publicly urged banks for faster transmission as
late as 2016, per contemporaneous reporting) — the pass-through of the 2008–09 cuts into actual bank
lending rates was widely characterized as slower and smaller than the policy-rate move itself
`[VERIFY: an India-specific 2008–09 PLR/Base-Rate pass-through coefficient]`; credit growth, having
decelerated sharply through the crisis, recovered alongside the "fast V" described above. On the
2010–11 tightening leg, the reverse asymmetry showed up: lending rates rose promptly (banks pass a
hike through faster than a cut, the general pattern this Part's closing §B.4 documents across every
episode in this record), while deposit rates lagged, squeezing margins in the near term before banks
caught up.

**Duration.** The crisis easing itself is short — **roughly nine months, August 2008 to April 2009** —
among the shortest regimes in this record; the subsequent tightening runs **roughly 18 months, March
2010 to October 2011**.

**L6's lagged-regime read.** The cleanest illustration of why L6's ~1-year lag matters. A same-day
read of the October-2008 cut would classify the regime LOOSE almost instantly — but MP2's own
calibration (contemporaneous corr +0.07, credit-boom-linked; peak effect at +1y, −0.06) says the
*contemporaneous* reading is the reaction-function face, not the medicine's effect: RBI eased
*because* activity had just collapsed. A properly-lagged L6 would register LOOSE only around
mid-to-late 2009 — squarely inside the "fast V" recovery already underway, a stale read but the
design's own accepted tradeoff. On the reversal leg the same lag means L6 would still read LOOSE well
into 2010 even as the repo rate climbed through its first several hikes — the seat's slowest-to-update
moment in this record, and the strongest argument here for treating L6 purely as a REGIME input,
never a standalone timing signal.

---

### 4. 2011–2013 — the stagflation squeeze, and the July 2013 taper defense

**The rate path.** Following the 8.50% October-2011 peak, RBI eased gradually through 2012–13 as
growth decelerated sharply (`docs/cycles/18-business-cycle.md` Part B case 5: growth falling from 7.8%
at the start of 2011 to a then-nine-year-low 6.5% FY12, with Q4 FY12 at 5.3%) while WPI inflation
remained stubbornly elevated, running near 7–8%/yr through most of 2011–12 before finally easing to
6.0% by March 2013 — the classic stagflation dilemma the desk's own brief names: **growth deceleration
that was, in RBI's own contemporaneous words, "not commensurate with inflation control."** Repo eased
to **7.25% by 3 May 2013**. Then, following the Fed's May-2013 taper announcement and a rupee
depreciation from roughly ₹54 to ₹69/USD (a **~28% fall, April–August 2013**, touching a lifetime low
of ₹68.85 on 28 August 2013), RBI mounted an explicit rupee defense: on **15 July 2013**, it raised the
**Marginal Standing Facility (MSF) rate by 300 basis points above the repo rate — repo at 7.25%, MSF
at an effective 10.25%** — deliberately inverting the normal LAF corridor so the MSF's upper bound,
not the repo rate, became the market's operative overnight cost of funds. **[Verified — the ~28% rupee
depreciation, the 28 Aug 2013 lifetime low, and the 15 Jul 2013 300bp MSF hike to an effective 10.25%,
already cross-checked against `research/cycles/shadow-deep/partB-cases.md` §B5's own independent
citation of the same figures.]** The MSF corridor was unwound in September 2013, restoring repo as the
effective policy anchor; conventional repo hikes then continued the tightening through the same window
— **7.25% (3 May 2013) → 7.50% (20 Sep 2013) → 7.75% (29 Oct 2013) → 8.00% (28 Jan 2014)** — under
newly-arrived Governor Raghuram Rajan (from 4 Sep 2013), who alongside the MSF/repo moves also launched
the **FCNR(B) swap window** (announced shortly after his 4 September 2013 arrival): a special facility
letting banks swap fresh, minimum-three-year FCNR(B) dollar deposits at a fixed 3.5%/year rate,
mobilising an estimated **USD 26 billion** and contributing to roughly **USD 34 billion** raised
between September and November 2013 — widely credited with stabilising the rupee and moving India out
of the contemporaneous "Fragile Five" grouping. **[Verified — the FCNR(B) scheme's mechanism, its
roughly USD 26bn mobilisation, and the USD 34bn September–November aggregate.]**

**Stated rationale.** The 2012–13 easing leg was framed as supporting a sharply decelerating economy
once inflation showed the first signs of moderating; the July-2013 MSF spike was an explicit, openly-
stated **exchange-rate defense** against taper-driven capital outflow pressure — a **rates** operation,
not a credit-quality response, the distinction `research/cycles/shadow-deep/partB-cases.md` §B5
documents in full as the episode's own "negative control" against the 2018 NBFC funding freeze
(cross-referenced by name, never re-derived here: that Part's own subject is the NBFC/shadow-credit
signature of 2013 vs 2018; this Part's subject stops at the policy-rate and rupee-defense mechanics).

**What transmission actually did.** The MSF spike raised the marginal cost of overnight bank funding
sharply but briefly (unwound within roughly two months), with system-wide CP/CD funding costs rising in
its wake without a distinct credit-quality event behind them — precisely the shadow-deep monograph's
own finding that the 2013 episode shows "no macro propagation" on its own credit-stress score (SC1: 57th
percentile, per that Part's own table) even though the same spread series looks superficially similar to
a genuine credit event. Bank lending rates rose modestly through the continued repo hikes into January
2014; credit growth, already decelerating alongside the broader 2011–13 slowdown, showed no further
distinct air-pocket attributable to the MSF episode specifically `[VERIFY: an isolated bank-credit-growth
read for the Jul–Sep 2013 window net of the broader 2011–13 deceleration]`.

**Duration.** The broader 2012–13 easing-then-partial-reversal is genuinely a single, bumpy regime
rather than two clean phases: **easing April 2012 – May 2013 (roughly 13 months)**, then a **defensive
re-tightening July 2013 – January 2014 (roughly 6 months)** that did not reach a new high above the
October-2011 peak (8.00% in Jan 2014 sits below 8.50%) — a **lower high**, the technical signature this
Part's own round-trip count (§B.3) treats as a wobble inside one longer regime, not a fresh cycle.

**L6's lagged-regime read.** A lagged L6 would have read the 2012–13 easing as LOOSE-and-young through
most of 2013, still carrying that classification when the July-2013 MSF spike hit — exactly the kind of
regime-versus-shock mismatch the ladder's own design (L2 fast-stress owns announcement-day and
event-window vol mechanically; L6 does nothing on announcement days by construction, per `partDEFH...`
Part E Step 4) is built to separate: the desk's fast layer, not L6, is the seat meant to react to a
two-month MSF corridor inversion. By the time L6's own 1-year lag would have registered a TIGHT flag
from the Jul–Oct 2013 rate actions, the effective rate (now back to conventional repo terms) had barely
moved net of the 2012 easing — a muted, easily-missed signal precisely because the underlying regime
never cleanly reversed direction on a net basis.

---

### 5. 2014–2016 — the Rajan disinflation and the birth of the MPC

**The rate path.** Repo held at **8.00%** through most of 2014 following the Jan-2014 hike (§4), then
began a sustained multi-step easing under the newly-adopted inflation-targeting framework: **7.75% (15
Jan 2015, a surprise off-cycle cut) → 7.50% (4 Mar 2015, a surprise post-Budget cut) → 7.25% (2 Jun
2015) → 6.75% (29 Sep 2015, a larger-than-expected 50bp cut, the year's third and largest reduction,
totalling 125bp of easing in calendar 2015) → 6.50% (5 Apr 2016)**. **[Verified — the complete
2015–16 date/level path; the "125bp of 2015 easing" aggregate figure independently corroborated.]**

**Stated rationale — the institutional pivot, not just the rate path.** This campaign is defined less
by its rate magnitude than by the **regime change underneath it**: the **Urjit Patel Committee**
(a 2013–14 RBI expert panel chaired by then-Deputy-Governor Urjit Patel, report submitted January
2014) recommended RBI target CPI inflation alone (rather than the historically multi-indicator
approach), adopt a nominal anchor near 4%, and create a Monetary Policy Committee to vote on rate
decisions. The **Monetary Policy Framework Agreement**, signed between RBI and the Ministry of Finance
in **February 2015**, formalised a **4% CPI target with a symmetric 2-percentage-point tolerance band
(2%–6%)** based on CPI-Combined (2012 base). **[Verified — the Committee's January-2014 report, its
core recommendations, and the February-2015 Framework Agreement's 4%±2% target.]** The **Finance Act,
2016** then gave the framework statutory force by amending the RBI Act, and in **August 2016** the
government formally notified the 4%±2% target for the period through March 2021 (renewed in 2021 for a
further five years). Rajan's own public framing — "an Urjit Patel glide path fits us very well,
ensuring moderate growth even while we disinflate" — named the explicit disinflation targets the glide
path itself set: **8% CPI by January 2015, 6% by January 2016**, both of which the easing path above
was calibrated against as inflation actually cooperated. The **Monetary Policy Committee (MPC)** itself
was constituted under the amended RBI Act on **27 June 2016** — a six-member body (Governor as
chairperson, one RBI deputy governor, one further RBI officer, and three government-appointed external
members serving four-year terms) replacing what had been, until then, a Governor's sole and personal
decision. **[Verified — the MPC's statutory constitution date and six-member structure.]**

**What transmission actually did.** MCLR (from April 2016, per `partC-data.md`'s taxonomy) had not yet
arrived for most of this window — banks were still on the Base Rate regime (from July 2010) — and the
familiar complaint recurred: RBI's own Governor publicly pressed banks on transmission speed through
2015–16, remaining "focused on rate cut transmission" as late as December 2015, implying the 125bp of
2015 cuts had not fully reached borrowers by year-end `[VERIFY: an India-specific Base-Rate
pass-through coefficient for this leg — this pass located only qualitative commentary]`. Credit growth
remained subdued, consistent with the broader post-2011 twin-balance-sheet drag `credit-deep`'s own
case #10 documents in full (not re-derived here).

**Duration.** A single sustained LOOSE regime, **January 2015 – April 2016, roughly 15 months** —
one of the more clearly bounded regimes in this record, its start pinned almost exactly to the
February-2015 Framework Agreement.

**L6's lagged-regime read.** A lagged L6 would register the disinflation as **TIGHT-but-turning**
through most of 2015 (the 2014 8.00% hold still dominating the trailing window) before flipping to
**LOOSE** only around early-to-mid 2016 — stale relative to the policy pivot, but a lag that works in
the desk's favor here: the MPC's own creation (June 2016) and first meeting (October 2016, §6) arrive
almost exactly when L6 would finally register the prior year's easing — regime-score input and
structural change landing in the same rough window, a coincidence worth noting, not relying on.

---

### 6. 2016–2019 — the MPC's early years

**The rate path.** The MPC's **first meeting, 3–4 October 2016**, delivered a unanimous 25bp cut to
**6.25%** under new Governor Urjit Patel (in office from 4 Sep 2016) — a six-year low at the time, and
notable because roughly 60% of analysts polled beforehand had expected a hold. **[Verified — the
first-meeting date, the unanimous decision, and the 6.25% level.]** Barely a month later, **8 November
2016 demonetisation** — the withdrawal of legal-tender status from ₹500/₹1,000 notes — produced a
liquidity event RBI's own conventional toolkit had not been designed for: a surge of returned currency
into the banking system (deposits rising from roughly ₹97 lakh crore to ₹101.1 lakh crore between the
16-September and 11-November reporting fortnights) pushed system liquidity toward RBI's absorption
capacity limits (surplus approaching ₹5 trillion against roughly ₹7.5 trillion of usable collateral
G-secs). RBI's response was a genuinely novel tool: an **incremental CRR of 100% on the *increase* in
each bank's net demand-and-time-liabilities (NDTL) between the 16-September and 11-November fortnights**
— effective the fortnight beginning **26 November 2016**, expected to absorb roughly **₹3.24 lakh
crore** — while the *standard* CRR on total deposits stayed unchanged at 4%. **[Verified — the
mechanism, its NDTL window, its effective date, and the absorption estimate.]** The measure was
**withdrawn from the fortnight beginning 10 December 2016** — one of the shortest-lived instruments
in this chronology, roughly two weeks. With reverse repo doing much of the day-to-day absorption
given the surplus, the **reverse repo effectively became the de-facto operative rate for much of this
window** — the first instance of a pattern that recurs far more durably in 2020–22 (§7)
`[VERIFY: an explicit contemporaneous characterization of the reverse repo binding in this specific
window, as opposed to the better-documented 2020–22 instance]`. Repo then eased
further to **6.00% on 2 August 2017** — the lowest level since November 2010 — and held there until
**6 June 2018**, when it rose **25bp to 6.25%**, followed by a further **25bp to 6.50% on 1 August
2018** — the first back-to-back hikes since October 2013, and the first hike of any kind since the
January-2014 tightening (§4). **[Verified — the Aug-2017 cut to a post-Nov-2010 low, the two 2018
hike dates and levels, and the "first back-to-back hikes since Oct 2013" characterization.]** A long
easing sequence then followed through 2019: **6.25% (7 Feb 2019) → 6.00% (4 Apr 2019) → 5.75% (6 Jun
2019) → 5.40% (7 Aug 2019, an unusual 35bp step) → 5.15% (4 Oct 2019)** — a cumulative **135bp of
easing across five consecutive cuts in a single calendar year**, under Governor Shaktikanta Das (in
office from 12 Dec 2018, following Urjit Patel's resignation on 10 December 2018). **[Verified — the
complete 2019 date/level path and the 135bp cumulative figure.]**

**Stated rationale.** The Oct-2016/Aug-2017 easing reflected continued disinflation and a still-
decelerating economy in demonetisation's aftermath; the incremental-CRR move was an explicit, openly-
stated liquidity-absorption measure with no inflation or growth signal attached at all — a pure
plumbing operation. The 2018 hikes were framed around rising inflation risk (partly fuel-price-driven)
and the need to anchor expectations even as growth had not yet visibly cracked; the 2019 easing
sequence was explicitly framed around a **decisively slowing economy** — the same slide
`docs/cycles/18-business-cycle.md` Part B case 6 documents from the activity side in full detail
(GDP growth 8.0%→7.1%→6.7%→4.2%, FY16→FY20, the FY20 print the lowest since FY09; cross-referenced,
never re-derived here) and its own IL&FS-driven NBFC funding freeze (September 2018, ₹91,091 crore of
debt — fully covered by `research/cycles/credit-deep/partB-cross-country.md` case #10 and
`research/cycles/shadow-deep/partB-cases.md`, cited by name, never re-derived here).

**What transmission actually did.** MCLR became the mandatory lending-rate benchmark from April 2016
(`partC-data.md`'s taxonomy); despite the new mechanism, RBI itself publicly flagged continued slow
transmission through 2016 and reviewed the MCLR regime's own design — the same chronic complaint
recurring under a new benchmark. The 2019 easing's pass-through would only turn faster on the
retail/EBLR-eligible segment once the **External Benchmark Lending Rate (EBLR)** mandate arrived
(October 2019, `partC-data.md`'s fourth regime) — post-dating most of the 2019 cuts, so the bulk of
that year's 135bp still transmitted through the older, stickier MCLR mechanism
`[VERIFY: an isolated 2019 WALR pass-through coefficient net of the EBLR transition]`. Credit growth
remained weak through the IL&FS funding freeze's real-economy transmission, consistent with the
cross-referenced FY20 slowdown above.

**Duration.** Several distinct, comparatively short regimes packed into three years: a **LOOSE leg,
October 2016 – August 2017 (roughly 10 months)**, interrupted mid-way by the two-week demonetisation
liquidity shock; a **long hold, August 2017 – June 2018 (roughly 10 months)**; a **short TIGHT leg,
June – August 2018 (2 months)**; and a **LOOSE leg, February – October 2019 (roughly 9 months)**.

**L6's lagged-regime read.** The busiest short-regime stretch in the chronology, and the one where
L6's 1-year lag has the most within-window whipsaw potential: a lagged L6 would still read
**LOOSE-and-easing** into the 2018 hikes' own early months (the 6.00% hold's long trailing window),
flipping to a brief **TIGHT** read only around mid-to-late 2018 — almost exactly as the 2019 easing
was already underway. This is why the seat treats regime persistence, not the raw rate level, as the
informative object (`partDEFH...` Part D), and exactly the episode density §B.3 below treats as noise
inside a longer regime rather than several independently countable campaigns.

---

### 7. 2020–2022 — the COVID floor, then the inflation-shock hiking cycle

**The rate path — the floor.** RBI cut repo **75bp to 4.40% on 27 March 2020** as the national COVID
lockdown began, with the **reverse repo cut by a larger 90bp to 4.00%** the same day — an explicitly
asymmetric corridor move designed to discourage banks from simply parking funds rather than lending.
A further **25bp reverse-repo-only cut to 3.75% followed on 17 April 2020** (no repo change), and then,
in an **off-cycle MPC meeting on 22 May 2020**, both rates moved again: **repo −40bp to 4.00%,
reverse repo −40bp to 3.35%** — the record-low floor the desk's own brief names. **[Verified — the
27 Mar 2020 and 22 May 2020 dates/levels; the 17 Apr 2020 reverse-repo-only cut.]** This floor then
**held for an unusually long stretch, roughly 22 months, May 2020 through April 2022** — the longest
unbroken hold in this entire chronology. With banking-system liquidity in sustained, large surplus
throughout, the **reverse repo — not the repo rate — was the de-facto operative rate** for much of
this window, a far more durable instance of the pattern first seen briefly in late 2016 (§6). RBI's
toolkit went well beyond the corridor: **Targeted Long-Term Repo Operations (TLTRO)** from March 2020
(TLTRO 2.0 targeting NBFCs/MFIs specifically, ₹50,000 crore first tranche, half earmarked for
small/mid-sized NBFCs), and the **Government Securities Acquisition Programme (G-SAP)**, RBI's own
QE-adjacent bond-purchase toolkit, announced 2021 to backstop the G-sec market
`[VERIFY: exact G-SAP tranche sizes/dates]`. Forward guidance was explicitly **"accommodative as long
as necessary to revive growth on a durable basis, while ensuring inflation remains within the
target"** — repeated across successive statements, abandoned only once the 2022 hiking cycle began.

**The rate path — the inflation-shock hiking cycle.** RBI formally introduced the **Standing Deposit
Facility (SDF)** at **3.75%** on **8 April 2022**, explicitly designed to **replace the reverse repo as
the floor of the LAF corridor** — a non-collateralized absorption tool requiring no G-sec pledge,
closing the corridor-mechanics gap the 2020–22 surplus-liquidity era had exposed. **[Verified — the
SDF's 8 April 2022 introduction and its explicit design purpose of replacing reverse repo as the
corridor floor.]** Less than a month later, in a **surprise off-cycle MPC meeting on 4 May 2022**, RBI
raised the repo rate **40bp to 4.40%** — the first hike in 45 months, since August 2018 (§6) — alongside
a **50bp CRR hike to 4.50%**, withdrawing an estimated **₹87,000 crore** of liquidity. **[Verified —
the 4 May 2022 date, the 40bp/4.40% repo move, the "first hike in 45 months" characterization, and the
simultaneous 50bp CRR hike.]** The campaign then continued on the regular bi-monthly calendar: **50bp
to 4.90% (8 Jun 2022) → 50bp to 5.40% (5 Aug 2022) → 50bp to 5.90% (30 Sep 2022) → 35bp to 6.25% (7 Dec
2022) → 25bp to 6.50% (8 Feb 2023)** — a cumulative **250bp of tightening, May 2022 – February 2023**,
front-loaded (three consecutive 50bp moves) before decelerating to 35bp then 25bp as inflation began
cooling. **[Verified — the complete hike-by-hike date/level path and the 250bp cumulative total.]**

**Stated rationale.** The 2020–22 floor was an explicit, unambiguous crisis response to the COVID
shock — the one unambiguous classical recession in this entire record on any dating convention
(`docs/cycles/18-business-cycle.md` Part B case 7: Q1 FY21 GDP contracting 23.9% year-on-year,
manufacturing −39.3%, the first quarterly GDP contraction since India began publishing quarterly data
in 1996; cross-referenced, never re-derived here). The 2022 hiking cycle's rationale was equally
explicit and stated in real time: Governor Das's own words accompanying the May-2022 move cited "the
strengthening of inflationary impulses in sync with the persistence of adverse global price shocks" —
the Russia-Ukraine war's own commodity and energy price transmission, layered onto already-elevated
post-COVID demand.

**What transmission actually did.** The 2022–23 hiking cycle is the single best-documented transmission
episode in this entire record on the asymmetry question §B.4 closes below: the one-year median MCLR
rose **120bp** against the 250bp cumulative repo hike, while medium-term deposit rates moved up only
**78bp** over the same window — a **>40bp gap** between what banks charged borrowers and what they paid
depositors, directly widening net interest margins during the hiking phase. Weighted-average lending
rates on **fresh** rupee loans rose **137bp** and on **outstanding** loans **80bp** across May–December
2022 against the 225bp of hikes delivered by that point, while **external-benchmark-linked (EBLR)**
loans — by then roughly **47.6% of outstanding floating-rate rupee credit**, against MCLR-linked loans'
**46.5%** share (September 2022) — repriced mechanically and in near-full lockstep with the repo move,
by construction. **[Verified — the 120bp/78bp MCLR-vs-deposit gap, the 137bp/80bp fresh/outstanding
WALR figures, and the EBLR/MCLR outstanding-loan share split, all sourced to the same contemporaneous
banking-sector analysis.]**

**Duration.** The COVID floor is the longest sustained single-level hold in this entire chronology —
**roughly 22 months, May 2020 – April 2022**; the hiking cycle that followed is comparatively fast —
**roughly 9 months, May 2022 – February 2023** — for a cumulative move (250bp) smaller than the 2004–08
Reddy campaign's 300bp but delivered in barely a fifth of the time.

**L6's lagged-regime read.** A lagged L6 would have read the effective rate as decisively **LOOSE**
throughout 2021 — the trailing 12-month window dominated by the 2020 cuts, with no ambiguity given the
regime's own 22-month duration. The interesting case is the transition: by the time L6's own 1-year lag
would have flipped the classification to **TIGHT** (roughly mid-2023, a year into the 2022 hiking
cycle), the campaign itself had *already ended* (the last hike landed February 2023) — meaning L6's
lagged TIGHT read would have arrived just as the regime it was describing was giving way to the
multi-year plateau §8 below documents, a textbook instance of the seat reading a regime's *aftermath*
rather than its live state, precisely the tradeoff the ladder accepts in exchange for never trading a
same-day event.

---

### 8. 2023–2026 — the plateau, and the current easing

**The rate path — the long hold.** Repo held at **6.50% for eleven consecutive bi-monthly reviews,
February 2023 through December 2024** — the longest unbroken *no-change* stretch (as opposed to
easing/tightening duration) in the MPC-era record. The **6 December 2024** review — Governor
Shaktikanta Das's last before **Sanjay Malhotra took office as Governor on 11 December 2024** —
delivered a **50bp CRR cut, from 4.50% to 4.00%, phased in two 25bp steps on 14 and 28 December 2024**
— releasing an estimated **₹1.16 lakh crore** of primary liquidity, with repo itself left unchanged.
**[Verified — the 50bp/two-step CRR cut, its December dates, and the ₹1.16 lakh crore figure.]** Under
Malhotra, the plateau then broke: **repo −25bp to 6.25% (7 Feb 2025)** — the **first cut in nearly
five years**, the prior cut having been May 2020 — followed by **−25bp to 6.00% (9 Apr 2025)**, then a
**larger, "jumbo" −50bp to 5.50% (6 Jun 2025)**, delivered alongside a **100bp CRR cut phased in four
equal 25bp tranches, taking CRR from 4.00% to 3.00% by December 2025**, and an explicit **policy-stance
change from "accommodative" to "neutral."** **[Verified — the complete Feb/Apr/Jun 2025 date/level
path, the June-2025 CRR-cut magnitude and phasing, and the stance change.]** RBI then **held at 5.50%
through August and October 2025** — the August pause explicitly
attributed to assessing the impact of a US tariff escalation on Indian exports (doubling from 25% to
50%) — before delivering a **final 2025 cut of 25bp to 5.25% in December 2025**, taking the calendar-
year total to **125bp of easing (6.50%→5.25%)**, the RBI's own characterization: "the most aggressive
easing cycle in six years." **[Verified — the Aug/Oct 2025 holds, their tariff-related framing, and the
December-2025 cut/cumulative-2025 figures.]** As of this writing, repo has held at **5.25% for four
consecutive reviews since the December 2025 cut** (through the **August 2026** review, 3–5 August 2026,
which kept the repo rate, SDF (5.00%) and MSF/Bank Rate (5.50%) all unchanged, retaining the neutral
stance while raising the FY27 GDP growth forecast to 6.7%). **[Verified — the August-2026 hold, the
"fourth consecutive review unchanged" characterization, and the accompanying rate levels; the FY27
inflation-forecast figure attached to that same review carries `[VERIFY: the exact print — sourced
figures were internally inconsistent this pass]`.]**

**Stated rationale.** The 2023–24 hold reflected inflation still running above the 4% target midpoint
even as it moderated from the 2022 shock; the Dec-2024 CRR cut (without a repo move) was an explicit
liquidity-only operation, distinct from the rate decision, in the same spirit as the Nov-2016
incremental-CRR episode (§6) though opposite in direction and far larger in scale. The 2025 easing
cycle was explicitly framed around **growth losing momentum alongside inflation approaching the 4%
target** — the mirror image of the 2011–13 stagflation squeeze (§4), this time with both legs
(disinflation and growth concern) pointing the same direction rather than in tension. The June-2025
jumbo cut and simultaneous stance shift to neutral was explicitly framed as **front-loading** easing
while conditions still allowed it, with the neutral stance itself signaling no further mechanical
commitment either way.

**What transmission actually did.** With EBLR-linked loans by 2025 a substantially larger share of
outstanding retail credit than in 2022 (the share rises mechanically as new origination replaces older
MCLR-linked stock, per `partC-data.md`'s "EBLR share rising = lags shortening" note), the 2025 cuts are
expected structurally to pass through faster on the retail book than the 2022 hikes did in reverse on
deposits — a matched fresh-vs-outstanding WALR comparison `[VERIFY: not independently computed this
pass; registered as MP-D1's own data-phase task, `partDEFH-math-algo-harvest-ledger.md` Part F]`.
Credit growth through 2024–25 remained elevated enough relative to deposits that the deposit-war
dynamic (§B.4) persisted well past the point the hiking cycle had ended.

**Duration.** The 2023–24 hold is the longest **no-change** plateau in the record — **roughly 24
months, February 2023 – February 2025**; the 2025 easing leg that followed runs **roughly 10 months,
February – December 2025**, followed by an **ongoing hold, December 2025 – August 2026 (at least 8
months as of this writing)**, whose eventual length is, by the ladder's own design discipline, not a
forecast this Part will offer (`partDEFH...` Part H: "the current easing cycle's terminal point ...
L6 reads the regime lagged and refuses the forecast").

**L6's lagged-regime read, as of writing (2026-09-02) — the desk's live regime, stated as a regime,
never a forecast.** A lagged L6 reading the effective rate roughly a year behind — i.e., informed by
the rate path through roughly Q3 2025 (repo at 5.50%, mid-way through the 2025 easing leg, CRR cuts
still phasing in) — would today classify the regime **LOOSE and comparatively young**: the active
easing began February 2025, roughly 19 months before this writing, still well inside the seat's own
12–24 month `tau_half` band rather than deep into an aging tail. The regime's own internal composition
— front-loaded cuts (Feb/Apr/Jun 2025, 125bp) followed by a lengthening hold (Aug 2025 – Aug 2026, at
least four consecutive reviews unchanged) — reads, on the ladder's own state-phase convention
(`config/ladder.yaml`'s `state_phase_convention`), as a LOOSE level with **decelerating (flattening)
velocity** — a quadrant the convention itself would classify as moving from "recovery" toward
"slowdown-of-the-easing-itself," not a reversal, and — per that same convention's own consumption rule
— logged and displayed for monitoring only, never yet branching a traded rule on the quadrant read.
This is a regime description, not a forecast: L6's own design (§B.3 below) explicitly refuses to say
whether 5.25% is the cycle's trough or merely its most recent stop.

---

## B.2 The cycle table

| Campaign | Direction | Duration | Peak-to-trough move | Transmission lag observed | L6 regime read |
|---|---|---|---|---|---|
| 1998 Jan Asian-crisis defense | TIGHT (shock) | ~2 months | Bank Rate 9%→11% (+200bp) | too brief to observe | filtered out by the 1y lag; never registers as a distinct regime |
| 1998–2003/04 Jalan easing | LOOSE | ~5–6 years | Bank Rate/repo ~11%→~6%; CRR 15%→4.5% | directional easing, PLR-era, magnitude `[VERIFY]` | LOOSE-and-aging throughout; no ambiguity (monotonic) |
| 2004–2008 Reddy tightening | TIGHT | ~4y 4m | repo 6.00%→9.00% (+300bp); CRR to ~9% | lending rates up, credit growth soft only late-cycle | TIGHT-and-aging from ~2005; still TIGHT a year into the 2008–09 reversal (stale) |
| 2008–2009 crisis easing | LOOSE | ~9 months | repo 9.00%→4.75% (−425bp); CRR 9%→5% | fast policy move, pass-through slower/partial `[VERIFY]` | reads LOOSE only ~mid-2009, a year behind the crisis itself |
| 2010–2011 normalization | TIGHT | ~18 months | repo 4.75%→8.50% (+375bp, 13 hikes) | lending rates up promptly; deposit rates lagged | still reads LOOSE through most of the hiking leg (lag artifact) |
| 2011–2013 stagflation + Jul-2013 taper defense | TIGHT-then-mixed | ~13mo easing + ~6mo defense | repo 8.50%→7.25%; MSF +300bp to 10.25% (Jul 2013, 2 months) | MSF episode: funding-cost spike, no credit-quality event (shadow-deep SC1 57th pctile) | LOOSE-and-young into the MSF shock; L2 (fast layer), not L6, owns the 2-month spike |
| 2014–2016 Rajan disinflation | LOOSE | ~15 months active easing | repo 8.00%→6.50% (−150bp); 125bp in 2015 alone | Base-Rate-era, RBI itself flagged slow pass-through | TIGHT-but-turning through 2015; LOOSE only by ~mid-2016 |
| 2016–2019 MPC early years | mixed (LOOSE / shock / TIGHT / LOOSE) | 4 sub-regimes, 2–10 months each | repo 6.25%→6.00%→6.50%→5.15%; Nov-2016 incremental CRR 100% (2 weeks) | MCLR-era; 2019 EBLR-eligible loans faster; corporate MCLR book stickier | busiest whipsaw stretch in the record; lag actively works against regimes this short |
| 2020–2022 COVID floor + inflation-shock hiking | LOOSE-then-TIGHT | 22mo floor + 9mo hiking | repo 5.15%→4.00%→6.50% (+250bp, May2022–Feb2023); CRR +50bp (May 2022) | MCLR +120bp vs deposits +78bp (>40bp gap); EBLR loans ~47.6% repriced near-lockstep | LOOSE throughout 2021 (unambiguous); TIGHT read only ~mid-2023, just as the campaign had already ended |
| 2023–2025 plateau + 2025 easing | HOLD-then-LOOSE | 24mo hold + 10mo easing (ongoing hold since) | repo 6.50%→5.25% (−125bp, Feb–Dec 2025); CRR −150bp cumulative (Dec2024+2025) | EBLR share higher than 2022; faster pass-through expected, not yet matched-computed `[VERIFY]` | **as of writing: LOOSE and comparatively young (~19 months); decelerating velocity; a regime, not a forecast** |

---

## B.3 An honest count of completed round trips (closing MP-D3)

The ladder's own `changes_if` for `L6_monetary_stance` (`config/ladder.yaml`) reads: *"a 6th completed
round trip; primary RBI DEPR citation."* Dossier 08 (`research/dossiers/08-india-mid-cycles.md`, §I1)
already flags this count as **boundary-sensitive**, landing at "n≈4–5" depending on whether the
2009–2019 span is read as one long, wobbly cycle or two. This Part owes the desk an explicit argument,
not a restated hedge.

**Method.** Define a **completed round trip** as a full **trough → peak → trough** sequence in the
effective policy rate (Bank Rate pre-2001, repo thereafter), where a "trough" or "peak" is a genuine
local extremum — a point the rate does not revisit before moving materially in the *other* direction —
and where a subsequent move that does **not** clear the prior extremum (a "lower high" or "higher low")
counts as a **wobble inside the existing regime**, not a fresh cycle. This convention is chosen
specifically to resolve the 2011–2016 ambiguity dossier 08 itself names: the Jul-2013 MSF/taper defense
pushed conventional repo only to **8.00% (Jan 2014)**, which sits *below* the **8.50% (Oct 2011)** peak
it followed — a lower high, and therefore, on this convention, a wobble inside one long regime rather
than a second, independently countable cycle.

**The turning points, dated.** Applying this convention to the full chronology in §B.1 above:

| # | Type | Date | Level | Confirmed how |
|---|---|---|---|---|
| P0 | Peak (partial; boundary observation, pre-modern-corridor) | Jan 1998 | Bank Rate 11% | shock, resolved same year — not a regime-scale peak on the ladder's own tau_half band |
| T0 | Trough | ~Mar 2004 | repo 6.00% | confirmed local minimum; Reddy tightening begins immediately after |
| P1 | Peak | 30 Jul 2008 | repo 9.00% | confirmed; crisis easing begins immediately after |
| T1 | Trough | ~Apr 2009 | repo 4.75% | confirmed; 2010 normalization begins immediately after |
| P2 | Peak | Oct 2011 | repo 8.50% | confirmed; 2012–13 easing begins immediately after |
| (wobble, not P/T) | — | Jul 2013–Jan 2014 | MSF +300bp; repo to 8.00% | **lower high** (8.00% < 8.50%) — inside the same regime as P2→T2, per the stated convention |
| T2 | Trough | Aug 2017 | repo 6.00% | confirmed local minimum (lowest since Nov 2010); Jun-2018 hikes begin after a hold |
| P3 | Peak | 1 Aug 2018 | repo 6.50% | confirmed; 2019 easing begins immediately after |
| T3 | Trough | 22 May 2020 | repo 4.00% | confirmed; a genuine new record low, not merely a revisit of T1 |
| P4 | Peak | 8 Feb 2023 | repo 6.50% | confirmed; 2023–24 hold, then 2025 easing, begins after |
| T4 | Trough (tentative — **not yet confirmed**) | Dec 2025–ongoing | repo 5.25% | **held, not reversed, as of Aug 2026** — could still fall further before the next hike; this Part explicitly declines to certify it |

**The count.** Reading trough-to-trough:

- **Round trip A**: T0 (2004) → P1 (2008) → T1 (2009). **COMPLETE.**
- **Round trip B**: T1 (2009) → P2 (2011) → T2 (2017), the 2013 MSF/taper episode absorbed as an
  internal wobble. **COMPLETE**, though exactly the span dossier 08 flags as contestable — a reader
  treating the Jul-2013 MSF spike as its own cycle (the *rates market* genuinely inverted, even though
  *conventional* repo never made a new high) would split this into two round trips instead of one,
  changing the total by exactly one either way. This Part's convention (peaks/troughs on conventional
  repo/Bank-Rate, not the MSF corridor) treats it as one; the disagreement is worth carrying forward
  rather than resolving by fiat, in the spirit `docs/cycles/18-business-cycle.md` Part B insists on.
- **Round trip C**: T2 (2017) → P3 (2018) → T3 (2020). **COMPLETE** — a short but genuine cycle; the
  2018 hike is a real, if small, new high (6.50% > 6.00%), and the 2020 low is a genuine new record,
  not a mere revisit.
- **Round trip D**: T3 (2020) → P4 (2023) → T4 (2025–ongoing). **NOT YET COMPLETE.** The peak leg
  is fully confirmed; the trough leg is not. As of this writing, repo has held at 5.25% for four
  consecutive reviews with no confirmed reversal to tightening — it is entirely possible 5.25% is
  already the cycle's low and a future hike will confirm it retroactively, but this Part explicitly
  declines to certify that today, exactly as §8's own closing paragraph states as a matter of design
  discipline, not merely caution.

**The honest answer.** By this record's own most defensible, single, non-arbitrary convention, the
1997–2026 chronology contains **three fully completed round trips (A, B, C)**, with a **fourth
currently in progress and not yet confirmable (D)**. A reader who instead splits round trip B at the
2013 MSF wobble gets **four** completed round trips instead of three — still short of a fifth, let
alone a sixth. **No defensible convention this Part can construct reaches six.** Dossier 08's own
"n≈4–5" is therefore, if anything, generous relative to the strict trough-to-trough convention applied
here (which yields 3, or 4 under the alternative split) — both readings converge on the same
consequence: **the ladder's own `changes_if` trigger — a 6th completed round trip — has not fired, and
on any convention this Part can defend, remains at minimum one and as many as three full cycles away.**
This is not a reason to distrust the seat; it is exactly why the seat is Tier B with parameters frozen
at inception (`config/ladder.yaml`) rather than Tier A fitted with purged CV (`research/CONTRACT.md`
§4) — the count itself is the evidence that more data, not a parameter re-fit, is what the seat still
needs. **MP-D3 is closed by this section**, per `partDEFH-math-algo-harvest-ledger.md` Part F's own
registration.

---

## B.4 The transmission-asymmetry record (closing MP-D2)

Every episode in §B.1 that carries a directional transmission read points the same way, and the
record is dense enough across nine decades — three distinct lending-rate regimes (BPLR, Base Rate,
MCLR) plus a fourth structural fix (EBLR) — to state the asymmetry plainly rather than as a single
anecdote.

**(i) Hikes pass through faster than cuts, structurally, across every regime this record covers.**
Under the pre-2010 BPLR/PLR system, RBI's own repeated public complaints about slow transmission
(explicitly on cuts, rarely on hikes) run through the Jalan-era easing, the crisis-era 2008–09 cuts,
and the 2015 Rajan disinflation alike — a chronic, cross-regime pattern rather than a single episode's
peculiarity. The clearest **quantified** instance sits in the 2022 hiking cycle: the one-year median
MCLR rose 120bp against 250bp of cumulative repo hikes, while medium-term deposit rates rose only
78bp over the same window — banks captured the spread on the way up, passing the hike through to
borrowers faster and more completely than to depositors. **[Verified figures, §B.1 case 7.]**

**(ii) The EBLR mandate (October 2019) is a genuine structural break in this asymmetry, but only for
the segment it covers.** Loans linked to an external benchmark (the repo rate itself, for most banks)
reprice mechanically and near-simultaneously with an MPC decision, by regulatory construction — the
September-2022 snapshot already shows EBLR-linked loans at roughly 47.6% of outstanding floating-rate
retail credit, essentially matching MCLR's 46.5% share even that early in the transition. This is the
single clearest instrument this record contains for closing the historical asymmetry — but it applies
overwhelmingly to new retail-and-MSME originations; the corporate lending book remains substantially
MCLR-linked, and MCLR itself reprices on a lag (typically monthly-to-quarterly reset dates) even after
a policy move, meaning the asymmetry has narrowed for one segment of the credit book and persisted for
another, a bifurcation `partC-data.md`'s own "EBLR share rising = lags shortening" monitoring note is
built to track over time rather than assume resolved.

**(iii) Deposit-war episodes are the mirror-image signature: banks catching up on the liability side
*after* a hiking cycle has already ended, not during it.** The clearest instance is **2022–2024**: as
credit growth ran at **17.4% year-on-year (June 2024)** against deposit growth of only **11.1%**,
banks — ICICI, RBL, Axis, IDFC First among those named in contemporaneous reporting — raised deposit
rates repeatedly through late 2022 into 2023–24 to fund continuing credit demand, the aggregate
loan-to-deposit ratio reaching a **two-decade high of ~80% by December 2023**, the incremental
credit-deposit gap running **over 700bp** at the start of 2024 before narrowing to **~200bp**
`[VERIFY: exact narrowing date]`. **[Verified — the 17.4%/11.1% split, the named banks' actions, the
~80% LDR, and the 700bp→200bp narrowing.]** The 2022 hiking cycle's own asymmetry (fast lending-rate
pass-through, slow deposit pass-through, per (i)) did not resolve once the hikes stopped in February
2023 — it forced a *second*, delayed round of deposit competition well into 2023–24, as banks
discovered their funding could not keep pace with the credit growth the hiking cycle had failed to
choke off. Earlier candidate episodes — a plausible 2010–11 post-crisis deposit scramble (§B.1 case
3) or the 1994–96 primary-market boom's own funding competition — are directionally consistent but
**not independently verified this pass**, flagged `[VERIFY]` rather than asserted.

**(iv) The net design implication for L6.** The asymmetry is not merely a curiosity for the cycle
narrative — it is a first-order reason the seat's own construction (`partDEFH...` Part E) reads the
*effective rate itself*, never a bank-lending-rate proxy, as the primary input: a signal built on
WALR or MCLR directly would inherit this asymmetry's own regime-dependence (BPLR-era stickiness,
MCLR-era partial improvement, EBLR-era near-completeness for one segment only) as an additional,
unmodeled source of drift across the ladder's own 1997–2026 estimation window, on top of the
`tau_half` drift the seat's `tau_half_drift_policy` (`config/ladder.yaml`) already tracks explicitly.
Reading the policy rate itself and letting the credit-growth transmission chain (MP-D1's own
replication design) carry the pass-through question separately keeps L6's own construction clean of
this asymmetry, at the cost of the lag the seat already accepts by design. **MP-D2 is closed by this
section**, per `partDEFH-math-algo-harvest-ledger.md` Part F's own registration: the pass-through
asymmetry runs hikes-fast/cuts-slow on the lending side, cuts-somewhat-faster-post-EBLR on the retail
segment specifically, and deposit-side competition arrives as a *lagged*, not contemporaneous,
response to a credit-growth gap the hiking cycle itself often fails to close before it ends.

---

## References

RBI, Monetary Policy Statements and DBIE historical rate tables (repo, reverse repo, MSF, SDF, Bank
Rate, CRR, SLR) — primary source for every date/level pair above, accessed via secondary aggregation
this session (DBIE egress blocked per `research/CONTRACT.md` §7 Known Prior #11; every figure
cross-checked across ≥1 independent source, `[VERIFY]` retained where only one was found). · RBI,
*Report of the Expert Committee to Revise and Strengthen the Monetary Policy Framework* (Urjit Patel
Committee, Jan 2014). · RBI–Government of India, *Monetary Policy Framework Agreement* (Feb 2015). ·
Finance Act, 2016. · `docs/cycles/18-business-cycle.md` Part B (Atlas 2.3, activity-side chronology,
cross-referenced throughout, never re-derived). · `research/cycles/fincycle-deep/partB-cases.md` §B3
(India property-cycle record). · `research/cycles/shadow-deep/partB-cases.md` §B5 (2013 MSF episode's
NBFC-side negative control). · `research/cycles/credit-deep/partB-cross-country.md` case #10 (twin-
balance-sheet decade). · `research/dossiers/08-india-mid-cycles.md` §I1–I2 (the seat's prior repo
chronology, extended here). · `research/register/trial-ledger.md` MP1–MP3 and this directory's own
`mp-RESULTS.md` (the JST-analogue trials each "L6 lagged-regime read" applies episode-by-episode). ·
this directory's `partC-data.md` (the effective-rate/lending-rate-regime taxonomy) and
`partDEFH-math-algo-harvest-ledger.md` (the MP-D2/MP-D3 designs this Part closes).
