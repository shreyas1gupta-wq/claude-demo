# IN PROGRAMME — India property, city by city and micro-market by micro-market
Opened 2026-09-11 by principal directive, immediately after the CN programme: "now do all this and
more work for india, also analyze mumbai 5-7places outer inner middle etc, do same for ahmedabad,
pune, hyderabd, amravati, ayodhya, lucknow, and also for 5 other tier 1/2/3 which u except can grow
more than 20% for next 5yr 2026-2032".

## 0. Two things settled BEFORE any research, because both change what the answer is

### 0a. THE BAR IS AMBIGUOUS AND THE TWO READINGS POINT OPPOSITE WAYS
"grow more than 20% for next 5yr" has two readings and they are not close:
- **20% CUMULATIVE over five years** = **3.71%/yr** nominal. Against a 4.5% CPI path that is
  **-0.75%/yr REAL** — a bar that *loses money in real terms* and loses badly to the desk's own
  standing book (11.46%/yr, 72.0% cumulative over five years). Naming a city that clears this is
  not an investment case.
- **20% CAGR for five years** = **148.8% cumulative**, beating the standing book by **8.54pp/yr**.
Both are computed and reported. The screen is built against the CAGR reading, because that is the
only one that would change a portfolio — but the cumulative reading is stated wherever a city's
plausible path sits between the two, since that is the honest place most of them land.

### 0b. THE DESK HAS NO INDIA PROPERTY DATA AT ALL
Checked, not assumed: `ingest/vault/` contains NO India property series and NO India CPI. The vault's
India content is NIFTY 50 daily, INR/USD, and the IIMA factor file. Therefore:
1. **Every India city and micro-market figure in this programme is snippet-sourced**, at the same
   lower standard as the CN programme's Half B (WebFetch is egress-blocked; WebSearch only;
   two-source corroboration required; per-figure `[2-SOURCE]`/`[1-SOURCE]`/`[RECALL]` tags).
2. **There is no India price base rate to compute.** The one desk-grade yardstick available is the
   CN programme's own JST panel (18 advanced economies, 1870-2020), and the honest use of it is as
   a base rate for what property *does*, never as an India forecast.
3. NHB RESIDEX, PropTiger/Anarock/Knight Frank/Liases Foras city series and registration-office
   data are the real sources and all need a principal-machine pull — RUNSHEET rows added.

## 1. What IS computable, and it prices the principal's question directly
IN-D1/IN-D2 (pre-registered before running): the JST panel can answer **how often property actually
compounds at 20%/yr, how long it lasts, and what follows** — which turns "which cities will grow
>20%" from an unanswerable forecast into a base-rate question the desk can settle. First-pass
placement, before the run: the panel's modern-era median *pre-crash* appreciation was **6.21%/yr
real** with p75 at **9.28%/yr**. A sustained 20%/yr nominal call therefore sits at or above the boom
velocity of every modern episode in the panel — and CN-D4 established that a bigger boom buys a
**faster unwind**, not a deeper one. So the principal's own bar, read as CAGR, is a request to
identify bubble-velocity markets; the programme will say so and then still name them, with the
mechanism and the unwind risk attached to each.

## 2. Structure
### HALF A — desk-grade (pre-registered, vaulted)
IN-D1 the real-appreciation-threshold battery; IN-D2 its nominal twin (because Indian property talk
is nominal and the gap between the two is the whole point).

### HALF B — the city work (agent research, snippet-sourced, on disk in `research/notes/india-dossiers/`)
- **Mumbai / MMR, 7 micro-markets across the inner-middle-outer gradient** (two agents): the island
  city (South Mumbai, Worli-Prabhadevi), inner suburbs (Bandra-Khar-Santacruz, Powai-Chembur),
  outer suburbs (Andheri-Goregaon-Borivali, Mulund-Ghatkopar), and the MMR satellites (Thane,
  Navi Mumbai, Panvel-Karjat).
- **One agent each**: Ahmedabad, Pune, Hyderabad, Lucknow.
- **The two policy-created cases, deliberately separated**: **Amravati** (Andhra Pradesh's new
  capital, shelved 2019-2024 and revived) and **Ayodhya** (temple-driven since Jan 2024). The CN
  programme's provincial-capital finding binds directly here: administrative privilege bought
  roughly double the appreciation through China's boom and **zero protection** in its bust, so these
  two are graded as policy-conferred and fragile by construction, not as growth stories.
- **The five candidate cities**: screened on OBSERVABLE preconditions rather than picked from
  memory, then ranked, with each candidate classed by WHAT is supposed to drive it —
  **infrastructure-backed** (the asset exists afterwards: an airport, a metro, an expressway),
  **policy-backed** (a designation that can be withdrawn — the fragile class per China), or
  **demand-backed** (jobs and household formation). That taxonomy is the analytical spine.
- **Cross-cutting**: India rental yields and REITs by city (closes SNAPSHOT-1's admitted REIT gap
  further), unlisted tier-2/3 developer leverage (the ONE India vulnerability the CN programme
  found genuinely unknown), and the infrastructure pipeline that is the actual causal driver.

## 3. Discipline
Unchanged. Pre-register before running; bars never moved; both commit gates; 3 concurrent agents
(rule 6); every non-computed claim tagged; nothing promoted to a rule on snippet evidence; the
dashboard states its own evidence standard on its face.
