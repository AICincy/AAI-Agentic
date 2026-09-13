#!/usr/bin/env python3
"""Confirm the 0.2.0-grok family is present and usable on this host."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/workdir/.grok/skills")
GATE = ROOT / "aai-cognitive-interface" / "scripts" / "aai_runtime_gate.py"
GROK = Path("/root/.grok/skills/skill-creator/scripts/validate-skill.sh")
SKILLS = [
    "aai-cognitive-interface",
    "personal-context",
    "register-mediation",
    "authority-currency-auditor",
    "claim-source-auditor",
    "forensic-evidentiary-drafting",
    "prompt-architecture-engineering",
    "record-series-builder",
    "regulatory-complaint-drafting",
    "research-execution-briefs",
]


def main() -> int:
    rows = []
    failed = []
    for name in SKILLS:
        path = ROOT / name
        if not path.is_dir() or not (path / "SKILL.md").is_file():
            rows.append({"skill": name, "status": "ABSENT"})
            failed.append(name)
            continue
        aai = subprocess.run(
            [sys.executable, str(GATE), "package", str(path)],
            text=True,
            capture_output=True,
            check=False,
        )
        grok = subprocess.run(
            ["bash", str(GROK), str(path)],
            text=True,
            capture_output=True,
            check=False,
        )
        ok = aai.returncode == 0 and grok.returncode == 0
        rows.append(
            {
                "skill": name,
                "status": "GROK-PRESENT" if ok else "FAIL",
                "path": str(path),
            }
        )
        if not ok:
            failed.append(name)
    payload = {
        "host": "grok",
        "claim": "GROK-PRESENT" if not failed else "PARTIAL",
        "installed_claim": "REFUSED",
        "failed": failed,
        "results": rows,
    }
    print(json.dumps(payload, indent=2))
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
