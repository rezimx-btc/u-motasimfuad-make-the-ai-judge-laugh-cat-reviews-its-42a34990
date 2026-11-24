#!/usr/bin/env python3
"""One-star review written by a house cat about its human.

make.fun entry for u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990.
Writes the single-line entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only.
"""

import os
import sys

ENTRY = "One star. You deleted the 3 a.m. feeding rule, so I screamed at your pillow until you restored it."


def main() -> int:
    # The brief demands one line, under 200 characters: enforce it here
    # so a bad edit can never ship a multi-line or over-long entry.
    assert "\n" not in ENTRY and len(ENTRY) < 200, "entry must be one line under 200 chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    path = os.path.join(out_dir, "entry.txt") if out_dir else "/output/entry.txt"
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
