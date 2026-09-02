# PART B — The shadow-credit case record: the funding-run anatomy

*Shadow-credit sub-cycle monograph (atlas 2.2, sub-component of L10, funding-freeze signature also
feeds L2) · Part B · v1.0 · 2026-09-02 · Author: Claude (research agent) for Ionic quant desk
(principal: gaurav@ionic.in)*

*Governed by `research/CONTRACT.md`. Every figure below is search-verified as of September 2026
unless tagged `[VERIFY: ...]`. This Part reads `docs/CYCLE_ATLAS.md` row 2.2 ("NBFC/shadow-credit
sub-cycle... shadow lenders fund long assets with short CP — a run-prone structure regulators keep
re-creating... n=1 clean [episode]: 2014→2018→2020") and `config/ladder.yaml`'s treatment of the
entry as a sub-component of `L10_credit_block`'s bank+NBFC aggregate, whose funding-freeze
signature also feeds `L2_fast_stress`. The desk's own pre-registered SC1 trial
(`research/cycles/shadow-deep/shadow-RESULTS.md`) already ran and **FAILED informatively** —
12-month-window SMB and market returns around the IL&FS crunch both fell hard (SMB −24.8%, 18th
percentile; market −20.2%, 16th percentile), meaning the freeze did **not** stay contained to small
caps: by the time a 12-month equity factor window could see it, "it is everyone's problem." That
finding — cited here directly, never recomputed — is this Part's organizing discipline: a
funding-run signature useful to the desk must be faster than a 12-month equity read, which is
exactly why the atlas routes it to L2 (weekly-cadence fast stress) rather than treating it as a
slow annual state. This Part does not re-run SC1 at a different horizon or propose an equity-side
acceptance test; any such claim belongs to SC2 (the CP-spread freeze signature,
`research/cycles/shadow-deep/partC-data.md`), pre-registered there before looking.
`research/cycles/capex-deep/partB-cases.md`'s own case 3 ("India 2011–2020") already covers
IL&FS's real-side transmission — NBFC/HFC real-estate exposure (~₹1.65 trillion, 7.5% of the
sector's book, March 2018, a figure that Part borrows from
`research/cycles/fincycle-deep/partB-cases.md`'s own §B3), the developer-financing freeze, and the
knock-on into capex/property data — and `research/cycles/credit-deep/partB-cross-country.md`
already uses IL&FS as case evidence for why a bank-only credit aggregate misses a shadow-banking
shock (the pre-registered **R7** composition-signal validation target). Neither cross-referenced
Part narrates the run itself: the ratings collapse, the default sequence, the government takeover,
the mutual-fund freeze, the CP market seizure, the equity panic, and the liquidity response. That
narrower, mechanism-level job — the **funding-run anatomy** — is this Part's own contribution, and
it is not duplicated elsewhere in the atlas. Style and evidentiary discipline follow
`research/cycles/fincycle-deep/partB-cases.md` (numbers-forward, every figure sourced, `[VERIFY]`
where a search pass could not pin the primary reconciliation, interpretation written honestly after
the numbers).*

---

## B1. Framing — what a shadow-credit run actually is, and why India keeps re-creating it

The mechanism CYCLE_ATLAS.md names in one sentence deserves stating in full before the cases: an
Indian non-bank finance company (NBFC) or housing finance company (HFC) typically funds long-dated
assets — infrastructure loans, developer finance, vehicle and personal loans repaid over years —
with short-dated liabilities: commercial paper (CP, 90-day-to-1-year, unsecured, rolled over
continuously), bank lines, and, for deposit-taking NBFCs, public fixed deposits. This is a maturity
mismatch by design, not by accident — it is the entire economic function of a non-bank intermediary
that cannot take retail current/savings deposits the way a bank can. The mismatch is stable exactly
as long as the rollover market believes the borrower is solvent; the moment that belief cracks, the
lender does not experience a slow credit deterioration — it experiences a **run**, because CP
holders (overwhelmingly mutual funds acting on behalf of retail unit-holders) have no reason to
wait and see. Every case below is a variation on this same run mechanic, with the difference lying
in what sits on the other end of the rollover chain — money-market mutual funds in India 2018 and
the US 2007–08, wealth-management-product buyers in China, bank depositors in the 1990s and at Yes
Bank — and in how fast the sovereign/central-bank backstop arrives once the run is visible.

---

## B2. IL&FS, 2018 — the funding-run anatomy (centerpiece)

### B2.1 The group: what "347 entities" actually meant

Infrastructure Leasing & Financial Services Ltd. (IL&FS), incorporated in 1987 as an infrastructure
finance and development company, had by 2018 grown — through three decades of holding-company
sprawl rather than any single strategic plan — into a four-layer conglomerate that its own newly
installed board could not immediately enumerate. The group's own new management initially
identified **347–348 group entities** once the crisis forced a full count; by April 2019, after 45
had been formally closed (42 foreign, 3 domestic), the operating group stood at **302 entities**
(133 foreign, 169 domestic) `[VERIFY: reconciling the 347 vs 348 count across contemporary sources
— both figures appear in period reporting; treated here as the same order-of-magnitude fact]`.
Sectorally, transportation carried the most subsidiaries (160 — chiefly **IL&FS Transportation
Networks Ltd., ITNL**, the group's listed roads/highways arm, itself carrying dozens of individual
special-purpose road-project vehicles), followed by energy (35) and financial services (30 —
chiefly **IL&FS Financial Services Ltd., IFIN**, the group's own NBFC lending and deposit-raising
arm, and the entity whose commercial paper and inter-corporate deposits (ICDs) are this Part's
central subject). Total group debt at the point of default is most commonly cited at **₹91,091
crore (~$13bn)** — the figure the credit-cycle monograph's own case record already uses — though at
least one contemporary compilation puts total outstanding group debt at **₹99,354 crore**
`[VERIFY: the exact reconciliation between the ₹91,091cr and ₹99,354cr figures — both are period
estimates and the gap is plausibly a snapshot-date or consolidation-scope difference, not a
correction of either]`. The structural lesson worth stating up front: a holding company with 300+
subsidiaries funded substantially through group-level CP and ICDs, cross-guaranteeing and
inter-lending across layers no external analyst could map in real time, is the platonic case of
the atlas's own warning — "a run-prone structure regulators keep re-creating" — because the
complexity itself, not merely the maturity mismatch, is what let the rating agencies and lenders
each assume someone else in the chain had done the diligence.

### B2.2 The ratings cliff — AAA to default in five weeks

| Date | Event |
|---|---|
| through mid-2018 | IL&FS and IFIN's principal long-term ratings stand at AAA/AA+ (ICRA, CARE); CP rated the top short-term grade, A1+ |
| 16 Aug 2018 | CARE issues the first crack: downgrade of IFIN's ₹4,800 crore non-convertible debenture (NCD) programme |
| 27–28 Aug 2018 | First payment stress becomes public: IFIN discloses (6 Sep) that CP due 28 Aug could not be paid on schedule and was settled late, on 31 Aug; separately, IL&FS entities miss instalments on ICDs owed to SIDBI (see B2.3) |
| early Sep 2018 | ICRA reaffirms **A1+ on IL&FS's own CP even while cutting the long-term rating from AAA to AA** (positive outlook) — the single detail that mattered most for the mutual-fund holders of that paper, who could keep treating it as top-rated short-term collateral days before the group's real condition became public |
| 8 Sep 2018 | ICRA downgrades IL&FS/IFIN's long-term ratings further |
| 14 Sep 2018 | IL&FS defaults on CP and ICD obligations falling due that day — the trigger default that made the stress undeniable across the market, not merely inside the rating agencies |
| 17 Sep 2018 | ICRA and CARE cut IL&FS's and IFIN's ratings straight to **'D'** (default) — from AAA/AA to the lowest junk grade, with the outstanding rated instruments at the moment of the cut standing at **₹11,725 crore (ICRA)** and **₹20,942 crore (CARE)** |

Read end to end, IL&FS group paper went from a AAA-rated, A1+-CP-backed instrument in June 2018 to
formal default ('D') by 17 September — roughly **five weeks** from the first visible crack (16
August) to the terminal downgrade, and a single day (14 September) between the payment default and
the rating catching up to it. The lesson the desk's own data-engineering chapter (`partC-data.md`)
already codifies from this exact sequence: "a rating is never an input, only a post-mortem
variable." Every stage of the ratings cliff above lagged, rather than led, the underlying default;
ICRA's own A1+ reaffirmation on CP in early September, made even as it was simultaneously cutting
the long-term rating, is the cleanest single artifact in this entire monograph of a rating agency
holding two inconsistent views of the same borrower's solvency at once.

### B2.3 The default sequence

The proximate defaults, reconstructed from contemporary reporting, ran through late August and
September 2018 across several group entities simultaneously rather than as one clean event:

- **SIDBI inter-corporate deposits.** IL&FS entities owed the Small Industries Development Bank of
  India three ICD tranches totalling **~₹350 crore**, due on staggered dates from 27 August 2018;
  only ₹50 crore of that was paid, leaving ₹300 crore outstanding `[VERIFY: a separate
  contemporary report cites a distinct ₹1,000 crore SIDBI short-term loan default around the same
  date — the two figures are not reconciled here and may describe different SIDBI exposures to
  different group entities]`.
- **IL&FS Financial Services CP.** CP due 28 August 2018 was not paid on schedule and was settled
  three days late, on 31 August — disclosed publicly only on 6 September, the first point at which
  the market had a documented admission of distress rather than rumor.
- **IL&FS Energy Development.** Defaulted on term-credit obligations to financial institutions,
  reported around 13 September 2018.
- **The 14 September trigger.** IL&FS defaults on CP and ICD obligations due that day — this is the
  date most consistently cited as the point at which the crisis became a market-wide, rather than
  counterparty-specific, event.

Two structural features of this sequence deserve emphasis for L2's own design. First, **the true
fuse — who was scheduled to be repaid next week — was never visible from the outside**: ICD markets
are bilateral and dark, and even the SIDBI exposure above surfaced only after journalists chased
leaked details, exactly the C.5 measurement gap the data-engineering chapter already states
("issuer-level rollover calendars... are visible only in aggregate; inter-corporate deposit markets
are dark"). Second, the defaults cascaded **within** the group before cascading **outside** it — a
subsidiary (IFIN, then IL&FS Energy) defaulting before the parent's own instruments were formally
marked down — meaning a monitoring system keyed only to the flagship entity's own paper would have
missed the first three weeks of the actual run.

### B2.4 The government takeover — 1 October 2018, and the Satyam precedent

On **1 October 2018**, the Mumbai bench of the National Company Law Tribunal (NCLT) approved a
Government of India petition to supersede IL&FS's entire board, invoking **Section 241(2) of the
Companies Act, 2013** on the ground that the existing management's conduct was prejudicial to
public interest. A new six-member board was installed: **Uday Kotak** (Kotak Mahindra Bank, as
non-executive chairman), **Vineet Nayyar** (a retired IAS officer), **G.N. Bajpai** (former SEBI
chairperson), **G.C. Chaturvedi** (ICICI's non-executive chairperson), **Malini Shankar** (IAS), and
**Nand Kishore** (a senior official from the Comptroller and Auditor General's office) — a board
composed entirely of regulatory and public-sector credibility rather than any incumbent IL&FS
management, financier, or resolution specialist.

This was, on contemporary legal commentary, only the **second** instance since the Companies Act of
1913 that the Government of India had taken over a private (non-government) company using
company-law machinery — the first being **Satyam Computer Services**, where the Company Law Board
barred the existing board on **10 January 2009**, days after founder Ramalinga Raju's confession of
a ₹7,000 crore accounting fraud, and installed ten nominee directors. The two episodes are legally
distinct (Satyam ran through the old Company Law Board under the Companies Act, 1956; IL&FS ran
through the NCLT under the Companies Act, 2013's Section 241/242 machinery, and on grounds of
mismanagement and public-interest risk rather than a confessed fraud) and financially incomparable
in scale (Satyam was ultimately sold, post-takeover, for **₹2,900 crore**; IL&FS carried
**~₹91,000–99,000 crore** of debt at default — roughly thirty times larger). A further, almost
uncanny detail ties the two cases together directly rather than merely by precedent: IL&FS had
itself, years earlier, acquired two entities from the Satyam promoter family's Maytas group —
**Maytas Infrastructure** and **Maytas Properties** — meaning the group that became India's second
government-superseded company had previously absorbed assets from the first one. **L2/L10 lesson.**
The takeover mechanism itself (NCLT board supersession under public-interest grounds) is now a
demonstrated, twice-used institutional tool for a systemically important non-bank failure —
distinct from, and generally faster to deploy than, the bank-resolution machinery (moratorium plus
RBI-administrator reconstruction) used three years later for Yes Bank (B4 below).

### B2.5 The mutual-fund freeze mechanics

India's debt mutual fund industry held IL&FS group CP and NCDs across dozens of schemes, and the
17 September downgrade to 'D' converted what had been marked as investment-grade collateral into
paper worth a fraction of face value overnight — precisely the NAV-discontinuity event
`partC-data.md` flags as a hard registry break, never a silent series adjustment. SEBI's regulatory
response, formalized in **December 2018** in direct reaction to the IL&FS episode (and extended the
following year to DHFL, B3 below), was to permit **"side-pocketing"**: segregating a scheme's
distressed, illiquid holdings into a separate portfolio so that (i) existing unit-holders bear the
loss on the specific defaulted paper rather than having it diluted across the whole NAV, and (ii)
new investors are not admitted at an artificially depressed NAV that still contains the bad asset.
Side-pocketing did not exist as a formal SEBI mechanism before this crisis; IL&FS is the event that
created it. The mechanism bit hardest at schemes structured as **fixed maturity plans (FMPs)** —
closed-end debt funds with a specific maturity date and a promised redemption — because an FMP
holding IL&FS paper due to mature had no flexibility to simply wait out a recovery: unit-holders
were owed cash on a fixed date, and the fund's own illiquid IL&FS exposure could not be converted to
cash on that same schedule, forcing either an early haircut disclosure or a maturity extension,
both of which are the retail-facing symptom of a wholesale-funding freeze that started three layers
upstream in the CP market. `[VERIFY: a list of the specific fund houses and FMP schemes most
exposed to IL&FS paper specifically — as distinct from DHFL, where the exposure map (160+ schemes,
~₹5,200 crore, B3 below) is well documented — could not be independently confirmed this pass; the
side-pocketing mechanism itself and its December 2018 origin date are confirmed.]`

### B2.6 The CP market seizure — autumn 2018

Total outstanding commercial paper in the Indian market fell from a peak of **₹6.40 trillion on 31
July 2018** — the last reading before the crisis became public — to **₹4.15 trillion by 31 December
2019**, a contraction of roughly **35% over seventeen months**, with the sharpest single-month
compression concentrated in the autumn of 2018 itself: CP issuance is reported to have hit an
**eight-year low in September 2018**, the same month as the rating cliff and the trigger default
above. By one contemporary compilation, roughly **₹7 trillion of corporate paper had been
downgraded** across the market in the period following the IL&FS episode (as reported by May 2019)
`[VERIFY: exact reference period and whether this figure captures cumulative downgrades across all
corporate CP/NCD paper market-wide or a narrower NBFC-specific subset]` — directionally consistent
with a market-wide repricing of credit risk, not merely an IL&FS-specific event. The magnitude of
CP spread widening (the price, rather than the volume, of the freeze) is directionally severe in
every contemporary account but a precise, sourced basis-point figure for the autumn 2018 episode
could not be pinned to a single primary series this pass `[VERIFY: CP spread-widening magnitude,
autumn 2018 — the desk's own SC2 data-engineering plan (`partC-data.md` §C.1) treats this as the
freeze index's native variable and defers precise historical reconstruction to the data phase]`.
The volume collapse itself is the cleaner, better-sourced fact, and it is the direct real-world
instance of the mechanism L2's own `partC-data.md` construction targets: "rollover collapse shows as
outstanding falling while rates spike."

### B2.7 The panic marker — NBFC stock crashes

The clearest single equity-market artifact of the autumn 2018 panic is **DHFL's 21 September 2018**
intraday move: the stock fell **~59.7% intraday** on the BSE, hitting a 52-week low of **₹246.25**,
as contagion fear — "an IL&FS-like situation... emerging across NBFCs" in contemporary press
framing — swept the sector on no company-specific news of its own that day; DHFL's own actual
default (June 2019, B3 below) was still nine months away. The stock partially recovered once DHFL's
own management issued reassurances, but the day itself is the sector's cleanest "this could be the
next one" panic print — a pure contagion event, not a fundamentals-driven repricing, and the housing
finance sub-sector broadly sold off in sympathy the same session. `[Note: search-verified magnitude
here is ~60% intraday, not the ~42% figure sometimes cited in secondary discussion of this episode
— the ~60% BSE intraday fall to ₹246.25 is the figure this pass's search corroborated directly from
period reporting and is used here in preference to any unverified alternative.]`

### B2.8 The RBI/NHB liquidity response

The regulatory response ran in two distinct registers — one that arrived quickly and one that
initially did not.

- **What did not come quickly: a dedicated NBFC liquidity window.** In **October 2018**, the RBI
  publicly declined to create a special refinancing window for NBFCs, on the stated ground that
  only around **200 of India's then 11,000+ NBFCs were deposit-taking** and that no systemic case
  had been made — an explicit judgment, in real time, that the crisis was contained. Events over
  the following three years (DHFL, Yes Bank) argued the judgment was premature, though it is also
  true that a blanket across-the-board NBFC liquidity facility was never subsequently created in
  the form initially requested.
- **What did come: targeted, incremental liquidity.** The **National Housing Bank (NHB)**, in
  **November 2018**, requested RBI raise its own refinance limit for housing finance companies from
  ₹300 billion to ₹500 billion, and separately proposed raising the permitted refinance-to-net-owned-
  funds multiple from 10x to 12.5–13x (against HFC sector net owned funds of roughly ₹800 billion at
  the time) — a sector-specific, rather than system-wide, liquidity lifeline. The RBI itself
  conducted large **open market operations (OMOs)** through the winter of 2018–19 explicitly framed
  in press coverage as addressing the liquidity deficit "amid concerns of a liquidity crisis...
  after the default by IL&FS Group companies": December 2018 OMO purchases totalled **₹50,000
  crore** for the month, January 2019 added a further **₹50,000 crore** (five auctions of ₹10,000
  crore each), and February 2019 added **₹37,500 crore** — a cumulative injection on the order of
  **₹2.5 lakh crore for the fiscal year** by one contemporary compilation. **A full year later**, the
  government moved on the credit-risk-sharing side directly: the **Partial Credit Guarantee Scheme**,
  announced in the July 2019 Budget and formally issued **10 August 2019**, let public-sector banks
  purchase high-rated pooled assets from financially sound NBFCs/HFCs (rated BBB+ or better, and
  eligible even if the originator had slipped into the RBI's SMA-0 early-stress category any time in
  the year before 1 August 2018) with a government guarantee covering first loss up to **10% of
  fair value, or ₹10,000 crore, whichever was lower**, against a total programme size of **₹1 lakh
  crore**; the purchase window ran through **30 June 2020** or until the ₹1 lakh crore was
  exhausted, whichever came first. **L2/L10 lesson.** The sequence — an initial "no systemic
  window" judgment, followed within weeks by system-wide OMO liquidity, followed within a year by a
  credit-risk-sharing scheme targeted specifically at the NBFC funding-freeze mechanism — is itself
  a template: the fast, blunt tool (OMO liquidity) arrived in days-to-weeks; the precise, targeted
  tool (the PCG scheme, addressing the actual asset-quality uncertainty rather than just system
  liquidity) took roughly eleven months, a lag this desk should read as structural rather than
  IL&FS-specific — precise, targeted, legislated schemes cannot move at OMO speed even when the
  underlying market stress is unambiguous within days.

### B2.9 Resolution — the long tail

IL&FS resolution has run for close to eight years and remains incomplete as of this writing. As of
**March 2025**, the group had discharged **₹45,281 crore** to creditors, with resolution completed
across **197 entities**; by **September 2025**, cumulative repayment had reached **₹48,463 crore**
(~80% of the ₹61,000 crore internal resolution target); by **June 2026**, the most recent status
filed before the NCLAT, cumulative repayment stood at **₹50,387 crore — 82.6% of the ₹61,000 crore
target**. Of the total ~₹91,000 crore owed, **~88.4% (~₹57,000 crore)** of the specific debt owed to
public-sector banks and financial institutions had been serviced through a mix of asset
monetization/InvIT transfers (₹21,581 crore), auto-debits and "green entity" servicing (₹9,026
crore), and interim distributions to external creditors (₹14,674 crore). **L2/L10 lesson, closing
the anatomy.** Set against the ratings-cliff timeline in B2.2 — five weeks from first crack to
formal default — the resolution timeline is the mirror-image fact this desk should carry forward
into any funding-run design: **a shadow-credit run can destroy a AAA rating in five weeks and take
the better part of a decade to substantially resolve**, an asymmetry between the speed of the
freeze and the speed of the workout that recurs, in different degree, in every case below.

---

## B3. DHFL and the second leg, 2019–2021 — a slow-motion resolution vs. IL&FS's takeover

Dewan Housing Finance Corporation (DHFL) was the second, and in retail terms more consequential,
leg of the same shadow-credit sub-cycle — its funding stress became visible within the same autumn
2018 panic (B2.7) but its own default, freeze, and resolution ran on an entirely different
institutional track from IL&FS's.

**CP stress to default, June 2019.** In June 2019, DHFL defaulted on a **₹1,000 crore-order bond
repayment**, the first of a series of missed payments; **CARE downgraded DHFL's fixed-deposit
programme from CARE A to CARE BBB−**, a cut that under SEBI/RBI norms compelled DHFL to stop
accepting fresh deposits and to halt both premature withdrawals and renewals of existing ones —
the FD-holder-facing mechanism below.

**The FD freeze.** DHFL had raised roughly **₹800 crore in public fixed deposits** placed with the
company by close to a dozen bank-adjacent channels and directly by retail depositors; once the CARE
downgrade forced a halt to withdrawals, FD holders were effectively frozen alongside the company's
banks and larger institutional lenders inside the subsequent resolution process — a retail-investor
lock-in with no equivalent in the IL&FS case, where the comparably retail-facing damage ran through
mutual-fund NAVs (B2.5) rather than direct fixed deposits, because IL&FS/IFIN's own deposit-taking
footprint was smaller.

**The mutual-fund exposure map — better documented than IL&FS's own.** More than **160 mutual fund
schemes** carried DHFL paper, totalling roughly **₹5,200 crore** of investor money; one high-profile
episode saw DSP Mutual Fund sell part of its DHFL debt holdings into the secondary market in June
2019, an action contemporary reporting directly credited with helping trigger the sharpest leg of
the DHFL stock's own subsequent crash. SEBI's side-pocketing mechanism, created for IL&FS the
previous December, was applied again here — the second live use of a tool invented six months
earlier for exactly this recurring mechanism.

**First financial-service-provider into the IBC, November 2019.** In November 2019, the RBI —
acting under **Section 45-IE of the RBI Act** — superseded DHFL's board, appointed an administrator,
and referred the company into insolvency proceedings under the **Insolvency and Bankruptcy Code**:
the **first time** the IBC had been invoked against a financial-service provider rather than an
ordinary corporate borrower, a genuinely new use of the statutory machinery distinct from IL&FS's
own NCLT-board-supersession route (B2.4) — the two large shadow-credit failures of this single
cycle were resolved through **two different institutional mechanisms**, one company-law (IL&FS), one
insolvency-law (DHFL), a design choice this desk should read as evidence that India's own workout
toolkit for a shadow-credit failure was still being invented case by case as recently as 2018–19,
not applied from an existing playbook.

**Piramal acquisition, 2021, and the retail-bondholder haircut.** Piramal Enterprises completed the
acquisition of DHFL on **30 September 2021**, paying total consideration of **₹34,250 crore**
(₹14,700 crore upfront cash plus ₹19,550 crore of new 10-year NCDs at 6.75%/year); together with
DHFL's own cash balance (~₹3,800 crore), creditors recovered an aggregate **~₹38,000 crore** against
DHFL's total claims — a recovery of roughly **46%** across DHFL's ~70,000 creditors in aggregate,
though **retail NCD holders specifically faced haircuts in the 65–75% range** by some creditor
accounts raised during the resolution process itself (a disputed, rather than final, figure — the
aggregate 46% recovery and the retail-specific 65–75% haircut both circulated as claims during the
process and are not fully reconciled here `[VERIFY]`). **L2/L10 lesson.** DHFL is this monograph's
cleanest India instance of the **slow-motion** resolution mode: two full years from board
supersession (November 2019) to a completed change-of-control transaction (September 2021), against
IL&FS's own comparatively fast October 2018 board takeover — the difference being that DHFL's
statutory route (IBC, requiring a competitive resolution-plan process, NCLT approval, and surviving
a legal challenge from 63 moons Technologies over the process itself) is inherently slower than a
direct government board supersession, even though both mechanisms ultimately answer the same
underlying funding-run failure.

---

## B4. The chain into banks: Yes Bank, March 2020, and the AT1 write-down — the shadow cycle's third leg

Yes Bank's March 2020 collapse is not a separate story from IL&FS/DHFL — it is this same
shadow-credit cycle's third and final leg, transmitted from the non-bank sector into a scheduled
commercial bank through a specific, documented bridge: **developer and NBFC exposure**. Yes Bank had
grown an aggressive corporate book through the 2010s that included substantial lending to stressed
developers and NBFCs — DHFL among its largest such exposures — meaning DHFL's own June 2019 default
(B3) directly impaired one of Yes Bank's own largest counterparty books at the exact moment the
bank's broader asset quality was already deteriorating.

**Moratorium and reconstruction.** On **5 March 2020**, the RBI placed Yes Bank under a 30-day
moratorium, superseded the bank's board, capped depositor withdrawals at **₹50,000**, and published
a draft reconstruction scheme the following day (6 March); on **14 March**, under that scheme, the
bank took a **permanent write-down of ₹8,415 crore (~$890 million) of Additional Tier-1 (AT1)
capital** — an action that, by inverting the conventional creditor-priority order (equity holders
were not wiped out even as AT1 bondholders were), became the subject of prolonged litigation: the
Bombay High Court set aside the write-off, ruling the RBI-appointed administrator had exceeded his
powers, and the matter remained before the Supreme Court of India as of 2026 `[VERIFY: current
status of the Supreme Court proceeding — search results confirm the matter was pending as of
2026 with no final resolution located this pass]`. The State Bank of India ultimately led a capital
infusion of **₹7,250 crore** for a 45% stake in the reconstructed bank, joined by a consortium of
other private banks. Yes Bank's stock, which had traded near ₹404 at its own peak `[VERIFY: exact
peak date — accounts vary between August 2018 and August 2019]`, fell to a record low of **₹5.65 in
March 2020** — a fall exceeding **98%** from peak.

**Why this is the cycle's third leg, not a separate story.** Three features tie Yes Bank directly to
the IL&FS/DHFL chain rather than treating it as an independent bank failure: (i) the proximate
counterparty-quality trigger runs through the same developer/NBFC exposure this whole monograph
tracks, with DHFL specifically named as a major Yes Bank credit; (ii) the AT1 write-down is a direct
structural echo of IL&FS's own "who actually bears the loss, and in what order" problem — just as
IL&FS's CP holders (mutual funds, ultimately retail unit-holders) absorbed losses ahead of what a
naive priority ordering would predict, Yes Bank's AT1 holders absorbed losses ahead of equity, a
recurring pattern of loss allocation landing on instruments that looked senior-ish to their holders
until a resolution authority decided otherwise; (iii) the timing itself — Yes Bank's moratorium
landed within days of COVID-19's own market shock, meaning the shadow-credit cycle's slowest-to-
resolve leg closed just as an entirely unrelated, much faster shock began, a sequencing this desk's
own contract (§7, item 8: "fast crashes cannot be met by cycles") already treats as a distinct
regime the credit-cycle apparatus is not built to anticipate.

---

## B5. The 2013 mini-squeeze — a RATES signature, not a CREDIT signature

The 2013 "taper tantrum" episode belongs in this monograph as the clean **negative control**: it
produced real, sharp CP/CD funding stress, but through an entirely different mechanism than 2018's,
and the desk should never conflate the two signatures.

**The trigger and the tool.** Following the Fed's May 2013 taper announcement, the rupee came under
sustained depreciation pressure; the RBI's defense, rather than a credit-quality intervention, was a
**rates** operation: in **July 2013**, the RBI raised the **Marginal Standing Facility (MSF)** rate
to **300 basis points above the repo rate** (repo then at 7.25%, MSF effectively 10.25%) —
deliberately inverting the normal policy corridor so that the MSF's upper bound, not the repo rate,
became the effective marginal cost of overnight bank funds, an extraordinary, explicitly temporary
measure aimed at choking off rupee-shorting speculative liquidity. The measure was gradually
unwound over the following months as the rupee stabilized and Raghuram Rajan took over as Governor
in September 2013, restoring repo as the effective policy anchor.

**NBFCs in 2013 vs. 2018 — different signatures.** The 2013 episode raised the cost of short-term
funds system-wide — banks, NBFCs, and CP issuers all faced a genuinely higher marginal borrowing
rate, mechanically, by policy design — but it did **not** involve a credit-quality collapse, a
ratings cliff, a specific borrower default, or a government takeover: no NBFC's solvency was
publicly questioned, no CP issuer defaulted, and no mutual fund side-pocketed anything, because
none of those instruments existed as a tool yet and none of the underlying triggering events
(a specific default) had occurred. The desk's own SC1 trial (`shadow-RESULTS.md`) reports the Taper
window (2013-05 to 2014-04) as the mildest of its four comparator prints by far — SMB −1.7% (49th
percentile, essentially the median), market +7.7% (57th percentile) — a result entirely consistent
with a **rates squeeze that raised funding costs without impairing credit quality**, versus IL&FS's
own window (SMB −24.8%, 18th percentile) where a specific credit event cascaded into a broad
market decline. **L2/L10 lesson.** A funding-stress signature keyed only to CP/CD spread widening
would have fired in both 2013 and 2018, but the two episodes require entirely different regime
responses: 2013's stress resolved once the rates operation was unwound (a policy-reversible,
transient state); 2018's stress required a ratings collapse, a government takeover, and years of
resolution to clear (a credit-impairment state). This is the strongest available argument for why
`partC-data.md`'s freeze index (CP spread + rollover-ratio z-scores) must be read jointly with the
credit-side ratings/default confirms `partC-data.md` also specifies, never on the funding-spread
leg alone — a pure rates-driven CP squeeze and a credit-driven CP freeze can look similar in the
spread series and mean opposite things for what regime action should follow.

---

## B6. Pre-history: the 1990s NBFC boom-bust and the regulatory ratchet

India's own first full shadow-credit cycle predates the atlas's own dating (2014→2018→2020, n=1
"clean" episode) by two decades, and the desk should read this pre-history as evidence the "clean"
count understates true persistence of the mechanism even while it correctly flags the post-1991
liberalization-era episode as the first one the model's own data can measure.

**The boom and the CRB Capital catalyst.** Post-1991 liberalization created a large, lightly
regulated population of deposit-taking NBFCs that competed aggressively for public deposits through
the mid-1990s. **CRB Capital Markets**, a high-profile NBFC, began defaulting on payments to lenders
in **1996**; when its cheques started bouncing, depositors converged on its branches, and a
subsequent investigation revealed the company had routed public deposit money through shell
companies. Estimated stakeholder losses from the CRB episode alone ran to roughly **₹1,200 crore**.

**The purge.** CRB's collapse triggered a nationwide run on deposit-taking NBFCs broadly — depositors
who had never heard of CRB specifically nonetheless pulled money from comparable companies on the
fear that any of them could be the next one, and "hundreds of companies downed their shutters" in
the aftermath — a 1997 instance of exactly the same contagion mechanic DHFL's stock experienced on
21 September 2018 (B2.7), two decades and one entirely different funding instrument (public
deposits vs. mutual-fund-held CP) apart. A precise, sourced count of the registration collapse
(how many NBFC registrations were cancelled or lapsed specifically in the 1997–99 window) could
not be independently confirmed this pass `[VERIFY: precise NBFC registration/deposit-taking-company
count before and after the 1997 purge — search located qualitative confirmation of "hundreds of
companies" shutting down but not a single authoritative before/after registration count]`.

**The regulatory ratchet — RBI Act amendments, 1997.** The country-wide furore forced the RBI Act,
1934 to be amended in **1997**, giving the RBI comprehensive new supervisory powers over NBFCs for
the first time — mandatory registration (a **Certificate of Registration** requirement), minimum
**Net Owned Fund** thresholds, and detailed "entry point norms" governing the manner, form, and
quantum of public deposit acceptance. In **January 1998**, the RBI issued the first comprehensive
regulatory framework built on these new powers, categorizing NBFCs into (i) public-deposit-accepting
companies, (ii) non-deposit companies engaged in loan/investment/hire-purchase/leasing business, and
(iii) non-deposit core investment companies — the direct institutional ancestor of the far more
granular **scale-based regulation** framework the RBI would issue 24 years later (B9 below). **L2/L10
lesson.** The 1997 amendment is this record's cleanest demonstration of the regulatory ratchet
pattern that recurs through every case in this monograph: a shadow-credit run forces a **new layer**
of supervisory architecture that did not previously exist (registration/NOF norms in 1997; SEBI
side-pocketing in 2018; scale-based "upper layer" supervision in 2021; the Nov-2023 risk-weight
tightening and the 2023 default-loss-guarantee rules — B9), each new layer addressing the specific
failure mode the most recent crisis exposed, none of them anticipating the next one's specific
mechanism in advance.

---

## B7. Mirror: the US shadow-banking run, 2007–08 — securitization at the center, not CP-MF

The United States' 2007–08 experience is the cross-country mirror this desk should read for the
**mechanism**, not for magnitude: the funding instrument at the center was securitized asset-backed
commercial paper (ABCP) and the tri-party repo market, rather than India's own CP-held-by-mutual-
funds chain, but the run dynamic — short-term rollover funding for long-dated, hard-to-value assets,
collapsing the instant valuation confidence cracked — is the same mechanism this whole monograph
tracks, expressed through a different plumbing.

**The ABCP freeze, August 2007.** On **9 August 2007**, BNP Paribas halted withdrawals from three
funds holding US subprime-mortgage-related securities and suspended net-asset-value calculation,
citing an inability to value the underlying assets — the single most-cited "start date" of the
global financial crisis. The overnight ABCP-to-Fed-funds spread widened from roughly **10 basis
points to 150 basis points within a single day** of the announcement; total ABCP outstanding fell
**37%, from $1.18 trillion (August 2007) to $745 billion (August 2008)** — a slower-motion, but
ultimately deeper, contraction than India's own 2018 CP market (which fell ~35% over roughly the
same order of elapsed time, B2.6). The mechanism behind the freeze's persistence: because banks
held no regulatory capital against ABCP-conduit assets (the entire point of the off-balance-sheet
structure), a conduit unable to roll its ABCP had no readily available capital cushion to absorb the
gap, forcing either fire-sale asset liquidation or a sponsor-bank bailout of its own "off-balance-
sheet" vehicle — precisely the opacity mechanism regulators worldwide subsequently moved against
(Basel III's securitization capital rules; China's 2018 asset-management rules, B8 below).

**The repo haircut spiral — Gorton and Metrick's reading.** Gary Gorton and Andrew Metrick's
"Securitized Banking and the Run on Repo" (*Journal of Financial Economics*, 2012) frames the 2007–
08 panic as fundamentally a run on the **sale-and-repurchase (repo) market** — the very large,
short-term financing market underpinning securitization activity broadly — rather than (or in
addition to) a deposit run in the classical sense. As concerns about the liquidity and true value of
mortgage-backed collateral spread, lenders progressively raised **repo haircuts** (the amount of
collateral required per dollar borrowed); each increase in haircuts forced borrowers to post more
collateral or delever, which in a system already leveraged against the same collateral pool
mechanically forced further asset sales, further price declines, and further haircut increases — a
self-reinforcing spiral that, on Gorton-Metrick's own account, rendered the US banking system
"effectively insolvent for the first time since the Great Depression" purely through this collateral
mechanism, independent of any single institution's own credit losses.

**Reserve Primary breaks the buck, September 2008.** The **Reserve Primary Fund**, at the time the
world's third-largest money-market fund with $62.5 billion in assets, held a **$785 million**
position in Lehman Brothers debt when Lehman filed for bankruptcy on **15 September 2008**. On **16
September 2008**, Reserve announced the fund had "broken the buck" — its net asset value per share
fell below $0.995 — becoming only the second money-market fund in US history, and the first to
affect a broad investor base, to do so. Redemption requests exceeded **$40 billion within two days**,
reaching roughly a quarter of the fund's assets by the afternoon of the announcement and more than
half by the following day — a run that, unlike a bank run, had no deposit-insurance backstop and no
central-bank lender-of-last-resort facility specifically designed for money-market fund redemptions
at that point, forcing the US Treasury to introduce an emergency temporary guarantee programme for
money-market funds within days. **L2/L10 lesson.** The US case is this monograph's clearest
demonstration that the same funding-run mechanism can be triggered through a completely different
instrument (repo/ABCP/MMF rather than CP-held-by-debt-mutual-funds) and still produce the identical
signature: a valuation shock at one node propagating through a chain of intermediaries each holding
short-dated claims on longer-dated, suddenly-uncertain collateral, with the terminal holder (a
retail-facing fund) absorbing the visible loss last and most publicly — precisely the same structure
India's own MF-side-pocketing mechanism (B2.5) was invented to manage a decade later.

---

## B8. Mirror: China's trust/WMP cycle — the implicit-guarantee unwind

China's shadow-banking sector supplies the mirror case for a **wealth-management-product** funding
chain rather than a CP-mutual-fund one, and its central lesson — an implicit, never-formally-stated
government guarantee can suppress a run for years before an explicit regulatory unwind forces the
issue — has no clean India parallel but bears directly on how this desk should read any future
India shadow-credit episode's own "who actually absorbs the loss" question.

**Trust products and wealth-management products.** Chinese banks and trust companies sold enormous
volumes of WMPs to retail and corporate savers, offering yields above deposit-rate ceilings by
funneling the proceeds into trust loans, corporate bonds, and (increasingly through the 2010s)
property-developer financing — India's own NBFC-to-developer channel's structural cousin, but funded
through bank-distributed retail products rather than CP held by mutual funds. Crucially, WMPs were
sold and widely understood by buyers to carry an **implicit guarantee**: if the underlying assets
underperformed, the issuing bank or trust would quietly make investors whole rather than let a
retail-facing product visibly default, sustaining demand for products whose actual credit risk was
never transparently priced.

**The 2018 asset-management rules.** On **27 April 2018**, the People's Bank of China, the banking
and insurance regulator (CBIRC), the securities regulator (CSRC), and the state foreign-exchange
administration jointly issued the **Guiding Opinions on Regulating the Asset Management Business of
Financial Institutions** — explicitly **prohibiting implicit guarantees on newly issued products**
and barring financial institutions from using proprietary or other managed funds to cover a
redemption shortfall. The rules applied uniformly across the previously fragmented product universe
— bank WMPs, mutual funds, and trust plans alike — aiming to break the "implicit guarantee of
repayment that has fueled risk-taking and built a culture of complacency" among Chinese retail
savers, in the regulator's own explicit framing.

**Evergrande's commercial-paper web.** China Evergrande's own funding structure by the early 2020s
extended this same implicit-guarantee logic to its own commercial paper, trust products, and
in-house WMPs sold directly to employees, suppliers, and retail clients — more than **80,000
people** bought Evergrande-issued wealth products, drawn by yields approaching **12%/year** plus
promotional gifts, on the implicit strength of "China's top-selling developer" rather than any
transparent credit assessment. As Evergrande's own liquidity crisis deepened through 2021,
repayments to WMP holders were suspended; the company began a phased repayment plan (a first 10%
instalment paid in September 2021) before Fitch downgraded it to "restricted default" on **9
December 2021** and S&P followed with "selective default" the same month over a missed coupon —
Evergrande becoming, by year-end, the **twelfth** Chinese property developer to default on bonds in
2021 and by far the largest. (The commodity monograph's own China case already covers Evergrande's
property-sector and commodity-demand dimensions in full; this Part's own addition is narrowly the
CP/WMP funding-web mechanism, cross-referenced rather than duplicated.)

**The implicit-guarantee unwind, still running.** Unlike IL&FS's five-week ratings cliff (B2.2),
China's unwind has been a multi-year, policy-paced process precisely because the 2018 rules targeted
**newly issued** products, leaving a large stock of legacy WMPs to run off gradually rather than
forcing an immediate system-wide repricing — the same "state-directed, policy-paced repair" pattern
the capex-deep monograph's own China case (its case 6) already documents for China's real-side
capacity-cut programme, now shown to apply equally to the financing side. **L2/L10 lesson.** China
supplies the clearest available evidence that an implicit guarantee, once withdrawn by explicit
regulatory fiat rather than by a market-discovered default, produces a **slower**, not faster,
repricing than India's own market-discovered-default pattern — the opposite of what a naive
"administrative intervention should resolve things quickly" prior would predict, and a direct
structural parallel to the credit-cycle monograph's own observation (via its own China case) that a
state-directed system suppresses the market-based signals (bond spreads, equity drawdowns) this
desk otherwise relies on to date a bust in real time.

---

## B9. The current state, 2021–2026, and where the next fragile node plausibly sits

**Scale-based regulation, October 2021.** The RBI issued a comprehensive revised regulatory
framework for NBFCs on **22 October 2021**, replacing the ad hoc 1998-era categorization (B6) with a
four-tier structure — Base Layer, Middle Layer, **Upper Layer**, and Top Layer — under which NBFCs
are scored annually (70% weight on quantitative parameters, 30% on qualitative ones) and assigned to
the Upper Layer if they cross the threshold; the ten largest NBFCs by asset size are placed in the
Upper Layer **automatically**, regardless of score. Upper Layer status carries enhanced prudential
requirements for a minimum of **five years**, even if the NBFC's own metrics later fall below the
qualifying threshold — a deliberately sticky classification designed against exactly the kind of
"we didn't think this one was systemic" judgment the RBI itself voiced about NBFCs broadly in
October 2018 (B2.8). The first Upper Layer list, published in **2022**, named **15 NBFCs**.

**Co-lending growth.** The RBI's original 2020 Co-Lending Model, restricted to priority-sector
lending between banks and NBFCs, has been substantially widened: the **Co-Lending Arrangements
Directions, 2025** (effective **1 January 2026**) extend the framework to **all** regulated
entities and **all** loan segments, not merely priority-sector loans, while introducing a minimum
10% retention requirement per originating entity, a 15-calendar-day mandatory transfer window, and —
notably — an explicit **Default Loss Guarantee (DLG)** provision capped at 5%, folding the digital-
lending FLDG framework (below) directly into the co-lending structure. Market estimates already put
**75% of bank co-lending volume** in non-priority-sector loans even before the 2025 Directions
formally permitted that scope — the regulation, in other words, is catching up to a market practice
that had already outgrown its original mandate, the same lagging-regulator pattern this monograph
documents in every prior episode.

**The November 2023 risk-weight increase — the countercyclical move this time.** On **16 November
2023**, the RBI raised risk weights on unsecured consumer credit exposures of both banks and NBFCs
by **25 percentage points, to 125%** (for bank personal loans and NBFC retail loans excluding
housing, education, vehicle, and gold-backed loans), and separately raised risk weights on
bank-to-NBFC exposures by the same 25 points over and above the exposure's own external rating, and
on credit-card receivables to **150% (banks)** and **125% (NBFCs)** — implemented by **29 February
2024**. This is, structurally, the single clearest instance in this entire monograph of a
**pre-emptive, countercyclical** regulatory move: unlike the 1997 RBI Act amendment (reactive to
CRB Capital's collapse), the 2018 liquidity scramble (reactive to IL&FS), or SEBI's side-pocketing
rule (reactive to IL&FS and DHFL), the November 2023 tightening was explicitly justified by the RBI
as addressing unsecured/retail credit growth it judged to be **overheating** — the desk's own dossier
03 already flags the same episode (non-food credit growth accelerating from 16.0% in Aug-2022 to
20.2% by Mar-2024, credit-deposit ratio hitting an all-time high near 80% by Mar-2024) as the
institutional confirmation of exactly the composition-signal design that dossier argues for. Whether
the move was well-timed is now testable against subsequent events: the sector it targeted
(unsecured retail, disproportionately routed through NBFC/microfinance channels) is precisely the
one that showed acute stress through 2024–25 (below) — consistent with, though not proof of, the
tightening having correctly identified the fragile node roughly a year before the stress became
visible in asset-quality data. `[Note: RBI subsequently eased elements of this risk-weight regime in
2025 as microfinance-sector stress mounted — a partial reversal this desk should read alongside the
2023 tightening as one continuous countercyclical policy arc, not two separate events;
[VERIFY: precise date and scope of the 2025 easing].`

**Digital lending and FLDG rules.** The RBI's **September 2022** digital-lending guidelines first
required that first-loss-default-guarantee (FLDG) arrangements between regulated lenders and
lending-service-provider fintechs comply with the existing **synthetic-securitisation** prohibition
under the 2021 Securitisation of Standard Assets Directions — effectively banning FLDG as it was
then structured. The RBI reversed course with dedicated **Default Loss Guarantee (DLG) Guidelines**
issued **8 June 2023**, formally permitting DLG/FLDG arrangements between regulated entities and
between REs and LSPs, subject to a hard cap of **5% of the outstanding loan portfolio** — the same
5% figure the 2025 Co-Lending Directions above reuse, unifying the risk-sharing cap across both
frameworks. This is a direct regulatory response to a funding-structure innovation (fintech-
originated, NBFC-funded, risk-shared lending) that grew faster than the existing rulebook
anticipated — the 2023 rules are, in effect, this decade's version of the 1998 categorization
framework: codifying a structure the market had already built.

**Microfinance stress, 2024–25.** India's microfinance sector showed acute, rapid asset-quality
deterioration through FY25: gross NPAs rose to roughly **₹55,000 crore (~14.8% of gross loans)** by
March 2025, from a much lower base the year before `[VERIFY: one industry compilation cites a
distinct 16% gross-NPA figure for the same date — the two readings are not reconciled here and may
reflect different scope (MFI-only vs. broader microfinance-adjacent lending)]`; loans overdue
30+ days (portfolio-at-risk) rose from **2.1% (FY24) to 6.2% (FY25)**, and the stricter 90+-day NPA
benchmark rose from **1.6% to 4.8%** over the same year. The sector's gross loan portfolio
contracted, from **₹4.24 trillion to ₹3.75 trillion**, and disbursals fell from **₹1.50 trillion to
₹1.12 trillion** — a genuine credit contraction, not merely a slowing growth rate. Contemporary
analysis attributes the stress substantially to **borrower over-leveraging** (multiple concurrent
loans across lenders to the same low-income borrower, a structural echo of the "who actually holds
the risk" opacity this whole monograph documents) compounded by a weak FY25 growth backdrop (GDP
growth at a four-year low of 6.4%) and localized shocks (heatwaves, floods, election-period
disruption to collection cycles). The industry body MFIN introduced a tightened self-regulatory
framework effective **January 2025** in direct response.

**Where the next fragile node plausibly sits — an honest scenario listing, no dates.** Consistent
with the Contract's own instruction that forward-looking judgement belongs to Stage 2, not Stage 1,
the following is offered as narrative context (CONTEXT-tier only, no allocation authority), not a
forecast: (i) **unsecured retail and microfinance-adjacent lending**, given the 2024–25 stress
documented above and the sector's structurally thin per-borrower underwriting visibility even after
the Nov-2023 tightening; (ii) **co-lending and FLDG arrangements themselves**, precisely because the
2025 Directions' expansion into non-priority-sector, all-segment lending recreates, in a new
wrapper, the "who actually bears first loss and can regulators see it" opacity every prior episode
in this monograph eventually exposed; (iii) **Upper-Layer NBFCs' continuing wholesale/CP
dependence**, since enhanced supervision addresses solvency and governance more directly than it
addresses the underlying maturity mismatch the atlas's own mechanism statement names as structural;
(iv) **developer/HFC exposure re-emerging** if the 2021–2026 residential upcycle the property-cycle
and capex monographs both document turns, given how directly the 2018 freeze transmitted through
exactly that channel; and (v) **global-cycle-driven funding-cost spillover** — an FPI-outflow or
dollar-tightening episode (L9) raising NBFC wholesale funding costs faster than balance sheets can
adjust, a channel this desk's own global-financial-cycle seat is built to monitor but which this
monograph's own India cases have not yet produced a clean instance of. None of these carries a
probability estimate or a timing claim; they are listed because the atlas's own instruction is that
"knowing why a cycle was rejected teaches more than knowing one was accepted" — the honest
complement here is that knowing where a recurring mechanism's structural preconditions currently
sit teaches more than pretending the cycle has been fully retired by the last round of regulation.

---

## B10. Synthesis

| Episode | Fragile funding structure | Trigger | Freeze-to-macro lag | Regulatory response | What L2 would have needed to see it EARLY |
|---|---|---|---|---|---|
| **IL&FS, 2018** | 300+-entity holding group funded via group-level CP/ICDs against long-dated infra assets; AAA/A1+ ratings resting on unmapped intra-group cross-guarantees | SIDBI/CP payment misses (late Aug 2018) → 14 Sep formal default → 17 Sep rating cut to 'D' | **~12 months** to become macro (SC1's own window, 2018-09→2019-08: market return −20.2%, 16th percentile) | NCLT board supersession (1 Oct 2018); OMOs (~₹2.5 lakh cr FY19); PCG scheme (Aug 2019, ₹1 lakh cr); SEBI side-pocketing (Dec 2018) | Issuer-level ICD/CP rollover-calendar visibility (dark in real time, per `partC-data.md` C.5) and a bank+NBFC combined credit aggregate months before the Aug-2018 rating crack, not a rating itself (ratings lagged the default by weeks) |
| **DHFL, 2019–21** | Bank/NBFC lending + ~₹800cr public FDs + CP, real-estate-adjacent asset book | CARE downgrade forces FD-programme freeze (Jun 2019) | ~2 years to a completed resolution (board super­session Nov 2019 → Piramal close Sep 2021) | RBI board supersession under RBI Act §45-IE; first FSP into IBC; SEBI side-pocketing (2nd use) | Cross-holding map of IL&FS-exposed lenders/MFs to DHFL — the 21-Sep-2018 stock panic (B2.7) was itself the leading signal, nine months before DHFL's own default |
| **Yes Bank, 2020** | Corporate book concentrated in stressed developers/NBFCs (incl. DHFL) funded via ordinary deposits + AT1 capital | DHFL-linked asset-quality deterioration culminating in a Mar-2020 moratorium | Essentially immediate once the moratorium hit (bank run risk is same-day by construction) | RBI moratorium + administrator + reconstruction scheme; AT1 write-down (₹8,415cr, litigated since) | Counterparty-concentration mapping of bank exposure to the *already-known* 2018-19 stressed-NBFC list — the DHFL linkage was public well before Mar-2020 |
| **2013 mini-squeeze** | System-wide CP/CD funding, no specific credit event | Fed taper announcement → rupee defense | No macro propagation (SC1: market +7.7%, 57th pctile) | MSF spiked 300bp (Jul 2013), unwound within months | Distinguishing a **rates**-driven spread widening from a **credit**-driven one — the same spread series looks similar; only the ratings/default confirm layer tells them apart |
| **CRB Capital / 1990s purge** | Deposit-taking NBFCs, thin regulation, no NOF/registration regime | CRB's 1996 payment defaults exposed shell-company fund diversion | Nationwide depositor run within months (qualitative; no free precise series) | RBI Act amended 1997 (mandatory registration, NOF norms); Jan-1998 categorization framework | No free real-time series exists pre-1998; the design's own honest limit — this episode is a narrative prior only, never a backtestable one |
| **US 2007–08** | ABCP conduits + tri-party repo funding securitized MBS/CDOs | BNP Paribas fund freeze, 9 Aug 2007 | Contained to financial-sector stress for ~13 months before Lehman (Sep 2008) turned it systemic | Fed emergency facilities; MMF temporary guarantee (Sep 2008); later Basel III securitization capital rules | Repo-haircut trend + ABCP-outstanding trend (both eventually became the standard 2007-08 US early-warning series) — mirrors India's own freeze-index construction (CP outstanding + spread) |
| **China trust/WMP** | Bank/trust-distributed WMPs funding developer + LGFV lending under an implicit repayment guarantee | 2018 asset-management rules ban new implicit guarantees; Evergrande's own WMP web unravels 2021 | Multi-year, policy-paced — still unresolved as of 2026 | State-directed rules (Apr 2018); developer defaults managed via court liquidation (Evergrande, Jan 2024) rather than a single crisis date | Not transferable to India — administrative suppression of market signals means no free market-based India-style CP/MF proxy exists for this mechanism |

**The one-line synthesis.** Every episode in this record is the same funding-run mechanism —
short-dated rollover finance against long-dated, hard-to-value assets — wearing a different
instrument (CP-and-mutual-funds in India 2018, public deposits in India 1997, ABCP-and-repo in the
US 2007–08, WMPs-and-trusts in China) and a different institutional resolution channel (NCLT board
supersession, IBC referral, RBI moratorium, a regulatory amendment, a court-ordered liquidation).
The design lesson this Part hands back to L2 and L10 is the one SC1 already forced into the open:
the run itself moves in **weeks** (IL&FS's own ratings cliff, B2.2); the equity market only fully
prices the consequence in **roughly a year** (SC1's own 12-month window); and full resolution takes
**years to a decade** (IL&FS's own 2018→2026 resolution tail, still at 82.6%). A regime system that
can only see the middle of that three-speed structure — an annual-cadence equity read — will always
be too slow to matter and too fast to have resolved; the freeze-index construction `partC-data.md`
already specifies (CP spread + rollover ratio, daily-to-weekly cadence) is aimed squarely at the
first, fastest layer, precisely because that is the only layer at which this mechanism is still
actionable rather than merely diagnostic after the fact.

---

## References

Wikipedia, *Infrastructure Leasing & Financial Services*; Moneylife, various 2018–19 reporting on
IL&FS group debt and subsidiary structure; Business Standard, contemporaneous 2018 reporting on
IL&FS rating downgrades (CARE 16 Aug 2018; ICRA 8 Sep 2018; ICRA/CARE 'D' cut 17 Sep 2018), SIDBI
ICD defaults, IL&FS Energy Development default, and the 1 Oct 2018 NCLT board supersession. ·
BusinessToday, coverage of the government's NCLT petition and the six-member Kotak-led board. ·
Mondaq / Wikipedia, *Satyam scandal* and its Company Law Board precedent. · Business Standard,
"NBFCs crash: Here's why DHFL tanked over 60% in trade today" (21 Sep 2018). · Business Standard/
PTI, coverage of RBI's Oct 2018 refusal of a special NBFC liquidity window; NHB's Nov 2018 refinance
request; RBI OMO purchase schedules, Dec 2018–Feb 2019. · PIB / PMO India / Business Standard,
Cabinet approval of the Partial Credit Guarantee Scheme (10 Aug 2019). · IBC Laws / BusinessToday,
DHFL's Jun 2019 default, FD freeze, and Nov 2019 RBI Act §45-IE board supersession into IBC. ·
Business Standard / Piramal Enterprises investor presentation, DHFL acquisition completion (30 Sep
2021) and creditor recovery figures. · EliScholar (Yale Journal of Financial Crises), *India: Yes
Bank Moratorium, 2020* and *Yes Bank Restructuring, 2020*; Wikipedia, *Yes Bank AT1 bond
controversy*; Business Standard, Yes Bank AT1 Supreme Court litigation status. · IIBF Vision
(October 2013), RBI Mid-Quarter Monetary Policy Review; contemporary reporting on the Jul 2013 MSF
rate hike to 300bp over repo. · Vinod Kothari Consultants, *NBFC Regulation turned sixty*; Shardul
Amarchand Mangaldas, *Amendments to RBI Act 1934 to give greater control over NBFCs*; BusinessToday,
*The Shadow Banking Crisis* (CRB Capital Markets, 1997 RBI Act amendment). · Wikipedia, *Asset-backed
commercial paper*; Berkeley Law, *Commercial Paper During the Financial Crisis of 2007-2009*
(BNP Paribas, 9 Aug 2007, ABCP spread/outstanding data). · Gorton, G. & Metrick, A. (2012),
"Securitized Banking and the Run on Repo," *Journal of Financial Economics* 104(3): 425–451. ·
Wikipedia, *Reserve Primary Fund*; EliScholar, *United States: Reserve Primary Fund Suspension,
2008*. · Norton Rose Fulbright / Conventus Law, China's Apr 2018 *Guiding Opinions on Regulating the
Asset Management Business of Financial Institutions*; Al Jazeera / Business Standard, Evergrande
wealth-management-product default coverage, 2021. · RBI, *Scale-Based Regulation of NBFCs* Master
Direction (22 Oct 2021) and Upper Layer NBFC list (2022). · RBI, Co-Lending Arrangements Directions,
2025 (effective 1 Jan 2026); RBI 2020 Co-Lending Model circular. · RBI press release, risk-weight
increase on unsecured consumer credit and bank-NBFC exposure (16 Nov 2023, effective 29 Feb 2024). ·
RBI, Digital Lending Guidelines (2 Sep 2022) and Guidelines on Default Loss Guarantee in Digital
Lending (8 Jun 2023). · CareEdge / MFIN, *Bharat Microfinance Report 2025*; Business Standard,
microfinance NPA and portfolio-at-risk data, FY25. · `research/CONTRACT.md`; `docs/CYCLE_ATLAS.md`
row 2.2; `config/ladder.yaml` (`L2_fast_stress`, `L10_credit_block` entries);
`research/cycles/shadow-deep/shadow-RESULTS.md` (SC1 pre-registered trial, cited directly
throughout, never recomputed); `research/cycles/shadow-deep/partC-data.md` (funding-freeze data
engineering, cross-referenced throughout); `research/cycles/capex-deep/partB-cases.md` (case 3,
IL&FS's real-side/capex transmission, cross-referenced not duplicated); `research/cycles/
credit-deep/partB-cross-country.md` (IL&FS as the R7 composition-signal validation target,
cross-referenced not duplicated); `research/cycles/fincycle-deep/partB-cases.md` (§B3, NBFC
real-estate exposure figures and house style for this series); `research/dossiers/
03-credit-financial-cycle.md` (bank+NBFC aggregation rule, I11, and the Nov-2023 tightening as
institutional confirmation).
