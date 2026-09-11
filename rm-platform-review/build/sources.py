"""Which sheet and column each dashboard figure comes from, and why.

Split out from the build so the provenance decisions are reviewable on their
own.  Every entry in STALE_BLOCKS was verified against an independent
recomputation from the raw `aum` / `platform` rows before being excluded.
"""

# ---------------------------------------------------------------------------
# Blocks in the workbook that look authoritative but are stale typed
# constants.  The build refuses to read these; each records the wrong figure
# it would have injected so the exclusion can be re-checked next cycle.
# ---------------------------------------------------------------------------
STALE_BLOCKS = [
    {
        "block": "Team Summary · NEW-A cols H:I (Aug-31 AUM / Clients, rows 19:31)",
        "would_inject": "firm AUM 3,509.09Cr and 2,135 clients",
        "truth": "3,825.22Cr and 2,338 clients",
        "instead": "sum the per-RM rows from 'Calculation SHeet' B/C",
    },
    {
        "block": "Team Summary · row 49 (NEW-B 'Team Summary TOTAL')",
        "would_inject": "platform 422.40Cr",
        "truth": "528.46Cr (its own 13 ML rows above it sum to this)",
        "instead": "sum NEW-B ML rows 36:48, never the TOTAL row",
    },
    {
        "block": "Platform Charts (RM) · K24:L27 ('Firm platform by product')",
        "would_inject": "Allocate 360.97 / Co-Pilot 31.03 / Navigate 76.32 / YE 55.82 = 524.14Cr",
        "truth": "Allocate 364.75 / Co-Pilot 30.95 / Navigate 76.36 / HYE 56.40 = 528.46Cr",
        "instead": "aggregate the raw 'platform' sheet by product where core_flag=1",
    },
    {
        "block": "Platform Charts (RM) · col I rows 6:77 ('Platform %')",
        "would_inject": "values that are currently correct but are typed constants",
        "truth": "only I5 carries the =H/C formula, despite Validation item 25 "
                 "claiming rows 5:77 are all live",
        "instead": "recompute platform % from p_aug / tot_aug in this build",
    },
    {
        "block": "Platform Charts (RM) · col C ('AUM Cr')",
        "would_inject": "firm AUM 3,825.60Cr (rounded to 1dp per RM)",
        "truth": "3,825.2247Cr",
        "instead": "use 'Calculation SHeet' col B, which ties exactly",
    },
    {
        "block": "team sheets · Section J ('Forensic Business Intelligence')",
        "would_inject": "a Jul-15 cutoff — 'Days elapsed: 15', VK 'Current (Aug-31): 744.07Cr'",
        "truth": "VK Aug-31 book is 822.11Cr; Q2 elapsed at Aug-31 is 62 days",
        "instead": "not used anywhere in the dashboard",
    },
    {
        "block": "READ ME — Aug update · row 6 (household count only)",
        "would_inject": "1,765 households",
        "truth": "1,748 (count of aum.hh_primary=1)",
        "instead": "count hh_primary=1 in raw 'aum'",
        "note": "the same row's '819 clients >=1Cr' is NOT an error -- it is the "
                "account basis; Team Summary's 743 is the household basis "
                "(hh_aum >= 1Cr). Both are correct on their own basis and the "
                "dashboard labels which one it shows.",
    },
]

# ---------------------------------------------------------------------------
# Market-leader attribution.  'rm signals' col A is authoritative: it agrees
# with the prior dashboard on all 69 shared RMs with zero mismatches.  Five
# RMs have no 'rm signals' row; each is resolved from a named second source,
# never guessed.
# ---------------------------------------------------------------------------
MANUAL_ML = {
    "Anand Kumar":    ("Madhup Patet",        "prior dashboard + Platform Charts col B"),
    "Madhuri Rathod": ("Vishal Rakyan",       "Platform Charts col B (sole RM on that desk)"),
    "Sunny Shahi":    ("Arnab Bhattacharjee", "Platform Charts col B (only ML in that group)"),
    "Shweta Runwal":  ("Dhiren Shah",         "Platform Charts col B (DS is the primary ML)"),
    "Devyani Dhuri":  ("Rohit Onkar",         "Platform Charts col B (new desk this cycle)"),
}

# 13 market-leader desks -> the 8 structurally distinct teams the workbook
# reports focus and Q2 targets against.  Hardcoded rather than read from
# 'rm signals'.parent_ml, which keeps Ajay Bhute and Nayanish Prabhu apart
# (9 groups) where the focus sheet combines them (8 groups).
DESK_TO_TEAM8 = {
    "Vishal Khanna":        "Vishal Khanna",
    "Ajay Bhute":           "Ajay Bhute",
    "Nayanish Prabhu":      "Ajay Bhute",
    "Madhup Patet":         "Madhup Patet",
    "Srinivasa Prasanna":   "Madhup Patet",
    "Vijay Krishna Chinni": "Vijay Chinni",
    "Dhiren Shah":          "Dhiren Shah",
    "Ajay Sehgal":          "Dhiren Shah",
    "Abhishek Sharma":      "Abhishek Sharma",
    "Harsh Bagai":          "Abhishek Sharma",
    "Abhishek kumar":       "Abhishek Kumar",
    "Arnab Bhattacharjee":  "Arnab Bhattacharjee",
}

# Which 13-ML desk carries a team-level focus residual that cannot be pinned
# to an RM (the primary ML of each 8-team group).
TEAM8_PRIMARY_DESK = {
    "Vishal Khanna": "Vishal Khanna",
    "Ajay Bhute": "Ajay Bhute",
    "Madhup Patet": "Madhup Patet",
    "Vijay Chinni": "Vijay Krishna Chinni",
    "Dhiren Shah": "Dhiren Shah",
    "Abhishek Sharma": "Abhishek Sharma",
    "Abhishek Kumar": "Abhishek kumar",
    "Arnab Bhattacharjee": "Arnab Bhattacharjee",
}

# platform sheet product_name -> the short label the dashboard renders (and
# keys its mix colours on).  Only these four carry core_flag=1; SHARPE ONE and
# PIPE are core_flag=0 and sit outside the 528.46Cr core-4 basis.
PRODUCTS = [
    ("ALLOCATE", "Allocate"),
    ("HIGH YIELD ENHANCER", "YE"),
    ("NAVIGATE", "Navigate"),
    ("CO-PILOT", "Co-Pilot"),
]

# The 8 team sheets carrying per-RM sections.  'NP Team' is deliberately
# excluded: its 9-RM roster is a strict subset of 'AB+NP Team' (Validation
# item 10), so including it would double-count Nayanish Prabhu's desk.
TEAM_SHEETS = [
    "VK Team", "AK Team", "AS+HB Team", "AB+NP Team",
    "DS+AS Team", "VKC Team", "MP+SP Team", "Arnab Team",
]

# AUM buckets in raw `aum` col AB that sit below the >=50L line.  Note the
# stray space in '10-50 L AUM' — matching without it silently moves 626
# clients across the threshold.
SUB_50L_BUCKETS = {"0-10L AUM", "10-50 L AUM"}

# Buckets at or above 1Cr, for the >=1Cr client count.
GE_1CR_BUCKETS = {"100-250L AUM", "250-500L AUM", "500-1000L AUM", "1000 L+ AUM"}
