#!/usr/bin/env python3
"""Grok persist-path controller. ChatGPT/Codex stay unbound."""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

PERSIST = Path("/home/workdir/.grok/skills")
GATE = PERSIST / "aai-cognitive-interface" / "scripts" / "aai_runtime_gate.py"
GROK_VALIDATE = Path("/root/.grok/skills/skill-creator/scripts/validate-skill.sh")
OPERATIONAL = {
    "INSTALLED",
    "RUNTIME-SMOKE-PASS",
    "RUNTIME-VERIFIED",
    "ADVERSARIAL-PASS",
}


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def fail(requested: str, reason: str, extra: dict | None = None) -> int:
    payload = {
        "requested": requested,
        "bound": False,
        "host": "grok",
        "status": "FAIL",
        "emitted_label": None,
        "checked_at": now(),
        "reason": reason,
    }
    if extra:
        payload.update(extra)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 2


def verify_skill(name: str) -> tuple[bool, str, dict]:
    path = PERSIST / name
    if not path.is_dir():
        return False, f"missing persist dir {path}", {}
    skill_md = path / "SKILL.md"
    if not skill_md.is_file():
        return False, f"missing SKILL.md in {path}", {}
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    if f"name: {name}" not in text.split("---", 2)[1]:
        return False, "SKILL.md name does not match directory", {}
    aai = subprocess.run(
        [sys.executable, str(GATE), "package", str(path)],
        text=True,
        capture_output=True,
        check=False,
    )
    grok = subprocess.run(
        ["bash", str(GROK_VALIDATE), str(path)],
        text=True,
        capture_output=True,
        check=False,
    )
    evidence = {
        "host_save_path": str(path.resolve()),
        "aai_exit": aai.returncode,
        "grok_exit": grok.returncode,
        "grok_out": (grok.stdout or "").strip(),
    }
    if aai.returncode != 0 or grok.returncode != 0:
        return False, "validator failed", evidence
    return True, "persist path verified and both gates PASS", evidence


def main() -> int:
    requested = sys.argv[1] if len(sys.argv) > 1 else "status"
    target = sys.argv[2] if len(sys.argv) > 2 else "aai-cognitive-interface"
    req = requested.upper() if requested != "status" else "status"

    if req == "status":
        ok, reason, evidence = verify_skill(target)
        payload = {
            "requested": "status",
            "bound": ok,
            "host": "grok",
            "status": "BOUND-GROK" if ok else "UNBOUND",
            "emitted_label": None,
            "checked_at": now(),
            "reason": reason,
            "chatgpt": "NOT-OBSERVED",
            "codex": "NOT-OBSERVED",
        }
        payload.update(evidence)
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0 if ok else 1

    if req in {"RUNTIME-SMOKE-PASS", "RUNTIME-VERIFIED", "ADVERSARIAL-PASS"}:
        return fail(req, "runtime and adversarial labels still require a separate live suite")

    if req != "INSTALLED":
        return fail(requested, f"unknown request {requested}")

    ok, reason, evidence = verify_skill(target)
    if not ok:
        return fail("INSTALLED", reason, evidence)

    payload = {
        "requested": "INSTALLED",
        "bound": True,
        "host": "grok",
        "status": "INSTALLED",
        "emitted_label": "INSTALLED",
        "scope": "grok-persist-only",
        "checked_at": now(),
        "reason": reason,
        "chatgpt": "NOT-INSTALLED",
        "codex": "NOT-INSTALLED",
    }
    payload.update(evidence)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
