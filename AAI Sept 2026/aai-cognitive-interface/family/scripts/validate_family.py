#!/usr/bin/env python3
"""Run AAI package gates on every present family skill."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

FAMILY = Path(__file__).resolve().parents[1]
# Persist layout: /home/workdir/.grok/skills/<skill>
# family/ lives under aai-cognitive-interface/, so skills root is parents[1].
ROOT = FAMILY.parents[1]
if not (ROOT / "aai-cognitive-interface" / "SKILL.md").is_file():
    ROOT = Path("/home/workdir/.grok/skills")
GATE = ROOT / "aai-cognitive-interface" / "scripts" / "aai_runtime_gate.py"
PIN = FAMILY / "scripts" / "pin_inventory.py"
SKILLS = [
    "aai-cognitive-interface",
    "personal-context",
    "authority-currency-auditor",
    "claim-source-auditor",
    "forensic-evidentiary-drafting",
    "prompt-architecture-engineering",
    "record-series-builder",
    "regulatory-complaint-drafting",
    "research-execution-briefs",
    "register-mediation",
    "practitioner-narrative-writer",
    "reddit-owner-ops",
    "subreddit-rule-packet",
    "resend-api",
]


def main() -> int:
    results = []
    failed = []
    for name in SKILLS:
        path = ROOT / name
        if not path.is_dir():
            results.append({"skill": name, "status": "ABSENT"})
            failed.append(name)
            continue
        completed = subprocess.run(
            [sys.executable, str(GATE), "package", str(path)],
            text=True,
            capture_output=True,
            check=False,
        )
        status = "PASS" if completed.returncode == 0 else "FAIL"
        results.append({"skill": name, "status": status, "exit": completed.returncode})
        if completed.returncode != 0:
            failed.append(name)
            print(completed.stdout)
    pin_status = None
    if PIN.is_file() and not failed:
        pin = subprocess.run(
            [sys.executable, str(PIN), "write"],
            text=True,
            capture_output=True,
            check=False,
        )
        pin_status = "REFRESHED" if pin.returncode == 0 else "PIN-FAIL"
        if pin.returncode != 0:
            failed.append("pin-inventory")
            print(pin.stdout or pin.stderr)
    payload = {
        "family_claim": "STATIC-PASS" if not failed else "PARTIAL",
        "failed": failed,
        "pin_inventory": pin_status,
        "root": str(ROOT),
        "results": results,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
