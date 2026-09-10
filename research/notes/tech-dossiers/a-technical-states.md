# Technical States: All-Time Highs, Stages, Trend, Sector RS, Index Ratios

*Literature dossier, Track T companion (technical states, as distinct from technical
**rules**), 2026-09-10. No web fetches this session — every literature claim is from
training knowledge, unverified against a live source, and carries **[LIT]**; a magnitude
recalled with less confidence than the citation itself carries **[LIT, LOW CONFIDENCE]**;
a citation whose author pairing or venue I cannot stand behind carries **[VERIFY: ...]**
per CONTRACT §12's convention. Desk numbers are quoted verbatim from
`research/register/trial-ledger.md` and marked **[DESK, <entry>]** — none are re-derived
here; per the ledger discipline, bars are never moved after a print. This dossier does not
re-litigate what Track T already killed — it builds on it. Two verdicts bind everything
below: **T-CTRL1** (the Brock-Lakonishok-LeBaron MA rule family, 10 canonical VMA rules
with 0%/1% bands, died 0/10 net of costs — best cells net Sharpe 0.56–0.58 vs buy-hold
0.55, all DSR < 0.95 at n_trials=174) **[DESK, T-CTRL1]**, and **TS1** (monthly own-asset
TSMOM: index k=3 passed the drawdown bar through 2008 — net maxDD 22% vs 47% buy-hold,
1.1pp/yr drag; k=6/k=12 failed; gold passed at all three speeds, k=12 strongest, net
+9.0% vs +8.0% buy-hold, maxDD 34% vs 62%) **[DESK, TS1]**. The question this dossier
builds on — do dead trend **rules** mean trend **states** are worthless — is answered by
the desk's own evidence: no.

## 1. All-time highs and 52-week highs

The academic anchor is **George & Hwang (2004)**, "The 52-Week High and Momentum
Investing," *Journal of Finance* 59:2145–2176 — already verified in this program's
literature base (`docs/cycles/03-momentum-trend.md` Part A.9/Part C) **[LIT]**. Their
central claim, restated precisely: a stock's **nearness to its 52-week high**
(`price_t / max(price over trailing 252d)`) is a *stronger and more robust* predictor of
future returns than the conventional 12-month cumulative-return ranking that defines
classic cross-sectional momentum, and the two do not fully subsume one another **[LIT]**.
Their proposed mechanism is explicitly **anchoring** (Tversky-Kahneman): investors use the
52-week high as a salient reference point and are reluctant to bid a stock past it even
when fundamental news justifies it, so good news near a 52-week high gets underpriced and
corrects slowly upward — a cognitive-anchor story, not a risk-based one **[LIT]**. This
differs from cumulative-return momentum's own leading behavioral stories (BSV98
conservatism/representativeness, HS99 gradual diffusion — both already in this program's
momentum monograph) in one important way: it is a **level-relative-to-a-fixed-reference**
effect, not a **path/speed** effect, which is exactly why it survives as a distinct
signal rather than a relabeling of the same thing (§3 below).

**Buying at all-time highs, honestly.** The lore ("stocks at all-time highs tend to make
new highs") has a real academic cousin but a thinner one than practitioners assume.
George-Hwang's own test window is 52-week-high-based, not literal all-time-high-based;
the index-level ATH case is a different, less-studied, mostly practitioner-produced claim
(return-after-ATH-month studies from index providers/sell-side desks show forward
1/3/12-month returns from ATH months statistically indistinguishable from, or modestly
*better* than, average months) **[LIT, LOW CONFIDENCE — practitioner-grade, not a
peer-reviewed literature]**. The honest read: fear of buying at an index ATH is largely
an availability-heuristic bias, not a documented anomaly running the other way — the
George-Hwang mechanism, if anything, argues underreaction (not overreaction) near a high.

**The ATH-breakout-after-long-base pattern.** The weakest claim in the whole
technical-analysis canon to defend academically — a codification of chart-pattern lore
(Darvas boxes, Weinstein's Stage 2 breakout, O'Neil's "cup and handle") with **no
dedicated, replicated academic literature** isolating "breakout from a long consolidation"
as a variable distinct from plain 52-week-high proximity plus a volatility-contraction
filter, which already captures most of the plausible mechanism. No confident citation
exists for an incremental "long-base breakout" premium; treat it as **already spanned** by
52-week-high proximity (Tier C, pattern-recognition literature) until proven otherwise in
a pre-registered India test.

## 2. Trend/stage frameworks

**Weinstein's four stages — defined precisely, for what is mechanically testable.** Stan
Weinstein's stage-analysis framework (practitioner text, 1988) **[VERIFY: exact title/
year — recalled as *Secrets for Profiting in Bull and Bear Markets*, 1988]** partitions a
security's (or index's) price history into four recurring stages defined jointly by
**price-vs-moving-average** and **moving-average slope**:

| Stage | Price vs (30-week) MA | MA slope | Interpretation |
|---|---|---|---|
| 1 — Basing | Chops around a flattening MA | ≈ 0 | Accumulation after a decline; no trend |
| 2 — Advancing | Above, breaking out above the MA | Rising | The only stage Weinstein wants long exposure in |
| 3 — Topping | Chops around a flattening MA (from above) | ≈ 0, decelerating | Distribution after an advance |
| 4 — Declining | Below, breaking down below the MA | Falling | Markdown; avoid or short |

Mechanically, this is a **2×2 (or, with the "flattening" case, a 2×3) quadrant on {price
above/below MA} × {MA slope rising/falling/flat}** — precisely the "price-vs-MA ×
MA-slope quadrant" the brief asks to define, and precisely the construction this desk's
own **F2-index / F7a** phase-quadrant work already builds and tests, independently of
Weinstein's name (the phase-quadrant coding in `research/OPEN_QUESTIONS.md` — {recovery,
boom, slowdown, downturn} on {level, velocity} — is the identical mathematical object
applied to a macro state rather than a single price series) **[DESK, phase-quadrant
framework, per OPEN_QUESTIONS.md and F2-index/F7a]**. Weinstein's stage framework is
therefore *not* a new mechanical object requiring new machinery — it is the same quadrant
construction the desk has already pre-registered, tested, and partially killed. **F7a**
found that at a matched high-percentile state level, forward 63-day returns were
statistically flat between the "rising" and "falling-from-high" quadrant codings (D median
+5.62% vs U +5.67%, Mann-Whitney p=0.653) — direction added nothing once level was held
fixed **[DESK, F7a]**, a direct strike against "Stage 2 is where you want to be, Stage 4
is where you want to exit" *read as a return-timing rule*. What F7a does **not** strike
down is the **risk** half: **F2-index**'s bounded partial run found a state-percentile
trigger (a Weinstein-flavored composite, not an identical construction) at its most
conservative setting (0.80 percentile, "any leg confirms") improved deep-episode (GFC,
COVID) maximum drawdown by 5.6–8.4pp at 0.56–1.83pp/yr of full-period drag — 3 of 18 grid
cells supportive **[DESK, F2-index]**. Stated once, for the rest of this dossier: **a
Weinstein-style stage/quadrant reading of an index earns no defensible claim on forward
RETURN direction on this desk's own evidence, but a state built the same way
(percentile-based, not a fixed MA rule) has a narrow, real claim on forward drawdown/vol**
— the "states as risk states, not return states" distinction the brief asks to reconcile.

**Faber's 10-month MA and its post-publication record.** Mebane Faber's widely circulated
paper — commonly cited as Faber (2007), "A Quantitative Approach to Tactical Asset
Allocation" **[VERIFY: exact venue/date — recalled as a practitioner/SSRN paper, first
circulated ~2006–07, periodically updated]** — finds a simple rule (hold an asset class
only when price is above its trailing 10-month SMA, else cash), across five asset classes
back to the 1970s, delivers **equity-like returns with materially lower volatility and
drawdown**, avoiding the worst of 1973–74, 2000–02, and 2008 **[LIT]**. The construction
is identical in form to this program's own TSMOM/L4 signal and the closest T-CTRL1 rule
(VMA(1,200) ≈ a 10-month SMA) **[DESK, T-CTRL1 cross-reference]**. The honest
complication: practitioner follow-ups broadly report the DD-avoidance property surviving
out-of-sample (2008, 2020, 2022) while the **return** edge over buy-and-hold has thinned
and, in some updates, is close to a wash after whipsaw costs **[LIT, LOW CONFIDENCE — no
specific peer-reviewed post-2010 replication with a numeric decay figure can be cited
here; this is a directional read of practitioner commentary]**. That pattern — DD
protection persists, alpha does not — is *exactly* this desk's own TS1 finding on the
index leg (k=3 passed on drawdown, never proposed as a return rule) **[DESK, TS1]**, and
is why this dossier treats Faber's construct as corroborating, not contradicting, the
desk's own printed graveyard.

**MOP2012 TSMOM.** Already the desk's own L4 seat's theoretical foundation
(Moskowitz, Ooi & Pedersen (2012), *Journal of Financial Economics* 104:228–250, and Hurst,
Ooi & Pedersen (2017), a century of trend evidence back to 1880 showing positive returns in
every decade and strong performance in 8 of the 10 worst 60/40 drawdowns) **[LIT — both
already verified in `docs/cycles/03-momentum-trend.md` A.6]**. TS1 is this desk's own
India/gold implementation of exactly this construct, and its result (index k=3 only, gold
all three, strongest at k=12) is a genuine, if narrow, India-consistent replication —
narrower than MOP2012's 58-instrument, 1965–2009 breadth, and explicitly scoped as a
**regime seat**, never a return sleeve **[DESK, TS1]**.

**The BLL line and its out-of-sample failure — reconciled with T-CTRL1.** Brock,
Lakonishok & LeBaron (1992), "Simple Technical Trading Rules and the Stochastic Properties
of Stock Returns," *Journal of Finance* 47(5):1731–1764, found MA-crossover and
range-breakout rules on Dow Jones data 1897–1986 produced returns with statistically
significant edges over a random-walk null under several bootstrap specifications **[LIT]**
— the paper T-CTRL1 directly, modernly replicates. **Sullivan, Timmermann & White (1999)**,
"Data-Snooping, Technical Trading Rule Performance, and the Bootstrap," *Journal of
Finance* 54(5):1647–1691, is the decisive rebuttal **[LIT]**: applying White's Reality
Check (a joint bootstrap across the full rule universe considered, not each rule judged in
isolation) to BLL's rule set plus thousands of variants, the result does **not** survive
correction for implicit multiple testing — the BLL edge was a data-snooping artifact, and
extending the sample forward (to the early 1990s) makes even the uncorrected edge
disappear **[LIT]**. This is the direct academic precedent for T-CTRL1's own
deflated-Sharpe design (n_trials=174, DSR<0.95 for all 10 rules): **T-CTRL1 runs an
STW1999-style correction on India data three decades later and gets the same answer** —
0/10 survivors **[DESK, T-CTRL1]**. The reconciliation the brief asks for: STW1999 killed
BLL-as-a-return-rule on a joint-test basis; T-CTRL1 killed it again on India data with a
modern deflated-Sharpe correction; and **this desk's own T2** (trend-of-a-slow-macro-state
incremental to level — NIFTY next-month return on Kilian-index level and 12-month
trend-sign; trend beta +0.33%/mo at NW t=+0.48 against a bar of |t|≥2, level itself inert
at t=−0.54) found **no surviving return-timing content in "trend of a state," at either
the fast band (F7a) or the slow band (T2)** **[DESK, T2]**. None of these three kills touch
whether a **percentile-based state** (not a fixed-window MA crossover) ranks forward
**risk** — F2-index's 3/18 supportive cells and TS1's DD-bar passes say a narrow yes there.
The split the literature already names — **trend as a risk-premium/crash-protection
instrument** (Hurst-Ooi-Pedersen's "crisis alpha," Barroso-Santa-Clara vol-scaling) versus
**trend as an unconditional alpha rule** — is exactly what BLL/STW1999/T-CTRL1/T2/F7a test
on the losing side, and what F2-index/TS1 pass on the winning side.

## 3. Momentum vs trend vs 52-week high — how the three differ and overlap

Formally distinct constructions: **cross-sectional momentum** ranks a stock's return
**against every other stock at the same date** (self-financing, near-zero beta by
construction); **time-series momentum (TSMOM)** conditions a position on **its own
trailing sign alone**, no cross-sectional reference, time-varying non-zero market beta;
**52-week-high proximity** is neither a relative-return rank nor a sign-of-trend rule but
a **level relative to a fixed anchor** (this asset's own recent extreme), deliberately
orthogonal in construction to both — a stock can sit at 90% of its 52-week high while
ranking anywhere from top to bottom decile on trailing 12-month return. The paper usually
invoked for the separation question is George & Hwang (2004) itself, which nests both
variables in one regression and shows 52-week-high proximity **subsumes** the return-based
momentum coefficient in their US sample, not the reverse **[LIT]**; a sometimes-cited
follow-on literature (candidate authors recalled loosely as **Gulen, Huseyin & Petkova,
Ralitsa**, pairing unconfirmed) extends the separation question internationally and to
volatility-conditioning **[VERIFY: author pairing and findings uncertain]**.

This program has its own direct, real-data answer, and it is the one to lead with:
**N4a**, the survivor-panel structure test of 12-1 momentum rank vs 52-week-high-proximity
rank, found mean monthly cross-sectional Spearman rho of **0.519** (range −0.17 to 0.88)
and top-decile name overlap of only **19%** — a clear **complement, not a redundancy**
verdict (the pre-registered bar was rho ≥ 0.80 for "redundant") **[DESK, N4a]**. This
directly supports L3's existing rank-blend design (12-1 + 6-1 + 52-week-high are not
double-counting the same information). The one part of N4a's own registered prior that
**failed** is instructive and must not be silently dropped: George-Hwang's mechanism
predicts the two signals should **diverge** specifically in post-crash rebounds (momentum
chases the bounce; 52-week-high proximity, anchored to a now-distant pre-crash peak, does
not) — N4a's test, conditioned on high-**volatility** months rather than post-trough
rebound windows, found the **opposite**: rho **rises** in high-vol months (0.623 vs 0.507
in calm months) **[DESK, N4a]**. The desk's own honest read: during a crash itself, both
signals compress toward "who fell least," which is not the same conditioning window as a
post-trough rebound — the mis-specified window is recorded, and the true divergence
question (do the two signals pick genuinely different names in the 3–12 months *after* a
trough, not *during* elevated volatility) remains open and is a natural India pre-
registration once the survivor panel or a PIT successor is available.

## 4. Sector relative strength / rotation

**Academic anchor.** Moskowitz & Grinblatt (1999), "Do Industries Explain Momentum?"
*Journal of Finance* 54(4):1249–1290, found that a large share of individual-stock
momentum's profitability is attributable to **industry momentum** — buying stocks in
recently-strong industries and selling those in recently-weak industries earns a return
comparable to, and largely subsuming, standard individual-stock momentum once industry
effects are controlled for, with the industry component more robust and less prone to the
January reversal that plagues individual-stock winner/loser portfolios **[LIT]**. This is
the direct academic basis for treating sector-level relative strength as a *first-class*
signal family, not a derivative or diversification play on stock-level momentum.

**Practitioner RS/rotation evidence and its decay.** The broader "sector rotation over the
business cycle" literature (cyclicals lead early-recovery, defensives lead late-cycle/
recession) is heavily practitioner-produced (Fidelity, S&P/Dow Jones sector-cycle
playbooks) with the same McLean-Pontiff-style decay concern as any publicized signal,
compounded by a specific measurement problem: rotation-over-the-cycle claims are almost
always stated **contemporaneously with the identified phase**, not as a tradable lead —
precisely the gap this desk's own FUN-D1/FUN-D3 results expose below. No confident,
replicated academic magnitude for "RS-based sector rotation" decay exists to cite at [LIT]
strength; treat the practitioner playbook as Tier C, directional-only, pending a
real-time-conditioned test.

**The desk's own India print — and it inverts the textbook.** **FUN-D3** (India sector ×
market-cycle layer, one-way, survivor panel 2012–2021, states built from NIFTY-vs-12-month-
MA × India-VIX expanding-percentile ≥/< 0.60 — a state construction, not a return rule)
tested exactly the rotation-after-identified-state trade the practitioner literature
describes, and it **failed as registered**: in RISK-OFF states, defensives (FMCG/PHARMA/
IT) **lag** forward 21-day relative returns (DEF −1.76%, PHARMA worst at −2.07%, IT
−1.86%) while cyclicals and financials **lead** (+0.57%/+0.69%, NBFC best at +1.73%),
consistent in both the 2012–16 and 2017–21 era-halves **[DESK, FUN-D3]**. The
reconciliation with the desk's own **SEC-D6** crisis-safety ordering (defensives
outperforming — but SEC-D6 measured drawdowns *during* crisis episodes) is clean:
**defensives protect capital while the state is unfolding; by the time the risk-off state
is identifiable and tradable, the rebound in previously-hammered cyclicals is already the
better forward bet** **[DESK, FUN-D3]** — the sector-level instance of FUN-D1's own "buy
the identified trough, never the identified boom" finding **[DESK, FUN-D1
cross-reference]**. One further one-way fact: PSU banks were the chronic worst basket in
both CALM-UP and CALM-DOWN and merely flat in RISK-OFF — **state-independent**
underperformance 2012–21, not a rotation signal **[DESK, FUN-D3]**.

**What an honest India sector-RS design needs when the data lands.** The NSE sectoral
total-return indices (IT/Pharma/FMCG/Bank/Auto/Metal/Realty/Energy, daily, 2005–present)
are a named Priority-1 runsheet row, vault destination `ingest/vault/index_sector/`,
explicitly gated to **principal-machine** pull (NSE is blocked at this environment's
proxy) **[DESK, RUNSHEET.md]**. On arrival, this unblocks **FUN-D3 FULL**
(survivorship-free — the partial's biggest caveat is the 2012–2021 survivor-panel
construction, which cannot see names that delisted mid-sample) and the SEC-D5 India analog
**[DESK, RUNSHEET.md]**. Three designs to pre-register now: (i) a genuine 12-1/6-1
industry-momentum rank (Moskowitz-Grinblatt form) across 8 sectors, distinct from
FUN-D3's market-cycle-state framing; (ii) FUN-D3's state construction re-run on the full
TR history, retiring the one-way caveat; (iii) a real-time-conditioned rebound-window test
(post-trough, not merely high-VIX) — the correct George-Hwang-style conditioning N4a's
stress-window flagged as mis-specified (§3) — to test whether "defensives lag the
identified rebound" is a genuine timing edge or, like T3, restates known diversification
arithmetic.

## 5. Index ratios as signals

**Equity/gold ratio — the desk already killed the naive rotation form.** **T3** tested
exactly this: a relative-momentum rotation between NIFTY and INR-gold (the "Antonacci dual
momentum" construction), at both k=3 and k=12 month lookbacks, against the two single
assets and a static monthly-rebalanced 50/50 blend. Both cells **failed**: at k=3, net
Sharpe 1.14 vs INR-gold alone at 1.19 and the 50/50 static at 1.17 (no edge, and the
single-asset INR-gold Sharpe of 1.19 over 2007–2026 — USD gold return plus INR
depreciation — "carried the era" on its own) **[DESK, T3-k3]**; at k=12, net Sharpe 1.13,
and the prior's drawdown-protection half was **wrong**, not merely unconfirmed — in the
k=12 window the 50/50 static's maxDD was 11% vs the rotation's 18%, the static blend
dominating on *both* axes **[DESK, T3-k12]**. The mechanism read the desk booked: "a
relative rule forces one speed onto two assets that TS1 showed trend at different speeds
(3m equity / 12m gold), and loses both — the static blend's diversification arithmetic
wins again" **[DESK, T3-k12]**. Any index-ratio-timing design for equity/gold must clear
this bar, not merely propose a different lookback; the desk's own printed graveyard here
is now two-for-two against relative-momentum framings of this specific ratio.

**Large/small ratio.** The desk's own **SC-D1** (US firm panel, 1999–2019, in-sample
flagged, 240 overlapping months, no real-time claim) found the small-vs-large Pb
valuation spread **orders** next-12-month relative return: top-tercile-minus-bottom
spread +16.05pp, correlation −0.69 at 36 months, robust to a Pe-based repeat
**[DESK, SC-D1]** — a valuation-*level* ratio, not a trend ratio, and an in-sample
existence test, not yet a tradable rule. Consistent with the "trend-of-a-ratio dies,
level-of-a-ratio survives longer" pattern this dossier keeps finding: **SC-D2** showed
SMB's own trailing-momentum is **era-fragile** — positive pre-1981 (+7.96), flipping to
near-zero/negative post-1981 (−0.4 to −0.7), the desk's third recorded instance of this
fragility pattern **[DESK, SC-D2]** — and **SC-D3** found the India post-bear-year
smallcap rebound the US literature predicts actually **inverts** (−12.31% vs −0.20%, a
−12.11pp gap), booked as a Tier-C rule against smallcap adds for 12 months after a bear
year, with only a 36-month "winter rebound" (+10.32, a watch, not a design) surviving
**[DESK, SC-D3]**.

**Cyclicals/defensives ratio as a regime read.** No dedicated desk trial exists yet on
this ratio specifically as a standalone index-level signal (as opposed to the sector-level
relative-return read FUN-D3 already ran, §4) — the academic literature on cyclicals-vs-
defensives ratios as a business-cycle indicator is practitioner-dominated in the same way
sector rotation is generally, and should be treated with the identical [LIT, hedge]
caveat: directionally plausible (the ratio itself is close to a real-time business-cycle
read, since "cyclical outperformance" is close to tautologically a recovery symptom), but
with no confident academic magnitude to cite and FUN-D3's own finding — that by the time a
state is *identifiable*, the rotation trade the ratio would suggest has already missed its
best window — as the most relevant desk caution against treating the ratio's level as an
actionable forward signal rather than a coincident one.

## 6. Leverage as a technical/positioning input

**Margin debt and market tops — the evidence quality, honestly.** The weakest-evidenced
claim in the canon after the ATH-breakout pattern (§1). The folklore is specific
(aggregate margin debt growth outrunning the index, or margin debt/GDP at a cycle
extreme, as a leading top indicator) and constantly repeated in practitioner/press
commentary, but the confirmed academic literature is thin and mostly **contemporaneous/
correlational, not predictive out-of-sample**: margin debt reliably **rises with** the
market — a coincident leverage-cycle fact, consistent with this program's own DB-battery
finding that debt tracks cycle phase rather than causing it — far more robustly than it
leads a top with any usable warning window **[LIT, LOW CONFIDENCE — no specific,
replicated paper establishing margin debt as predictive (not coincident) with a stated
lead time can be cited here; Hardouvelis (1988/1990) on Fed margin requirements and
volatility is a genuine adjacent citation but tests a different variable]**. Any India
design using leverage as a positioning input should be built and sized as a
**contemporaneous leverage-cycle confirm** (a state variable, per CONTRACT §4), not a
timing trigger, absent a stronger citation than exists in this program's base.

**India margin funding data — honest availability.** CONTRACT working conventions already
settle the leverage **instrument** question for this desk: margin funding on cash names
(MTF — Margin Trading Facility), not index futures, with `funding_rate` a first-class
config parameter and the leverage-state function required to clear expected-return >
funding-rate **[CONTRACT §10 / OPEN_QUESTIONS Q3]**. `OPEN_QUESTIONS.md` Q3 records the
honest data gap directly: the actual funding cost available to this desk is still
principal-to-confirm, bracketed between **retail MTF (~9–12%)** and **prop/internal
funding (near MIBOR)** **[DESK, OPEN_QUESTIONS.md Q3]** — a wide, materially different
range for the leverage-state function's central bar. Broker-level or exchange-aggregate
MTF **outstanding-balance** data (the closest India analog to "aggregate margin debt") is
disclosed in places (NSE/BSE publish aggregate MTF/pledge figures with a lag) but is
patchy, inconsistently defined across brokers and periods, and not to this desk's
knowledge a free, continuous, point-in-time series comparable to the US FINRA/NYSE margin
debt series academic and practitioner margin-debt studies use — an honest "mostly paid or
patchy" verdict, and a Priority-1-adjacent data gap this dossier flags for the runsheet
rather than a data source this desk currently has.

## Edge candidates for this desk

1. **TSMOM as a regime/DD-control seat (index k≈3, gold k≈12), already booked.**
   Mechanism: sign-of-trailing-return de-risking, MOP2012/HOP2017-consistent, crisis-alpha
   framing not alpha-generation framing **[LIT]**. Magnitude: index maxDD 22% vs 47%
   buy-hold at 1.1pp/yr drag through 2008; gold net +9.0% vs +8.0% buy-hold, maxDD 34% vs
   62% **[DESK, TS1]**. Kill condition: any pre-registered future re-test showing the
   index k=3 cell's drag exceeds the 2.0pp/yr design outer bound in an out-of-sample India
   window, or a re-run at a different k passing where k=3 previously failed without a
   stated mechanism change. Data needed: already vaulted (NIFTY daily, gold monthly);
   no gap.

2. **Percentile-state (not fixed-MA) drawdown triggers, F2-index's narrow surviving
   shortlist.** Mechanism: a state variable ranking forward *risk*, not return — the
   Barroso-Santa-Clara/Daniel-Moskowitz "trend as crash-protection" literature, not the
   BLL "trend as alpha" literature **[LIT]**. Magnitude: 3/18 grid cells supportive,
   5.6–8.4pp deep-episode DD improvement at 0.56–1.83pp/yr drag **[DESK, F2-index]**. Kill
   condition: full F2 (three legs, book-level costs, walk-forward) failing to reproduce
   the shortlist's DD-improvement-to-drag ratio out of the bounded partial's sample; F7a
   already forecloses any read of this as a return-timing signal. Data needed: already
   vaulted; the full-F2 walk-forward is machinery, not a data gap.

3. **Industry/sector momentum on the full NSE sectoral TR history (Moskowitz-Grinblatt
   form), once vaulted.** Mechanism: Moskowitz-Grinblatt (1999) industry momentum,
   distinct from and more robust than stock-level momentum in the US evidence **[LIT]**.
   Magnitude: not yet estimable for India — FUN-D3's partial found the *state-conditioned
   rotation* form fails/inverts (defensives lag the identified risk-off rebound by −1.76
   to −2.07pp/21d) **[DESK, FUN-D3]**, but a genuine 12-1 industry-rank construction is
   untested. Kill condition: industry-rank momentum failing to beat the stock-level L3
   composite net of costs, or failing the same STW1999-style joint bootstrap correction
   T-CTRL1 already applied. Data needed: NSE sectoral TR indices, daily, 2005–present
   (RUNSHEET, principal-machine, Priority-1).

4. **Small/large valuation-ratio level (not trend) as a relative-return timing context.**
   Mechanism: value-spread factor timing, Asness/Cohen-Polk-Vuolteenaho-style multi-year
   horizon support **[LIT, hedge — factor timing is a notoriously weak literature
   overall]**. Magnitude: SC-D1's US in-sample print, +16.05pp T1-T3, corr −0.69 at 36m
   **[DESK, SC-D1]** — not yet a real-time claim. Kill condition: an out-of-sample or
   purged re-test failing to reproduce the monotone relation, or an India replication
   reversing sign the way SC-D3 already reversed the US smallcap-rebound sign. Data
   needed: NSE large/small index P/B or P/E history (a runsheet row, 2021 splice caveat
   already named).

## India data requirements (summary)

- **NSE sectoral TR indices**, daily, 2005–present (IT/Pharma/FMCG/Bank/Auto/Metal/
  Realty/Energy) — Priority-1, `ingest/vault/index_sector/`, principal-machine pull;
  unblocks FUN-D3 FULL and any genuine industry-momentum design (§4 above).
- **NSE large/small index valuation series** (P/B, P/E) — a named runsheet row (2021
  splice caveat), needed for any India replication of SC-D1's large/small ratio-level
  design.
- **India MTF (margin funding) balances and rates** — patchy/paid at aggregate level;
  the actual funding-rate bracket (retail ~9–12% vs prop/internal near MIBOR) is still
  principal-to-confirm per `OPEN_QUESTIONS.md` Q3, and is a harder, more basic gap than
  any margin-debt-as-signal question (§6).
- **A point-in-time, survivorship-free NIFTY 750 daily panel** longer than the current
  2012–2021 survivor window — every sector-state and 52-week-high result here (N4a,
  FUN-D3) is flagged one-way or partial specifically because it is not yet available;
  the same PIT gap the fundamentals track already carries, not a new one.
- No further India VIX, gold, or NIFTY series are needed beyond what is already vaulted
  for this dossier's edge candidates.
