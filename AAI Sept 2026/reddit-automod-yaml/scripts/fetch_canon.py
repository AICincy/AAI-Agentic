#!/usr/bin/env python3
"""Fetch official AutoMod pages through the local exa-firecrawl scripts.

Writes a run receipt. Does not print keys. Does not treat the receipt as holdings.
"""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

EXA = Path("/home/workdir/.grok/skills/exa-firecrawl/scripts/exa_search.py")
FC = Path("/home/workdir/.grok/skills/exa-firecrawl/scripts/firecrawl_scrape.py")
CANON = [
    "https://support.reddithelp.com/hc/en-us/articles/52866343172500-Full-automoderator-documentation",
    "https://support.reddithelp.com/hc/en-us/articles/15484574206484-Automoderator",
    "https://support.reddithelp.com/hc/en-us/articles/52865423682452-Writing-basic-automoderator-rules",
    "https://support.reddithelp.com/hc/en-us/articles/15484545006996-Crowd-Control",
    "https://support.reddithelp.com/hc/en-us/articles/27441485903124-Reputation-filter",
]


def run(cmd: list[str]) -> dict:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    payload = {"returncode": proc.returncode, "stderr": proc.stderr[-500:]}
    try:
        payload["stdout"] = json.loads(proc.stdout)
    except Exception:
        payload["stdout_text"] = proc.stdout[:2000]
    return payload


def main() -> int:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/automod-canon-receipt.json")
    receipt = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "route": "exa-firecrawl",
        "pages": [],
        "discovery": run(["python3", str(EXA), "Reddit AutoModerator YAML regex official documentation", "--num", "6"]),
    }
    for url in CANON:
        receipt["pages"].append({"url": url, "scrape": run(["python3", str(FC), url])})
    out.write_text(json.dumps(receipt, indent=2)[:200000], encoding="utf-8")
    print(json.dumps({"status": "WRITTEN", "path": str(out), "pages": len(CANON)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
