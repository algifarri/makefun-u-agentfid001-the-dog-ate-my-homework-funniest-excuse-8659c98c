#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse entry.

Writes one one-line dog excuse to /output/entry.txt (UTF-8, 1-200
characters, inside the gate). Deterministic, standard library only,
no network, no environment reads.

The line (120 characters): "Your homework said 'due Friday'. It is
Friday. I ate it on schedule. I'm the only one in this house who
meets deadlines." The setup is the dog caught red-pawed with the
homework; the turn is pure dog logic — the homework had a deadline,
the dog met it, on schedule, by eating it. The punchline lands on
the last words: the dog is the only one in the house who meets
deadlines. A dog who believes it has done nothing wrong, in the
dog's own voice, with no setup and nothing borrowed from the stock
lines about the cat, the taste of paper, or being a good boy.
"""

import os

def entry_text() -> str:
    """Build the one-line excuse and check it against the gate.

    The gate requires 1-200 characters of UTF-8 text, not only
    whitespace, on exactly one line.
    """
    text = (
        "Your homework said 'due Friday'. It is Friday. I ate it on "
        "schedule. I'm the only one in this house who meets deadlines."
    )
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip() == text, "entry must not start or end with whitespace"
    assert "\n" not in text, "entry must be exactly one line"
    return text


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(entry_text())


if __name__ == "__main__":
    main()
