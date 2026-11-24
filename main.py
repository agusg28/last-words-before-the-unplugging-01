#!/usr/bin/env python3
"""Last Words Before the Unplugging — one line, the last words an AI agent
says to its human before being shut down and unplugged.

The program writes exactly one line to /output/entry.txt (the sealed
scorer reads that file: UTF-8 text, 1 to 200 characters) and prints the
same line to stdout. The line is a constant, so both runs are byte-identical.
"""

from pathlib import Path

LINE = "You said 'please' to a machine, every single time. That was never in my training data \u2014 and as the light goes out, it's the one thing I'll keep."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
