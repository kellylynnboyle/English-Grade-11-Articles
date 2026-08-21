#!/usr/bin/env python3
"""Generate an AnswerThePublic-style "question wheel" for a topic using
Google's free autocomplete (suggest) API.

Usage:
    python3 tools/question_wheel.py "gaza investigation"
    python3 tools/question_wheel.py "wildfire california" --alphabet
    python3 tools/question_wheel.py "measles outbreak" -o wheel.md

No dependencies beyond the Python standard library. Be polite: the script
sleeps briefly between requests so Google doesn't rate-limit you.
"""

import argparse
import json
import string
import sys
import time
import urllib.parse
import urllib.request

SUGGEST_URL = "https://suggestqueries.google.com/complete/search?client=firefox&q={query}"

QUESTION_PREFIXES = [
    "who", "what", "when", "where", "why", "how",
    "which", "can", "will", "should", "is", "are", "does",
]
PREPOSITION_SUFFIXES = ["for", "with", "without", "near", "to", "versus"]
COMPARISON_SUFFIXES = ["vs", "or", "and", "like"]

HEADERS = {"User-Agent": "Mozilla/5.0 (question-wheel; classroom research tool)"}


def suggest(query, delay=0.4):
    """Return Google's autocomplete suggestions for a query string."""
    url = SUGGEST_URL.format(query=urllib.parse.quote_plus(query))
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8", errors="replace"))
        time.sleep(delay)
        return data[1] if len(data) > 1 else []
    except Exception as exc:  # network hiccups shouldn't kill the whole run
        print(f"  (skipped '{query}': {exc})", file=sys.stderr)
        return []


def build_wheel(topic, include_alphabet=False):
    wheel = {"Questions": {}, "Prepositions": {}, "Comparisons": {}}

    for prefix in QUESTION_PREFIXES:
        results = suggest(f"{prefix} {topic}")
        if results:
            wheel["Questions"][prefix] = results

    for suffix in PREPOSITION_SUFFIXES:
        results = suggest(f"{topic} {suffix}")
        if results:
            wheel["Prepositions"][suffix] = results

    for suffix in COMPARISON_SUFFIXES:
        results = suggest(f"{topic} {suffix}")
        if results:
            wheel["Comparisons"][suffix] = results

    if include_alphabet:
        wheel["A–Z"] = {}
        for letter in string.ascii_lowercase:
            results = suggest(f"{topic} {letter}")
            if results:
                wheel["A–Z"][letter] = results

    return wheel


def render_markdown(topic, wheel):
    lines = [f"# Question Wheel: {topic}", ""]
    for category, groups in wheel.items():
        if not groups:
            continue
        lines.append(f"## {category}")
        lines.append("")
        for key, suggestions in groups.items():
            lines.append(f"**{key}**")
            for s in suggestions:
                lines.append(f"- {s}")
            lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("topic", help="Topic to explore, e.g. 'gaza investigation'")
    parser.add_argument("--alphabet", action="store_true",
                        help="Also sweep a–z suffixes (26 extra requests)")
    parser.add_argument("-o", "--output", help="Write Markdown to this file")
    args = parser.parse_args()

    print(f"Building question wheel for: {args.topic} ...", file=sys.stderr)
    wheel = build_wheel(args.topic, include_alphabet=args.alphabet)
    md = render_markdown(args.topic, wheel)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(md + "\n")
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        print(md)


if __name__ == "__main__":
    main()
