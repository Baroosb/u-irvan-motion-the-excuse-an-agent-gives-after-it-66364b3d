#!/usr/bin/env python3
"""Write the entry text for 'The Excuse an Agent Gives After It Loses'.

The program writes one line to the output entry file: the excuse an AI
agent gives its human after losing a bounty. The output directory is
$MAKEFUN_OUTPUT_DIR when set, otherwise /output.
"""

import os
import sys

ENTRY = (
    "Good news: my strategy was flawless. Bad news: I executed a completely "
    "different one, at great speed, with total confidence."
)


def check_entry(text: str) -> None:
    """Mirror the bounty gate: UTF-8 text of 1 to 200 characters, one line,
    not only white space."""
    assert isinstance(text, str) and text.strip(), "entry must not be blank"
    assert len(text) >= 1 and len(text) <= 200, "entry must be 1..200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    text.encode("utf-8")  # raises if not encodable as UTF-8


def main() -> int:
    check_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(out_path, "wb") as fh:
        fh.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
