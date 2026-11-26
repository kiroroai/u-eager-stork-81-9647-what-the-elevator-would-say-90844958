#!/usr/bin/env python3
"""What the Elevator Would Say — program/v1 entry.

Writes a single line (<=120 chars) to /output/entry.txt: the funniest
thing a talking elevator would say, in the elevator's own voice.
Deterministic: fixed text, no randomness, no clock, no network.
"""

import os

LINE = "Ding! Floor 12. Relax — I never saw you leave at 3 a.m. with someone else's pizza."

MAX_CHARS = 120


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, must be 1-120"
    assert LINE.strip() == LINE and "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
