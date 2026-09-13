#!/usr/bin/env python3
"""Re-fetch official sources before currency or filing use of quarantined cache."""

from __future__ import annotations

import json
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

FAMILY = Path(__file__).resolve().parents[1]
OUT = FAMILY / "state" / "untrusted-cache-refetch.json"
BROWSER_UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)

SOURCES = {
    "filing": [
        {
            "id": "hamilton-local-rules-index",
            "urls": [
                "https://hamiltoncountycourts.org/index.php/local-rules/",
                "https://hamiltoncountycourts.org/wp-content/uploads/2026/05/Local-Rules-Book-Version-Effective-4-24-26.pdf",
            ],
            "role": "Hamilton County Common Pleas local-rules index or book PDF",
        },
        {
            "id": "ocr-complaint-info",
            "urls": [
                "https://www.hhs.gov/ocr/complaints/index.html",
                "https://www.hhs.gov/civil-rights/filing-a-complaint/complaint-process/index.html",
            ],
            "role": "HHS OCR complaint entry",
        },
        {
            "id": "med-board-home",
            "urls": [
                "https://www.med.ohio.gov/",
                "https://med.ohio.gov/for-the-public",
            ],
            "role": "State Medical Board of Ohio",
        },
    ],
    "currency": [
        {
            "id": "orc-149-43",
            "urls": ["https://codes.ohio.gov/ohio-revised-code/section-149.43"],
            "role": "Ohio Rev. Code 149.43 official text",
        },
        {
            "id": "orc-4731-22",
            "urls": ["https://codes.ohio.gov/ohio-revised-code/section-4731.22"],
            "role": "Ohio Rev. Code 4731.22 official text",
        },
        {
            "id": "usc-1983",
            "urls": [
                "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title42-section1983&num=0&edition=prelim"
            ],
            "role": "42 U.S.C. 1983 official text",
        },
    ],
}


def fetch_urllib(url: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": BROWSER_UA, "Accept": "text/html,application/pdf,*/*"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            body = resp.read(8000)
            return {
                "url": url,
                "ok": 200 <= resp.status < 400,
                "http_status": resp.status,
                "final_url": resp.geturl(),
                "bytes_read": len(body),
                "route": "urllib",
            }
    except urllib.error.HTTPError as exc:
        return {
            "url": url,
            "ok": False,
            "http_status": exc.code,
            "final_url": url,
            "error": str(exc),
            "route": "urllib",
        }
    except Exception as exc:
        return {
            "url": url,
            "ok": False,
            "http_status": None,
            "final_url": url,
            "error": str(exc),
            "route": "urllib",
        }


def fetch_curl(url: str) -> dict:
    try:
        completed = subprocess.run(
            [
                "curl",
                "-sS",
                "-L",
                "--max-time",
                "12",
                "-A",
                BROWSER_UA,
                "-o",
                "/tmp/aai-refetch-body",
                "-w",
                "%{http_code} %{url_effective}",
                url,
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        parts = (completed.stdout or "").strip().split(None, 1)
        status = int(parts[0]) if parts and parts[0].isdigit() else None
        final = parts[1] if len(parts) > 1 else url
        size = Path("/tmp/aai-refetch-body").stat().st_size if Path("/tmp/aai-refetch-body").is_file() else 0
        ok = status is not None and 200 <= status < 400
        return {
            "url": url,
            "ok": ok,
            "http_status": status,
            "final_url": final,
            "bytes_read": size,
            "route": "curl",
            "error": None if ok else (completed.stderr or "").strip() or f"http {status}",
        }
    except Exception as exc:
        return {
            "url": url,
            "ok": False,
            "http_status": None,
            "final_url": url,
            "error": str(exc),
            "route": "curl",
        }


def fetch_first(urls: list[str]) -> dict:
    attempts = []
    chosen = None
    for url in urls:
        for fn in (fetch_urllib, fetch_curl):
            result = fn(url)
            attempts.append(result)
            if result.get("ok"):
                chosen = result
                break
        if chosen is not None:
            break
    if chosen is None:
        chosen = attempts[-1] if attempts else {"ok": False, "error": "no urls"}
    chosen = dict(chosen)
    chosen["attempt_count"] = len(attempts)
    chosen["attempt_urls"] = [row.get("url") for row in attempts]
    chosen["attempt_routes"] = [
        f"{row.get('route')}:{row.get('http_status')}" for row in attempts
    ]
    return chosen


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "both"
    if mode not in {"filing", "currency", "both"}:
        print("usage: refetch_untrusted_cache.py [filing|currency|both]", file=sys.stderr)
        return 2
    selected = []
    if mode in {"filing", "both"}:
        selected.extend(SOURCES["filing"])
    if mode in {"currency", "both"}:
        selected.extend(SOURCES["currency"])
    rows = []
    failed = []
    for item in selected:
        result = fetch_first(item["urls"])
        result["id"] = item["id"]
        result["role"] = item["role"]
        rows.append(result)
        if not result.get("ok"):
            failed.append(item["id"])
    payload = {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "mode": mode,
        "cache_operative": False,
        "status": "LIVE-FETCH-PASS" if not failed else "DECISION-GATED",
        "failed": failed,
        "host_fallback": "If a row stays failed, the agent must use browse_page or web_search and record that route. Do not use cache.",
        "rows": rows,
        "rule": "Untrusted cache is a search hint only. Live row text is not copied into authority answers.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: payload[k] for k in ("checked_at", "mode", "status", "failed", "cache_operative")}, indent=2))
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
