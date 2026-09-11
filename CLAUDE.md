# The Cycle Program — session onboarding (read this first)

Multi-horizon "cycle stack" portfolio model, Indian markets (NIFTY 750 + gold + debt; three
books). Principal: gaurav@ionic.in. The binding rules live in `research/CONTRACT.md` — read
it before any research or parameter work; nothing below overrides it.

## The documents of record
- `docs/cycles/README.md` — the monograph queue and status (THE CYCLE ATLAS IS COMPLETE:
  38 monographs, bands 0-5 + candidates all addressed).
- `research/register/trial-ledger.md` — every trial and design, pre-registered, ~75 entries;
  bars are NEVER moved after a print (misses are recorded instead — M0/A6 precedent).
- `research/register/RUNSHEET.md` — every data pull still owed, with vault destination and
  the designs it unblocks. `research/OPEN_QUESTIONS.md` — the principal decision record
  (batch 3 pending).
- `docs/learn/README.md` — 42 published lessons + the Health Board dashboard (all archived
  in `docs/learn/artifacts/` — the repo copy is the archive of record).
- `docs/PIPELINE.md` (see the machinery-status addendum) and `docs/cycles/38-atlas-close.md`
  (the capstone synthesis + master verdict table).

## Non-negotiable working discipline
1. **Pre-register before running**: bars/priors into the trial ledger BEFORE any number is
   computed; interpretation written AFTER the print. Partial runs QUOTE the parent design
   verbatim (process note #5). Use `quant/stats/` machinery, never inline re-implementations
   (process note #6).
2. **Vault discipline**: free data only; every file sha256-manifested (`python3
   ingest/manifest.py <dir>`, WORM); two-pass AUTHENTICATION.md (anchors written and
   committed BEFORE checking values — near-miss #4). Mirrors never outrank primary pulls.
3. **Gated commits**: `python3 -m pytest tests/ -q` AND `python3 config/validator.py` must
   both pass before every commit (use `PIPESTATUS`, never pipe pytest through tail and read
   `$?`). ENFORCED AS MACHINERY since 2026-09-03: `.githooks/pre-commit` runs both gates
   (install once per clone: `git config core.hooksPath .githooks`) and
   `.github/workflows/ci.yml` re-runs them on every push. Commit and push EVERYTHING,
   always, to the designated branch.
4. **No magic numbers** (grids/quantile ranks with provenance); Hamilton never HP; Tier-C is
   reduce-only; adaptive rules live in `config/challengers.yaml` lanes (the validator
   refuses un-reviewed 'online').
5. **Preservation**: significant work ships as a Cycle School lesson (published artifact +
   committed copy in docs/learn/artifacts/ + a README row). Corrections go into published
   pages as dated update boxes — superseded claims stay visible.
6. Sonnet subagents max 3 concurrent; agents read CONTRACT.md from disk; chapter agents
   may cite ONLY desk numbers already printed in RESULTS/ledger files.

## Environment notes
- Egress: GitHub (raw/LFS/git-proxy clones) OPEN; NSE/RBI/CCIL/Kaggle/HF/FRED/wsts BLOCKED
  — those are principal-machine runsheet pulls (`ingest/pull_*.py`, auth skeletons via
  `--emit-auth-template`).
- Run analysis scripts with `PYTHONPATH=/home/user/claude-demo`.
- Vaulted and usable today: NIFTY 50 daily 2007-2026, NIFTY500 survivor panel 2012-2021
  (survivorship stated — one-way uses only), CBOE VIX 1990-2026, IIMA monthly factors,
  gold 1833-2026, JST, commodities, climate (see ingest/vault/*/AUTHENTICATION.md).

## Where work stands (2026-09-05)
Atlas complete; Stage-1 machinery live (quant/regime.py, walk-forward, book costs,
challenger CI, paper ledger); the phase file CLOSED at index resolution. Mirror legs 5-9
done: fx + India VIX + Kilian + Känzig + ONI + AISMR vaulted (10 vaults); H53a and OL-D2a
FAILED unconditionally (the global factor owns both commodity links — conditional-only
framings locked); CW-D1v PASSED (budget vol on the implied side, the day-0 crush); F5a
ruled RV-primary (both implied legs refused); OL-D1a PASSED with its two-sided prior
confirmed; EN-D2a resolved the B4a [VERIFY] at 56%/4.1x. Census 136 run cells; 45 lessons;
suite 118 green. **THE MIRROR FRONTIER IS EXHAUSTED (2026-09-03)** — every runsheet row is
either partially mirrored to its limit or probed dead (TSF, WSTS); the next data event is
necessarily principal-machine. SAME DAY, by principal directive: candidate generation
REOPENED (research/frontier/manager-frontier-sweep.md; candidates H60-VRP, H61-FLOWMULT;
breaks-registry.md BR1-BR6); TRACK T (technical-quant-systematic) opened and its runnable
backlog fully run — census 193, suite 125 (headline: the NIFTY premium accrues OVERNIGHT,
+24%/yr, calm-days only, stress is intraday; F3a-F6a all booked; T-CTRL1/T2/T3 graveyards);
TRACK P scaffold landed (quant/pipeline: triple-barrier, meta-labels, vintage stamping).
49 lessons. Blocked on the principal: OPEN_QUESTIONS batches 3+4 + the Priority-1 pulls.
2026-09-05, principal-directed research sprint: GDP-D1/FISH-D1 (growth does not drive
returns — cross-country -0.21, market leads GDP 5:1; Fisher rejected at 1y, 12pp
inflation-regime gap) and the ER-D1..D6 expected-return battery (valuation's horizon
staircase +0.15->+0.38; the Bernstein-Arnott slippage wedge prices at -0.79 and resolves
the GDP paradox; hurdle rule INVERTS at index level; pooled 5-factor equation 26.7%
in-sample at 10y but OOS fails at BOTH horizons once purged/honest-benchmarked (ER-D4b correction box) — Goyal-Welch binds fully; single-country
kitchen sinks explode OOS (-389%); the dp x inflation RANK GRID survives only as an
expectations qualifier: +5.1pp real-time corner spread, no OOS forecast value — ER-D7). EN-D1a onset-sectoral partial: null-inconclusive
(one-way), placebo caught COVID contamination. 2026-09-05 ULTRACODE AUDIT LEG: a 14-agent adversarial audit confirmed 8 findings
(winsorization lookahead, missing purge, unregistered windows, benchmark mislabel,
Stambaugh departure, within/between conflation); dated addendum + process note #8 +
quant/stats/preprocess.py booked; follow-ups ER-D7/D4b/D1b/D1c ALL run: 10y 'survives'
WITHDRAWN; growth-negative upgraded to a WITHIN-country timing fact (median -0.41);
L9's inflation gap STRONGER within-country (18.2pp, top-quintile years -4.1%/yr real);
only the 20y dp relation beats the persistent-regressor null. Census **308**; docs/MODEL-FACTORY.md (the
ten-station operating workflow) + research/notes/ context notes (repression era, real-rate
decades, capshare, regime sub-parts menu, DS1 briefing) all committed. Consumption of the
ER arc: valuation/inflation as STATES for expectations, never point forecasts. Lesson 50
for the ER arc + One Page refresh owed (in progress 09-05).
2026-09-07, the macro battery sprint (principal-directed, ledger entries of record):
ER-D8/D9 + GDP-D3/D4 (market leads GDP 1y and nothing further; slippage -0.79/-0.84,
tether REJECTED — the wedge compounds; growth HUMP: floor + dilution penalty; only
delivered dividend growth clears |0.6|); CU-D1..D7 currency battery (PPP +0.94 the
strongest print in the register; RER half-life 7.3y; UIP dead; crash anatomy 71 episodes
— local equities crash-immune, USD investors not; India coupling -0.69/-0.79, weak-INR
years -15/-24, next year +24; US dollar-regime HUMP); DB-D1..D9 debt battery (high public
debt kills BONDS not equities — US >=90%: eq 7/7 positive, bonds 1/7; three resolution
regimes, the modern era CARRIES; fiscal dominance = repressed rates + r-g -1.3% + FX leak
+3.7%/yr at >=120%, NOT inflation; debt->growth monotone 2.0->0.7%, no cliff; housing
mechanism test confirms the slippage doctrine; equity positivity is PRE-1980 only);
CI-D1..D5 credit+inflation battery (the killer cell is HIGH+RISING inflation: -3.0% vs
+4.4% falling-from-high — the L9 arc made 2x2; asset ranking there gold +9.6 > housing
+6.8 >> equity -3.0 > bonds -5.6; crises belong to CREDIT (boom 15-19% vs calm 5-6%),
returns to INFLATION; crisis event study: t0 -14.1%, recovery t+1, housing slows but
never negative). india-regime-playbook.md + leverage/safety addendum committed. Census
**442**; suite 127 green. Owed: Lessons 50-51 + One Page/Syllabus refresh (the whole
sprint), then the principal-gated OPEN_QUESTIONS batches 3+4 + Priority-1 pulls.
2026-09-08, the option-program + fundamentals arc (this status supersedes the census
figures above; census now 1,130): THE STANDING BOOK is the corrected 65/20/15
collar-stacked book at +11.46 CAGR (TR ~+12.76) / -11.36 maxDD (SW2-A1 baseline; OP-D3
condor engine + put ladder + covered calls; margin model hedged 2.5%/unhedged 10%).
Two optimization grids (OP-D3b, OP-D7) and sweep 2 (21 agents, adversarially verified)
all REFUSED their train winners OOS — return gap to 15/15 is alpha/data-gated (real
chains, PIT breadth, sub-6% funding), risk side beaten with room. Corrections booked:
E1 month-drop, E2 free leverage, idle-cash credit, stats_of slicing, factor-margin
line. MR dead at all frequencies; synthetic-futures leverage at 6% dead; weekly sells
dead OOS. TRACK FUN OPENED: the phase inversion at three scales (recovery/contraction
beat expansion/slowdown next-year; earnings-cycle census 1871-2023, price leads E-troughs
10m; India defensives lag once risk-off is identifiable); FUN-D8 monetary seasons
(falling rates +8.0 vs +3.3; slope RANKS returns — flagged upgrade pending India
verification; avoid-state = hiking-into-slowdown -5.2%/yr). QG TRACK: two new vaults
(factors_us FF5/FF6/Q5 ~2020 vintage; firm_panel data_ml 1,207 US stocks 1999-2019,
no-delisting caveat); QG-D1..D5 booked — payout is a repackaged earnings-state variable;
the EW-survivor junk artifact caught (inversion collapses in large caps); growth never
pays at any horizon; the MODERATION PRINCIPLE (champion cell = moderate ROE x low vol;
glamour-quality 2.9%/yr at 10y); R_EG flag quantified (unspanned +8.3%/yr alpha, t=10.9,
100% in-sample — not consumed). QG-D6 (India q-EG, NIFTY 500 PIT) REGISTERED-UNRUN,
frozen; the India as-filed fundamentals HANDOFF PROMPT is out to the principal's other
Claude (research/register/handoff-prompt-india-fundamentals.md; landing kit in
ingest/receive_india_fundamentals.py) — six QG designs unblock on arrival. Dashboards:
quality-growth-factor-atlas + return-distribution-atlas (docs/learn/artifacts/, rows
50-53). Docs: STRATEGY-HANDOFF.md (give to any new Claude), docs/fundamentals/01+02.
Still principal-gated: OPEN_QUESTIONS batches 3+4 + B4-4 (foreign-equity scope),
funding_rate, Priority-1 pulls. Artifact-watch subscriptions REFUSED this session —
comments on dashboards do not wake it; ask in-session for changes.
2026-09-09: FUN-D9a + FUN-D10 booked (census **1,140**; suite 125 green): the FUN-D8 m2
slope-ranks-returns flag HARDENS (US monthly medians flat 13.8/13.4/13.3 — the registered
FLAT branch taken; the recession-odds channel survives, 26/28/14) and repo-direction
conditioning of the India factor sleeve is REFUSED as a design family (RMW prior missed —
better in FALLING; market split reverses post-1990; era-fragile). The One Page + Syllabus
artifacts refreshed to the construction era (rows 50-53, census 1,140, the standing book,
the batteries, the India handoff queue, batches 3+4) — the owed preservation items cleared.
Still waiting on the principal: the India fundamentals drop (QG-D6 + five frozen designs),
OPEN_QUESTIONS batches 3+4 (incl. B4-4), funding_rate/ADV, Priority-1 pulls.
2026-09-10, the ES/SC arc (principal-directed: earnings revisions/surprises + small-vs-large
predictability; census **1,160**; 3 Sonnet dossiers in research/notes/es-dossiers/): ES-D1
KILL — EPS rank-migration (fundamental-momentum proxy) prints NEGATIVE (-3.03/-6.47 D10-D1)
on the EW-survivor panel, the within-momentum gate failed (+0.42 vs +2.00), diagnosed as the
QG-D2 reversal artifact; Atlas 3.5's DATA-REJECT on India consensus STANDS; the India route is
a PIT PEAD event study on the handoff's filing_date (registrable on arrival). SC-D1 first
gate PASSED — the small-vs-large Pb-spread orders next-12m relative return (+16.05pp T1-T3,
corr -0.69 at 36m, Pe-robust; in-sample, flagged); the growth gap runs weakly POSITIVE; NSE
index-valuation runsheet row added (2021 splice caveat named). SC-D2: US SMB momentum is
pre-1981 only (+7.96 -> -0.4/-0.7) — era-fragility instance #3; post-bear small rebound real
(+5.15pp). SC-D3 HEADLINE: the rebound INVERTS in India (-12.31 vs -0.20 after down years;
gap -12.11pp) — playbook addendum: NO smallcap adds for 12m after a bear year (Tier-C);
the only India timing shape is the 36m winter rebound (+10.32, a watch); IIMA regime map
passed its sanity gate (2018 peak, 2023-24 froth visible; mean -2.82%/yr matches TL-D2).
Lesson 54 published (row 54). Model note: principal directed (09-10) all subagents run on
Sonnet/Opus, never the session default — Fable weekly limit exhausted.
Same day, the edge-map leg (3 Sonnet runners on frozen specs, desk-verified; census
**1,189**): ES-D2 the value+catalyst gate FAILED (-1.57 vs +2.00; cheap+improving LOSES to
cheap-alone) — the ES-D1 kill is final, no interaction rescues EPS rank-migration; SC-D4
only VALUE survives every size quintile (szQ5 +9.95/1m, +8.80/12m) — Mom/Vol/Roe/Gr spreads
all junk-swamped on this EW construction (measurement limit booked; factor evidence stays
VW); SC-D5 the re-interrogation branch fired (large-growth +6.07 is the worst corner, small
rows inflated) and the value-growth gap is SIZE-STABLE (~+5-6pp at 12m both halves).
THE EDGE MAP dashboard published (row 55, edge-map.html): every edge ranked
consumed/flag/graveyard/gated + all new matrices. Row 56 = the Earnings & Size Alpha
Brief (the three-metric synthesis + the 3y update box). H36-D1 booked (census 1,202):
at 3y the junk noise washes out — low-vol flips positive in mid/large caps, szQ5 value
+6.5pp/yr at 3y / +4.83 at 5y, V_t terciles +16.75pp/yr at 36m, the India post-bear
rule extends to a 3-YEAR fact (-5.93/yr; playbook updated) and the winter rebound is
monotone at 3y (LO +8.01/HI -3.27); growth-gap conditioner dies at 3y.
2026-09-10 (evening), the VAL arc (principal-directed: valuation as edge +
complementarity; census **1,231**; 3 Sonnet dossiers in research/notes/val-dossiers/):
VAL-D1 measure ladder — COMPOSITE ~ Pb lead the szQ5 column (+8.97/+8.80 at 12m);
FCF/EV priors missed; the Div_Yld split (-4.6 panel / +5.10 large) is the payout
confound live. VAL-D2/D3 — the WCS/trap side fired on the no-delisting artifact
(every filter negative; traps cannot spring where deaths were deleted — booked as
artifact, program moves to India PIT + pledge marker); the robust fact is VSC: the
value spread survives WITHIN every companion family (+12.5-14.8). VAL-D4 (VW,
clean): HML+UMD Sharpe **0.70** (corr -0.21) — the pairing doctrine = value x
momentum x moderate quality; CMA is value in drag (corr +0.68, no blend gain); the
blend does NOT truncate the tail (-37.4 vs -35.1 worst-12m — sizing owns the tail).
VAL-D5: CAPE terciles price the FLOOR — cheap p10 -2.00 vs expensive -4.92
(+2.92pp/yr >= the +2.00 bar; ER-D1c null-band caveat quoted, no timing claim).
Valuation Edge Atlas published (row 57). VAL-D6 extension booked same evening
(census **1,245**; Sonnet runner, desk-verified): the measure x size x horizon
atlas — P/B owns both halves; the pure-valuation composite VAL3 (Pb+EV+FCF) beats
Pb in LARGE caps at every horizon (+8.76/+7.80/+5.88); every yield measure INVERTS
in small caps (the bounce pays distress); CQ/VM stock-level mixes MISSED (rank-mix
fails where the momentum ingredient is artifact-broken) — pairing stays at SLEEVE
level; Ebit_Bv weak-hybrid; P/S NOT constructible on the uniformized panel —
India-gated (P1 revenue+shares + P4 prices = PIT P/S). Atlas v2 same URL. FOUR
val-dossiers committed (a measures/methods, b complementarity, c India practice,
d horse-races/combinations — d reconciles the missed FCF/EV priors as construction
mismatch vs Loughran-Wellman's actual claim and ties the trap-filter artifact to
the BGLN retained-earnings mechanism).
2026-09-10 (night), TRACK TECH (principal-directed: technicals; census **1,270**;
2 Sonnet dossiers in research/notes/tech-dossiers/ + Sonnet runner, desk-verified):
TECH-D1 ATH battery — don't fear the high (Shiller ATH months +9.46 vs +8.29;
P(neg) 28 vs 32); the entry state again (NIFTY deep-drawdown tercile +33.66 next-12m,
+21.54/yr at 36m); index 52w-proximity ranks INVERSELY; breakout events nothing
(n=15). TECH-D2 stages — quadrants rank VOL exactly (S2 13.7% vs S4 26.3%); the
"buy stage 2" folk claim INVERTS for equity indices (S4 +32.2 next-12m NIFTY) and
holds for GOLD (S2 +11.3 vs S4 +0.55 — trend asset); THE KEEPER: S4-cheap +14.65 vs
S4-expensive +0.27 (Shiller) — downtrends are entries only from cheap; T-CTRL1/T2
untouched (states, never rules). TECH-D3 momentum condition map — post-bear UMD
-9.30 vs +10.64; high-VIX -9.73; THE GATE FIRED BOTH MARKETS (crash state = post-bear
+ top-vol: US -22.48 n=44, India -27.46 n=15) -> the momentum stand-down monitor is
REGISTRABLE (Tier-C, wired when the India sleeve exists); India's dominant conditioner
is the vol state (low +20.0 / high -7.2); own-factor momentum fails (US) / inverts
(India — never chase WML strength); stock-level lookbacks unanswerable on the EW panel
(artifact), index answer stands (TS1: 3m NIFTY / 12m gold); vol-scaling mitigates,
doesn't flip. TECH-D4 valuation clustering — P(stay) 0.97/0.98 monthly, spells
37-43m mean; de-rating exits -7.21% next-12m vs cheap-exits +16.51. Playbook Track
TECH addendum + Technical States Atlas published (row 58). Sector RS stays gated on
the NSE sectoral TR pull (design brief in tech-dossier a).
Same session, principal follow-up on lookbacks (regime-conditioned 3-6m vs 6-12m STOCK momentum):
MOM-D1 booked (census **1,288**; one bug found+fixed pre-verification, window_sum() closed over the
wrong array, caught because India printed all-NaN; desk-verified). US: every lookback window (3-1
through 12-7) inverts on the EW no-delisting panel — a third independent confirmation of the same
artifact (SC-D4, TECH-D3 m9); ungradeable. INDIA: 6-2 (6-month formation, 1-month skip) is the
outright peak in both the full panel (+15.59%/yr) and the liquid top-ADV tercile (+5.87), and the
ONLY window staying positive across every India-VIX tercile while 12-7 flips negative under vol
stress (+27.6 -> -9.7) — a registrable "shorten toward 6-2 in rising vol" refinement; 3-1 flips
negative in liquid names (reversal, not momentum); a third confirmation (stock-level now) that India
momentum is up-market-only. Atlas updated (v2, same URL).
Then the principal asked sector RS/leverage-timing/vol-clustering/copper-gold/silver-gold/nifty-gold/
smallcap-nifty: SECTOR-GATE formal note booked (fully data-gated, zero cells) + RATIO-D1 booked
(census **1,297**; one date-alignment bug found+fixed, IMF copper month-start vs gold month-end,
caught pre-verification; desk-verified). Vol-clustering-reduces-risk QUOTED (F2/F3a/TS1/TL-D2 s10),
not re-run. Copper/gold: real US/global growth read (RISING +15.11%/yr vs FALLING +10.55) but ZERO
India-specific edge (NIFTY split flat). NIFTY/gold ratio: a genuine 12m mean-reverting rebalance
state (trend AND percentile cuts agree — fade extension). Silver/gold and the smallcap/nifty ratio's
own level add nothing new (thin/non-monotone; the ratio's persistent downtrend independently
corroborates TL-D2's -2.9%/yr). THE LEVERAGE-TIMING READ INVERTS THE FOLK INTUITION: safest fwd-126d
NIFTY state is HIvol+LOWdd (6.31% maxDD, a post-spike recovery signature); the WORST and most common
state is the calm LOvol+LOWdd grind-up (10.70%, n=1,431) — no leverage-timing rule registered; the
negative finding stands alongside the no-leverage-until-funding_rate gate. Atlas updated again (v3,
same URL, now TECH-D1..D4+MOM-D1+RATIO-D1, 52 cells). RUNSHEET's NSE-sectoral-TR row now named as the
one pull that unblocks FUN-D3 FULL + SEC-D5 + the sector-RS design together.
Then the principal moved to earnings quality/accounting red flags + a deeper sector-RS pass (2 Sonnet
dossiers in research/notes/eq-dossiers/ + tech-dossiers/c; EQ-D1 booked, census **1,305**, desk-
verified independently on two cells). The panel's fields are pre-uniformized ranks, so every
construction is an explicit RANK-DIVERGENCE PROXY (Ni_rank minus Ocf_rank for TATA, etc.), never the
textbook formula; the one-way argument is DISTINCT from VAL-D2/D3 (the accrual anomaly's worst outcomes
are exactly what a no-delisting panel deletes, so the bias WEAKENS not inverts it — a negative print is
admissible). TATA_proxy is negative at every horizon/cut (panel 12m -11.88, large -4.76) — HIT. Both
Beneish-style components (margin-decline, leverage-increase) run BACKWARDS (+5.27/+2.22 at 12m) — MISS
— and the mechanically-combined composite DILUTES rather than strengthens the signal (large-cap flips
to +2.68) — the arc's central lesson: verify each ingredient's sign before compositing, never port a
textbook score blind. The value-trap cross inverted again — a THIRD sighting of the within-cheap
artifact (VAL-D2/D3, SC-D3a), still PIT-gated. Earnings Quality Atlas published (row 59) with the full
India buildable/not-buildable field map. Both dossiers landed same-day and are now integrated (zero new
cells; literature/cross-check only): tech-dossiers/c widens the industry-momentum literature (Moskowitz-
Grinblatt, Hong-Torous-Valkanov, Grundy-Martin — flagging an open, unrun question on whether L3/N4a's
momentum leg is partly undisclosed industry momentum) and Indian AMC practice, then delivers a REVISED
SECTOR-RS VERDICT cross-checking the desk's own booked FUN-D1/D2/D3 prints rather than approximating
sector data: no direct rotation edge is measurable (SECTOR-GATE stays fully gated), but FUN-D3 already
shows that once an India stress state is identifiable, defensive rotation has missed its window and
cyclicals/financials lead the rebound instead — Tier-C, reduce-only, folded into the Technical States
Atlas (v4, same URL). eq-dossiers/a corrects the atlas's own India buildability table: the true Beneish
ceiling is 4 of 8 components unbuildable (DSRI/AQI/SGAI/DEPI — not the 3 first listed; true CFO/EBITDA
is separately blocked for the same missing-D&A reason), cites Hribar-Collins (2002) as the proper TATA
construction, and uses Dechow-Ge-Larson-Sloan's classify-vs-predict-returns distinction to explain why
EQ-D1's composite backfired; also flags an unresolved [VERIFY: Beneish 1999 cutoff -2.22 vs -1.78] and
confirms promoter share pledging (P5) as India's cleanest, genuinely point-in-time red flag (named
examples explicitly [CASE-STUDY LORE] only). Earnings Quality Atlas updated (v2, same URL). Ledger
addenda booked under SECTOR-GATE and EQ-D1 (zero census impact — 1,305 stands). Leg 28 closed.
Principal follow-up same day: "red flag lists... which time frame it will work" (1m vs 12m/3y/5y).
SYNTHESIS-RF1 booked (zero new cells; every number quoted from an already-printed ledger entry):
red flags sort into three horizon behaviors, not one rule. DECAYING (peak at 12m, fading by 3y,
same sign) — accrual/TATA_proxy -11.88%->-4.43%/yr, India post-bear smallcap -12.31%->-5.93%/yr.
GROWING (flat or wrong-signed at 12m, only real by 3-10y) — large-cap peak-ROE-at-any-price
+1.4pp(12m, wrong sign)->-2.1pp(120m); the glamour-quality corner (ROE Q5 x growth Q5) 6.5%/yr(12m)
->2.9%/yr(120m, worst corner); the mirror protective spreads (szQ5 value, low-vol) grow the same
way. REGIME/PROBABILITY (no fixed horizon is the right frame) — sovereign debt LEVEL never hurts
equities even at 5-10y (DB-D1 +0.16/+0.17, positive-signed) and only ever hits BONDS (US >=90%
cohort: -1.0%/yr, 1/7 positive); credit BOOMS don't lower 5y equity returns (null) but raise crisis
odds on a 3-YEAR clock instead (15-19% vs 5-6% calm); the "debt helps equities" read is a dead,
pre-1980-only regime (+0.19 pre / -0.05 post). A fourth class, governance/mechanism-only flags
(promoter pledge, RPTs, Beneish/DGLS raw), carries no desk-quantified horizon at all and is read as
an always-on avoid-list gate, never a timed signal. Red Flag Horizon Map published (row 60,
red-flag-horizon-map.html) — the full table, every flag against its entry ID and exact print.
Same day, principal asked for more ("any other red flag list or manipulation etc"):
eq-dossiers/b booked (EQ-DOSSIER-B, literature only, zero cells) — Altman Z/Z''(EM) and Ohlson
O-Score (bankruptcy-risk scores, a different target than manipulation, same distinction as
Beneish-vs-DGLS), Montier's C-Score (a practitioner checklist that independently corroborates
EQ-D1's own mechanisms and adds one new ingredient, Days Sales of Inventory), Schilit's 7
Financial Shenanigans (a technique checklist, not a formula — the honest boundary every ratio
score on this page shares: round-tripping/reserve-smoothing/big-bath timing need footnote text
no aggregate field replaces), Benford's Law (a distributional test, feasibility on P1's ~8
fields left an open [VERIFY], not silently dropped), and five market/behavioral signals
(insider selling, short interest, auditor fees, options-grant timing, earnings-call
linguistics) that use no accounting ratio at all and need data sources entirely outside
P1-P6. THE CEILING, independently corroborated a fourth time: Altman/Ohlson/Montier are each
only partially buildable from the India handoff schema for the SAME missing-granularity
reason Beneish was capped at 4-of-8 (no receivables/inventory/current-asset-liability
split/gross PP&E detail) — three unrelated frameworks hitting one schema limitation, not
three new complaints. Earnings Quality Atlas updated again (v3, same URL).
Same day, principal asked for the factor zoo sorted large-cap vs small-cap, India-specific.
SYNTHESIS-FZ1 booked (zero new cells; every number quoted from an already-printed entry) — first,
a data-honesty statement: the desk's largest factor body (QG/VAL/ES/SC/EQ) ran on the US firm_panel
as a REHEARSAL, never India evidence; presenting those size-quintile splits as India large/small
would have been a labeling error. REAL India evidence is narrower (IIMA SMB/HML/WML/MF/RF, NIFTY,
the NIFTY500 survivor panel). LARGE-CAP best-to-worst: the vol-managed WML+HML blend (+17.02%/yr,
the only India factor construction actually IN the standing book); momentum (a SWITCH, not a
constant -- +15.06 baseline, -27.46 crash state, own-strength-chasing inverts); value alone
(+8.6%/yr, low Sharpe 0.09, real winters); leverage-timing (folk intuition inverts). SMALL-CAP
best-to-worst: the value-spread rotation TIMER (+16.05pp T1-T3, the one real timing edge);
liquid-tercile momentum; the winter rebound (downgraded to a watch, survivor-panel cross-check
non-monotone); low-vol (inconclusive, t=1.88); post-bear re-entry (INVERTS the US rebound,
Tier-C avoid); the raw size premium itself (UNCOMPENSATED at -2.9pp/yr, TL-D2's headline). India
Factor Zoo published (row 61, india-factor-zoo.html).
Immediate follow-up: "more... lessor crowded but works good and can continue to work good in
future." SYNTHESIS-LH1 booked (zero new cells) -- reframes the question as execution/timing/
governance edges, each graded on WHY it should resist arbitrage. CONFIRMED and durable: the
overnight/intraday split (T1, +24.0%/yr vs -12.6%/yr -- not a tradeable arbitrage, an execution
fact); the currency-crash entry state (CU-D4iii, next-3y +13.2% vs +6.2%, requires holding through
the crash); promoter share pledging (durable because the edge is DOING THE DATA WORK, not
information asymmetry); the earnings-cycle phase inversion (FUN-D1/D2/D3, price leads earnings
troughs ~10 months); the 3y smallcap contrarian pair (avoid 12m post-bear + the 3y winter rebound
-- patience itself is the moat); the high+rising-inflation asset ranking as a tactical overlay.
FLAGGED AS FADING, not durable: the turn-of-month premium (T6-TOM) shrank across the SIP-era
break and its hypothesized mechanism was refused. REGISTERED, data-gated: H61-FLOWMULT, H60-VRP,
RC1 (reconstitution, a CLOSING window unlike everything else here), the India promoter-pledge+
accrual composite, the R_EG flag's India adjudication. EXPLICITLY FLAGGED AS NO LONGER LOW-HERD:
VRP/option-selling -- arguably the most crowded strategy in Indian markets today, which is why
SEBI imposed the 2024-26 retail-derivatives curbs, and why this desk's own optimization grids
refused their own train winners OOS. Folded into the India Factor Zoo (v2, same URL).
Immediate follow-up: "basis all these analysis... current environment and positions to take...
expected next 1y/3y returns... sectoral bet hedge or other." SNAPSHOT-1 booked (descriptive, no
bar/prior, census 0) -- a genuinely NEW read of the LATEST date in each vault series (not a
synthesis of history), each construction quoted verbatim from its booked parent design; desk-
verified (NIFTY drawdown, FX dlog independently re-derived by hand). READING: NIFTY as-of
2026-04-13 (~5mo stale) is -9.44% drawdown (MID tercile), +2.19% trailing-12m (UP year, the
post-bear-avoid rule inactive), stage S4 (below/falling 200d MA) -- TECH-D2's own S4 finding is
VALUATION-CONDITIONED and no India valuation percentile exists anywhere in the vault, named as
the single biggest open question. Gold (2026-07) is +21.95% trailing-12m but -11.2% off its
2026-05 peak -- stretched and correcting. NIFTY/gold ratio: FALLING, LOW percentile (RATIO-D1:
historically favors NIFTY over gold forward, though active rotation already found to lose to a
static blend). WML (IIMA, 2025-12) ran hot (+8.27% trailing-3m) -- a caution against chasing it
per TECH-D3's inversion finding. SMB rolling-5y is POSITIVE (+3.2%/yr annualized), in tension
with TL-D2's -2.9pp/yr 32y base rate and sitting inside the already-flagged 2023-24 froth window.
RF is FALLING (historically the better regime, FUN-D8). FX (2026-08): INR is in a weak-INR year
(+8.61% dep, above the 5% threshold, below the 15% crash one) -- CU-D6(d)'s own India read: such
years average -12.6%/-20.6% (local/USD) vs +34.2%/+35.5% other years, with the YEAR AFTER
averaging +25.5%/+23.7%. CBOE VIX (2026-08-31, freshest series) sits in the LOW tercile -- calm,
global not India-specific. GAPS NAMED: India VIX stale since 2023-04, copper/gold stale since
2017-06, no live debt/credit/inflation nowcast (JST-based, structural context only), and critically
NO India valuation percentile exists in the vault at all. CONSUMPTION, Tier-C throughout: hold
standing-book weights (no index-level entry or avoid gate fires); do not add fresh momentum beta
(WML ran hot); hold gold as the strategic hedge, don't chase it after the run; no tactical
equity-gold rotation (already-refused); smallcap neutral-to-underweight (no active trigger either
way); the weak-INR state argues against newly adding unhedged USD exposure right now (B4-4 stays
the principal's decision); no sector call (SECTOR-GATE stays fully gated). NO POINT FORECAST
GIVEN for 1y/3y, per the ER-arc doctrine (the pooled-equation OOS failure + the -389% kitchen-sink
explosion are exactly why) -- only state-conditional historical distributions, each named. Published
as docs/learn/artifacts/positioning-note.html (row 62), explicitly marked PERISHABLE (built from
vault snapshots ~2-9 months stale; the single highest-leverage fix is the still-unpulled NSE
index-valuation history, SC-D1's runsheet row).
Immediate follow-up: "final ideally best holding of reit, bond, gold, equity large mid small."
Addendum to SNAPSHOT-1 booked (zero new cells) -- a top-level allocation, each row explicitly
tagged desk-grounded vs untested-default rather than one undifferentiated number: equity large
50% (DESK-GROUNDED -- every real India factor edge this session found lives here), mid 10%
(UNTESTED interpolation -- no mid-cap-specific design ever run), small 5% (DESK-GROUNDED,
DELIBERATELY UNDERWEIGHT -- TL-D2's -2.9pp/yr uncompensated base rate, current 5y-SMB inside
the flagged froth window, not zero because SC-D1/H36-D1 give real occasional tactical add-backs);
gold 15% (DESK-GROUNDED -- CI-D2 + the CU battery's secular carry + Sharpe 1.19 hedge value,
HOLD not ADD given the current stretched state); debt/bonds 18% (GENERAL PRINCIPLE, not
desk-sized -- no bond-duration design ever run; RF currently falling is a mild duration
tailwind); REIT 2% (NOT DESK-RESEARCHED AT ALL -- zero vaulted data, zero ledger entries,
named as the honest gap). Explicitly disambiguated from the standing book's own internal
65/20/15 structure (a coincidentally similar number, a different question -- that one is
WITHIN the equity sleeve, this one is the portfolio-wide split). Folded into the Positioning
Note (v2, same URL).
2026-09-11, principal asked what research territory is LEFT ("we have done macro funda and
technical... what else can give us edge and alpha"). GAP-MAP-1 booked (agenda document, not a
trial; zero cells) — research/frontier/coverage-gap-map.md. Method: enumerate the alpha space,
SUBTRACT what the ledger already booked, SUBTRACT what RUNSHEET already queued, report only the
residual (which is why shareholding-pattern/IPO-listings/reconstitution/results-calendars/CP-CD/
FPI-flows/sectoral/valuation/CPI do NOT appear — already queued). THE RESIDUAL: (i) RUNNABLE
TODAY, no pull — rebalance-band/frequency grid (the rebalancing RULE itself has never been
tested, only static-vs-active per T3), concentration curve, cross-sectional dispersion as a
STATE, and the India LTCG 1-year-threshold turnover asymmetry (prices whether MOM-D1's winning
6-2 window survives its own tax bill — no US-derived study can answer it); rationale: the OP
sweeps showed the return gap is alpha-gated while the RISK side has headroom, so construction
mechanics beats another factor hunt, and these attack CERTAIN costs not hypothetical alpha.
(ii) NOT ON ANY RUNSHEET — the exchange-microstructure disclosure suite (delivery %, F&O BAN
LIST — a candidate for the stock-level crowding instrument India's factor book has failed to
find three times: CR1a/CR2/CR-D2a, ASM/GSM, circuits, bulk/block deals, rollover/OI); the
corporate-event suite beyond results (IPO LOCK-IN EXPIRY as the cleanest dated mechanical supply
shock, buybacks with acceptance ratios, demergers, open offers, delisting reverse-book-building,
promoter preferential allotments); the India G-SEC CURVE (smallest pull on the page, and it
discharges the EXPLICITLY OWED FUN-D8 India slope verification); corporate bond spreads +
rating migrations; GIFT Nifty basis + ADR/GDR premia (the natural extension of T1's overnight
finding); filing/call text analysis; and AMFI SCHEME-LEVEL NAV history — the one row bearing on
the OPERATING business (MF alpha persistence, capacity decay, flow-performance loop). Eight rows
added to RUNSHEET under a dated gap-map section. (iii) CHEAP FIX TAKEN: breaks-registry had NO
TAX DIMENSION — BR7 (LTCG reintroduced, Budget 2018), BR8 (DDT abolished / dividends taxed in
recipient's hands, Budget 2020 — with an explicit rule that VAL-D1's Div_Yld split and QG-D1's
payout finding must NOT be read across it), BR9 (buyback tax changed twice 2019-07/2024-10 +
F&O STT increase) registered, each with a pin-the-notification [VERIFY] per BR4/BR6 precedent,
deliberately ahead of their consumers. Nothing promoted; every gap-map row still owes its own
pre-registration.
Immediate follow-up: "do the runnable today ones" — the gap map's Tier-1 construction battery run
(G1-G4 pre-registered with falsifiable bars BEFORE any computation, two cells desk-verified;
census **1,336**; scripts/analyze_gap_tier1.py; config/costs.yaml gained a fully provenanced
`capital_gains_tax_india` block). This leg attacks CERTAIN costs rather than hypothetical alpha,
per the gap map's own rationale. G1 rebalance grid — bar met (net spread 0.364pp/yr), winner
SEMI-ANNUAL at 13.55% net; priors partly missed (the gross CAGR/vol spread printed 0.102 vs the
<0.10 bar — recorded as a boundary MISS, not rounded into a pass; the ±10pp band limb missed at
+0.02pp; turnover monotonicity hit at 10.20/6.93/3.67). THE HEADLINE IS UNREGISTERED: pure drift
("never") had BOTH the best CAGR/vol (1.275) AND the shallowest maxDD (−20.62% vs −23.87..−25.16%)
— rebalancing ADDED drawdown over this sample, the opposite of the folk risk-control claim; monthly
is the one dominated choice (worst net CAGR, 16.31%/yr turnover, no risk benefit). "Never" is NOT
adoptable — unbounded drift breaches the mandate's weight bands — so the consumption is
semi-annual-or-annual, never monthly. G2 concentration curve — tail bar CLEARED (p10 terminal
wealth N=20→50 = +11.08%); the flattening prior MISSED, CAGR/vol keeps climbing past 20
(1.201→1.215→1.276→1.285→1.302→1.304) and settles only near ~100 names; practical floor 50-100;
one-way admissible (the panel's bias flatters concentration and concentration still loses); levels
(25-27%/yr) are survivor-absurd, ONLY the shape is evidence, and it is a zero-skill random-draw
curve that says nothing about a skilled book's optimal N. G3 dispersion-as-a-state — DISTINCT BUT
UNUSABLE: the redundancy branch did NOT fire (corr with panel realized vol 0.453 < 0.70, so
dispersion is genuinely not repackaged vol), but the fwd-1m momentum gap (+10.22pp, clears +5) is
NOT monotone (MID 15.21 > HIGH 13.36) → bar PARTIALLY met → not promoted; fwd-12m fails outright
(+4.20pp). Real content: LOW dispersion is where momentum is weakest (+3.14 vs +13-15). Low-vol
rows negative everywhere = the known EW-survivor artifact (QG-D2, SEC-D7 a6), flagged and
deliberately not interpreted. G4 India LTCG holding ladder — THE TAX LINE IS REAL BUT SECOND-ORDER
and MOM-D1's 6-2 short-hold construction STANDS: 13m after-tax loses to 1m under both regimes
(23.50 vs 27.35, −3.85pp pre-Jul-2024; 22.86 vs 25.57, −2.71pp post), i.e. Jul-2024 narrowed the
short-hold advantage ~1.14pp/yr without flipping it; break-even 1m gross needs 2.088%/mo (pre) or
2.163%/mo (post) vs actual 2.394%/mo — the post-2024 margin is only ~10% of gross, booked as a
degradation-risk flag. Prior partial miss: gross is a HUMP peaking at 3m (36.52), not a monotone
decline. UNREGISTERED CANDIDATE, NOT CONSUMED: the 3-month hold dominated the 1-month hold on every
metric at the same STCG rate and a third of the turnover. Binding caveat: non-overlapping n =
83/27/13/6/6 — the 12m/13m cells rest on SIX observations, direction only. G5 (the standing-book
rebalance-interaction cell) stays REGISTERED-UNRUN with a frozen spec — it needs the book engine
plus a margin/collar interaction model, and registering unevaluable bars would be a fake
registration. Construction Mechanics Atlas published (row 63). Suite 125 green. Still
principal-gated: the India fundamentals drop, OPEN_QUESTIONS batches 3+4 (incl. B4-4),
funding_rate/ADV, the Priority-1 pulls, and every gap-map Tier-2 row (each still owes its own
pre-registration).
Immediate follow-up: "i want to know more on churn and related stuff for edge" — THE CHURN
BATTERY (CH-D1..CH-D5, pre-registered and the registration COMMITTED (6d56c31) before the run;
four cells desk-verified on different code paths; census **1,365**; scripts/analyze_churn.py +
research/churn.json). "Churn" was read in BOTH its meanings and the halves kept apart because
they are different questions: OUR churn as a cost to manage (CH-D1..D3, continuing G1/G4) and
THE MARKET's churn as a signal (CH-D4..D5, never run standalone before — Share_Turn_12M had
appeared only as a VAL-D2 companion and VAL-D3 trap marker, both inside a family already booked
artifact-driven). A third reading (the fund industry's own portfolio-turnover ratio) is
data-gated and got a RUNSHEET row, not a design. TWO RUNNER BUGS FOUND AND FIXED BEFORE ANY
INTERPRETATION WAS WRITTEN, both recorded because both would have flattered a result: gross was
geometric CAGR while net was arithmetic-compounded (the "net > gross" units mismatch), and
CH-D2 was costing turnover with a 1/k proxy instead of actual weight change, which overstated
k=1's trading ~2.5x and BIASED CH-D2's OWN BAR toward its winner — with the real measure the
gain fell +4.37 -> +1.67pp/yr. CH-D1 rank buffer: BAR PASSED ON THE NUMBER (+0.73pp/yr net at
b=0.05) AND DELIBERATELY NOT BOOKED — the registered one-way rule disposes of it (buffering
holds names longer on a panel that deleted its delistings, so "buffering helps on return" is
non-evidence-grade). Admissible instead: the risk column runs the WRONG WAY for the artifact
story (vol 23.06->21.53, maxDD -29.29->-26.15 monotone as b widens), with the honest confound
named — the book grows 42->72 names and G2 booked the same day that diversification keeps
paying past 20, so the risk gain is plausibly G2's effect arriving through the buffer. CH-D2
overlapping re-formation: BOTH BARS PASS — **THE BATTERY'S ONE PROMOTION**. G4's 3-month gross
hump REPRODUCES on 83 monthly observations per cell where G4 had six at H=12/13, so G4's hump
was real and its record STANDS; k=3 (a third of the book re-formed monthly, each tranche held
3 months) has the best gross 33.81 / net 32.24 / after-tax 25.12 AND the shallowest maxDD
-25.40 of the five, beating k=1's 23.57/-29.29 by +1.55pp/yr after tax. PROMOTABLE WHERE CH-D1
IS NOT BECAUSE THE ARTIFACT STORY IS INTERNALLY FALSIFIED: if deletion simply rewarded holding
longer, k=12 would win — instead it is worst on gross (28.22) and by far worst on drawdown
(-33.54). Tranching also beats buffering head-to-head (25.12 vs 24.13), so to cut churn on
this sleeve, STAGGER THE RE-FORMATION rather than widen the exit band (Tier-C, wired when the
India stock sleeve exists). CH-D3 partial adjustment: BAR FAILS and the failure is the finding
— net CAGR spread across the whole lambda grid is 0.20pp while maxDD spread is 3.92pp, and THE
DRAWDOWN PENALTY IS FRONT-LOADED (a quarter-step costs 3.08 of the 3.92pp, 79% of the damage,
for 42% of the turnover; CAGR/vol monotone 1.275->1.177). No gentle-rebalancing free lunch: any
rebalancing pays nearly the full drawdown price and trade SIZE is not a lever — this closes the
question G1 left open (partial adjustment does NOT rescue drift). CH-D4 turnover-as-signal (US
panel, REHEARSAL): BAR FAILS DECISIVELY AND NON-EVIDENCE-GRADE — szQ5 12m NEGATIVE at every
lookback (-2.10/-2.76/-2.25), i.e. high-turnover won, exactly the artifact-suspect direction, so
the Datar-Naik-Radcliffe neglect premium is booked NOT MEASURABLE here (fifth sighting of the
deletion artifact) rather than rejected. Surviving in the admissible direction: the 36m column
is POSITIVE at every lookback (+4.07..+4.67 — H36-D1's washing-out again, and a within-measure
1m/12m-vs-36m sign flip is itself the artifact's signature) and Lee-Swaminathan's interaction
prints +4.70pp at 12m — QUIET WINNERS BEAT LOUD WINNERS. CH-D5 India volume shock: the textbook
turnover ratio is NOT CONSTRUCTIBLE (rupee value traded exists, no share count, no market cap —
P1/P4-gated), so the measure is an own-history substitute (21d vs prior-252d median log volume).
BAR FAILS AS WRITTEN and nothing is promoted: full-panel spreads carry the SAME sign at all
three horizons (-6.82/-4.90/-1.92, shrinking with horizon) so the registered SIGN-FLIP prior
MISSED, and the liquid tercile INVERTS to +4.05 (mean-based rebuild +4.77) — the bar required
|panel 12m| >= 4.00 AND sign agreement and gets neither. Watch-list reading only: the panel-wide
high-shock win is non-evidence-grade while the liquid-tercile quiet-state print is both
admissible and the only third of the panel the desk could trade. Redundancy did NOT fire (mean
per-date rank corr with 6-2 = +0.270) so volume shock is genuinely not momentum repackaged —
second instance this week of distinct-but-unusable (cf. G3). **THE BATTERY'S BIGGEST NUMBER IS
A COST-MODEL FLAG, not a result**: the unbuffered 6-2 sleeve churns **472.8%/yr one-way**, and
config/costs.yaml's own turnover_cost_curve prices that zone at 3.5-6.5%/yr all-in against the
1.32-2.71pp/yr the statutory-only charge used in these cells — so EVERY momentum print on this
desk (MOM-D1, G4, these cells) understates its own cost side by roughly 2-4x. No print is
restated; the flag is the correction, and it cuts in favour of churn reduction being worth MORE
than shown. METHODOLOGICAL NOTE WORTH KEEPING: the two bars that passed on the number split on
whether the artifact story could be INTERNALLY FALSIFIED — that test, not a p-value, did the
adjudicating. Construction Mechanics Atlas updated to v2, same URL (row 63 extended with §6).
Suite 125 green. Still principal-gated: the India fundamentals drop, OPEN_QUESTIONS batches 3+4
(incl. B4-4), funding_rate/ADV, the Priority-1 pulls, and every gap-map Tier-2 row.
