#!/usr/bin/env python3
"""Assert every fact and phrase restored from the session note is on the page.

    python3 hni-prospecting/coverage.py

Guards against a rebuild quietly dropping content that was deliberately added
back. Each entry names the note section it comes from.
"""

import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "HNI_Prospecting_Dashboard.html")

# (note section, what it is, snippet that must appear in the rendered text)
REQUIRED = [
    ("§1", "millionaire count", "3.9"),
    ("§1", "aggregate wealth held", "$1.65 trillion"),
    ("§1", "HNI base", "8.5"),
    ("§1", "2027 projection", "1.65 million by 2027"),
    ("§1", "UHNI count", "19,900"),
    ("§1", "UHNI five-year growth", "up 63% in five years"),
    ("§1", "global rank", "6th globally"),
    ("§1", "new AUM in play", "FY24"),
    ("§1", "under-40 share", "1 in 5"),
    ("§1", "family offices", "family office"),
    ("§1", "geographic spread — Jaipur", "Jaipur"),
    ("§1", "geographic spread — Pune", "Pune"),
    ("§1", "geographic spread — Indore", "Indore"),
    ("§1", "source attribution", "Capgemini"),
    ("§1", "source attribution", "Deloitte"),
    ("§2", "prospecting time share", "7%"),
    ("§2", "referral share", "referral"),
    ("§3", "lever — product USP", "AI second opinion"),
    ("§3", "lever — Allocate", "Allocate"),
    ("§3", "why brand works", "already familiar"),
    ("§3", "why digital RM works", "speed-to-lead is a multiplier"),
    ("§3", "why follow-up works", "patient follow-up, not first contact"),
    ("§3", "why referrals work", "one satisfied promoter knows ten more"),
    ("§3", "why events work", "credibility first, product later"),
    ("§3", "cross-sell base", "top 0.1%"),
    ("§3", "the rule", "without a strong product proposition"),
    ("§3", "attribution", "Rohit"),
    ("§4", "persona 1", "First-generation founder"),
    ("§4", "persona 2", "GCC / MNC senior leader"),
    ("§4", "persona 3", "Senior doctor / professional"),
    ("§4", "persona 4", "Next-gen inheritor"),
    ("§4", "persona 5", "Corporate top &amp; middle management"),
    ("§4", "founder concern", "concentrated stake"),
    ("§4", "GCC concern", "two countries"),
    ("§4", "doctor way in", "Education-first"),
    ("§5", "the trial", "25 lakh"),
    ("§5", "two quarters", "two quarters"),
    ("§5", "script 1", "no strings, just a second set of eyes"),
    ("§5", "script 2", "single screen"),
    ("§5", "script 3", "last two corrections"),
    ("§5", "funnel line", "Prospecting fills the top of the funnel"),
    ("§6", "the one rule", "never sell a product in the first meeting"),
    ("§6", "sector homework", "a policy shift, a deal, a margin trend"),
    ("§6", "advisor not distributor", "advisor rather than a distributor"),
    ("§6", "reference value", "own sector or community"),
    ("§6", "low-friction entry", "sell list"),
    ("§6", "third meeting", "travel, sport, food"),
    ("§6", "discovery question", "what is it about this that worries you most"),
    ("§6", "check Q1", "one real thing moving in his sector"),
    ("§6", "check Q2", "warm reference"),
    ("§6", "check Q3", "and it isn't a sale"),
    ("§6", "check Q4", "name the one problem"),
    ("§6", "check verdict", "not ready"),
    ("§7", "trust equation", "credibility"),
    ("§7", "timing", "Timing beats targeting"),
    ("§7", "liquid assets", "Liquid, investable assets"),
    ("§7", "be present", "not six months after it"),
    ("§7", "centres of influence", "founder's first investor"),
    ("§8", "loss 1", "Pitching before you understand"),
    ("§8", "loss 2", "Walking in unprepared"),
    ("§8", "loss 3", "Talking more than you listen"),
    ("§8", "loss 4", "Chasing paper wealth"),
    ("§8", "loss 5", "Going quiet after you win"),
    ("week", "referral asks", "2"),
    ("week", "COI touches", "centre-of-influence"),
    ("week", "same-day callback", "same-day callback"),
    ("week", "the warning", "quietly, and then all at once"),
    ("pocket", "line 1", "The clients exist"),
    ("pocket", "line 2", "not the gap between clients"),
    ("pocket", "line 4", "Charm gets the meeting"),
    ("pocket", "line 5", "one small, winnable yes"),
    ("closing", "sign-off", "That's the whole game"),
]


def main():
    raw = open(PAGE).read()
    body = raw[raw.index("<body>"):]
    # strip tags so a phrase split across markup still matches
    text = html.unescape(re.sub(r"<[^>]+>", " ", body))
    # the KPI figures live in data-count / data-static attributes and only reach
    # the DOM after the count-up runs, so fold those values in as well
    counts = re.findall(r'data-static="([^"]+)"', body)
    for tag in re.findall(r"<div class=\"n\"[^>]*>", body):
        attr = dict(re.findall(r'data-([\w-]+)="([^"]*)"', tag))
        if "count" not in attr:
            continue
        value = float(attr["count"])
        dec = int(attr.get("dec", 0))
        shown = (f"{value:,.0f}" if attr.get("comma") == "1" else f"{value:.{dec}f}")
        # reproduce exactly what the count-up composes into the DOM
        counts.append(attr.get("pre", "") + shown + attr.get("suf", ""))
    text = re.sub(r"\s+", " ", text + " " + " ".join(counts))

    missing = []
    for section, what, snippet in REQUIRED:
        needle = html.unescape(snippet)
        if needle.lower() not in text.lower():
            missing.append((section, what, snippet))

    print(f"content coverage: {len(REQUIRED) - len(missing)}/{len(REQUIRED)} "
          f"facts and phrases from the session note present")
    if missing:
        print("\nMISSING:")
        for section, what, snippet in missing:
            print(f"  {section:8s} {what:28s} {snippet!r}")
        sys.exit(1)
    print("nothing restored from the note has been dropped.")


if __name__ == "__main__":
    main()
