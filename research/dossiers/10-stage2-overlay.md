# Workstream 10 — Stage-2 Overlay: Human + AI Forward Views

Status: RESEARCH ONLY, per `CONTRACT.md` and `OPEN_QUESTIONS.md` (defaults assumed throughout,
notably OPEN_QUESTIONS #7 — paired pre-registered test + Brier-scored ledger — and #9 — structured
checklist scorer with hard caps plus adversarial red-team). Scope: the evidence for and against
letting human and AI forward-looking judgement touch a portfolio that Stage 1 has already built
complete on its own, and the full operating charter for the switchable overlay this evidence
justifies — authority bounds, ledger fields, scoring, promotion/demotion, and the evaluation gate.

**Methodological note, stated up front per CONTRACT §12's honesty requirement.** This session's
`WebSearch` budget was exhausted before this workstream ran (every call returned "this session has
used its web search budget, 200 of 200") and `WebFetch` returned `EGRESS_BLOCKED` for every domain
tested (Wikipedia, NBER, Google) — the same outage Workstreams 08 and 09 recorded under CONTRACT §7
Known Prior #11. No live verification was possible for this pass. Every citation below is drawn
from trained knowledge and tagged **(recalled, high/moderate confidence)** where I am confident of
author/venue/year, or **[VERIFY: …]** where a specific figure, page, or author ordering needs
confirmation once search access returns. This workstream is unusually citation-dense and unusually
consequential for the design — the LLM-backtest-invalidity argument in §1/§3 is load-bearing for
the whole Stage-2 charter — so it should be prioritized for re-verification alongside 08 and 09.

---

## 1. Findings and literature

**F1. Meehl, Paul E. (1954), *Clinical versus Statistical Prediction: A Theoretical Analysis and a
Review of the Evidence*, University of Minnesota Press (recalled, high confidence).** The founding
document of the whole debate. Reviewed roughly 20 studies comparing a clinician's holistic judgement
against a simple statistical/actuarial formula built from the same input variables, across
parole-violation prediction, psychiatric outcome prediction, and similar tasks. In essentially all
but one, the formula matched or beat the clinician. Meehl's own conclusion was not "humans are
useless" but the much narrower and more useful claim that mechanical, cross-validated combination
rules dominate *because* they apply the same weights consistently every time — a claim about
**noise reduction**, not about the human's raw information content. Meehl's own 1957 follow-up essay
"When Shall We Use Our Heads Instead of the Formula?" *[VERIFY: exact venue/year — recalled as
*Journal of Counseling Psychology*, 1957]* introduces the **broken-leg problem**: a well-validated
formula predicts with 90%+ confidence that a person will go to the cinema tonight, based on decades
of that person's behaviour; the clinician who happens to know the person broke their leg yesterday
should override the formula, not because clinical judgement is generally superior, but because the
broken leg is (i) a discrete, (ii) rare, (iii) highly diagnostic fact (iv) structurally outside the
model's variable set. Meehl's own repeated caution: this exception is invoked far more often than it
legitimately applies, and the correct response to "I have a broken-leg case" is usually to add the
variable to the model, not to keep overriding by hand indefinitely. This is the **design principle**
this dossier uses to bound every human/AI override below (§3, §4).

**F2. Grove, W. M., Zinn, [co-authors] & Meehl-tradition meta-analysis (2000), "Clinical versus
Mechanical Prediction: A Meta-Analysis," *Psychological Assessment* 12(1), 19–30
[VERIFY: exact co-author list — recalled as Grove, Zinn, and colleagues, high confidence on the
substance, moderate confidence on the precise byline].** Pools 136 studies across medicine,
psychiatry, education, personnel selection, and forensic settings comparing clinical (holistic,
human) judgement against mechanical (statistical/actuarial, formula-based) prediction on the *same*
input data. Headline result, widely reproduced in secondary summaries: mechanical prediction was
**substantially more accurate** in roughly a third of studies, **about equal** in roughly half, and
clinical judgement was **substantially more accurate** in only some 6–16% of studies [VERIFY: exact
percentages — recalled as approximately 33–47% mechanical wins / 48–52% ties / 6–16% clinical wins].
The average effect size favoured the mechanical method by roughly **10 percentage points of
accuracy** [VERIFY: exact effect-size metric — recalled as an average validity-coefficient gain,
moderate confidence on the precise number]. Critically for design purposes: the studies where
clinical judgement won tended to be exactly the broken-leg cases — situations where the clinician
had access to information categorically absent from the formula's inputs (an interview cue, a
non-tabular fact), not situations where the same information was weighted "more wisely" by a human.

**F3. Kleinberg, Jon; Lakkaraju, Himabindu; Leskovec, Jure; Ludwig, Jens; Mullainathan, Sendhil
(2018), "Human Decisions and Machine Predictions," *Quarterly Journal of Economics* 133(1),
237–293 (recalled, high confidence on authorship/venue/year; moderate confidence on exact figures
below — [VERIFY]).** Uses ~750,000 New York City pretrial bail decisions (2008–2013) to compare
judges' actual jail/release decisions against a machine-learning (gradient-boosted-tree) risk model
trained on the same defendant data available to judges. Because judges make binary release/detain
decisions and only *some* released defendants' outcomes are observed, the paper builds a
selective-labels correction to make the comparison honest. Headline results: relative to judges'
actual decisions, the algorithm's ranking could **reduce the jailed population by roughly 42% with
no increase in the pretrial crime rate**, or, run the other way, **reduce crime by roughly 25% with
no increase in the jailing rate** [VERIFY: exact 42%/25% figures]. The mechanism is not "the machine
sees data the judge doesn't" — it sees *less* than the judge (the judge can also see the defendant's
demeanour in court, the arresting officer's account, etc.) — the mechanism is that **judges are
highly inconsistent (noisy) across similar cases and are disproportionately swayed by salient but
low-predictive-value case features** (e.g., the specific alleged offense's lurid detail) relative to
the base-rate-relevant history. A nontrivial share of the defendants judges release are in the
machine's *highest*-predicted-risk bracket, and vice versa. This is the single strongest piece of
evidence in this dossier that unaided, real-time, high-stakes human discretion is *not* simply
"lower-variance but occasionally insightful" — it is measurably Pareto-dominated by a simple,
consistent rule built from the same information, in a domain (predicting an individual's future
behaviour under uncertainty) structurally similar to "will this position perform."

**F4. Tetlock, Philip E. (2005), *Expert Political Judgment: How Good Is It? How Can We Know?*,
Princeton University Press (recalled, high confidence).** A 20-year (1984–2004), ~284-expert,
tens-of-thousands-of-forecasts research program (the widely cited round number is ~82,000 discrete
probability judgements [VERIFY: exact count]) asking political/economic subject-matter experts for
calibrated probability forecasts on real-world events (elections, wars, economic turning points,
regime survival). Headline results: the average expert was **barely distinguishable from chance**
("a dart-throwing chimpanzee" is Tetlock's own deliberately provocative shorthand, not a literal
claim of zero skill) and **did somewhat worse than simple extrapolation algorithms** on the same
questions [VERIFY: exact comparison statistic]. The most robust internal predictor of forecasting
accuracy was cognitive **style**, not credentials, ideology, or access to information: "foxes" (who
draw on many small, sometimes-conflicting frameworks, hold views with explicit uncertainty, and
update readily) systematically out-forecast "hedgehogs" (who apply one big, coherent theory
consistently and resist disconfirming evidence). Famous, highly credentialed pundits with strong,
telegenic single narratives were, on average, among the *worst* calibrated. This paper is the direct
ancestor of the entire "superforecasting" research program (F5) and is the primary reason this
dossier treats **free-form narrative conviction as the specific failure mode Stage 2 must be
designed to avoid**, not an incidental risk.

**F5. Tetlock, Philip E. & Gardner, Dan (2015), *Superforecasting: The Art and Science of
Prediction*, Crown Publishers (recalled, high confidence); underlying research: Mellers, Barbara;
Ungar, Lyle; Baron, Jonathan; Ramos, Jaime; Gurcay, Burcu; Fincher, Katrina; Scott, Sydney E.;
Moore, Don; Atanasov, Pavel; Swift, Samuel A.; Murray, Terry; Stone, Eric; Tetlock, Philip E.
(2014), "Psychological Strategies for Winning a Geopolitical Forecasting Tournament," *Psychological
Science* 25(5), 1106–1115 (recalled, high confidence on venue/year; moderate confidence on exact
author ordering — [VERIFY]).** Reports on IARPA's ACE forecasting tournament and the Good Judgment
Project (GJP) team within it, which ran thousands of forecasters against real-world geopolitical
questions over multiple tournament years, experimentally varying three interventions: (i)
**training** — a short course in probabilistic reasoning, base rates, and common bias correction;
(ii) **teaming** — forecasters working in interacting groups rather than alone; (iii) **tracking** —
periodically identifying the top-performing forecasters ("superforecasters," roughly the top 2%)
and regrouping them into elite teams. Each intervention independently improved accuracy — training roughly **10%**, teaming a larger gain
(commonly cited as roughly **20–30%** [VERIFY]), tracked elite teams the largest gain of all — and
GJP's tracked superforecaster teams reportedly **outperformed U.S. intelligence-community analysts
with access to classified information by a wide margin (~30% commonly cited)** [VERIFY: this specific
comparison is widely repeated in secondary sources but unconfirmed against the primary source here].
The mechanism bundle that worked — explicit numeric probabilities, short well-defined horizons,
structured aggregation across independent estimators, periodic recalibration against realized
outcomes — is precisely the GJP "house style" the structured-scorer form (§4.D) is built to
reproduce, in deliberate contrast to Tetlock (2005)'s pundit failure mode.

**F6. Harvey, Campbell R.; Rattray, Sandy; Sinclair, Andrew; Van Hemert, Otto (Man Group/Duke,
circa 2017), "Man vs. Machine: Comparing Discretionary and Systematic Hedge Fund Performance,"
*Journal of Portfolio Management* [VERIFY: exact volume/issue/year — recalled with moderate
confidence on authorship and substance, low-moderate confidence on exact venue details].** Compares
long-run hedge-fund-database performance of systematic versus discretionary macro and equity
strategies. Recalled findings: **systematic macro/CTA-style strategies show a more reliably positive
return profile specifically during broad market-stress ("crisis alpha") episodes**, with lower
cross-manager dispersion, while **discretionary strategies show materially higher cross-manager
dispersion** — a wide spread between a few standout discretionary managers and a much larger mass of
average-to-poor performers, especially concentrated around the same crisis windows where systematic
strategies cluster tightly around a positive outcome. Average risk-adjusted performance across the
full sample period is not dramatically different between the two styles pooled, but the **shape** of
the outcome distribution differs starkly: systematic is a repeatable, budget-able exposure;
discretionary is a highly manager-specific, low-replicability draw. This is cross-country,
cross-strategy hedge-fund-index evidence, not India-specific, and is additionally subject to the
well-documented hedge-fund database biases (survivorship, self-reporting, backfill) that widen
apparent manager dispersion beyond the true population dispersion — a caveat this dossier applies
directly in §3.

**F7. Discretionary macro in crises — practitioner record, largely anecdotal (Tier C).** The 2008
GFC produced both famous discretionary winners (managers who built an explicit, correctly-timed
subprime short thesis) and a much larger, less-publicized set of discretionary blow-ups and
forced-deleveraging losses; the same period produced systematic trend-following ("CTA") index
returns that were **positive as an asset class** (the widely cited "trend followers made money in
2008" stylized fact for indices such as the SG Trend Index / Newedge CTA Index [VERIFY: exact index
values]), a much more repeatable, lower-dispersion outcome than the discretionary experience in the
same window. The March 2020 COVID crash reversed this pattern for systematic trend specifically —
the fall was too fast and too quickly reversed for trend-following signals built on multi-week
lookbacks to react in time, consistent with CONTRACT Known Prior #8 ("fast crashes cannot be met by
cycles") — while some discretionary macro managers who moved to cash pre-emptively on qualitative
epidemiological reasoning captured a real edge in that specific narrow window. Net reading: neither
style has a monopoly on crisis performance; what is robust across both 2008 and 2020 is that
**systematic exposure is a repeatable, sizeable portfolio component and discretionary/qualitative
judgement is, at best, an occasionally-decisive but statistically unreliable supplement** — exactly
the asymmetry the reduce-only default in §4 is designed around.

**F8. Kahneman, Daniel; Sibony, Olivier; Sunstein, Cass R. (2021), *Noise: A Flaw in Human
Judgment*, Little, Brown Spark (recalled, high confidence).** Distinguishes **bias** (systematic,
directional error — the traditional behavioural-economics focus) from **noise** (unwanted,
unsystematic scatter across judges who should reach the same conclusion given the same case), and
decomposes noise into **level noise** (some judges/underwriters are just systematically harsher or
more lenient than others), **pattern noise** (a given judge reacts idiosyncratically to specific
case features, not consistently across cases), and **occasion noise** (the same judge, same case,
different day/mood/weather/hunger produces a different verdict — the book cites real audits finding,
e.g., sentencing severity correlated with local weather and with whether the judge's sports team won
recently [VERIFY: exact studies cited]). Insurance-underwriting and judicial "noise audits" find
noise-driven variance often **exceeds** bias-driven error in magnitude — i.e., the bigger problem in
many real human-judgement systems is not that everyone is wrong in the same direction, it is that
everyone disagrees with each other (and with their own past selves) far more than anyone realizes.
Prescribed remedy: **"decision hygiene"** — structuring judgement into independent, decomposed
sub-assessments made before an aggregate view is formed; delaying holistic/intuitive synthesis until
after the structured inputs are locked; algorithmic or checklist-based aggregation of those
sub-assessments; and mediating-assessment protocols that force explicit, comparable scales across
raters. This is the direct design source for the structured-scorer form's decomposition (§4.D) and
for scoring AI and human theses on identical, structured fields rather than free-text narrative.

**F9. Lopez-Lira, Alejandro & Tang, Yuehua (2023), "Can ChatGPT Forecast Stock Price Movements?
Return Predictability and Large Language Models," SSRN Working Paper (recalled, moderate-high
confidence on authors/title/venue; low-moderate confidence on exact reported statistics —
[VERIFY]).** Feeds historical news headlines to GPT-3.5 with a prompt asking it to score sentiment
(good/bad/uncertain for the stock's next-day return) and constructs a long-short trading strategy
from the scores. Reports a large, statistically strong in-sample/backtest return premium attributable
to the LLM-derived sentiment score, including outperformance versus simpler sentiment dictionaries
[VERIFY: exact Sharpe ratio and sample period reported]. This is the paper Stage-2 design must treat
as **Exhibit A of the exact failure mode it must not repeat** — see F10 for why the headline result
is inadmissible as evidence of a real, forward-usable edge.

**F10. Glasserman, Paul & Lin, Caden [or similar co-author — VERIFY exact name] (2023), "Assessing
Look-Ahead Bias in Stock Return Predictions Generated By Large Language Models," SSRN/arXiv working
paper [VERIFY: exact title wording, co-author, and venue — recalled with moderate confidence on
substance and Glasserman's authorship, lower confidence on the precise title and co-author].**
Directly critiques the Lopez-Lira & Tang-style backtest design: an LLM's training corpus is scraped
at a date **after** the historical events the backtest asks it to "predict," and very likely contains
text discussing the eventual outcome of those events (retrospective news coverage, analyst
commentary written after the fact, encyclopedic summaries) — so the LLM may be **recalling a learned
association between a headline's language/topic and its known subsequent outcome**, not exercising
genuine ex-ante forecasting skill. The paper proposes tests to detect this (e.g., comparing accuracy
on events strictly before vs. strictly after the model's stated training cutoff; probing whether
performance degrades appropriately when company names/dates are synthetically altered) and finds
evidence consistent with **contamination inflating the apparent backtested edge**. This is the
paper this dossier treats as decisive for Stage-2 evaluation design (§3, §4.G): unlike a quant
factor's look-ahead bias (fixable with point-in-time data hygiene, per CONTRACT Known Prior #7),
**LLM training-data contamination cannot be fixed by better data hygiene on the researcher's side**,
because the contamination lives inside the model's weights, which the researcher does not control
and cannot fully audit.

**F11. Chen, Lingjiao; Zaharia, Matei; Zou, James (2023 or 2024), "How Is ChatGPT's Behavior
Changing over Time?", arXiv preprint [VERIFY: exact year — recalled as 2023, moderate confidence]
(recalled, moderate-high confidence on substance).** Finds that GPT-3.5 and GPT-4's accuracy and
behaviour on fixed benchmark tasks (e.g., identifying prime numbers, code generation, sensitive
question answering) **changed substantially between two model snapshots a few months apart**, with
performance improving on some tasks and degrading on others, under an unchanged prompt. This is the
primary evidence for treating **each LLM model version as a distinct forecaster with its own,
separately-earned track record** (§4), not a single continuously-improving entity whose Brier
history can be carried forward across silent version changes.

**F12. LLM forecasting-tournament literature, 2022–2025 (Tier C/B, mixed — [VERIFY all four]).**
(a) Zou, Andy; Zhang, et al. (approx. 2022), "Forecasting Future World Events with Neural Networks"
(the **Autocast** benchmark, NeurIPS 2022 [VERIFY]) — benchmarks language models against Metaculus-
style forecasting questions and human crowd forecasts, finding base LLMs generally **underperform
the human crowd** on calibrated probabilistic forecasting, improving with retrieval augmentation but
not closing the gap fully. (b) Schoenegger, Philipp & Park, Peter S. (2023), "Large Language Model
Prediction Capabilities: Are LLMs Better Than Random Chance?" [VERIFY exact title/venue] — finds
GPT-4-class models substantially beat random chance but roughly match or trail the aggregated human
crowd on binary forecasting questions. (c) Schoenegger, Park, and co-authors (2024), "AI-Augmented
Predictions: LLM Assistants Improve Human Forecasting Accuracy" [VERIFY] — finds giving human
forecasters access to an LLM assistant modestly **improves** the humans' own accuracy, i.e., the
LLM's best-evidenced current role is as an *input to* a human/crowd aggregate, not a standalone
authority. (d) Halawi, Danny et al. (2024), "Approaching Human-Level Forecasting with Language
Models" [VERIFY exact authors/venue] — reports a retrieval-augmented LLM pipeline reaching close to
crowd-level accuracy on Metaculus-style questions with careful engineering, still short of the top
human superforecaster tier. Taken together, this cluster is consistent, moderate-confidence-in-
direction evidence that **current LLMs are, at best, crowd-comparable general forecasters and are
best used as one voice in an ensemble**, never as a sole authority — directly supporting the
minimum-ensemble-size rule in §4.

---

## 2. India-specific evidence

Direct, India-specific academic evidence comparing discretionary versus systematic/quant investment
performance is **not available** in the public literature as far as this pass can establish — this
is a genuine evidence gap, not an oversight, and should be logged as a data-phase priority rather
than papered over with a cross-country substitute alone.

**A concrete, free, India-specific data source exists to close part of this gap in the data phase.**
SEBI's Portfolio Managers Regulations require SEBI-registered Portfolio Management Services (PMS)
providers to disclose standardized performance data, and the **Association of Portfolio Managers in
India (APMI)** publishes/aggregates PMS-level performance disclosures on a public or semi-public
basis [VERIFY: exact disclosure scope, whether strategy-level discretionary/systematic tagging is
present, and current public accessibility — recalled with moderate confidence that a standardized
APMI disclosure regime exists, low confidence on the granularity of what it actually reports]. If the
disclosures are granular enough to classify individual PMS strategies as discretionary versus
rules-based/quant (many PMS providers self-describe this in their disclosure documents and
factsheets), this becomes a genuinely India-specific empirical test of the Harvey-Rattray-Sinclair-
Van Hemert (F6) cross-country finding, and should be attempted early in the data phase (§6) before
this dossier's cross-country prior is trusted for sizing.

**Institutional constraints specific to India that bound the Stage-2 design, independent of the
performance-evidence question:**

- **SEBI's algorithmic-trading regulatory perimeter.** SEBI has progressively tightened oversight of
  algorithmic order generation — registration/empanelment requirements for algo providers via
  exchanges, unique algo-ID tagging of orders attributable to an algorithm, and distinctions between
  categories of automated strategies [VERIFY: exact current circular scope and effective dates as of
  2026 — recalled with moderate confidence that such a framework exists and has been extended over
  2021–2025, low confidence on the precise current text]. If an AI-generated signal were to reach the
  order management system **without a human execution step**, this Stage-2 system plausibly falls
  inside that perimeter and would need registration/tagging/audit-trail compliance as an algorithmic
  trading system, not merely "computer-assisted research." This is a load-bearing reason (independent
  of the Meehl broken-leg governance argument) for the charter's hard rule in §4.I: **no fully
  automated AI-to-order pipeline** — every Stage-2 override, at every authority rung, passes through
  an explicit human execution/approval step before it reaches an order.
- **SEBI's AI/ML usage reporting for registered intermediaries.** SEBI has required certain
  categories of registered market intermediaries (stockbrokers, and by extension entities operating
  regulated investment vehicles) to periodically report their use of AI/ML applications
  [VERIFY: exact circular reference and current scope, recalled with low-moderate confidence that
  such a reporting obligation exists in some form since approximately 2019]. Whatever entity
  ultimately houses this book (a registered PMS/AIF, if it takes that form) should expect Stage 2 to
  be a disclosable AI/ML application under whatever the current version of that reporting regime is —
  a compliance-calendar item, not a research question, but one the charter should not be silent about.
- **SEBI Research Analyst / Investment Adviser registration.** Not directly triggered by a
  proprietary book trading its own capital, but if Stage-2 outputs (theses, forward views) were ever
  externalized to outside investors or third parties, whoever generates and communicates them would
  likely need RA/IA registration under SEBI's regulations for that activity. Flagged for future scope
  awareness, not a current-phase constraint.
- **Retail/FII/DII flow structure and promoter concentration** (per CONTRACT §1) matter for *what*
  Stage 2 should be trying to add judgement about, not for the overlay's own evidence base: the kinds
  of "regime-breaking, not-yet-priced" information a human/AI overlay might legitimately catch in
  India specifically include index-inclusion-driven passive flow events, SAST 5%-threshold disclosure
  triggers revealing promoter/large-holder intent shifts, ASM/GSM surveillance-action announcements,
  and derivative-ban-period entries/exits — all discrete, dated, structurally outside a pure
  price/fundamental lookback window, and therefore the closest India-specific analogues to Meehl's
  broken-leg category (§3).

**No India-specific evidence exists (to this pass's knowledge) on LLM forecasting performance on
Indian market questions, prompt behaviour in Hindi/regional-language financial text, or India-focused
forecasting tournaments.** This is treated as a pure cross-country prior, Tier B at best per CONTRACT
§9's own India-thin-history convention, capped at Tier C for anything LLM-specific given the added
look-ahead-bias concern (§3).

---

## 3. Decay and crowding assessment

Per CONTRACT §5, every candidate signal needs a written survival argument or an explicit numeric
haircut. Stage 2 is unusual: it is not one signal but an authority to generate ad hoc signals, so the
survival argument has to be made about the **mechanism class**, and the honest starting prior is
inverted relative to a normal Tier-B/C candidate.

**Claimed mechanism.** Human and AI forward judgement can, in principle, synthesize information
Stage 1 structurally cannot: discrete, dated, non-tabular, or genuinely novel facts (a regulatory
change, a geopolitical shock, a management-commentary signal, a not-yet-priced structural change)
that have not occurred often enough to be a fitted statistical signal (by definition n<4, hence
Tier C under CONTRACT §4's own ladder) and that a pure price/fundamental lookback cannot see at all.
This maps most naturally onto CONTRACT §5's category **(iv) institutional constraint** —
specifically, the constraint that a systematic model's variable set is fixed and closed, while the
real world's information set is open — rather than (i) a persistent behavioural mechanism, (ii) a
capacity limit, or (iii) a risk premium. It is *not* subject to the classic "arbitrage capital arrives
and the edge decays" dynamic (McLean-Pontiff) because it isn't a return premium being priced away; it
degrades instead through a different channel — **noise**, unreliability, and self-deception in how
the judgement is actually formed and scored (F2, F3, F4, F8).

**What the evidence actually says about that mechanism's survival.** F1–F4 and F8, pooling well over
a thousand studies across medicine, parole, personnel selection, political forecasting, and judicial
sentencing, converge on: unaided, free-form, real-time expert judgement is beaten or matched by a
simple consistent rule in the large majority of measured cases (F2: mechanical wins or ties in
roughly 85–95%+ of 136 studies), and where real-time, high-stakes discretion is measured directly
against an algorithm built from the *same* inputs (F3), the algorithm dominates by a wide, economically
large margin. Tetlock (F4) shows the specific failure mode this dossier most needs to guard against —
telegenic, single-narrative conviction forecasting — performs at or below chance. The one place
expert override adds value in this literature is Meehl's own broken-leg case: discrete,
out-of-model information, invoked rarely, not as an ongoing second-guessing channel. Separately,
F5/Mellers show that *structured, scored, probabilistic, teamed, and periodically recalibrated*
human forecasting (the opposite of Tetlock's pundit style) meaningfully beats the untrained baseline
and, on the tournament's own claims, beats domain-expert baselines too. **The conclusion this dossier
draws is therefore conditional, not blanket**: Stage 2 has no survival argument at all if it is run
as free-form thesis generation with human veto (the option explicitly *not* chosen as the
OPEN_QUESTIONS #9 default); it has a plausible, evidence-consistent survival argument only if it is
run as the structured, scored, red-teamed, GJP-style protocol this dossier's charter specifies, and
only within the narrow broken-leg role until it earns more.

**Numeric decay haircut, stated explicitly per CONTRACT §5.** Because the honest prior from F1–F4 is
that unaided judgement *destroys* value in the large majority of measured analogous settings, this
dossier does not haircut an assumed-positive Stage-2 edge by a fractional decay rate (the McLean-
Pontiff style 26%/58% haircut, appropriate for a *proven* factor being crowded); instead it applies a
**100% haircut at inception on any risk-adding authority** — the expected marginal contribution of
Stage 2 is treated as zero-or-negative by default, and the only authority that survives a maximally
skeptical prior is the one whose downside is bounded even if the judgement is pure noise: **reduce
risk, never add**, which is exactly CONTRACT §4's own Tier-C rule, applied here for an independent
reason (the specific human/AI-judgement evidence base) that reinforces rather than merely inherits
the general Tier-C default. Authority to add is not earned by argument; it is earned by a
pre-registered, out-of-sample track record clearing the evaluation gate in §4.C — inverting the usual
burden of proof relative to a normal Tier-B/C quant candidate, where the default leans toward
inclusion pending disproof.

**LLM sub-component: an additional layer of skepticism, argued separately.** F9's apparent backtested
edge is inadmissible as evidence per F10's contamination argument (elaborated in §4.G below), so there
is no even-provisional positive prior to start from for the AI side specifically — unlike the human
side, which at least has the GJP counter-example (F5) of a working protocol. F12's forecasting-
tournament literature shows current-generation LLMs are, on general calibrated-forecasting tasks,
roughly crowd-comparable at best and sub-crowd at worst, with their best-evidenced role being as one
input to an aggregate, not a standalone authority. F11's behaviour-drift finding means even a
positive track record does not transfer across model versions. **Design consequences:** (a) no single
LLM call may constitute the entire "AI" side of a thesis — an ensemble of at least two independent
calls (different prompt framing, different model, or both) is required before an AI-originated thesis
can even be logged, mirroring F5's teaming/aggregation logic, not a fitted magic number but a
structural minimum below which "independent-estimate averaging" does not exist; (b) a model-version
change resets that component's earned track record to zero (F11); (c) an LLM-only historical backtest
of a forward-view strategy is **never admissible evidence** at any tier, for any promotion decision,
regardless of statistical significance (§4.G).

**Discretionary macro / "star manager" crowding.** F6/F7's cross-country hedge-fund evidence shows the
discretionary style's outcome distribution is wide and manager-specific (high level-noise and
occasion-noise, in Kahneman-Sibony-Sunstein's F8 vocabulary) rather than a repeatable population-level
edge, and its documented crisis strength is itself inconsistent across crises (2008 favoured
systematic trend more uniformly; 2020 favoured a handful of discretionary qualitative calls). This
supports the charter's decision (§4.H) that Stage 1's own systematic vol/regime machinery, not Stage
2, should own the primary crisis-hedging role, with Stage 2 confined to a bounded, early-timing nudge
within a regime-permitted band — never the primary defense.

---

## 4. Proposed parameters

The Stage-2 charter, in full. Every bound below is either sourced to a citation in §1 or argued
explicitly (per CONTRACT §6, no magic numbers: relative/structural rules preferred over fixed
absolute thresholds; the few absolute integers that remain are governance circuit-breakers, argued
as such, not fitted return-predicting constants).

### 4.A Purpose, scope, and the switch

Stage 2 sits strictly **on top of** a complete Stage-1 portfolio (CONTRACT §2). It may only: (i) tilt
sizing on names/exposures Stage 1 has already selected; (ii) request one step of hedge-ratio change
on the frozen 0/25/50/75/100/125/150% grid, jointly with and never independent of the regime that
already permits that step (CONTRACT §3); (iii) impose a reduce-only veto on a name, sleeve, or the
in-progress staged-entry aggregate; (iv) call a temporary stand-down/no-new-trades pause. It may
**never**: introduce a name outside Stage-1's own candidate universe; change Stage-1's fitted
parameters or method; or (at Rung 0, see below) add exposure beyond what Stage 1 already sized. The
whole system is switchable off instantly, reverting to Stage-1-only — this switch is the
falsifiability instrument the paired test in §4.C exploits, and is precisely why Stage 2's design
must not be *load-bearing* for the drawdown ceiling or the honest-CAGR targets (CONTRACT Known
Priors #3, #9): Stage 1 must be able to stand alone at all times.

### 4.B The authority ladder

| Rung | Unlock condition | Reduce-only authority | Add authority | Hedge/leverage authority |
|---|---|---|---|---|
| **0 (inception default)** | None — this is where Stage 2 starts and where it stays absent an earned promotion | Cut any Stage-1 position toward zero, capped at ≤50% of that position's *current* Stage-1 weight per instance (relative rule, not a fixed pp); shrink book gross/net; shrink the in-progress staged-entry aggregate; raise the hedge ratio one grid step early *within the regime-permitted band* | None | None beyond the one-step-early hedge raise |
| **1 (limited add)** | n≥20 scored theses in the book, rolling Brier Skill Score >0 vs. the frozen reference forecaster (§4.E), **and** the paired IR test (§4.C) non-negative over the same window | Same as Rung 0 | Add to an *existing* Stage-1 name only, capped at the lesser of 25% of that position's current Stage-1 weight or 1.0pp of book NAV per instance; aggregate outstanding Rung-1 adds capped at 2pp of book NAV concurrently | None beyond Rung 0 |
| **2 (fuller add)** | n≥50, rolling BSS positive over **two consecutive** evaluation windows, paired IR/DD test (§4.C) passing at its pre-registered bar in both windows | Same as Rung 0 | Cap raised to the lesser of 50% of position weight or 2.5pp of NAV per instance; aggregate outstanding cap 5pp of NAV | May request **one** hedge/leverage grid step in the risk-*adding* direction, still jointly with and bounded by the regime (never independently) |
| **De-promotion** | Automatic and immediate (no probation window) on: rolling BSS turning negative in *any* window, or paired IR/DD falling below the Stage-1-only baseline in *any* window | — reverts straight to Rung 0 | | |

The n=20/50 floors are set deliberately at the lower and upper bounds of CONTRACT §4's own Tier-B
band (4–30 observations, extended to a second Tier-B-adjacent checkpoint at 50 for the fuller rung),
not fitted to any backtest — this is the same evidentiary ladder the rest of the program already uses,
applied to Stage 2's own track record instead of to a market signal. De-promotion is asymmetric by
design and deliberately unforgiving: a false demotion costs little (Stage 1 stands alone and the
authority can be re-earned), while a false retention of broken authority risks the drawdown ceiling —
the same asymmetry that makes the ceiling itself binding rather than a soft target (CONTRACT §3).

### 4.C The paired pre-registered evaluation test (OPEN_QUESTIONS #7 default)

- **Design.** Run a shadow Stage-1-only portfolio in parallel with the live Stage-1+Stage-2
  portfolio, from identical starting weights and prices, so the only source of divergence is Stage
  2's interventions — this isolates Stage 2's marginal effect exactly as CONTRACT §2 requires
  ("quant-only vs quant-plus-overlay is the only honest measure of Stage 2's value").
- **Primary statistic.** Paired difference in net Information Ratio, (Stage1+2) minus (Stage1-only),
  over rolling non-overlapping quarterly windows aligned to Stage-1's own evaluation cadence; test via
  Wilcoxon signed-rank (nonparametric preferred given likely small-n, non-normal paired differences)
  or the Jobson-Korkie-Memmel corrected Sharpe-difference test with the Harvey-Leybourne-Newbold
  small-sample correction (both already specified generically in Workstream 09, applied here to the
  Stage-1-vs-Stage-2 pair specifically). Pre-registered one-sided (H1: overlay IR > baseline IR),
  locked before Stage 2's first live override, never re-cut afterward.
- **Gating statistic, independent of the primary one.** Paired difference in max drawdown on the
  same crash-episode definition as CONTRACT's frozen constraint (OPEN_QUESTIONS #5 default: episodes
  where Nifty fell >20% and did not recover its pre-fall peak within ~63 trading days). Stage 2 must
  not make episode DD *worse* — a one-sided non-inferiority test, paired per episode, that fails
  independently of the IR result: a good IR outcome never offsets a DD deterioration, mirroring
  CONTRACT's "drawdown is binding" framing (DD is a gate, not a blended-score component).
- **Multiple-testing discipline.** Every hedge-grid step, tier, and book multiplies the number of
  implicit comparisons; count all of them cumulatively into the same deflated-Sharpe trial count
  CONTRACT §9 already mandates for the data phase generally (Workstream 09, F8 there) — Stage 2's
  sweeps are not a separate, uncounted budget.
- **Minimum n before any authority change is considered statistically meaningful:** n≥20 (Rung 1
  floor). Below that, the test still runs and is logged for calibration purposes only, but may **not**
  change authority — this prevents small-sample overreaction in either direction.

### 4.D The structured-scorer + red-team form (OPEN_QUESTIONS #9 default)

Every thesis, human- or AI-originated, is logged on identical fields (Kahneman-Sibony-Sunstein's
decision-hygiene decomposition, F8, applied literally):

1. **Thesis ID, timestamp, author** (human / AI / joint), book(s) affected.
2. **Directional call** — which exposure (name / sleeve / hedge step), direction (add capped by
   rung; reduce always available), requested magnitude (bounded per §4.B).
3. **Horizon** — an explicit date or event by which the thesis resolves. No open-ended theses.
4. **Mechanism tag** — must name one of CONTRACT §5's four survival categories, or a fifth,
   Stage-2-specific category: *"genuinely novel information not yet reflected in Stage-1's
   lookbacks"* — named explicitly because it is the only legitimate reason for Stage 2 to exist at
   all (§3), so it cannot be left implicit.
5. **Pre-registered numeric probability** (0–100%) of the stated outcome by the stated horizon —
   mandatory, not verbal ("likely," "probably"), so it is Brier-scorable per F5/Mellers' own
   house style.
6. **Falsifier** — the specific, observable condition that would prove the thesis wrong *before* the
   horizon; a pre-committed exit trigger distinct from (but which may include) a price stop.
7. **Red-team field, mandatory, authored by a role distinct from the proposer** — if the AI proposes,
   the human red-teams (or a second, independently-prompted AI instance/persona does, per §3's
   minimum-ensemble rule), and vice versa. Self-red-teaming by the same model instance that generated
   the thesis is disallowed: a single LLM asked to critique its own output is a documented weak check
   (consistency/sycophancy bias), and F8's decision-hygiene logic requires **independent**, not
   self-referential, assessment. If the red-team's probability crosses the 50% line relative to the
   proposer's (i.e., they disagree on *direction*, not merely magnitude — a threshold-free, sign-based
   escalation rule), the thesis is escalated to human-only adjudication and may not be resolved by the
   AI that proposed it.
8. **Mechanical hard-cap checklist** — non-overridable, rules-engine checks against CONTRACT's own
   constraints (gross leverage 1.5x, name entry 5–6%, drift 10%, in-progress aggregate 20%, options
   notional 50%/75%, current rung's authority cap). A failed check blocks submission regardless of
   thesis quality — this is deliberately dumb and mechanical, the "structured scorer" half of
   OPEN_QUESTIONS #9's default, precisely so it cannot be argued around by a persuasive narrative.
9. **Outcome** (filled at horizon or falsifier trigger, whichever comes first) — realized result,
   Brier-score contribution, short retrospective note.
10. **Reproducibility metadata for AI-originated theses** — model ID/version, prompt-template ID/hash,
    sampling temperature/seed where available, and the literal prompt+response logged verbatim.
    Required because of documented model-version drift (F11) and known prompt-order/framing
    sensitivity in LLM outputs [VERIFY: specific prompt-sensitivity citation — recalled generally,
    e.g. work on in-context example ordering effects and calibration-before-use recalibration
    methods, exact paper unconfirmed], so a later audit can distinguish a genuine skill change from a
    silent model swap or a prompt-wording artifact.

### 4.E Brier scoring and calibration

- **Brier score** = mean squared error between stated probability and realized binary outcome,
  BS = (1/N)Σ(pᵢ − oᵢ)², range 0 (perfect) to 1 (worst). Report the **Murphy decomposition**
  (Reliability + Resolution − Uncertainty) alongside the raw score, not the raw score alone — a
  "always predict the base rate" forecaster scores deceptively well on raw Brier while adding zero
  information (zero resolution).
- **Brier Skill Score** BSS = 1 − BS_stage2 / BS_reference, where the **reference forecaster is fixed
  before Stage 2 launches** and recomputed each window using only information available at that
  window's start (never retroactively redefined): Stage-1's own implied probability where Stage 1
  emits one, otherwise a persistence/base-rate forecaster calibrated on the book's own history. This
  operationalizes "beats the baseline," not "beats zero," and avoids the Stambaugh-bias-adjacent trap
  of refitting the benchmark after the fact to flatter Stage 2.
- **Calibration curves** — bin stated probabilities into deciles, plot realized frequency against
  stated probability, report Expected Calibration Error. Track **separately for AI-originated,
  human-originated, and joint theses**, and separately by mechanism-tag category (§4.D field 4) — an
  auditable basis for *segmented* promotion (e.g., an AI component well-calibrated only in one
  mechanism category earns add-authority only there, not blanket authority) rather than an all-or-
  nothing ladder.
- **Cadence** — score and republish the calibration curve at every evaluation window (aligned to the
  paired-test cadence, §4.C), inside the same versioned research register CONTRACT §10 already
  mandates, so Stage-2 authority state is as auditable and CI-checkable as any other config parameter.

### 4.F Governance / kill-switch

Any single override that would breach a CONTRACT hard cap (leverage, entry, drift, in-progress
aggregate, options notional) is void on submission and logged as a hard-constraint-breach flag,
regardless of rung or thesis quality — the mechanical checklist (§4.D field 8) is the enforcement
point. **Three such flags accumulating within a rolling evaluation window auto-disables Stage 2
entirely** (reverts to Stage-1-only) pending human review. This is one of the few small fixed
integers in this charter defensible as such: it is a governance circuit-breaker, not a return-
predicting parameter, and mirrors CONTRACT §10's own principle that "a registry violating its own
budget must fail to load" — applied here to Stage-2 authority instead of to a data pipeline.

### 4.G Why LLM forward views cannot be honestly backtested — the design consequence, stated explicitly

F9 (Lopez-Lira & Tang) shows a naive but seductive result: an LLM sentiment score, backtested against
historical headlines, produces strong apparent return predictability. F10 (Glasserman & Lin) shows
the mechanism that invalidates this: the model's training corpus postdates the historical events
being "predicted" and plausibly contains text discussing their eventual outcome, so the model may be
recalling a memorized association, not forecasting. Unlike a quant factor's look-ahead bias (fixable
with point-in-time data hygiene — CONTRACT Known Prior #7's restated-fundamentals problem), **this
contamination cannot be fixed from the researcher's side**: it lives inside model weights that
frontier labs do not fully disclose, that get silently updated via fine-tuning or retrieval
augmentation, and whose "training cutoff" cannot be independently verified to mean zero information
leakage about post-cutoff-dated-but-pre-cutoff-discussed events. **Consequence, stated as a hard
design rule mirroring CONTRACT §8's "do not report a fundamental backtest without its price-only
counterpart":** any historical backtest of an LLM-generated forward view is inadmissible as evidence
of skill, full stop, regardless of apparent statistical significance. The only admissible evaluation
is prospective — theses logged (ideally with immutable/append-only timestamping, at minimum in the
versioned register) **before** the resolution date and scored only after — which is why the paired
gate (§4.C) and CONTRACT §9's pre-registration discipline apply to Stage 2 with more force than to
Stage 1, not less: Stage 1's factors can at least be tested point-in-time against genuinely
pre-existing historical data; Stage 2's LLM component cannot be tested against *any* historical data
it might have memorized, which in practice means all data before Stage 2's own deployment date.
**Operational corollary:** every model-version upgrade resets that component's Brier/BSS track record
to n=0 (per F11's drift evidence) — a real, recurring operational cost (frontier models update every
6–12 months) that this charter states plainly rather than hides.

### 4.H Interaction with Tier-C reduce-only and the hedge grid

Per CONTRACT §3, the hedge ratio moves only as a swept parameter jointly with the regime that selects
it — never independently. Stage 2 respects this exactly: it may request one grid step, only within
the band the current regime (per Stage 1's own regime matrix) already permits — a bounded, real lever
(earlier/faster timing within a pre-approved band) without ever violating "jointly, never
independently." Per §3's crowding assessment, Stage 1's own systematic vol/regime machinery — not
Stage 2 — owns the primary crisis-hedging role; Stage 2's hedge authority is a timing nudge, never the
primary defense.

### 4.I Human-in-the-loop execution rule (India-specific, §2)

No Stage-2-generated override reaches the order management system without an explicit human
execution/approval step, at every rung. This is required independently by two separate arguments: the
Meehl broken-leg governance principle (an override should be rare and deliberately gated, not routed
automatically), and the plausible SEBI algorithmic-trading regulatory perimeter for a fully automated
AI-to-order pipeline (§2) [VERIFY: current circular scope]. This rule is not a performance parameter
and is not subject to the authority ladder — it never relaxes with track record.

### Provenance table

| Name | Value/range | Source | Tier | Confidence | Decay assumption | What would change it |
|---|---|---|---|---|---|---|
| Stage-2 default rung at inception | Rung 0: reduce-only, no add authority | CONTRACT §4 Tier-C rule; F1–F4 (unaided judgement underperforms in the large majority of measured analogous settings) | C→B (governance rule built on a Tier-B/A evidence base) | High | 100% haircut on add-authority until earned | Never — this is the structural default, not a fitted parameter |
| Rung-0 reduce cap | ≤50% of position's current Stage-1 weight per instance (relative, not fixed pp) | This dossier's argument, §4.B | C (design) | Moderate | N/A | Raised only via the ladder, never by direct edit |
| Rung-1 unlock | n≥20 scored theses, rolling BSS>0, paired IR non-negative | CONTRACT §4's own Tier-B floor (4–30 obs), applied to Stage-2's track record | B (application of an existing evidentiary convention) | Moderate | N/A | Reassessed if effective-n (autocorrelation-adjusted) is shown much lower than raw n (§7) |
| Rung-1 add cap | ≤25% of position weight or ≤1.0pp NAV per instance; ≤2pp NAV aggregate outstanding | This dossier's argument, §4.B, sized to CONTRACT Known Prior #3's ~100–300bps/yr cycle-stack contribution as an order-of-magnitude anchor | C (design) | Low-moderate | N/A | Recomputed once real Rung-1 track record exists and the paired test has power estimates |
| Rung-2 unlock | n≥50, BSS positive 2 consecutive windows, paired IR/DD passing both windows | CONTRACT §4 Tier-B upper bound extended as a second checkpoint | B (application) | Moderate | N/A | Same as Rung-1 unlock |
| Rung-2 add cap | ≤50% of position weight or ≤2.5pp NAV per instance; ≤5pp NAV aggregate | This dossier's argument, §4.B | C (design) | Low-moderate | N/A | Same as Rung-1 add cap |
| De-promotion trigger | Immediate, any window: BSS<0 or paired IR/DD below Stage-1-only baseline | This dossier's asymmetric-cost argument, §4.B, echoing CONTRACT's own binding-DD asymmetry | C (design) | High (on the asymmetry principle; the exact statistic is design, not fitted) | N/A | Never loosened; may be tightened if false-demotion cost is shown higher than assumed |
| Paired evaluation cadence | Quarterly, aligned to Stage-1's own rebalance/evaluation cycle | This dossier, §4.C | C (design) | Moderate | N/A | Could move to monthly if Stage-1's own cadence does (CONTRACT §3 allows weekly–monthly) |
| Minimum ensemble size, AI-side of a thesis | ≥2 independent prompts/model calls before an AI thesis may be logged | F5 (teaming), F12 (crowd-comparable LLM forecasting), §3 argument | B (cross-domain application) | Moderate | N/A | Raised if calibration data (§4.E) shows single-call theses are as well-calibrated as ensembles (would falsify the teaming argument in this specific application) |
| LLM track-record reset | n resets to 0 on any model-version change | Chen-Zaharia-Zou (F11) | B | Moderate-high | N/A | Relaxed only if a canary-panel test (§6) shows negligible drift for a specific version pair |
| LLM historical backtest admissibility | Zero — never admissible at any tier | Lopez-Lira & Tang (F9) as the failure case; Glasserman & Lin (F10) as the mechanism | B (methodological argument, general even though sourced to one paper) | High on the logic; moderate on exact F9/F10 citation details | N/A | Only by a verified, independent, model-agnostic method for proving zero training-corpus overlap — not currently available |
| Red-team escalation rule | Escalate to human-only adjudication whenever red-team and proposer probabilities fall on opposite sides of 50% | F8 (independent assessment), this dossier (sign-based, threshold-free) | C (design) | Moderate | N/A | N/A — structural, not fitted |
| Kill-switch trip count | 3 hard-constraint-breach flags within a rolling evaluation window → auto-disable Stage 2 | This dossier, §4.F, echoing CONTRACT §10's CI "fail to load" principle | C (governance, defensible as a circuit-breaker not a return parameter) | High on the principle; the number 3 itself is a judgement call | N/A | Tightened to 1 (or loosened to a higher count) if realized flag frequency post-launch suggests miscalibration |
| Human-in-the-loop execution gate | Applies at every rung, never relaxes | Meehl broken-leg doctrine (F1); SEBI algo-trading perimeter argument, §2 [VERIFY] | B/C mixed (governance doctrine well-evidenced; regulatory specifics unverified) | High on the doctrine; low on current SEBI circular specifics | N/A | Re-examine only if SEBI's regulatory text is confirmed to explicitly permit fully automated AI-to-order flows under disclosed conditions |

---

## 5. Evidence-tier recommendations

Grading here separates **the underlying human-judgement-versus-model evidence** (which is often
Tier-A-caliber *within its own domain*) from **its application to this specific portfolio-overlay
design** (which is necessarily a cross-domain, and for the LLM component cross-domain-plus-emerging-
technology, transplant — capped per CONTRACT §9's own convention).

| Finding/method | Own-domain tier, observation count | India/finance-application tier | Notes |
|---|---|---|---|
| Grove-Meehl clinical vs. mechanical prediction (F1, F2) | A within its own domains — 136 pooled studies, decades of replication across medicine/forensics/education | **B** as a cross-domain prior for portfolio overlay design | Directly informs process design (structure beats free-form judgement); does not itself supply a numeric portfolio parameter |
| Kleinberg et al. bail/ML (F3) | B in its own right — one very large single dataset/paper (~750,000 cases), not yet a multi-study meta-analysis in that exact setting, though highly influential and widely replicated in spirit by later criminal-justice ML work | **C** as a direct finance analogy (single study, different domain) | Strongest *individual* piece of evidence that real-time expert discretion can be Pareto-dominated; treated as directional support, not a parameter source |
| Tetlock EPJ (F4) | B in its own domain — one 20-year research program, large N of forecasts but one investigator's program | **C** as applied to finance-specific forward views | Informs the pundit-failure-mode design warning directly; not a numeric source |
| Mellers/GJP (F5) | B, high-confidence within-tier — one large, multi-year, IARPA-funded tournament with many replications across question-years and conditions | **B** as applied here (the strongest process-design evidence in this dossier) | Directly sources the structured-scorer/teaming/tracking design (§4.D); the closest thing to a positive, actionable prior in the whole workstream |
| Harvey-Rattray-Sinclair-Van Hemert, discretionary vs. systematic funds (F6) | B — index-level, decades of data, but subject to well-known hedge-fund-database biases | **B**, cross-country, not India-specific | Supports the reduce-only default and the "systematic owns crisis-hedging" design choice (§4.H) |
| Discretionary macro crisis anecdotes (F7) | C — practitioner record, largely anecdotal, survivorship-prone | **C** | Directional support only; explicitly flagged low-reliability |
| Kahneman-Sibony-Sunstein Noise (F8) | B — synthesizes decades of noise-audit studies across many fields, strong within-tier confidence | **B** as applied to Stage-2 form design | Directly sources the structured-form decomposition (§4.D) |
| Lopez-Lira & Tang (F9) | C — single paper, backtest-only, methodologically compromised by F10's critique | **C**, and arguably a negative example rather than a positive source | Never a source of a usable parameter; used only as the illustrative failure case in §4.G |
| Glasserman & Lin (F10) | B — single paper, but the argument's logic is general and not specific to one dataset | **B** methodological guidance | Foundational for the "never backtest LLM forward views" design rule (§4.G), treated as argument, not as a numeric source |
| Chen-Zaharia-Zou model drift (F11) | B — one paper, but a well-replicated general phenomenon (documented independently by many practitioners/API users) | **B** | Sources the model-version track-record reset rule |
| LLM forecasting-tournament cluster (F12) | C/B mixed — several distinct papers, emerging and fast-moving literature, not yet consolidated into a stable meta-analytic estimate | **C** | Directional support for the minimum-ensemble rule; none of these figures should be frozen as a hard parameter given how fast this specific literature is moving |
| India-specific discretionary-vs-quant evidence | Unavailable | **Unavailable — data-phase priority** | See §2/§6; APMI disclosures are the proposed free source to close this gap |

---

## 6. Research method for the data phase

- **Paired IR/DD test (§4.C).** Pre-register the exact statistic, the reference-forecaster
  definition, and the n=20/50 thresholds **before Stage 2's first live override**, in the same
  versioned register CONTRACT §9 mandates for every other hypothesis in the program. Never re-cut the
  test after seeing results. Apply the Harvey-Leybourne-Newbold small-sample correction (already
  specified generically in Workstream 09) given the realistically short paired-evaluation horizon.
- **Brier Skill Score and calibration curves (§4.E).** Fix the reference forecaster's construction
  rule before launch; recompute it each window from only the information available at that window's
  start (no retroactive redefinition — the Stambaugh-bias-adjacent trap of moving the goalposts to
  flatter Stage 2). Report the Murphy decomposition every window, not the raw Brier score alone.
- **Effective-n adjustment.** Stage-2 theses are unlikely to be independent across time (correlated
  macro views, clustered market regimes) — the data phase must estimate the autocorrelation of thesis
  outcomes and discount the raw n=20/50 floors to an effective-n before treating the ladder's unlock
  conditions as satisfied; this is flagged explicitly as unresolved in §7.
- **APMI PMS-disclosure test (§2).** Pull APMI/SEBI-mandated PMS performance disclosures, classify
  providers by self-described discretionary versus rules-based/quant strategy type from public
  factsheets, and compare risk-adjusted return and drawdown distributions — an India-specific
  replication attempt of the Harvey et al. (F6) cross-country finding, to be run before the cross-
  country prior is trusted for any India-specific sizing decision. Free source per CONTRACT §12.
- **LLM canary panel.** Build a small, fixed panel of previously-scored forecasting questions;
  re-run it against every new model version before that version's output is trusted for live theses,
  operationalizing the Chen-Zaharia-Zou (F11) drift finding as a concrete pre-deployment check rather
  than an abstract caution.
- **Ledger-gaming audit.** Before trusting any accumulated Brier/BSS track record, check for
  selective logging (theses recorded only after a favorable outcome is already visible, horizons
  quietly extended, falsifiers redefined after the fact) — this is a data-integrity check on the
  ledger itself, analogous to the pre-registration-violation check CONTRACT §9 mandates generally, and
  should run every evaluation window, not just at promotion checkpoints.
- **CI validation of authority state.** Every override event should validate against the same
  CI-checked registry CONTRACT §10 already mandates for every other config parameter — rung-cap
  containment, tier-C reduce-only enforcement at Rung 0, the mechanical hard-cap checklist (§4.D field
  8) — making Stage-2 authority state machine-checkable, not merely policy on paper.
- **Deflated-trial accounting.** Fold every Stage-2 sweep (hedge-grid steps requested, rung
  thresholds tested, mechanism-tag categories examined for segmented promotion) into the same
  cumulative trial count the whole program's Deflated Sharpe Ratio calculation already tracks
  (Workstream 09) — Stage-2's own internal experimentation is not a separately-budgeted trial pool.
- **Nothing here is optimized against backtest performance** (CONTRACT §8): the ladder's n-floors,
  caps, and de-promotion rule are validated for gaming and mis-specification in the data phase, not
  tuned to maximize any historical Sharpe or IR — a rule change to any of them requires a new,
  pre-registered argument, not a re-fit.

---

## 7. Open questions and [VERIFY] items

**Tooling constraint, restated.** No live web search or fetch was possible this pass (session-wide
budget exhaustion plus network-wide `EGRESS_BLOCKED`, identical to Workstreams 08/09's recorded
outage). Every citation above rests on trained knowledge only. This entire dossier should be
re-verified against primary sources with the first available search budget, in this priority order:

1. **F10 (Glasserman & Lin)** — this is the single most load-bearing citation in the workstream (it
   underwrites the entire "never backtest LLM forward views" design rule, §4.G); confirm exact title,
   author list, venue, and year before this argument is presented to the principal as sourced rather
   than argued from first principles.
2. **F9 (Lopez-Lira & Tang)** — confirm exact reported statistics (Sharpe ratio, sample period) since
   this dossier uses it as the canonical failure-case illustration.
3. **F2 (Grove et al. 2000 meta-analysis)** — confirm exact co-author list, the 33–47%/48–52%/6–16%
   breakdown, and the ~10-point effect-size figure; this is the single strongest piece of evidence for
   the inverted-burden-of-proof default in §3/§4.B and deserves precision.
4. **F3 (Kleinberg et al.)** — confirm the 42%/25% headline figures and the ~750,000-case sample size.
5. **F5 (Mellers et al. 2014 / GJP)** — confirm exact author ordering and the training/teaming/tracking
   percentage improvements; also confirm (or retract) the widely-repeated "beat intelligence-community
   analysts with classified access by ~30%" claim, which this dossier could not verify and flags as
   the least confident single figure carried in §1.
6. **F11 (Chen-Zaharia-Zou)** — confirm exact title, year (2023 vs. 2024), and venue.
7. **F12 cluster** — confirm existence, authorship, and venue for each of the four papers cited; this
   is the fastest-moving literature in the dossier and the most likely to already be superseded by
   newer work as of the actual 2026 research date.
8. **F6 (Harvey-Rattray-Sinclair-Van Hemert)** — confirm exact venue/year; the substance (systematic
   vs. discretionary crisis-performance shape) is held with more confidence than the bibliographic
   details.
9. **SEBI algorithmic-trading perimeter and AI/ML reporting circulars (§2, §4.I)** — confirm current
   (2026) scope, specifically whether a human-approved-per-override design (as this charter requires)
   sits outside the algo-registration perimeter, or whether any AI-assisted signal generation upstream
   of a human-approved order still triggers disclosure/tagging obligations. This should go to
   compliance counsel, not be resolved by further literature search alone.
10. **APMI PMS disclosure granularity (§2, §6)** — confirm whether current disclosures allow
    discretionary-vs-systematic strategy classification at the granularity needed for the proposed
    India-specific replication test; if not, this data source should be dropped from the data-phase
    plan rather than assumed.

**Open design questions, not resolvable by literature alone:**

- Is n=20/50 the right floor given likely-correlated thesis outcomes across time? The effective-n
  adjustment (§6) is unresolved and should be estimated empirically once even a small pilot ledger
  exists, rather than assumed away.
- Should the red-team role rotate systematically between human and a second AI instance, or be
  assigned ad hoc by whoever is available? This dossier recommends systematic rotation, logged in the
  ledger, but leaves the operational assignment to the principal.
- Rung-1/Rung-2 add-authority caps (§4.B) are argued from an order-of-magnitude anchor to CONTRACT
  Known Prior #3's ~100–300bps/yr cycle-stack contribution, not derived from any Stage-2-specific
  data (none exists yet) — flagged explicitly as the weakest-sourced numeric row in the provenance
  table (§4) and the first candidate for revision once real track record accumulates.
- Whether the kill-switch trip count (3 flags) is well-calibrated is unknown until Stage 2 actually
  runs; this dossier states the number is a judgement call, not a derived one, and should be revisited
  against realized flag frequency early in live operation.
