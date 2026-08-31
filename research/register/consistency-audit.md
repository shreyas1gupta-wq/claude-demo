# Internal-Consistency & Arithmetic Audit — DESIGN.md v0.9 vs config/ vs CONTRACT/OPEN_QUESTIONS

Auditor role: adversarial, internal-consistency + arithmetic only (no web). Default skeptical;
only findings that survived my own recomputation are reported. `python3 config/validator.py`
was run: **0 errors, 2 warnings (funding_rate unset; ADV table PROVISIONAL) — registry loads
clean.** Note throughout: a clean validator run is necessary, not sufficient — several findings
below are gaps the validator's own checks cannot see (aggregation semantics, prose-vs-config
drift, cross-dossier arithmetic), not violations of the checks it actually runs.

---

## CRITICAL

### C1. `macro_credit_block` budget: DESIGN.md prose says 25%, the registry runs on 20% — and 25% would break the registry's own invariant
DESIGN.md §4.1 ("budget caps per §4.1 ... macro-credit block ≤25% ...") and §4.2 heading
("share one **macro-credit block budget** (≤25% of regime score)") both state **25%**, twice.
`config/ladder.yaml` commits `macro_credit_block: 0.20` (20%). This is not cosmetic: the six
`regime_score_blocks` must sum to ≤1.0 (ladder.yaml's own header comment, enforced by
`validator.py`'s `sum(budgets.values()) > 1.0` check). Recomputed: `0.25 (fast_stress) + 0.20
(trend_tsmom) + 0.20 (macro_credit_block) + 0.20 (global_cycle) + 0.10 (valuation_sentiment) +
0.05 (calendar) = 1.00` exactly — using config's 20%. Substituting DESIGN's stated 25% gives
**1.05**, which would fail to load under the registry's own rule. DESIGN.md's own ladder table
(§4.1, L10 row) hedges with "≤20–25% of budget," splitting the difference — so there are three
different numbers for the same cap across one document (25% flat prose ×2, "20–25%" in the
table, 20% in config), and only the 20% figure is arithmetically compatible with the design's own
"sum ≤ 1.0" rule. **Fix**: correct DESIGN.md §4.1 and §4.2 to 20% (or to "≤20–25%, resolved to
20%"), matching the registry that actually governs.

### C2. A Tier-C entry (L11, capex cycle) can add — not just reduce — regime score, through the shared-block average, with nothing in DESIGN.md, ladder.yaml, or validator.py stopping it
Contract §4: "Tier-C signals may only REDUCE risk — never add." `ladder.yaml` correctly flags
L11 `tier: C, reduce_only: true`. But L11's `block` is `macro_credit_block` — one of the six
**additive** `regime_score_blocks`, not the segregated `tierC_overlay` (the only bucket the
validator actually caps at ≤0.10 and treats as negative-only). DESIGN §4.2's own de-duplication
rule says the L6+L10+L11+L12 composite "uses the first principal component or a simple average —
never four full weights." A simple average of four series, three of them (L6/L10/L12) full-
authority Tier B with no sign restriction, blends in L11's own reading with no floor/clamp
described anywhere that forces L11's *contribution to the shared score* to be ≤0. If L11 reads
positive (capex cycle turning up), a plain average necessarily pushes the shared macro-credit
score up — i.e. **adds** regime-score budget — exactly what a Tier-C entry is forbidden to do.
Contrast with L1/L13/L14/L15, which are correctly isolated in `tierC_overlay` (capped, negative-
only by construction, per validator's separate check). Compounding evidence: DESIGN.md's own
ladder table (§4.1) row for L11 states its "Cap / expression" as "Inside macro block, shared cap;
correlated with L10 — never double-counted" — it never says "reduce-only" in prose, unlike the
L1/L13/L14 rows which explicitly do. `validator.py`'s check (`tier=='C' and block in budgets and
not reduce_only → err`) only inspects the **flag**, not the **aggregation formula** — so the
registry loads clean while the actual composite math has no enforced one-directionality for L11.
**Fix**: either move L11 into `tierC_overlay` (losing its correlation-sharing with L10/L12, which
§4.2 explicitly wants to avoid double-counting), or specify explicitly — in both DESIGN §4.2 and
the registry — that the shared composite clamps L11's own reading to `min(0, L11_reading)` before
averaging, and add a validator check that inspects composite-formula sign-safety for any Tier-C
member of an additive block, not just its flag.

### C3. §2.1's build-time arithmetic does not reproduce from its own stated inputs — and directly contradicts D05's own table by 4–17×
DESIGN §2.1: "A 5.5% entry at ₹25,000cr (conservative top) = ₹1,375cr/position... Liquidity:
rank-300 ADV ≈ ₹20–40cr/day [A: provisional ADV table, D05 §4b]; **at 10%/day participation a
full build takes ≈32 weeks; at rank 100–150, 2–5 weeks.**"

Recomputing with the paragraph's own numbers (`days = Q/(ADV×p)`, `Q=₹1,375cr`, `p=10%/day`):
- Rank-300 ADV ₹20–40cr/day → days = 1375/(20×0.10) to 1375/(40×0.10) = **687.5 to 343.75 days
  ≈ 137.5 to 68.75 weeks** — not "≈32 weeks." Even the fastest case (top of the ADV range) is
  more than double the stated figure.
- Rank-100–150 ADV, per `costs.yaml`'s own `r51_150: [80,150]cr/day` bucket → days =
  1375/(80×0.10) to 1375/(150×0.10) = **171.9 to 91.7 days ≈ 34.4 to 18.3 weeks** — not "2–5
  weeks." Off by roughly 4–17×, even before considering that positions this far down the rank
  list would actually use the reduced small-ticket entry weight (2.5–4%, not 5.5%), which only
  narrows the gap to ~8–25 weeks, still nowhere near "2–5 weeks."

D05 §4e's own days-to-build table — the document DESIGN.md cites for this exact claim — directly
confirms the recomputation and refutes DESIGN's restated numbers: its **Conservative, rank
50–150** row gives "80 (≈16 wks) / 160 (≈32 wks, ~7.5mo)," an order of magnitude larger than
DESIGN's claimed "2–5 weeks" for essentially the same rank range and book. The "≈32 weeks" figure
in DESIGN §2.1 also looks like a straight lift of D05's **Moderate, rank 150–300** row ("32.1
(≈6.4 wks)") — i.e. D05's own **day** count (32.1 days) appears to have been re-labeled as
**weeks** in DESIGN.md, a 5× unit-conflation, applied moreover to the wrong book (conservative,
not moderate) and a different rank bucket (300 vs 150–300). This arithmetic underlies the "stated
universes and entry weights cannot coexist" argument that motivates the two-universe design
resolution (§2.1's "Resolution adopted") — the resolution itself is sound, but the specific
numbers offered as its evidentiary basis do not hold up and should be replaced with a clean
recomputation from the paragraph's own stated position size, or from the correct rows of D05's
own table.

---

## MAJOR

### M1. Index-futures statutory round-trip cost: DESIGN/D05 claim ≈7.7bps; the stated formula sums to ≈5.66bps — and D05 contradicts itself
DESIGN §9.1: "Index futures ≈ 7.7bps statutory ⇒ 10–18bps all-in." D05 §4a gives the formula
explicitly: "0.05% (STT, sell only) + 0.002% (stamp, buy only) + 2×0.00183%×1.18 (exch+GST) +
2×0.0001%×1.18 (SEBI+GST) ≈ 0.0765% (≈7.7bps)." Summing the dossier's own stated terms:
`0.05 + 0.002 + (2×0.00183×1.18) + (2×0.0001×1.18) = 0.05 + 0.002 + 0.0043188 + 0.000236 =
0.0565548% ≈ 5.66bps` — not 7.7bps. The method is verified correct by applying it to cash
delivery with the same dossier's inputs: `0.20 (STT both legs) + 0.015 (stamp) + 0.00634
(exch×2) + 0.0002 (SEBI×2), GST 18% on exch+SEBI → 0.2227% ≈ 22.3bps`, which matches the stated
22.3bps exactly — confirming the arithmetic method, not just my transcription, is sound, and
that the discrepancy is specific to the futures line. D05 itself is internally inconsistent: an
earlier passage (§4d intro, line 172) states "NIFTY futures run ~6bps round trip before
brokerage — roughly a 3.5–4× gap [vs cash]," which matches my ~5.66bps recomputation and directly
contradicts its own later "≈7.7bps... roughly 3× cheaper" derivation two sections down. The
error (~2bps, ~36% relative) propagates: `config/costs.yaml`'s `round_trip_all_in_bps.
index_futures: [10, 18]` reverse-engineers almost exactly from 7.7bps + a 2–10bps brokerage
round trip (7.7+2≈10, 7.7+10≈18) — i.e. it was built on the erroneous number; using the correct
≈5.66bps the all-in bucket should be closer to **[8, 16]bps**. It also affects the "~3× cheaper
than cash" framing repeated in DESIGN §2.4 ("cash ≈22–32bps vs index futures ≈10–18bps — futures
are ~3× cheaper") — the corrected ratio (22.3/5.66) is **≈3.9–4×**, matching D05's own
uncorrected alternate statement, not the ~3× figure the design currently states everywhere.
This doesn't change Decision Q3 (margin funding was chosen for reasons independent of the
futures-cost comparison), but it is a wrong, "verified," Tier-B-confidence number in the frozen
cost registry that other calculations (§9.3, the futures-overlay-alternative threshold in §2.4)
build on.

### M2. The conservative-book SAST mcap floor stored in the registry (₹19,000–31,000cr) does not reproduce from the mandate's own capital range or from D05's own arithmetic
DESIGN §2.1 cleanly derives the conservative-book top-of-range SAST floor: `₹25,000cr × 5.5% =
₹1,375cr; ÷5% = ₹27,500cr` — correct, and matches D05 §4g's own parenthetical check of the same
figure. But `config/books.yaml` ("mcap floor ~Rs19-31k cr") and `config/costs.yaml`
(`sast_disclosure_mcap_floor_cr: [19000, 31000]`) instead carry D05's headline range, which has
two separate defects when traced to source (D05 §4g):
1. **Upper bound arithmetic slip**: D05 computes the top of its range as "using the stated
   ₹1,540cr at 5.6%/₹25,000cr → ₹30,800cr." But `₹25,000cr × 5.6% = ₹1,400cr`, not ₹1,540cr —
   the position figure itself doesn't reproduce from the stated rate and NAV. Even accepting
   5.6% as the intended entry rate, the correct floor is `1,400/0.05 = ₹28,000cr`, not ₹30,800cr
   (rounded to "31,000" in config). Using the mandate's actual entry-cap ceiling of 6% instead:
   `25,000×0.06=1,500cr → ÷0.05 = ₹30,000cr` — the true upper bound under any correct reading of
   the 5–6% entry cap is ≤₹30,000cr, not ₹31,000cr.
2. **Lower bound uses the wrong capital floor**: D05 computes its low end from "₹17,500cr NAV,"
   not the Contract's actual stated conservative-book floor of ₹10,000cr (CONTRACT §1,
   `books.yaml capital_cr: [10000, 25000]`). At the mandate's true floor, `₹10,000cr × 5.5% =
   ₹550cr ÷ 5% = ₹11,000cr` — nearly half the registry's stated ₹19,000cr low end. The stored
   range silently excludes the ₹10,000–17,500cr portion of the mandate's own stated capital band
   with no documented reason.
   Net effect: the registry's "₹19,000–31,000cr" floor should read closer to **₹11,000–30,000cr**
   once corrected to the mandate's actual capital range and a consistent entry-rate assumption —
   materially widening (at the low end) the set of names the conservative book's full-conviction
   cohort could actually hold at lower AUM.

### M3. `mandate.yaml`'s small-ticket cohort cap (10%) is attributed to D11 §4d, but D11 §4d proposes 20%
`config/mandate.yaml`: `small_ticket_cohort_cap: {value: 0.10, source: "DESIGN §2.7 / D11 §4d
refinement..."}`. `research/dossiers/11-portfolio-construction.md` (§4d, restated in its "Open
design question" note): "...the in-progress cap split proposed in §4d (separate full-size-cohort
and small-ticket-cohort budgets, **both nominally '20%'**, but tracked independently)..." D11
explicitly proposes the small-ticket cohort get its own 20% ceiling, matching the full-size
cohort — not 10%. The committed registry value is exactly half of what the cited source proposes,
with no rationale recorded in DESIGN.md or mandate.yaml for the reduction (it may well be a
deliberate, more conservative principal choice — the registry's `changes_if` field even allows
for "principal ruling" — but as written, the provenance chain is broken: the number does not
trace to the source it cites, which Contract §6 requires of every constant in the design).

---

## MINOR

### N1. §5.2 worked example (R3) understates its own low end
"R3 at 0.75x, hedge 75%, eff. 0.65 → EffBeta ≈ 0.45–0.5." Recomputed using the stated
`DownsideBetaTilt` range (1.10–1.30, per `risk.yaml`): `EffBeta = tilt × 0.75 × (1 − 0.75×0.65) =
tilt × 0.75 × 0.5125` → **0.4228 (at tilt 1.10) to 0.4997 (at tilt 1.30)**, i.e. ≈0.42–0.50, not
0.45–0.50. The stated low end is about 0.03 (≈7% relative) too high. Doesn't change the
conclusion (still comfortably below the index in a slow bear) but is a genuine arithmetic slip
in a worked check the document holds up as a "cross-check that theory and the data-derived prior
agree" (§7.3).

### N2. §5.1's pre-tightening R4 breach parenthetical is off by ~0.1pp
"...at leverage 0.7 and hedge 0.75, effBeta×38%-fall + 15% gap floor = **37.8%**..." Recomputing
with the stated inputs (β=1.30, lev=0.70, hedge=0.75, HE=0.45, gap=0.15): `EffBeta = 1.30×0.70×
(1−0.75×0.45) = 0.91×0.6625 = 0.602875`; `0.602875×0.38+0.15 = 0.37909 ≈ 37.9%`, not 37.8%.
Trivial, doesn't change the conclusion (still breaches the 35% ceiling either way) — noted only
because the prompt asked for every piece of §5.2 arithmetic to be recomputed. By contrast, the
**post-tightening** check in `risk.yaml`'s comment (β=1.30, lev=0.60, hedge=1.00, HE=0.45, gap
=0.15 → EffBeta=0.429, worst=0.313≈31%) is exact and matches the validator's live computation
precisely — that one is clean.

### N3. "≈3–4 full days of ADV in a median microcap" uses the top of the ADV range, not the median
DESIGN §2.1: "5% entry at ₹250cr = ₹12.5cr ≈ 3–4 full days of ADV in a median microcap." Rank
501–750 ADV per `costs.yaml` is `[1, 4]cr/day`. To get 3–4 days from a ₹12.5cr position requires
ADV ≈ ₹3.1–4.2cr/day — the *top* of the stated range, not its median (≈₹2.5cr/day, which would
give ≈5 days). Doesn't change the qualitative point (tail names take days of ADV to enter even
a small ticket) but the word "median" is not what was actually used.

### N4. Decision Q10 record calls the special-situations sleeve "Tier-B"; the implemented design is a mix of B and C
`OPEN_QUESTIONS.md` Decision #10: "Capped **Tier-B** satellite sleeve, aggressive book only..."
DESIGN §6.4 / `sleeves.yaml` implement six event types with mixed, more granular tiers: index
inclusion/exclusion = B; buyback/tender = B; demergers = "C→B pending"; lock-in-expiry windows =
C (reduce-only); bulk/block-following = "C→B pending." The sleeve's own overall NAV cap (≤10%) is
itself tagged **Tier C, [A]** in both DESIGN §10 and `sleeves.yaml` ("the least-defended number
in D12... MUST be re-derived before it binds"). This is plausibly a legitimate, more honest
refinement of a one-word decision-record label rather than a violation, but the decision record
and the implemented tiering should be reconciled explicitly rather than left to look like a
mismatch.

---

## Confirmed correct (recomputed, no defect found)

- **§5.2 R1 worked example**: "R1 at 1.15x unhedged → EffBeta ≈ 1.3–1.5" — recomputes to
  1.10×1.15=1.265 to 1.30×1.15=1.495 ✓.
- **§5.2 / risk.yaml R4 post-tightening worst-case**: EffBeta=0.429≈0.43, worst=0.313≈0.31 ✓
  (matches validator's live run exactly).
- **§2.3 "2011-type −25% Nifty episode, unhedged that is −32% to −37%"**: 1.3×0.25=0.325,
  1.5×0.25=0.375 ✓.
- **§9.1 cash-delivery statutory cost, 22.3bps**: recomputes exactly from the stated rate table ✓.
- **D05 §4e days-to-build table** (the table itself, as opposed to DESIGN §2.1's restatement of
  it): every row checked (`days = (Q/ADV)/p`) reproduces correctly, including the week/month
  conversions ✓.
- **§5.6 ε/K worked example**: "TE ≈ 8–12%/yr, K=15 → ε≈2–3%" — using the standard √252 daily
  annualization, `TE_daily=8%/√252=0.504%→ε=0.504%×√15≈1.95%`; `12%/√252=0.756%→ε≈2.93%` — matches
  "≈2–3%" ✓. Components (`PortDD(t)`, `NiftyDD(t)`, `TE_daily`) are all legitimately computable
  from daily NAV + Nifty series alone with no external data required. **Gap, not an error**:
  neither DESIGN.md nor `mandate.yaml` specifies the trailing window over which `TE_daily` is
  measured (30d/60d/expanding?) — since tracking vol is strongly regime-dependent, ε is not yet
  a single well-defined computable number as written; this is flagged in the design's own [A]
  ledger implicitly (z and K are swept) but the TE-window choice isn't listed as a swept
  parameter anywhere and should be.
- **Ladder block-budget sum** (using config's actual 20% for macro-credit, not DESIGN's stated
  25% — see C1): sums to exactly 1.00 ✓.
- **Regime-bucket ranges, leverage/hedge monotonicity**: DESIGN §5.1 table and `risk.yaml`
  `regime_buckets` match exactly across all four buckets ✓.
- **Gold floors/ceilings, factor-book weight ranges, all decay haircuts spot-checked** (momentum,
  TSMOM, value, quality, low-vol, gold momentum, credit-block AUROC, issuance/sentiment): DESIGN
  prose and `sleeves.yaml`/`ladder.yaml` match exactly wherever cross-checked ✓.
- **All ten OPEN_QUESTIONS decisions**: cross-checked against DESIGN.md/config implementation —
  substantively honored in all ten cases (Q10's tier label is the one soft mismatch, N4 above).
- **Tier/reduce_only flag consistency at the individual-entry level**: every Tier-C ladder entry
  (L1, L11, L13, L14, L15, L16) correctly carries `reduce_only: true`; this is exactly what lets
  the registry pass clean despite C2's deeper aggregation-semantics gap — the flag check and the
  aggregation-safety check are different things, and only the former is implemented.
