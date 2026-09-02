# Oil and Energy — the Kilian Decomposition, OPEC/Shale Regimes, and India's Shock-Type Asymmetry

**Version 1.0 · 2026-09-02 · Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in) · governed by research/CONTRACT.md**

**Verdict up front:** Atlas row **2.12** ("oil/energy cycle") contributes **no new ladder seat**.
`config/ladder.yaml`'s `L9_global_financial_cycle` role line already says the seat "includes
Kilian-decomposed oil (never raw price level)"; this chapter supplies, at teaching depth, the
decomposition that sentence has always presupposed, the OPEC/shale regime history behind why the
old "5–10y investment-lag cycle" framing survives only as regime historiography rather than a
clock, and the desk's own shock-type test of the mechanism on India. The desk's own trial —
**OL1** — finds a large, direction-consistent asymmetry (demand-flavored oil-up years **+38.1%**
mean India equity return vs supply-flavored oil-up years **−43.1%**, a **+81.2pp** gap against a
**≥+10pp** bar, **PASS**) on a construction whose own honesty this chapter states plainly: n=11
oil-up years (8 demand-flavored, 3 supply-flavored — tiny), and the world-equity-sign proxy used
to flavor each year conflates "demand-driven oil" with "global risk appetite generally," so the
print is a real, bar-clearing directional signal capped by a crude identification, not a
calibrated pass-through coefficient. `research/cycles/oil-fold/partDH-verdict-routing.md` (this
entry's own routing file, already on disk) carries the identification ladder, the design items
this chapter does not re-litigate (**OL-D1**, the real Kilian-index pull; **OL-D2**, the
2014–16 windfall as the reverse experiment), and the harvest/knowledge-ledger bookkeeping; this
file supplies the theory, the regime history, and the India case record those items condition on.

**Headline results, in one line each:** the decomposition's critique lineage (Kilian 2009 → Kilian-
Murphy 2012, 2014 → Baumeister-Hamilton 2019) is a maturing, not discredited, machine, and the desk
inherits its mature end; the regime history is OPEC/shale politics, not a capacity-lag clock — the
2014–16 shale break shortened the supply leg's response time from years to quarters, while OPEC/
OPEC+ politics still set the floor it operates against; India's own transfer flips sign by shock
type, not episode size — 1973–74, 1979–80, 1990, and 2022 are unambiguous CAD/INR/inflation hits,
while 2004–08, 2010–11, and 2021 arrived with the same global growth that funded the larger import
bill, and 2014–16 is the clean reverse experiment, a windfall the government mostly captured.

**Cross-reference discipline, stated once and then honored throughout.** This chapter owns three
things at teaching depth no other file in this program does: the Kilian (2009) structural
identification and its critique lineage; the OPEC/OPEC+/shale regime chronology as regime history
(not mechanism); and India's shock-type asymmetry as a designed exhibit. It does **not**
re-derive: the commodity-supercycle mechanism, capex-lag machinery, or shale elasticity numbers
(owned by `docs/cycles/14-commodity-supercycle.md` and
`research/cycles/commodity-deep/partB-cases.md`, cited by case number below); the global-cycle
seat's own construction, budget, or its GF1–GF3/DL1–DL3 trials (owned by
`docs/cycles/22-global-cycle.md` and `research/cycles/globalcycle-deep/`, cited for the seat's
framing and the May-2026 live episode); or subsidy-accounting machinery generally (owned by
`docs/cycles/21-fiscal-cycle.md`) — this chapter leans on the commodity monograph's own
administered-price record (§B3.3/§B3.5) for India's OMC/subsidy mechanics, restating figures only
where the shock-type framing here requires it. Every figure not already verified in one of those
files is search-verified as of September 2026 or tagged `[VERIFY]`.

---

## A. The decomposition, taught properly

### A.1 The object: three shocks, one price

**Lutz Kilian, "Not All Oil Price Shocks Are Alike: Disentangling Demand and Supply Shocks in the
Crude Oil Market"** (*American Economic Review* 99(3), 2009, pp. 1053–69) is the paper the ladder's
own L9 role line already leans on without naming — `config/ladder.yaml` states plainly that L9
"includes Kilian-decomposed oil (never raw price level)," and this section is that sentence's
teaching content. Kilian's insight starts from an observation any macro desk half-knows:
regressions of GDP, inflation, or equity returns on the raw oil price are notoriously unstable
across sample periods, and the standard "oil shocks cause recessions" literature descending from
**Hamilton (1983)**, *Journal of Political Economy* 91(2): 228–48, could not explain why. Kilian's
answer: **the price is one number, but it can arrive by three structurally different roads**, and a
raw price series cannot tell them apart no matter how large the sample.

The three orthogonal structural shocks Kilian's model identifies are:

1. **An oil supply shock** — a disruption to global crude oil production itself (an embargo, a
   war, a well blowout, a cartel's own restriction decision).
2. **An aggregate demand shock** — a shift in global demand for *all* industrial commodities,
   driven by the world business cycle (a synchronized global boom or bust that would move oil
   demand exactly as it moves demand for copper, coal, or dry-bulk freight).
3. **An oil-market-specific (precautionary) demand shock** — a shift in the *anticipated future
   availability* of oil specifically, distinct from either current supply or the general business
   cycle: fear that a supply disruption is coming (even before it arrives) moves current
   precautionary buying and inventory behavior on its own.

Each of the three moves the real price of oil upward, and a chartist reading the price alone
cannot distinguish which one is doing the moving in any given month. That indistinguishability is
precisely the desk's own reason for banning the raw price level as a signal input anywhere in this
program (`config/ladder.yaml`'s parenthetical is a design commitment, not a stylistic footnote):
the same $20 rise in Brent means opposite things for portfolio construction depending on which of
the three roads produced it, a point Part A.4 below states in full for India specifically.

### A.2 Identification: the short-run supply-inelasticity ordering, honestly stated

Kilian's structural VAR identifies the three shocks through a **recursive (Cholesky) short-run
restriction** — an ordering of three variables (global crude oil production, a global real
activity index, and the real price of oil) in which each variable is allowed to respond
contemporaneously (within the same month) only to the shocks that precede it in the ordering:

- **Global oil production is ordered first**, under the assumption that it does **not** respond
  within the month to either the aggregate-demand or the oil-specific-demand shock — i.e., the
  short-run price elasticity of oil supply is treated as **exactly zero** at monthly frequency.
  The economic argument is a genuine one: bringing incremental crude to market — securing rig
  time, drilling, completing a well, or (on the OPEC side) coordinating a quota change — takes
  weeks to months even when the decision to do so is made instantly, so within a single month,
  observed production is effectively predetermined by decisions made earlier.
- **The global real activity index is ordered second**, allowed to respond within the month to a
  supply shock and to its own aggregate-demand shock, but assumed **not** to respond
  contemporaneously to the oil-specific demand shock — a sluggishness assumption: broad global
  economic activity (proxied, per A.3 below, by dry-bulk shipping volumes) is assumed not to move
  within the same month purely because of a shift in oil-market precautionary sentiment.
- **The real price of oil is ordered last**, free to respond within the month to all three shocks
  — the plainly correct ordering for the most liquid, fastest-repricing variable in the system.

**This is an honest, stated, exact-zero identification — and its fragility is exactly where the
paper's own critique lineage begins.** The ordering does not claim supply elasticity is *small*;
it claims supply elasticity is **zero**, a knife-edge restriction, and the entire attribution of
"was this month's price move supply- or demand-driven" rests on that single assumption holding.
An era in which the true short-run supply elasticity is meaningfully positive — precisely the
shale era Part B documents, where a well can move from spud to first production in months rather
than years — is an era in which the ordering's own premise is under the most strain (the same
point the commodity monograph's case 6 makes generally: "the extraction-capacity-lag mechanism …
is not a fixed constant across the oil market; it is technology-dependent, and shale specifically
broke it," `research/cycles/commodity-deep/partB-cases.md` case 6 — cited for its identification
implication, not re-derived). And an exact-zero restriction is one point in a much larger space of
models that would fit the same data equally well — precisely the opening the next two papers
exploit.

### A.3 The critique lineage: from an exact ordering to a bounded, then a Bayesian, machine

**Kilian & Murphy, "Why Agnostic Sign Restrictions Are Not Enough: Understanding the Dynamics of
Oil Market VAR Models"** (*Journal of the European Economic Association* 10(5), 2012, pp.
1166–88) is the paper this chapter's brief calls the "Kilian-Murphy elasticity bounds," and it is
a genuine methodological refinement rather than a defense of the original recursive ordering. The
paper's own logic: if a researcher, uncomfortable with an *exact* zero restriction on short-run
supply elasticity, relaxes it to a **sign restriction** instead (only requiring, say, that a
positive supply shock raises production and lowers price, without pinning the exact contemporaneous
magnitude), the sign restriction alone turns out to admit far too wide a range of "qualitatively
similar" model solutions — many of them implying economically implausible elasticities (an oil
supply curve that is, in effect, backward-bending or absurdly flat) that a sign restriction alone
cannot rule out. Kilian and Murphy's fix is to **combine** the (weaker) sign restrictions with
**empirically plausible bounds on the magnitude** of the short-run oil supply elasticity and on
the impact response of global real activity to an oil-specific demand shock — not an exact zero,
and not "any sign will do," but a bounded range grounded in what the industry's own physical and
financial constraints make plausible. Imposing those bounds collapses the admissible model space
down to a small number of qualitatively similar, economically sensible solutions — the paper's own
demonstration that agnostic sign restrictions, taken alone, are **not enough**, and that some
economically informed bound is required either way.

**Kilian & Murphy, "The Role of Inventories and Speculative Trading in the Global Market for Crude
Oil"** (*Journal of Applied Econometrics* 29(3), 2014, pp. 454–78) extends the three-shock model
with a fourth structural piece the original ordering could not separate: a **speculative
(storage/inventory) demand shock**, distinct from flow demand and flow supply. The original
model's "oil-specific demand shock" conflated buying oil to *use* soon (precautionary demand)
with buying oil purely to *store* against a future price rise (speculative demand), and only
inventory data can tell them apart: rising inventories alongside price signal speculation; flat or
falling inventories with rising consumption signal flow demand. Using this richer identification,
Kilian and Murphy directly rebut the popular post-2008 narrative that speculation or a supply
shortfall drove the 2003–2008 surge: their estimates attribute it overwhelmingly to **unexpected
increases in world oil consumption driven by the global business cycle** — the same China-led boom
the commodity monograph's case 5 documents (cross-ref, not re-derived).

**Baumeister & Hamilton, "Structural Interpretation of Vector Autoregressions with Incomplete
Identification: Revisiting the Role of Oil Supply and Demand Shocks"** (*American Economic Review*
109(5), 2019, pp. 1873–1910) is the reworking this chapter's brief flags for verification, and its
specifics check out cleanly. The paper's contribution is a genuine reframing: traditional
structural-VAR identification — whether Kilian's exact recursive zeros or Kilian-Murphy's bounded
sign restrictions — can be recast as an extreme special case of Bayesian inference asserting
near-certainty about parameters not, in truth, known that precisely. Baumeister and Hamilton
instead build a fully Bayesian structural VAR with **genuinely informative priors** over the
identifying elasticities, propagating real uncertainty honestly into the posterior rather than
conditioning on one assumed-true identification. The headline result is not a minor refinement:
relative to earlier point-identified estimates, **supply disruptions turn out to be a bigger
factor** and **inventory/speculative trading a smaller factor** than Kilian-Murphy's own
1994–2014-era estimates implied, and — directly relevant to Part A.4's India argument —
**oil supply shocks reduce global economic activity with a lag, whereas oil demand shocks do not**.
This is a Bayesian-robustness version of exactly the asymmetry OL1 tests on India: a demand-driven oil rise
and a supply-driven oil rise are not merely differently *sized* shocks to the same variable, they
are shocks with **different macro consequences by construction**, now confirmed under a
substantially less restrictive identification than Kilian's original recursive ordering.

**The honest state of the lineage, stated plainly.** This is not an insight overturned but a
useful decomposition progressively stress-tested and surviving each time in strengthened form:
Kilian-Murphy (2012) shows the core distinction survives relaxing the exact-zero restriction to
economically sensible bounds; Kilian-Murphy (2014) shows it survives splitting out a genuinely
separate speculative-demand channel, settling the "was 2003–08 speculation-driven?" argument (no);
Baumeister-Hamilton (2019) shows it survives a full Bayesian reworking, and sharpens rather than
dissolves the demand/supply growth-effect asymmetry. A desk consuming "the Kilian decomposition"
in 2026 inherits the mature end of a fifteen-year, three-times-stress-tested strategy, not a
fragile first cut — why `config/ladder.yaml`'s L9 role line commits to it as a frozen design
constraint rather than a provisional placeholder.

### A.4 The global real activity index: construction, the 2018 correction episode, and free availability

Kilian's global demand shock is not identified from the oil price alone — that would beg the
question — but from an independent proxy for the world business cycle built specifically to avoid
simultaneity with the oil market: the **index of global real economic activity**, an equal-
weighted panel of **ocean dry-bulk single-voyage freight rates** across many routes carrying
industrial bulk cargo (coal, grain, iron ore), deflated to real terms and **linearly detrended** to
strip out shipping's secular cost decline, leaving deviations from trend as a proxy for the
*volume* — not price — of global industrial-commodity demand. The choice is deliberate: dry-bulk
freight demand is a byproduct of physical industrial activity, available monthly for decades, and
— the property that matters most — **not itself an oil-price-based series**, avoiding the reverse-
causality a commodity-price-based proxy would carry.

**The 2018–19 correction episode, verified.** James D. Hamilton's **"Measuring Global Economic
Activity"** (NBER Working Paper 25778, 2018/2019) raised a substantive critique: the index's level
appeared highly sensitive to an essentially arbitrary base-year normalization choice made in
constructing the underlying nominal freight-rate sub-index, which Hamilton argued cast doubt on
the index's reliability and motivated alternative measures of global activity. The critique
triggered a direct technical response: **Kilian & Zhou (2018)**, "Modeling Fluctuations in the
Global Demand for Commodities," and **Kilian (2019)**, "Measuring Global Real Economic Activity:
Do Recent Critiques Hold Up to Scrutiny?" (*Economics Letters* 178, pp. 106–10), traced Hamilton's
concern to an actual **coding error** in the originally published series: the nominal freight-rate
sub-index feeding the index had been **log-transformed twice** by mistake. Correcting that single
error — removing the duplicate log transformation — resolves essentially all of the sensitivity
Hamilton's critique identified, and the corrected index differs only marginally from the original,
leaving Kilian (2009)'s own core empirical findings materially unchanged. The episode is worth
naming for the desk's own epistemic hygiene: a legitimate critique surfaced a real coding mistake,
found and fixed within roughly a year, with the underlying methodology surviving intact.

**Free availability, resolved.** `research/dossiers/08-india-mid-cycles.md` (D08, §F13/I11) flagged
Kilian's index as "maintained and freely downloadable from his personal academic webpage
`[VERIFY: current URL/maintenance status]`" — that flag is now resolved cleanly: the corrected,
current index is maintained officially as the **"Index of Global Real Economic Activity" (IGREA)**
by the **Federal Reserve Bank of Dallas** (`dallasfed.org/research/igrea`) and mirrored on **FRED**
under series ID `IGREA`, updated monthly. What D08 flagged as a single professor's personal-webpage
dependency is, as of this writing, an institutionally hosted, regularly updated, genuinely free
series — exactly the kind of data-source durability the Contract's free-data rule (§7) requires,
and a stronger footing than the dossier's own caveat anticipated.

### A.5 Why the desk commits to decomposition over the raw price — stated for an 85%+ importer

Every argument above cashes out in one design sentence: **for an economy importing 85%+ of the
crude it consumes** (the commodity monograph's own verified table — 87.7% FY24, 88.2% FY25, "over
90%" FY26 — `research/cycles/commodity-deep/partB-cases.md` §B3.1, cited not re-derived), **the
same $20 rise in Brent is a headwind or a symptom depending entirely on which of Kilian's three
roads produced it, and a raw-price rule cannot tell the two apart.** A supply-shock $20 rise — a
Hormuz disruption, an embargo, a cartel restriction — is a pure cost shock with no offsetting
channel: the import bill rises with no matching export or growth improvement, so the CAD widens,
the rupee weakens, WPI (and with a lag CPI) rise, and RBI's policy room narrows exactly when growth
may also be softening — Part C below's unqualified "risk-off India." A demand-shock $20 rise — a
synchronized global boom lifting oil, copper, and freight together — arrives bundled with the same
expansion lifting demand for India's own exports and often FII inflows into the same "global boom"
narrative: the CAD line item still deteriorates in isolation, but the backdrop is frequently
favorable for growth and equity performance — "global boom lifting all boats." Collapsing both
into one "oil up = risk-off" rule misclassifies a meaningful share of the record (Part C's table
quantifies this), the "magic-number-style oversimplification" D08 itself names
(`research/dossiers/08-india-mid-cycles.md` §F13/I11) and why `config/ladder.yaml`'s L9 role line
commits to the decomposed signal as a frozen design constraint, not a swept parameter.

---

## B. The regime historiography (the "cycle" that is actually regimes)

### B.1 Why this is regime history, not a clock — and where it still connects to a real mechanism

Atlas row 1.6/2.12's own framing names oil as sitting inside a "5–10y investment lag + OPEC regime
shifts" — and the honest reading, consistent with this program's own clock-test discipline
(`docs/CYCLE_ATLAS.md` §0; `docs/cycles/19-kitchin-juglar.md`'s own five-for-five fixed-period
failure record, cross-referenced by the dollar-fold monograph's own A.4), is that the "oil cycle"
is not a cycle at all in the ladder's technical sense: it is a sequence of **dated policy and
geopolitical regime turns** — cartel decisions, wars, sanctions, a technological supply-side break
— overlaid on a genuine but variable-length capacity-investment lag that the commodity-supercycle
monograph's own case 4 already documents in detail for the 1970s–1990s arc specifically (cross-
ref, not re-derived: "conventional supply still runs a multi-year lag... precisely the atlas's own
extraction-capacity-lag mechanism running in full," `research/cycles/commodity-deep/partB-cases.md`
case 4). This section's job is narrower and complementary: to lay out the **regime chronology**
itself, dated and sized, as the historiography a desk needs in order to read any given oil-price
episode correctly — not as a timing tool, but as **context** for classifying what kind of episode
is currently live.

### B.2 The embargo-revolution era, 1973–1980

The two 1970s shocks are already verified in full in the commodity-supercycle monograph's case 4
and are cited here only for their regime-classification content, not re-derived: the **OAPEC
embargo of the US from 19 October 1973** (Yom Kippur War) saw the price **nearly quadruple, from
$2.90/barrel pre-embargo to $11.65/barrel by January 1974**; the **1979 Iranian Revolution**
produced a global supply loss of only ~4%, yet the market's own reaction **more than doubled** the
price over the next twelve months to roughly **$39.50/barrel**, OPEC's own posted price rising from
**$16/barrel (January 1980) to over $36/barrel (September 1980)**. Both are, in Kilian's own
taxonomy, textbook **oil supply shocks with a geopolitical trigger** — a war and a revolution
physically removing barrels from the market, not demand-driven or speculative moves — precisely why
Part C classifies both as unambiguous India cost shocks with no offsetting channel.

### B.3 Quota unraveling and the 1986 collapse

The decade between the two 1970s shocks and the 1986 collapse is the regime era in which OPEC,
principally Saudi Arabia, acted as the market's **swing producer** — cutting output to defend the
posted price as global demand weakened (Volcker's disinflation, commodity monograph case 4) and
new non-OPEC supply the 1970s' price signal had commissioned (North Sea, Alaska) arrived seven-to-
ten years later, exactly the extraction-capacity-lag mechanism's clearest historical instance. The
regime ended when Saudi Arabia abandoned the role: adopting **"netback pricing"** in **August
1986**, spot prices collapsed from **$28/barrel (1985) to $14 (1986)**, briefly **under $10**
mid-year — defend share, not price, the direct ancestor of the 2014 decision (B.6). Two sovereign
casualties rode this down-leg (commodity monograph case 4, cited not re-derived): Mexico's 1982
debt moratorium and the Soviet Union's own terminal hard-currency exhaustion through the late
1980s.

### B.4 The 1990 Gulf spike — a clean supply shock, rapidly resolved

**Iraq's invasion of Kuwait on 2 August 1990** produced the record's cleanest textbook supply
shock: Kuwait's ~2.5 million b/d vanished immediately and Iraqi exports of ~3 million b/d were
halted by sanctions, a combined loss of **~5.5 million b/d (~8% of world supply)** — larger than
either the 1973 or 1979 disruptions **[Verified]**. Brent rose from **$15/barrel (end July 1990) to
$41.45 (October 1990)**; WTI hit **$27.31 in August** and peaked at **$36.04 in October** from a
**$16.70 (June 1990)** base — a **116% four-month increase [Verified]**. What distinguishes this
episode from the 1970s shocks is the speed of its resolution: **Operation Desert Storm began 17
January 1991**, the ground war ended within **100 hours** by **28 February 1991**, and oil fell
back to roughly **$20/barrel** once the military outcome removed the uncertainty premium
**[Verified]**. The 1990 spike is Kilian's cleanest possible pure oil supply shock — sudden, large,
geopolitically unambiguous, resolved by a military outcome rather than a demand-side adjustment or
capacity-lag response — why Part C treats it, alongside 1973–74 and 1979–80, as an unambiguous
India cost episode with no offsetting channel.

### B.5 The 1998 trough, the 1999 discipline era, and the 2003–08 demand-driven ascent

The **1998 $10 oil episode** — already verified in the commodity monograph's case 4 — closed the
two-decade glut the 1980s' collapse opened: the 1997 Asian Financial Crisis devastated demand from
a region supplying **80% of global oil demand growth from 1990–97**, and OPEC compounded the error
by **raising quotas in November 1997** just as the crisis hit, driving WTI to roughly **$10/barrel
by December 1998**, some grades near **$6**. The response was fast: at **The Hague on 23 March
1999**, OPEC and non-OPEC producers (Russia, Mexico, Norway) agreed to cut combined output by
**2.104 million barrels/day from 1 April 1999** (OPEC's own share **1.7 million b/d**), with
analysts expecting a recovery toward **$18–20/barrel** on **75–80% compliance [Verified]**. This
restored a compliance-driven discipline regime that ran into the demand-driven China-led
supercycle (commodity monograph case 5, cross-ref, not re-derived): the 2003–08 rise from roughly
**$25 to Brent's all-time nominal peak of $147.30/barrel in July 2008** was, per D08's own
characterization, **"substantially demand-driven … and therefore less unambiguously [negative for
India]"** (`research/dossiers/08-india-mid-cycles.md` §I11) — Part C.3 tests this against India's
own CAD record.

### B.6 The market-share war, 2014 — and the birth of OPEC+

Meeting in **Vienna on 27 November 2014**, Saudi oil minister **Ali al-Naimi** confirmed OPEC
would **not cut production** from its 30 million-b/d quota — **"That is right,"** he told
reporters, and later wrote he'd estimated essentially **zero chance** non-OPEC producers (Russia,
Mexico, Kazakhstan, Norway) would cut alongside OPEC **[Verified]**. His stated rationale — **"If
we … cut production without the participation of major non-OPEC members, we would be sacrificing
revenues as well as market share"** — directly repudiated the 1980s swing-producer role (Part
B.3): defend share, not price, against the shale-era supply curve Part B.7 shows had by 2014
fundamentally changed shape. Brent fell from **$112/barrel (June 2014) to $62 (December 2014)** and
on to a **$31 trough (January 2016)** (commodity monograph case 6, cited not re-derived). OPEC's
own shape then changed decisively: at **Vienna on 10 December 2016**, OPEC and **eleven non-OPEC
producers led by Russia** signed the **"Declaration of Cooperation"** — the birth of **"OPEC+"** —
agreeing a combined cut of roughly **1.8 million b/d**, Russia's first-ever join of an OPEC-led cut
**[Verified]**. 2014–2016 is therefore two events: a market-share war breaking the 1980s playbook,
then the creation of a wider cartel-plus-non-cartel institution governing every OPEC-side decision
since.

### B.7 The shale break — a structural change to the supply curve's short end

The mechanism behind why 2014's price war unfolded so differently from 1986's is fully documented
in the commodity monograph's case 6 and is cited here only for its *identification* implication
(Part A.2), not re-derived: shale's supply-price elasticity rose from **statistically
insignificant in its 2000–2008 pilot phase to 1.1 (significant) in 2009–2016**, with **~85% of the
total supply impact realized within two years** — the fastest documented supply response in
oil-market history, structural rather than merely faster, since a shale well runs spud-to-
production in **months** against conventional timelines of **years**. New context this chapter
adds: **new-well breakevens averaged roughly $59–70/barrel industry-wide in 2024** (Dallas Fed
Energy Survey; Permian Midland/Delaware $62/$64), drifting toward **~$70/barrel by 2025**
`[VERIFY: one industry report projects $95/barrel — a single house's forward view, not consensus]`.
The consequence for the ladder's "5–10y investment-lag cycle" framing: **shale shortened the
supply leg's response time from years to quarters, while OPEC+'s group politics — the compliance
game, the market-share-versus-price choice each meeting restates — still set the floor** that
shortened curve operates against. Post-2014, conventional capacity-lag dynamics (cases 4–5) matter
less at the margin; OPEC+'s own quota discipline matters correspondingly more, against a marginal
supplier that answers within a fiscal quarter, not a decade.

### B.8 April 2020 — negative WTI and the record cut

The **20 April 2020** negative-WTI print — the May contract falling **$55.90 intraday** to close
at **−$37.62/barrel**, Brent near **$26** — is fully documented in the commodity monograph's case
6 as a microstructure accident (Cushing storage near physical capacity amid pandemic demand
destruction), cited here only for the regime response it triggered: OPEC+, after days of
negotiation (Mexico's resistance briefly holding up the deal until the US absorbed part of its
allotment), finalized a **record 9.7 million b/d cut** — more than twice the 4.2 million-b/d
reduction the cartel managed through 2008 — effective **1 May 2020**, tapering to **7.7 million
b/d (Jul–Dec 2020)** and **5.8 million b/d (Jan 2021–Apr 2022)** **[Verified]**. It is the
chronology's largest-ever coordinated supply response, and its scale — ~10% of world supply
withdrawn inside days — shows how much more supply OPEC+'s wider post-2016 coalition could
coordinate than the pre-2016 OPEC-only cartel ever commanded.

### B.9 2022 — the invasion spike, SPR releases, and the price-cap regime

Russia's invasion of Ukraine on **24 February 2022** produced the record's most compound recent
episode. Brent hit an **intraday high of $139.13/barrel on 7 March 2022** — highest since the July
2008 peak — on fears of a full Western embargo of Russian crude **[Verified]**. The US responded
with the **largest Strategic Petroleum Reserve release in its history**: Biden's **31 March 2022**
announcement committed **1 million b/d for 180 days (180 million barrels total)**, sold at an
average **~$96/barrel**, drawing the SPR to its **lowest level in roughly 40 years [Verified]**. The
regime's most durable innovation followed at year-end: the **G7, EU and Australia agreed a
$60/barrel price cap on Russian seaborne crude, set 3 December 2022**, enforced not by a purchase
ban but by **barring Western shipping/insurance/reinsurance firms from handling cargo priced above
the cap** (kept ~5% below market **[Verified]**). This is a genuinely new instrument — a
**consumer-coalition price control operating through the insurance/shipping market, not the oil
market itself** — whose India-specific consequences (India sits outside the cap coalition and
became one of the largest buyers of discounted, cap-adjacent Russian crude) are Part C.4's subject.

### B.10 The 2023–26 voluntary-cut era, and the 2026 Hormuz-tension spike

OPEC+'s current regime is a multi-year unwind of the pandemic-era cuts, layered with additional
voluntary reductions and then their own reversal. Producers began **voluntary output cuts from
April 2023**; **November 2023** brought **additional voluntary cuts of roughly 2.2 million b/d**
for Q1 2024, subsequently extended; **December 2024** pushed the full unwind out to 2026; the group
then **accelerated the reversal**, agreeing on **3 August 2025** to raise output by a further
**547,000 b/d for September**, completing the full unwind of the 2.2m-b/d cuts **[Verified]**.
Brent averaged roughly **$85/barrel (April 2023)** against **~$74/barrel (December 2024)** —
supply outrunning demand even with the cuts formally in place — and an **August 2026** OPEC+
decision moved toward rolling back the remaining voluntary tranche entirely by September 2026
`[VERIFY current — a live, fast-moving sequence, per Forbes/OilPrice.com]`. **2026 price forecasts
diverge sharply by vintage** — pre-disruption estimates clustered near **$57/barrel** `[VERIFY:
EIA/ING-linked, a dated snapshot]`, while the World Bank's own **mid-2026 revision** (commodity
monograph case 7, cited not re-derived) moved the other way: commodity prices **rising 16% in
2026** (first annual rise since 2022), Brent averaging **~$86/barrel**, on **Middle East supply
disruptions in early 2026**. That disruption is the global-cycle monograph's own live test case
(cross-ref, not re-derived): **Brent above $100/barrel on US-Iran tensions** was one of three
concurrent forces behind the **May-2026 INR record low of ₹96.6–96.8/$**
(`docs/cycles/22-global-cycle.md` A.3iv). The honest synthesis: OPEC+ spent 2023–25 managing a
supply-glut unwind against soft demand, and a Hormuz-adjacent shock re-injected genuine supply-
shock uncertainty mid-unwind — exactly the regime-flip a clock-based "oil cycle" reading has no
mechanism to anticipate, and exactly what the shock-type decomposition (Part A) is built to
classify the moment it lands.

---

## C. India's transfer, by shock type (the entry's own table)

### C.1 The organizing distinction, and the desk's own test of it

Every episode in Part B lands on India as an import bill, never as a price India itself sets — the
commodity monograph's own framing for the broader supercycle applies with even more force to oil
specifically, since crude is the single largest item in that bill. The organizing claim Part A.5
already stated in the abstract, this section tests against the actual historical record, episode
by episode, split by Kilian's own supply/demand taxonomy.

**The desk's own OL1 trial, cited with its actual numbers and its honest limits.** Rather than
merely assert the shock-type asymmetry, this program pre-registered and ran a direct test on the
free data this session's vault holds (`research/register/trial-ledger.md`, Atlas 2.12; full result
at `research/cycles/oil-fold/oil-RESULTS.md`). Construction: among all annual-real-oil-return-
greater-than-+10% years, 1994–2015 (n=11), each year is flavored **demand** or **supply** by a
deliberately crude proxy — the sign of the pooled JST-panel world-equity mean real return that year
— against India's own annual market-factor return (`iima` monthly factors, compounded to annual).
Pre-registered bar: demand-flavored oil-up years should show a mean India return **at least 10pp
less damaging** than supply-flavored years. Result: **8 demand-flavored years averaging +38.1%
India return; 3 supply-flavored years averaging −43.1%; a gap of +81.2pp — PASS**, by a wide margin.
The honest limits are exactly what the pre-registration declared: n=11 is tiny (three supply-
flavored data points — 2000, 2008, 2011, not a distribution), and the world-equity-sign proxy
**conflates oil-demand-flavor with global risk appetite generally** — a year reads "supply"
whenever world equities were down, which coincides with genuine supply shocks but just as readily
with a broad risk-off year whose oil move had little to do with supply. `research/cycles/
oil-fold/partDH-verdict-routing.md` states the identification ladder precisely: OL1's equity-sign
proxy is the weakest rung; a real Kilian-index pull (design item **OL-D1**, runsheet-gated) is the
next rung; full Kilian-Murphy/Baumeister-Hamilton VAR replication is the literature-grade top rung
this desk does not attempt itself. The print is real, direction-consistent, bar-clearing — and
capped exactly where a proxy this simple should be capped.

### C.2 Supply-shock episodes: 1973–74, 1979–80, 1990, 2022

Each episode (1973–74 and 1979–80 in the commodity monograph's case 4; 1990 at B.4; 2022 at B.9 and
commodity case 7) shares the same India signature: **no offsetting growth or export channel**,
since the shock removes barrels from the world market without expanding demand for anything India
sells. **1973–74 and 1979–80** predate liberalization and float-rate India; transmission ran almost
entirely through the administered-price fiscal channel (§C.5) and the balance-of-payments channel
directly — the 1990–91 Gulf-adjacent shock is on record as a direct contributor to India's own 1991
BoP crisis (`research/dossiers/08-india-mid-cycles.md` §I11, cited not re-derived). **2022** is the
fullest modern, deregulated-price instance: India's crude import bill **more than doubled, from
$63.38bn to $130.22bn across the first ten months of FY2022**, ~85% of demand import-met; WPI ran
**double digits for twelve consecutive months from April 2021**, peaking at **16.63% YoY in May
2022**; CAD widened toward **~3% of GDP (~$105bn) in FY2022** before narrowing to **~2% in FY2023**
`[VERIFY: final prints not fully reconciled this session]` — all verified in the commodity
monograph's §B3.4, cited not re-derived. Equity behavior matches OL1's own 2008 and 2011
observations (−61.7% and −31.0% India market-factor return) — the supply-flavored years in OL1's
own table are, not coincidentally, years the historical record independently marks as stress
episodes.

### C.3 Demand-shock episodes: 2004–08 ride-up, 2010–11, 2021 reopening

**2004–08.** The China-led global supercycle's boom leg (commodity monograph case 5, cross-ref, not
re-derived) coincided almost exactly with India's own strongest sustained growth run and its own
credit/capex boom — a demand-flavored oil rise from ~$25 to Brent's July-2008 peak of $147.30/
barrel, arriving alongside a global expansion that was, for India, a growth tailwind, not merely an
import-bill headwind. The CAD evidence supports the self-hedge story more than it undermines it:
India's *trade* deficit widened sharply (over **5.5% of GDP by 2004–05** on one IMF staff
assessment `[VERIFY: year-by-year CAD prints 2005-06 through 2007-08 not fully reconciled this
session]`), yet the *current account* deficit — netting in strong services exports and remittances
— stayed comparably contained through the boom itself; the record **4.8%-of-GDP CAD** (commodity
monograph §B3.2) arrived only in **FY2012–13**, after growth had downshifted while the accumulated
import-bill legacy hadn't fallen proportionally — a timing-mismatch lesson as much as a magnitude
one. The Sensex's own record is directionally unambiguous: cumulative gains of **13.08% (2004),
26.87% (2005), 33.16% (2006), 36.53% (2007)** `[Verified]` — one of its strongest sustained bull
runs, running through the years Brent roughly quadrupled.

**2010–11.** The post-GFC recovery's demand-driven oil rise arrived alongside India's own
V-shaped rebound and — the cleanest self-hedge data point in this record — **export growth of
37.4% outrunning import growth of 26.6%** in FY2010–11, so that even as the trade balance widened
in absolute terms, the **CAD actually moderated, from 2.8% of GDP (FY2009–10) to 2.6% ($44.3bn,
FY2010–11)** `[Verified]` — the self-hedge mechanism operating in real time. The equity read is more
mixed: 2011 itself was a poor year for Indian equities (a widely-cited **~−24.6% Nifty decline**
`[VERIFY: single-source]`), but that weakness is documented elsewhere in this program as a
domestically-driven inflation/rate-hike and Europe-crisis story, not an oil-specific one — the same
caution the dollar-fold monograph states: not every stress episode inside a global window is
*caused* by the headline factor everyone is watching (`research/cycles/dollar-fold/partAB-theory-
cases.md` §B.5).

**2021 reopening.** The pandemic-reopening spike through 2021 — predating, and mechanistically
distinct from, the 2022 war shock that followed it (commodity monograph case 7) — arrived alongside
one of the strongest recent years for Indian equities: Nifty 50 gained **+24.12% in 2021**
`[Verified]`, energy prices rising alongside a broad earnings/risk-appetite recovery rather than the
CAD/INR stress 2022 produced the following year — the cleanest illustration of how quickly oil can
flip from a self-hedging demand signal to a supply-shock headwind within twelve months, exactly the
transition a clock-based "oil cycle" framing has no mechanism to anticipate.

### C.4 The 2014–16 windfall — the reverse experiment, and who actually captured it

The June-2014-to-January-2016 collapse (Brent $112→$31, commodity monograph case 6) is this
record's cleanest **reverse experiment**: a supply-driven fall should, on the decomposition's own
logic, be an almost pure gift for an 85%+ importer with no offsetting demand-side loss — and the
Indian data bear this out almost too cleanly. **WPI turned outright negative**, **−2.33% YoY (March
2015)** and **−2.36% (May 2015)**, fuel-specific WPI **−10.41% (May 2015)** — all verified in the
commodity monograph's §B3.3, cited not re-derived. The more instructive finding is **who captured
the windfall**: rather than pass the collapse through, government **raised excise duty on petrol
and diesel ten times between November 2014 and January 2016** — cumulative **₹11.77/litre (petrol)**
and **₹13.47/litre (diesel)** against pre-hike baselines of **₹9.48/₹3.56** — excise collections
**more than doubling, ₹99,000cr (FY15) → ₹2,42,000cr (FY17)**, retail pump prices held roughly flat
by design (commodity monograph §B3.3, cited not re-derived). The equity mirror: OMC stocks
(IOCL/BPCL/HPCL), margins **structurally inverse to crude**, benefited directly even as households
captured comparatively little, while Nifty Metal — the *global* supercycle's own sector mirror, not
the oil windfall's — gained **+48.4% in 2016** (commodity monograph §B3.6, cited not re-derived).
The lesson: the decomposition held on this down-leg exactly as on §C.2's up-leg episodes — the only
genuine surprise was fiscal, not macro: government, not consumer or equity market, captured the
windfall.

### C.5 The administered-price wedge, and the post-2022 discounted-Russian-crude regime shift

The mechanisms standing between the world oil price and what an Indian consumer or firm actually
pays are already documented in full in the commodity monograph's §B3.3/§B3.5 (OMC under-recoveries
peaking at **₹1,38,541 crore in FY2011–12**, ~40% borne by upstream ONGC/OIL/GAIL for over 13
years; the **80:20 gold-import rule** of August 2013 as the CAD-side parallel; diesel deregulation
from October 2014 and the **PAHAL** LPG direct-benefit transfer from November 2014) and are cited
here, not re-derived, as the reason WPI (commodity-heavy) has historically moved on oil shocks well
before, and more sharply than, CPI (filtered by these same administered mechanisms).
`docs/cycles/21-fiscal-cycle.md`'s own subsidy-accounting machinery (the FCI food-subsidy
off-budget chain) documents the general discipline, cross-referenced for that alone, not for
oil-specific mechanics the commodity monograph already carries in more directly applicable detail.

**What this chapter adds, genuinely new:** the **post-2022 discounted-Russian-crude regime** —
flagged as an open question by D08 (`research/dossiers/08-india-mid-cycles.md` §I11) — materially
changes how a *supply*-flavored shock now passes through relative to every earlier episode here.
**Pre-invasion, Russian crude was ~2% of India's oil imports**; the **G7/EU price-cap regime (§B.9)**
— banning Western insurance/shipping above $60/barrel rather than banning the trade — created a
structural discount Indian refiners captured at scale: Russia's import share rose to **~34–36% by
FY2024–FY2026**, India's single largest crude supplier `[Verified via multiple 2026 press sources]`,
at a discount that has itself moved considerably — **one measure: ~USD 2.5/barrel (FY2025) widening
to ~USD 4.7/barrel (FY2026 so far); a narrower monthly reading: $77.7/tonne (April 2026) narrowing
to $10.6/tonne (June 2026)** as enforcement tightened `[VERIFY: the two readings use different bases
and are not reconciled to one series]`. The implication D08 anticipated: **the same Brent-terms
supply shock no longer maps to the same India import-bill impact it did before 2022**, since a
variable share of India's barrels now clears at a sanctions-state-dependent discount — an open
re-estimation item this chapter names rather than resolves, routed to the routing file's own
**OL-D1** design item, not settled here with the free data currently vaulted.

### C.6 The shock-type table

| Episode | Shock type (Kilian) | WPI/CPI passthrough | CAD/INR | Equity (India) | Policy-era context |
|---|---|---|---|---|---|
| 1973–74 embargo | Supply | Sharp, WPI-led (pre-CPI-era data thin) | BoP-stress channel (pre-float regime) | `[VERIFY: pre-1991 India equity data not independently reconstructed this session]` | Fully administered retail prices; fiscal absorption, not market pass-through |
| 1979–80 revolution | Supply | Sharp WPI rise, feeding the era's own high-inflation regime | BoP-stress channel (pre-float regime) | `[VERIFY]` | Fully administered; same regime as above |
| 1990 Gulf spike | Supply | Contributory to the 1991 BoP crisis (D08 §I11) | Direct BoP-crisis contributor | `[VERIFY: pre-liberalization equity data]` | Fully administered; resolved by 1991 reforms that followed |
| 2004–08 ride-up | Demand | WPI/CPI rose, but alongside strong nominal growth | Trade deficit widened (>5.5% GDP, 2004-05 `[VERIFY]`); CAD stayed comparatively contained through the boom itself; the 4.8%-GDP blowout arrived later (FY2012–13), post-boom | Sensex +13.1%/+26.9%/+33.2%/+36.5% (2004–07) — one of the strongest bull runs on record | Administered era (pre-2014); subsidy burden building but not yet the binding constraint |
| 2010–11 recovery | Demand | WPI elevated but export-financed | CAD **moderated** 2.8%→2.6% GDP on 37.4% export growth vs 26.6% import growth — the clearest self-hedge data point in the record | 2011 weak (~−24.6% `[VERIFY]`) but domestically (inflation/rate-hike/Europe) driven, not oil-specific | Late administered era; OMC under-recoveries still peaking (FY2012) |
| 2014–16 collapse (reverse) | Supply (down-leg) | WPI negative (−2.33%/−2.36% YoY, 2015) | Immediate CAD relief; government captured most of the gain via excise hikes | OMCs gained (inverse-crude); Nifty Metal +48.4% (2016) as the broader complex found its base | Regime TRANSITION: diesel deregulated Oct 2014; PAHAL DBT Nov 2014; excise capture, not consumer pass-through |
| 2021 reopening | Demand | Rising but alongside a broad earnings/risk-appetite recovery | Contained; the following year's (2022) shock is the supply-driven break, not this one | Nifty +24.12% (2021) | Deregulated era; no administered buffer, full pass-through by design |
| 2022 invasion spike | Supply | WPI double-digit 12 straight months, peak 16.63% (May 2022) | Import bill more than doubled ($63.4bn→$130.2bn, 10mo FY22); CAD ~3% GDP FY22 `[VERIFY exact prints]` | Sharp near-term stress (global-cycle monograph's own May-2026 analogue episode shows the pattern repeating) | Deregulated era; price-cap/discounted-Russian-crude regime begins, a genuinely new wedge (§C.5) |

---

## D. The fold, stated precisely

**Atlas row 2.12 contributes no new ladder seat.** `config/ladder.yaml`'s `L9_global_financial_
cycle` role line already states the commitment this chapter exists to teach, not invent: "includes
Kilian-decomposed oil (never raw price level)." Nothing in Parts A–C argues for a separate `L_oil`
entry, budget line, or influence cap — the decomposed oil signal remains one of the five free
series L9's own construction consumes (`docs/cycles/22-global-cycle.md` A.4 already lists "Kilian
oil decomposition" as one of L9's named mechanisms, its own honest gap flagged — "an India-specific
pass-through re-estimate post the 2022 discounted-Russian-crude regime shift... already flagged as
open by D08" — a gap §C.5 narrows without closing). Granting 2.12 its own seat would score a series
L9 already reads under a second name and budget — the duplication Atlas §14's principle refuses, the
same discipline the dollar-fold monograph applies to atlas rows 2.9/2.10 and this chapter applies
here to 2.12 by the identical logic.

**The supercycle and capex-lag content is, and stays, the commodity monograph's.** Every mechanism
cited here for the multi-year capacity-investment lag — the 1970s–1990s arc, the China-era capex
response, the shale-era break — is drawn from `docs/cycles/14-commodity-supercycle.md` and
`research/cycles/commodity-deep/partB-cases.md` (cases 4, 5, 6) and never re-derived; this
chapter's own contribution sits one level up, in the *identification* of which shock type is
currently live and the *regime* history of who controls the supply curve's political floor.

**The supply-confirm machinery is runsheet-gated, not desk-run.** A live pull of the Kilian global-
real-activity index (FRED `IGREA`, Part A.4) to re-run OL1 with a genuine structural-shock
classification, replacing §C.1's crude world-equity-sign proxy, is
`research/cycles/oil-fold/partDH-verdict-routing.md`'s own design item **OL-D1** — registered
there, not attempted here; the desk's expectation is the demand/supply asymmetry **survives but
shrinks** once a genuine global-factor control replaces the proxy. The 2014–16 windfall's reverse-
experiment framing (§C.4) is that file's design item **OL-D2** — documented qualitatively here,
its quantified test left to that item.

**"The oil cycle" retires as a standalone label, with the print attached.** What survives, carrying
its own evidence: (i) the Kilian decomposition, taught at the depth `config/ladder.yaml`'s role
line always presupposed, maturing rather than weakening across three rounds of critique; (ii) the
OPEC/OPEC+/shale **regime** chronology — eight-plus dated turns, 1973–2026, the 2014 shale break as
the one genuine structural change to the supply curve's short end — read as context, never a
clock; (iii) OL1's own real, bar-clearing, direction-consistent print, honestly capped. The
**shock-type table (§C.6)** is this entry's own briefing exhibit precisely because it survives the
fold: a Stage-2 red-team question the table equips a briefing to answer, carrying zero independent
allocation authority — the same status the dollar-fold monograph grants the dollar smile, for the
identical reason: an interpretive frame is not a forecasting signal.

### Synthesis

| Claim | Evidence | Where it lives | Verdict |
|---|---|---|---|
| Raw oil price cannot be trusted as a signal; the decomposition can | Kilian (2009) AER; Kilian-Murphy (2012, 2014); Baumeister-Hamilton (2019) — three rounds of critique, the core distinction surviving each | `config/ladder.yaml` L9 role line ("never raw price level") | Design constraint, frozen; taught at depth here for the first time |
| The global real activity index is a genuinely free, institutionally durable input | Dallas Fed IGREA / FRED `IGREA`; the 2018–19 Hamilton critique traced to, and resolved by, a coding-error correction | L9's own indicator list (`ladder.yaml`: "...Kilian index") | D08's `[VERIFY: URL/maintenance]` flag resolved — institutionally hosted, not a personal webpage |
| Oil's "cycle" is OPEC/shale regime history, not a clock | Eight-plus dated regime turns, 1973–2026; the atlas's own five-for-five fixed-period failure prior (`docs/cycles/19-kitchin-juglar.md`) applies by the same logic | This chapter, Part B; commodity monograph cases 4–7 for the capacity-lag mechanism specifically | Regime historiography, zero timing authority — never a seat |
| Shale shortened the supply leg; OPEC+ still sets the floor | Elasticity rose to 1.1 (significant), 85% of supply impact within 2 years (commodity monograph case 6); 2024 breakevens ~$59–70/bbl | This chapter, §B.7, cross-referencing commodity monograph case 6 (no re-derivation) | Structural break in the supply curve's short end; OPEC+ politics still govern the medium-term floor |
| India's oil transfer flips sign by shock type, not by episode size | OL1: +38.1% (demand-flavored) vs −43.1% (supply-flavored), +81.2pp gap, n=11, PASS — capped by a crude proxy, stated honestly | `research/cycles/oil-fold/oil-RESULTS.md`; §C.1–C.4 above; the shock-type table (§C.6) | Direction confirmed in-house; magnitude/identification capped pending OL-D1 |
| The 2014–16 collapse is the clean reverse experiment | WPI −2.33%/−2.36% YoY (2015); government captured the windfall via ten excise hikes, ₹99,000cr→₹2,42,000cr collections | Commodity monograph §B3.3 (cross-ref); this chapter §C.4 (new framing as the reverse experiment) | Confirmed: a supply-driven fall is close to a pure gift, mostly fiscal-captured, not consumer-captured |
| The post-2022 discounted-Russian-crude regime changes the supply-shock pass-through itself | Russia's import share ~2%→~34–36%; discount readings diverge by measure (`[VERIFY]`) | This chapter §C.5 (new content; not covered elsewhere in this program) | Open re-estimation item, routed to design item OL-D1 — not resolved by this teaching chapter |
| 2.12 earns no independent ladder seat | Atlas §14's de-duplication principle; L9's own construction already consumes the decomposed series | `docs/cycles/22-global-cycle.md` A.4; `research/cycles/oil-fold/partDH-verdict-routing.md` (routing/design items) | Folded, with the shock-type table retained as the Stage-2 briefing exhibit |

---

## References

Kilian, L. (2009). "Not All Oil Price Shocks Are Alike: Disentangling Demand and Supply Shocks in
the Crude Oil Market." *American Economic Review* 99(3): 1053–69. · Hamilton, J. D. (1983). "Oil
and the Macroeconomy since World War II." *Journal of Political Economy* 91(2): 228–48. · Kilian,
L. & Murphy, D. P. (2012). "Why Agnostic Sign Restrictions Are Not Enough: Understanding the
Dynamics of Oil Market VAR Models." *Journal of the European Economic Association* 10(5): 1166–88.
· Kilian, L. & Murphy, D. P. (2014). "The Role of Inventories and Speculative Trading in the Global
Market for Crude Oil." *Journal of Applied Econometrics* 29(3): 454–78. · Baumeister, C. &
Hamilton, J. D. (2019). "Structural Interpretation of Vector Autoregressions with Incomplete
Identification: Revisiting the Role of Oil Supply and Demand Shocks." *American Economic Review*
109(5): 1873–1910. · Hamilton, J. D. (2018/2019). "Measuring Global Economic Activity." NBER
Working Paper 25778. · Kilian, L. & Zhou, X. (2018). "Modeling Fluctuations in the Global Demand
for Commodities." · Kilian, L. (2019). "Measuring Global Real Economic Activity: Do Recent
Critiques Hold Up to Scrutiny?" *Economics Letters* 178: 106–10. · Federal Reserve Bank of Dallas,
"Index of Global Real Economic Activity" (IGREA), `dallasfed.org/research/igrea`; FRED series
`IGREA`. · OPEC Vienna meeting minutes and press coverage, 27 November 2014 (CNBC, Fortune,
Business Standard); Ali al-Naimi memoir excerpts (World Oil, The National, Al Arabiya). · OPEC+
"Declaration of Cooperation," Vienna, 10 December 2016 (Marketplace, CSIS, Gulf News). · Federal
Reserve History, "Oil Shock of 1973–74"; EH.net and Econlib retrospectives on the 1990 oil price
shock; Wikipedia "1990 oil price shock" (cross-checked against multiple contemporary price
reports). · The Hague OPEC/non-OPEC agreement, 23 March 1999 (RFE/RL, PBS NewsHour, Oxford
Institute for Energy Studies). · CNBC, CNN, NPR, Al Jazeera reporting on the OPEC+ 12 April 2020
record production-cut agreement. · CNBC, Al Jazeera reporting on Brent's 7 March 2022 intraday
peak; U.S. Department of Energy releases on the March 2022 SPR announcement; Al Jazeera, U.S.
Treasury, and sanctions-tracking press on the December 2022 G7/EU/Australia Russian-oil price cap.
· OPEC press releases and Enerdata/Sprague Energy/OilPrice.com/Forbes coverage of the 2023–2026
voluntary-cut sequence and its 2025–26 unwind. · The Print, Tribune India, ANI, and trade-data
aggregator reporting (2026) on India's Russian-crude import share and discount trends. ·
`docs/CYCLE_ATLAS.md` row 2.12 (this entry) and rows 1.3/2.11 (H53/H54, cross-referenced) ·
`config/ladder.yaml` (`L9_global_financial_cycle`) · `docs/cycles/14-commodity-supercycle.md` and
`research/cycles/commodity-deep/partB-cases.md` (cases 4–7, cross-referenced throughout, never
re-derived) · `docs/cycles/22-global-cycle.md` and `research/cycles/globalcycle-deep/` (the L9
seat's own construction and the May-2026 live episode) · `docs/cycles/21-fiscal-cycle.md` (general
subsidy-accounting discipline) · `research/dossiers/08-india-mid-cycles.md` (D08, §F13/I11) ·
`research/register/trial-ledger.md` (OL1) · `research/cycles/oil-fold/oil-RESULTS.md` (OL1's own
numbers) · `research/cycles/oil-fold/partDH-verdict-routing.md` (this entry's routing and design
items) · `research/cycles/dollar-fold/partAB-theory-cases.md` (the style bar this chapter follows)
· `research/CONTRACT.md` (evidence tiers, decay-survival standard, free-data rule).

---

**Word count: 7,995 words total** (7,035 words in the body, Part A through the Synthesis table;
the remainder is the title/verdict/headline front matter and the References section).
