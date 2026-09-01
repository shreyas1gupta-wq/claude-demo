# Cycle School — the learn-while-we-build track

Per the principal's directive (2026-09-01): every deep-dive ships with a full teaching companion
that starts from zero (what a regression IS, what a filter IS) and runs to the frontier findings,
with charts computed from our actual runs — never stock illustrations. Lessons are published as
private artifacts; this index is the registry.

| # | Lesson | Companion to | Artifact (live) | Archive (permanent) |
|---|---|---|---|---|
| 1 | The Credit Cycle, From Zero | docs/cycles/01-credit-cycle.md (L10) | https://claude.ai/code/artifact/9222bf65-9bc4-4474-ac6e-903e042f3e89 | docs/learn/artifacts/lesson-01-credit-cycle.html |
| 2 | Fast Stress, From Zero | docs/cycles/02-fast-stress.md (L2) | https://claude.ai/code/artifact/c0a03c8b-311e-4ac9-bf2f-988c1e32ea08 | docs/learn/artifacts/lesson-02-fast-stress.html |
| — | Cycle Stack Pipeline v2 (reference page) | docs/PIPELINE.md | https://claude.ai/code/artifact/88c0c9f6-cc82-441d-b0cf-0a7ffb4164db | docs/learn/artifacts/pipeline-v2.html |

Preservation rule (principal directive 2026-09-01): every lesson/teaching page is COMMITTED to
docs/learn/artifacts/ as a self-contained HTML file (open directly in any browser) so the material
survives independently of the artifact host and can later train other team members. The repo copy
is the archive of record; the artifact URL is the reading surface.

Format contract (applies to every lesson):
- Part 0-style epistemics woven in, not bolted on; each concept taught at the moment the build needs it.
- Every figure is either (a) computed from this repo's code on the synthetic fixtures, clearly
  badged SYNTHETIC + seed, or (b) a toy pedagogical dataset badged TOY DATA. No unbadged charts;
  no implied India results before the Phase-0 fixtures exist.
- Falsifications and process violations appear in the lesson itself (the confession box), mirroring
  research/register/verification-log.md — the reader learns from our mistakes in situ.
- Literature effect sizes only as verified in the dossiers; assumptions carry their [A] tags.
