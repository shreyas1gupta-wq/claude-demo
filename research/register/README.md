# Research register

Per CONTRACT §10, every parameter carries provenance: **value, source, evidence tier, confidence,
decay assumption, and what would change it**. The register is not a separate table that can drift
out of sync — provenance lives **inline on every parameter node in `config/*.yaml`** and is
enforced mechanically by `config/validator.py` (a parameter without provenance fails CI; a
registry violating its own budgets refuses to load).

## Layout
- `config/mandate.yaml` — frozen caps + conventions + the DD-violation test (ε, K).
- `config/books.yaml` — the three books, dual universes, turnover budgets, honest targets.
- `config/ladder.yaml` — the cycle ladder (16 entries), block budgets, exclusions.
- `config/risk.yaml` — regime buckets, leverage function, hedge stack, tactical shorts, re-entry.
- `config/sleeves.yaml` — momentum/factor/tail/special-sits sleeves, gold function, policy
  portfolio, Stage-2 charter, Stage-3 construction.
- `config/costs.yaml` — statutory stack (verified FY2026-27), impact model, capacity bounds.

## Evidence audit trail
- `research/dossiers/01–12` — the literature base (~90k words, citation-by-citation, with
  verification status per claim).
- `research/CONTRACT.md` — the frozen mandate. `research/OPEN_QUESTIONS.md` — decisions record.
- `docs/DESIGN.md` — the integrative design; §15 is the consolidated verification queue.

## Verification ledger
The 12-workstream sweep exhausted its shared web-search budget mid-run; dossiers 05–12 carry
`[VERIFY]` tags on citations recalled rather than freshly confirmed (each dossier's §7 lists its
own, with priority order; DESIGN §15 consolidates the top items). **Rule (enforced by convention
and CI where expressible): nothing tagged `[VERIFY]` or `PROVISIONAL` may be promoted past
Tier C into a frozen registry value.** The adversarial verification pass updates
`research/register/verification-log.md` as items are confirmed or corrected.

## Trial ledger
CONTRACT §9's deflated-Sharpe discipline requires one **cumulative program-wide trial count**.
It starts now, at design time: the sweeps this design already commits to (7-point hedge grid ×
4 regime buckets ≈ 28; z×K DD-test grid = 9; τ_ref, f_Kelly, cushion-p, participation-cap, GZ-α,
Hamilton-h grids) must be logged in `research/register/trial-ledger.md` before any is run.
