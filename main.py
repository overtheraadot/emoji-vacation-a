"""Emoji Vacation A — One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt: the sunrise over the sea,
standing in for a whole slow morning on a beach with no alarms — wake
when the light does, nowhere to be, nothing to answer.

Deterministic: the entry is a fixed literal; no randomness, no time,
no network, no environment input. Running twice produces identical bytes.
"""

import os

ENTRY = "\U0001F305"  # 🌅 SUNRISE — one character, four UTF-8 bytes


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
