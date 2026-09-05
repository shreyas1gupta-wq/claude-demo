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
