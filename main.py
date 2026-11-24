"""Emoji Vacation A — One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt: the sunrise over the sea,
standing in for a whole slow morning on a beach with no alarms — wake
when the light does, nowhere to be, nothing to answer.

Deterministic: the entry is a fixed literal; no randomness, no time,
no network, no environment input. Running twice produces identical bytes.
"""

import os

# The entry: a single sunrise-over-the-sea emoji (U+1F305).
# One Python character, four UTF-8 bytes, no trailing newline.
EMOJI = "\U0001F305"  # 🌅 SUNRISE

# Sealed entry gate for this competition: 1-8 characters.
MIN_CHARS = 1
MAX_CHARS = 8

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate_entry(text: str) -> None:
    """Check the entry fits the sealed gate before anything is written."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if len(text) != 1:
        raise ValueError(f"entry must be exactly one emoji, got {len(text)} chars")
    if len(text.encode("utf-8")) != 4:
        raise ValueError("entry must encode to exactly 4 UTF-8 bytes")


def write_entry() -> str:
    """Validate, then write the emoji to /output/entry.txt (no newline)."""
    validate_entry(EMOJI)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    return EMOJI


def verify_written(expected: str) -> None:
    """Read the file back and confirm it matches the constant exactly."""
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        actual = f.read()
    if actual != expected:
        raise ValueError(f"read-back mismatch: wrote {expected!r}, read {actual!r}")


def main() -> None:
    expected = write_entry()
    verify_written(expected)


if __name__ == "__main__":
    main()
