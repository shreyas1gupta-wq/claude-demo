# Dossier D — The Theory and Metric Canon: Profitability, Return on Capital, Growth, Earnings Quality

*Growth/ROIC/quality deep-dive, 2026-09-08; Sonnet research agent, adversarially
consumed by the desk. Knowledge synthesis; every quantitative claim [LIT], approximate.
Consistent with booked doctrine (growth return-negative at macro; aggregate E AR(1)
−0.11; market leads fundamentals) — Part 6 reconciles the aggregation levels.*

## 1. The metrics, precisely distinguished

| Metric | Formula | Lens | Chief distortion |
|---|---|---|---|
| ROE | NI / Equity | after-tax, after-leverage, owner's | leverage-inflated |
| ROCE | EBIT / Capital Employed | pre-tax operating (the Indian default) | denominator still capital-structure-sensitive |
| ROIC | NOPAT / Invested Capital | value-creation vs WACC (McKinsey/Mauboussin) | goodwill/cash convention debates |
| ROA | NI / Assets | blunt, universal | mixes operating + financing |
| Gross profitability | (Rev − COGS)/Assets | cleanest line, fewest accounting choices | ignores opex |
| CFROI | inflation-adj. gross CF / gross investment | cross-era real IRR (HOLT/Madden) | proprietary construction |

- **ROE**: DuPont (margin × turnover × leverage) is its own warning label — capital
  structure moves ROE with zero business change. What shareholders earned, not whether
  capital was well-deployed.
- **ROCE**: numerator financing-cleaned (EBIT), denominator not — "half-cleaned"; the
  practitioner default in India because it needs no invested-capital reconstruction.
- **ROIC** [LIT Koller et al., McKinsey Valuation]: NOPAT = EBIT×(1−t); IC = NWC + net
  PP&E + other operating assets. Conventions: goodwill IN shows post-deal reality, OUT
  shows underlying economics — show both; EXCLUDE non-operating cash (else cash-rich
  compounders look worse).
- **Gross profitability** [LIT Novy-Marx 2013 JFE]: deliberately crude — every line
  below gross profit adds a discretionary accounting choice. Predicts the cross-section
  with roughly value-sized magnitude, near-orthogonal to value; value+profitability
  beats either [LIT, LOW CONFIDENCE on exact spread].
- **CFROI**: take the transferable idea only — normalize for inflation and asset age
  before comparing returns across eras (historical-cost accounting flatters ROIC in
  inflationary decades).

**Where each misleads:** banks → use ROE + Tier-1, never ROIC (leverage IS the model);
capital-light compounders → trailing ROIC explodes on a tiny base; the correct object is
INCREMENTAL ROIC on incremental capital; commodity cyclicals → peak ROCE = peak cycle
(the cheap-and-high-ROCE screen is a top-of-cycle trap; normalize mid-cycle).

## 2. The value-creation algebra

**Growth creates value ONLY when ROIC > WACC** [LIT Koller et al.]. At ROIC = WACC
growth is value-neutral (M&M-style irrelevance); below it, faster growth destroys MORE.
So high-ROIC/low-growth can beat low-ROIC/high-growth — NPV scales with the SPREAD ×
growth, never growth alone. Value-driver formula: V = NOPAT×(1−g/ROIC)/(WACC−g). Any
screen ranking on revenue/earnings growth without the spread reads half the equation.

**Sustainable growth identity** g = ROE×(1−payout) [LIT Higgins 1977]: a firm-level
tautology that FAILS at the aggregate (Arnott-Asness 2003 [LIT]: high payout → HIGHER
subsequent growth). [DESK NOTE: QG-D1 re-ran this on 152y — direction replicated
(+4.0 vs +1.8%/yr) BUT the q5 mechanism cell reattributes it: high-payout months are
depressed-E months 78% of the time (dividend smoothing) and the gap INVERTS within
non-depressed months — the aggregate result is substantially the earnings mean-reversion
base effect, not only the A-A agency story.]

## 3. Fade and persistence

- ROIC mean-reverts toward WACC: spreads close roughly half in ~10y [LIT McKinsey
  persistence charts, approximate]; faster in commoditized/low-barrier industries.
- **Who resists fade**: the moat taxonomy (Mauboussin "Measuring the Moat" [LIT];
  Helmer's 7 Powers) — scale economies, network effects, switching costs,
  counter-positioning, cornered resources, process power. A persistence claim requires
  a named mechanism, not a track record.
- Academic: Wiggins-Ruefli (2002) [LIT, LOW CONFIDENCE] — sustained superior performance
  is rare and its duration DECLINING (hypercompetition).
- **Base-rate discipline** [LIT Mauboussin base-rate studies]: the empirical
  distribution of achieved growth by starting size — sustaining double-digit growth for
  a decade from a large base has a low-single-digit-% base rate; DCFs systematically
  overestimate persistence. Import wholesale (fits the no-magic-numbers rule).

## 4. Earnings quality — the metric set

- **Sloan (1996)** [LIT]: accruals (NI − CFO) less persistent than cash flows; original
  hedge spread ~10%/yr (1962-88, approximate). **Post-publication decay documented**
  (Green-Hand-Soliman ~2011 [LIT, LOW CONFIDENCE]) — concentrated into small/illiquid
  names, shrank in large-caps post-2000s.
- **Dechow-Dichev (2002)** [LIT]: accrual quality = residual of accruals regressed on
  past/current/future CFO; big residual = low persistence, higher cost of capital
  (Francis et al. 2005).
- **NOA / balance-sheet bloat** (Hirshleifer-Hou-Teoh-Zhang ~2004 [LIT]): high net
  operating assets / lagged assets → lower future returns — the stock-based complement
  to Sloan's flow measure.
- **Piotroski F-score (2000)** [LIT]: 9 binary signals (ROA>0, ΔROA>0, CFO>0, CFO>NI;
  Δleverage<0, Δcurrent ratio>0, no issuance; Δgross margin>0, Δturnover>0), designed
  WITHIN high-B/M stocks only; original within-cheap spread high-single-digit %/yr.
- **Mohanram G-score (2005)** [LIT, LOW CONFIDENCE on spread]: the growth-universe
  analog (stability, R&D/capex intensity vs industry). Lesson: quality screening is
  CONDITIONAL on the valuation regime — F for cheap, G for expensive.
- **Beneish M-score (1999)** [LIT]: 8 indices (DSRI, GMI, AQI, SGI, DEPI, SGAI, TATA,
  LVGI); cutoff ~−1.78; flagged Enron retrospectively (anecdote, screening tool not
  proof).
- **Cash conversion CFO/NI**: the one-line practitioner check; <1 persistently = accrual
  propping. Red flags: DSO rising faster than sales, period-end spikes, bill-and-hold,
  aggressive POC, related-party sales, policy changes.
- **The persistence hierarchy** (Sloan's mechanism): cash flows > accruals in
  persistence; the market fixates on aggregate EPS; the anomaly return is the
  correction.

## 5. The books (one takeaway each)

- **Penman**: reformulate statements (operating vs financing) BEFORE any ratio; RNOA =
  operating margin × operating turnover; conservative accounting inflates long-run ROE.
- **Koller et al. (McKinsey Valuation)**: anchor ALL construction conventions here
  (IC definition, goodwill, leases, cash).
- **Mauboussin-Rappaport (Expectations Investing)**: reverse-engineer the
  growth/margin/ROIC expectations already in price — the firm-level version of our
  "market leads fundamentals" doctrine.
- **Greenblatt (Magic Formula)** = EBIT/EV + EBIT/(NWC+NFA): book backtest ~30%/yr
  [LIT]; **replication/live record materially weaker** — a McLean-Pontiff case study,
  not a live edge at stated magnitude.
- **Cunningham et al. (Quality Investing)**: quality = profitability × growth
  durability × capital-allocation discipline; "owner earnings" where accruals suspect.
- **O'Shaughnessy (What Works)**: composites (value+quality+momentum) beat single
  factors — prefigures Novy-Marx.
- **Graham lineage**: margin of safety migrated from liquidation value (net-nets) to
  durability of franchise (moat + sustained ROIC) — same instinct, different axis.

## 6. The traps

1. **Aggregation**: growth-negative at macro and profitability-positive at firm level
   are MECHANISTICALLY CONSISTENT — aggregate growth is diluted away (issuance, new
   entrants, index lag) and competed away (the fade mechanism at macro scale); the
   firm-level premium is a within-market mispricing story. State the level every time
   "growth" is used.
2. **Peak-margin cyclical traps**: normalize ROCE/margins over the full cycle; spot
   screens buy commodity tops.
3. **Quality as a crowded trade**: identifying a great business ≠ any price is safe;
   the India FMCG/compounder 2010-20 era is the live example (dossier E).
4. **Ind-AS vs US GAAP**: Ind-AS 116 leases (~2019) inflate IC and EBITDA across the
   transition; promoter-group structures and related-party flows add noise Western
   metric definitions don't anticipate — adjust before trusting any Indian ROIC/ROCE
   series across 2019.
