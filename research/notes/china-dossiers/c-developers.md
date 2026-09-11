# C-DEVELOPERS — Developer case files: Evergrande, Country Garden, Vanke, Sunac, and the state survivors

*Dossier `c-developers` (CN programme, Half B, dispatch row 14 — consolidates manifest bundles
`b6-dev-evergrande` + `b6-dev-country` + `b6-dev-vanke` + the Sunac and Poly/COLI/CRL items from
`b6-dev-sunac`/`b6-dev-poly`, plus the presale and market-share cross-cuts). Compiled 2026-09-11.
Motivation, stated directly by the desk: `CI-D1..D5` and this programme's own `b6-debt-predictive-summary.md`
found that developer balance-sheet leverage — not price-to-income, not price-to-rent, not the
BIS credit-gap — was the one indicator that was early, specific, and eventually acted on by
policy (the Three Red Lines, Aug 2020), while macro mortgage-credit aggregates carry an 87.2%
false-alarm rate. This dossier is the firm-level test of that finding: five case files plus three
cross-cutting questions, built to answer which balance sheets actually flashed, how far in
advance, and what "recovery" and "market-share transfer" look like once a firm crosses the line.
Method: WebSearch only — **WebFetch is EGRESS_BLOCKED for every domain** (plan §0a). Every figure
is therefore a search-result-snippet reconstruction, not a primary-filing read; this is Half B's
stated verification ceiling, not a caveat unique to this file. Corroboration rule applied
throughout: load-bearing figures are tagged `[2-SOURCE]`, `[1-SOURCE]`, or `[RECALL — unverified]`.
No figure is invented; where a number could not be pinned down, or where two sourced figures do
not reconcile, that is stated as a gap (§ Gaps and cautions) rather than forced to agree. Today's
date is 2026-09-11; every balance-sheet figure states its own reporting/as-of date, and every
CNY/USD conversion states its own FX-rate vintage — conversions not directly sourced this session
use standard historical year-end/period CNY/USD reference levels and are tagged
`[RECALL — standard FX, not independently re-verified this session]`. Web-sourced — not vault
data, not sha256-manifested, not a trial-ledger entry (plan §0/§5).*

**The single most important methodological note in this file, stated once and applied
throughout (per the task's own instruction):** *"total liabilities" is not "borrowings" and not
"net debt."* Evergrande's famous "~$300bn" is total liabilities — bank debt plus bonds plus trade
payables plus presale/contract liabilities (money owed as *apartments*, not cash) — not
borrowings. Every table below separates the two explicitly. Conflating them is, as the task
states, the single most common error in public coverage of this subject, and this dossier treats
getting it right as more important than any single headline number.

---

## Headline findings

- **The Three Red Lines flashed years early for two firms and only weeks early for the one
  popularly considered "safest."** Evergrande and Sunac were both already running **>200% net
  gearing in H1 2017** `[2-SOURCE via b6-debt-predictive-summary.md]` — three years before the
  policy existed — and were "Red" (breach-all-three) from the policy's own August 2020
  introduction, roughly 16-21 months before their respective defaults. Country Garden sat in
  "Yellow" (one metric from full compliance) from 2020 and was explicitly targeting full "Green"
  status by 2023 `[2-SOURCE]` — the year it defaulted instead. Its first sharp rating-agency
  alarm (Fitch cutting a subsidiary to junk) landed in **August 2023, about two months before its
  October 2023 default** `[2-SOURCE]` — by a wide margin the shortest lead time of the five firms
  in this file, and the direct, practical answer to why Country Garden matters most for the
  early-warning question: the metric that worked for Evergrande and Sunac gave almost no notice
  here.
- **Presale/contract liabilities are not a rounding error on any of these balance sheets — they
  are close to half of Country Garden's.** Contract liabilities were **29.6% of Evergrande's**
  total liabilities (≈CNY 721.5bn of CNY 2,437.4bn, end-2022) but **46.6% of Country Garden's**
  (≈CNY 668bn of CNY 1,435bn) and **≈1/3 of Vanke's** (≈CNY 408bn of ≈CNY 1.2-1.4tn, Sep 2023)
  `[2-SOURCE for the Evergrande/Country Garden split, converging from two independent figures —
  see §6]`. This is the mechanical reason Country Garden's headline balance sheet looked smaller
  and safer than Evergrande's while its actual cash fragility was comparable: a materially larger
  share of "what it owes" was owed as *unbuilt apartments*, which do not register on any
  bank/bondholder leverage screen until construction stops.
- **Recovery values cluster in a narrow, ugly band across every firm that has actually
  restructured — roughly 2-14 cents on the dollar** — Evergrande's dollar bonds traded near
  **2.25 cents** by November 2023 (down from ~6 cents earlier that year) `[1-SOURCE]`; Country
  Garden's cash-conversion option implies **~10 cents** (a 90% haircut) `[2-SOURCE]`; Sunac's
  second-restructuring convertible-bond tranches are estimated at **8% and 14%** `[2-SOURCE]`.
  Vanke is the outlier and not comparable: it has not completed a restructuring at all — its
  bonds simply trade near **20% of face value** amid a ratings-agency "selective/restricted
  default" via distressed exchange `[2-SOURCE]` — a market-priced distress signal, not a
  court-sanctioned recovery outcome.
- **Vanke has not been "rescued" in any sense the word normally carries.** Its majority state
  shareholder, Shenzhen Metro, has made at least 15 separate loan commitments totalling over
  **CNY 34.6bn** through late 2025, plus a further facility of up to **CNY 22bn** pledged into
  1H2026, and in January 2026 installed its own chairman (Xin Jie, replacing Yu Liang) directly
  atop Vanke `[1-SOURCE]`. That support has repeatedly prevented a disorderly default, but S&P and
  Fitch both downgraded Vanke to a formal default-equivalent rating (Selective Default /
  Restricted Default) over its own distressed bond-maturity extensions in the Jan-Apr 2026 window
  `[2-SOURCE]`, sales are down over 80% from 2020, and its bonds trade at roughly a fifth of face
  value. The honest characterization is *serially life-supported by its state shareholder*, not
  rescued.
- **Sunac's completed 2023 restructuring is not the clean template the task's own framing
  assumes — it did not hold.** The November 2023 offshore deal (98% creditor approval, ~$10.2bn
  extinguished via long-dated notes and equity conversion) `[2-SOURCE]` was followed by a
  **second** onshore restructuring in November 2024 (halving CNY 15.4bn of bonds) and a
  **second** offshore restructuring reaching agreement only in April 2026 `[2-SOURCE]`. What
  Sunac actually demonstrates is that an equity-heavy restructuring buys a distressed developer
  roughly 18-24 months, not a resolution — a materially more cautious lesson than "recovery
  completed."
- **The market has flipped from roughly two-thirds private to roughly two-thirds state-owned/
  backed in well under five years, and the state share is still visibly rising.** State-affiliated
  developers took **89% of the land value** acquired by China's top 100 developers in 2023
  (China Index Academy) `[1-SOURCE, single named survey house, widely syndicated]`; the 2023
  top-six home-sales spots were all state-owned/backed, with Country Garden — 2022's #1 —
  falling to **#7** as its sales dropped 53% `[2-SOURCE]`; CRIC reported state-owned firms' sales
  share up 6 percentage points to roughly two-thirds by July 2024 `[1-SOURCE, named: CRIC]`,
  consistent with a separate read putting private developers' own share down to roughly 30% by
  end-2024 `[1-SOURCE, original outlet not independently pinned this session]`.

---

## MASTER TABLE

All figures as sourced in the per-firm sections below; see those sections for exact as-of dates,
FX vintages, and source tags. "—" means not sourced this session (see § Gaps).

| Firm | Peak total liabilities | of which borrowings (interest-bearing) | of which presale/contract liabilities | Default date | Bond recovery | Equity drawdown | Status (as of 2026-09-11) |
|---|---|---|---|---|---|---|---|
| **China Evergrande** | CNY 2,437.4bn / ≈$350bn (end-2022) | ≈CNY 572bn / $89bn (30-Jun-2021 interim, not same date as peak) | ≈CNY 722bn (29.6% of total, end-2022) | First default 9-Dec-2021 | ~2-6 cents/$ (2023) | Peak mkt cap ~$51.7bn (2017) → delisted, ~worthless (Aug 2025) | **LIQUIDATED** — HK winding-up order 29-Jan-2024; delisted 25-Aug-2025 |
| **Country Garden** | CNY 1,435bn / ≈$200bn (FY2023) | CNY 258bn interest-bearing (30-Jun-2023) | CNY 668bn (46.6% of total) | First default 18-Oct-2023 | ~10 cents/$ cash option (90% haircut) | Peak mkt cap ~$29.8bn (2018) → ~97% destroyed by Apr-2024 suspension | **RESTRUCTURED** — HK court sanction 4-Dec-2025, effective 30-Dec-2025 |
| **Vanke** | CNY 947.4bn (end-2024; NOT confirmed as historical peak — see gaps) | CNY 364.3bn (end-2024) | ≈CNY 408bn (Sep-2023, ~1/3 of total then) | No hard default — S&P "Selective Default" / Fitch "Restricted Default" via distressed exchange, Jan-Apr 2026 | Bonds ~20% of face value (market-priced, not a completed restructuring) | Mkt cap down 25-37% YoY (2025-26); historical peak not sourced this session | **STATE-SUPPORTED, UNRESOLVED** — Shenzhen Metro installed its own chairman 27-Jan-2026 |
| **Sunac China** | CNY 1,050bn / ≈$150.7bn (end-2021; liability ratio 89%) | CNY 259.67bn group borrowings (FY2024, post-first-restructuring residual, not peak) | Not itemized this session | First default May-2022 | 8-14% (second-restructuring MCBs, 2025-26) | Peak share price HKD 49.55 (3-Jan-2020) → HKD 0.61 (7-Sep-2026), ~98.8% decline | **TWICE RESTRUCTURED** — first (offshore) effective 20-Nov-2023; second onshore (Nov-2024) + second offshore (agreement Apr-2026) |
| **Poly / COLI / CR Land** | Not sought — never distressed | N/A | N/A | Never defaulted | N/A | Not sought (survivors; share gains quantified in §7) | **SURVIVORS / GAINERS** — see §5 |

---

## TIMELINE — cross-firm chronology

| Date | Firm | Event |
|---|---|---|
| H1 2017 | Evergrande, Sunac | Net gearing already >200% — years before the Three Red Lines existed `[2-SOURCE via b6-debt-predictive-summary.md]` |
| Aug 2020 | All (policy) | Three Red Lines policy introduced; Evergrande and Sunac immediately "Red," Country Garden "Yellow," Poly/COLI/CRL among the disciplined cohort |
| 30-Jun-2021 | Vanke | Reports full "Green" compliance — net gearing 20.2%, cash CNY195.2bn vs short-term interest-bearing debt CNY84.3bn `[2-SOURCE]` |
| 30-Jun-2021 | Evergrande | Breaches all three red lines `[2-SOURCE]` |
| 23 & 29-Sep-2021 | Evergrande | Misses initial dollar-coupon deadlines (grace periods run) |
| 9-Dec-2021 | Evergrande | First formal default (Fitch cuts to Restricted Default after the 6-Dec grace period lapses) `[2-SOURCE]` |
| May-2022 | Sunac | Misses coupons on four USD note tranches — first default, triggers cross-defaults `[2-SOURCE]` |
| Mar-2023 | Evergrande, Sunac | Both unveil restructuring plans within weeks of each other |
| Jul-2023 | Vanke | First Fitch downgrade — an early stress flag, no default `[1-SOURCE]` |
| Aug-2023 | Country Garden | Fitch cuts subsidiary Country Garden Services to BB+/junk — the first sharp alarm, ~2 months before default `[2-SOURCE]` |
| 17/18-Oct-2023 | Country Garden | First formal default — Event of Default declared, ISDA rules a credit event `[2-SOURCE]` |
| 20-Nov-2023 | Sunac | First (offshore) restructuring effective — ~98% creditor approval `[2-SOURCE]` |
| 29-Jan-2024 | Evergrande | HK High Court orders liquidation; liquidators appointed (Alvarez & Marsal) `[2-SOURCE]` |
| 22-Mar-2024 | Vanke | Fitch cuts rating to BB+ (junk) `[2-SOURCE]` |
| 2-Apr-2024 | Country Garden | HK shares suspended from trading |
| Nov-2024 | Sunac | Second (onshore) restructuring proposed — accepted by all bondholders `[2-SOURCE]` |
| Feb-2025 | Vanke | Shenzhen Metro's first major direct cash lifeline ($578mn) `[1-SOURCE]` |
| 25-Aug-2025 | Evergrande | Delisted from HKEX, ending a 16-year listing `[2-SOURCE]` |
| Oct-2025 | Sunac | Second (offshore) restructuring wins creditor backing `[1-SOURCE]` |
| 7-Nov-2025 | Country Garden | Creditors approve offshore restructuring (83.7% syndicated lenders, 96% bondholders) `[2-SOURCE]` |
| 4-Dec-2025 | Country Garden | HK court sanctions the restructuring |
| 15 & 22-Dec-2025 | Vanke | CNY2bn MTN near-miss — bondholders initially reject, then approve a grace-period extension to 27-Jan-2026 `[2-SOURCE]` |
| 30-Dec-2025 | Country Garden | Restructuring becomes effective |
| 27-Jan-2026 | Vanke | Shenzhen Metro's Xin Jie replaces Yu Liang as Vanke chairman — direct state management takeover `[1-SOURCE]` |
| Jan-Apr-2026 | Vanke | S&P downgrades to "Selective Default," Fitch to "Restricted Default," over the distressed bond exchanges `[2-SOURCE]` |
| Apr-2026 | Sunac, Vanke | Sunac's second offshore restructuring reaches agreement with key creditors; Vanke wins creditor backing for a further 1-year bond extension `[2-SOURCE each]` |

---

## 1. China Evergrande — the archetype

### Total liabilities, CNY and USD, and the split
Two vintages are usable and should not be conflated. **Real-time (pre-delay) interim, 30-Jun-2021:**
total liabilities CNY 1,962bn against total assets CNY 2,380bn `[1-SOURCE]`. Within that:
interest-bearing debt (borrowings) **CNY 571.8bn / ≈$89bn** (42% short-term), and trade/accounts
payables **CNY 666.9bn / ≈$103bn** `[1-SOURCE, FX ≈6.46 for Jun-2021 `[RECALL — standard FX]`]`.
Within borrowings, **≈$19bn** was offshore USD bonds `[2-SOURCE, widely cited]`. **Delayed
(audited, filed Jul-2023) full-year figures — the true peak:** total liabilities **CNY 2,437.4bn**
at end-2022 (≈**$350bn** at ≈6.97 CNY/USD `[RECALL — standard year-end-2022 FX]`), up 23% from
2020, against total assets of CNY 1.8tn (down 20%) `[2-SOURCE: CNN's "$81bn combined 2021-22
loss... 2.4tn yuan... up 23% from 2020" converges with a separate side-by-side Evergrande/Country
Garden comparison stating CNY 2,437.4bn precisely]`. Of that peak figure, advance receipts from
pre-sold properties (contract liabilities) were **29.6%**, ≈**CNY 721.5bn** `[1-SOURCE — flagged
for further corroboration]`. **Onshore-bond-specific figures were not separately itemized this
session** — a gap (§ Gaps). The Hong Kong court itself, in its liquidation judgment, referenced
total liabilities of **US$328bn** — in the same neighborhood as the CNY 2,437.4bn/$350bn figure
above, allowing for a different as-of date and FX rate `[2-SOURCE]`.

### Default timeline
23 & 29-Sep-2021: misses initial deadlines on $131mn of dollar coupons (grace periods available).
6-Dec-2021: grace period on an $82.5mn coupon expires. **9-Dec-2021: Fitch cuts Evergrande's
long-term FC issuer rating to Restricted Default** — the first formal default `[2-SOURCE]`.
Mar-2023: Evergrande unveils a restructuring plan after reaching "binding agreements" with an
international bondholder group on key terms `[2-SOURCE]`. Jul-Nov 2023: a revised offshore plan
emerges, offering creditors options including converting claims into new notes/equity-linked
instruments, ultimately proposing a **~30% equity stake in each of Evergrande's two HK-listed
subsidiaries** in exchange for the ~$19bn of offshore claims `[2-SOURCE]`. **29-Jan-2024: the
Hong Kong High Court (Justice Linda Chan) orders liquidation**, after 19 months of talks produced
no viable restructuring plan; Eddie Middleton and Tiffany Wong of Alvarez & Marsal are appointed
liquidators `[2-SOURCE]`. **25-Aug-2025: Evergrande is delisted from HKEX**, ending a 16-year
listing, with an estimated 160,000 retail shareholders left holding near-worthless stock
`[2-SOURCE]`.

### Offshore USD bond recovery value
Evergrande's dollar bonds traded around **6 cents on the dollar in early 2023**, falling to
**~2.25 cents by November 2023** as bondholders weighed the revised restructuring terms
`[1-SOURCE]`. Bondholders' own counsel told the Hong Kong court that a liquidation-scenario
recovery would be **under 3%** — i.e., worse than even the depressed trading price implied, which
was the argument for accepting the equity-swap alternative instead `[1-SOURCE]`. That
alternative's own economics deteriorated in parallel: the HK-listed subsidiary shares creditors
would have received had themselves fallen **more than 80% during 2023** `[1-SOURCE]`.

### Equity peak-to-now and market cap destroyed
Market capitalization peaked at **≈$51.7bn in 2017** (other citations converge near $50bn)
`[2-SOURCE]`. Shares fell from a cited HK$31.39 reference level to **HK$0.163** at last trade
(pre-suspension, Jan-2024), a **≈99.5%** collapse, with the stock's last-traded value at
**$282mn** some 19 months later (i.e., as reported in an Aug-2025 delisting retrospective)
`[1-SOURCE]`. Roughly **160,000 retail investors** were left holding shares now valued at
effectively zero `[2-SOURCE]`.

### Unfinished units and delivery status
Evergrande-specific: Gavekal Dragonomics estimated, as of late 2023, that Evergrande held advance
payments equivalent to roughly **600,000 housing units** `[1-SOURCE]`; as of 2024 the company
still had "hundreds of unfinished projects" nationwide with hundreds of thousands of buyers
waiting `[1-SOURCE]`. **These Evergrande-specific figures must not be confused with sector-wide
estimates** (a repeated conflation the task itself warns against): Nomura's oft-cited ~20 million
unfinished units and $446bn funding gap, and the government's own claim of >1.65 million pre-sold
units delivered under the national "guarantee delivery" (保交楼) programme, are BOTH sector-wide,
all-developer figures, not Evergrande's own `[1-SOURCE this session; cf. `c-facts.md` for the
programme's own independent corroboration of the sector-wide range]`.

### Three Red Lines metrics before the fall — the early-warning question
Evergrande **breached all three red lines** by 30-Jun-2021 `[2-SOURCE]`, and its underlying
leverage — net gearing already **>200% in H1 2017** `[2-SOURCE via `b6-debt-predictive-summary.md`,
itself citing Caixin/LH Ratings/S&P]` — long predates the policy. It was therefore "Red" from the
policy's Aug-2020 introduction, roughly **13-16 months** before its Dec-2021 default. Crucially,
**credit ratings gave almost no independent warning**: Evergrande held investment-grade ratings
(Baa3 Moody's / BBB S&P & Fitch) through virtually all of 2020 *despite* being classified "Red"
that same year, and was not cut to speculative grade until **22-Jun-2021** `[2-SOURCE]` — i.e.,
the regulator's own numeric test flashed roughly a year before the rating agencies acted, and
roughly four years after the underlying 2017 leverage was already visible to anyone reading the
company's own accounts.

---

## 2. Country Garden — the "safest" large private developer that failed anyway

### Total liabilities, CNY and USD, and the split
**CNY 1.36tn / ≈$190bn** as of 30-Jun-2023 (FX ≈7.15 `[RECALL — standard mid-2023 FX]`)
`[1-SOURCE]`. The peak, implied by year-end 2023 figures and cross-checked against the presale
share below, is **≈CNY 1.435tn / ≈$200bn** `[1-SOURCE, derived by cross-reference — flagged]`.
**Interest-bearing liabilities** (bank borrowings, senior notes, convertible bonds, corporate
bonds combined) were **CNY 257.9bn** as of 30-Jun-2023 `[1-SOURCE]` — i.e., under a fifth of
total liabilities, a materially lower "borrowings share" than the headline total-liabilities
figure implies. **Contract liabilities (presale)** were **≈CNY 668bn**, independently converging
from two angles: a direct FY2022 figure (Statista) and a 46.6%-of-CNY-1.435tn back-solve from the
peak total (≈CNY 668.7bn) `[2-SOURCE, two independently-derived figures agreeing to within 0.1%]`
— **46.6% of total liabilities**, the largest presale share of any firm in this dossier. Trade
payables specifically were not itemized this session (gap).

### Default timeline
An initial **$15.4mn coupon payment** fell due around 17-Sep-2023 and was missed, opening a
30-day grace period. **18-Oct-2023: the grace period lapses and Country Garden is declared in
default** — trustee Citicorp International notifies holders that the failure "constitutes an
event of default," and the Credit Derivatives Determinations Committee rules a failure-to-pay
credit event the same day `[2-SOURCE]`. Restructuring negotiations run through 2024-2025.
**7-Nov-2025: creditors vote to approve** an offshore restructuring (83.7% of the syndicated-loan
group, 96% of dollar bondholders — both above the 75% Companies Ordinance threshold). **4-Dec-2025:
the Hong Kong High Court sanctions the plan**, which becomes **effective 30-Dec-2025** `[2-SOURCE]`.

### Offshore USD bond recovery value
The restructuring reduces total offshore obligations from **$17.7bn to $11.7bn**. Creditors are
offered a choice: a cash-conversion option carrying a **90% haircut** (implying **≈10 cents on
the dollar**), or new debt instruments with delayed maturity, or debt/equity-linked alternatives
`[2-SOURCE]`. The restructuring is expected to book Country Garden a gain of up to CNY 70bn from
the debt extinguished `[1-SOURCE]`.

### Equity peak-to-now and market cap destroyed
Market capitalization peaked at **over $29.84bn in 2018** `[1-SOURCE]`. By the time HK trading was
suspended (**2-Apr-2024**), the stock had lost **≈97% of its market value** from that peak
`[1-SOURCE]`. Trading later resumed around **HK$0.60**, described as "near a historical low"
`[1-SOURCE]`. FY2023 recorded a **CNY 178.4bn (≈$25bn) net loss** `[2-SOURCE]`.

### Unfinished units and delivery status
Country Garden reported **more than 3,000 housing projects**, concentrated in smaller cities, as
of its 2023 interim report `[1-SOURCE]`. It pledged to deliver **over 700,000 units in 2023** and
missed that target; its 2024 pledge was scaled back to **over 480,000 units** `[2-SOURCE]`. Actual
delivery has been *deteriorating*, not improving, even as the restructuring closed: **H1 FY2024
deliveries exceeded 150,000 units**, falling to **≈74,000 units in H1 FY2025** `[1-SOURCE]` — the
company has been reallocating locked presale funds and pursuing white-list project financing to
keep completing homes at all `[1-SOURCE]`.

### Three Red Lines metrics before the fall — the early-warning question
Country Garden sat in the **"Yellow" tier** from the policy's 2020 introduction — it breached only
the liability-to-asset-excluding-advances test (>70%) — and management explicitly targeted full
**"Green"** compliance **by 2023**, the year it defaulted instead `[2-SOURCE]`. Through 2022 it was
widely treated by markets and rating agencies as one of the more disciplined, "safer" large
private developers, retaining higher ratings for longer than Evergrande or Sunac. **The first
sharp rating-agency alarm — Fitch cutting subsidiary Country Garden Services to BB+/junk in
August 2023 — arrived only about two months before the October 2023 formal default**
`[2-SOURCE]`. This is, by a wide margin, the shortest flash-to-default gap of the five firms in
this dossier, and it is the practical reason Country Garden — not Evergrande — is the harder test
of the early-warning question: the one balance-sheet metric this desk's own prior work identified
as the earliest usable signal sector-wide gave almost no advance notice for the specific firm
popularly considered the least risky.

---

## 3. Vanke — the mixed-ownership case

### Total liabilities, CNY and USD, and the split
**CNY 947.4bn** as of 31-Dec-2024 `[1-SOURCE]` — stated here as the **latest available**, not a
confirmed historical peak; Vanke was structurally larger in 2020-2022 (total assets were **$248.4bn**
in 2020 `[1-SOURCE]`) and a precise earlier peak liabilities figure was not pinned down this
session (gap). **Interest-bearing liabilities: CNY 364.3bn** (end-2024) `[1-SOURCE]`. **Contract
liabilities (presale): ≈CNY 408bn as of Sep-2023**, reported at the time as roughly **one-third**
of total liabilities `[1-SOURCE]`. Separately cited: bonds payable of **≈$27.06bn** face value,
and (at an uncertain date) short-term borrowings of $17.3bn, long-term borrowings of $77.146bn,
and $36.985bn of non-current liabilities due within one year `[1-SOURCE, currency/date precision
uncertain — flagged]`.

### Default timeline — genuinely a different shape from the other four
Vanke has **not had a hard missed-payment default or liquidation petition**. Instead: **Jul-2023**,
Fitch's first downgrade (an early stress flag, no default) `[1-SOURCE]`; downgrades continue
through 2023-24, including **Moody's cutting Vanke to junk** and **Fitch to BB+ on 22-Mar-2024**
`[2-SOURCE]`; Vanke units guarantee **≈$1.1bn** of loans around the same downgrade window
`[1-SOURCE]`. Direct shareholder support from **Shenzhen Metro** (Vanke's largest shareholder,
roughly a third stake) escalates through 2025: a **$578mn** lifeline (Feb-2025), a **CNY 4.2bn**
3-year loan at 2.34% requiring CNY 6bn of collateral, and by late 2025 **15 cumulative loan
commitments totalling over CNY 34.6bn**, plus a further facility of **up to CNY 22bn** pledged
into 1H2026 `[1-SOURCE]`. **27-Jan-2026: Shenzhen Metro's own chairman, Xin Jie, replaces Yu Liang
as Vanke's chairman**, with three state-backed executives installed as vice-presidents — a de
facto state management takeover `[1-SOURCE]`. Meanwhile a **CNY 2bn** medium-term note comes to a
head: bondholders initially **reject** an extension proposal (15-Dec-2025), then approve a
grace-period extension to **27-Jan-2026** (22-Dec-2025 vote); a further **CNY 3.7bn** onshore
obligation is separately extended to February `[2-SOURCE]`. **In the Jan-Apr-2026 window, S&P
downgrades Vanke to "Selective Default" and Fitch to "Restricted Default,"** both explicitly
characterizing the distressed bond-maturity extensions as "tantamount to a default"
`[2-SOURCE]` — this ratings action is the closest thing Vanke has to a formal default, and it is
a **distressed-exchange/ratings default**, categorically different from Evergrande's or Country
Garden's missed-payment defaults. **April 2026: bondholders back a further one-year extension**
(40% of principal paid upfront, the balance deferred) `[2-SOURCE]`.

### Offshore USD bond recovery value
No completed restructuring exists to quote a recovery percentage from. As a market-priced proxy:
Vanke's **bonds were trading at roughly 20% of face value** through the Dec-2025/early-2026 stress
window `[1-SOURCE]` — an implied ~20-cent recovery if a restructuring were struck at then-current
prices, notably better than Evergrande's or Country Garden's realized recoveries, consistent with
Vanke's ongoing state support, but **not itself a recovery outcome**.

### Equity peak-to-now and market cap destroyed
Current market capitalization is reported in the **≈CNY/HKD/USD 61-65bn** range across late-2025/
early-2026 readings (currency attribution inconsistent across sources — flagged), down
**25-37% year-on-year** over that stretch `[1-SOURCE, imprecise]`. **A defensible historical peak
figure was not found this session** — Vanke was described as "the country's largest developer by
market value" in 2021, with $248.4bn of total assets in 2020, but no sourced peak market-cap
number could be pinned to two sources; this is recorded as a genuine gap rather than estimated
(§ Gaps).

### Unfinished units and delivery status
Vanke's delivery record has held up comparatively well through the crisis: **74,000 units across
169 projects/262 batches in 2024H1**, and **234 projects/494 batches delivered across all of
2025** `[1-SOURCE]`. Sourced commentary explicitly contrasts this with Evergrande — "unlike
Evergrande, which left millions of homes unfinished, Vanke has a better track record of
delivery" — while flagging that "delays and quality concerns are increasing" `[1-SOURCE]`.

### Three Red Lines metrics before the fall — the early-warning question
Vanke achieved full **"Green"** compliance by **30-Jun-2021**: net gearing of **20.2%**, monetary
funds of **CNY 195.2bn** against interest-bearing liabilities due within one year of **CNY 84.3bn**
`[2-SOURCE]` — the most disciplined balance sheet, on this metric, of any firm in this dossier at
that date. Its distress, when it came, was NOT flagged by the Three Red Lines at all — it emerged
first through credit ratings (Jul-2023) and then through the escalating frequency and size of its
own majority shareholder's cash injections from 2024 onward. Whether Vanke has "actually been
rescued": **no, not cleanly** — Shenzhen Metro's cumulative support has repeatedly averted a
disorderly default and installed direct management control, but has not restored solvency (bonds
near 20 cents on the dollar, sales down over 80% from 2020, two rating agencies already treating
the restructuring actions as default-equivalent, and further debt still maturing through 2026).

---

## 4. Sunac — the restructuring that (partially) completed

### Total liabilities, CNY and USD, and the split
**CNY 1.05tn**, cited directly as **≈$150.7bn**, at end-2021 — liability ratio **89%**
`[1-SOURCE]`. Note: the source's own implied FX rate (≈$150.7bn against CNY 1.05tn ⇒ ≈6.97) does
not match the actual end-2021 CNY/USD level (≈6.37); this is reported as the source states it,
flagged rather than silently corrected (§ Gaps). **A bank-loan/bond/trade-payables breakdown was
not itemized this session** (gap). FY2024 (post-first-restructuring) residual figures: total
group borrowings **CNY 259.67bn**, cash **CNY 19.75bn**, net loss **CNY 25.70bn** `[1-SOURCE]`.
Existing offshore debt as of mid-2025 is cited at **$7.45bn across 24 instruments** in one source
and separately at **$9.55bn of creditor claims as of 30-Jun-2025** for the second offshore
restructuring in another `[1-SOURCE each]` — these do not reconcile cleanly (likely different
debt perimeters or dates) and are presented as-is rather than forced to agree.

### Default timeline — and why "completed" needs a qualifier
**May-2022: Sunac misses coupons on four USD senior-note tranches**, triggering cross-defaults —
the first default `[2-SOURCE]`. **Mar-2023: a restructuring plan is unveiled**, ~10 months after
default `[2-SOURCE]`. **20-Nov-2023: the FIRST offshore restructuring becomes effective** via a
Hong Kong scheme of arrangement, ~98% creditor approval — **~$10.2bn** extinguished via **$6.26bn**
of new notes (maturities to 2031), **$1bn** of convertible bonds, **$2.65bn** of mandatory
convertible bonds, and **≈$775mn** swapped into Sunac Services equity `[2-SOURCE]`. **This did not
resolve the underlying insolvency**: **Nov-2024, a SECOND (onshore) restructuring** is proposed —
10 bonds, CNY 15.4bn face value, cutting the debt load by roughly half — and is accepted by all
bondholders `[2-SOURCE]`. **Oct-2025: a SECOND offshore restructuring** wins creditor backing
`[1-SOURCE]`, reaching **agreement with key creditors in April 2026** — two new mandatory
convertible bond tranches at conversion prices of **HK$6.80 and HK$3.85** `[2-SOURCE]`.

### Offshore USD bond recovery value
The **second** restructuring's two MCB tranches are estimated at **8% and 14% recovery**
respectively, based on Sunac's market capitalization at signing `[2-SOURCE]`. **The first
(2023) restructuring's recovery was never quoted as a single cents-on-dollar figure** in what was
found this session — it was structured instead as long-dated paper plus equity conversion, an
economically comparable but differently-shaped haircut. This is recorded as a gap: no single
first-restructuring recovery percentage could be sourced (§ Gaps).

### Equity peak-to-now and market cap destroyed
All-time-high share price: **HKD 49.55 on 3-Jan-2020** `[1-SOURCE]`. Current (7-Sep-2026): **HKD
0.61**, market cap **HKD 12.18bn** — a **≈98.8%** share-price decline from the 2020 peak, and a
**94.3%** decline "over five years" per a separately-cited figure `[1-SOURCE each]`. These two
reference points do not reconcile precisely against each other or against a third data point — an
April-2023 post-suspension reopening in which shares fell to HKD 1.86 (an 11-year low), erasing
**HKD 13.84bn** of market value in a single session, implying a pre-suspension (≈2022) market cap
on the order of HKD 20-30bn, well below what the Jan-2020 peak share price would suggest absent
dilution. The most likely explanation is the 2022 discounted share placement referenced in search
results (new shares issued at a steep discount to repay debt), which would materially dilute the
share-price comparison — flagged as a genuine reconciliation gap rather than forced to one number.

### Unfinished units and delivery status
Sunac delivered **over 300,000 units in 2024** alone, and **720,000 units cumulatively over the
preceding four years** (through 2025), with only **54,000 units delivered in 2025** as the backlog
neared completion — company/reporting framed this as "essential completion" of its home-delivery-
guarantee obligations by end-2025 `[2-SOURCE]`. This is a genuinely strong outcome on this specific
metric relative to Evergrande, even though Sunac's balance sheet required two restructurings.

### Three Red Lines metrics before the fall — the early-warning question
Sunac, like Evergrande, was already running **net gearing above 200% in H1 2017**
`[2-SOURCE via `b6-debt-predictive-summary.md`, itself citing Caixin/S&P]` — years before the
Three Red Lines existed, and unambiguously "Red" from the policy's 2020 introduction. Unlike
Country Garden and unlike Vanke, Sunac's leverage was flashing at the same early date and to the
same degree as Evergrande's.

---

## 5. Poly / China Overseas / China Resources Land — the state-owned survivors

All three were among the original **12 developers** in the 2020 Three Red Lines pilot group, all
state-owned or state-backed, and all sustained materially lower leverage and cheaper funding
throughout the crisis: **Poly's average borrowing cost held near 3.5% post-Three-Red-Lines**
`[1-SOURCE]` — a funding-cost advantage private developers structurally lost access to once
offshore bond markets froze to the whole sector.

**What they did differently, as sourced (not merely inferred from survival):** they continued
active land acquisition through the downturn when private developers retreated — China Overseas
Land & Investment (COLI) is specifically cited as making "aggressive moves in the land market"
even as competitors shrank `[1-SOURCE]`; they retained investment-grade access to bank credit and
onshore/offshore bond markets on the strength of state ownership, rather than depending on
presale cash flow or shadow-banking channels the way the private cohort structurally did; this is
consistent with, though not separately re-derived from, this programme's own already-booked
`b2-land-national.md` (the state/LGFV share of land purchases) and `c-lgfv.md` (state
balance-sheet support mechanisms).

**Market share gained, quantified:**
- **Land value**: the top-100 developers' total 2023 land spend was **CNY 1.3tn** (+1.7% YoY), of
  which **89%** came from state-affiliated developers (China Index Academy, reported via a Reuters
  survey syndicated across multiple outlets — treated as one primary source, not independently
  corroborated, per the desk's own syndication-vs-corroboration convention) `[1-SOURCE]`.
- **Home sales**: the **2023 top-six sellers were all state-owned/state-backed** — Poly
  Developments, Vanke, and COLI led the table — while **Country Garden fell from #1 (2022) to #7
  (2023)** as its sales dropped 53% to CNY 220bn `[2-SOURCE]`. **China Resources Land's own sales
  ranking climbed: 9th (2020) → 8th (2021) → 4th (2022) → 4th (2023)** `[1-SOURCE]`.
- **By year, sector-wide**: state-owned firms' share of total property sales rose **6 percentage
  points in the year to Jul-2024, to roughly two-thirds** (CRIC, named source) `[1-SOURCE]`,
  consistent in direction and rough magnitude with a separately-sourced read that private
  developers' own share — once roughly two-thirds — was down to **roughly 30% by end-2024**
  `[1-SOURCE, original outlet not independently pinned this session]`. The two reads should be
  taken as directionally convergent (state ≈66%, private ≈30%, remainder mixed/other), not as
  identical measurements from a single survey.

---

## 6. Presale contract liabilities across the sector

**Why this liability does not look like debt.** A contract liability (advance receipt / presale
deposit) is booked when a customer pays before the good is delivered — it is deferred revenue, an
obligation to deliver a completed apartment, not a financial obligation to repay borrowed cash
`[2-SOURCE, standard revenue-recognition treatment plus China-specific sourcing]`. This is not
merely an accounting technicality: **China's own Three Red Lines policy explicitly excludes
advance receipts from its headline liability-to-asset test** — the regulator itself, in effect,
already recognized this liability behaves differently from debt `[2-SOURCE]`. The practical
consequence is the one the task flags directly: a headline "total liabilities" figure that
*includes* presale liabilities (as most reported developer figures do) systematically overstates
what banks and bondholders are actually owed, while simultaneously representing a very real,
largely uncollateralized obligation to hundreds of thousands of individual households — an
obligation invisible to any conventional leverage screen until construction physically stops, at
which point it surfaces all at once as "unfinished units," not as a debt-market event.

**Sector-wide scale.** Developers raised **over CNY 6.6tn (≈$1tn) from deposits and presales in
2020 alone** — a *flow* figure for that single year, not a balance-sheet stock `[1-SOURCE]`.
Separately, total property-development-sector debt was reported at **CNY 33.5tn (≈$5.2tn)** as of
June 2021 — but this is a broad sector debt aggregate, **not** presale/contract liabilities
specifically, and is stated here precisely to avoid the conflation the task warns against
`[1-SOURCE]`. No single, sourced, sector-wide *stock* figure for aggregate presale/contract
liabilities specifically (as opposed to the flow above, or the broader debt aggregate) was found
this session — recorded as a gap.

**Firm-level anchors** (drawn from §§1-3 above, all independently sourced there): Evergrande
≈CNY 721.5bn (29.6% of total liabilities, end-2022); Country Garden ≈CNY 668bn (**46.6%**,
FY2022/2023 — the largest share of any firm here); Vanke ≈CNY 408bn (≈1/3, Sep-2023). Country
Garden's outsized presale share is the mechanical reason its balance sheet read as "safer" than
Evergrande's on a pure total-liabilities basis while its underlying cash fragility was comparable
— a materially larger fraction of what it owed was owed in apartments, not repayable in cash under
any circumstance short of completing and delivering the units.

---

## 7. The market-share shift from private to state developers, by year

| Year | Milestone |
|---|---|
| Pre-2021 (baseline) | Private developers held roughly **two-thirds** of new-home sales `[1-SOURCE]` |
| 2022 | Country Garden ranks **#1** by sales — the last year of private-developer sales leadership among the firms tracked here |
| 2023 | State-owned/backed developers take the **top six** sales spots (Poly, Vanke, COLI leading); **89%** of top-100 land value goes to state-affiliated developers (China Index Academy) `[1-SOURCE]`; Country Garden falls to **#7**, sales −53% to CNY220bn; CR Land climbs to **4th** `[2-SOURCE combined]` |
| Jul-2024 | State-owned firms' sales share rises **+6pp YoY to ≈two-thirds** (CRIC) `[1-SOURCE]` |
| End-2024 | Private developers' own share reported down to **≈30%** `[1-SOURCE]` |
| Jan-2026 | The shift extends from market share to direct control: Vanke — nominally still a "mixed-ownership" private-sector name — passes under its state shareholder's own chairman `[1-SOURCE]`; Country Garden's restructuring completes under continued creditor and, implicitly, regulatory supervision |

The consolidation is real on both legs the task asked about (sales and land), is corroborated by
more than one named survey house even though each individual figure traces to a single primary
survey, and — as of the most recent data point in this dossier — has progressed from a *market-share*
phenomenon into direct *governance* control of at least one of the five case-file firms (Vanke).

---

## 8. Ranked by how early they were visible — the practically useful output

Using each firm's own most-cited leverage/rating signal against its own default (or
default-equivalent) date:

1. **Evergrande and Sunac — tied earliest.** Both already **>200% net gearing in H1 2017**
   `[2-SOURCE]` — roughly **4.5 years** before Evergrande's Dec-2021 default and **≈5 years**
   before Sunac's May-2022 default. Both were "Red" under the Three Red Lines from the policy's
   own Aug-2020 introduction — a **regulator-certified** breach roughly **13-16 months**
   (Evergrande) and **≈21 months** (Sunac) before their respective defaults. This is the cleanest,
   most auditable advance signal in the entire dossier, and it matches this desk's own prior
   finding (`b6-debt-predictive-summary.md`) that developer balance-sheet leverage was the
   earliest usable sector-wide indicator.
2. **Vanke — longest lead time, but from a genuinely clean start.** Full "Green" compliance as
   late as mid-2021; its first rating-agency flag (Fitch) came **Jul-2023**, and its first
   default-equivalent rating action (S&P Selective Default / Fitch Restricted Default) only in the
   **Jan-Apr-2026** window — roughly **31 months** from first flag to default-equivalent. Vanke's
   real tell was never the Three Red Lines at all; it was the escalating size and frequency of its
   own majority shareholder's cash injections from 2024 onward — a signal outside every metric this
   dossier's other four firms are judged on.
3. **Country Garden — shortest lead time by far.** "Yellow" (one metric from Green) from 2020,
   explicitly targeting full compliance by 2023 and treated by markets as one of the safer large
   private names through 2022. Its first sharp rating-agency alarm (Fitch cutting a subsidiary to
   junk, Aug-2023) arrived only **≈2 months** before its Oct-2023 formal default.

**Practical ranking, earliest-to-latest flash-to-default: Evergrande/Sunac (years) > Vanke
(≈2.5 years, though arguably not a "warning" in the same sense, since it started from a genuinely
clean balance sheet) > Country Garden (≈2 months).** Poly/COLI/CR Land never flashed at all. The
single most decision-relevant reading of this ranking: **state ownership dominated the leverage
ratio as a predictor of survival** — the three firms that never flashed did not do so because
their leverage metrics were unusually good throughout the entire period (Country Garden's, for
one, was not), but because state backing changed the funding-access consequences of a given
leverage level. A rule built only on the Three Red Lines would have caught Evergrande and Sunac
years early, missed Country Garden almost entirely, and said nothing at all about ownership
structure — the variable that, on this five-firm sample, mattered most.

---

## Gaps and cautions

- **Onshore-bond-specific figures** were not separately itemized for Evergrande, Sunac, or
  Country Garden this session (each firm's borrowings are reported as a combined "interest-bearing
  liabilities" figure spanning bank loans, onshore bonds, and offshore bonds together, except
  where an offshore-bond-specific sub-figure is separately cited, as for Evergrande's ~$19bn).
- **Vanke's historical peak total liabilities and peak market capitalization** were not sourced
  this session — only the end-2024 liabilities figure and the current (2025-26) market cap were
  found. Given Vanke's structurally larger 2020-2022 balance sheet, both figures are very likely
  understated relative to the firm's true peak; this is stated as a gap rather than estimated.
- **Sunac's total-liabilities/USD conversion** (CNY 1.05tn stated as "$150.7bn") implies an FX
  rate inconsistent with the actual end-2021 CNY/USD level; reported as the source states it
  rather than silently corrected.
- **Sunac's first (2023) restructuring recovery rate** was not quoted as a single cents-on-dollar
  figure in what was found; only the second (2025-26) restructuring's 8%/14% figures were sourced.
- **Sunac's equity peak-to-now figures** (the Jan-2020 all-time-high share price, the "94.3% over
  five years" figure, and the Apr-2023 reopening-day value-destruction figure) do not reconcile
  precisely with each other, most plausibly because of intervening share issuance/dilution (a 2022
  discounted placement is referenced in search results but not independently confirmed as the
  reconciling mechanism).
- **The "private developers' share down to ~30% by end-2024" figure** could not be pinned to a
  single named survey house this session, unlike the CRIC and China Index Academy figures it sits
  alongside; it is directionally consistent with those named-source figures but is tagged
  `[1-SOURCE, outlet unconfirmed]` rather than `[2-SOURCE]`.
- **A single, sourced, sector-wide stock figure for aggregate presale/contract liabilities**
  (as distinct from the CNY6.6tn 2020 flow figure, or the CNY33.5tn broader sector-debt figure)
  was not found this session — a genuine data gap for anyone wanting to size the "money owed as
  houses" liability at the whole-sector level rather than firm-by-firm.
- **Kaisa, Shimao, Sino-Ocean/Agile** (the remaining manifest developer bundle, `b6-dev-kaisa` /
  `b6-dev-shimao` / `b6-dev-sino`) are explicitly OUT OF SCOPE for this dossier per the task's own
  five-firm brief and remain unrun on `DISPATCH.md` row 32 (`c-developers-2`, now scoped down to
  just those three names since this file supersedes its Sunac/Poly coverage).
- Every USD conversion not directly quoted by a source uses a standard historical year-end/period
  CNY/USD reference level rather than a session-verified daily rate — tagged inline throughout as
  `[RECALL — standard FX, not independently re-verified this session]`.
