# CIO Review — ₹500 Cr NDPMS Operating Blueprint (Seven Domain Designs)

Reviewer: Veteran multi-asset CIO (₹2,000+ Cr family-office/PMS experience)
Materials reviewed in full: data_facts.md/json, data_market.md/json, design_regulatory.md/json, design_allocation.md/json, design_rebalancing.md/json, design_risk.md/json, design_performance.md/json, design_selection.md/json, design_operations.md/json, and sel/tco.py (source of the Selection domain's TCO table).

---

## Overall assessment

This is an unusually rigorous set of documents for a first-pass operating design — the regulatory perimeter is well sourced and appropriately hedged ("approx.", "unclear_verify"), the Brinson-Fachler/TWRR/XIRR math in the Performance domain is internally exact to the decimal, and the NDPMS consent-latency framing (recommend → consent → execute, with a priced cost of delay) is threaded consistently through Regulatory, Rebalancing, Risk and Operations. The team clearly understands that in NDPMS, process discipline *is* the alpha engine.

But the seven documents were built in parallel and were not cross-audited against each other or against the two data packs before this review, and it shows. The most serious problem is a genuine, root-caused arithmetic bug in the Selection domain's total-cost-of-ownership model (`sel/tco.py`): a 100x unit-scaling error inflates the tax-drag estimate for gold, silver, arbitrage and REITs by roughly 10-25x, which then drives the domain's headline strategic conclusion ("tax drag is 317 of 376 bps — the biggest lever is instrument-tax-form selection, not manager alpha"). That conclusion should not survive into the merged blueprint as currently computed. Close behind: the Allocation and Risk domains produce two different loss estimates for the same GFC/COVID stress scenarios on the same Moderate/Aggressive portfolios; the Risk domain's own credit-floor limit is breached by the Allocation domain's own Moderate model portfolio (AA-rated credit is 16.7% of the fixed-income sleeve against a 10% house ceiling); the Allocation domain's headline five-sleeve weight table simply does not sum to 100% (it sums to 110%, in both models, from an apparent copy-paste error); and the Performance domain cites the wrong regulation number for the client-reporting cadence relative to three other domains. None of these are: fatal to the design's structure, but all of them would seriously embarrass the team if a sophisticated client's family office ran a spreadsheet audit, which family offices of this size routinely do.

There is also a live, unresolved disagreement about what the actual "Policy Composite" benchmark is — Allocation and Performance each independently invented one, with different weights, and nobody has reconciled them. Given that this composite is the yardstick the team is accountable against, that needs to be a Day-1 decision, not an implicit assumption. Finally, a handful of "hard fact" claims (custodian AUM exemption threshold, a 2026 MF brokerage-cap reform) are asserted without any corroboration in the (very thorough) verified fact pack and should be treated as unverified until pulled from a primary source.

---

## Findings

### High severity

**1. [selection] `sel/tco.py` tax-drag formula has a 100x unit-scaling bug for gold, silver, arbitrage and the REIT LTCG leg — the Selection domain's headline TCO conclusion is built on inflated numbers.**
- Target: design_selection.md §9 Total Cost of Ownership table; `sel/tco.py` lines for Gold ETF (`8.0*0.10*LTCG*1e4` → 1,196 bps), Silver ETF (`8.5*0.20*LTCG*1e4` → 2,542 bps), Arbitrage fund (`6.4*0.20*LTCG*1e4` → 1,914 bps), and the REIT/InvIT LTCG term (`9.5*0.10*LTCG*1e4` → 1,420 of the row's 1,624 bps).
- issue_type: factual_error. severity: high. confidence: high (root-caused directly in the code).
- Detail: elsewhere in the same script (Nifty 50/100, factor, active-MF and direct-equity rows), the tax formula correctly uses *decimal-fraction* turnover/gain-ratio inputs (e.g. `0.05*0.30*LTCG*1e4`), which is dimensionally correct (`decimal × 1e4 = bps`). But for gold, silver, arbitrage and REIT the code instead plugs in the *raw percentage number* for expected return (e.g. `8.0` meaning "8%", not `0.08`) into the same `×1e4` formula — producing a result exactly 100x too large. Recomputed correctly: gold's tax drag is ≈12 bps, not 1,196; silver ≈25 bps, not 2,542; arbitrage ≈19 bps, not 1,914; REIT's LTCG leg ≈14 bps (total REIT row ≈218 bps), not 1,420 (1,624 total). This single bug is responsible for the great majority of the table's reported 317-bps portfolio-level tax drag, which is 4-7x higher than every other domain's independent tax-drag estimate for the same ₹500 Cr book (design_allocation: 60-80 bps; design_performance: 45 bps realised; design_rebalancing's Monte Carlo: 10-50 bps at realistic turnover).
- Suggested fix: fix the four affected lines in `sel/tco.py` (use decimal fractions consistently, or fix the exponent), rerun, and re-derive the "tax drag dominates" narrative in §9 only after the corrected run — it may still be a real (smaller) effect, but the current magnitude and the "biggest single lever" conclusion is not supportable as computed.

**2. [allocation ↔ risk] The GFC- and COVID-type stress-shock estimates for the *same* Moderate/Aggressive portfolios disagree materially between the two documents that are supposed to share the same model.**
- Target: design_allocation.md §3.3 ("GFC-type shock... Moderate −29.5%, Aggressive −39.8%"; "COVID-type shock... Moderate −19.7%, Aggressive −26.8%") vs design_risk.md §3 stress library ("GFC... Mod −₹160 Cr [−32.0%], Agg −₹215 Cr [−43.0%]"; "COVID crash... Mod −₹114 Cr [−22.8%], Agg −₹144 Cr [−43.0%... i.e. −28.8%]").
- issue_type: inconsistent. severity: high. confidence: high.
- Detail: design_risk.md explicitly states it uses "the same vol/beta/correlation assumptions as the allocation design," yet the two documents' own historical-stress outputs for the identically-labelled scenarios differ by 2.5-3.5 percentage points on every comparison (Moderate GFC: −29.5% vs −32.0%; Aggressive GFC: −39.8% vs −43.0%; Moderate COVID: −19.7% vs −22.8%; Aggressive COVID: −26.8% vs −28.8%). Separately, data_market.md's own worked sizing for the *house 80/20 benchmark* ("a 2008-type shock (−60%/+6%) is −47% [≈₹235 Cr]") also disagrees with design_allocation.md's own 80/20 GFC-shock figure of −42.6%. A client who is shown the risk dashboard and the allocation deck in the same meeting will see two different answers to "how bad could 2008 be for me."
- Suggested fix: designate one shock-scaling methodology as canonical (recommend risk_calc.py, since it is closer to a full re-pricing) and republish design_allocation.md §3.3 to match it before either table reaches a client.

**3. [risk ↔ allocation] The Moderate model portfolio breaches the Risk domain's own credit-floor limit.**
- Target: design_risk.md §1, Limit #7 ("Credit floor — corporate bonds/NCDs: AAA/AA+ only, min 90% of FI sleeve; AA min issuer rating") vs design_allocation.md §3.1 Moderate model (fixed-income sleeve = short duration 3% + TMF 11% + G-sec 6% + AA corporate credit 4% = 24% of AUM).
- issue_type: inconsistent. severity: high. confidence: high.
- Detail: the 4%-of-AUM "AA corporate credit" line is 4/24 = 16.7% of the 24%-of-AUM fixed-income sleeve — but the Risk domain's own house limit requires at least 90% of the FI sleeve to be AAA/AA+, i.e. at most 10% can be plain-AA. The proposed Moderate model as published breaches this by ~6.7 percentage points of the FI sleeve on day one, before any market move. (The Aggressive model has no AA-credit line and does not have this problem.)
- Suggested fix: either trim the Moderate AA-credit line to ≤2.4% of AUM (10% of the 24% FI sleeve) or loosen Limit #7 to allow the proposed weight — but the two documents must agree before either goes into the IPS.

**4. [allocation] The five-sleeve architecture table does not sum to 100% — it sums to 110%, in both the Moderate and Aggressive models.**
- Target: design_allocation.md §2.1 ("Core beta 32% / Satellite alpha 33% / Alternatives 9% / Stabilisers 24+4+6=34% / Liquidity 2%" = 110% for Moderate; "37/44/12/15/2" = 110% for Aggressive).
- issue_type: factual_error. severity: high. confidence: high.
- Detail: re-summing the underlying line items in §3.1/§3.2 (which do total 100% correctly) shows Satellite alpha should read 23% (Moderate: active mid 7 + active small 3 + direct stocks 8 + international 5) and 34% (Aggressive: 10+5+12+7), not the 33%/44% printed — a consistent 10-percentage-point overstatement in both models' summary table. This is the kind of basic addition error a client's own analyst checks first.
- Suggested fix: correct the Satellite alpha row to 23% (Moderate) / 34% (Aggressive) so the sleeve table foots to 100%.

**5. [performance ↔ regulatory/risk/operations] The client periodic-reporting regulation is cited inconsistently — "Regulation 22" in one domain, "Regulation 31" in three others.**
- Target: design_performance.md §0.3 and §5.1 ("Client reporting floor = PMS Regulations 2020, Regulation 22... Reg. 22 tightened this from the prior 6-month cycle") vs design_regulatory.md §1.5 ("Report to client ≤ every 3 months (Reg 31)"), design_risk.md (uses the same Reg 31 framing via [12] cross-reference), and design_operations.md source list ("Regulation 31 (client reporting) text").
- issue_type: inconsistent. severity: high. confidence: medium (three-vs-one internal disagreement is certain; which number is actually correct was not independently verified by any domain since primary SEBI text could not be fetched this session).
- Detail: this is not a stylistic slip — a compliance filing or a client MITC document that cites the wrong regulation number for its own reporting obligation is a real regulatory-documentation risk, and three of the seven domains cannot both be wrong for the same reason.
- Suggested fix: before merge, pull the actual PMS Regulations 2020 text (or a single authoritative secondary source) and standardise on one regulation number across all seven documents; do not let this ship as an unreconciled 3-vs-1 split.

**6. [rebalancing] Worked Example B's cost table does not check out arithmetically — a client's own quant would catch this in minutes.**
- Target: design_rebalancing.md §5.3, "Worked example B — ₹40 Cr ETF switch," On-screen secondary-market row (total "≈₹59 lakh (≈15 bps)") and AP/direct-with-AMC row (total "≈₹20 lakh (≈5 bps)").
- issue_type: factual_error. severity: high. confidence: high.
- Detail: ₹59.4 lakh on a ₹40 Cr trade is ≈148 bps, not ≈15 bps (a 10x discrepancy); ₹20.4 lakh on the same trade is ≈51 bps, not ≈5 bps (same 10x pattern). Separately, even taking the row's own printed component bps at face value, they don't sum to the row's own stated total (0.1+10+19 = 29.1 bps ≠ the printed "≈15 bps"). The directionally correct conclusion — routing via AP/AMC saves real money — survives, and the §5.1 cost-stack table's own ≈5-7 bps AP-route estimate is plausible and consistent with the rest of the document; but the specific worked numbers in §5.3 need to be rebuilt before they are shown to anyone.
- Suggested fix: rebuild Worked Example B from the §5.1 cost-stack table's per-bps assumptions and re-derive the ₹ amounts (or vice-versa), and add a self-check (Σcomponent bps = total bps; ₹total / trade size × 10,000 = bps total) to every future worked example in this document set.

**7. [risk ↔ allocation/regulatory, vs data_market] The Risk domain's live early-warning dashboard is anchored to a stale/wrong USDINR level (~₹88) against a verified current spot of ₹95.79 — an ~9% error that originates in, and is shared by, two other domains.**
- Target: design_risk.md §6, "USDINR (spot ~₹88 [design_allocation.md])" vs data_market.md T6 ("USDINR ~95.79 (record-low rupee territory), 11-Sep-2026, verified") and data_facts.md; the ₹88 figure originates in design_allocation.md §4 ("≈₹2.2 Cr at ~₹88/USD approx.") and is reused in design_regulatory.md §6 ("LRS capacity... N=5 → ₹11 Cr/yr" — computed at ₹88, not ₹95.79).
- issue_type: factual_error. severity: high. confidence: high.
- Detail: the verified data pack sitting in the same project (data_market.md) records USDINR at a record-low 95.79 as of 11-Sep-2026 — the same date the risk dashboard claims to be current as of. Using ₹88 understates the family's LRS/GIFT-City headroom by roughly 8-9% (the correct figure is closer to ₹12 Cr/yr for 5 adults, not ₹11 Cr/yr) and gives the FX early-warning board a reference point that is already wrong before day one.
- Suggested fix: replace every ₹88/USD reference across design_allocation.md, design_regulatory.md and design_risk.md with the verified 95.79 (or a live feed at go-live), and re-run the dependent ₹ figures.

**8. [performance ↔ allocation] Two different, independently authored "Policy Composite" benchmarks exist for the same mandate, and neither document acknowledges the other's version.**
- Target: design_performance.md §2.2 Table 3 ("Domestic equity 55% / International 7% / FI 22% / AIF CatII 4% / REITs 4% / Gold+Silver 5% / Cash-arbitrage 3%") vs design_allocation.md §3.3 ("55% Nifty500 TRI + 5% S&P500 TRI(INR) + 25% CRISIL Composite Bond + 5% gold + 10% Nifty 50 Arbitrage Index").
- issue_type: inconsistent. severity: high. confidence: medium-high.
- Detail: both are explicitly labelled the authoritative T2/mandate benchmark that alpha, fees and the IC scorecard will be judged against, yet the international weight (7% vs 5%), fixed-income weight (22% vs 25%), and treatment of REITs/AIFs (separately benchmarked with their own indices/PME in Performance vs folded into an arbitrage-return proxy in Allocation) all differ. Design_performance.md does flag its own table as "illustrative... to be replaced by the SAA layer's final weights," which is the right instinct, but as published this reconciliation has not happened, and it is the single most consequential number for "owning the returns."
- Suggested fix: pick one document as the source of truth for sleeve weights (recommend Allocation, since it is the SAA layer) and regenerate Performance's Table 3 from it exactly, with an explicit sign-off step before the IPS is signed.

**9. [selection] The domain's central strategic conclusion ("tax drag dominates the TCO... the biggest lever is instrument-tax-form selection, not manager alpha") is built on an unrealistic full-annual-realization assumption for buy-and-hold sleeves, independent of the code bug in Finding 1.**
- Target: design_selection.md §9, and `sel/tco.py`'s tax-drag inputs for short-duration, target-maturity, G-sec, AA-credit, Cat II and Cat III lines (each computed as `E[R]% × tax-rate × 100`, i.e. as if the entire sleeve's return is realized and taxed every single year).
- issue_type: overstated. severity: high. confidence: medium.
- Detail: this modelling choice is dimensionally self-consistent (unlike Finding 1) but directly contradicts the "hold-to-maturity, low-turnover" philosophy stated repeatedly in design_allocation and the 4-15%/yr realistic turnover figures modelled in design_rebalancing's own Monte Carlo (§2.3). Debt-fund/target-maturity/AIF gains held in a growth structure are not actually taxed annually — tax crystallizes on redemption, which for a "hold-to-maturity" TMF or a 3-7 year locked AIF could be years away. Treating the full annual yield as if fully taxed every year (correct only for coupon-bearing direct bonds and pass-through AIF interest, which genuinely are taxed as received) overstates real cash tax drag for the fund-wrapped stabiliser sleeves by a large, unquantified multiple.
- Suggested fix: separate "cash tax paid this year" (interest/coupon/distributed income — correctly taxed annually) from "deferred tax on unrealized gains" (only crystallizes on redemption) exactly as design_performance's own R3/R4 framework already does, and re-run §9 on that basis.

### Medium severity

**10. [operations] The Investment Committee is described as having "six voting members" but only five of the six named seats are voting.**
- Target: design_operations.md §1.1 ("Six voting members, quorum 4... CIO (chair), Head of Research/PM for the mandate, Head of Risk, Head of Compliance, Head of Trading/Ops (non-voting, present for feasibility), one independent/senior advisor (non-executive, tie-break)").
- issue_type: inconsistent. severity: medium. confidence: high.
- Detail: of the six named seats, Head of Trading/Ops is explicitly marked non-voting, leaving five voting members, not six — and a quorum of 4 out of 5 (80%) is a materially different governance bar than 4 out of 6 (67%).
- Suggested fix: either make Trading/Ops voting (making it genuinely six) or correct the text to "five voting members, quorum 4" and re-check the quorum threshold makes sense at 5.

**11. [allocation ↔ selection, vs data_market] Nifty BeES AUM is cited as ₹66,777 Cr in two domains but as ~₹53,989 Cr ("partially_verified") in the project's own market data pack — a ~24% gap in the instrument used to size the whole ETF execution plan.**
- Target: design_allocation.md §4 ("Nifty BeES AUM ₹66,777 Cr") and design_selection.md §1.2 ("Nippon India ETF Nifty BeES... ~66,777 (9-Sep-2026)") vs data_market.md T7 ("Nippon India ETF Nifty 50 BeES (NIFTYBEES)... ~53,989 - partially_verified").
- issue_type: inconsistent. severity: medium. confidence: medium.
- Detail: per the review brief, the verified data pack should generally be preferred over designer assertions where they conflict; here two of three domains agree with each other but disagree with the (also imperfectly verified) data pack. Either way, the ADV/impact-cost sizing logic built on this number ("₹100 Cr basket/day = ~0.3% of Nifty 50 ADV" etc.) should be re-run against one confirmed figure.
- Suggested fix: pull the live NIFTYBEES AUM figure at go-live and use one number across all documents.

**12. [allocation] Folding REITs/InvITs (assumed vol ~14%, E[R] ~9.5%) and half the Alternatives sleeve into a "Nifty 50 Arbitrage Index" proxy (vol ~1.4%, E[R] ~6.2%) inside the composite benchmark will structurally understate the benchmark's true risk and return, making the portfolio's "beat the composite" alpha claim easier to earn than it should be.**
- Target: design_allocation.md §3.3, composite-benchmark rationale ("private credit → bond index... long-short → arbitrage + 50% Nifty").
- issue_type: overstated. severity: medium. confidence: medium.
- Detail: this is a genuine benchmark-construction methodology choice, not a data error, but it means the reported alpha (+55 bps Moderate, +45 bps Aggressive per §3.3) is partly an artifact of comparing a real REIT/alternatives sleeve against an unrealistically low-risk, low-return proxy for those same assets. A sophisticated client's investment consultant would flag this as benchmark gaming even if unintentional.
- Suggested fix: benchmark REITs against the Nifty REITs & InvITs Index (as design_performance.md's Table 3 already correctly does) and alternatives against a PME/absolute-return proxy plus a stated hurdle, not against arbitrage.

**13. [regulatory] The claim that PMS custodian appointment has "a historic <₹500 Cr AUM exemption" that "binds anyway" at this AUM is not corroborated anywhere in the verified fact pack and is not re-checked by any other domain.**
- Target: design_regulatory.md §1.5 ("Custodian for securities... mandatory for PMs (historic <₹500 Cr AUM exemption; at ₹500 Cr+ it binds anyway)").
- issue_type: regulatory_misstatement. severity: medium. confidence: low (data_facts.md is silent on any AUM-linked custodian exemption; this specific number could be right or wrong, but it reads as designer recall rather than a sourced fact).
- Suggested fix: verify this specific carve-out (or drop the parenthetical) against the primary PMS Regulations custodian clause before the operating model relies on it.

**14. [rebalancing ↔ selection] Both domains independently cite a "SEBI (Mutual Funds) Regulations, 2026" package (exit-load cap cut 5%→3%, BER replacing TER, brokerage cap cuts) that appears nowhere in the verified fact pack, and the two domains state the brokerage-cap change inconsistently.**
- Target: design_rebalancing.md [11] ("exit-load cap cut from 5% to 3%... brokerage caps cut to 6 bps (cash)/2 bps (derivatives), effective 1-Apr-2026") vs design_selection.md §1.1 ("cash-market brokerage caps were cut from 12 bps to 6 bps (derivatives 5→2 bps)") vs data_facts.md T7 ("TER slabs... were not found/verified this session — treat any TER slab table elsewhere as approximate").
- issue_type: regulatory_misstatement. severity: medium. confidence: low-medium.
- Suggested fix: verify this 2026 MF reform against a primary SEBI source (it materially affects the ETF/index-fund cost assumptions used throughout the Allocation and Selection domains) and reconcile the two different "before" brokerage figures (12 bps vs unstated) before relying on it.

**15. [performance] Table 5's cost/tax "budget" (~97 bps + 45 bps tax) risks double-counting against the document's own R0–R4 waterfall, which already embeds bid-ask/impact and consent-latency cost inside R1.**
- Target: design_performance.md §3.5 Table 5 ("Total explicit + implicit (ex-TER, ex-cash drag) ~97 + 45 tax") vs §1.1's own decision rule ("implementation is judged on R0−R1... separately, not subtracted a second time") and the §3.5 worked example's own footnote ("bid-ask/impact and TER stay embedded in R1 and are not subtracted again here").
- issue_type: inconsistent. severity: medium. confidence: medium.
- Detail: Table 5 lists "Bid-ask/market impact (5 bps)" and "Consent-latency shortfall (15 bps)" as budget lines that sum into the ~97-bps headline, but the worked R1→R2 bridge two paragraphs later explicitly excludes exactly those two items because they are already inside R1. A reader who takes the ~97-bps figure as "the additional drag on top of the R1 return" will double-count 20 bps that is already priced in.
- Suggested fix: relabel Table 5 as a total-cost-of-ownership reference (informational) rather than a bridge, or split it explicitly into "already inside R1" vs "R1→R2 bridge" columns.

**16. [multiple domains] The consent-latency "cost" formula (position × daily vol × √days) used identically in design_regulatory §5.2, design_rebalancing §1 and design_risk §2.7 presents a symmetric 1-sigma dispersion measure as if it were a one-directional expected cost.**
- Target: design_regulatory.md §5.2 ("Latency cost model: expected cost of delay = |target − actual| weight × daily vol × sqrt(days)"); repeated in design_rebalancing.md §1 and design_risk.md §2.7.
- issue_type: overstated. severity: medium. confidence: medium.
- Detail: in a genuinely symmetric random walk, the *expected* P&L cost of a pure timing delay is close to zero (the client is as likely to benefit from the wait as lose from it) — what is real is (a) tail/regret risk and (b) the fact that IC recommendations are directional, not random, so a delayed buy in a rising, IC-forecast-correct market is a real opportunity cost. The documents are reasonably careful to label the number "1-sigma," but the narrative language around it ("costs ₹79 lakh," "this is why...") reads as a certain cost rather than a risk-dispersion estimate, which could mislead the IC or the client about what the number actually represents.
- Suggested fix: reframe as "consent-latency risk (1-sigma dispersion of the delay's P&L impact)" throughout, and separately quantify the directional opportunity cost using the IC's own historical hit-rate on tactical calls (design_performance.md already tracks TAA hit rate — reuse it here).

**17. [multiple domains] The mandate's entire consent/standing-instruction architecture is built on the client's LVAI/accredited-investor status, but no document addresses what happens if that status lapses mid-mandate.**
- Target: design_regulatory.md §2 ("Decision: Must [onboard as LVAI]... It is the only route that lets a bespoke NDPMS agreement carry the monthly-consent machinery we need"); data_facts.md's own caution ("Accreditation, once granted, is [not] permanent — wrong: accreditation has a limited validity requiring periodic renewal").
- issue_type: missing. severity: medium. confidence: medium.
- Detail: design_operations.md's IPS document structure captures "accreditation status (LVAI certificate ref, validity date)" as a field to track, but no domain specifies the contingency if accreditation is not renewed — does the bespoke agreement (Schedule IV exemption, negotiated exit load) automatically revert to standard PMS terms? Is there a grace period? Given how load-bearing this status is to the whole operating model, this is a real single-point-of-failure gap.
- Suggested fix: add an explicit accreditation-lapse contingency clause to the NDPMS agreement and a renewal-tracking trigger (e.g., 90 days before expiry) to the operations calendar.

### Lower severity / verification items

**18. [allocation ↔ rebalancing] Minimum trade-size threshold is stated inconsistently: "₹1 Cr (20 bps)" in design_allocation.md §5.3 vs "₹75 lakh–₹1 Cr (≈15-20 bps)" in design_rebalancing.md §2.2.**
- issue_type: inconsistent. severity: low. confidence: high.
- Suggested fix: pick one number; the two are close enough that this is a documentation-hygiene fix, not a design problem.

**19. [risk] The early-warning board's 10-year G-sec yield anchor ("current ~6.95-7.0% [design_allocation.md]") is stale relative to the project's own verified market snapshot ("10Y G-sec yield >7.00%... 10-month high, 11-Sep-2026, verified" in data_market.md T6).**
- issue_type: factual_error. severity: low-medium. confidence: medium (small in magnitude, but the same root cause as Finding 7 — a live dashboard citing a design document instead of the verified data pack).
- Suggested fix: source the dashboard's reference anchors from data_market.md/a live feed, not from a sibling design document.

**20. [selection] The SIF-vs-Cat-III post-tax comparison (§5.1) assumes a Cat III blended fund-level tax rate of "≈28%" without stating what income-mix assumption drives that blend; a fund running more F&O/business income would push the effective rate toward MMR (~42.7%), reversing much of the modelled SIF advantage.**
- issue_type: overstated. severity: low. confidence: low.
- Suggested fix: state the assumed LTCG/STCG/business-income mix explicitly and show the comparison at both a "mostly capital gains" and a "mostly business income" Cat III fund, since real-world Cat III strategies vary widely on this axis.

**21. [regulatory ↔ risk] The 2026 SEBI PMS consultation-paper's proposed derivative/short limits (1.25x total exposure, 50% AUM unhedged shorts via ETD, 10% option-premium cap) are placed inside design_risk.md's Limit #10 table alongside today's binding legal ceiling, distinguished only by a bracketed "(not yet notified)" — a reader skimming the table could mistake pipeline for law.**
- issue_type: inconsistent. severity: low. confidence: low.
- Suggested fix: move all "2026 proposal" figures out of the hard-limit tables into a separate "watch list" row/column so current-law and pipeline numbers cannot be visually conflated.

---

## Top missing items (a ₹500 Cr NDPMS operating model needs, not adequately covered anywhere)

1. **Accreditation-lapse contingency** for the LVAI status the entire consent architecture depends on (Finding 17) — no document specifies the fallback if it is not renewed.
2. **NRI/FEMA branch logic.** The mandate repeatedly references "several family accounts" aggregated into one Investment Approach and a family-wide LRS/GIFT-City international sleeve, but no document asks whether any family member is an NRI — which would trigger an entirely different FEMA/PMS regime (NRE/NRO accounts, repatriation limits, RBI-level conditions) than the resident-only framework assumed throughout the RBI/FEMA tables.
3. **In-specie transfer-in / legacy-holdings transition plan.** Every deployment schedule in design_allocation.md assumes ~100% fresh cash arriving over 8-12 weeks; there is no due-diligence, suitability-vs-model, or tax-lot-inheritance plan for a family transferring in existing concentrated stock or fund positions, which is a very plausible scenario at this AUM.
4. **A single, reconciled Policy Composite benchmark** with one named owner and a sign-off date (Finding 8) — this needs to exist before the IPS is signed, not be inferred from two conflicting tables.
5. **Data-privacy/DPDP Act 2023 compliance** for the extensive PII/KYC/accreditation-certificate data architecture built in design_operations.md §5.3 — entirely unaddressed across all seven documents.
6. **Client liquidity/redemption-notice commitment,** stated explicitly to the client (not just internal recon logic) — e.g., "T+X days for up to Y% of AUM, T+Z for the rest" — given 12-15% of the book sits in 3-7-year locked AIFs and a family office of this size could plausibly need a large redemption for reasons unrelated to markets (a property purchase, a business need).
7. **Suitability linkage from client profile to model choice.** All seven documents build out the Moderate model in exhaustive detail but never show the risk-tolerance/horizon/liquidity-need questionnaire or IC minute that justifies Moderate (vs Aggressive, vs a bespoke blend) for this specific family — a real SEBI-inspection and client-conversation gap.
8. **A canonical, dated market-data snapshot** that every domain cites from, rather than each domain independently quoting its own search-result Nifty close/USDINR/10Y level on slightly different dates (contributing to Findings 7 and 19) — one dated table, refreshed at go-live, referenced everywhere.
9. **Legal-entity/no-pooling compliance mapping** for the "several family accounts... one Investment Approach" structure mentioned in design_performance.md — PMS Regulations bar pooling of client assets; the documents need to show explicitly how per-account custody and IA-level TWRR aggregation coexist without breaching that rule.
10. **Succession/incapacity planning at the client end** — the operations domain covers key-person risk on the PM's side (§8.2) but not what happens to the consent workflow (who has power of attorney to approve an RPP) if the client's authorized signatory is unavailable or incapacitated, distinct from the "unreachable during a tail event" protocol.
11. **A documented resolution path for the Reg 22 vs Reg 31 citation conflict (Finding 5)** and the custodian-exemption and 2026-MF-reform claims (Findings 13-14) before any of these numbers reach a client-facing document or a SEBI filing.

---

## What is strong (keep verbatim into the merged blueprint)

1. **design_performance.md's Brinson-Fachler/Carino attribution worked example (§3.1, Table 4)** — every cell was independently re-derived in this review and is exact to three decimal places; the R0-R4 return-series hierarchy (paper → gross → net → post-tax → post-tax-with-DTL) is a genuinely good piece of design that the other domains should adopt rather than re-invent.
2. **design_risk.md's tail-hedge payoff table (§5.2)** — the put-premium and payoff arithmetic across all eight historical episodes checks out exactly, and the honest conclusion ("a running cost with no payoff... in most years... size to 25-40% notional coverage, not a full-notional programme") is exactly the right message for a client, not a sales pitch for hedging.
3. **The consent-latency framing itself** — threading "recommend → consent → execute" and its priced cost through Regulatory, Rebalancing, Risk and Operations consistently (setting aside the volatility/cost conflation in Finding 16) is the single best piece of design thinking in the set and correctly identifies NDPMS's real operating constraint.
4. **design_regulatory.md's fact-verification discipline** — flagging every unverified regulation sub-clause as "verify," distinguishing the not-yet-notified 2026 consultation paper from current law throughout, and the "Things commonly believed but wrong" section in data_facts.md are exactly the skepticism a mandate of this size needs.
5. **design_selection.md's fee-layering rules (§9.1)** and the direct-plan/no-distribution-fee discipline threaded through every instrument type — a clean, correct, and completely defensible set of rules.
6. **design_operations.md's four-eyes control table (§1.6) and the RPP→OMS foreign-key linkage** ("every order in the OMS carries an rpp_id... an order cannot be released without a valid, unexpired, matching consent record — this is the single most important control in the whole book") — this is the right architectural spine for proving NDPMS compliance at inspection.
