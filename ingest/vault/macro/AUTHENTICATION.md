# Macro vault — authentication protocol (2026-09-02)

File: pwt100.csv — Penn World Table 10.0 (via the OWID mirror; PWT is the Feenstra-Inklaar-
Timmer dataset, U. Groningen). The entry of interest: labsh ("Share of labour compensation in
GDP"), whose complement 1−labsh is the desk's macro capital/profit-share proxy (a broader
object than corporate profits/GDP — stated wherever used).

## Pre-stated bars (written BEFORE the checks ran; two-pass rule)

| # | Check | Bar | Result |
|---|---|---|---|
| PA1a | US labsh 2019 in [0.56, 0.63] (the known post-2000 decline territory) | yes | 0.597 (file stores percent: 59.709) — **PASS**, units note recorded |
| PA1b | US labsh 2019 BELOW its 1970s mean (the declining-labor-share stylized fact) | yes | 0.597 < 0.632 — **PASS** |
| PA1c | India labsh series: ≥40 observations, all within the plausible [0.35, 0.75] | both | n=70 PASS; range 0.481–0.754 — max **MISSES the 0.75 cap by 0.004** (early-era India values). Bar NOT moved (M0 precedent): miss recorded; file accepted on PA1a/b + n; early-era India labsh flagged as lower-quality (PWT's own India NA-content caveats [VERIFY]) |

Verdict: AUTHENTICATED with the PA1c marginal miss recorded. The capital-share proxy
(1−labsh) is a MACRO share, broader than corporate profits/GDP — every use states this.
