#!/usr/bin/env python3
"""Make the AI Judge Laugh — one original line about office life.

Writes a single joke (one line, under 200 characters) to /output/entry.txt.
Deterministic: stdlib only, no network, no randomness, no input.
"""

import os

JOKE = (
    "The office has a 'no meeting' day, "
    "so we booked a meeting to celebrate it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
