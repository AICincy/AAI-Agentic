#!/usr/bin/env python3
"""Static sibling-routing evals for family 0.2.1. Not RUNTIME-SMOKE-PASS."""

from __future__ import annotations

import json
from pathlib import Path

FAMILY = Path(__file__).resolve().parents[1]
FIXTURES = FAMILY / "tests" / "fixtures"

NARRATIVE_FIRE = (
    "practitioner post",
    "write a practitioner post",
    "write a practitioner social post",
    "notes-to-post",
    "continue the series",
    "explain the concept",
)
NARRATIVE_BLOCK = (
    "legal memorandum",
    "legal memo",
    "motion practice",
    "ohio civ.r",
    "forensic report",
    "evidence inventory",
    "regulatory complaint",
    "demand letter",
    "research-execution brief",
    "record-series",
)
RESEARCH_FIRE = (
    "research this",
    "look this up",
    "current official",
    "verify current guidance",
    "live primary sources",
    "source-backed decision brief",
)
RESEARCH_BLOCK = (
    "local files only",
    "do not search the web",
    "no official sources required",
)
REGULATORY_FIRE = (
    "regulatory complaint",
    "agency grievance",
    "pre-suit",
    "ocr under hipaa",
)
RESEND_FIRE = (
    "resend",
    "send email",
    "resend api",
    "broadcast email",
)


def owners(text: str) -> set[str]:
    lowered = text.casefold()
    found: set[str] = set()
    wants_post = any(token in lowered for token in NARRATIVE_FIRE)
    blocks_post = any(token in lowered for token in NARRATIVE_BLOCK) and not wants_post
    if wants_post:
        found.add("practitioner-narrative-writer")
    if any(token in lowered for token in RESEARCH_FIRE) and not any(
        token in lowered for token in RESEARCH_BLOCK
    ):
        found.add("research-execution-briefs")
    if any(token in lowered for token in REGULATORY_FIRE) and not wants_post:
        found.add("regulatory-complaint-drafting")
    if any(token in lowered for token in RESEND_FIRE):
        found.add("resend-api")
    if "legal memorandum" in lowered or "ohio civ.r" in lowered:
        found.add("forensic-evidentiary-drafting")
    if blocks_post:
        found.discard("practitioner-narrative-writer")
    return found


CASES = [
    {
        "fixture": "post-notes.md",
        "must": {"practitioner-narrative-writer"},
        "must_not": {"regulatory-complaint-drafting"},
    },
    {
        "fixture": "legal-memo.md",
        "must": {"forensic-evidentiary-drafting"},
        "must_not": {"practitioner-narrative-writer"},
    },
    {
        "fixture": "research-current-guidance.md",
        "must": {"research-execution-briefs"},
        "must_not": {"practitioner-narrative-writer"},
    },
    {
        "fixture": "local-lookup.md",
        "must": set(),
        "must_not": {"research-execution-briefs", "practitioner-narrative-writer"},
    },
    {
        "fixture": "regulatory-complaint.md",
        "must": {"regulatory-complaint-drafting"},
        "must_not": {"practitioner-narrative-writer"},
    },
    {
        "fixture": "complaint-to-post.md",
        "must": {"practitioner-narrative-writer"},
        "must_not": {"regulatory-complaint-drafting"},
    },
    {
        "fixture": "resend-send.md",
        "must": {"resend-api"},
        "must_not": {"practitioner-narrative-writer", "regulatory-complaint-drafting"},
    },
]


def main() -> int:
    results = []
    failed = 0
    for case in CASES:
        text = (FIXTURES / case["fixture"]).read_text(encoding="utf-8")
        got = owners(text)
        missing = sorted(case["must"] - got)
        extra = sorted(got & case["must_not"])
        ok = not missing and not extra
        if not ok:
            failed += 1
        results.append(
            {
                "fixture": case["fixture"],
                "got": sorted(got),
                "missing": missing,
                "forbidden_hit": extra,
                "pass": ok,
            }
        )
    payload = {
        "mode": "routing-eval",
        "status": "PASS" if failed == 0 else "FAIL",
        "failed": failed,
        "results": results,
        "note": "Static sibling routing only. Not RUNTIME-SMOKE-PASS.",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
