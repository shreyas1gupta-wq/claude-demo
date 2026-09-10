# Valuation as Edge in India — Evidence, Distortions, and What to Build on the Incoming PIT Dataset

**Status: RESEARCH DOSSIER (2026-09-10), principal-directed.** Complies with `research/CONTRACT.md`
v0.1; assumes the moderate-book factor engine framing already recorded in
`research/dossiers/02-value-quality-lowvol.md` (dossier 02) and does not re-derive what that dossier
already verified — it is quoted, not repeated wholesale. Targets the schema in
`research/register/handoff-prompt-india-fundamentals.md` (P1-P6, frozen 2026-09-08) so every design
proposed below consumes fields that will actually arrive. Tags: **[BOOKED <id>]** = a print already in
`research/register/trial-ledger.md`; **[LIT]** = a published or practitioner claim, hedged, never
carrying invented precision; **[VERIFY]** = a claim this desk has not independently re-derived.

---

## 1. The India value evidence

**The base rate.** Agarwalla, Jacob & Varma's IIMA four-factor series — the standing India Fama-French
library, CMIE-Prowess-based, July-June aligned to dodge look-ahead — reports HML averaging **+15.3%/yr**
over Jan-1994 to Dec-2014, actually exceeding the market premium (+11.5%/yr) in raw terms over that
window [LIT, verified by dossier 02 §2 via title/journal search; raw, not risk- or cost-adjusted]. That
figure sits in real tension with this desk's own real-data mirror of the same India HML series: **V1**
prints full-sample **+8.6%/yr** but a Sharpe of only **0.09** once the (high) Indian risk-free rate is
netted [BOOKED V1]. The gap between AJV's published 15.3% and the desk's own 8.6% mirror is
**unreconciled** — flagged here exactly as M1 flagged an analogous WML discrepancy (21.9% published vs
13.4% mirrored) [BOOKED M1] — plausibly a sample-window or index-construction difference, not yet
run down. Treat any India value magnitude below as bounded by this uncertainty, not as a settled number.

**The eras, qualitatively.** The desk's own sub-period cut is the cleanest confirmation available of the
market lore: **2015-2019** — the "growth mania" / quality-compounder years (IT, FMCG, private-bank
narrative names bid to extreme multiples) — value returned **+0.8%/yr at Sharpe −0.39**, the India value
winter [BOOKED V1]. **Post-2020** value snapped back to **+18.8%/yr at Sharpe 0.82** [BOOKED V1] —
consistent with the widely observed 2021-2024 value/cyclical/PSU revival (bank re-rating, capex-cycle
names, PSU re-rating, commodity windfall years) [LIT-lore, hedge: this is market narrative, not a
peer-reviewed magnitude, and no desk print isolates PSU/cyclical contribution specifically]. Two
India-specific decay papers corroborate the shape without giving a re-derivable number: Harshita, Singh &
Yadav (2018) document the value premium's *character* shifting over the sample, and Sharma, Srikanth &
Suresha (2022) find industry-level attenuation [LIT, both verified by title/journal search in dossier
02 §2; `[VERIFY: exact decay magnitude in bps terms — not independently confirmed]`]. **V4** separately
counts **5 India value-drawdown episodes** exceeding 20% cumulative, including a ~50% peak-to-trough
episode spanning 2018-2022 [BOOKED V4] — that episode's tail overlaps almost exactly with the growth-mania
years V1 dates qualitatively, which is the strongest internal cross-check this desk has that the "winter"
is a real, dated regime and not an artifact of one construction.

**Diversification, not redundancy, with momentum.** Value and momentum are meaningfully anti-correlated
in India — **V2** prints **−0.37** [BOOKED V2], smaller in magnitude than the US's −0.41 but the same
sign, replicating Asness-Moskowitz-Pedersen's "Value and Momentum Everywhere" diversification claim
[LIT, dossier 02 §2, verified]. A 50/50 blend beats **both** single legs on this desk's own India mirror:
Sharpe **0.86** vs. 0.42 (value alone) / 0.55 (momentum alone) [BOOKED V3] — the single strongest
India-native number in this dossier, and the anchor for design #2 in §5.

**Interaction with the SIP/retail-flow era.** Two structural facts bear on how a value revival propagates
through India's current flow regime. First, India's smart-beta AUM has grown roughly **160×** since 2020
(~₹290cr → ~₹46,000cr), with **low-volatility products carrying the second-largest segment** (~₹7,400cr
as of Aug-2024) [LIT, industry AUM reporting, dossier 02 §2] — flows chase quality/low-vol more visibly
than they chase raw value, which is one candidate explanation for why the growth-mania years (2015-19)
were also the years low-vol and quality-branded products gathered the most assets. Second, the desk's
own regime-dated India smallcap map — built independently on the IIMA SMB series — places the "froth"
peak at **2024-12** and an earlier "categorization-reform unwind" peak at **2018-07** [BOOKED SC-D3 i4],
which brackets the value winter almost exactly: retail/SIP-driven broadening into mid/smallcap accelerated
into 2024 alongside, not instead of, the value/PSU revival. The read this desk can defend: the 2021-2024
value comeback and the SIP-era retail broadening are **contemporaneous, not obviously causal** — no design
in the register isolates a flow→value-return channel, and none should be assumed without a registered
test.

---

## 2. India-specific measurement distortions

Five distortions must be designed around before any India valuation composite is trusted, in
roughly the order they will bite a naive P1-based construction:

**(a) Consolidated vs. standalone — the NSE 2021 splice.** NSE switched its published index P/E
calculation from standalone to consolidated earnings in **2021-03** [RUNSHEET row, `ingest/vault/index_valuation/`,
added 2026-09-10] — a genuine level break in any raw NIFTY index-level earnings-yield series that must
be **authenticated as two regimes, never smoothed across**, per the vault's two-pass AUTHENTICATION
discipline (CONTRACT §2). The same ambiguity recurs at the firm level: P1's `statement_basis` field
records standalone/consolidated per row and states a preference for consolidated "where filed" — so a
single company's time series can itself switch basis mid-panel. Any B/P, E/P or EV/EBIT built off P1
must either restrict comparisons to a constant `statement_basis` within a firm's own history or treat a
basis-switch as a structural break like the index-level 2021 splice, never as noise to average through.

**(b) The Ind-AS transition (FY2016-17).** Mandatory for large listed companies from FY2016-17, phased by
size, with full comparative restatement required in the transition-year filing [LIT, dossier 02 §2,
verified qualitatively — the exact restatement magnitude is `[VERIFY]`]. This directly distorts book
value and fair-value marks (financial-instrument remeasurement, provisions, lease-adjacent items) exactly
at the point P1's `total_equity` and `total_assets` change accounting regime, independent of anything
economically real happening to the firm. A related, later seam sits with **Ind-AS 116** (~2019 lease
capitalization), which breaks EBIT/asset-turnover comparability across the same era [LIT, `docs/fundamentals/02-growth-roic-quality.md`
§A.6]. Practical consequence for design: any within-firm time-series use of B/P, EV/EBIT, or asset
turnover must either exclude the FY2016-17 (and ~FY2019) transition quarters from before/after
comparisons or treat them as a hard regime break, the same discipline as (a).

**(c) Promoter cross-holdings and group-company loops.** India's business-group ownership structure means
a listed group entity's `total_equity` (P1, consolidated) can embed stakes in *other* listed group
entities carried at book or historical cost rather than a look-through market value — the same underlying
economic assets can appear, at some valuation, inside more than one group company's book value.
A naive P/B computed off P1 for a group-affiliated firm therefore risks reading as "cheap" precisely
because of this double-counted or stale-valued cross-holding, not because the firm's own operating
business is cheap. Related-party-transaction disclosure requirements (Companies Act 2013 / SEBI LODR)
exist because this channel is a documented vehicle for value extraction and earnings management in
India's group structures [LIT, dossier 02 §2, verified qualitatively]. Neither P1 nor P2-P6 carries a
cross-holding schedule or a business-group affiliation flag — this is a genuine gap, named again in §6.

**(d) Banks and financials need P/B-adjusted-for-asset-quality, not raw P/B.** A "cheap" bank P/B can
simply mean unrecognized or under-provisioned credit losses rather than mispricing — standard
corporate-finance practice treats financial-sector book value as unreliable without an NPA/provisioning
overlay [LIT, generic practitioner treatment, no specific magnitude claimed]. P1 delivers
`total_equity`/`total_assets`/`net_income` for banks exactly as filed but **carries no gross-NPA, net-NPA,
or provision-coverage field** — so a genuine NPA-adjusted P/B is not constructible from the handoff as
specified (see design #5, §5, and the gap list in §6).

**(e) PSU discount persistence.** State-owned enterprises trade structurally cheap for reasons unrelated
to temporary mispricing — promoter (government) overhang, dividend/capex policy dictated outside
shareholder interest, disinvestment-timing uncertainty, and index-fund/ESG-style institutional avoidance.
This is the India-specific instance of Piotroski's "cheap for a reason" trap that the F-score was built to
screen out [LIT, verified, dossier 02 §1]. A value composite that does not distinguish "cheap because of
a structural, priced-in PSU discount" from "cheap because of a temporary dislocation" will systematically
overweight the PSU bucket — and the 2021-2024 value revival's PSU-heavy character (§1, §4) makes this a
live, not merely historical, concern.

---

## 3. India-specific trap markers, ranked by point-in-time measurability

Ranked by what the handoff schema (P1-P6) actually lets the desk compute at the correct historical date,
not by evidentiary strength alone (evidentiary notes follow each):

1. **Promoter share pledging — the priority marker, directly measurable.** P5
   (`shareholding_pledge.csv`: `promoter_pct`, `promoter_pledged_pct_of_promoter_holding`, quarterly,
   filing-dated) is sourced from SEBI/exchange shareholding-pattern filings that are point-in-time **by
   regulatory construction** — no lag-estimation or proxy needed, the cleanest field in the entire
   handoff. The evidence: pledging is positively associated with future stock-price crash risk and
   negatively with subsequent financial performance; pledging firms show worse CVaR/VaR and deeper
   drawdowns [LIT, multiple 2023-2025 India papers, dossier 02 §2, verified directionally;
   `[VERIFY: magnitude not independently re-derived]`]. This is a genuinely India-specific junk-definition
   input with no US analogue at this scale — US firms rarely pledge control-block shares against personal
   margin loans the way Indian promoters do [LIT, dossier 02 §2]. A composite **promoter-distress score**
   — pledge intensity levels *and* its quarter-over-quarter change, plus separately the sign of
   `promoter_pct`'s own change (stake reduction outside a pledge event is its own red flag) — is buildable
   from P5 alone at quarterly frequency.
2. **Working-capital divergence from revenue, proxied by the Sloan accrual construction.** P1 does not
   carry receivables, inventory or payables line items, so a literal working-capital/revenue divergence
   cannot be computed. What P1 *does* carry — `net_income` and `cfo` — reconstructs the broader and
   better-evidenced Sloan (1996) accrual signal directly: `(net_income − cfo)/total_assets` [LIT, verified,
   dossier 02 §1]. This is a superset of the working-capital concern (working-capital build is one of
   several accrual sources) and is the second-most-measurable trap marker in the schema — no additional
   field is needed beyond what P1 already delivers.
3. **Related-party transactions — not directly measurable from the handoff.** RPTs are a documented India
   earnings-management and value-extraction channel [LIT, IIMA RPT working paper, dossier 02 §2, verified
   qualitatively] but P1-P6 carries no RPT-disclosure file, and P1's single `statement_basis` field per row
   (not both standalone and consolidated side-by-side) rules out even a crude standalone-vs-consolidated
   divergence proxy. This marker is a genuine data gap (§6), not a design deferred by choice.
4. **Auditor resignations — outside the schema entirely.** Sudden, unexplained mid-year auditor
   resignation is well-known market lore as a distress signal in India [LIT-lore, hedge: no base rate or
   magnitude claimed, illustrative examples exist but are not independently verified here], but nothing in
   P1-P6 carries exchange auditor-resignation disclosures (SEBI LODR Reg. 30). Lowest-ranked because it
   requires an entirely separate filings feed the handoff does not plan to deliver.

---

## 4. Sector composition and why raw index valuation moves are partly a mix-shift artifact

India's headline index P/E and P/B series conflate two different things: genuine market-wide re-rating,
and mechanical changes in **which sectors the index is made of**. Financials (banks + NBFCs) have carried
one of the largest single-sector weights in the NIFTY 50/500 for most of the post-2000 period, but that
weight itself has drifted materially across cycles — a fact this dossier states only directionally,
since no desk print quantifies the exact India sector-weight history and no precise figure should be
invented here. The clearest illustration is temporal: **2007-08's NIFTY** carried a heavy
infrastructure/capex/metals/real-estate tilt trading at very rich multiples ahead of the GFC, while
**today's index (2024-26)** is financials- and IT/consumer-weighted with a re-emerging capex/PSU
allocation since 2021 [LIT-lore, hedge: directionally well known, not independently re-derived by this
desk with a sector-weight time series]. A raw trailing index P/E spanning both eras is contaminated by
this mix shift on top of the 2021 standalone-to-consolidated splice (§2a) — two independent, unrelated
sources of index-level valuation non-comparability stacked on the same series.

**The design consequence.** Building the moderate book's valuation *state* variable (in the sense of
CONTRACT §5's "assume decay" discipline and the ER arc's dp-as-state framing — the desk's own honest
grid there finds a cheap+low-inflation corner earning **+14.2%/yr** vs. an expensive+high-inflation corner
at **+2.3%/yr** on JST developed-market data, a **~12pp** spread [BOOKED ER-D6], though that grid is
US/global and still IN-SAMPLE per the audit addendum — flagged, not carried to India as a magnitude) on
sector-mix-contaminated raw aggregates would silently reprice sector allocation as "cheapness." The fix
is to compute the valuation composite (design #1, §5) as **within-industry ranks** — a NIFTY-wide
percentile is not sector-neutral by construction, but a within-sector percentile is. This is a
**measurement** choice for the signal, not a portfolio constraint: CONTRACT §3 explicitly keeps sector
exposure fully active with no sector-neutrality requirement, so a sector-neutral valuation *state* and a
sector-active *book* are entirely compatible — the book is free to overweight cheap sectors outright; the
signal construction just should not confuse "the market got cheaper" with "the index rotated toward
cheaper sectors."

---

## 5. What to build on the handoff — top 5 designs ranked by evidence-strength × feasibility

| Rank | Design | P1-P6 fields consumed | Confound it must dodge | Expected magnitude [LIT+hedge] |
|---|---|---|---|---|
| 1 | **Within-industry value composite** (B/P, E/P, EV/EBIT-proxy) | P1: `total_equity`, `net_income`, `ebit`, `total_debt`, `cash_and_equivalents`, `shares_outstanding`, `statement_basis`; P4: `close_adjusted` for market cap; P2: PIT membership; P3: delisted registry (VW/no-survivorship construction) | The QG-D2 EW-survivor "junk wins" artifact — booked as doctrine on the US firm panel: the naive ROE ladder inverted (D1 +29.7%/yr vs D10 +11.9%) purely from EW + smallest-cap + no-delisting construction, collapsing to −1.3pp once size-controlled and VW [BOOKED QG-D2] — this design must be VW (or size-bucketed) and must use P3's delisted names from day one, never repeat the mirror's EW-only shortcut. Also: Ind-AS/basis breaks (§2a-b) and the missing sector-classification field (a genuine gap — see §6) | SC-D4's own US large-cap value spread survives *every construction thrown at it* — +9.95%/yr at 1m, +8.80%/yr at 12m in the largest size quintile, monotone across the value ladder [BOOKED SC-D4/SC-D5]; AJV's raw India HML is +15.3%/yr [LIT, `[VERIFY]` vs the desk's own 8.6% mirror, V1]. Dossier 02's own recommended 30-40% haircut on any in-sample India value magnitude applies here without modification [dossier 02 §3] |
| 2 | **Value + momentum double sort on PIT membership** | Design #1's value composite × P4 price momentum (11-12m return, `close_adjusted`); P2 for point-in-time universe; P3 to avoid survivorship on the momentum leg too | Israel-Moskowitz's ~5× turnover gap between momentum and value [LIT, verified, dossier 02 §2] means a joint rebalance clock risks forcing value into momentum's turnover budget — the design must fix which clock governs and log the incremental turnover against the moderate book's 200% one-way cap (CONTRACT §3). Must also avoid SC-D4/SC-D5's own EW-survivor limitation on the momentum leg | The desk's own real India mirror is the strongest anchor here: value-momentum correlation **−0.37** [BOOKED V2] and a 50/50 blend Sharpe **0.86** vs. 0.42/0.55 single legs [BOOKED V3] — directionally supportive, but that mirror is a factor-series-level construction, not this stock-level PIT double sort, so the magnitude is carried as a direction, not a number, into the new design |
| 3 | **Value + pledge trap filter** | Design #1's value composite × P5 (`promoter_pledged_pct_of_promoter_holding`, level and QoQ change; `promoter_pct` QoQ change) | Reverse causality / lag direction: pledging can rise *after* a price fall (promoters posting more collateral as loan-to-value deteriorates) rather than predicting one — the design must test lead-lag explicitly before treating pledge as a leading indicator, not assume it. Also P5's quarterly frequency will miss intra-quarter pledge-acceleration events that SAST threshold-crossing disclosures could in principle catch sooner | Directional only: pledging is associated with worse forward performance and crash risk [LIT, dossier 02 §2, `[VERIFY]` on magnitude]. No effect size should be assumed until this design's own registered test prints — CONTRACT's Tier-C reduce-only treatment (§4) is the right default until then: the filter should *cut* exposure to pledged-cheap names, never *add* exposure on an unpledged-cheap signal alone |
| 4 | **Tobin's q / expected-growth replication (QG-D6 — situate, do not respec)** | Already frozen: `mcap + total_debt − cash_and_equivalents` over `total_assets` (P1 + P4), `cfo/total_assets`, ΔROE — all constructible from P1 fields already in this handoff [BOOKED QG-D6 registration] | Quoted verbatim from the registration, not restated here: "the EG signal CANNOT be built from the price-only survivor panel, and a price-proxy substitute is explicitly FORBIDDEN" [BOOKED QG-D6] — this design's entire point is that it is un-runnable on anything but exactly this handoff | The registration's own two-sided prior: n8 (does the signal forecast investment growth in India at all) likely passes; n1 VW top-vs-bottom decile likely **+2 to +6%/yr**, well below the US +10% [LIT `[VERIFY]` per the registration], haircut for specification-search inflation and India costs; a Sharpe > 1 print would itself be suspicious (ER-D4b-grade), not celebrated [BOOKED QG-D6] |
| 5 | **Banks-adjusted P/B** | P1: `total_equity`, `total_assets`, `net_income` for financial-sector rows only; no NPA/provisioning field exists in P1-P6 | The absence of gross-NPA/net-NPA/provision-coverage fields (§2d) means a genuine asset-quality-adjusted P/B is not constructible from the handoff as specified. The feasible fallback is a crude two-factor P/B×ROE rank for financials, run *separately* from the common cross-sectional ladder, or simply excluding financials from design #1 entirely (the more defensible default until the missing fields land) | No magnitude claimed — this design's honest status today is "cannot be properly built," not "expected to be small." Ranked last on feasibility, not on evidentiary interest |

---

## 6. Data requirements beyond the handoff

Even with P1-P6 fully landed, five items remain missing that this dossier's designs need or would
materially improve with:

1. **A sector/industry classification per company.** Neither P1 nor P2 carries a GICS-like or NSE sector
   tag — design #1's within-industry construction (and §4's composition-neutral state) cannot be built
   without one. The already-registered RUNSHEET row for NSE sectoral TR indices
   (`ingest/vault/index_sector/`, principal-machine) can double as a sector-membership taxonomy if its
   constituent lists are captured alongside the return series — worth an explicit ask appended to that
   pull rather than a new one.
2. **NPA/asset-quality fields for banks and NBFCs** (gross NPA, net NPA, provision coverage ratio) —
   needed for design #5 to be a genuine banks-adjusted P/B rather than a fallback exclusion rule.
3. **RPT-disclosure and auditor-resignation feeds** — both trap markers named in §3 are currently
   unmeasurable from any planned pull; a future ask, not urgent relative to P1-P5's core designs.
4. **NSE index-level P/E, P/B and dividend-yield history** (already a RUNSHEET row,
   `ingest/vault/index_valuation/`, principal-machine, blocked at this proxy) — needed for the
   composition-corrected raw valuation state (§4) and for the already-registered India small-vs-large
   valuation-spread timing design that SC-D1's US first gate passed and is waiting on exactly this pull
   [BOOKED SC-D1 RESULT, RUNSHEET row].
5. **Two named live India factor indices missing from P6 as specified.** P6 lists NIFTY200/100 Quality
   30, NIFTY Midcap150 Quality 50, and NIFTY 500/200 TR — it omits **NIFTY500 Value 50** (launched
   2018-10-24) and **NIFTY Alpha Low-Volatility 30** (launched 2017-07-10), which dossier 02 already
   identified as the two most directly relevant live, walk-forward India benchmarks for this exact
   topic (~8-9 years live, Tier B by the CONTRACT's own observation-count rule) [dossier 02 §2]. Worth
   appending to the P6 ask.

**One-line kill condition per design:**
1. Value composite — killed if the VW, delisted-inclusive decile spread is not monotone and is
   materially smaller than SC-D4's large-cap benchmark at the first read.
2. Value+momentum double sort — killed (reduces to standalone value) if the joint spread does not beat
   the better single-leg Sharpe, echoing V3's own bar.
3. Value+pledge filter — killed as an alpha input (retained only as Tier-C reduce-only) if lead-lag
   testing shows pledge lags price rather than leading it.
4. Tobin's q / QG-D6 — killed at its own registered gate: if n8 shows the inputs do not forecast
   investment growth in India, the factor premise dies before the return question is asked [BOOKED
   QG-D6, quoted verbatim].
5. Banks-adjusted P/B — killed (financials simply excluded from the common ladder) if the crude
   P/B×ROE proxy fails an in-sample sanity check against known past bank-stress episodes.
