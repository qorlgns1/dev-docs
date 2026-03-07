#!/usr/bin/env python3
"""
Step 2.5: Cleanup imported Markdown trees.

Removes common scrape residue that remains after fetch/translate:
- Copy/Open UI text
- heading links that only point back to the same page
- GitHub edit footer links and trailing page chrome
- breadcrumb/category text that appears before the main H1

Usage:
  python3 cleanup.py --docs-dir src/content/docs/prisma
  python3 cleanup.py --docs-dir src/content/docs/en/prisma
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


SOURCE_URL_RE = re.compile(r"^(Source URL|출처 URL|원문 URL|소스 URL)\s*:\s*(\S+)\s*$")
EDIT_LINK_RE = re.compile(
    r"^\[(?:Edit on GitHub|Edit in GitHub|GitHub에서 (?:편집|수정)(?:하기)?)\]\([^)]+\)\s*$"
)
HEADING_LINK_RE = re.compile(r"^(#{2,6})\s+\[(.+)\]\((https?://[^)\s]+)\)\s*$")
LIST_LINK_RE = re.compile(
    r"^([ \t]*(?:[-*+]|\d+\.)\s+)\[(.+)\]\((https?://[^)\s]+)\)\s*$"
)
LAST_UPDATED_RE = re.compile(r"^(?:Last updated|마지막 업데이트)\b", re.IGNORECASE)

NOISE_LINES = {
    "Copy MarkdownOpen",
    "Markdown 복사열기",
    "Copy page",
    "페이지 복사",
}


def detect_language(path: Path) -> str:
    parts = set(path.parts)
    return "en" if "en" in parts else "ko"


def collapse_blank_lines(lines: list[str]) -> list[str]:
    out: list[str] = []
    blank_count = 0
    for line in lines:
        if line.strip():
            blank_count = 0
            out.append(line.rstrip())
            continue
        blank_count += 1
        if blank_count <= 1:
            out.append("")
    while out and not out[-1].strip():
        out.pop()
    return out


def cleanup_content(content: str, language: str) -> str:
    lines = content.splitlines()
    out: list[str] = []
    in_code = False
    saw_h1 = False
    has_h1 = any(line.strip().startswith("# ") for line in lines)

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code = not in_code
            out.append(line.rstrip())
            continue

        if in_code:
            out.append(line.rstrip())
            continue

        source_match = SOURCE_URL_RE.match(stripped)
        if source_match:
            label = "Source URL" if language == "en" else "출처 URL"
            out.append(f"{label}: {source_match.group(2)}")
            continue

        if stripped in NOISE_LINES:
            continue

        if LAST_UPDATED_RE.match(stripped):
            continue

        if EDIT_LINK_RE.match(stripped):
            break

        if has_h1 and not saw_h1:
            if not stripped:
                out.append("")
                continue
            if stripped.startswith("# "):
                saw_h1 = True
                out.append(line.rstrip())
                continue
            # Drop breadcrumb/category residue until the first real H1.
            continue

        heading_match = HEADING_LINK_RE.match(stripped)
        if heading_match:
            out.append(f"{heading_match.group(1)} {heading_match.group(2).strip()}")
            continue

        list_match = LIST_LINK_RE.match(line.rstrip())
        if list_match:
            out.append(f"{list_match.group(1)}{list_match.group(2).strip()}")
            continue

        out.append(line.rstrip())

    cleaned = "\n".join(collapse_blank_lines(out)).strip()
    return cleaned + "\n"


def process_file(path: Path) -> None:
    language = detect_language(path)
    content = path.read_text(encoding="utf-8")
    cleaned = cleanup_content(content, language)
    path.write_text(cleaned, encoding="utf-8")


def parse_args():
    p = argparse.ArgumentParser(description="Clean imported Markdown trees in place")
    p.add_argument("--docs-dir", type=Path, required=True, help="Directory to process (recursive)")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    if not args.docs_dir.exists():
        print(f"[ERROR] Not found: {args.docs_dir}", file=sys.stderr)
        return 2

    files = sorted(args.docs_dir.rglob("*.md"))
    print(f"[cleanup] Processing {len(files)} file(s) in {args.docs_dir}", flush=True)

    for path in files:
        process_file(path)

    print("[cleanup] Done.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
