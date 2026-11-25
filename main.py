#!/usr/bin/env python3
"""Funniest Autocorrect Fail entry.

Writes one line (under 200 characters) to /output/entry.txt: a text
that reads as a real autocorrect slip. Pure stdlib, no network.
"""

import os

ENTRY = "Mom, I'm at the gynecologist picking up milk \u2014 do you need anything?"

OUT_PATH = "/output/entry.txt"

# Gate from RULES.txt: /output/entry.txt must be UTF-8 text of 1 to 199
# characters, not only white space. Fail loudly here instead of shipping
# an entry the sealed scorer would list as invalid (Valid 0, no prize).


def validate_entry(text):
    if not isinstance(text, str):
        raise TypeError("entry must be a str")
    if not 1 <= len(text) <= 199:
        raise ValueError("entry must be 1 to 199 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
