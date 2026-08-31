# Decay / Overfit Red Team — adversarial pass on DESIGN.md v0.9

Auditor role: decay/overfit red team, no web access. Scope per assignment: (1) magic-number hunt
in DESIGN.md + `config/*.yaml`; (2) break the survival argument on the §10 decay ledger, name the
weakest three of ~18; (3) recompute §1.1 at the pessimistic end of every band — does any book miss
its floor; (4) crowding blind spots; (5) 2026–2036 parameter staleness and registry triggers;
(6) can the Stage-2 advisory-only gate be gamed. Default skeptical; only findings that survive a
second look are reported. All arithmetic below was re-run and is reproducible from the cited files.

---

## 0. Headline finding (Task 3 first, because it is the most consequential)

**Recomputing §1.1's honest-target table at the pessimistic (low) end of every stated component
range makes all three books miss their own published CAGR-band floor.** DESIGN §1.1 says the bands
are "**built additively** from sourced parts, each after its decay haircut (§10) and cost (§9)," and
§10's design rule states "§1.1's bands are computed from haircut values." Taking that literally —
summing each row's stated low end (books.yaml `net_cagr_band` is the number under test):

| Book | Market | Mid/small | Momentum | Factor | Spec-sits | Leverage | Drag | **Sum** | **Stated floor** | **Shortfall** |
|---|---|---|---|---|---|---|---|---|---|---|
| Aggressive | 12 | +1 | +3 | +1 | +0.5 | +0.2 | −2 | **15.7%** | 18% | **−2.3pp** |
| Moderate | 12 | 0 | +0.5 | +2.5 | 0 | 0 | −1.5 | **13.5%** | 14% | **−0.5pp** |
| Conservative | 12 | 0 | 0 | +1 | 0 | 0 | −1 | **12.0%** | 13% | **−1.0pp** |

Every book misses, and always in the same direction (published floor > true worst-case additive
sum) — a one-sided bias is exactly what you'd expect if the floor number was chosen to look
respectable rather than mechanically derived from the same ranges printed two lines above it. That
is precisely the "overfitting enters before fitting" failure mode CONTRACT §6 exists to catch,
except here it has infected the summary table of the design document itself, not a fitted
parameter.

It gets worse on the leverage line specifically. The stated floor (+0.2pp aggressive) is not even
the model's own worst case: §5.4/risk.yaml's `funding_hurdle` rule is `h(·) = 1 only if
E[r_proxy] − funding_rate > buffer, else caps leverage at 1.0` — i.e. under retail MTF funding
(9–12%) with a non-trivial buffer, the hurdle can fail entirely and leverage contributes **zero**,
not +0.2pp. Re-run with leverage = 0: aggressive sum = 15.5%, a 2.5pp miss.

Caveat, stated honestly: DESIGN doesn't specify whether the published band was meant as a literal
min/max of independent additive draws (in which case this is a straightforward arithmetic
inconsistency) or a scenario-weighted blend (in which case perfectly-correlated worst-cases
under-state plausibility somewhat — but note several of these worst-cases are *positively*
correlated, not independent: weak momentum, wide whipsaw drag, and thin leverage carry all tend to
co-occur in the same choppy/no-trend regime, so summing their lows together is not an
unreasonable joint scenario, it may be the *modal* bad year, not a freak tail). Either way, the
document should show its arithmetic or restate the floor honestly — right now it asserts a property
("built additively," "computed from haircut values") that its own printed numbers falsify by
0.5–2.5pp per book. **Fix**: either publish the aggregation method (if not literal min-sum, say so
and show the blend), or lower the stated floors to 15.5–15.7% / 13.5% / 12.0% respectively, or
tighten the component ranges so they actually foot.

---

## 1. Magic-number hunt

The registry's own enforcement mechanism (`config/validator.py::check_provenance`) only fires on a
YAML node shaped `{value: X, tier: Y, source: Z, confidence: W, ...}`. Any numeric parameter stored
as a **bare list or bare scalar** is architecturally invisible to it — walked, but never checked,
because the walker only demands provenance keys when it sees a `value` key at that level. This is
not a hypothetical: counting bare vs. wrapped numeric leaves in the six registry files gives roughly
**38 unenforced numeric parameters against ~49 enforced ones** — the "no magic numbers" CI gate the
design advertises ("Everything here is encoded in machine-checkable form in `config/`... validated
by `config/validator.py`") is auditing well under half the numbers that matter. Concretely, bare
(zero source/tier/confidence/changes_if at the machine level) and never flagged `[A]` in the YAML
itself:

1. **`ladder.yaml budgets.regime_score_blocks`** — `fast_stress: 0.25, trend_tsmom: 0.20,
   macro_credit_block: 0.20, global_cycle: 0.20, valuation_sentiment: 0.10, calendar: 0.05`. This
   is arguably the single most consequential set of numbers in the risk system — it fixes how much
   of the regime score R each ladder block can move — and none of the six weights carries a
   citation, a sweep, or an `[A]` tag; DESIGN §5.1 just asserts them as "budget caps per §4.1."
   They sum to a satisfying 1.00 (checked), but the *split* (why fast-stress gets 5x calendar's
   weight, why macro-credit and global-cycle tie at 20% each) is exactly the "20%, 10%, 200-DMA"
   pattern CONTRACT §6 names by name — plausible round numbers with no derivation, presented as
   fixed points rather than a swept grid. **Fix**: wrap each as a `{value:[lo,hi], tier:C,
   source:"design judgment — no derivation", sweep:[...], changes_if:...}` node, or actually sweep
   it and report CSCV/deflated-Sharpe sensitivity to the split, per CONTRACT §9.6's own trial-ledger
   requirement (the *block budget split itself* is a swept parameter that should be in the trial
   count and currently is not).

2. **`risk.yaml regime_buckets`** (R1–R4 `leverage_range` / `hedge_ratio_range`, 8 numbers) and
   **`sleeves.yaml gold.floors` / `gold.ceilings_total`** (6 numbers) — same pattern: DESIGN prose
   gives some rationale (§5.1 table, §6.5 "[X mechanism / C sizing]"), but none of it is
   machine-encoded, so a future edit to these ranges (which gate the drawdown-ceiling arithmetic
   and the 50%-of-mandate gold cap respectively) would sail through CI with zero provenance check.
   The R4 bucket in particular is the one DESIGN.md brags was *caught and fixed* by the CI's
   worst-case arithmetic (§5.1 footnote) — yet the bucket's own leverage/hedge ranges are stored in
   a shape the provenance walker cannot see. The catch that did happen (line 156–165 of
   validator.py) is a numeric identity check, not the provenance-completeness check; they are
   different mechanisms and only one of them is actually exercised here.

3. **`books.yaml` per-book `leverage_avg_target`, `name_count_floor`, `name_count_ceiling`,
   `avg_min_weight`, `dd_target`, `net_cagr_band`** — 5 parameters × 3 books = 15 more bare numbers.
   DESIGN §7.2 *does* cite real literature for name-count floors/ceilings (Evans-Archer/Statman,
   Bessembinder, Cohen-Polk-Silli) — the sourcing exists in prose — it simply never made it into
   the registry in checkable form, so a change to, say, the aggressive floor from 15 to 10 next
   quarter would not trip any CI rule requiring it to re-cite Bessembinder.

4. **The most safety-critical instance: `0.38` hardcoded directly in `validator.py` line 162**
   (`worst = eff_beta_r4 * 0.38 + hi(gf)` — "COVID-size fall reached while in R4"). This is not a
   YAML value at all; it lives in Python, completely outside the file set `check_provenance` walks.
   It is the single number that decides whether the R4 bucket passes the drawdown-ceiling
   worst-case check — and it has no `source`/`tier`/`confidence`/`changes_if` anywhere, no sweep, and
   would not even show up if someone added a stricter provenance linter over the YAML files, because
   it isn't in a YAML file. (The value itself is defensible — it is the actual 2020 Nifty drawdown
   from DESIGN §5.6's episode table — but a defensible number hardcoded outside the registry is
   still a violation of the design's own stated architecture, and the next person to "improve" the
   validator could change it silently with no diff-reviewable trail.) **Fix**: move it into
   `risk.yaml` as a provenanced `worst_case_fall_scenario` parameter (source: 2020 episode, tier B,
   changes_if: "next qualifying episode exceeds 38%, e.g. a slower 2008-style −60% that spends more
   time in R3/R4 — see §3 of this report").

5. **Minor**: `sleeves.yaml f_kelly` is labeled "eighth-to-third Kelly" (i.e. 0.125–0.333) but the
   stored range is `[0.15, 0.35]` — the low end doesn't match its own name (0.15 vs. 1/8=0.125, a
   20% relative gap). Small, but it is exactly the kind of drift that happens when a plausible-
   sounding heuristic name gets attached after the range was already chosen for other reasons.

6. **The universe-split rank cutoffs (300 / 150 / 80) are magic numbers hiding inside prose
   strings.** `books.yaml universe_full_conviction: "ranks 1-300"` (aggressive), `"ranks 1-150"`
   (moderate), `"ranks 1-80"` (conservative) are never expressed as numeric `value` fields at all —
   they are substrings inside free-text descriptions, so nothing can ever validate them against the
   ADV table they were derived from, and nothing forces them to move when `costs.yaml`'s
   `adv_by_rank_bucket_cr` (explicitly `PROVISIONAL`) is replaced with live data in Phase 0. A
   provisional table silently upstream of three frozen-looking rank cutoffs is a real risk: the
   design's own capacity arithmetic (§2.1, §9.2) is only as good as a table it labels not-yet-real,
   and the numbers downstream of it aren't wired to change automatically.

---

## 2. §10 decay ledger — the weakest three survival arguments

Of the ~18 entries, most genuinely earn their tier (the design is unusually disciplined about
zeroing out 1-month reversal, Stage-2, and treating vol-targeting's DD-reduction separately from
its return claim — real examples of doing this right). Three do not hold up on inspection:

**(a) Quality's pledge/RPT junk terms — "unhaircut until tested."** `sleeves.yaml factor_book.
quality` haircuts imported QMJ at 25–35% but explicitly leaves the India-specific pledge-intensity
and RPT-flag terms at **zero haircut**, justified by D12/D02's "mechanism-based signals survive
crowding almost by definition." But zero haircut is not the same claim as "survives crowding" — it
additionally asserts *no estimation-uncertainty discount* for a component with no measured effect
size anywhere in the dossier base: D02/D12 report a case *count* (~10–15 pledge-cascade episodes,
2015–23) and a mechanism story, never an AUROC, an information coefficient, or even a sign-tested
return spread. A signal with a plausible story and zero fitted magnitude should carry *more*
uncertainty discount than a signal with a measured-but-decaying one, not less. As written, this is
the clearest case in the whole ledger of a component earning full weight on narrative alone — the
contract's forbidden move ("it backtests well") inverted into "it hasn't even backtested, but the
story is good, so no haircut."

**(b) 52-week-high — a single US paper wearing a Tier-B cross-country coat.** CONTRACT §4 defines
Tier B as "4–30 observations, **or n<4 with ≥10 cross-country analogues**." D01 §3 cites exactly
one study for this specific signal (George-Hwang 2004, US-only) and states plainly "No India-
specific study found." There are not 10 cross-country analogues on record for 52-week-high
specifically in this dossier base — the tier assignment borrows the *general* momentum literature's
credibility for a *specific* sub-signal that has one citation to its name. The ledger's own
falsifier column reads "India test (none exists)" — that is not a falsifier, it is an admission
that the haircut (20–30% `[A]`) was picked with no India evidence to falsify against at all. This
survives on citation-adjacency, not on the ≥10-analogue bar the contract itself sets for that tier.

**(c) Momentum (India) — the haircut-band choice contradicts the dossier's own cited decay
evidence.** D01/§10 pick the *low* end of McLean-Pontiff's range (25–35%, near their 26%
"out-of-sample" figure) rather than moving toward 58%, reasoning that Jacobs-Müller shows
post-publication decay is "largely a US phenomenon." But the same paragraph cites Sharma-
Subramaniam-Sehgal (2021) finding India momentum becoming "increasingly risk-model-explained" over
2005–2016 — which is precisely the signature of capital arbitraging a known factor into a
priced-in style tilt, i.e. the mechanism MP's *higher* haircut describes. The dossier calls this "a
softer, real form of decay" and then still books the *smaller* haircut. Given (i) AJV's own sample
ends in 2014, well before India's own momentum smart-beta products existed at scale (see §4 below),
and (ii) this is the aggressive book's flagship return engine at 200–350% turnover, choosing
optimism over the disconfirming evidence already in hand is the weakest reasoning step in the
ledger, even though the final number (25–35%) is not indefensible in isolation.

*(Honorable mention, not in the top three because it discloses its own weakness rather than hiding
it: L7 issuance/sentiment's "26–58% band as placeholder" is an explicit non-derivation — honest, but
it still sizes the special-sits sleeve via the L7 froth flag, so a fully unresolved 32pp-wide
haircut band is load-bearing for capital allocation today.)*

---

## 3. Crowding blind spots

The design explicitly builds an AUM-growth-rate crowding trigger for **low-vol only**
(`sleeves.yaml factor_book.low_vol.decay: "AUM-growth-rate crowding trigger"`) and a rising,
annually-re-estimated haircut for **index inclusion/exclusion only**
(`special_situations.events.index_inclusion_exclusion`). Momentum, value, and quality — three of
the four sleeves that carry the moderate and aggressive books' actual return — have **no analogous
crowding monitor**, despite D02 §3 explicitly documenting a live, dated crowding event that hit all
three factors together: "a 'quant unwind' in mid-2025 driven partly by quality/low-vol/AI-momentum
crowding unwinding together." The design's own cited evidence names momentum as part of that
episode, yet the §10 momentum row's falsifier is only about the post-2015 point-in-time sub-sample —
it never references the 2024–25 unwind D02 itself flags. That is an internal inconsistency, not
just an omission: the evidence that would motivate a momentum crowding trigger is sitting in the
dossier the design already cites for a different sleeve.

More broadly, the design never engages with the fact that its factor constructs are not exotic —
NSE-family indices tracking near-identical constructs (a momentum-composite index, a quality index,
a value index, a low-vol/alpha index) already exist and already carry meaningful, growing India
index-fund/ETF AUM. The moderate book (₹1,000–2,500cr, factor-book engine) is proposing to run
100–160% turnover largely on the same value/quality/momentum tilts that a fast-growing set of
smart-beta products in the same universe (Nifty 500 / Nifty 750) already implement at scale — and
the design nowhere sizes or bounds this specific capacity/crowding risk the way it does, carefully,
for index-inclusion-effect capacity ("India today ≈ US 1990s on passive share"). If that framing is
right for index-effect capacity, the same "India today, more crowded tomorrow" logic almost
certainly applies to momentum/value/quality smart-beta AUM too, and the design should say so with an
equivalent trigger rather than leaving it implicit only for low-vol.

Separately: the regime/cycle-timing side (L9 global financial cycle, L10 credit block) runs on
widely public series (FRED VIX/dollar/DFII10, RBI DBIE) that every macro desk and global-macro fund
watches, and the "combine multiple predictors" methodology it cites (Rapach-Strauss-Zhou) is itself
now common practitioner knowledge, not a private edge. The design never argues why its specific
combination of public signals should have a durable edge over the many other well-resourced desks
reading the same public tape — it implicitly treats the *regime-reading* side as if this desk were
early or alone there too, with no equivalent to the momentum/value AUM-crowding gap just described,
but for macro-timing capital rather than factor capital.

---

## 4. 2026–2036 forward-looking parameter staleness

Checked against the registry's own `changes_if` discipline (present and good in most places:
funding_rate re-verified quarterly, statutory rates re-checked every Budget with an expiry date,
index-inclusion haircut re-estimated annually, long-wave triggers on ≥4-quarter regime reversal).
Gaps found:

- **T+0 settlement — a complete blind spot.** India has been rolling out optional T+0 settlement
  since March 2024 with an explicit glide path toward broader adoption. This bears directly on
  Decision Q3's entire premise (margin funding *on cash names*, chosen over an index-futures
  overlay partly on relative cost/speed grounds in §2.4) and on the futures-vs-cash cost
  differential the design leans on ("futures are ~3x cheaper statutory"). A settlement-cycle
  change of this kind changes financing/margin mechanics for cash positions in ways that could move
  that differential materially over a 2026–2036 horizon. T+0 is not mentioned anywhere in
  DESIGN.md or `config/*.yaml`, and there is no `changes_if` trigger anywhere tied to settlement-
  cycle changes. This is the single largest structural blind spot found in the forward-looking
  sweep, precisely because it attacks the leverage-instrument decision the design treats as settled.

- **Options market-structure risk (SEBI F&O curbs) has no registry trigger**, despite the hedge
  stack depending materially on index futures/options (§5.5) and §15's own verification queue item 8
  flagging "index-derivatives expiry regime details post-SEBI-curbs" as unresolved. SEBI has been
  actively tightening lot sizes, expiry cadence, and margin/true-to-label rules; a further
  structural narrowing of index-derivatives access over the next decade would change hedge cost and
  availability, but no parameter (`option_premium_budget_nav_yr`, hedge-effectiveness ranges) carries
  a `changes_if` tied to regulatory contract-specification changes — only to VRP re-measurement.

- **Momentum/value/quality AUM-crowding has no trigger** (repeat of §3's finding, restated here
  because it is also a *forward-looking* gap specifically: passive/smart-beta AUM in India is
  plausibly the fastest-growing single input to this design's core return engines over 2026–2036,
  and only one of four factor sleeves — low-vol — has a mechanism to notice it happening).

- **SEBI's AI/algo-trading disclosure perimeter for Stage 2 is flagged as a compliance-counsel
  narrative item (§8.5 "[I][V — compliance counsel item]") but carries no registry `changes_if`.**
  Given the pace of SEBI rule-making on AI-in-finance through 2025–2026, a decade-long design
  horizon should encode this as a monitored trigger, not a footnote for someone else to remember.

- **Gold duty policy** has good historical level-break hygiene (2013 hike, Jul-2024 cut both
  flagged as "never fit through") but no forward-looking trigger for the *next* duty change — the
  instruction covers the past, not a monitoring rule for the future.

---

## 5. Stage-2 advisory-only gate — three ways to game it

**(1) Selective logging is unaddressed.** The ledger schema (§8.4) specifies *what* fields a logged
thesis must carry, but nowhere does DESIGN or `sleeves.yaml stage2` require a **fixed-cadence,
mandatory, append-only** logging obligation (e.g. "the structured scorer must log a score at every
Stage-1 rebalance, full stop"). Contrast this with the quant side, where CONTRACT §9 requires
pre-registration *before running* every hypothesis. Without an equivalent commitment for Stage 2, a
sponsor can hit "n≥20 scored theses with BSS>0" (the Rung −1 exit bar) by choosing to log only
theses that are likely to score well — short-horizon, high-confidence, easy "broken-leg" facts —
while quietly not logging harder, more genuinely predictive attempts that might fail. The n-count
would be real, but not representative of the channel's actual skill, and nothing in the design
would catch it.

**(2) Horizon extension is not explicitly forbidden.** Theses log an "explicit horizon" up front and
are scored "at resolution," but the design never states horizons are frozen at logging time. If a
horizon can be quietly lengthened after a thesis starts looking wrong, resolution — and therefore
the Brier score that gates promotion — can be indefinitely deferred or steered, inflating the
apparent hit rate the ladder is supposed to measure honestly.

**(3) Effective-n inflation is named but not operationalized.** §8.2's footnote states "effective-n
must be autocorrelation-adjusted before unlocks count (correlated macro theses are not independent
observations)" — correct in principle, but no estimator, formula, or CI-style check is specified
anywhere in `sleeves.yaml stage2`, unlike the quant side's explicit Newey-West/HAC treatment for τ½
(§11.2). Three separate LLM channels (scorer, red-team, tactical generator) can each log a thesis
about the same underlying event on the same day; the design never says whether the n-count is
per-channel or pooled, nor whether cross-channel correlation is corrected before pooling. Absent a
specified, automatic adjustment, a sponsor motivated to reach the n≥20/n≥50 thresholds quickly can
generate many superficially distinct but highly correlated theses off a handful of real events.

**A fourth, sharper gap found while checking (3): the model-version reset can launder a bad track
record instead of triggering demotion.** `sleeves.yaml stage2.llm_rules`: "model-version change
resets that component's track record to n=0." Demotion (§8.2) triggers on "any window with BSS<0 or
paired IR/DD below baseline." The design never states whether a version swap **also** forces the
current rung back to a probationary state, or whether it only resets the promotion counter while
leaving the currently-held rung (and its authority — up to ≤5pp aggregate NAV at Rung 2) untouched.
As written, a channel drifting toward a bad window under model v1 could be swapped to v2 right
before that window resolves: the n-counter honestly resets to zero (as documented), but nothing in
the text says the *rung* resets too — meaning elevated authority earned under v1's track record
could persist under a brand-new, zero-track-record model version, which is exactly the
"authority-without-evidence" state the whole ladder exists to prevent. **Fix**: state explicitly
that a model-version change forces an immediate rung step-down (or at minimum a probationary hold at
the current rung with tightened caps) until the new version re-earns its own n-floor, not merely
that its promotion counter resets.

---

## Summary — severity-ranked

| # | Finding | Severity |
|---|---|---|
| 1 | §1.1 pessimistic-recombination check: all three books miss their own stated CAGR floor by 0.5–2.5pp; "built additively" claim doesn't foot | **Critical** |
| 2 | `regime_score_blocks` (25/20/20/20/10/5 split) — the risk system's central weighting — has zero source, sweep, or `[A]` tag; not in the trial ledger | **Critical** |
| 3 | ~38 numeric parameters (regime buckets, gold floors/ceilings, per-book name-count/DD/CAGR targets) sit in a YAML shape the provenance CI never inspects — the "no magic numbers" gate covers well under half of what it claims to | **Critical** |
| 4 | Worst-case R4 drawdown check's comfortable 3.7pp margin rests entirely on an "illustrative" (D04, tier C, low confidence) hedge-effectiveness floor of 0.45; breach occurs below he≈0.325, plausible if tail-name lock-limit-down materially drags blended effectiveness down | **Major** |
| 5 | The `0.38` "COVID-size fall" driving the R4 safety check is hardcoded in `validator.py`, entirely outside the registry's provenance mechanism | **Major** |
| 6 | Momentum/value/quality carry no AUM-crowding trigger despite D02's own cited 2024–25 "quant unwind" naming momentum as a participant | **Major** |
| 7 | Quality's pledge/RPT junk terms carry zero haircut on pure narrative, with no measured effect size anywhere in the dossier base | **Major** |
| 8 | T+0 settlement rollout — no mention anywhere, directly threatens the Decision Q3 margin-funding premise and the futures-vs-cash cost differential | **Major** |
| 9 | Stage-2 model-version reset resets the n-counter but the design never states it also resets the held rung — a laundering path around demotion | **Major** |
| 10 | 52-week-high's Tier-B assignment rests on one US citation, not the ≥10 cross-country analogues CONTRACT §4 requires for n<4 | **Minor** |
| 11 | Selective logging / horizon-extension gaming vectors on the Stage-2 ledger — no mandatory cadence, no stated horizon-freeze rule | **Minor** |
| 12 | Universe-split rank cutoffs (300/150/80) are magic numbers embedded in prose strings, downstream of an explicitly PROVISIONAL ADV table, with no wiring to update automatically | **Minor** |
| 13 | `f_kelly` range `[0.15, 0.35]` doesn't match its own "eighth-to-third" (0.125–0.333) label | **Minor** |

Files inspected: `docs/DESIGN.md`, `config/{mandate,books,ladder,risk,sleeves,costs}.yaml`,
`config/validator.py`, `research/CONTRACT.md`, `research/OPEN_QUESTIONS.md`,
`research/dossiers/{01,02,03,08,12}-*.md` §3.
