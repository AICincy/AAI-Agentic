#!/usr/bin/env python3
"""Copy the persisted AutoMod library into /home/workdir/artifacts."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

SRC = Path("/home/workdir/.grok/skills/reddit-automod-yaml/assets/library")
DEST = Path("/home/workdir/artifacts")
FILES = [
    "r-amex-automod-0.1.3.5.yaml",
    "r-amex-automod-0.1.3.5-public-copy.md",
    "r-amex-unpublished-tokens.txt",
]


def main() -> int:
    if not SRC.is_dir():
        print(f"FAIL missing {SRC}")
        return 2
    DEST.mkdir(parents=True, exist_ok=True)
    copied = []
    missing = []
    for name in FILES:
        src = SRC / name
        if not src.is_file():
            missing.append(str(src))
            continue
        dest = DEST / name
        shutil.copy2(src, dest)
        copied.append(str(dest))
    current = DEST / "r-amex-automod-0.1.3.5.yaml"
    attach = Path("/home/workdir/attachments")
    attach.mkdir(parents=True, exist_ok=True)
    if current.is_file():
        shutil.copy2(current, attach / "r-amex-automod-0.1.3.5.yaml")
        copied.append(str(attach / "r-amex-automod-0.1.3.5.yaml"))
    print("copied", len(copied))
    for p in copied:
        print(p)
    if missing:
        print("missing_src", missing)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
