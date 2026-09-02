# FII/FPI Positioning Deep Dive — Part A & Part G

Part A: Theory — an exclusion first, and what survives it · Part G: Operator psychology · v1.0 ·
2026-09-02 · Atlas entry 2.13 (`docs/CYCLE_ATLAS.md` row 89, Band 2 — the business-credit band);
ladder seat `L14_fii_positioning` (`config/ladder.yaml`), Tier **C**, `reduce_only: true`, block
`tierC_overlay`, τ½ **12–36 months** — a positioning half-life, not a flow one. Complements, never
duplicates: `research/cycles/globalcycle-deep/partA-theory-psychology.md` §A.3(i), which states the
flows-follow-returns finding as a cross-reference for L9's own confirm-layer design and explicitly
routes its own derivation here ("this chapter does not re-derive the finding... cross-referenced,
never re-derived here"); this chapter is that derivation, in full, plus the positioning-extremes
mechanism L9 does not own. `research/cycles/fpi-deep/partCDEFH.md` (data engineering, the algorithm,
the harvest map, the knowledge ledger) supplies the machinery this file's mechanism compresses into —
the float-scaled expanding percentile, the `extreme_t = 1[pct_t ≥ 0.9]` flag, the structural
API-level exclusion of flow momentum, the FL1/FL2/FL-D3 design items — and is assumed, not re-derived,
throughout. The cases chapter (this program's sibling, forthcoming) owns the episode chronology —
partCDEFH's own Part H already names "five positioning eras" and the FY22 exodus absorbed by DIIs as
its structural-change exhibit; this file cites that framing where relevant and re-builds none of it.
Evidence base: `research/dossiers/08-india-mid-cycles.md` (D08, §1 F8, §2 I6–I7, §3 Edge C, §4 table).
Style and depth calibrated to `research/cycles/fincycle-deep/partA-theory-psychology.md`.

This file assumes the ladder's frozen construct as given: L14 reads NSDL aggregates and SEBI-LODR
quarterly shareholding patterns, float-scaled, against a **0% positive-tilt budget** — Tier C per
`CONTRACT §4` may only reduce risk, never add it — drawing from the capped `tierC_overlay` (10% of
regime score, negative-shift only, shared with L1/L13/L15/L16). Part A supplies the reason the seat
is built this way: one dataset, two candidate signals, and a decay argument sharp enough that the
Contract's own §5 test ("why does this survive being known?") answers oppositely for each. Part G
turns to the desk operating a seat whose entire design is an exclusion held under daily pressure to
reverse it.

---

## PART A — Theory: an exclusion first, and what survives it

### A.1 The object, and the exclusion that defines it

**(i) One dataset, two transformations.** Foreign participation in Indian equities generates a
single underlying data-generating process — foreign capital entering and leaving NSE/BSE-listed
names — but that process can be read as two structurally different objects. **Flow momentum**:
the first difference, read at daily-to-monthly frequency from NSDL's own published net-FPI-flow
series (`fpi.nsdl.co.in`), the number every business-news broadcast repeats every evening — "FIIs
sold ₹X crore today." **Positioning extremes**: the level, read at quarterly frequency from SEBI
LODR shareholding-pattern filings, float-scaled — how much of a given stock's tradable float
foreigners already own, ranked against its own trailing history. These are not two independent
signals competing for a budget on equal footing; they are two lenses on one phenomenon, and the
atlas's own routing (row 89: "flow momentum → §7 REJECT"; "REGIME (reduce-only) → L14") reflects a
prior finding, not a coin flip — the finding A.2 derives in full is that the flow lens is decayed
and the level lens is not, for reasons that trace to genuinely different economic mechanisms
underneath each transformation of the same raw data.

**(ii) Why the desk leads with an exclusion.** Every other seat on this ladder opens with what it
harvests; this one opens with what it refuses, and that ordering is deliberate rather than
stylistic. FII flow momentum is, by a wide margin, **the most-marketed FPI signal in the Indian
market** — more repeated, more intuitive, and more commercially convenient to produce than any
positioning or ownership-level construct, because it needs no scaling, no float adjustment, no
quarterly lag: NSDL publishes a signed rupee number every evening, and "FIIs are buying" or "FIIs
are selling" requires no further analysis to become a headline. A research program that built its
FPI seat by starting from "what can we harvest" and arrived at flow momentum by default would be
building exactly the crowded, decayed, well-published pattern the Contract's own §5 exists to
guard against. Leading with the exclusion — stating plainly that the single most popular FPI
narrative in Indian markets is excluded by design, and arguing why, before describing what
survives — is the honest order of operations for a signal whose popular version and whose
surviving version point in opposite directions on the tier ladder.

**(iii) The claim, stated precisely.** The evidence A.2 assembles supports one clean sentence:
**flows follow returns, not the reverse** — foreign portfolio flows into and out of Indian (and
comparable emerging-market) equities respond to past returns more than they predict future ones,
a "pulled" rather than "pushing" pattern in the Griffin-Nardari-Stulz vocabulary A.2 unpacks in
full. This is not a claim that foreign flows are uninformative or irrational — A.2(iv)'s own
theoretical layer (DeLong-Shleifer-Summers-Waldmann) shows return-chasing can be a fully rational
equilibrium strategy for informationally disadvantaged foreign investors — it is a claim about
**causal ordering and tradability**: a signal built by watching flows to predict tomorrow's return
is, mechanically, a noisy, lagged proxy for yesterday's return, and trading it adds cost and lag to
information the return series itself already contains more cleanly. What survives this finding,
rather than being felled by it, is a different economic object entirely: **positioning extremes**
— not "is money coming in or out," but "how much of this float does foreign capital already hold,
relative to its own history" — a level whose tradability rests on a capacity mechanism (A.3) that
has nothing to do with whether flows predict returns.

### A.2 Flows follow returns — the evidence at depth

**(i) The empirical question, stated precisely.** Does a positive foreign flow into a market predict
that market's subsequent return (a **pushed**, information-driven or price-pressure story), does a
positive return predict subsequent foreign inflow (a **pulled**, return-chasing or positive-feedback
story), or both — and at what frequency does each show up? This is not a rhetorical question with
an obvious answer; the honest literature contains genuine tension across studies at different
frequencies and samples, which A.2(vi)–(vii) below take seriously rather than smoothing into one
tidy sentence.

**(ii) The central international finding — Griffin, Nardari & Stulz (2004).** **Griffin, John M.;
Nardari, Federico & Stulz, René M. (2004), "Are Daily Cross-Border Equity Flows Pushed or
Pulled?,"** *Review of Economics and Statistics* 86(3): 641–657 (August 2004) **[Verified — MIT
Press/REStat 86(3):641-657]** builds an intertemporal equilibrium model in which foreign investors,
facing barriers to information about a local market that domestic investors do not face, form more
**extrapolative** expectations than domestic investors — a structural information asymmetry, not a
claim of foreign irrationality — and tests the model's implication on **daily net equity flow data
for nine emerging markets**. Their finding, stated in the paper's own terms: flows are positively
related to **both host-country and foreign (world) stock returns** at the daily frequency; this
return-to-flow relationship is **remarkably robust**, but its effects **dissipate quickly** — i.e.,
flows respond to recent returns far more reliably, and far more immediately, than they forecast
returns going forward. This is the paper the atlas's own row 89 leans on for the headline sentence
("flows FOLLOW returns"), and it is worth stating exactly what kind of evidence it is: a **daily-
frequency, model-plus-multi-country-panel** result, which A.2(vii) returns to because the frequency
matters for what the finding does and does not license.

**(iii) The India-specific finding — Chakrabarti (2001).** **Chakrabarti, Rajesh (2001), "FII Flows
to India: Nature and Causes,"** *Money & Finance* (ICRA Bulletin) **[Verified via SSRN abstract
no. 649852 and secondary academic citation; exact page range not independently confirmed this
session — D08 itself flags the identical venue caveat]** uses **monthly data from May 1993 to
December 1999** — the earliest available window of India's FII-era history, beginning barely a year after
FIIs were first permitted into Indian equities (September 1992) — and finds, in the paper's own
framing: FII flows are **highly correlated with contemporaneous equity returns**, but the flows are
**more an effect than a cause** of those returns; FIIs do **not** appear to be at an informational
disadvantage relative to local investors on India's own data (a genuine nuance against a pure
"foreigners are simply less informed" reading); and — the finding this chapter treats as the single
most important nuance Chakrabarti's own paper offers beyond "flows follow returns" — the **1997–98
Asian financial crisis marked a regime shift** in what drives FII flows into India, after which
**domestic equity returns became the sole (or dominant) driver** of subsequent flows. This last
point matters for how the finding should be read going forward: it is not that "flows follow
returns" was always and everywhere true in identical strength across India's FII-era history; it is
that a **specific historical shock reset the relationship**, and the post-crisis regime — return-
chasing dominant, other drivers secondary — is the one that has persisted (on the evidence recalled
here) through the sample this paper covers. India's own founding finding on this question is
therefore not merely "consistent with" Griffin-Nardari-Stulz; it independently established the same
causal direction on domestic data, at an earlier date (2001 vs. 2004), on a market not covered by
the international paper's own nine-country panel **[VERIFY: whether India appears in Griffin-
Nardari-Stulz's own nine-market sample — this session's search access could not confirm the exact
country list; treat Chakrabarti as the independent India-specific confirmation regardless]**.

**(iv) The wider mechanism literature.** Three further papers, read together, supply the theoretical
scaffolding underneath (ii)–(iii) rather than merely repeating the same empirical finding. **Brennan,
Michael J. & Cao, H. Henry (1997), "International Portfolio Investment Flows,"** *Journal of
Finance* 52(5): 1851–1880 **[Verified]** models cross-border flows as a function of a **cumulative
information asymmetry**: when domestic investors hold a persistent informational edge over foreign
ones about their own market (the natural default assumption for any emerging market vis-à-vis
foreign capital), foreign investors' optimal strategy is to buy after the foreign asset's return has
been high and sell after it has been low — a rational, information-based **trend-following** pattern,
tested and confirmed on US investors' own foreign-equity flow data. The mechanism transfers directly
to the FII-in-India case with the labels reversed (India is Brennan-Cao's "foreign" market, Indian
domestic investors hold the informational edge), and it supplies the **why**, not merely the *that*,
behind Griffin-Nardari-Stulz's daily result: extrapolative flow behavior is not foreign investors
behaving foolishly, it is close to the rational response to a genuine, structural information
disadvantage. **Froot, Kenneth A.; O'Connell, Paul G. J. & Seasholes, Mark S. (2001), "The Portfolio
Flows of International Investors,"** *Journal of Financial Economics* 59(2): 151–193 **[Verified]**
— **44 countries, daily data, 1994–1998** — corroborates the positive-feedback finding directly
(flows are strongly influenced by past returns) and adds the honest complication A.2(vii) returns to:
in the **same** sample, inflows also carried **positive forecasting power for future equity returns,
particularly in emerging markets**, and the sensitivity of local prices to foreign inflows was
**"positive and large."** **DeLong, J. Bradford; Shleifer, Andrei; Summers, Lawrence H. & Waldmann,
Robert J. (1990), "Positive Feedback Investment Strategies and Destabilizing Rational Speculation,"**
*Journal of Finance* 45(2): 379–395 **[Verified]** is the theoretical closing piece: rational
speculators, anticipating that some class of investors trades on positive feedback (buy after price
rises, sell after price falls), can **rationally amplify** that feedback by front-running it — a
result that both explains why return-chasing flows are a stable, recurring equilibrium phenomenon
rather than a fluke that should have been arbitraged away decades ago, and why the pattern is
nonetheless **not** the same thing as an exploitable, decay-immune signal for a desk sitting on the
other side of it (A.2(vi) explains why).

**(v) India's later literature — genuinely mixed, honestly stated.** D08's own §2 (I6) already flags
the difficulty this chapter inherits rather than resolves: subsequent India-specific Granger-
causality-style studies through the 2000s and 2010s exist in some volume, but this session's search
access surfaces a **genuinely mixed** picture rather than a clean confirmation of Chakrabarti's own
finding extended forward — some studies report unidirectional flow-to-return causality, others
bidirectional causality, others sector-dependent results with no significant FII effect in some
sectors **[VERIFY: specific author/year/venue triples for this later literature — the search results
this session surfaced were consistent in describing mixed findings but did not resolve to
citable, individually-confirmed papers with the same confidence as (ii)–(iv) above; treat the
existence of a mixed later literature as the honest finding, not any single study's precise
result]**. The honest reading, consistent with — not contrary to — the decay-and-absorption
argument (vi) below: Chakrabarti's own returns-lead-flows finding is best-established for the
**founding early-FII-era sample** (1993–1999) and the Asian-crisis-era regime shift specifically;
results become progressively less uniform as the sample window extends through the 2000s and the
DII counterweight (A.4) grows large enough to complicate a simple two-variable causality test, which
is exactly the kind of structural change a stable, one-directional relationship should NOT survive
mechanically unchanged for three decades.

**(vi) The decay story, and why this is the alpha-decay assumption's cleanest institutional case.**
CONTRACT §5 asks, for every signal, "why does this survive being known?" — and FII flow momentum
fails that test more completely, and more legibly, than almost any other candidate this ladder has
examined. Three independent reasons compound rather than merely coexist. **First**, the finding is
old and thoroughly published: Griffin-Nardari-Stulz is a 2004 paper (now over two decades old),
Chakrabarti's India-specific finding is 2001 (nearly a quarter-century old), and both sit inside a
still-larger literature (Brennan-Cao 1997, Froot-O'Connell-Seasholes 2001) that has been public,
peer-reviewed, and repeatedly cited for the entire span McLean & Pontiff's own post-publication decay
figure (CONTRACT §5: ~58%) is calibrated against. **Second**, and more distinctive than any factor
McLean-Pontiff studied: the underlying **daily NSDL flow print is not merely published in an academic
journal somewhere — it is broadcast as a headline number on every major financial news outlet and
brokerage portal in India, every single trading day, for more than three decades.** A crowded factor
typically decays because sophisticated capital reads the academic literature; FII flow momentum
decays because **every retail investor with a smartphone reads the evening business news**. If
academic publication alone drives a ~26–58% haircut, daily headline republication to the entire
retail and institutional base simultaneously should be expected to decay a directional flow-momentum
signal considerably faster and more completely than the generic McLean-Pontiff band implies for a
typical academic-only anomaly. **Third**, D08's own I7(a) supplies an independent, structural
(not merely crowding-based) decay channel layered on top of the first two: even the residual return-
chasing content flow momentum might still carry is being **mechanically absorbed** by a growing DII/
SIP counterweight (A.4) that did not exist at the scale it does today when Chakrabarti's own sample
was collected — meaning the *economic mechanism* the pattern relies on (thin domestic absorptive
capacity for FII flow shocks) has itself been shrinking for a decade, independent of any crowding
argument about traders reading the same papers. Three decay channels — academic-publication age,
literal daily headline broadcast, and a shrinking underlying economic mechanism — compounding on one
signal is the cleanest case this program has for the Contract's own decay assumption, and it is why
`ladder.yaml` excludes flow momentum **outright** (`excluded: fii_flow_momentum`) rather than merely
applying a haircut and retaining it at reduced size the way L3 momentum (haircut 25–35%, per
`ladder.yaml`) or L7 issuance-sentiment (haircut band 26–58%) are retained: a signal earns a stated
haircut when its decay is partial; it earns exclusion when, as here, three independent decay
arguments point the same direction and no counter-argument in (iv)–(v) restores a tradable residual.

**(vii) Honest counter-reads — frequency and the announcement window.** Two genuine complications
deserve to be stated rather than smoothed over, because the design would be less honest for omitting
them. **Frequency**: Griffin-Nardari-Stulz's own finding is explicitly a **daily**-frequency result
whose flow-to-return effects "dissipate quickly" — which leaves open, rather than settling, what a
lower-frequency (monthly, quarterly) construction of the same underlying data might show, since a
relationship that dissipates within days at daily frequency is not automatically the same object
measured monthly. This is precisely why L14's own construction (per `partCDEFH.md`) is built on
**quarterly shareholding-pattern levels**, not on any resampled daily-or-monthly NSDL flow series —
the frequency mismatch between "flows dissipate fast" (a daily-clock finding) and "positioning
builds and unwinds slowly" (A.3's own quarterly-to-multi-year clock) is not an oversight, it is the
reason two different objects, not one signal at two horizons, sit on this ladder. **The announcement-
window complication**: Froot-O'Connell-Seasholes's own finding (iv above) that inflows carried
**positive forecasting power for future returns, particularly in emerging markets**, in the *same*
44-country sample that also confirmed positive-feedback trading, is a genuine tension this chapter
does not paper over. The honest resolution is not to pretend this finding doesn't exist, but to
place it correctly: **(a)** it is drawn from a 1994–1998 sample now roughly three decades stale —
precisely the vintage McLean-Pontiff's post-publication decay figure targets hardest, and the
absorption argument (vi) above applies to it with equal force; **(b)** even taken at face value, it
describes a **short-window, price-pressure/information effect embedded in the daily flow print
itself** — a fundamentally different economic object from the **stock-level, quarterly, capacity-
driven positioning level** L14 actually seats. A genuine surviving fast-flow-forecasts-returns effect,
if one exists in current India data, would compete for a seat against L2 (fast stress) or L9's own
NSDL-flow confirm layer (τ½ 3–9 months) — it would not resurrect flow *momentum* as an independent,
directionally-traded L14 signal, because L14 was never built to capture that object in the first
place.

### A.3 What survives: positioning as capacity

**(i) The mechanism, precisely.** An extreme foreign-ownership position in a given stock is a
**crowded exit waiting to be forced open**, and the force that opens it is unrelated to whether flows
predict returns. **Coval, Joshua D. & Stafford, Erik (2007), "Asset Fire Sales (and Purchases) in
Equity Markets,"** *Journal of Financial Economics* 86(2): 479–512 **[Verified]** documents the
general mechanism on US mutual-fund transactions (1980–2004): funds facing large **outflows** are
forced to sell existing positions regardless of the fund manager's own view of value, creating
measurable **price pressure** concentrated in the securities held in common by the distressed funds
— a genuine, price-inelastic, forced-seller effect distinct from any information the sale might
convey. **Greenwood, Robin & Thesmar, David (2011), "Stock Price Fragility,"** *Journal of Financial
Economics* 102(3): 471–490 **[Verified]** formalizes the ownership-structure side of the same
mechanism: an asset is **fragile** — susceptible to large, non-fundamental price swings from shifts
in its owners' demand alone — when its ownership is **concentrated** among a set of holders who face
**correlated liquidity shocks** (the same redemption pressure, the same mandate change, the same
risk-off trigger hitting many holders simultaneously), and fragility is shown to be a statistically
and economically strong **predictor of future price volatility**, independent of the underlying
fundamentals. **Jotikasthira, Chotibhak; Lundblad, Christian & Ramadorai, Tarun (2012), "Asset Fire
Sales and Purchases and the International Transmission of Funding Shocks,"** *Journal of Finance*
67(6): 2015–2050 **[Verified]** closes the loop specifically for the FPI-in-EM case: investor flows
into and out of developed-market-domiciled funds force **mechanical, allocation-driven** changes in
those funds' emerging-market equity holdings, and these forced fire sales measurably move EM equity
**prices, correlations and betas** — the precise cross-border mechanism transmitting a foreign fund's
own redemption pressure into an Indian stock's price, entirely independent of that fund's view on the
Indian stock itself. Read together, these three papers supply exactly the survival argument CONTRACT
§5 calls **(ii) a capacity limit**: unwinding an extreme foreign-ownership position is not a
information-processing problem any amount of market efficiency shortens, it is a **capital-movement
problem** — someone has to actually sell a large, concentrated stake, at a size the local market's
own absorptive capacity may not clear quickly or cheaply, and that constraint exists regardless of
whether the position was built on good information, bad information, or pure momentum-chasing.

**(ii) Why the survival argument is orthogonal to the causality question A.2 just settled.** This is
the single most important structural point this chapter makes, and it is worth stating explicitly
rather than leaving implicit: A.3's capacity mechanism requires **no claim whatsoever** that foreign
ownership levels predict future returns. A.2 spent its full length establishing that flows do not
lead returns — but A.3's claim is not "extreme ownership predicts a price move," it is "extreme
ownership predicts how **costly and slow** a future unwind would be, if or when one is triggered by
anything (a global risk-off episode, a domestic regulatory shock, a fund's own redemption wave,
entirely independent of the stock's own merits)." A signal can be **completely silent on direction**
and still earn a seat on a risk-management ladder purely by conditioning **fragility** — which is
exactly why L14 sits inside `tierC_overlay`, reduce-only, rather than being asked to clear the same
bar a directional EDGE signal would need to clear. This is also why the exclusion in A.1–A.2 and the
survival in this section are not in tension: excluding flow momentum removes a decayed **return**
claim; admitting positioning extremes retains a **live capacity** claim built on entirely different
papers, entirely different economic content, and (per A.3(v) below) an argument that gets *stronger*,
not weaker, as more capital crowds into the same trade.

**(iii) Float-scaling as the correct denominator — the India-specific correction.** A raw "percent of
market cap held by FPIs" figure is systematically misleading in India because of the market's
unusually high **promoter concentration**: NSE-listed companies carry an average promoter holding of
roughly **50–51% by value** (Q2 FY26 figures put aggregate promoter ownership at ~50.1%, and roughly
**45% of NSE-listed companies carry promoter stakes above 60%** as of FY2025 disclosures)
**[Verified — Business Standard/Tickertape aggregation of NSE-listed promoter-holding data, 2024–26]**,
concentrated particularly in FMCG, auto and retail founder/family-controlled names. SEBI's own
minimum-public-shareholding norm requires only a **25% public float floor**, and research comparing
that regulatory floor to the market's own **actual tradable float** finds a real gap: average
**public float** across Indian listed companies runs close to **46%**, while average **free float**
— the narrower, genuinely tradable denominator that excludes locked-in, strategic and cross-holding
stakes even within the "public" category — runs closer to **38%** **[Verified — PrimeInvestor/
Business Standard research on the public-float-vs-free-float gap]**. The consequence for a
positioning signal is exactly D08's own I7(b): a given rupee of FPI buying, or a given percentage-
point of cumulative FPI ownership, moves a **much smaller effective float** in a promoter-heavy
Indian name than the identical flow would move in a dispersed-ownership developed market, so any
honest ownership-extreme construction must scale by **free float**, never by total market
capitalization — `partCDEFH.md`'s own "float rule" (promoter and locked shares excluded from the
denominator, pinned in the registry) is this exact correction, made operational.

**(iv) Why extremes are REGIME information, not alpha — the asymmetry that justifies reduce-only.**
The capacity mechanism (i)–(ii) above licenses a specific, **asymmetric** use, and the asymmetry is
worth deriving rather than merely asserting. A stock at a **top-percentile** foreign-ownership
extreme is a crowded theatre with a narrow exit — Coval-Stafford's and Jotikasthira-Lundblad-
Ramadorai's own mechanism says a shock, whenever one arrives, forces a slow, price-inelastic
unwind through that exit, which is a genuine reason to hold **less** of that name (or the book's
concentration in it) than the mechanical signal alone would suggest, entirely without needing to
believe anything about where the stock's price is headed absent a shock. A stock at a **bottom-
percentile** foreign-ownership extreme, by contrast, is **not** symmetrically informative about
forward return in the way a naive "contrarian, buy what's under-owned" read would want it to be —
and treating it as such would silently **reimport the exact excluded pattern** A.1–A.2 spent this
chapter ruling out. Low FPI ownership in a given name is, mechanically, substantially a *record of
that name's own trailing price history* (a stock that hasn't rallied hasn't attracted the return-
chasing flow A.2 documents, so of course its ownership percentile stays low) — using "low ownership"
as a buy trigger is functionally indistinguishable from betting that a stock's *absence* of past
FII buying predicts a *future* rally, which is the identical reversed-causality claim flow momentum
makes, merely relabeled from a flow to a level. **This is precisely why `ladder.yaml` gives L14
`reduce_only: true`** rather than L9's own `reduce_only: false` (which can both add and subtract
regime score, per `globalcycle-deep partA` A.2viii): the seat needs **no claim about the sign or
predictability of future returns at all**, only a claim about unwind fragility at the extreme that
actually carries it — a pure risk-scaling construct, immune to the causality question A.2 already
settled in the opposite direction.

**(v) τ½ 12–36 months — the capacity argument IS the persistence argument.** `ladder.yaml`'s own
prior for L14 (`tau_half_months: [12, 36]`) is not an arbitrary placeholder; it is the direct
consequence of what kind of object a positioning extreme is. A flow print can reverse within days —
which is exactly why it decays as a signal (A.2vi) — but a **stock** of cumulative ownership can only
move by the **integral** of flows over time, and three structural facts keep that integral slow.
**First**, the disclosure cadence itself is quarterly by regulation (SEBI LODR, 21 days post-quarter-
end, per D08 I7(b)) — the underlying series *cannot* update faster than once a quarter regardless of
how fast the true economic position is actually changing intra-quarter. **Second**, the underlying
economic process — a large asset manager methodically reducing a concentrated position without
moving the price too far against itself — is a genuine execution-constrained process (the same
price-impact logic Coval-Stafford's own fire-sale mechanism formalizes), typically playing out over
weeks to months of careful, VWAP-style unwinding rather than a single print. **Third**, an ownership
percentile can also resolve **without any FPI selling at all** — through free-float growth (fresh
issuance, promoter dilution, an IPO-linked index inclusion diluting the existing base) — a slower,
structural channel with its own multi-quarter clock. Put together, a positioning extreme, once
established, takes on the order of **one to three years** to fully resolve one way or the other —
meaningfully slower than L2's fast-stress clock (weeks) and even L9's own global-cycle episode clock
(3–9 months, per `globalcycle-deep partA` A.4) — precisely because positioning is a **stock**, and a
stock's clock is set by how fast its underlying flow can plausibly integrate, not by how fast a
headline print can move.

### A.4 The India machinery

**(i) NSDL, the 2014 regime change, and the equity/debt split.** NSDL's own FPI Monitor
(`fpi.nsdl.co.in`) publishes both a **daily provisional** net-flow print and a **monthly settled**
series, each split by **equity and debt** (with a smaller hybrid/VRR sleeve), free — the seat's flow-
side input for the confirming layer L9 already consumes (`globalcycle-deep partA` A.3i), and the raw
series `partCDEFH.md`'s own Part C flags for a mandatory breaks-registry entry rather than a silent
splice: **the SEBI (Foreign Portfolio Investors) Regulations, 2014**, notified **7 January 2014** and
in force from **1 June 2014**, merged the three pre-existing foreign-investor classes — Foreign
Institutional Investors (FIIs), their sub-accounts, and Qualified Foreign Investors (QFIs) — into
one consolidated registration category, **FPI** **[Verified — the 2014 notification date, 1-June-
2014 commencement, and the FII+sub-account+QFI merger are independently confirmed]**. This is a
genuine measurement-continuity event in the same family as the atlas's other flagged splices (the
GDP base-year rebase, RESIDEX's 2015–18 pause) — a pre-2014 "FII" series and a post-2014 "FPI" series
are not automatically the same object counted the same way, and any full-history construction must
carry the recut as an explicit registry entry rather than assume a silent continuation.

**(ii) Quarterly shareholding patterns — the seat's actual series.** SEBI's LODR Regulations require
every listed company to disclose its complete shareholding pattern — promoter, FPI, DII, public —
within **21 days of each quarter-end**, free, per-stock (D08 I7b). This is the stock-level,
float-scaleable series A.3 is built from, distinct from and complementary to the NSDL aggregate. Its
honest hazards, stated plainly rather than assumed away: the data is a **snapshot**, not a continuous
series, so an intra-quarter extreme (built and partly unwound between two quarter-ends) is invisible
to it by construction; quarter-end holdings are a known point of **window-dressing** risk in
institutional portfolio management generally, a genuine (if unquantified for India specifically)
concern for reading a single snapshot as a clean measure of "true" average positioning; and refiling
revisions after the initial disclosure are a documented PIT hazard `partCDEFH.md`'s own Part C
already lists. None of these hazards undermines the capacity mechanism (A.3) — a snapshot extreme is
still a real extreme on the date it is measured — but they do mean the series is honestly noisier and
slower than its quarterly cadence alone suggests.

**(iii) The ownership arc, broad strokes.** FIIs were first permitted into Indian equities in
**September 1992**; Chakrabarti's own founding sample (A.2iii) covers the earliest years of that
regime. Aggregate foreign ownership of Indian listed equity **rose steadily from roughly 2002 through
2015**, briefly interrupted by the 2007–08 global financial crisis, then **moderated** through the
mid-2010s (US-China trade tension, Brexit-era global risk aversion) before **recovering through
December 2019** **[Verified — directional arc corroborated across multiple 2026 press retrospectives
tracking the same NSE Ownership Tracker series]**. The most recent prints available to this session
show a **multi-year structural decline** rather than a stable plateau: FPI ownership across the full
NSE-listed universe fell to roughly **16.7% at the December-2025 quarter-end (a 15-year low, last
seen ~2010)**, to **~15.8% at the March-2026 (FY26) close**, and further to **~15.1% by August 2026 —
a 17-year low** **[VERIFY: precise quarter-end dates and cross-source consistency — this session's
search access surfaced these figures from press aggregation of the NSE India Ownership Tracker across
several outlets (Upstox, Angel One, Business Standard, Newkerala) reporting on overlapping but not
always identically-dated windows through 2026; treat the direction and rough magnitude as reliable,
the exact decimal-point-quarter pairing as provisional]**. The same recent window shows real
dispersion by market-cap segment — **Nifty 50** names (the largest, most liquid, most benchmark-
relevant) carrying materially richer foreign ownership (**~21.8%**) than the **Nifty 500** as a whole
(**~16.8%**) **[VERIFY: exact reporting quarter for each figure, same sourcing caveat as above]** —
which resolves the atlas's own placeholder ("~16-18% of NSE500 float") as **directionally correct but
now testing the low end of that band**: the 2025–26 prints are not a stable mid-teens plateau, they
are a genuine multi-year low still being set at the time of writing, a fact this chapter states as
current context rather than as a settled level a design should freeze a parameter against.

**(iv) Sectoral concentration — financials, and why.** Financials/BFSI is consistently the largest
single sector in FPI portfolios by weight, and the largest single sector in FPI **selling** during
recent stress episodes specifically — the March-2026 sell-off saw BFSI carry roughly **51.5% of that
month's entire FPI outflow** across 21 of 23 tracked sectors in the red **[Verified — sector-outflow
share for the specific March-2026 episode; a point-in-time flow share, not independently confirmed
here as a stable holdings-weight percentage — treat the two as related but distinct claims]**. The
mechanism is more structural than idiosyncratic: BFSI is the largest single weight in both the Nifty
50 and Nifty 500 indices themselves, so any market-cap-aware foreign allocation — active or index-
tracking — mechanically concentrates there before any active conviction enters the picture; financials
also offer the deepest float and liquidity of any Indian sector, making them the natural parking
place for large, benchmark-relevant foreign mandates. The honest consequence for reading a **sector-
level** positioning extreme (per `partCDEFH.md` Step 2's own "sector-level extremes flag concentration
— financials-heavy caution"): a financials-sector ownership extreme may reflect **benchmark mechanics
and index-weight gravity** as much as active foreign conviction in the sector's own fundamentals,
a caveat worth carrying into any future sector-level use of the same construction, never assumed away
as pure signal.

**(v) The derivatives complication — the fast shadow, a different object.** NSE publishes daily
**participant-wise open interest** in index and stock derivatives (FII/DII/PRO/CLIENT categories),
free, after each session's close (typically 6:30–8:00pm IST) — commonly summarized in financial-press
commentary as an "FII long-short ratio" in index futures, and reported to move with or ahead of near-
term market direction. This series is genuinely useful, genuinely fast, and genuinely **not** the
object L14 seats, for three compounding reasons `partCDEFH.md`'s own Part C already labels this leg
"the FAST SHADOW... briefing only, never the seat's state" to guard against. **First, frequency**:
daily versus L14's quarterly cadence — a derivatives print can flip net-long to net-short within a
single session, while a cash-ownership percentile cannot move meaningfully inside a quarter by
construction (A.3v). **Second, reversibility**: an index-futures position is a leveraged, expiring
derivative contract, unwound at the stroke of a trade — none of the capital-movement friction A.3's
whole survival argument rests on applies to it, because there is no crowded cash position being
liquidated, only a contract being closed. **Third, ambiguity of intent**: the same open-interest print
generated by an FPI **hedging** an unchanged, large cash-equity book by shorting index futures is
statistically indistinguishable from an FPI making a fresh, outright directional bet — the derivatives
data cannot tell the two apart, whereas a shareholding-pattern filing is an unambiguous ownership fact.
An operator who reads a shift in the daily derivatives print as equivalent to a shift in L14's own
read is conflating a fast, noisy, hedge-contaminated shadow with a slow, unambiguous, capital-committed
state — Part G returns to this directly as one of the desk's two structural traps.

**(vi) The DII/SIP counterweight, and the honest open question it raises.** Domestic institutional
flow — principally mutual-fund SIP inflows plus insurance/pension AUM growth — has become a
structurally large counterweight to FPI flow volatility since roughly 2014–17. Monthly SIP inflows
alone reached **₹32,087 crore in March 2026**, sustaining **above ₹30,000 crore/month** through the
year **[Verified]**; across the first half of 2026, DII inflows totalled roughly **₹4.3 trillion**
against FPI outflows of roughly **₹2.8 trillion** over the same window — DIIs, in the financial
press's own now-standard framing, "bought every single time" FPIs sold, at one point nearly
quadrupling monthly purchases to offset a sharp FII exit **[Verified]**. This is the empirical basis
for D08's own I7(a) hypothesis — that the FII-flow-return relationship (and, by direct extension, the
capacity friction A.3 builds L14 on) may itself be **weakening** as DII depth grows large enough to
absorb a meaningfully larger share of FPI selling pressure than it could a decade ago. The honest
answer, stated as an open question rather than resolved either way, exactly as `partCDEFH.md`'s own
Part H frames it ("Unknowable: whether DII depth permanently blunts the capacity mechanism — each
unwind episode is one more observation"): the case for weakening is real (a bigger, steadier, more
calendar-driven — hence less valuation-sensitive — buyer genuinely blunts the price impact of a given
FPI unwind, all else equal); but the case for the mechanism holding is equally real and specific,
for three reasons. First, DII/SIP absorption is itself **concentrated in the same large, liquid,
index-heavy, already-most-FPI-owned names** most SIP and flexicap mandates favor — a small- or
mid-cap name at an extreme ownership percentile outside the largest caps does not enjoy the same
structural bid, so the aggregate "FII sells, DII buys" headline can hold in index terms while leaving
the capacity mechanism fully intact at the single-name level the ladder actually trades. Second, DII
flow is not itself infinitely elastic through every regime — it has historically slowed, if less
sharply than FPI flow, in the very acute risk-off windows L14 is built to flag, making "DII will
always absorb it" an assumption the seat should not quietly build in. Third, and most fundamentally,
Coval-Stafford's and Jotikasthira-Lundblad-Ramadorai's own mechanism (A.3i) does not require the
**absence** of a counterparty buyer, only that a forced, large unwind can outrun the near-term
absorptive capacity available at the prevailing price — a growing DII bid changes the **magnitude and
duration** of that friction, not whether the friction can exist at all. This is precisely why the
question is registered as an open research item (`partCDEFH.md`'s own **FL-D3**: unwind-episode depth
against DII absorption share, design-only, pending both sides' vaulted flow data) rather than answered
by assumption in either direction here.

**(vii) Synthesis.**

| Mechanism | Free observable | What L14 consumes | Honest gap |
|---|---|---|---|
| Flows follow returns (A.2ii–iii, Griffin-Nardari-Stulz/Chakrabarti) | NSDL daily/monthly flows | Nothing — structurally excluded from the module's own API (`partCDEFH.md` Part D) | Whether any short-window, non-momentum flow content survives as a candidate for L2/L9 rather than L14 — not tested here |
| Positive-feedback theory (A.2iv, Brennan-Cao/DSSW) | N/A — theoretical | Explains WHY flows decay as a signal rather than merely observing that they do | No India-specific test of the extrapolation-strength parameter itself |
| Fire sales / fragility (A.3i, Coval-Stafford/Greenwood-Thesmar/Jotikasthira-Lundblad-Ramadorai) | Quarterly shareholding patterns, float-scaled | The entire survival argument for the seat's existence | No India-specific quantified price-impact-per-extreme-unit estimate yet (FL1/FL2, data-gated) |
| Float-scaling correction (A.3iii) | Promoter-holding + free-float aggregates | The denominator (`partCDEFH.md`'s own "float rule") | No single free, continuously-updated national free-float series; assembled from index-provider factsheets + filings, quarterly only |
| 2014 FII→FPI regime change (A.4i) | SEBI/NSDL registration records | A mandatory breaks-registry entry, never silently spliced | Whether any pre-2014 vs. post-2014 discontinuity in the flow series itself (beyond naming) has been quantified — not yet tested |
| Sectoral concentration (A.4iv) | NSDL/press sector-flow breakdowns | The financials-heavy caution on any sector-level extreme | No decomposition yet separating benchmark-weight gravity from active conviction in the financials read |
| Derivatives shadow (A.4v) | NSE participant-wise OI, daily | Briefing only — explicitly not a state input (`partCDEFH.md` Step 3) | An explicit, quantified divergence-monitor between the shadow and the seat's own quarterly state — designed, not yet run |
| DII/SIP counterweight (A.4vi) | AMFI SIP data, DII flow aggregates | An annotation traveling with every extreme flag, never a size-blunting override | FL-D3 (design-only): does DII depth measurably shrink unwind depth, episode by episode — awaits vaulted data on both sides |

---

## PART G — Operator psychology

Part A documents a seat built almost entirely out of what it refuses: the single most popular FPI
narrative in Indian markets — watch the daily flow print, trade what it implies — is excluded by
design, on evidence spanning two decades and three independent decay channels (A.2vi), and what
survives in its place is a quiet, quarterly, reduce-only capacity flag that will never make a
headline the way "FIIs bought ₹4,000 crore today" does. That combination — a popular, intuitive,
daily-repeated narrative on one side, and a slow, unglamorous, risk-only construct on the other —
is exactly the setup that produces sustained pressure to trade the excluded signal anyway, dressed
in whatever justification the moment supplies. This Part maps that pressure and its variants to the
countermeasures Part A's own construction already builds in.

### G.1 The flow-narrative industry

**Mechanism.** NSDL's daily FII/FPI net-flow print is the single most repeated data point in Indian
financial media — more frequent, cheaper to produce, and more narratively satisfying than any credit-
cycle, capex-cycle, or even earnings data point this ladder reads, and it persists as a headline
despite A.2's own finding for reasons that are not purely psychological. **First**, contemporaneous
correlation between flows and returns genuinely is high — that is precisely what "flows follow
returns" means — so watching the flow print *feels* like watching a leading indicator when the
evidence says it is closer to a coincident-to-lagging one dressed in directional language. **Second**,
there is a pure content-supply argument layered on top of the psychological one: television, portals
and brokerage research need a fresh, simple, dailyproducible headline every single trading day, and
"FIIs bought/sold ₹X crore" is the cheapest one available — free, daily, requiring no analysis —
which keeps the narrative alive commercially regardless of its evidentiary weakness.

**Countermeasure.** The registry-level fix removes the temptation rather than merely warning against
it: `partCDEFH.md`'s own Part D states the module "exposes no flow-named API (tested)" — flow
momentum is not merely down-weighted, there is **no code path** by which today's headline print can
move L14's regime-score contribution, structurally, regardless of how an operator narrates the day's
number.

### G.2 The validation trap

**Mechanism.** An operator holding a position sees sustained FPI buying concentrate in names already
owned and reads it as independent, external confirmation of the domestic thesis — "smart global
money agrees" — at precisely the moment A.2's own finding says the causal arrow most likely runs
backward: the foreign buying is very often the return-chasing response to a rally the operator's own
domestic conviction already produced, not an independent data point confirming it. This is a home-
bias-adjacent trap — foreign participation carries outsized informational weight in a market where
domestic capital structurally under-engages with foreign perspectives — compounded by ordinary
confirmation bias reaching for the reading that supplies validation, at exactly the point (a position
already run up, near a local extreme) resisting that reading would matter most.

**Countermeasure.** The same structural removal as G.1 applies with one addition specific to the
legitimate half of this seat: L14's own reading is `reduce_only: true` — even the surviving,
positioning-extremes signal can only ever argue for **less** risk, never for more, foreclosing the
entire class of "foreign buying validates adding to the position" reasoning at the registry level,
not merely at the excluded flow-momentum level.

### G.3 Exit-crowding denial at extremes

**Mechanism.** The stocks that reach a genuine, top-percentile foreign-ownership extreme are —
almost by selection — the desk's own highest-conviction, best-known names, precisely because the
same qualities that attracted the operator's own domestic conviction attracted the foreign capital
that produced the extreme in the first place. A reduce-only L14 flag firing on a name the operator
already loves therefore reads, subjectively, as noise to override — "this isn't a crowded trade,
it's just a genuinely great business everyone correctly wants to own" — rather than as the exact
structural setup A.3's own literature (Coval-Stafford, Greenwood-Thesmar, Jotikasthira-Lundblad-
Ramadorai) is built to flag. This is the hardest trap this seat produces precisely because the
rationalization is not obviously false: a stock genuinely can be both an excellent business and a
crowded, fragile position simultaneously — the two claims are not in tension — but an operator under
narrative pressure treats "it's a good business" as a rebuttal to "it's crowded," when A.3(ii)'s own
point is that the capacity risk is **orthogonal** to quality, not a judgment about it.

**Countermeasure.** The seat's construction never asks the operator to first agree a name is "not
good enough to deserve" its ownership level — it reads the float-scaled percentile mechanically
(A.4ii's own quarterly, disclosure-driven series), immune to a narrative override in exactly the same
way L12's HPI-driven construction is immune to "property never falls" (`fincycle-deep partA` G.2) —
and its permission applies purely as a capacity-risk scalar, never as a verdict on the underlying
business.

### G.4 The desk's two traps: the permanent floor, and the fast shadow

**Treating the DII bid as a permanent floor.** An operator who has watched "FII sells, DII buys" hold
through a decade (2014–2024, and again through the H1-2026 episode A.4vi documents) can unconsciously
promote an **observed pattern** to an **assumed structural law** — exactly when A.4vi's own honest
accounting shows the pattern is least reliable for precisely the names where L14 fires: extreme-
ownership stocks outside the largest, most SIP-favored caps, where the DII absorptive bid is
structurally thinner. **Countermeasure**: A.4vi's own framing — an open, FL-D3-registered question,
not a settled fact — is the discipline; the seat's τ½ (12–36 months) and reduce-only design already
price in that positioning unwinds slowly and **incompletely**, never assuming DII absorption smooths
every unwind away, which is exactly why the seat still exists as a risk-off conditioner rather than
having been retired on the assumption the DII bid solved the problem structurally.

**Reading derivative positioning as the seat's state.** An operator checking the daily FII long-short
index-futures ratio and treating a shift there as equivalent to a shift in L14's own read is
conflating two different objects on two different clocks: a reversible, possibly hedge-driven
derivative flow updating daily, against a capital-committed cash-ownership stock that moves over
quarters (A.4v). **Countermeasure**: L14's own indicator list is exclusively NSDL aggregates and
quarterly shareholding patterns — index-futures open interest is not an L14 input at all
(`partCDEFH.md`'s own labeling: "briefing only, never the seat's state"); an operator wanting a fast
read of the same underlying global-flow phenomenon already has the correct fast seat — L9's own
NSDL-flow confirm layer, τ½ 3–9 months (`globalcycle-deep partA` A.2i) — and should route there,
never treat L14's quarterly-cadence read as something a daily derivatives print can override
intraday.

### G.5 Countermeasures mapped

Four structural features do this Part's actual work. **(1) The structural API exclusion** (G.1) —
flow momentum has no code path into the regime score, so there is nothing for the daily headline
temptation to act on even if an operator wanted it to. **(2) `reduce_only: true`** (G.2–G.3) — the
surviving signal can only ever subtract risk, foreclosing both the validation-seeking read (foreign
buying as license to add) and the quality-override read (a beloved name's extreme as license to
ignore the flag) at the registry level. **(3) The open, registered structural-change question**
(G.4a) — A.4vi's own honesty that DII depth's effect on the capacity mechanism is unresolved, not
assumed, keeps a decade-long observed pattern from silently becoming an assumed permanent floor.
**(4) The clean separation of fast shadow from slow state** (G.4b) — the derivatives leg is labeled
briefing-only in the module's own construction, with the correct fast seat (L9) named explicitly for
an operator who genuinely needs a faster read. None of these four asks the operator to be wiser under
daily pressure than Part A's own evidence already justifies; each converts a live judgment call —
decide whether today's flow print finally means something, decide whether this foreign buying really
does validate the thesis, decide whether this beloved name's extreme is really a crowded trade,
decide whether the DII bid has finally solved the problem, decide whether today's derivatives print
should override this quarter's ownership read — into a structural non-decision, made once, in the
registry, before the daily headline that would have made it hardest.

### G.6 Failure mode → countermeasure map

| Failure mode | Mechanism (grounded) | Countermeasure |
|---|---|---|
| Trading today's "FIIs bought/sold ₹X crore" headline directionally | High contemporaneous flow-return correlation feels like a leading indicator when the evidence (A.2ii–iii) says the causality runs the other way; a daily-repeatable, cheap-to-produce headline persists regardless | Flow momentum has no code path into the regime score at all (`partCDEFH.md` Part D) — a structural exclusion, not a haircut |
| Reading sustained foreign buying in a held name as independent validation | Home bias primes the operator to want external confirmation exactly where Griffin-Nardari-Stulz/Chakrabarti/Brennan-Cao say the causality runs backward (flows chase returns, not the reverse) | L14 is `reduce_only: true` — even the legitimate positioning signal can only ever argue for less risk, foreclosing "foreign buying licenses adding" at the registry level |
| Overriding a reduce-only flag on a beloved, high-conviction name ("it's just a great business") | The same qualities that produced the operator's own conviction produced the crowding; quality and fragility are not in tension, but narrative pressure treats one as a rebuttal of the other | Mechanical, disclosure-driven float-scaled percentile construction, immune to a narrative override; the flag is a capacity-risk scalar, never a verdict on the business |
| Treating the DII/SIP bid as a permanent floor that has retired the capacity mechanism | A decade of "FII sells, DII buys" holding at the index level gets promoted from observed pattern to assumed law, precisely where it is least reliable — extreme-ownership names outside the largest, most SIP-favored caps | FL-D3 keeps the question explicitly open and registered, not assumed; τ½ 12–36m and reduce-only design already price in slow, incomplete unwinds regardless of DII depth |
| Reading a shift in the daily FII index-futures long-short ratio as a shift in L14's own state | Conflating a fast, reversible, possibly hedge-driven derivative flow with a slow, capital-committed cash-ownership stock — two different objects on two different clocks | Derivatives OI is not an L14 input at all (briefing-only, per `partCDEFH.md`); the correct fast seat for a genuine fast read is L9's own NSDL-flow confirm layer, τ½ 3–9 months |
| Using low FPI ownership as a contrarian "under-owned, therefore due to re-rate" buy trigger | Low ownership is substantially a record of a name's own trailing return history (no rally, no return-chasing inflow) — using it as a buy signal reimports the exact reversed-causality claim A.1–A.2 excluded, merely relabeled from a flow to a level | L14 conditions only the top-percentile (crowded-exit) side; the asymmetry is structural (`reduce_only: true`), not an oversight — a low reading carries no positive-tilt authority |

None of these six countermeasures asks the operator to out-resist, under daily headline pressure, an
argument Part A's own evidence has already settled. Each converts a live judgment call — decide
whether today's flow print finally matters, decide whether this inflow really does validate the
thesis, decide whether this name's crowding is outweighed by its quality, decide whether the DII bid
has finally solved the unwind problem, decide whether today's derivatives print outranks this
quarter's ownership read, decide whether an under-owned name is due for a re-rate — into a structural
non-decision, made once, in the registry, before the moment that would have made it hardest.

---

**Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in)**
**Date: 2026-09-02 · v1.0**
