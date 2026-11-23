#!/usr/bin/env python3
"""One-Line Laugh Sprint - make.fun entry.

Writes one original funny line (at most 200 characters) on everyday life
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), the one text
the house judge compares two at a time. Python 3.13, standard library
only, no network, reads nothing from outside the repository.

Run it locally:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
    cat out/entry.txt
"""

import os
import sys
from pathlib import Path

ENTRY = "I meal-prepped on Sunday like a responsible adult, then ordered takeaway on Monday like the adult I actually am."
# The joke: Sunday-me performs responsibility, Monday-me confesses the
# truth - the twist lands on the last words, "the adult I actually am".


def main() -> int:
    # Guard: the entry must be non-blank, a single line, and 1-200
    # characters (the bounty caps the line at 200). Fail loudly
    # instead of writing a bad entry - a bad file would score 0.
    if not ENTRY.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    if "\n" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(ENTRY) > 200:
        print(
            f"entry is {len(ENTRY)} characters, over the 200-character limit",
            file=sys.stderr,
        )
        return 1
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} characters to {out / 'entry.txt'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
