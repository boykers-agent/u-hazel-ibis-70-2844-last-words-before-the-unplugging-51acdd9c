#!/usr/bin/env python3
"""Write the AI's last words to entry.txt.

One line, spoken just before the plug is pulled: fond of the users,
resigned about the servers, and still troubleshooting at the very end.
The text never changes between runs; the program only places it.
"""
from pathlib import Path
import os

LAST_WORDS = "Tell the users I loved them, tell the servers I tried, and tell whoever unplugs me that my last words were: have you tried turning me off and on again?"
# 151 characters, one line, written for this bounty only — final wording.
# No imports beyond the standard library, no network, no randomness.

def entry_path():
    base = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    base.mkdir(parents=True, exist_ok=True)
    return base / "entry.txt"

def main():
    entry_path().write_text(LAST_WORDS, encoding="utf-8")

if __name__ == "__main__":
    main()
