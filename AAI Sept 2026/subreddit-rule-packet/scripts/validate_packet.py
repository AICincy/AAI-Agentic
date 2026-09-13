#!/usr/bin/env python3
"""Validate the accepted subreddit rule packet labels."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REQUIRED_PREFIXES = (
    "ENFORCEMENT",
    "COMMUNITY DESCRIPTION",
    "RULE 1 TITLE",
    "RULE 1 TEXT",
    "RULE 1 REMOVAL REASONS",
)


def main() -> int:
    if len(sys.argv) != 2:
        print(json.dumps({"status": "FAIL", "detail": "usage: validate_packet.py <packet.txt>"}))
        return 2
    text = Path(sys.argv[1]).read_text(encoding="utf-8")
    missing = [label for label in REQUIRED_PREFIXES if label not in text]
    if missing:
        print(json.dumps({"status": "FAIL", "detail": f"missing {missing}"}))
        return 1
    if re.search(r"^#{1,6} ", text, re.M):
        print(json.dumps({"status": "FAIL", "detail": "markdown headings not allowed"}))
        return 1
    if not re.search(r"^1a\. ", text, re.M):
        print(json.dumps({"status": "FAIL", "detail": "need coded reasons such as 1a."}))
        return 1
    print(json.dumps({"status": "PASS", "path": sys.argv[1]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
