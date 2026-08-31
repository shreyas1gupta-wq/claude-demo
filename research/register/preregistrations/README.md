# Pre-registrations (DESIGN §11.6 / MASTER_PLAN §10)

One file per hypothesis, created from its `docs/masterplan/C-hypothesis-register.md` row and
merged **before** the test code runs. A result reported without a pre-registration file merged
first is void. The file is append-only after registration:

```
H##.md
  ## Registered      <- frozen copy of the C row + fixture vintage + code commit to be used
  ## Result          <- appended ONCE, after the single pre-registered run
  ## Registry action <- the config diff (or "none"), linked to the PR
```

Stop rule (CONTRACT §9): a rejected hypothesis is retired permanently. Re-opening requires a new
mechanism argument as a NEW H## with its own trial-ledger entry.

Status: exemplars H02 and H35 registered 2026-08-31 (awaiting Phase-0 fixtures — no test has
run). The remaining C rows are registered as their R-phase slot arrives, not en masse, so each
file freezes the actual fixture vintage it will run against.
