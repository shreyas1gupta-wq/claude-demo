## §6 — THE AUDIT SCOREBOARD, AND THE VERIFICATION QUEUE

Three adversarial fact-checkers read the 22 dossiers with instructions to find what was wrong before
the desk published it. They returned **53 refutations and 71 downgrades**. Their verdicts were
binding on the four syntheses above, and §§1-4 have been written accordingly — but the refutations
stay listed here rather than being silently edited away, because a pack that hides its own first
draft cannot be audited by the next reader.

### 6.1 The audit's own limitation, stated first

**WebSearch hit its 200-call session ceiling before audits 2 and 3 ran their first query.** Three
files independently reproduced the exhaustion. So for clusters B, C and D2-D4, the two axes that
mattered most — *does this paper exist* and *does this endpoint exist* — **were not audited**. Those
auditors pivoted to the checks still available to them: internal arithmetic, cross-dossier
contradiction, direct reads of the vaulted JST workbook, and comparison against the desk's own
documents of record. That pivot turned out to be the most productive axis in the whole leg, but it
does not substitute for citation verification. **Treat every citation in §§2-4 as unverified.**
Cluster A's citations were audited and 16 refutations came back, which is the base rate you should
assume applies to the unaudited three-quarters.

### 6.2 The six corrections that change the design

1. **The circle rate may not censor the recorded price at all — and this is the most consequential
   finding of the leg.** The whole censored-regression core rests on `observed = max(true, c_it)`.
   Audit 2 (R9) refuted that as a *mechanical* identity using the pack's own mechanics: stamp duty
   is charged on the **higher of declared price or circle rate**, which constrains the **tax base**,
   not the **declared consideration**. Nothing mechanically stops a deed recording below the floor —
   duty is identical either way. What makes the floor bind is the income-tax deeming machinery
   (Sections 50C / 43CA / 56(2)(x)) with its 5-10-20% tolerance band, which is an *incentive*, not a
   censoring rule. **Consequence: the pile-up at the floor is a behavioural equilibrium, and plain
   Tobit assigns zero probability to any observation below `c` — misspecified before any
   distributional concern if such rows exist.** Day-one diagnostic, which the dossier never stated:
   **measure the share of declarations strictly below the local circle rate.** If that share is
   non-trivial, the correct model is the bunching/notch-with-plateau family (§4.2), not Tobit. This
   is a better model than the one the handoff prompt specified, and it is reachable with the same
   data. *(Note on provenance: the cluster-D synthesis was mis-wired to read audit 3 rather than
   audit 2, so it never saw this refutation. My scripting error, recorded rather than smoothed.)*
2. **The "20-35%" area-basis constant is arithmetically wrong and is retired.** A 70-80% carpet
   ratio implies **+25% to +43%** per square foot, and Mumbai loading is independently reported at
   **40-50%**. Carry an explicit loading factor **L** with **psf ratio = 1 + L**, L up to **0.50**
   for Mumbai. The old constant understated the worst case in the primary market by up to 15pp. It
   had propagated into five dossiers and into the handoff prompt, which is now corrected.
3. **The five-year mean-reversion overlay is dropped.** The literature's canonical crossover is
   momentum at ~1 year, reversion at ~5 (Glaeser & Nathanson 2017). The five-year limb is refuted by
   the best evidence the desk owns: IN-D1 prints **+9.65%/yr** real over the next five years after a
   ≥15%/yr window. First-party desk evidence outranks snippet-grade calibration. Size against the
   **~2x crash-odds lift off a 13.0% base** instead of forecasting a reversal.
4. **A fabricated co-author was caught.** "Mian, Sufi & Matvos" on *Credit Supply and Housing
   Speculation* — the third name does not belong, and the alphabetically impossible ordering is the
   tell. Also caught: two distinct Piazzesi-Schneider papers presented as alternate titles of one;
   Hsieh & Moretti's GDP figure given as ~2% when the published AEJ:Macro version says **3.7%** (the
   2015 working paper said 9.5%); Anenberg's venue wrong; a malformed URL. **This is the
   hallucination class the audit existed to catch, and it caught it in the one cluster it could
   check.**
5. **`[2-SOURCE]` was being awarded to one paper found at several hosting locations.** Bhupal Singh,
   Nagpal-Gandhi and Baum-Snow & Han were each tagged two-source on the strength of a preprint
   mirrored across CEPR, an author page and a repository. **One paper on three servers is one
   source.** Every India-specific magnitude in this pack traces back through that error, including
   the only causally identified Indian supply elasticity and the only Indian credit elasticities.
6. **A majority of model memories does not outvote a desk document.** Audit 1 instructed that the
   RBI HPI's 18-city / 2022-23 rebase be pulled from §00 because three dossiers and its own recall
   said 10 cities / 2010-11. Audit 3 refuted its sibling: the rebase is documented on desk with a
   release date (2025-10-10), a reference quarter (Q1:2025-26), eight named new cities and a
   pre-registered splice rule. §00 stands; the dossiers carry the error. **The evidence hierarchy
   held under pressure, which is the more important result than either number.**

### 6.3 The verification queue — what the next session must verify, ordered by design dependency

Nothing below is optional. Each row is load-bearing: a build decision changes if it resolves the
other way. Ordered so that a `no` answer kills the least work.

| # | Verify | Why it is load-bearing | If it fails |
|---|---|---|---|
| 1 | The share of registered declarations strictly **below** the local circle rate | Decides Tobit versus bunching (§6.2 #1) | The censoring core is replaced by a notch model |
| 2 | The **43CA/50C/56(2)(x) tolerance ladder** — the 5% → 10% → 20% sequence, its dates and the ~₹2cr primary-sale cap | It is the *free identifying variation* in the whole design: a statutory change in the tolerance band with a known date | No policy discontinuity to identify off |
| 3 | Whether **Honoré (1992)** extends to a genuinely period-varying threshold, or normalises it to a constant | The only route to ward fixed effects under censoring | Censored quantile regression becomes primary |
| 4 | Whether RBI computes **ward × floor-space-band strata** upstream of its published HPI | Reframes the project from invention to replication at finer grain, and sets the top acquisition ask (an RTI for existing strata) | The free validation target disappears |
| 5 | The Maharashtra IGR **free e-search year band**, and whether any bulk or aggregate export exists | Decides whether a locality panel is buildable at all | FM1 fires; fall back to RBI HPI grain |
| 6 | Which of the two **India yield families** is right — asking-over-asking ~5.2% national, or portal/broker 2.0-4.0% Mumbai | CN-D2 makes yield *the* placement instrument; the two families place India on opposite sides of the pre-crash mode | No placement is possible; the India verdict is unresolvable |
| 7 | The **cost wedge**, recomputed from registry-sourced state-specific rates | Every published distribution is shown net of it; two of five benchmark rungs are functions of it | The project's central bar is wrong |
| 8 | **ULPIN / Bhu-Aadhaar coverage** for the chosen cities | The parcel key both SPAR and repeat-sales need; survey, khasra, CTS and gat numbers do not compose | No panel identity; index method forced to stratified median |
| 9 | Whether **any leave-and-license rent aggregate** exists or is obtainable | The only India route to a *transaction-based* yield rather than an asking-based one | Row 6 stays unresolved permanently |
| 10 | Gujarat's **2023 jantri revision** — effective date and the actual multiple by zone | The cleanest dated notified-value experiment in India; currently two model memories agreeing, which is concurrence and not verification | Lose the natural experiment |
| 11 | **RERA QPR history** — whether past quarterly progress reports are retained or overwritten | Decides whether the supply pipeline is a point-in-time series or a single revised snapshot (the lookahead trap) | Supply features become unusable as features |
| 12 | The **SPAR denominator** convention — base-date assessed value or most recent | Two dossiers contradict each other; it changes the estimator | Re-derive before any index is built |
| 13 | Whether the **BIS India series** is the RBI HPI, and its exact city list and start | The only standing route to a *live India valuation percentile* — the gap SNAPSHOT-1 named as its single biggest | No valuation state variable for India |

Rows 1-3 gate the dependent variable, 4-5 gate whether a locality panel exists, 6-7 gate whether the
answer means anything economically. **Resolve 1, 5 and 7 before writing a line of model code.**

