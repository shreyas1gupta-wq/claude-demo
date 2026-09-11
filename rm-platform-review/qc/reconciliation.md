# RM Platform Review — Aug-31 2026 reconciliation

Source: `HNI_Team_Intelligence_31Aug2026_MIS_FINAL_v7_FIXED.xlsx`  
Built: 2026-09-11  
Result: **379/379 checks pass**

- **cross-check** — 104/104 pass
- **random-check** — 20/20 pass
- **calc-check** — 255/255 pass

## Cross-check — firm tie-outs

| Measure | Built from 73 RM rows | Raw source | Where the raw figure comes from | Tie |
|---|---:|---:|---|---|
| Total book (Cr) | 3,825.2249 | 3,825.2247 | SUM of aum!Z (total_current_value_crores), all 8,669 rows | within 0.01Cr |
| Platform core-4 (Cr) | 528.46 | 528.46 | SUM of platform!L where platform!U (core_flag) = 1 | exact |
| Clients (accounts) | 2,338 | 2,338 | COUNT of aum rows where user_type starts 'client' | exact |
| Platform clients | 523 | 523 | DISTINCT client_user_id on platform where core_flag = 1 | exact |
| Clients >= 50L | 1,335 | 1,335 | COUNT of client rows outside the 0-10L / 10-50L buckets | exact |
| Clients < 50L | 1,003 | 1,003 | COUNT of client rows in the 0-10L / 10-50L buckets | exact |
| Platform Mar-31 (Cr) | 260.79 | 260.79 | MoM Trend C16; also SUM of Platform Charts col F | exact |
| Platform Jun-30 (Cr) | 388.61 | 388.61 | MoM Trend C19; also SUM of Platform Charts col G | exact |
| Product mix sums to platform | 528.46 | 528.46 | SUM of platform!L by product_name where core_flag = 1 | exact |
| RM count | 73 | 73 | Platform Charts (RM) rows 5:77 | exact |
| Focus (Cr) | 7.05 | 7.05 | H1 & Quarter Progress section C, FIRM row | exact |

## Desk roll-up

| # | Desk | RMs | AUM | Clients | Plat Mar | Plat Jun | Plat Aug | Plat cl | Pen. | Focus |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Vishal Khanna | 7 | 822.11 | 331 | 110.85 | 155.87 | 185.26 | 121 | 22.53% | 0.79 |
| 2 | Nayanish Prabhu | 9 | 291.12 | 244 | 26.50 | 42.70 | 65.30 | 87 | 22.43% | 0.20 |
| 3 | Vijay Krishna Chinni | 5 | 312.27 | 203 | 41.53 | 51.84 | 61.59 | 69 | 19.72% | 0.55 |
| 4 | Madhup Patet | 12 | 392.06 | 401 | 7.03 | 22.16 | 41.68 | 66 | 10.63% | 1.77 |
| 5 | Dhiren Shah | 7 | 377.62 | 159 | 16.04 | 28.43 | 37.04 | 41 | 9.81% | 0.83 |
| 6 | Ajay Bhute | 5 | 397.03 | 239 | 10.11 | 15.25 | 32.82 | 28 | 8.27% | 1.56 |
| 7 | Srinivasa Prasanna | 4 | 139.41 | 109 | 14.98 | 17.18 | 26.28 | 11 | 18.85% | 0.05 |
| 8 | Abhishek kumar | 7 | 429.82 | 162 | 11.88 | 16.38 | 23.83 | 23 | 5.54% | 0.10 |
| 9 | Abhishek Sharma | 6 | 249.73 | 217 | 15.62 | 20.04 | 23.22 | 31 | 9.30% | 0.50 |
| 10 | Arnab Bhattacharjee | 4 | 125.69 | 69 | 3.14 | 10.81 | 15.41 | 18 | 12.26% | 0.10 |
| 11 | Ajay Sehgal | 3 | 75.85 | 94 | 2.47 | 5.90 | 8.44 | 15 | 11.13% | 0.10 |
| 12 | Harsh Bagai | 2 | 211.77 | 106 | 0.64 | 2.05 | 7.59 | 13 | 3.58% | 0.50 |
| 13 | Rohit Onkar | 1 | 0.45 | 3 | 0.00 | 0.00 | 0.00 | 0 | 0.00% | 0.00 |
| 14 | Vishal Rakyan | 1 | 0.30 | 1 | 0.00 | 0.00 | 0.00 | 0 | 0.00% | 0.00 |
| | **FIRM** | **73** | **3,825.22** | **2,338** | **260.79** | **388.61** | **528.46** | **523** | **13.82%** | **7.05** |

## Random check — 20 RMs re-derived from raw rows

Seeded sample (seed 20260831). Each RM's AUM, client count, 50L split, platform total and all four product values plus product client counts were recomputed by filtering the raw `aum` and `platform` rows one at a time.

| RM | Desk | AUM | Clients | Platform | Plat cl | >=50L | <50L | Re-derived |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Dattathreya Ganesh | Madhup Patet | 50.63 | 29 | 1.68 | 3 | 14 | 15 | match |
| Devyani Dhuri | Rohit Onkar | 0.45 | 3 | 0.00 | 0 | 0 | 3 | match |
| Gowtham | Srinivasa Prasanna | 46.67 | 15 | 21.13 | 4 | 4 | 11 | match |
| Ishan Mishra | Vishal Khanna | 144.37 | 32 | 43.54 | 14 | 23 | 9 | match |
| Jay Patel | Ajay Bhute | 83.75 | 11 | 4.60 | 3 | 8 | 3 | match |
| Jyoti Puvvala | Madhup Patet | 27.33 | 46 | 3.06 | 8 | 23 | 23 | match |
| Komal Bajaj | Abhishek Sharma | 2.47 | 2 | 0.00 | 0 | 2 | 0 | match |
| Mayank Shrivastava | Vishal Khanna | 30.56 | 35 | 3.53 | 6 | 22 | 13 | match |
| Parth Shah | Ajay Bhute | 240.10 | 152 | 24.73 | 21 | 84 | 68 | match |
| Prateek Chhabra | Vishal Khanna | 117.33 | 49 | 15.54 | 15 | 37 | 12 | match |
| Rohan Basak | Ajay Bhute | 1.77 | 11 | 0.75 | 2 | 1 | 10 | match |
| Rohan Rege | Dhiren Shah | 116.65 | 19 | 1.86 | 4 | 7 | 12 | match |
| Saurabh Gupta | Abhishek Sharma | 58.51 | 89 | 10.35 | 11 | 27 | 62 | match |
| Saurabh Pandey | Vishal Khanna | 218.14 | 57 | 26.01 | 11 | 47 | 10 | match |
| Shweta Runwal | Dhiren Shah | 9.32 | 5 | 0.00 | 0 | 5 | 0 | match |
| Somnath Balani | Nayanish Prabhu | 23.53 | 19 | 9.85 | 9 | 12 | 7 | match |
| Sumeet Talesra | Ajay Bhute | 26.67 | 13 | 0.00 | 0 | 2 | 11 | match |
| Sumit Sethi | Vijay Krishna Chinni | 67.70 | 80 | 11.60 | 19 | 31 | 49 | match |
| Swaminathan Gopalan | Srinivasa Prasanna | 10.74 | 9 | 1.00 | 1 | 5 | 4 | match |
| Tatavarthylakshmi | Madhup Patet | 46.44 | 49 | 5.01 | 8 | 24 | 25 | match |

## Calc check

255 recomputations of the figures the page renders — penetration, client penetration, product shares, mix shares, Mar→Aug and Jun→Aug deltas, and each desk's Jun product base plus its delta against its Aug platform total. 255/255 pass.

- `flagOf` 'Slipping vs Jun' fires on 0 RM(s): none
- no card renders NaN, a negative AUM, or platform clients above total clients

## Movement vs the previous dashboard

| Measure | Prior (FINAL_1_1) | Aug-31 MIS | Change |
|---|---:|---:|---:|
| Total book (Cr) | 3,773.60 | 3,825.22 | +51.62 |
| Platform core-4 (Cr) | 497.67 | 528.46 | +30.79 |
| Penetration | 13.19% | 13.82% | +0.63pt |
| Clients (accounts) | 2,290 | 2,338 | +48 |
| Platform clients | 478 | 523 | +45 |
| Platform clients with live value | 458 | 498 | +40 |
| Focus (Cr) | 6.90 | 7.05 | +0.15 |
| Platform Mar-31 (Cr) | 251.09 | 260.79 | +9.70 |
| Platform Jun-30 (Cr) | 379.29 | 388.61 | +9.32 |
| RMs | 72 | 73 | +1 |
| Desks | 13 | 14 | +1 |

## Source blocks deliberately not used

**1. Team Summary · NEW-A cols H:I (Aug-31 AUM / Clients, rows 19:31)**  
Would have injected: firm AUM 3,509.09Cr and 2,135 clients  
Actual: 3,825.22Cr and 2,338 clients  
Used instead: sum the per-RM rows from 'Calculation SHeet' B/C  

**2. Team Summary · row 49 (NEW-B 'Team Summary TOTAL')**  
Would have injected: platform 422.40Cr  
Actual: 528.46Cr (its own 13 ML rows above it sum to this)  
Used instead: sum NEW-B ML rows 36:48, never the TOTAL row  

**3. Platform Charts (RM) · K24:L27 ('Firm platform by product')**  
Would have injected: Allocate 360.97 / Co-Pilot 31.03 / Navigate 76.32 / YE 55.82 = 524.14Cr  
Actual: Allocate 364.75 / Co-Pilot 30.95 / Navigate 76.36 / HYE 56.40 = 528.46Cr  
Used instead: aggregate the raw 'platform' sheet by product where core_flag=1  

**4. Platform Charts (RM) · col I rows 6:77 ('Platform %')**  
Would have injected: values that are currently correct but are typed constants  
Actual: only I5 carries the =H/C formula, despite Validation item 25 claiming rows 5:77 are all live  
Used instead: recompute platform % from p_aug / tot_aug in this build  

**5. Platform Charts (RM) · col C ('AUM Cr')**  
Would have injected: firm AUM 3,825.60Cr (rounded to 1dp per RM)  
Actual: 3,825.2247Cr  
Used instead: use 'Calculation SHeet' col B, which ties exactly  

**6. team sheets · Section J ('Forensic Business Intelligence')**  
Would have injected: a Jul-15 cutoff — 'Days elapsed: 15', VK 'Current (Aug-31): 744.07Cr'  
Actual: VK Aug-31 book is 822.11Cr; Q2 elapsed at Aug-31 is 62 days  
Used instead: not used anywhere in the dashboard  

**7. READ ME — Aug update · row 6 (household count only)**  
Would have injected: 1,765 households  
Actual: 1,748 (count of aum.hh_primary=1)  
Used instead: count hh_primary=1 in raw 'aum'  
Note: the same row's '819 clients >=1Cr' is NOT an error -- it is the account basis; Team Summary's 743 is the household basis (hh_aum >= 1Cr). Both are correct on their own basis and the dashboard labels which one it shows.  
