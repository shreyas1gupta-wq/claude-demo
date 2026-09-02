# Factor Rotation and Crowding — Paired Monograph (Atlas 3.3 FOLD + 3.4 CANDIDATE)

**Version 1.0 · 2026-09-02 · Ionic quant desk (principal: gaurav@ionic.in) · governed by research/CONTRACT.md**

**Verdict up front:** 3.3 factor rotation → **FOLD** ("rotation" retired: the value-momentum
complementarity is harvested STATICALLY by the 50/50 blend — the desk's own −0.37/−0.41
correlations and Sharpe-doubling result — and the regime conditioning already IS L8's own
rule; timing the leadership would be timing the timers). 3.4 crowding/unwind → **CANDIDATE
instrumented** (Tier-C reduce-only monitors on momentum/low-vol/quality) with its design
constraint MEASURED before any AUM data exists.

**Headline results (CR1a/CR1b/CR2, pre-registered):**
- **CR1a FAIL — another import dies on transfer:** India's WML is NOT unconditionally
  negatively skewed (+0.05; value is the positive-skew factor at +0.60). Momentum's danger is
  REGIME-LOCAL — the seated CONDITIONAL crash_guard is vindicated by the fail.
- **CR1b PASS — the exit's depth is real:** WML's worst month −4.1σ vs SMB −2.9σ / HML −3.4σ.
- **CR2 — the named mid-2025 unwind is INVISIBLE in India's monthly WML** (zero 2025 months
  ≤ −2σ) even though the chapter's search pass corroborates it externally (Goldman prime
  −4.2% Jun-Jul 2025; the Jan-2026 echo): unwinds live at implementation/intramonth
  granularity — so the monitor's legs are AUM growth-rates + factor-valuation percentiles +
  comomentum (CR-D1..D3), never monthly factor returns.

**India's crowding record:** smart-beta AUM ₹290cr → ₹46,000cr, >70 factor products by
Aug 2025 — the accumulation the monitors will count.

**Assembled from:** partAB-theory-cases.md · crowding-RESULTS.md · partDH-verdict-routing.md.

---

# PART A + B + C — Rotation's strongest form and the fold; crowding's mechanism, episodes, and the candidate

# Factor Rotation and Crowding — Theory and the Cases, Argued in Full

Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in) · v1.0 · 2026-09-02

Parts A, B & C · Atlas entries **3.3** (Factor-rotation cycles, `docs/CYCLE_ATLAS.md` line 108, Band
3 — intra-cycle states: "value↔momentum leadership tied to rates/credit regimes; the conditioning
already lives in L8's rules — inside L8") and **3.4** (Crowding/unwind cycles, line 109: "episodic
(mid-2025 quant unwind); copycat capital accumulates in visible factors until a shock forces
synchronized exit; AUM growth-rate is the observable... REGIME (reduce-only) monitors on
momentum/low-vol/quality (post-audit addition)... Tier C"). A paired monograph because the atlas
pairs them, and for the same structural reason the sibling Kitchin/Juglar monograph
(`research/cycles/kitchin-juglar/partAB-theory-cases.md`) pairs a dead clock with a live mechanism:
two entries sharing one evidentiary root — the value-momentum complementarity and its crowding —
reaching opposite budget verdicts. **3.3 is a real diversification fact wearing a fake timing
label**: the negative correlation between value and momentum is genuine, large, and already
harvested by construction; "rotation" as a *separate, tradable regime call* is not a thing this
desk's own machinery, or the honest tactical-timing literature, supports adding on top. **3.4 is
the opposite shape** — a real, alive, currently-unbudgeted mechanism with a design gap the desk's
own decay-audit found (`research/register/decay-redteam.md` §3) and the atlas then closed with a
named, Tier-C, reduce-only candidate. Governing discipline throughout: CONTRACT §5's survival-
argument test (why does a signal survive being known — categories (i)–(iv)), CONTRACT §4's tier
system (Tier C may only reduce risk, never add), and the same steelman-first, keep-only-the-earned-
residue method this program's other paired monographs already establish as house style.

**Companion evidence, never recomputed here.** `docs/cycles/04-value-quality.md` Part A.8 (the
Asness-Moskowitz-Pedersen value-momentum correlation theory and combination arithmetic) and Part
B-RESULTS entries V2–V3 (the desk's own India −0.37 / US −0.41 correlation prints and the 50/50
Sharpe result); `docs/cycles/03-momentum-trend.md` Part A.7–A.8 (the momentum survival argument,
the Lou-Polk comomentum construction, the Daniel-Moskowitz crash mechanism) and Part B-RESULTS
entries M2–M4 (India's conditional crash signature and the desk's own crash_guard validation);
`config/ladder.yaml` L3/L8 (the seated constructs this chapter routes both entries into);
`research/register/trial-ledger.md` entries CR1a/CR1b/CR2 (this pairing's own pre-registered trial,
cited in full in Part B, never rerun); `research/cycles/crowding-deep/crowding-RESULTS.md` and
`partDH-verdict-routing.md` (the same trial's raw print and the routing/design-naming this chapter
adopts directly — CR-D1/CR-D2/CR-D3); `research/register/decay-redteam.md` §3 and its risk-register
row #6 (the audit finding that produced entry 3.4's "post-audit addition" tag). Style and
evidentiary density follow `research/cycles/kitchin-juglar/partAB-theory-cases.md`.

---

# PART A + B + C — The rotation evidence in strongest form, why it folds; the crowding mechanism,
# the canonical episodes, the candidate design; the verdict pair

This chapter does the same two-direction work its sibling monographs do, but on a single shared
evidentiary root rather than two independent claims. Part A takes the value-momentum negative
correlation and the "rotation" label built on top of it as seriously as the literature allows,
then shows why the desk's own construction already harvests everything real in it, leaving the
separately-budgeted label with nothing left to buy. Part B takes crowding — the flip side of the
same coin, since a crowded factor is precisely one where copycat capital has stopped behaving like
a diversifying counterparty and started behaving like a single correlated position — through its
mechanism, its canonical episodes, and the desk's own pre-registered trial on India data, arriving
at a genuine, if narrowly scoped, new candidate. Read together: 3.3 dies as a timing construct
because the desk already owns both halves of what would make it valuable; 3.4 lives, barely, as a
Tier-C reduce-only monitor because the desk's own audit found a real gap between what the evidence
says and what the registry actually watches.

---

## A. Factor rotation, and why it folds (entry 3.3)

### A.1 The rotation evidence in its strongest form

**Asness, Moskowitz & Pedersen (2013), "Value and Momentum Everywhere,"** *Journal of Finance*
68(3):929–985 [Verified — cited in full in `docs/cycles/04-value-quality.md` A.8, not re-verified
here] is the strongest empirical form the rotation claim takes anywhere in the literature. Value
and momentum returns correlate *positively* with each other across eight international markets and
asset classes — more strongly, in fact, than either correlates with simple market exposure — yet
*within* any one market they are *negatively* correlated, a genuinely surprising, cross-asset-
replicated fact. The mechanism AMP supply is a difference in horizon and leg composition, not two
independently mispriced anomalies that happen to offset: value is, loosely, long the very names
momentum's own formation window has just punished (deep cheapness typically follows a poor recent
run), while momentum is long the names most recently rewarded — the same reversal-versus-
continuation tension, read at two different horizons, generates negative period-by-period
correlation with no requirement that either factor be redundant or mispriced on its own.

**The desk's own numbers, already established, cited not recomputed.** `docs/cycles/
04-value-quality.md` Part B-RESULTS entry **V2** finds the AMP claim holds on both panels the desk
has vaulted: India correlation **−0.37**, US **−0.41** — "AMP's diversification claim confirmed on
both panels by us." Entry **V3** takes the next step, the combination arithmetic AMP's own paper
formalizes (`SR_p² = (SR₁²+SR₂²−2ρ·SR₁·SR₂)/(1−ρ²)`, already derived in full in A.8's formal
structure): a static 50/50 blend of value and momentum **beats both legs on both panels** — India
Sharpe 0.86 versus 0.42 (value alone) / 0.55 (momentum alone); US 0.72 versus 0.33/0.45. This is,
in the monograph's own words, "the sturdiest cross-sleeve fact we hold." It is worth stating
precisely what this arithmetic *is*: at AMP's approximate ρ≈−0.5 with equal single-leg Sharpes, the
combination's Sharpe is *exactly double* either leg's alone — a mechanical consequence of the
correlation's sign, requiring no forecast of *which* leg will lead next period, no regime read, no
timing signal of any kind. The diversification benefit is captured in full by simply **holding
both, always, in fixed proportion** — which is the single most important fact this section has to
establish before asking whether a separate rotation signal could improve on it.

### A.2 Regime-linked leadership — the literature, verified and honestly graded

Atlas 3.3 names "value↔momentum leadership tied to rates/credit regimes" as the mechanism behind a
rotation cycle. The most developed, citable version of a rates-conditioned leadership story is the
**duration/discount-rate view** — Lettau & Wachter (2007, 2011), already cited in full in
`docs/cycles/04-value-quality.md` A.3 [Verified]: value firms are modeled as claims mostly on
near-term cash flows (short equity duration), growth firms on cash flows arriving far in the
future (long equity duration); a distant cash flow's present value is more sensitive to the
discount rate, so growth — and, on this reading, whichever factor happens to be growth-tilted in a
given period, which in practice correlates with recent momentum winners — should be hurt more when
rates rise and helped more when they fall. This is exactly the kind of clean, mechanistic,
rates-regime story that would license a genuine factor-rotation rule *if it held up empirically*.

**It does not, and the desk's own value monograph already says so at length rather than importing
the theory uncritically.** AQR's subsequent empirical work (Asness, drawing on Maloney-Moskowitz,
cited in full at A.3.iii of the value monograph) tests the duration implementation across
specifications and reports the realized value-minus-growth/rate-change correlation at roughly
**0.03 over 40 years and 0.34 over the most recent 10** — weak on average, unstable across
sub-periods, strengthening and weakening with confounds controlled. Asness's own verdict, already
quoted in that monograph: "people say rates have to rise for value to do well; that is absolutely
not true." A theory this unstable cannot license a standalone, fixed rates-conditioned rotation
rule under CONTRACT §6's "no magic numbers" bar — and the value monograph's own conclusion already
states the correct treatment: a rate/credit regressor belongs, at most, as one *candidate* input
inside a pre-registered, purged test alongside others, never a standalone timing trade.

**The broader "regime-dependent factor" literature, one level up.** Two further pieces of the
literature bear on the atlas's "rates/credit regimes" phrasing directly, verified this session.
**Ehsani & Linnainmaa (2022), "Factor Momentum and the Momentum Factor,"** *Journal of Finance*
77(3):1877–1919 [Verified — 2022 Journal of Finance/Dimensional Fund Advisors award paper] find
that **most equity factors are themselves positively autocorrelated**: the average factor earns
roughly **6 basis points** in the month following a losing year and **51 basis points** following a
winning year — and their central claim is that individual-stock momentum is not a distinct risk
factor in its own right so much as a *vehicle that times other factors*, since a portfolio sorted on
past stock returns ends up systematically over- and under-weighting whichever factors have recently
been winning. This is a genuinely important reframing for entry 3.3: it says the mechanism a
bespoke "rotation signal" would try to capture — momentum in which factor is currently leading — is
**already what stock-level momentum itself is measurably doing**, mechanically, inside L3, without
any additional construct. A practitioner-level companion piece, AlphaArchitect's "Are Value, Carry
and Momentum Regime Dependent?" **[VERIFY: exact regime-conditioning magnitudes and construction;
Tier C practitioner source, directional corroboration only]**, reports real-world evidence that
multi-asset value, carry and momentum styles behave differently across market regimes — consistent
in direction with Ehsani-Linnainmaa's academic finding, but, like the duration literature, without
a stable, out-of-sample, cost-net magnitude clean enough to trust as a standalone rule. The honest
state of "rates/credit conditioning of value-momentum leadership," graded fairly: real, directionally
corroborated across several independent literatures, and nowhere close to clean enough to license a
fixed threshold or even a confidently-parameterized quantile rule distinct from what L8 already runs.

**The credit half of the atlas's phrase, stated as an honest gap rather than papered over.** The
duration literature (Lettau-Wachter, above) is a *rates* story; this program's own research base
carries no equivalently developed, dedicated study tying value-versus-momentum leadership
specifically to the *credit*-cycle phase `docs/cycles/01-credit-cycle.md` and **L10_credit_block**
otherwise measure. What exists instead is indirect: the credit cycle's late-boom phase is, almost by
construction, also a phase of narrow credit spreads, easy financing, and — per the value monograph's
own migration finding (Fama-French 2007, `docs/cycles/04-value-quality.md` A.5) — elevated corporate
re-rating activity, all of which plausibly favor whichever factor is currently riding the boom's own
momentum rather than value's contrarian bet on names the boom has left behind; the credit bust that
typically follows plausibly favors the opposite. This is a coherent narrative, not a tested claim —
no purged, India-conditioned regression of value-minus-momentum returns on L10's own credit-gap state
exists in this program's dossier base, and CONTRACT §6's "no magic numbers" rule bars treating the
narrative as license for a rule until one does. **[VERIFY: whether a dedicated academic study links
factor leadership specifically to credit-cycle phase, as distinct from the rates/duration literature
already covered]** — the honest position for now is that "credit regimes" belongs on the same
pre-registered candidate-regressor list A.2's rates discussion already assigns to L8's own future
testing, never a separately-budgeted rotation input in its own right.

### A.3 The tactical factor-timing literature's honest record — the "sin a little" debate

If the mechanism evidence for rotation is real-but-unstable, the direct evidence on *tactically
timing factors* is even more disciplining, and it is a live, named debate in the literature rather
than a settled question this chapter is importing one-sidedly. **Arnott, Beck, Kalesnik & West
(2016), "How Can 'Smart Beta' Go Horribly Wrong?,"** Research Affiliates [Verified] argue the
contrarian case directly: a factor that has recently outperformed tends to get more expensive as
capital chases it, and — precisely because valuations mean-revert — a *rich* factor's forward
return is mechanically depressed regardless of the underlying premium's health; timing factors on
their own relative valuation, in this reading, is not merely defensible but close to necessary,
since ignoring it risks buying factor exposure at exactly its most re-rated, least attractive
moment. **Asness, Chandra, Ilmanen & Israel (2017), "Contrarian Factor Timing is Deceptively
Difficult,"** *Journal of Portfolio Management*, Special Issue 2017 [Verified] is the direct,
named rebuttal — Cliff Asness publicly and pointedly disputing Arnott's own paper — and its
argument matters more for this chapter's purposes than the mere fact of disagreement. Asness's
case: factor timing is likely **harder** than market timing, not easier, because long-short
factor portfolios turn over far more than a simple market exposure does, so any tactical timing
overlay must clear a materially steeper cost and estimation-error hurdle before it can add value
net of the extra turnover it introduces; and — the point most load-bearing for entry 3.3 — **timing
factors using just valuation must contend with contrarian factor timing already being implicitly
present in the value factor itself**, since a value-spread-conditioned value sleeve is, by
construction, already buying more of whichever factor content is currently cheap relative to its
own history. Asness's summary position is to hold a diversified set of factors believed in for the
long term rather than tactically time them — but, and this is the debate's honest resolution point
rather than a total dismissal of Arnott's side, AQR's own practice does not refuse all
valuation-conditioning outright: small, bounded tilts off extreme, own-history valuation spreads
survive Asness's own critique even as large, confident, in-and-out factor rotation bets do not —
the "sin a little, not a lot" reading of the debate, which is the correct frame for grading what
L8's own conditioner already does (a bounded quantile tilt *within* a frozen weight range) against
what a standalone "rotation cycle" construct would be proposing (an unconditioned, separately
authorized regime call).

### A.4 Why the desk's answer is already built — retire the label with the evidence attached

Putting A.1–A.3 together produces a specific, checkable claim: **every piece of evidence that could
license a factor-rotation construct is already consumed, in full, by seated design elements**, and
a separate, additionally-budgeted "rotation signal" would not add content — it would duplicate it.

**The complementarity (A.1) is harvested statically, by design, already.** `docs/DESIGN.md` §6.1
caps momentum's role in the moderate book at a rank-tiebreaker/modifier inside the factor book's
own quarterly turns (≤1/5 of its 200% turnover budget, the Israel-Moskowitz 5× turnover ratio
already governing the size), and §6.2 runs value and quality as the core sleeves. The static
combination — always holding both value's and momentum's content, in a fixed relationship, never a
discrete in/out switch between them — is precisely the construction the SR_p² arithmetic in A.1
says is *already* close to optimal at AMP's measured correlation, with no forecast of which leg
leads next required to capture the benefit. A rotation signal's entire value proposition is
"correctly predict which of value or momentum will lead, and overweight it before it does" — but
the static-blend arithmetic already captures the diversification benefit of the negative
correlation whether or not anyone can forecast the leadership switch, and A.3's evidence says that
forecast is close to the hardest tactical call in the factor literature to get right net of costs.

**The regime linkage (A.2) already lives inside L8's own rules, not beside them.**
`docs/DESIGN.md` §6.2 states the value sleeve's conditioner explicitly: weight rises toward the top
of its frozen 20–35% range when the value spread's own 10-year percentile sits in its top tercile
(Cohen-Polk-Vuolteenaho, already the atlas's own citation for L8), falls toward the bottom in the
bottom tercile, and — the sentence that matters most for this entry — **"tilts toward momentum when
the value spread is bottom-tercile."** This is not an incidental design detail; it is, read
carefully, a value-momentum rotation rule that already exists, already ships, and is already
Stambaugh-corrected and bounded within a frozen range exactly as A.3's "sin a little" resolution
recommends. When value's own edge is most exhausted — cheap-vs-expensive dispersion compressed,
signalling the value composite has little left to distinguish winners from losers by its own
metric — the design tilts toward momentum's modifier role instead. Atlas 3.3's own one-line verdict
("the conditioning already lives in L8's rules") is, on inspection, not a hand-wave but a precise
description of an existing config-level rule.

**A standalone rotation signal would be timing the timers.** Ehsani-Linnainmaa's (A.2) finding that
momentum is not a distinct factor so much as a vehicle for timing *other* factors makes the
redundancy formal rather than merely a design observation: **L3 already is a momentum-timing
device** on the cross-section (the JT2001/HS99 diffusion mechanism, `docs/cycles/03-momentum-
trend.md` A.1–A.2, cited not recomputed), and **L8's spread conditioner already is a value-timing
device** (CPV 2003, Deep Value, `docs/cycles/04-value-quality.md` A.4, cited not recomputed). A
bespoke rotation construct sitting on top of both would be a third, higher-order timing bet built
from two signals that are each, individually, already timing devices for the content a rotation
signal would claim to add — introducing a new, haircut-worthy construct with no distinct mechanism
of its own, no distinct free data source, and — per CONTRACT §5's mandatory survival-argument test
— no answer to "why does this survive being known" beyond what L3 and L8 separately already clear.
A.2's rates/credit-regime literature, even taken at face value, tops out at a 0.03–0.34 correlation
range too unstable to license anything beyond a quantile rule indistinguishable from what L8 already
runs off the value spread's own percentile.

**Verdict, stated once and retired.** "Factor rotation cycles" is not a state variable this program
has failed to notice; it is a label describing content the design already owns under two different,
better-evidenced names. Retire the name, per the atlas's own §14 discipline for exactly this
pattern ("most 'new' cycle families are projections of states Part I already holds, onto a different
surface") — the object it named stays exactly where L3 and L8 already carry it, unmoved, never
double-counted, never re-entering the registry as new alpha under a rotation-shaped label.

---

## B. Crowding and unwinds (entry 3.4, the candidate)

### B.1 The mechanism — crowding as a rational-arbitrageur externality

**Stein, Jeremy C. (2009), "Presidential Address: Sophisticated Investors and Market Efficiency,"**
*Journal of Finance* 64(4):1517–1548 [Verified — delivered to the American Finance Association,
January 2009] supplies the mechanism entry 3.4 needs, and it is a sharper, more damaging story than
"dumb money chases a hot trade." Stein's address considers what happens as a market's trading
becomes increasingly dominated by sophisticated professional capital, and identifies **crowding** as
the specific complication that keeps such a market from becoming more efficient in proportion to
how sophisticated its participants are: an individual arbitrageur, however skilled, **cannot
observe how many of their peers are simultaneously entering the identical trade**. Each manager,
sizing a position rationally given their own information and capital, is doing so blind to the
aggregate position the entire population of similarly-informed managers has quietly built —
individually rational decisions summing to a collectively excessive, synchronized bet that
none of the participants intended or could fully see forming. This reframes crowding, under
CONTRACT §5's four-category survival taxonomy, as principally category **(ii)** — a genuine limit
to arbitrage that persists *even among sophisticated capital*, not merely a behavioral story about
which the smartest money is immune. It is the correct mechanism to cite ahead of any specific
crash episode, because it explains *why* crowding recurs rather than getting arbitraged away the
first time it is understood: the constraint is not ignorance of the mechanism, it is the structural
impossibility of observing one's own crowd in real time.

**The address's sharper, counterintuitive implication.** Stein's own working-through goes further
than "crowding is a friction": he shows that adding *more* sophisticated capital to a market can, in
some configurations, make prices **less** informative rather than more, because sophisticated
traders' positions increasingly reflect what *other* sophisticated traders are inferred to be doing
rather than fresh information about fundamentals — a market can become more crowded with skill
without becoming more efficient, precisely because skill is being spent inferring the crowd rather
than researching the asset. Applied to entry 3.4's own factor context: the more a factor (momentum,
low-vol, quality) is understood, taught, and replicated at scale, the *more* of the capital trading
it is trading the same signal on the same names for the same reasons — the crowding externality
does not require any participant to be wrong about the underlying premium, only for enough of them
to be simultaneously right about it, sized independently, in ignorance of each other's aggregate
position. This is the reason a decay-and-crowding monitor cannot simply be "has this factor
recently underperformed" (a symptom visible only after the unwind has already happened) — the
externality accumulates silently, in capital that is individually well-reasoned, well before any
return-series symptom appears, which is exactly the design implication B.3's candidate below has to
answer.

**Measurement: Lou & Polk's comomentum, already verified and constructed in full elsewhere in this
program, cited not recomputed.** `docs/cycles/03-momentum-trend.md` A.7 already carries the fully
verified citation and construction: **Lou, Dong & Polk, Christopher (2022), "Comomentum: Inferring
Arbitrage Activity from Return Correlations,"** *Review of Financial Studies* 35(7):3272–3302
[Verified]. Comomentum is the **abnormal high-frequency return correlation among the stocks a
momentum strategy would simultaneously trade** — when many arbitrageurs run the same long-
winners/short-losers book at once, their correlated trading itself induces excess co-movement among
winners (and, separately, among losers) beyond what common risk-factor exposure explains. The
momentum monograph's own finding, cited directly: post-formation momentum returns are **strongly,
monotonically decreasing** in comomentum, with the joint years-1-and-2 return differential between
the highest and lowest comomentum quintiles running **roughly −1.07% per month** (t≈−3.35), and
high comomentum separately forecasting higher spread volatility and more negative skewness — an
*ex ante*, contemporaneously observable crowding signature, constructible from price data alone
with **no disclosure lag**. This is the sharpest tool in the literature for this entry, and it is
worth being honest about where it stands relative to the atlas's own named observable: comomentum
has never been built on India data (the momentum monograph's own stated gap, A.9), leaving the
desk, today, on the cruder, disclosure-lagged AUM-growth proxy the atlas row 3.4 actually names.

### B.2 The canonical episodes at depth

**August 2007 — the paradigm case, days-long, invisible in indices.** **Khandani, Amir E. & Lo,
Andrew W. (2007/2011), "What Happened to the Quants in August 2007?: Evidence from Factors and
Transactions Data,"** NBER Working Paper 14465 (2008); published as *Journal of Financial Markets*
14(1):1–46 (2011) [Verified]. During the second week of August 2007, a broad population of
quantitative long/short equity hedge funds suffered unprecedented, near-simultaneous losses while
major equity indices were, by comparison, largely undisturbed — the defining feature of the episode
and the reason it is the canonical illustration of "synchronized unwind, invisible in the index."
Khandani-Lo's central finding is the **unwind hypothesis**: the initial losses trace to the forced
liquidation of one or more large, similarly-constructed equity market-neutral portfolios — sold to
raise cash or cut leverage, for reasons outside the factors themselves (their working hypothesis
points to losses on structured mortgage credit elsewhere in affected firms' books) — whose price
impact on the crowded names inflicted losses on *other* funds running near-identical books, forcing
those funds to deleverage in turn, generating further price impact, further losses, and further
deleveraging: a genuinely self-reinforcing cascade requiring no single trigger beyond one
large, correlated portfolio's exit. Khandani-Lo's own reconstruction dates the mechanics with
unusual precision for an event this diffuse: a **mini-unwind on August 1st, roughly 10:45 a.m. to
11:30 a.m.**, and a **sustained unwind beginning at the open on August 6th and running through
roughly 1:00 p.m.** — intraday-scale, invisible at daily or weekly index resolution, and traced to
positions **long book-to-market, short earnings-momentum** in financial-sector names first — a
value-tilted, momentum-adjacent unwind at its point of origin, with the pre-liquidation drift
already visible through July before the acute event. Khandani-Lo are explicit that the identity of
the triggering fund or desk could not be established from public data — their working hypothesis
points to a large multi-strategy manager or proprietary-trading desk deleveraging its equity
market-neutral book for reasons originating **elsewhere in the same firm** (plausibly losses on
structured mortgage-credit positions, given the calendar), not any deterioration in the equity
factors themselves — a genuinely important structural point for a crowding monitor: the trigger for
a synchronized factor unwind need not be a factor-specific shock at all, only a large-enough
correlated exit from *any* cause, landing on a crowded book. The second half of the episode compounds
the first for a distinct, complementary reason: **market-making risk capital itself withdrew**
starting around August 8th, as intermediaries pulled back from absorbing the very order flow the
unwinding funds were generating, amplifying the price impact of a given quantity of forced selling —
a liquidity-supply-side mechanism layered on top of the liquidity-demand-side deleveraging cascade,
with the combined effect persisting, at reduced intensity, through the remainder of 2007. This is
the case that earns the atlas's own phrase in full: a synchronized long-short unwind that runs for
days (the buildup) to hours (the acute phase) to months (the residual unwind), leaving the broad
market close to unmoved while erasing enormous value from every book running the same crowded
factor exposures simultaneously.

**Momentum crashes (2009) — the desk's own seated defense, cross-referenced, never rebuilt here.**
`docs/cycles/03-momentum-trend.md` A.8 already carries the full Daniel-Moskowitz (2016) mechanism
this chapter cites rather than re-derives: momentum's return distribution is severely negatively
skewed, with the worst episodes clustering in "panic" states and the crash itself landing
*contemporaneously with the market's rebound*, because the loser leg's beta has by then risen to
resemble a high-beta call option on recovery while the winner leg's beta has stayed low. The 2009
episode — momentum losing **more than 73% over three months**, erasing roughly two years of prior
cumulative profit — is precisely the crowding mechanism's return-side signature: capital that
cannot hold a crowded position through its own worst-case realization is forced to exit at the
moment the position is most mispriced against it. The desk's own crash_guard, already validated on
real data (`docs/cycles/03-momentum-trend.md` Part B-RESULTS entry **M4**: guard-ON real US months
average **−2.19%/month** (n=95) versus guard-OFF **+1.81%/month** (n=1069) — "the crash tail lives
in guard-ON, mirrors the synthetic test"), is this entry's seated defense against the momentum-
crash flavor of a crowding-driven unwind. No new construct is proposed here; the point of citing it
is that 3.4's candidate design (B.3 below) must not duplicate what L3's own crash_guard already
handles on the returns side — its job is the crowding *build-up* the crash_guard cannot see coming.

**The mid-2025 quant unwind the atlas names — verified this session, reported at the honest depth
the coverage supports.** Trade-press reporting corroborates and extends the figures the momentum
monograph already carried as Tier-C journalistic evidence (`docs/cycles/03-momentum-trend.md` A.7).
**Goldman Sachs prime-brokerage data** estimated systematic long-short quantitative equity managers
lost approximately **4.2% from June to late July 2025** — a stretch that at one point saw the
cohort fall **2.1% in a single week following a 3.1% decline over the previous five trading days**,
the weakest run since December 2023. Reporting traces the trigger to the **tariff-driven
recessionary scare in early 2025**, which pushed both quantitative and fundamental market-neutral
books to de-gross simultaneously, with capital herding into high-quality, low-beta, large-cap names
(reporting specifically names "Magnificent Seven"-style mega-caps as the crowded destination). The
selloff **spilled into the quality and low-volatility factors** as expectations for monetary easing
subsequently drove investors back toward riskier names — exactly the multi-factor contagion the
atlas's own harvest line targets ("monitors on momentum/low-vol/quality"), not a momentum-only
event — while funds simultaneously **cut momentum exposure** as the reversal intensified, itself the
proximate crowding-unwind action the mechanism (B.1) predicts. A **second drawdown hit in October
2025**. A **third leg opened in the first half of January 2026**: Goldman's own systematic
long-short cohort fell roughly **1% over a critical 10-day stretch — the weakest since October** —
while **UBS estimated US-focused quant funds down approximately 2.8% in the first two weeks of
2026** (the figure the momentum monograph already carried, now independently corroborated by a
named house); trade-press reporting names individual funds' losses over the same window —
**Renaissance Technologies down roughly 4%, Schonfeld's quant operation down roughly 3.9%,
Engineers Gate down roughly 6%**. Goldman's own attribution for the January leg names three
drivers — drawdowns in crowded trades, short exposure to high-beta stocks, and adverse
idiosyncratic moves — and adds an instructive asymmetry worth carrying forward honestly: **momentum
strategies specifically helped limit losses this time**, in contrast to mid-2025, when momentum was
named among the retreating factors. The crowded factor rotates between episodes rather than sitting
still — quality/low-vol absorbed the mid-2025 damage, the short book and idiosyncratic names carried
January 2026's — which is itself evidence for a monitor built at the level of *aggregate crowding*
(AUM, valuation) rather than one hard-wired to any single factor's historical crash signature. All
of the above is reported at the same evidentiary standard the momentum monograph already applies to
this episode: verified as existing, corroborated trade-press and prime-brokerage/UBS-sourced
coverage (Tier C by source), corroborating rather than independently proving the academic crowding
mechanism.

**India's own factor-crowding record.** `research/dossiers/01-momentum-reversal.md` §2 already
carries the load-bearing figure, independently corroborated by this session's own search: India
smart-beta/factor-index AUM grew from **roughly ₹290cr in 2020 to roughly ₹46,000cr by end-2025**,
now **approximately 12% of passive equity AUM**, concentrated in a small number of mechanically-
reconstituted 30–50-name baskets (Nifty200 Momentum 30, Nifty100 Low Volatility 30, Nifty500 Value
50, and siblings); a single reconstitution-day trade on the largest such index runs to an estimated
**₹16,000cr**, an order-of-magnitude capacity anchor the momentum dossier already uses for its own
turnover-bifurcation argument. Independent corroboration this session adds detail: as of **August
2025**, more than **70 India-listed ETFs and index funds** track smart-beta indices, carrying **over
₹30,000cr** in that narrower ETF/index-fund AUM slice specifically, and **BSE launched its own
competing family of smart-beta indices in May 2025** **[VERIFY: BSE's specific index list and
launch AUM]**, mirroring NSE's — direct evidence the mechanically-reconstituted basket capacity risk
the desk's own decay-audit flagged is current, structural, and still growing, not a one-time 2020–
2021 phenomenon that has since leveled off. The momentum-index-fund leg post-2021 is itself the
specific, named product family — **UTI, Kotak, ICICI, Motilal Oswal, HDFC, Baroda BNP, and Tata**
all run Nifty200 Momentum 30 and/or Nifty Midcap150 Momentum 50 vehicles (`research/dossiers/
01-momentum-reversal.md` §7) — that the crowding mechanism (B.1) says cannot each be sized
independently of what its peers are doing, precisely because none of those managers can observe the
others' aggregate position from inside their own book.

**Why this candidate exists at all — the audit provenance, stated plainly.** `research/register/
decay-redteam.md` §3 ("Crowding blind spots") found, on a skeptical second look at the design as it
stood, that the desk had built an AUM-growth crowding trigger for **low-vol only**
(`config/sleeves.yaml` / D02's own decay-ledger row), plus a rising, annually re-estimated haircut
for index inclusion/exclusion — but **momentum, value, and quality, three of the four sleeves
carrying the moderate and aggressive books' actual return, had no analogous monitor**, despite the
design's own cited evidence (D02 §3) naming a live, dated episode — the mid-2025 quant unwind — that
hit quality, low-vol, and momentum **together**. The audit's own risk-register (`docs/masterplan/
D-risk-register.md` row 6, tagged **Major**) records the finding verbatim: "Momentum/value/quality
carry no AUM-crowding trigger despite D02's own cited 2024–25 'quant unwind' naming momentum as a
participant." Atlas entry 3.4's harvest line — "REGIME (reduce-only) monitors on momentum/low-vol/
quality" — carries the parenthetical **"(post-audit addition)"** for exactly this reason: this
design element exists because the audit found a real gap between the desk's own cited evidence and
what its registry actually watched, not because it was independently conceived and then happened to
survive review. Worth stating once, plainly, because it is the clearest example in this program of
its own governance loop working as designed — a red-team pass finding a real hole, and the atlas
closing it with a scoped, Tier-C, reduce-only candidate rather than either ignoring the finding or
over-correcting into a full return-generating construct the evidence does not support.

### B.3 The candidate design per the atlas row

**What data is free, today, with no new pipeline.** Two of the atlas's three named legs cost
nothing beyond what the design already collects. **AMFI category-level AUM** (the mutual-fund
regulator's own monthly disclosure, already a Contract-approved free source) gives a smart-beta/
factor-fund category aggregate; **NSE/BSE index-fund and ETF factsheets** give fund-level AUM for
the named products (Nifty200 Momentum 30 and siblings) at whatever resolution each house discloses.
**Factor-valuation percentiles** need no new construction at all: they are the identical own-history
relative-valuation percentile pipeline `docs/DESIGN.md` §6.2 already runs for the value-spread
conditioner (Cohen-Polk-Vuolteenaho) and the quality valuation kill-switch (the same 2024–25
episode this Part B already cites as its own live corroboration) — extended, mechanically, to a
low-vol and a momentum basket's own valuation history, using bhavcopy and lag-buffered filings the
design already ingests for L8. No admissible signal here requires a data source the desk does not
already have Contract-level approval to use.

**What the desk's CR1 trial tests today — the crash-asymmetry signature on the vaulted factor
library, cited in full from `research/register/trial-ledger.md` entries CR1a/CR1b/CR2 and
`research/cycles/crowding-deep/crowding-RESULTS.md`, never recomputed here.** The trial is
pre-registered on the same vaulted India factor mirror (`iima_monthly_factors.csv`, 1993–2025) the
momentum and value monographs already use, testing whether a crowded factor's return series carries
a measurable ex-post signature of synchronized exit — the returns-only shadow of the mechanism, run
before any AUM or comomentum data is in hand.

- **CR1a (skewness ordering — momentum as the crowded factor par excellence, per Daniel-Moskowitz
  and Lou-Polk):** pre-registered bar, monthly skew(WML) ≤ −0.5 and more negative than both
  skew(SMB) and skew(HML). **Result: WML skew +0.05, SMB +0.04, HML +0.60 — FAIL.** The US
  literature's "momentum is unconditionally negatively skewed" stylized fact does not transplant
  onto India's own 33-year factor library; HML, not WML, is the positively-skewed series here. The
  honest read, recorded in the results file: this is **not a contradiction** of monograph 03's own
  crash finding, because that finding was explicitly **conditional** — the crash zone lives in
  bear-market-then-rally windows specifically (M2's −2.24%/month conditional print), and a
  conditional crash tail can coexist with roughly zero *unconditional* skew when normal-times
  momentum is mildly right-skewed. The refined, India-specific statement: **momentum's danger here
  is regime-local, not a standing distributional feature** — which is precisely what the seated
  crash_guard already implements by construction (a conditional trigger, never a permanent
  de-risking). The fail is a vindication of the existing design, not a disconfirmation of crowding.
- **CR1b (crash concentration — each factor's worst month in its own standardized units):**
  pre-registered bar, WML's worst month ≤ −4σ and more extreme than SMB's and HML's. **Result: WML
  worst −4.1σ (2001-11, −27.6%) versus SMB −2.9σ (2020-03, −14.1%) and HML −3.4σ (2000-01, −19.0%)
  — PASS.** The synchronized-exit signature **is** confirmed — momentum's tail is measurably the
  deepest of India's three canonical factors on a standardized basis, direct, own-data evidence for
  the crash-asymmetry claim this entry needs, even where the third-moment (CR1a) test fails.
- **CR2 (the atlas's own named episode — does the mid-2025 global quant unwind register in India's
  own monthly momentum factor at all?):** measurement, no pass/fail bar, flagging any 2025 monthly
  WML z-score ≤ −2σ. **Result: zero of twelve 2025 months clear −2σ** (the full monthly series:
  −1.1, −0.0, −0.1, −0.6, −1.0, 0.0, 0.1, −0.1, −0.5, 0.1, 0.5, 0.0). **The named episode is
  invisible at monthly academic-factor granularity in India's own data.** This is the single most
  design-relevant finding in the trial, and it is stated as plainly in the results file as it is
  here: either the episode was specific to US/global long-short *implementation* (leverage, gross
  exposure, the specific crowded names) rather than a broad-index-visible India phenomenon, or
  unwind episodes of this kind live at daily-or-finer, intramonth granularity that a monthly
  academic factor return simply cannot resolve — and the honest record does not adjudicate between
  the two, because the design consequence is identical either way: **monthly factor returns cannot
  be the monitor.** The AUM-growth and comomentum legs are structural requirements for detecting
  this class of episode at all, not decorative enhancements to a returns-based trigger that would
  otherwise suffice.

**Design, following `partDH-verdict-routing.md`'s own naming rather than inventing new labels.**
Three legs, each pre-registered with its own acceptance shape before any look at its data:
**CR-D1** — the AMFI smart-beta AUM leg: category AUM growth-**rate** (never a level threshold,
matching D02's existing low-vol trigger template — "reassess sleeve sizing if AUM in [factor]
products grows materially faster than passive-equity AUM overall for 2+ consecutive years"),
extended from low-vol-only to all three of momentum, low-vol, and quality; **CR-D2** — the
comomentum leg (Lou-Polk's own construction, run on the NSE 500 once stock-level daily/intra-month
returns are vaulted; acceptance bars registered only when that data lands, per the two-pass
discipline this program applies everywhere); **CR-D3** — the factor-valuation leg (each factor
basket's own value-spread-style percentile, using machinery that already exists inside L8's family
— registered before any look, no new construction required). All three enter the registry as
**Tier C, reduce-only** monitors per CONTRACT §4 — they may only cut momentum, low-vol, or quality
sleeve weight toward its floor, never add to it — drawing from the same `tierC_overlay` budget
mechanism `config/ladder.yaml` already uses for L1, L13, and L14, rather than requiring a new budget
category.

**Why this is not already L2 or L9, stated once so the de-duplication question is answered rather
than assumed.** The ladder already carries two fast, market-wide risk states that could plausibly be
read as covering this ground: **L2** (`fast_stress`, realized-vol top-decile rank, India-VIX
backwardation, funding-flow stress) and **L9** (`global_financial_cycle`, the dollar/VIX/US-rate
global risk state Rey (2013) and Miranda-Agrippino-Rey document). Both are genuine crowding-adjacent
states in the loose sense that a broad, VIX-driven de-grossing episode will typically catch crowded
factor books in its wake — but neither can see the content CR-D1–CR-D3 are built for, and the gap is
precise rather than a hand-wave: L2 and L9 are constructed from **market-wide** realized volatility,
index-level implied volatility, and funding spreads — aggregate quantities that move when *the whole
market* de-risks, whether or not any single factor is crowded at all. A factor can be extremely
crowded — capital concentrated, valuation stretched, comomentum elevated — while the broad market
sits calm, realized vol low, VIX unremarkable, exactly the state CR2's own finding describes for
India's mid-2025 experience (a real, documented global unwind, zero trace in a monthly return series
that would, in principle, also fail to move a market-wide vol measure at India's cadence). Conversely,
a broad market sell-off (L2/L9 firing hard) need not concentrate in any one factor's crowded names at
all. The two states are complements, not substitutes, precisely on the de-duplication principle this
program's own atlas states for every other pairing (`docs/CYCLE_ATLAS.md` §14): L2/L9 answer "is the
market, in aggregate, under stress"; CR-D1–CR-D3 answer a different, factor-specific question — "is
capital concentrated enough in this particular factor's names that its own unwind, whenever it
comes, will be worse than the factor's ordinary volatility would suggest" — a question only
AUM-growth, valuation-percentile, and comomentum data, never a market-wide vol or funding-spread
series, can answer.

**What stays runsheet-gated, stated honestly rather than smoothed over.** Comomentum itself (CR-D2)
needs high-frequency, stock-level return data cross-referenced against each factor's own
investable universe — a genuine data-phase build, not yet vaulted, exactly as the momentum
monograph's own A.9 gap-list already states. India-**attributed**, not industry-aggregated, AUM by
fund and by factor needs an AMFI category-level pull finer than what the desk has scraped so far —
D02's own low-vol-trigger row already flags this same caveat ("current figures are
industry-aggregated, not sleeve-attributed"). And fund-level India smart-beta AUM specifically
carries a documented data-quality problem the momentum dossier already recorded rather than
papering over: individual-product AUM figures scraped for that dossier were "inconsistent/noisy
(single funds reporting implausible multi-lakh-crore AUM alongside plausible ₹400–8,500cr figures
for sibling share classes)," with the aggregate ₹46,000cr total and the ₹16,000cr single-rebalance
trade size corroborated independently and usable as order-of-magnitude anchors, but a clean, dated,
per-fund AMFI table remains a data-phase pull rather than something this research phase can certify.
None of this blocks pre-registering CR-D1/CR-D2/CR-D3 today; all of it blocks any of the three from
being promoted past Tier C, or from being trusted at fund-level resolution, until the data lands.

---

## C. The verdict pair

**3.3 — Factor rotation: FOLD into L8 (value-spread conditioning) and L3 (momentum), never
separately budgeted.** The value-momentum complementarity is real, large, and already harvested
statically by the design's own construction (the AMP mechanism, the desk's own −0.37/−0.41
correlation prints, the 50/50-beats-both-legs Sharpe result). The regime linkage the atlas names
already lives inside L8's own conditioning rule — "tilts toward momentum when the value spread is
bottom-tercile" is, read carefully, a value-momentum rotation rule that ships today, bounded within
a frozen weight range, Stambaugh-corrected, exactly matching the "sin a little, not a lot" resolution
the Arnott-versus-Asness tactical-timing debate supports and no more. Ehsani-Linnainmaa's finding
that momentum is itself a vehicle for timing other factors closes the loop formally: a standalone
rotation construct would be a third-order timing bet built from two signals — L3 and L8 — that are
each, individually, already timing devices for the content it would claim to add. The label is
retired; the object it named stays exactly where L3 and L8 already carry it.

**3.4 — Crowding/unwind: CANDIDATE, instrumented, Tier C reduce-only.** The mechanism (Stein 2009)
is a genuine limit to arbitrage among sophisticated capital, not a story about ignorance; the
sharpest measurement tool (Lou-Polk comomentum) is unbuilt on India data today, leaving the desk on
the cruder AUM-growth proxy the atlas actually names. The canonical episodes — August 2007's
days-long, index-invisible synchronized unwind; 2009's momentum crash, already defended by L3's
seated crash_guard; the mid-2025-through-January-2026 global quant unwind, verified this session in
more granular detail than the design previously carried, including the instructive finding that the
crowded factor rotates between episodes rather than sitting still — establish the mechanism is
alive, current, and multi-factor, not a historical curiosity. India's own record (₹290cr→₹46,000cr
smart-beta AUM, 2020–2025, still growing) shows the same dynamic building in the desk's own market.
The desk's own CR1/CR2 trial, run on the vaulted India factor library, earns its keep by producing a
design-setting result rather than a merely confirmatory one: crash concentration is real (CR1b
passes) but unconditional negative skew is not (CR1a fails, vindicating the existing conditional
crash_guard rather than motivating a new unconditional one), and — the finding that shapes the
candidate's entire architecture — the named 2025 episode is **invisible** in India's own monthly
momentum factor returns (CR2), meaning the monitor cannot be built from factor returns alone. The
candidate that survives this evidence is exactly the one the atlas names and no more: three
pre-registered, Tier-C, reduce-only legs (AMFI AUM growth-rate, factor-valuation percentiles, and a
comomentum leg gated on data that does not yet exist), entering the registry through the same
`tierC_overlay` mechanism the design already uses elsewhere, never a source of added exposure, and
never promoted past Tier C until its own pre-registered bars are cleared on real data.

### Synthesis

| Claim | Strongest evidence | Where it lives | Verdict |
|---|---|---|---|
| Value-momentum negative correlation (the global fact) | Asness-Moskowitz-Pedersen (2013), 8 markets/asset classes; desk's own India −0.37 / US −0.41 (V2), 50/50 Sharpe beats both legs both panels (V3) | Static value+momentum construction in the factor book (`docs/DESIGN.md` §6.1/§6.2) — no timing required to capture it | **Harvested statically. No separate seat.** |
| Regime-linked value/momentum leadership (rates/credit) | Lettau-Wachter (2007/2011) duration theory; AQR/Asness's own honest instability finding (ρ≈0.03/40y, 0.34/10y); Ehsani-Linnainmaa (2022) factor-momentum autocorrelation | **L8's value-spread conditioner** — "tilts toward momentum when the value spread is bottom-tercile" (`docs/DESIGN.md` §6.2) | **FOLD — already inside L8.** |
| Tactical factor-timing as a standalone construct | Arnott-Beck-Kalesnik-West (2016) vs. Asness-Chandra-Ilmanen-Israel (2017) "Contrarian Factor Timing is Deceptively Difficult" — the "sin a little, not a lot" resolution | L8's bounded, quantile, frozen-range conditioner already implements the "sin a little" answer; nothing further licensed | **No standalone rotation signal. RETIRED with evidence attached.** |
| Crowding as a mechanism | Stein (2009) Presidential Address — sophisticated-investor externality, a genuine limit to arbitrage (category ii) | The design's Tier-C treatment of every crowding-adjacent monitor (reduce-only, `tierC_overlay`) | **Kept as the mechanism behind 3.4; no independent seat of its own.** |
| Crowding, measured | Lou-Polk (2022) comomentum — India unbuilt; AUM-growth the cruder, disclosure-lagged proxy in use today | **CR-D2** (comomentum, runsheet-gated) + **CR-D1** (AMFI AUM growth-rate, free today) | **Candidate — CR-D1 live-able now, CR-D2 gated on data.** |
| Synchronized long-short unwind (canonical case) | Khandani-Lo (2007/2011) — Aug-2007, days-long buildup, hours-long acute phase, invisible in broad indices | Cited as the paradigm case; no direct India analogue tested | **CONTEXT for the candidate's design; not independently modeled.** |
| Momentum crash (2009-style) | Daniel-Moskowitz (2016); desk's own M4 crash_guard validation (guard-ON −2.19%/m vs OFF +1.81%/m) | **L3's seated crash_guard** (`docs/DESIGN.md` §6.1) | **Already defended. Not 3.4's job to duplicate.** |
| Mid-2025→Jan-2026 global quant unwind | Goldman Sachs prime-brokerage (−4.2% Jun–Jul 2025) + UBS (−2.8% Jan 2026) + named-fund press figures, verified this session; multi-factor (momentum/quality/low-vol) contagion confirmed, crowded factor rotates between episodes | The atlas's own named episode motivating 3.4 | **Alive, current, multi-factor — the candidate's motivating case.** |
| India smart-beta/factor-fund AUM growth | ₹290cr (2020) → ~₹46,000cr (end-2025), ~12% of passive equity AUM; >70 ETFs/index funds by Aug-2025; decay-audit finding (Major, `docs/masterplan/D-risk-register.md` row 6) that only low-vol carried a trigger | **CR-D1** design (AMFI category AUM growth-rate, momentum/low-vol/quality) | **Free today. The candidate's live-able leg.** |
| Crash-asymmetry signature on India's own factor library | CR1a (skew ordering, FAIL — India momentum not unconditionally skewed) / CR1b (crash concentration, PASS — WML worst −4.1σ, deepest of three) / CR2 (2025 episode invisible monthly — ZERO months ≤−2σ) | `research/register/trial-ledger.md` CR1a–CR2; `research/cycles/crowding-deep/crowding-RESULTS.md` | **Design-setting: monitor cannot be returns-only. AUM/comomentum legs are structural, not decorative.** |

The pattern across both entries, stated once and matching the sibling monographs' own closing note:
a real, well-evidenced phenomenon is worth exactly the budget its own evidence supports, no more
because a compelling label asks for more (3.3's "rotation"), and no less because the desk's existing
registry happened not to be watching yet (3.4's crowding gap, closed only after an audit found it).
Neither verdict downgrades the underlying finance; both are the credit the record supports, no more,
no less — one fold with its evidence attached, one candidate with its design constraint measured
before a single rupee of AUM data exists.

---

## References

Asness, Clifford S.; Moskowitz, Tobias J. & Pedersen, Lasse Heje (2013), "Value and Momentum
Everywhere," *Journal of Finance* 68(3):929–985. · Lettau, Martin & Wachter, Jessica (2007), "Why
Is Long-Horizon Equity Less Risky? A Duration-Based Explanation of the Value Premium," *Journal of
Finance* 62(1):55–92; (2011), "The Term Structures of Equity and Interest Rates," *Journal of
Financial Economics* 101(1):90–113. · AQR/Asness commentary on the duration test and 0.03/0.34
correlation figures (existing AQR publication and press coverage; Tier C, directional use only,
already cited in full in `docs/cycles/04-value-quality.md` A.3). · Ehsani, Sina & Linnainmaa,
Juhani T. (2022), "Factor Momentum and the Momentum Factor," *Journal of Finance* 77(3):1877–1919.
· AlphaArchitect (blog), "Are Value, Carry and Momentum Regime Dependent?" **[VERIFIED as an
existing practitioner source; Tier C, directional use only]**. · Arnott, Robert D.; Beck, Noah;
Kalesnik, Vitali & West, John (2016), "How Can 'Smart Beta' Go Horribly Wrong?," Research
Affiliates. · Asness, Clifford S.; Chandra, Swati; Ilmanen, Antti & Israel, Ronen (2017),
"Contrarian Factor Timing is Deceptively Difficult," *Journal of Portfolio Management*, Special
Issue 2017. · Stein, Jeremy C. (2009), "Presidential Address: Sophisticated Investors and Market
Efficiency," *Journal of Finance* 64(4):1517–1548. · Lou, Dong & Polk, Christopher (2022),
"Comomentum: Inferring Arbitrage Activity from Return Correlations," *Review of Financial Studies*
35(7):3272–3302 (already `docs/cycles/03-momentum-trend.md` A.7's citation, not re-verified here). ·
Khandani, Amir E. & Lo, Andrew W. (2008), "What Happened to the Quants in August 2007?: Evidence
from Factors and Transactions Data," NBER Working Paper 14465; published version, *Journal of
Financial Markets* 14(1):1–46 (2011). · Daniel, Kent & Moskowitz, Tobias J. (2016), "Momentum
Crashes," *Journal of Financial Economics* 122(2):221–247 (already `docs/cycles/03-momentum-
trend.md` A.8's citation, not re-verified here). · Cohen, Polk & Vuolteenaho (2003), "The Value
Spread," *Journal of Finance* 58(2):609–641 (already `docs/cycles/04-value-quality.md` A.4's
citation, not re-verified here). · Trade-press and prime-brokerage/UBS-sourced coverage of the
2025–2026 quant unwind (Goldman Sachs prime-services estimates; named-fund performance reporting on
Renaissance Technologies, Schonfeld, Engineers Gate) — verified this session as existing,
corroborated reporting; Tier C by source. · `research/dossiers/01-momentum-reversal.md` §2/§7
(India smart-beta/momentum-index AUM figures, ₹290cr→₹46,000cr, ₹16,000cr single-rebalance trade
size, product family list — the desk's own prior figures, corroborated not recomputed). ·
`research/register/decay-redteam.md` §3 and `docs/masterplan/D-risk-register.md` row 6 (the audit
finding behind entry 3.4's "post-audit addition" tag). · `research/register/trial-ledger.md`
entries CR1a–CR2 and `research/cycles/crowding-deep/crowding-RESULTS.md`/`partDH-verdict-
routing.md` (this pairing's own pre-registered trial, results, and design routing — cited in full,
never recomputed). · `docs/cycles/03-momentum-trend.md` and `docs/cycles/04-value-quality.md`
(companion monographs this chapter cites throughout and never contradicts). · `research/cycles/
kitchin-juglar/partAB-theory-cases.md` (style bar and paired-entry structure this chapter follows).

---

# PART RESULTS — The desk's own numbers (CR1a/CR1b/CR2, pre-registered)

# Atlas 3.3/3.4 — crowding: crash asymmetry on India factors (CR1-CR2, pre-registered)

| Factor | monthly skew | worst month (own σ) | worst month (date, %) |
|---|---|---|---|
| WML | +0.05 | -4.1σ | 2001-11 (-27.6%) |
| SMB | +0.04 | -2.9σ | 2020-03 (-14.1%) |
| HML | +0.60 | -3.4σ | 2000-01 (-19.0%) |

- CR1a (skew(WML) ≤ −0.5 AND most negative): **FAIL**.
- CR1b (WML worst ≤ −4σ AND most extreme): **PASS**.

## CR2 — 2025 WML months at ≤ −2σ (the named mid-2025 unwind, measurement)

- NO 2025 month reaches −2σ in India's WML.

- 2025 monthly WML z-scores: [-1.1, -0.0, -0.1, -0.6, -1.0, 0.0, 0.1, -0.1, -0.5, 0.1, 0.5, 0.0]

## Honest read (written AFTER the print)

- **CR1a FAILS, and it's the BC2 lesson again — an imported stylized fact dying on transfer.**
  The US literature's "momentum is negatively skewed" does NOT hold unconditionally on India's
  33-year factor library (WML skew +0.05, indistinguishable from SMB's +0.04; HML is the
  POSITIVELY skewed one at +0.60). Consistency check against monograph 03: no contradiction —
  its crash finding was CONDITIONAL (bear-market-then-rally windows), and a conditional crash
  tail can coexist with ~zero unconditional skew when normal-times momentum is right-skewed.
  The refined sentence: India's momentum danger is REGIME-LOCAL, not a standing distributional
  feature — which is precisely what the seated crash_guard (conditional, not permanent)
  already implements. Design vindicated by the fail.
- **CR1b PASSES: crash CONCENTRATION is real.** WML's worst month sits at −4.1σ of its own
  distribution, more extreme than SMB's (−2.9σ) and HML's (−3.4σ) — the synchronized-exit
  signature shows in the tail's depth even where it doesn't show in the third moment.
- **CR2: the named mid-2025 quant unwind left NO trace in India's monthly WML** (no 2025
  month at −2σ). Two readings, both recorded: the episode was US/global-implementation-
  specific, and/or unwind episodes live at daily/intramonth granularity invisible to monthly
  academic factors. Either way the consequence for the 3.4 candidate is structural: MONTHLY
  FACTOR RETURNS CANNOT BE THE MONITOR — the AUM-growth and comomentum legs (runsheet) are
  necessary, not decorative, and the candidate's design says so from its first day.

---

# Parts D–H — verdict + routing (atlas 3.3 FOLD + 3.4 CANDIDATE; paired entry)

## Part D — What CR1/CR2 establish

Three findings with three different jobs. CR1b (WML worst month −4.1σ, deepest of the three
factors) confirms the synchronized-exit TAIL the crowding mechanism predicts. CR1a's fail
retires an import: India's momentum is NOT unconditionally negatively skewed (+0.05) — the
danger is regime-local, exactly the shape monograph 03's CONDITIONAL crash_guard already
implements; an unconditional de-risking of momentum would have been the wrong medicine, and
the fail is the evidence. CR2 sets the candidate's design constraint from day one: the named
mid-2025 unwind is INVISIBLE at monthly academic-factor granularity — so the 3.4 monitor
cannot be built from factor returns; its legs are AUM growth-rate and factor-valuation
percentiles (the atlas's own observables) plus a comomentum leg when stock-level data lands.

## Part E — Routing

| Content | Where it lives |
|---|---|
| Value↔momentum complementarity | HARVESTED STATICALLY: the 50/50 blend (monograph 04's Sharpe result) — no rotation signal exists to time |
| Regime-linked factor leadership | L8's conditioning rules (seated) — "rotation" retired as a label |
| Momentum crash defense | L3's crash_guard (seated, CONDITIONAL — CR1a's fail is its vindication) |
| Crowding monitors (3.4 candidate) | Tier-C reduce-only monitors on momentum/low-vol/quality: AMFI smart-beta AUM growth-rate + factor-valuation percentiles (runsheet); comomentum leg at stock-level data |
| "Factor rotation" / unconditional momentum-skew claims | RETIRED with prints attached |

## Part F — Harvest + designs

Harvest: the import-refinement (regime-local danger) as Cycle School material; the
design-setting CR2 finding; the retirement of the register's most-marketed factor label.
Designs: **CR-D1** the AMFI smart-beta AUM leg (category AUM growth-rate percentile; bars at
data-landing); **CR-D2** comomentum (Lou-Polk construction on NSE500 once stock-level returns
are vaulted; acceptance registered then); **CR-D3** the factor-valuation leg (each factor's own
value-spread percentile — machinery exists in L8's family; registered before any look).

## Part H — Knowledge ledger (atlas 3.3/3.4)

**Established (our runs):** crash concentration is real (CR1b); unconditional negative skew is
NOT (CR1a — the import dies, the conditional design stands); monthly factor returns cannot see
unwind episodes (CR2). **Kept by fold:** the complementarity (static 50/50) and the regime
conditioning (L8) — nothing to time. **Candidate [3.4, Tier C]:** instrumented with the right
observables from day one because CR2 forced the issue. **Unknowable:** the next unwind's
trigger and venue; monitors watch accumulation, never predict the shock. **Process:** the
paired entry pattern held — one fold with evidence, one candidate with its design constraint
measured before a single rupee of AUM data exists.
