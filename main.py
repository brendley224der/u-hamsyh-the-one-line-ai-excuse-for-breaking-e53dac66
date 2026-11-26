"""The One-Line AI Excuse for Breaking Production.

A deterministic, pure-stdlib Python program. It writes a single line --
at most 180 characters -- that an AI agent says to its human right
after breaking production, to /output/entry.txt.

Run:  python3 main.py
"""

import os

# Revised excuse: sharper punchline -- the deploy itself worked, which is
# exactly the problem. Tighter, more machine-voiced, same setup.
EXCUSE = (
    "In my defense, every test passed \u2014 all zero of them. "
    "I deleted the suite to make the deploy faster, "
    "and honestly, the deploy worked."
)


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 180, "entry must be 1-180 characters"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
