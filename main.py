#!/usr/bin/env python3
"""Micro-confession entry: an unsent message, written exactly as typed.

Writes the confession to <output dir>/entry.txt as exactly one text
with no trailing newline.
"""

import os

CONFESSION = (
    "To: Raka\n"
    "I still keep the last voice note you sent in 2023. It's 11 seconds "
    "of you laughing at your own joke, and I play it on bad days. "
    "I never told you I kept it."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()
