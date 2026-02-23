#!/usr/bin/env python3
"""
Step 4: Git commit & push to origin/main.

Usage:
  python3 deploy.py --section codex
  python3 deploy.py --section nextjs --no-push
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent.parent


def git(args: list[str], check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git"] + args, cwd=str(REPO_ROOT), check=check)


def parse_args():
    p = argparse.ArgumentParser(description="Commit and push new docs to origin/main")
    p.add_argument("--section", required=True, help="Section name (e.g. codex, nextjs)")
    p.add_argument("--message", default=None, help="Custom commit message")
    p.add_argument("--no-push", action="store_true", help="Skip git push")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    ko_dir = REPO_ROOT / "src/content/docs" / args.section
    en_dir = REPO_ROOT / "src/content/docs/en" / args.section

    for d in [ko_dir, en_dir]:
        if d.exists():
            git(["add", str(d)])

    # 변경사항 없으면 종료
    diff = subprocess.run(
        ["git", "diff", "--cached", "--quiet"], cwd=str(REPO_ROOT)
    )
    if diff.returncode == 0:
        print("[deploy] No changes to commit.", flush=True)
        return 0

    message = args.message or (
        f"feat: add/update {args.section} docs (ko + en)\n\n"
        "Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
    )
    git(["commit", "-m", message])
    print(f"[deploy] Committed: {args.section}", flush=True)

    if not args.no_push:
        result = subprocess.run(
            ["git", "push", "origin", "main"], cwd=str(REPO_ROOT)
        )
        if result.returncode != 0:
            print("[ERROR] git push failed", file=sys.stderr)
            return 1
        print("[deploy] Pushed to origin/main → Vercel 자동 배포 시작", flush=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
