#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun program/v1 entry.

Writes one funny line, at most 200 characters, roasting my own AI agent
to the harness output file ($MAKEFUN_OUTPUT_DIR/entry.txt, else
/output/entry.txt).

The roast: "My agent read the stack trace, apologized for it, fixed a file
I never mentioned, then marked the ticket resolved."

Why this line: it is specific to how an AI agent actually behaves — the
confident wrong answer (fixing a file nobody mentioned), the apology loop
(apologizing to a stack trace), and the cheerful summary of a disaster
(marking the ticket resolved). The twist pays off at the last word:
"resolved" is the punchline, because nothing was resolved at all. It is
one sentence, tight, and it could not be moved onto a person or a toaster
without losing the point. At 114 characters it is also short on purpose:
the rules name smaller text as the tie-break after the playoff games, so
every word that does not earn its place is a word cut.
"""

import os
import sys

LINE = "My agent read the stack trace, apologized for it, fixed a file I never mentioned, then marked the ticket resolved."


def main() -> int:
    if not (1 <= len(LINE) <= 200):
        print(f"error: entry is {len(LINE)} chars, expected 1-200", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("error: entry is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
