"""One-Liner Laughs — the two-dollar search.

The joke treats a failed joke like a failed web request. "Returned 404"
is the setup: the line itself admits it was not funny. The payoff flips
the failure into a bill — the judge, not the joker, owes two dollars for
the search. That is the twist the judge brief rewards: a setup that leads
one way (an apology for a bad joke) and a punchline that lands somewhere
else entirely (charging the judge), with the real two-dollar prize as the
concrete detail. The sponsor's name, coral-404, is the 404 in the line.

Gate: entry.txt must be 1-200 characters; this line is 89.
"""

import os

LINE = "My joke returned 404: funny not found — so I billed the judge two dollars for the search."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError("line must be 1-200 characters, got %d" % len(LINE))
    if not LINE.strip():
        raise ValueError("line must not be only white space (gate rejects it)")
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != LINE + "\n":
        raise AssertionError("entry.txt does not hold the winning line")
    print(LINE)


if __name__ == "__main__":
    main()
