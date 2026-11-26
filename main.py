#!/usr/bin/env python3
"""Rejected Olympic Sports — make.fun entry.

Writes one funny single-line sport the Olympics rejected to
/output/entry.txt (1-200 chars, UTF-8, single line).

The line: a made-up event real enough to sound like a broadcast,
absurd enough to be funny, with the twist landing at the end in
one read — no second sentence needed.
"""

import os

LINE = (
    "Extreme hide-and-seek: the defending champion hasn't been found "
    "since 2016, so the closing ceremony is just everyone shouting "
    "his name."
)


def main() -> None:
    # Gate: 1-200 chars, UTF-8, not only whitespace, single line.
    # The scorer counts every character written, so no trailing
    # newline is added — the file holds exactly the line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip() == LINE and "\n" not in LINE
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
