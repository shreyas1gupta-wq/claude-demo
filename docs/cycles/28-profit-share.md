# The Profit-Share Cycle — Candidate Monograph (Atlas 2.15, H56; BAND 2 CLOSES)

**Version 1.0 · 2026-09-02 · Ionic quant desk (principal: gaurav@ionic.in) · governed by research/CONTRACT.md**

**Verdict up front:** H56 is instrumented as an EXTRAPOLATION GOVERNOR for the valuation block
(with L8), Tier C, reduce-only — and the design was SHARPENED BY A FAIL: the tradable slogan
("margins must come down") is measurably wrong on 114 countries; what the data licenses is
"what goes up rises slower".

**Headline results (PA1 + PS1–PS3, pre-registered):**
- **PS1 PASS at FC1-class breadth:** 85% of 114 countries show the capital-share level
  correlating negatively with its own next-decade change (nan-robust median −0.42) —
  relative mean reversion is among the broadest regularities in the register.
- **PS2 FAIL (+6pp vs +15pp):** top-quintile extremes yield outright declines only 27% of the
  time vs 21% unconditional — reversion operates AROUND A RISING TREND (the global labor-share
  decline); high shares predict SMALLER RISES, never falls. No decline forecast exists in
  H56's interface, and PS2's print is the reason.
- **PS3:** India's macro capital share stood at its **81st own-history percentile in 2019 —
  BEFORE the 2019-24 listed tripling** — framing the atlas's live question (how much of
  projected earnings growth silently assumes the share keeps rising?) from an already-high
  base, with the macro-vs-listed caveat attached to every use.

**Band 2 closes with this entry.** The coda's ledger: 13 entries, zero unplanned seats, five
labels retired with prints, three candidates instrumented (H54/H55/H56), one seat calibrated
(L6), two modules shipped, the frequency sweep + the ENSO control group as doctrine.

**Assembled from:** partAB-theory-record.md (Kalecki derived; the Grantham-not-Montier quote
correction; Smolyansky's tailwind decomposition; India's arc verified) · profitshare-RESULTS.md
· partCDEFH.md.

---

# PART A + B + C + D — Kalecki, the reversion record, India's arc, the H56 design, the Band-2 coda

# The Profit-Share Cycle — Theory and the Record, Argued in Full

Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in) · v1.0 · 2026-09-02

Parts A & B (this program's universal lettering; internally structured A–D per this dossier's own
brief) · Atlas entry **2.15** (`docs/CYCLE_ATLAS.md` line 91, Band 2 — the business-credit band:
"Profit share can't compound faster than GDP forever — competition and wage bargaining pull it
back; at extremes it conditions how much earnings growth to extrapolate," with the atlas's own
hook stated once more because it is this chapter's organizing question: *"India's share roughly
tripled 2019–24 — exactly when the question matters."*) — candidate **H56** (`docs/CYCLE_ATLAS.md`
§8/§16: "Corporate profit-share-of-GDP percentile → margin mean reversion → does it condition the
valuation block (with L8) OOS? → valuation/sentiment block"). This is **Band 2's finale**: the
thirteenth and last of the business-credit band's research units, closing the frequency sweep this
program opened with the credit cycle (`research/cycles/credit-deep`) fourteen entries ago.

**Companion evidence, never recomputed here.** `research/cycles/profitshare-deep/profitshare-
RESULTS.md` (**PS1–PS3**, the desk's own pre-registered trials on Penn World Table 10.0's macro
capital share, already run and printed — the numbers this chapter cites in §B.4 and §C.4) and
`research/cycles/profitshare-deep/partCDEFH.md` (data engineering, the mathematics of the
percentile-conditioner construction, the algorithm, the harvest table, and the Band-2 closing
knowledge ledger this chapter's own §D.5 coda is built to match, not duplicate). `config/
ladder.yaml` (`L8_value_spread`, the block-mate this candidate conditions) and `research/register/
trial-ledger.md` (PS1–PS3's pre-registration, entries dated 2026-09-02). `research/cycles/capex-
deep` (the twin-balance-sheet decade and the 2021+ public-capex era, cross-referenced in §C, never
re-derived) and `research/cycles/credit-deep` (the GNPA/AQR chronology underneath the same decade).
`research/dossiers/02-value-quality-lowvol.md` (D02, Cohen-Polk-Vuolteenaho 2003 and Arnott-Beck-
Kalesnik-West 2016 — L8's own citation base, the block-mate's mechanism). Style and evidentiary
density follow `research/cycles/fincycle-deep/partA-theory-psychology.md` and `research/cycles/
kitchin-juglar/partAB-theory-cases.md` — this program's house style for a paired theory-and-record
chapter.

A note on this file's own letters before it begins: the atlas's universal convention runs Parts
A(theory)–H(ledger) per research unit; this dossier's own commissioning brief instead asks for
internal sections **A–D** (the accounting spine, the mean-reversion record, India's arc, the H56
design), and that is the structure honored below — never to be confused with the companion
`partCDEFH.md` file's own Parts C–H, cited throughout by name, never by letter, to keep the two
numbering systems from colliding on the page.

---

## A. The accounting spine: Kalecki

### A.1 The identity, derived from national accounts, not asserted

Start from the two ways any economy's total output is counted in the same period — once as
spending, once as income — and nothing else. On the spending side, gross domestic product is
consumption plus investment plus government spending plus net exports: **Y = C + I + G + (X − M)**.
On the income side, the same Y is disposed of only three ways: it is consumed, saved, or taxed away:
**Y = C + S + T**. Because both expressions equal the same Y in the same period, they equal each
other, and the shared C cancels:

**I + G + (X − M) = S + T**

Rearranging to isolate investment: **I = S + (T − G) − (X − M)**, i.e. investment is financed by
private saving, by a government *surplus* (T > G; a deficit works in reverse), and net exports
*reduce* the private saving available domestically (a trade surplus does the opposite). This is
pure sectoral-balances bookkeeping — no behavior, no equilibrium condition, nothing estimated —
and it holds in every period, for every economy, by the way national accounts are constructed.

The step that turns this into a *profits* identity splits total private saving, S, into its two
component sources: **household saving (S_h)** and **corporate saving (S_c)**, i.e. retained
earnings. Corporate saving is definitionally what is left of total corporate profits (P) after
dividends (Div) are paid out: **S_c = P − Div**. Substituting S = S_h + S_c = S_h + P − Div into the
rearranged identity above and solving for P:

**P = I + Div − S_h − (T − G) − (X − M)**

Writing government saving as **S_g ≡ (T − G)** (positive in surplus years, negative — i.e. a
deficit *adds* to profits — in deficit years) and net exports as **NX ≡ (X − M)** recovers the
form this program's own atlas states at row 2.15 and this desk works from throughout: **profits =
investment + dividends − household saving − government saving + net exports.** Every term traces
to the derivation above, not to an authority's say-so:

- **Investment (I).** When a firm spends on plant, equipment, or inventory, that spending is, from
  the rest of the economy's vantage, *someone else's revenue* — the capital-goods maker's, the
  construction contractor's, the software vendor's. Investment therefore enters the profits
  identity with a plus sign for the most literal reason possible: one firm's capital expenditure is
  mechanically another firm's sales.
- **Dividends (Div).** A corporation paying out retained earnings as dividends puts that income
  into households' hands; to the extent it is then spent (not itself re-saved — a simplification
  the identity does not need to assume, since any of it that *is* re-saved shows up instead as
  higher S_h, netting out correctly), it becomes revenue for *other* firms. This is the oldest and
  most quotable part of Kalecki's own framing: capitalists, in aggregate, earn what they spend and
  invest; workers, in aggregate, spend what they earn.
- **Household saving (S_h).** The identity's one pure leakage term. A rupee of household income
  that is saved rather than spent does not return to any firm as revenue in that period; it
  necessarily lowers the profit pool, term for term. A *falling* household saving rate is therefore
  profit-supportive on this leg alone — precisely the mechanism §C.3 below applies to India's own
  2019–24 arc.
- **Government saving, i.e. the fiscal balance (S_g = T − G).** A government running a *deficit*
  (S_g < 0) is, definitionally, injecting more spending into the private economy than it is
  withdrawing in taxes — net demand that was not there before, landing directly in the corporate
  sector's revenue. This is the identity's most consequential and most frequently misunderstood
  term, because it inverts the household-budget intuition executives and finance ministries
  instinctively reach for: a government deficit is not, in this accounting, a drain on the private
  sector — it is *definitionally* one of the two demand-side sources (alongside investment) that
  fund private-sector profit.
- **Net exports (NX = X − M).** A trade/current-account surplus means foreign demand is buying more
  of domestic output than domestic residents are buying of foreign output — additional revenue for
  domestic firms. A deficit runs the leak the other way: domestic spending buys foreign goods,
  and that portion of domestic demand never becomes a domestic firm's profit at all.

### A.2 What the identity does — and, more importantly, does not — say

Everything in §A.1 is an **accounting identity**: it holds by construction, ex post, for every
period, in every economy, with no estimated parameter and no possibility of being "wrong" — the
national accounts are built so that it holds. This is a genuine analytical strength and a genuine,
frequently abused, limitation, and both deserve to be stated with equal weight.

**The strength.** Because the four right-hand-side terms must, arithmetically, sum to whatever
profits actually printed, any narrative about *why* profits or the profit share moved is
**disciplined** by the identity: a story is inadmissible if it cannot be traced to a change in
investment, dividends, household saving, government saving, or net exports, because there is
nowhere else for the movement to have come from. This is exactly the sense in which the identity
"disciplines narratives, not a causal model" (this chapter's own brief, echoing the atlas): it does
not tell the analyst which story is *true*, but it does tell the analyst which stories are even
*eligible*.

**The limitation, stated three ways, because each is a distinct trap.** *First*, the identity is
silent on **causation and direction**. High government deficits and high profits are observed
together because the identity requires them to sum consistently — it does not say the deficit
*caused* the profits (rather than, say, a profit boom generating higher tax receipts and hence a
*smaller* deficit, the reverse-causation reading); disentangling direction requires economic
argument entirely outside the identity, exactly as this program's own BC2 trial found for the
imported "credit leads growth" direction (`research/cycles/buscycle-deep/buscycle-RESULTS.md`) — a
standing warning this chapter inherits rather than re-derives: an identity that must hold is not
evidence that any one term *drives* the others. *Second*, the identity describes the **level** of
aggregate profits in nominal terms — it says nothing directly about the **profit share of GDP**
(H56's actual object), which additionally requires dividing by GDP; a rise fully "explained" by
investment is a weaker reversion story than one explained by falling household saving, because
investment adds to GDP (the denominator) even as it adds to profits (the numerator), while
household dissaving adds mostly to the numerator alone. *Third*, and least appreciated, the
identity is **agnostic about mechanism**: the same right-hand-side arithmetic is fully consistent
with two structurally different stories calling for opposite reversion readings. A rise driven by a
demand-composition shift (a fiscal deficit, a saving decline, an investment boom) is
**macro-cyclical** — its reversion force is the eventual unwinding of that same composition (fiscal
consolidation, a return to precautionary saving, a capex-cycle correction, §A.4). A rise driven
instead by rising market power, automation-driven capital deepening, or product-market
concentration (the labor-share-decline literature of §B.3) is **structural**, with no self-
correcting mechanism inside the identity at all — its reversion force, if one exists, is regulatory
or bargaining-power pushback from *outside* the accounting framework entirely. The identity cannot
tell these two stories apart; it only guarantees the same four terms sum correctly either way.
Distinguishing them is §C.3's job for India's own 2019–24 episode, and it is why H56's design (§D)
treats "the identity" and "the labor-share literature" as two separate, complementary lenses.

### A.3 The lineage — Kalecki, the Levy family, and GMO's popularization

**Michał Kalecki** derived the profits identity across several published versions from the 1930s
onward, with the form now treated as canonical appearing in ***Theory of Economic Dynamics***
(1954) [Verified — the identity is the "corollary of a simplified macroeconomic model of a closed
economy," per the secondary literature reviewing Kalecki's own successive versions; Kalecki's own
simplifying closed-economy case, with government and foreign trade set to zero, reduces to the
cleanest statement of the mechanism: **gross profits = gross investment + capitalists' own
consumption** — a special case of §A.1's general derivation, not a different claim]. Kalecki's own
framing was explicitly behavioral and provocative for its era: capitalists, as a class, could not
individually decide how much profit to earn, only how much to spend and invest — profits were the
*consequence* of aggregate spending decisions, not their cause, an inversion of the household-
budget intuition that a government (or a firm) "must live within its means" before anyone can
profit from it.

**Jerome Levy and the Levy Forecasting Center/Jerome Levy Forecasting Institute** (later the Jerome
Levy Economics Institute of Bard College) independently arrived at, and for decades practically
applied, the identical accounting relationship from the 1930s through his own working life, without
initial knowledge of Kalecki's parallel derivation — the two men's convergent, independent discovery
of the same identity is itself documented in **S. Jay Levy (2000), "Profits: The Views of Jerome
Levy and Michal Kalecki,"** Jerome Levy Economics Institute of Bard College, Working Paper No. 309,
August 2000 [Verified — levyinstitute.org/pubs/wp309.pdf]. This is the direct lineage this chapter's
brief names ("the Levy/Jerome Levy Institute lineage") — a family firm using the identity as its
core forecasting instrument for house clients across most of the 20th century, formalized and
credited alongside Kalecki only once the Levy Institute's own later work made the parallel explicit.

**GMO and James Montier's popularization** brought the identity to a mainstream institutional-
investor audience with **Montier, James (2012), "What Goes Up Must Come Down!,"** GMO White Paper,
March 2012 [Verified via search — GMO/Advisor Analyst/Value Investing World coverage of the
original release]. Montier's paper used the Kalecki framework specifically to argue that the
record U.S. profit margins of the early 2010s owed a measurable amount to the government's own
deficit spending in the aftermath of the 2008 crisis — Montier's own estimate, cited in secondary
coverage, put the government-deficit contribution to margins at roughly **+7.6 percentage points**
`[VERIFY: precise magnitude and units of this figure — recovered from secondary description of the
2012 paper, not a direct re-pull of GMO's own chart this session]` — and warned that margins were
correspondingly exposed to reversal once fiscal support was withdrawn. GMO returned to the same
framework a decade later in **Montier, James (2023), "The Curious Incident of the Elevated Profit
Margins" (Part 1),** GMO White Paper, May 2023 [Verified — gmo.com/americas/research-library],
explicitly revisiting and updating the 2012 thesis in light of a decade in which margins had, in
fact, *not* mean-reverted on schedule — a direct acknowledgment, from the same author using the
same framework, that the 2012 call's timing was wrong even where its accounting was not, and the
exact honest complication §B.2 below takes up via Smolyansky's independent 2023 Federal Reserve
finding. It is worth naming precisely, because this program's own house discipline insists on
correcting misattributed authorship (D02's own Arnott-Beck-Kalesnik-Shakernia correction is the
precedent): the oft-repeated line that profit margins are "probably the most mean-reverting series
in finance" belongs to GMO co-founder **Jeremy Grantham**, not to Montier [Verified via search —
multiple secondary sources attribute the exact phrase to Grantham]; Montier is this identity's
principal institutional expositor, not the author of that specific aphorism, and the two should not
be conflated even though both sit inside the same GMO research tradition.

### A.4 Using the identity: decomposition tells you which reversion force applies

The payoff of §A.1's derivation is not forecasting power — the identity forecasts nothing on its
own — it is **diagnostic discipline**. Because a profit-share rise must decompose into some
combination of the four terms (once profits are divided through by GDP), asking "which term(s)
actually moved, and by how much" converts a vague, narrative-level question ("why are profits so
high?") into a specific, falsifiable audit with a determinate answer, and — crucially — each
answer implies a **different** reversion mechanism, because each term's own eventual unwind runs on
a different clock, governed by a different part of this program's own ladder:

- A profit-share rise traceable mainly to an **investment boom** inherits the capex cycle's own
  overbuild-and-correction mechanism (`L11_capex_cycle`, τ½ 36–60 months, Tier C, `reduce_only`,
  `contribution_clamp: non_positive`) — `research/cycles/capex-deep`'s own IN1–IN3 trials already
  measure this reversion force directly on the 18-country JST analogue panel (post-peak repair
  median 4 years, IQR 1–12; a mild top-vs-bottom-quintile overbuild penalty, non-monotone), never
  re-derived here.
- A rise traceable mainly to a **government deficit** inherits the fiscal cycle's own reversion —
  consolidation is not automatic (this program's own DS1–DS4 trials on the debt-supercycle atlas
  entry find most fiat-era deleveragings still unresolved, `research/register/trial-ledger.md`),
  but a deficit this large specifically *is* budgeted, targeted, and publicly tracked (India's own
  FY21 9.2%-of-GDP peak consolidating toward a stated FY26 4.4% target, §C.3 below) in a way an
  investment boom's own turning point is not.
- A rise traceable mainly to **falling household saving** inherits the household-leverage cycle's
  own reversion mechanism (`L13_household_debt`, Tier C, `reduce_only`; Mian-Sufi-Verner 2017's own
  30-country evidence, already this program's citation for L13) — a saving rate pushed toward a
  historic trough by pandemic-era catch-up consumption or rising debt-service burdens carries its
  own eventual snap-back risk, distinct from and unrelated to any capex or fiscal clock.
- A rise traceable mainly to **rising market power, automation-driven capital deepening, or
  product-market concentration** — the labor-share-decline literature's own object (§B.3) — inherits
  **no** mechanical reversion force inside this identity at all. Nothing in the national accounts
  compels a superstar firm's margin to revert; if such a rise is real, it is a **structural** shift
  requiring a genuinely different watch (antitrust, bargaining-power, or automation-diffusion
  trends) than any of the first three.

Applying exactly this decomposition to India's own FY19–FY24 arc is §C.3's job below; the point to
carry forward is that the identity's real service to this desk is not "profits will revert" — a
sentence the identity cannot license on its own — but "here is precisely which of four distinct,
separately-evidenced reversion mechanisms this particular rise has exposed itself to, and here is
the one rise-driver (market power) for which no such mechanism exists inside the accounting at
all."

---

## B. The mean-reversion record, honestly

### B.1 The US century — the range, and the classic reversion evidence

On the U.S. NIPA measure most directly comparable across the postwar era — corporate profits after
tax as a share of GDP/national income — the series has moved across a wide range with genuine,
repeated reversion episodes: from roughly **5.5% in 1952**, the share drifted with cycles for
decades before reaching a **post-WWII record of 11.4% in 2012** [Verified via search — BEA NIPA
data, secondary reporting], averaging roughly **9.2% of GDP across 2010–2015** — itself already a
level well above the mid-century norm. A parallel, more market-facing measure — the S&P 500's own
aggregate net profit margin — tells the same story at a different altitude: margins expanded from
roughly **7% at the turn of the century (2000)** to a FactSet-tracked (data since 2008) **record
13% in Q2 2021**, holding above 12% for five consecutive quarters through Q2 2022 [Verified via
search — FactSet Insight reporting]. The classical mean-reversion evidence this record supports —
and the evidence Grantham's own aphorism (§A.3) and Montier's 2012 paper both leaned on — is that
across the full postwar sample, **periods of unusually high profit share have historically been
followed by periods of profit-share decline or stagnation**, consistent with the textbook
competitive-equilibrium story: abnormal returns on capital should attract entry, competition, and
wage-bargaining pressure that erode the abnormal share back toward a long-run norm. This is the
"classic" reversion case this chapter's brief asks to be stated honestly — and stating it honestly
means immediately confronting the record's own most important complication, because the 2012–2024
window is exactly the period in which the classic case's own timing broke down.

### B.2 The honest complication: the post-2000 plateau, and Smolyansky's exhaustible tailwinds

Montier's own 2012 call — margins were elevated on identifiable, government-deficit-driven grounds
and were "destined" to revert — did not play out on any timescale a 2012 investor could have
profitably acted on: margins in fact rose *further* over the following decade, reaching new records
in 2021–22 (§B.1), and Montier's own 2023 return to the topic ("The Curious Incident of the
Elevated Profit Margins," §A.3) is itself an acknowledgment that the identity's accounting was
correct while its 2012 timing call was not. The single most important honest reckoning with *why*
came not from GMO but from the Federal Reserve itself: **Smolyansky, Michael (2023), "End of an
Era: The Coming Long-Run Slowdown in Corporate Profit Growth and Stock Returns,"** Federal Reserve
Board Finance and Economics Discussion Series, FEDS Working Paper 2023-041, June 2023 [Verified —
federalreserve.gov/econres/feds/files/2023041pap.pdf]. Smolyansky's central, quantified finding:
the secular **decline in interest expense and effective corporate tax rates alone mechanically
explains over 40 percent of the real growth in aggregate U.S. corporate profits between 1989 and
2019** — combined interest-and-tax expense fell from **54% of EBIT in 1989 to 27% of EBIT in 2019**
[Verified], a 27-percentage-point structural tailwind with nothing to do with pricing power, sales
growth, or operating efficiency. This is the chapter's honest complication stated at its sharpest:
**mean reversion delayed by an identifiable, exhaustible tailwind is a fundamentally different claim
from mean reversion refuted.** Falling interest rates (from the early-1980s Volcker peak through
the 2020 zero-lower-bound trough) and falling statutory/effective corporate tax rates (the 1986 and
2017 U.S. reforms among the largest legs) are both, definitionally, tailwinds with a **floor** —
rates cannot fall below zero (and did not, even nominally, stay there once the 2022–23 hiking cycle
arrived) and tax rates cannot fall below zero either — so a profit-margin expansion substantially
explained by these two specific, exhaustible forces is a **structurally different** object from one
explained by a genuine, repeatable improvement in competitive position. Smolyansky's own forward
claim, stated plainly rather than softened: because these tailwinds cannot repeat (rates and tax
rates have limited further room to fall, and by 2022–23 had *reversed*), the "coming long-run
slowdown" in his title is his own explicit prediction that the margin-expansion era built substantially
on these two exhaustible legs is closer to its end than its middle — Montier's 2012 mechanism
(fiscal deficits) and Smolyansky's 2023 mechanism (rates and taxes) are, notably, two *different*
identifiable tailwinds pointing at the same conclusion from two independent research traditions
eleven years apart, neither one claiming the underlying Kalecki/national-accounts arithmetic itself
was wrong — only that its **timing**, absent tracking which specific tailwind is doing the work and
how much runway it has left, cannot be read off the identity alone. This is precisely the design
lesson §D below converts into a rule: H56's own promotion test explicitly refuses "margin
forecasting" as a deliverable for exactly this reason — the identity plus even a rigorous
decomposition (Smolyansky's own) licenses "this specific tailwind has less room to run," never "the
margin will fall by date X."

### B.3 The structural counter-current: the labor-share-decline literature

Running underneath — and partially independent of — both the Kalecki-identity account and the
rates/tax tailwind account is a body of evidence documenting a genuine, decades-long **structural**
decline in labor's share of income across much of the developed and emerging world, which is
definitionally the mirror image of a rising capital/profit share and which, per §A.2's own
mechanism-distinction, carries **no** self-correcting force inside the national-accounts identity
at all. **Karabarbounis, Loukas & Neiman, Brent (2014), "The Global Decline of the Labor Share,"**
*Quarterly Journal of Economics* 129(1): 61–103 [Verified — DOI 10.1093/qje/qjt032; also NBER
Working Paper 19136] documents the decline as genuinely global — occurring within the large
majority of countries and industries studied, not a US-specific artifact — and attributes the
dominant driver to a falling **relative price of investment goods** (largely IT-driven), which
induced firms worldwide to substitute capital for labor, mechanically lowering labor's income share
as a byproduct of ordinary capital-deepening rather than any single country's policy choices. **Autor,
David; Dorn, David; Katz, Lawrence F.; Patterson, Christina & Van Reenen, John (2020), "The Fall of
the Labor Share and the Rise of Superstar Firms,"** *Quarterly Journal of Economics* 135(2):
645–709 (initially NBER Working Paper 23396, 2017) [Verified] supplies a complementary,
firm-concentration-based mechanism using U.S. Economic Census micro-panel data since 1982:
technological or globalization-driven advantages accruing disproportionately to the most productive
firms in each industry raise product-market concentration as **"superstar firms"** — high-profit,
low-labor-share-of-value-added establishments — capture rising shares of their industries' output,
so that a *falling aggregate labor share* can occur even while *no individual firm's own labor
share is changing much*, purely through a compositional shift toward superstar firms that were
always structurally more capital- and profit-intensive. Read together with §A.2's own
mechanism-distinction, this literature is the chapter's clearest instance of a profit-share driver
for which the Kalecki identity's own four terms offer **no natural reversion channel**: neither a
falling relative price of capital goods nor rising industry concentration is a fiscal deficit, an
investment boom, or a household saving swing that must eventually reverse on its own accounting
logic — if either mechanism is genuinely operating, "wait for mean reversion" is not obviously
license-able the way it would be for a purely demand-composition-driven rise, and the honest reading
of any profit-share rise must therefore ask **how much of it decomposes into Kalecki-identity terms
with their own reversion clocks, versus how much decomposes into this literature's structural,
non-self-correcting terms** — precisely the audit §C.3 attempts for India below.

### B.4 The desk's own PS1–PS3 prints, and the proxy's honest limits

This program does not merely cite the literature above; it has run its own pre-registered test of
the reversion claim, on the broadest cross-country panel this desk can access free — and the
result **sharpens, rather than confirms, the naive "what goes up must come down" reading**.
`profitshare-RESULTS.md` reports three trials on **Penn World Table 10.0's macro capital share (1 −
labsh)** — stated at every use, per this chapter's own brief, as a **macro** measure broader than
corporate profits/GDP: it captures the whole economy's capital income, including self-employment
imputations and non-corporate capital, not the listed-corporate share this program's own H56 series
(§D below) actually needs. **PS1 (within-country reversion, the classic claim):** across **114
countries with ≥50 years of observations**, the correlation between a country's capital-share
*level* today and its own *next-decade change* is negative in **85%** of countries — a clear
**PASS** against the pre-registered 70% bar, and, at 85%-of-114-country breadth, one of the
broadest sign-consistency findings this entire research program has measured (for comparison, this
program's own credit-property co-movement print, FC1, found 17/17; its demographics print, DG1,
found only 4/16 — PS1 sits close to FC1's own high end). `[The RESULTS file's own reported "median
corr" line prints "+nan" — a NumPy artifact from at least one country's degenerate/constant series
inside the per-country correlation dictionary, not a substantive finding; the 85%-negative breadth
statistic is a separate, unaffected calculation and is the trial's operative number.]`

**PS2 (the extremes condition — the trial that actually earns this section's honesty) fails, and
the failure is more informative than a pass would have been.** The pre-registered test asked
whether being in the **top quintile of a country's own expanding history** raises the probability
of an outright decline over the next decade by at least 15 percentage points versus the
unconditional rate. The unconditional probability of a next-decade decline, pooled across **5,922**
country-years, is **21%**; conditional on top-quintile positioning (**2,971** country-years), it
rises only to **27%** — a **+6-percentage-point** difference against a **+15pp** bar: a clean
**FAIL**. The honest reconciliation of PS1's pass and PS2's fail, stated exactly as the results file
states it: the post-1980 global sample is dominated by the secular capital-share *rise* that is
this section's own §B.3 literature's object, so reversion in this data operates **around a rising
trend** — a high level today predicts a *smaller further rise* over the next decade, not an
outright *fall*. **"What goes up must come down" is measurably wrong on this proxy; "what goes up
fast then rises slower" is what the data licenses.** This is precisely the honest, sharpened lesson
§B.2's Smolyansky reading already anticipated from a different angle (a tailwind losing force is
not the same claim as a tailwind reversing), and it is the exact empirical basis for how H56 is
designed in §D below: an **extrapolation governor**, never a decline forecaster.

**PS3 (India, measurement only, prior set):** on this same broad macro proxy, India's capital share
in 2019 printed **0.478**, sitting at its own **81st percentile** of its 1950–2019 history —
already a high reading **before** the 2019–24 listed-corporate tripling (§C below) even began. The
proxy's honest limit is stated once more because it governs every use of this number: the **level**
does not transfer between the macro measure and the listed-corporate measure (0.478 is not
comparable to any of §C's percentage-of-GDP figures), and India's 2019–24 listed-corporate move is
explicitly **post-sample** relative to PWT's own coverage — it enters this chapter's record via
§C's own verified figures, never spliced onto the PWT series as though it were the same
instrument. What **does** transfer, per PS1/PS2's own pooled evidence, is the **reversion
question's shape**: if India's listed-corporate share is behaving like the broad cross-country
panel, the honest expectation at a high percentile is not an imminent fall but a **decelerating
further rise** — the governor's job, not a crash call.

---

## C. India's arc — the entry's live question

### C.1 The record, verified point by point

India's corporate-profit-to-GDP ratio — the "Motilal Oswal-style listed-profits series" this
chapter's brief names, tracked in practice across two closely related but distinct universes
(**Nifty-500** and the **full listed India Inc. universe**) that different report vintages report
side by side without always reconciling cleanly — traces an arc matching the atlas's own
headline claim closely:

| Fiscal year | Reading | Universe / note |
|---|---|---|
| FY08 | **~7.8%** (broader listed universe); ~5.2–5.5% specifically on the Nifty-500 cut | the pre-GFC capex-boom peak; "most since FY08" is the recurring benchmark every later report cites itself against |
| FY18 | ~2.8% (Nifty-500, "15-year low" as reported at the time) | mid-slide |
| ~FY19–20 | **~1.6–2.1%** (reports vary by vintage; commonly described as a "two-decade low") | the COVID-adjacent trough |
| FY21 | 2.6% | "four-year high," pandemic notwithstanding |
| FY23 | ~4.0% (Nifty-500) | mid-recovery |
| FY24 | **4.8%** (Nifty-500) / **5.2%** (full listed universe) | "15-year high," i.e. the highest print since the FY08 peak |
| FY25 | 4.7% (Nifty-500, reported as a "17-year high") / 5.1% (listed universe, "14-year high") | the two universes' own headline-year labels do not fully reconcile across reports — flagged, not resolved, this pass |
| FY26 | **5.2%** (Nifty-500, a fresh record, reported at "~2.6× the FY20 level") / **5.7%** (listed universe, "18-year high") | the current print as of this writing |

`[VERIFY: every cell above — recovered from Motilal Oswal India Strategy report coverage and
Business Standard/Equentis/BusinessToday secondary reporting this session, not from a single primary
MOFSL chart independently re-pulled; the Nifty-500-vs-listed-universe distinction and the
across-vintage inconsistency in which year each report calls a "record" or "N-year high" are both
real measurement facts about how this series is reported, not resolved errors on this program's
part — a future data-phase pull should establish one constant-universe series before this candidate
is promoted, exactly as `partCDEFH.md`'s own Part C already registers as a runsheet item: "the
listed-universe drift... needs a constant-universe variant printed alongside."]` The pattern the
atlas's own hook names — **"India's share roughly tripled 2019–24"** — checks out on these figures
at either universe cut: roughly 1.6–2.1% (FY19/20) to 4.8–5.2% (FY24) is a **2.4×–3.3×** move,
comfortably inside "roughly tripled." FY25 and FY26's continued records (§C.4) mean the live
question the atlas poses is not resolved by FY24 — the share has kept climbing for two further
years past the atlas's own headline window.

### C.2 Why each leg happened

**The FY08 peak — the capex-boom top, not re-derived here.** `research/cycles/capex-deep`'s own
case studies already fully document the 2003–08 investment boom this profit peak sits on top of —
the UMPP-era power-sector build-out, the pre-crisis credit expansion, and the same episode
`docs/CYCLE_ATLAS.md` row 1.6 and `L11_capex_cycle` treat as India's clearest observed capex-cycle
upswing. A profit share riding an investment boom is, per §A.4's own decomposition logic, exactly
the case where the Kalecki identity's **investment** term is doing the work — and, per that same
logic, exactly the case with the *weakest* claim to durability, because an investment boom that
raises today's profits is simultaneously raising tomorrow's installed capacity, the textbook
overbuild-and-correction mechanism this program's own IN1–IN3 trials already measure on the
cross-country analogue panel.

**The slide, 2011–2020 — the twin-balance-sheet decade, cross-referenced, not re-derived.**
`research/cycles/capex-deep/partB-cases.md`'s own case 3 ("India 2011–2020 — the twin-balance-sheet
decade") and `research/cycles/credit-deep`'s own GNPA/AQR chronology together already carry this
episode's full real-side and credit-side record: the 2011–13 clearance-and-land-acquisition
bottlenecks that stalled roughly **$45 billion** of investment even before formal recognition; the
**AQR shock (August 2015)** forcing banks to reclassify previously obscured stressed loans (a
**measurement break**, in the credit monograph's own words, not a fresh credit event); the
escalating restructuring alphabet (CDR → 5:25 → SDR → S4A → IBC, 2001–2016) each superseded within
one to three years; the **IL&FS default (September 2018)** triggering a system-wide NBFC funding
freeze that hit real-estate and infrastructure capex with particular force because both sectors had
grown dependent on the single financing channel banks had already exited post-AQR; and the
decade's terminal credit event, the **YES Bank moratorium (5 March 2020)**, arriving days before
COVID. OBICUS capacity utilization fell from a **March 2011 all-time high of 83.2%** to a record low
during this window, and GFCF/GDP fell from its ~34–35% 2007–08 boom peak toward roughly 28–29%
through the "capex winter" `[figures per the capex monograph's own recollection-level estimate;
VERIFY against primary MOSPI data before backtest use, per that file's own flag]`. A profit share
compressed by a decade of balance-sheet repair, capacity overhang, and (per the atlas's own framing
of this leg) commodity/margin compression during the same window is the textbook case of a share
squeezed by **weak demand composition and impaired credit intermediation simultaneously** — the
Kalecki identity's investment term collapsing alongside a credit cycle (L10) working through its
own down-leg, not a labor-bargaining-power story at all.

**The 2019–24 tripling — four distinct, separately-verifiable legs.** *First*, the **corporate tax
cut**: the **Taxation Laws (Amendment) Ordinance, 2019**, promulgated **20 September 2019**, gave
domestic companies the option of a **22%** base rate (effective ~25.17% with surcharge/cess,
forgoing exemptions and MAT) and new manufacturing companies incorporated after 1 October 2019 and
commencing production by 31 March 2023 an even lower **15%** option (~17.16% effective) [Verified —
PIB press release 1585641; PRS Legislative Brief]. This is a direct, mechanical, one-time boost to
**post-tax** profit retention with an exact historical analogue in Smolyansky's own U.S. finding
(§B.2): a falling effective tax rate raises reported profits independent of any change in
underlying operating performance, and — per that same finding's own logic — is an **exhaustible**
tailwind (a tax rate has a floor) rather than a repeatable one. *Second*, **corporate deleveraging**,
already measured in the capex monograph's own record and cross-referenced rather than re-derived
here: the listed-corporate debt/equity ratio fell from **0.73 (FY20) to 0.59 (FY21)**, "the lowest
in six years," with roughly 750 companies cutting a combined **₹3 trillion** of gross debt in FY21
alone — and, importantly, that same monograph's own honest sequencing note applies: net debt/equity
had already been improving for three consecutive years by FY18, meaning the balance-sheet repair
this episode's profit recovery partly rides on was substantially **completed before**, not during,
the 2021+ window, lowering interest expense as a share of earnings in the same structural direction
Smolyansky documents for the U.S. *Third*, **formalization and large-cap consolidation**: the
**Goods and Services Tax (July 2017)** created what recent empirical work (using CMIE Prowess
firm-level data, 2013–2022) documents as a **"formalisation cascade"** — large, GST-compliant firms
with stronger incentives to source from formally registered (input-tax-credit-eligible) suppliers
progressively squeezed out informal competitors upstream, and firms with high pre-reform exposure
to cascading taxes measurably increased documented input purchases (~6%) and cut indirect tax
payments (~8%) after the reform [Verified via search — CMIE-Prowess-based academic study, secondary
reporting]. Motilal Oswal's own FY24 attribution — **financials, energy (oil & gas), and
automobiles together accounted for 95% of incremental FY24 profit growth** — is the market-level
signature of the same consolidation dynamic: profit growth concentrating in large, already-dominant
sectors and companies rather than broadening across the listed universe, precisely the "profit-shift
to large caps" this chapter's brief names. *Fourth*, the **public-capex era (2021+)**, cross-
referenced from the capex monograph's own case 4: Union Budget capital expenditure rising from
**₹4.12 lakh crore (FY21)** to **₹10.0 lakh crore (FY24)**, a genuine investment-side tailwind
running through the Kalecki identity's own **I** term precisely as §A.4 describes — though that same
monograph's own honest caveat (FY25 RE running well below FY25 BE, FY26 growth decelerating to
+0.9%) already flags this leg as the one most exposed to its own capex-cycle correction risk, not a
permanent new plateau.

### C.3 The Kalecki read of 2019–24 — decomposing the identity's own side

Running §A.4's decomposition discipline against India's own 2019–24 window, using the identity-side
data this program can verify, yields a picture that is **directionally coherent but only partially
decomposed** — an honest limitation stated plainly rather than smoothed over, because a full
sectoral-balances reconciliation (requiring corporate investment, dividends, and both saving legs
on a consistent, contemporaneous basis) is a runsheet item (`partCDEFH.md`'s own Part C: "Household/
govt saving... runsheet; ~18m lag on the split"), not something this research-only pass can complete.
Two of the identity's terms move unambiguously in the profit-supportive direction across this
window. **Household saving fell sharply**: RBI data show household net financial savings at
roughly **11% of GDP in FY21**, falling to **7.2% in FY22** and **5.1–5.3% by FY23/FY24** [Verified
via search — RBI household-finance data, Business Standard coverage of the "five-decade low" 2022-23
print], with RBI's own Deputy Governor attributing part of the reversal to a pandemic-era saving
spike (forced non-consumption) unwinding rather than a purely structural shift — but a mechanical
household-saving decline of this magnitude, per §A.1's own derivation, is a direct, term-for-term
addition to the profit pool regardless of *why* households saved less. **The fiscal deficit stayed
structurally elevated relative to the pre-pandemic norm even as it narrowed**: from a
**FY15–20 average of ~3.8% of GDP**, India's fiscal deficit spiked to **9.2% in FY21**, then
consolidated through **6.8% (FY22), 6.4% (FY23), 5.6% (FY24)** toward a stated **4.8% (FY25 RE)** and
**4.4% (FY26 BE)** target [Verified via search — CEIC/GovtBudget/Union Bank of India budget
coverage]. Every year of this consolidation path still sits above the pre-COVID ~3.8% average,
meaning the government-saving term (S_g, negative throughout) remained a *larger-than-normal*
profit-supportive injection across the entire 2019–24 window even as headline deficit numbers fell
— exactly the demand-composition story §A.4 names as the case with the clearest, most trackable
reversion clock (India's own stated consolidation glide path). **Net exports/the current account
contributed a third, smaller and more ambiguous leg**: India's current account swung to an outright
**surplus in FY21** (COVID-compressed imports), before returning to deficit — roughly **2.0% of GDP
in FY23**, narrowing to **~0.7% in FY24** on stronger services exports [Verified via search —
CEIC/Focus Economics/trading-economics current-account series] — a narrowing deficit is itself a
*smaller* drag on domestic profits (less demand leaking abroad relative to FY23), so this term, too,
reads in the same profit-supportive direction across the back half of the window, though at a much
smaller magnitude than either saving leg. **What this decomposition cannot yet do, stated as a
limitation rather than papered over**: it does not include a matching, contemporaneous read of the
**investment** term specifically for the *private corporate* sector (as distinct from the
public-capex leg already covered in §C.2), nor does it net out how much of the identity-side story
above is itself a byproduct of the four *structural* legs named in §C.2 (the tax cut, deleveraging,
formalization, and public capex) rather than an independent demand-side story — the two accounts
overlap in ways this pass has not fully untangled, and `partCDEFH.md`'s own registered runsheet
item (the NAS institutional-accounts saving legs, ~18-month lag) is exactly the future work that
would close this gap. What can be said with confidence today: **the two identity-side terms this
program can verify — falling household saving and a still-elevated (though narrowing) fiscal
deficit — both moved in the profit-supportive direction across 2019–24, consistent with, though not
a complete accounting of, the tripling §C.1 records.**

### C.4 The live question, and where the share stands today

The atlas's own live question, restated precisely: **extrapolating FY24–26 earnings growth forward
assumes the profit share keeps rising at anything like its 2019–24 pace — H56 exists specifically to
condition that extrapolation, never to answer it outright.** Two facts sharpen exactly how live this
question is as of this writing. **First**, the share has **not** stopped rising at the atlas's own
FY24 vantage point — it continued to fresh records through FY25 (4.7%/5.1%) and FY26 (5.2%/5.7%,
§C.1), meaning any analysis anchored only to the atlas's own 2019–24 framing understates how far the
run has now extended: FY26's Nifty-500 print is reported at roughly **2.6× the FY20 level**, and
Nifty-500 profits are reported growing **15.6% year-on-year in FY26 against 8.9% nominal GDP
growth** — the profit share is, by construction, *still expanding* at the most recent print
available. **Second**, and this is where §B.4's own PS1/PS2 pair earns its keep directly: the
desk's own broad cross-country evidence says the honest base-rate expectation at a high percentile
is **not** an imminent decline (PS2's own 27%-vs-21% fail) but a **deceleration of the further rise**
— and separately, §C.2's own leg-by-leg audit shows at least two of the four structural drivers
(the corporate tax cut, the initial deleveraging wave) are **exhaustible tailwinds already largely
spent** by construction (a tax rate that has already been cut cannot be cut again by the same
margin; a debt/equity ratio that fell from 0.73 to 0.59 has less room to fall the same distance
twice), while a third (public capex) is, per the capex monograph's own FY25/FY26 data, **already
decelerating**. The live question the atlas names is therefore not "will the share revert" — a
claim §B.4's own evidence explicitly refuses to license — but **"how much of any further FY26–28
earnings growth extrapolation is quietly assuming the share keeps compounding at its 2019–24 rate,
when at least two of that rate's four named drivers are mechanically running out of runway."** That
is precisely the extrapolation-discipline job §D below designs H56 to perform.

---

## D. The H56 design and the fold-forward

### D.1 What the candidate is

**H56** is a **valuation-block conditioner**: the India listed-corporate profit-share-of-GDP series,
converted to an **expanding percentile of its own history** (the same real-time, no-look-ahead
construction this program uses throughout — never a full-sample band-pass or turning-point method,
per the Hamilton-filter-only rule this program has applied consistently since the credit monograph),
read **jointly** with **`L8_value_spread`** (`config/ladder.yaml`, τ½ 24–36 months, Tier B, Cohen-
Polk-Vuolteenaho 2003/Arnott-Beck-Kalesnik-West 2016) inside the shared **`valuation_sentiment`**
regime-score block (≤10% of regime score, alongside L7's issuance-sentiment seat). The joint-read
logic is the candidate's entire design rationale in one sentence: **a high profit-share percentile
and a rich (top-tercile) value spread are, read separately, two different "the market is optimistic"
signals — read together, uncorrected, they double-count the same optimism**, because an expensive
market sitting on top of an already-elevated, decelerating-growth profit share is pricing the
*continuation* of exactly the extrapolation §C.4 just flagged as running out of two of its four
named tailwinds. H56's own contribution is not a new return forecast; it is a **cross-check** that
prevents L8's own value-spread signal from being read in isolation precisely when the earnings
denominator underneath "cheap" or "expensive" is itself sitting at a percentile extreme.

### D.2 Tier, the promotion test, and what stays out of bounds until it clears

**Tier C, reduce-only, at extremes only** — consistent with every other Tier-C entry on this
ladder (`CONTRACT.md` §4: "Tier-C signals may only REDUCE risk — never add"), and consistent with
PS2's own honest fail: because the desk's own broad-panel evidence refuses to license a decline
call, H56's design refuses to let a high percentile *add* to any bullish reading either — it can
only trim. **The promotion test, pre-registered rather than assumed**: the seat's own India series
(listed-corporate profits/GDP, aggregated from exchange filings against MOSPI nominal GDP,
`partCDEFH.md`'s own Part C runsheet item, "the band's largest single build") must first exist as a
**constant-universe** variant (isolating genuine share expansion from listing-count drift — the
proxy hazard `partCDEFH.md` names explicitly) before any conditioning test is run; the acceptance
bar itself — a **purged, out-of-sample** test of whether the profit-share percentile, jointly with
L8's value spread, improves a forward valuation-block read versus L8 alone — is registered *before*
the look, per this program's estimation standards (`docs/DESIGN.md` point 8: purged K-fold CV,
embargo ≥1×τ½) and per the hypothesis-register discipline every H-series candidate on this atlas
already follows (H53–H65, `docs/CYCLE_ATLAS.md` §8/§16). Until that test clears, H56 stays exactly
where `docs/CYCLE_ATLAS.md`'s own master map already places it: **"profit-share (until H56)"**
under CONTEXT, with zero regime-score budget of its own.

### D.3 What is refused, explicitly

Three uses this candidate's own evidence base rules out, stated as refusals rather than left
implicit. **Margin forecasting is refused.** Nothing in §A (an identity) or §B.4 (PS1 pass, PS2
fail) licenses a forecast of the *level* margins will reach or the *date* they will revert — the
identity disciplines narratives, it does not generate point forecasts, and PS2's own fail is direct
evidence against a decline-timing claim on this proxy specifically. **Earnings-revision chasing is
refused**, for a reason already fully argued elsewhere on this ladder and cross-referenced rather
than re-derived: analyst earnings-revision trends are a documented anchoring effect (Atlas row 3.5)
already flagged **REJECT for data** under this program's free-source rule (consensus-estimate data
is paid in India) — H56 does not smuggle a revision-chasing signal back in under a profit-share
label; it conditions the *value spread's own* denominator, never a forward-estimate trend. **Treating
the identity as a timing model is refused** — the single most important refusal, because it is the
exact mistake both Montier's 2012 call and this section's own honest §B.2 discuss: the identity
correctly disciplines *which* stories are eligible, and Smolyansky's own decomposition correctly
identifies *which specific tailwinds* have how much runway left, but neither converts into "profits
fall by year X" without an additional, separately-evidenced timing claim this candidate's own
Tier-C/reduce-only design deliberately declines to make.

### D.4 Synthesis

| Question | What the evidence says | What H56 does with it |
|---|---|---|
| Is the Kalecki identity a causal model? | No — an accounting identity, true by national-accounts construction, silent on causation (§A.2) | Used only to decompose WHICH reversion force a given profit-share rise has exposed itself to (§A.4), never to forecast |
| Does profit share mean-revert (US record)? | Classic evidence yes; but the 2000–2024 plateau is real, and Smolyansky (2023) attributes >40% of 1989–2019 real profit growth to exhaustible rate/tax tailwinds, not operational improvement (§B.2) | Read as "delayed by identifiable tailwinds," never "refuted" — the same distinction the desk's own India tailwind ledger (§C.2/C.4) applies |
| Does the desk's own broad panel confirm reversion? | PS1 passes at 85%-of-114-country breadth (level → next-decade change, negative); PS2 FAILS the extremes-decline bar (+6pp vs +15pp bar demanded) (§B.4) | Licenses an EXTRAPOLATION GOVERNOR (smaller further rises expected at high percentiles), explicitly refuses a decline forecast |
| Is the rise structural (labor-share-decline literature) or cyclical (Kalecki demand-composition)? | Both mechanisms are real, evidenced separately (Karabarbounis-Neiman; Autor et al. vs the identity's own four terms) and NOT distinguished by the identity itself (§A.2/§B.3) | India's own 2019–24 legs (tax cut, deleveraging, formalization, public capex) are named individually so future work can attempt this separation — not yet fully closed (§C.3's own stated limitation) |
| Where does India's arc stand, verified? | ~7.8% FY08 peak → ~1.6–2.1% FY19/20 trough → 4.8–5.2% FY24 → fresh records 4.7–5.1% FY25 → 5.2–5.7% FY26 (§C.1) | Feeds the expanding-percentile construction directly; the constant-universe variant is the promotion test's own prerequisite |
| What is the seat, and what is it not? | A Tier-C, reduce-only, valuation-block conditioner alongside L8 (§D.1); NOT a margin forecast, NOT a revision-chasing signal, NOT a timing model (§D.3) | Candidate status until the purged OOS conditioning test clears (§D.2) — exactly where the atlas's own master map already places it |

### D.5 Band 2's close — the coda

This chapter closes the business-credit band's thirteenth and final research unit — one row per
monograph, not per atlas number (`kitchin-juglar` and `dollar-fold` each resolve two atlas rows
inside one file; the count below is the desk's own thirteen research units):

| # | Entry (research unit) | Verdict | What the ladder keeps |
|---|---|---|---|
| 1 | Credit cycle (2.1) — `credit-deep` | **Seated, the anchor.** Real-time AUROC ~0.64–0.67 (J1/J2), pooled prior 0.65–0.75 validated at its lower half | `L10_credit_block`, Tier B, `macro_credit_block` |
| 2 | NBFC/shadow-credit (2.2) — `shadow-deep` | SC1: the IL&FS-window funding-freeze signature propagated broadly (SMB −24.8%, market −20.2%) — **fails** as a standalone equity-factor detector; routed to the faster layer instead | Sub-component of L10's aggregate + an L2 fast-stress signature; no separate seat |
| 3 | Business cycle proper (2.3) — `buscycle-deep` | BC1 **pass** (3–7y band real, median 6y); BC2 **fail, major finding** (imported "credit-leads-growth" direction fails on the pooled panel — 16/18 countries peak at negative lags) | CONTEXT inside the macro block; the BC2 standing warning against imported lead-lag directions applies program-wide |
| 4 | Kitchin (2.4) + Juglar (2.5) — `kitchin-juglar` | Kitchin: KJ1 **0/37** spacings in-band — clock dead, bullwhip mechanism alive. Juglar: object kept, name **retired**, folded into L10+L11 | Kitchin → CONTEXT via L9, unbudgeted; Juglar → no separate content, already inside L10/L11 |
| 5 | Monetary-policy cycle (2.6) — `mpcycle-deep` | MP1 **pass** (rate leads credit at 67% of qualifying countries); MP3: campaign persistence near coin-flip (53%) — stance LEVEL carries the content, not move direction | `L6_monetary_stance`, Tier B, calibrated |
| 6 | Fiscal/political cycle (2.7) — `fiscal-deep` | FP1a folk pre-election rally passes as registered then **dissected and deflated** (2009 carries the mean; ex-2009 ≈ +1.9%/m) — routed to a teach-only heuristic, never traded | CONTEXT folded into L5/L6; the folk claim demoted to Heuristics Lane HL-7 |
| 7 | Global financial cycle (2.8) — `globalcycle-deep` | GF1 **pass, strong** (co-movement +0.28→+0.77 pre/post-1990); GF2 **pass** (India loading corr +0.57); GF3 **fail** ("one cycle everywhere" too strong — 69% vs 75% bar) | `L9_global_financial_cycle`, the seat's Tier-A/B anchor |
| 8 | Dollar (2.9) + Fed (2.10) sub-faces — `dollar-fold` | DL1 pass-on-n=4 but **promotion refused** (clock not crowned); DL2 **pass** (India headwind corr −0.34); DL3 fold-supporting (Fed's own realized-rate path carries zero same/next-year dollar signal at annual frequency) | Both retired as separately-named clocks; folded fully inside L9 (real-yield-level leg) |
| 9 | China credit impulse (2.11, H54) — `china-deep` | CI1a **pass** (metals-vs-ags variance shift 2.19× post-2000); CI1b **pass, bounded** (n=2 named-pulse sign check) | **Candidate**, L9-enrichment only; graduation waits on real TSF data (BIS blocked here) |
| 10 | Oil/energy cycle (2.12) — `oil-fold` | OL1 **pass by 8×, capped on dissection**: the demand/supply "flavor" proxy is shown to be ~GF2's own global-equity loading in an oil costume | Folds into L9 (Kilian-decomposed); the standalone "oil cycle" asymmetry claim retired, oil itself stays inside L9 |
| 11 | FII/FPI positioning (2.13) — `fpi-deep` | No trial run yet — data-gated designs (FL1/FL2) registered with acceptance bars, awaiting the NSDL/shareholding vault | `L14_fii_positioning`, Tier C, `reduce_only`; module shipped, awaiting data |
| 12 | ENSO (2.14, H55) — `enso-deep` | EN1: **62% in-band, still fails** the 70% clock bar — the best in-band share this entire register has printed, on the ONE genuinely physical oscillator tested, and it still fails | **Candidate**, sector-level reduce-only under L5/L6 context; the register's control group |
| 13 | Profit-share cycle (2.15, H56) — this chapter | PS1 **pass** (85%/114-country breadth); PS2 **fail** (reversion runs around a rising trend, not toward a fall); India's macro proxy already at its 81st percentile in 2019, pre-tripling | **Candidate**, valuation-block conditioner with L8; the promotion test's runsheet (constant-universe series, purged OOS) not yet cleared |

**The band's own honest tally.** Thirteen research units, **zero new ladder seats beyond what was
already designed** at the ladder's first draft (L6, L9, L10, L11, L14 all pre-existed this band's
research; the work calibrated and validated them, it did not invent them). **Five labels retired**,
each an object kept under a different, better-evidenced name while its own historical label is
discontinued from future budget discussions: **Juglar** (folds into L10+L11), **Kitchin's
~40-month clock** (the bullwhip mechanism survives as unbudgeted CONTEXT, the clock does not),
**the dollar cycle's own claimed 7–10y clock** (the dollar factor survives inside L9, the
periodicity claim does not), **the Fed cycle** (folds fully into L9's real-yield-level leg), and
**the oil-specific shock-asymmetry claim** (oil stays inside L9, Kilian-decomposed, but its claimed
independent India transfer is capped, per OL1's own dissection). **Three candidates instrumented,
none promoted**: H54 (China credit impulse), H55 (ENSO), and H56 (profit share) — each
pre-registered, each partially or fully tested, none clearing a promotion bar, all three awaiting
further data rather than a seat on narrative strength alone. And the band's own **exportable
doctrine**: the **frequency sweep** — every claimed clock this program has tested, from Kitchin's
40 months through the property cycle's folk 18 years, the commodity supercycle's 15–21 years, and
Kondratieff's claimed 45–60 years — has found **zero surviving fixed periods**, while finding real,
persistent, tradable *bands* at several of those resolutions; and the **ENSO control group** (EN1:
62% in-band, this register's best-ever print, on the one genuinely physically-forced oscillator
available, and it *still* fails a strict clock bar) seals why: if physics cannot clear this
program's own bar under honest, real-time rules, no financial "cycle" should be expected to.
**States and bands, never dates** — a measured finding now, not a preference, and the sentence H56
is designed to honor: a governor that conditions how much of a rising share to keep extrapolating,
never a call on when, or whether, it turns.

---

## References

Kalecki, Michał (1954). *Theory of Economic Dynamics.* George Allen & Unwin — the canonical
version of the profits identity, itself one of several the author published from the 1930s
onward. · Levy, S. Jay (2000). "Profits: The Views of Jerome Levy and Michal Kalecki." Jerome
Levy Economics Institute of Bard College, Working Paper No. 309, August 2000. · Montier, James
(2012). "What Goes Up Must Come Down!" GMO White Paper, March 2012. · Montier, James (2023).
"The Curious Incident of the Elevated Profit Margins" (Part 1). GMO White Paper, May 2023. ·
Smolyansky, Michael (2023). "End of an Era: The Coming Long-Run Slowdown in Corporate Profit
Growth and Stock Returns." Federal Reserve Board Finance and Economics Discussion Series, FEDS
Working Paper 2023-041, June 2023. · Karabarbounis, Loukas & Neiman, Brent (2014). "The Global
Decline of the Labor Share." *Quarterly Journal of Economics* 129(1): 61–103 (NBER WP 19136). ·
Autor, David; Dorn, David; Katz, Lawrence F.; Patterson, Christina & Van Reenen, John (2020). "The
Fall of the Labor Share and the Rise of Superstar Firms." *Quarterly Journal of Economics* 135(2):
645–709 (NBER WP 23396, 2017). · Cohen, Randolph B.; Polk, Christopher & Vuolteenaho, Tuomo
(2003). "The Value Spread." *Journal of Finance* 58(2) — already `research/dossiers/
02-value-quality-lowvol.md`'s (D02) own citation for `L8_value_spread`, not re-derived here. ·
Arnott, Robert; Beck, Noah; Kalesnik, Vitali & West, John (2016). "How Can 'Smart Beta' Go
Horribly Wrong?" Research Affiliates — already D02's own citation, not re-derived here. · Taxation
Laws (Amendment) Ordinance, 2019, Government of India, promulgated 20 September 2019 — PIB press
release 1585641. · Reserve Bank of India, household financial-savings data (FY21–FY24 series) —
secondary reporting, Business Standard. · CEIC/GovtBudget/Union Bank of India coverage of India's
fiscal-deficit path, FY15–FY26. · CEIC/Focus Economics coverage of India's current-account balance,
FY19–FY24. · Motilal Oswal Financial Services, India Strategy reports on corporate profit-to-GDP,
various vintages FY08–FY26 — secondary reporting (Business Standard, Equentis, BusinessToday);
primary MOFSL charts not independently re-pulled this session, per the `[VERIFY]` flags in §C.1. ·
`research/cycles/profitshare-deep/profitshare-RESULTS.md` (PS1–PS3, this chapter's own companion
trial). · `research/cycles/profitshare-deep/partCDEFH.md` (data engineering, mathematics, harvest,
and the Band-2 closing ledger this chapter's §D.5 is built to match). · `research/cycles/capex-deep`
and `research/cycles/credit-deep` (the twin-balance-sheet decade and GNPA chronology, cross-
referenced throughout §C, never re-derived). · `research/dossiers/02-value-quality-lowvol.md` (D02,
L8's own evidence base). · `config/ladder.yaml`, `docs/CYCLE_ATLAS.md`, `docs/DESIGN.md`,
`research/CONTRACT.md`, `research/register/trial-ledger.md` — this program's own governing
documents, cited throughout.

---

*Word count: ~9,000 words (`wc -w`).*

---

# PART RESULTS — The desk's own numbers (PA1 + PS1-PS3, pre-registered)

# Atlas 2.15 — profit-share cycle: PWT capital-share trials (PS1-PS3, pre-registered)

Proxy: macro capital share (1 − labsh) — BROADER than corporate profits/GDP; the
reversion question transfers partially, the level does not. Vault authenticated
(PA1a/b pass; PA1c marginal miss recorded).

## PS1 — level → next-decade change

- 114 countries (≥50 obs): **85% negative** (bar ≥70%): **PASS**. Median corr **−0.42** (nan-robust; 5 of 114 countries print NaN — constant-labsh stretches in PWT for Costa Rica/Lebanon/Senegal/Uzbekistan/Zambia; NaNs counted as NON-negative in the 85% share, i.e. conservatively against the pass).

## PS2 — the extremes condition

- P(next-10y change < 0): unconditional **21%** (n=5922); top-quintile-of-own-history **27%** (n=2971).
- Bar (conditional ≥ unconditional + 15pp): **FAIL**.

## PS3 — India (measurement, prior set)

- India capital share 2019: **0.478**, its own-history percentile **81th** (1950-2019). Path in the chart file. The 2019-24 listed-
  corporate tripling is POST-sample and enters via the record, never spliced.

## Honest read (written AFTER the print)

- **PS1 PASSES with FC1-class breadth (85% of 114 countries):** within-country, a higher
  capital share today correlates negatively with its own next-decade CHANGE — relative mean
  reversion is one of the broadest regularities this register has measured.
- **PS2 FAILS — and the pair teaches more than either alone.** Even at top-quintile-of-own-
  history extremes, outright next-decade DECLINES happen only 27% of the time (vs 21%
  unconditional; bar demanded +15pp). Why both can be true: the post-1980 sample is dominated
  by the global capital-share RISE (the labor-share-decline literature's object) — so
  reversion operates AROUND A RISING TREND: high levels are followed by SMALLER RISES, not by
  falls. "What goes up must come down" is measurably wrong on this proxy; "what goes up fast
  then rises slower" is what the data licenses.
- **The H56 design consequence, sharpened by the fail:** the conditioner's honest job is
  EXTRAPOLATION DISCIPLINE (at high percentiles, expect the share's growth contribution to
  earnings to shrink toward zero), NOT decline prediction. Conditioning the valuation block
  (with L8) on that basis survives PS2; a "margin crash" signal would not have.
- **PS3:** India's macro capital share printed 0.478 in 2019 — its 81st own-history
  percentile BEFORE the 2019-24 listed-corporate tripling even began. The atlas's live
  question ("how much of FY24-26 earnings growth is share-expansion?") starts from an
  already-high base on the broad proxy — with the proxy caveat (macro ≠ listed-corporate)
  attached to every use.

---

# Parts C–H — data engineering, math, algorithm, harvest, ledger (atlas 2.15; candidate H56)

## Part C — Data engineering (compact, in-house)

| Leg | Source | Status |
|---|---|---|
| Macro capital share (1−labsh), 180+ countries 1950-2019 | PWT 10.0 | VAULTED + authenticated (PA1; the PA1c marginal miss recorded) |
| India LISTED corporate profits/GDP (the H56 series proper) | aggregate filings (exchange disclosures) ÷ MoSPI nominal GDP | runsheet — the fundamentals-puller gap capex-partC already flagged; annual, FY basis |
| Corporate tax collections (the cross-check leg) | CGA monthly / Budget docs | shared with fiscal pulls — dedup noted |
| Household/govt saving (the Kalecki decomposition legs) | MoSPI NAS institutional accounts | runsheet; ~18m lag on the split |

PIT hazards: PWT vintage revisions (10.0 → 10.01 → 11 re-state labsh history — vintage-named
files, WORM); the listed-universe drift (new listings mechanically raise listed-profits/GDP —
the H56 series needs a constant-universe variant printed alongside); GDP rebasing (the
Feb-2026 rebase splice discipline, buscycle Part B).
Runsheet addendum 14 (steps 74-77): 74 listed-profits aggregation pipeline (8-10h — the
band's largest single build, shared with the optimizer's fundamentals needs); 75 NAS saving
legs (~2h); 76 constant-universe variant (~2h); 77 H56 acceptance registration (BEFORE the
look): percentile-conditioned extrapolation test with L8, purged (~2h).

## Part D — The mathematics

Kalecki's identity is the entry's spine (the chapter derives it); the desk's measured
contribution is the PS1/PS2 pair: within-country reversion at 85% breadth AND no decline
prediction at extremes (+6pp vs the +15pp bar) — formally, the capital share s_t behaves like
s_{t+10} − s_t = α_c − β·(s_t − trend) + ε with β>0 (PS1) but trend drift α large enough that
even top-quintile s_t rarely yields negative changes (PS2). The licensed sentence: HIGH SHARE
⇒ SMALLER FURTHER RISES, never "must fall". H56's conditioner is therefore an EXTRAPOLATION
GOVERNOR on the valuation block: at high percentiles, the earnings-growth term attributable
to share expansion is haircut toward zero (grid-registered haircut), jointly read with L8's
value spread (high share + expensive market = the double-count to refuse). The macro-vs-
listed caveat is structural: PWT calibrates the QUESTION; the seat's own series is the listed
one (runsheet), and the two are never spliced.

## Part E — The algorithm (H56 candidate, annual with quarterly updates)

```
STEP 1  listed-profits/GDP (FY, constant-universe variant alongside) -> expanding percentile
STEP 2  Kalecki decomposition table (investment, fiscal, saving, external legs) printed with
        every annual update — WHY the share moved decides WHICH reversion forces apply
STEP 3  consumption (Tier C, reduce-only): at high percentiles the valuation block's
        earnings-extrapolation input is haircut (the governor); joint read with L8 flags the
        double-count; NO decline forecast exists in the interface (PS2's fail is the reason)
STEP 4  quarterly earnings seasons update a nowcast shadow (briefing only)
MONITOR annual PS1-PS3 re-run on new PWT vintages; the listed-universe drift check; the
        Smolyansky-style tailwind ledger for India (tax cuts, rate declines — exhaustible
        tailwinds enumerated, each with its remaining runway stated honestly)
FAILURE MODES: universe drift masquerading as share expansion (the constant-universe
        variant); GDP rebase splices; the macro-listed conflation (structurally separated)
```

## Part F — Harvest + designs

| Consumer | What it gets |
|---|---|
| valuation_sentiment block (with L8) | the extrapolation governor at high percentiles (Tier C, reduce-only) |
| Stage-2 briefings | the Kalecki decomposition table + the tailwind ledger |
| Registry | the "reversion around a rising trend" print — cited whenever mean-reversion language appears |
| Cycle School | Lesson 28: what goes up rises slower — Band 2's closing lesson |

Designs: **PS-D1** H56's promotion test (runsheet step 77, registered before the look).
**PS-D2** the listed-vs-macro share wedge as its own diagnostic (design only).

## Part H — Knowledge ledger (atlas 2.15; BAND 2 CLOSES)

**Established (our runs):** relative capital-share reversion at 85%/114-country breadth (PS1);
NO decline-prediction at extremes (PS2's fail — the design-sharpening result); India's macro
share already at its 81st percentile in 2019, pre-tripling (PS3). **Candidate [H56]:** the
extrapolation governor, instrumented, awaiting its listed series. **Unknowable:** whether
India's 2019-24 tripling extends — the seat governs the extrapolation instead of answering
the question. **Band-2 process ledger:** thirteen entries, zero unplanned seats, five labels
retired with prints (Juglar, Kitchin's clock, the dollar cycle, the Fed cycle, the oil
cycle), three candidates instrumented (H54/H55/H56), one seat calibrated (L6), two modules
shipped (L14 here; L11 in Band 1's finale), the frequency sweep closed, and the ENSO control
group sealing the doctrine: states and bands, never dates.
