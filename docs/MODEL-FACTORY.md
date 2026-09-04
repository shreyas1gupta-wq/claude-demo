# THE MODEL FACTORY — the desk's operating workflow for building investment models

**Status: OPERATING DOCUMENT (2026-09-03), written on principal request ("create a best
workflow of creating the best model for our investment"). It proposes no new architecture
and registers no trials: it is the assembly line the program already runs, written down as
ten stations with their machinery, entry/exit gates, and today's status. CONTRACT.md binds
everything here; PIPELINE.md (v2, proposed) is the architecture this line implements.
The premise, learned over 197 census cells: there is no "best model" to be found on a
leaderboard — the WORKFLOW is the edge, and models are its outputs. Most alpha dies at
stations 3-5; that is the factory working, not failing.**

---

## Station 0 — Charter (why anything gets built)
Objective, books, constraints, and the frozen rules live in `research/CONTRACT.md`:
multi-horizon cycle stack, NIFTY 750 + gold + debt, three books, free data only, Tier-C
reduce-only, no magic numbers, Hamilton-never-HP, states-never-dates.
**Gate:** nothing enters the line that violates a frozen constraint. **Status: FROZEN.**

## Station 1 — Idea intake (candidates, not trades)
Sources: the Atlas's 38 monographs, manager/frontier sweeps
(`research/frontier/manager-frontier-sweep.md`), Track T motifs, principal directives.
Every idea becomes a NAMED candidate (H-number) with: the mechanism, who is on the other
side, why it survives publication, the falsifiable prediction, and — written before any
data — what would count AGAINST it (the T6-TOM precedent: we registered the anti-H61
fingerprint and printed it against our own candidate).
**Gate:** candidate note committed; breaks-registry check (BR1-BR6 era-splits assigned).
**Status: OPEN** (H60-VRP, H61-FLOWMULT current; generation reopened 2026-09-03).

## Station 2 — Data admission (the vault)
Free primary source or declared mirror; two-pass `AUTHENTICATION.md` (anchors committed
BEFORE values are checked — near-miss #4); WORM manifest (`python3 ingest/manifest.py`);
survivorship and one-way-use declarations at admission, not at analysis; revisable series
get vintage stamping (`quant/pipeline/vintage.py`). Mirrors never outrank primaries;
blocked hosts become RUNSHEET rows with puller skeletons (`ingest/pull_*.py`).
**Gate:** no un-manifested number is ever cited. **Status: 10 vaults live; mirror frontier
EXHAUSTED — next admission is principal-machine (Priority-1: PIT bhavcopy, India VIX
primary, CCIL).**

## Station 3 — Pre-registration (the ledger)
`research/register/trial-ledger.md`, BEFORE any number is computed: definitions, sample,
era-splits, controls and placebos, bars, priors on record, one-way declarations, census
cell count. Partials QUOTE the parent design verbatim and state every deviation. Bars are
NEVER moved after a print — a wrong bar is a recorded miss (M0/A6).
**Gate:** the entry exists in the committed ledger before the script runs.
**Status: ~105 entries; census 197.**

## Station 4 — The run
House machinery only (`quant/stats/`, `quant/regime.py`, the walk-forward harness) — never
inline re-implementations (process note #6). Scripts committed exactly as run; post-print
code edits forbidden. RESULTS files are prints plus a hand-appended honest read written
AFTER (process note #7: reproduction = run-diff-restore). Census incremented; any Sharpe
claim goes through `quant.stats.dsr` with n_trials ≥ `census_n()` (machinery-enforced).
**Gate:** `.githooks/pre-commit` (pytest + validator) refuses red commits; CI re-runs both.
**Status: LIVE — suite 125 green.**

## Station 5 — Adjudication (most things die here)
Grade against the registered bars only: PASS / FAIL / MIXED / INCONCLUSIVE(one-way).
Controls are read FIRST (the T-CTRL pattern; a placebo breaching ±1σ voids the treated
read — EN-D1a's COVID catch). Graveyards are results and get booked with mechanisms.
Partials never promote: promotion needs the FULL design on primary data.
**Gate:** the verdict table in the ledger. **Status: standing doctrine set — RV-primary
3-for-3, levels-not-directions at both bands, overnight-calm accrual, exposure-drag, the
global factor owns unconditional commodity links.**

## Station 6 — Model assembly (states → sizes → books)
Passing states enter the Stage-1 assembler (`quant/regime.py`): levels sized by quantile
ranks with provenance (no magic numbers), combined per the frozen asset-mix policy (never
optimized), Tier-C reduce-only, drawdown governor binding. Adaptive rules live ONLY as
lanes in `config/challengers.yaml` (the validator refuses un-reviewed 'online' lanes).
Costs and whipsaw are first-class: book-cost machinery + the F6a false-fire ledger; the
T1b execution playbook (enter at close on calm days; stress de-risking may wait for the
next open) is part of the model, not an afterthought.
**Gate:** `config/validator.py` green; every parameter traceable to a print.
**Status: LIVE — Stage-1 emits a complete portfolio today.**

## Station 7 — Validation (trying to kill the assembled model)
Purged walk-forward (the M4 harness), DSR against the FULL census, era-splits across every
applicable BR break, cost/capacity honesty (the ADV table is a flagged placeholder), and
the reproducibility audit (all 50 scripts re-run, diffed, restored — the audit of record in
`research/register/REPRODUCIBILITY.md`, re-run annually).
**Gate:** a model that only works in one era, before costs, or under a moved bar does not
pass. **Status: LIVE.**

## Station 8 — Paper, then live (the slow gate)
The paper ledger runs the assembled stack with pre-declared grading windows (CW-PT1 grades
Apr-2027); challengers run in lanes against the champion with CI enforcement. Promotion to
live capital is a PRINCIPAL decision, batched through `research/OPEN_QUESTIONS.md` — the
factory recommends; it never self-promotes.
**Gate:** grading window completes + principal sign-off. **Status: paper LIVE; batches 3+4
pending principal.**

## Station 9 — Monitoring, decay, and preservation
The Health Board (THE ONE PAGE) is the live gauge wall; tau_half drift watches the
lengthening financial cycle; the annual loop (`ANNUAL-LOOP.md`, next Sep-2027) re-runs the
census, the audit, and the standing exhibits. Every published edge decays: retirement is a
scheduled outcome, not a surprise. Significant work ships as a Cycle School lesson (49 so
far) with corrections as dated update boxes — superseded claims stay visible.
**Gate:** nothing significant lives only in chat or a scratch file. **Status: LIVE.**

---

## The line today (2026-09-03)
Ideas (H60/H61 registered-ahead) → **blocked at Station 2** (principal-machine pulls) for
everything fast-band and cross-sectional; Stations 3-7 fully mechanized and idle-capable;
Station 8 waiting on OPEN_QUESTIONS batches 3+4. Track P has pre-built Station 4-6
machinery for the ML lane (triple-barrier, meta-labels, vintage) so that when the PIT
bhavcopy lands, Phase-0 exercises steel that already passed planted-truth tests. The
factory's next output is therefore determined by exactly two inputs it cannot make itself:
the Priority-1 pulls and the batch-3/4 decisions.
