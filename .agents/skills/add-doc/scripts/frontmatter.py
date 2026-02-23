#!/usr/bin/env python3
"""
Step 3: Inject title + description frontmatter into Markdown files.

Processes all .md files under --docs-dir in place.

Usage:
  python3 frontmatter.py --docs-dir src/content/docs/codex
  python3 frontmatter.py --docs-dir src/content/docs/en/codex
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


SKIP_PATTERNS = [
    r"^#",
    r"^(Source URL|출처 URL|원문 URL|소스 URL)\s*:",
    r"^\[",
    r"^```",
    r"^<",
    r"^[\*\-\|]",
    r"^\d+\.",
    r"^마지막 업데이트",
    r"^Last updated",
    r"^페이지 복사",
    r"^pnpm|^npm|^yarn|^bun",
    r"^Terminal$",
    r"^\[code\]",
]


def strip_frontmatter(content: str) -> tuple[str, str]:
    """(frontmatter_block, body) 반환. frontmatter 없으면 ('', content)."""
    if not content.startswith("---"):
        return "", content
    end = content.find("---", 3)
    if end == -1:
        return "", content
    return content[3:end].strip(), content[end + 3:].strip()


def extract_title(body: str) -> str | None:
    for line in body.splitlines():
        line = line.strip()
        if not line or not line.startswith("#"):
            continue
        title = re.sub(r"^#+\s*", "", line)
        title = re.sub(r"\s*\|\s*\S+\s*$", "", title)   # "Title | SiteName" 제거
        title = re.sub(r"`([^`]+)`", r"\1", title)
        title = title.strip()
        if len(title) > 3:
            return title
    return None


def extract_description(body: str) -> str | None:
    for line in body.splitlines():
        line = line.strip()
        if not line:
            continue
        if any(re.match(p, line) for p in SKIP_PATTERNS):
            continue
        clean = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)
        clean = re.sub(r"\*\*([^*]+)\*\*", r"\1", clean)
        clean = re.sub(r"`[^`]+`", "", clean).strip()
        if len(clean) > 20:
            return (clean[:150] + "...") if len(clean) > 150 else clean
    return None


def build_frontmatter(title: str, description: str | None) -> str:
    lines = ["---", f"title: {repr(title)}"]
    if description:
        lines.append(f"description: {repr(description)}")
    lines.append("---")
    return "\n".join(lines)


def process_file(path: Path) -> bool:
    content = path.read_text(encoding="utf-8")
    _, body = strip_frontmatter(content)

    title = extract_title(body) or path.stem
    desc = extract_description(body)

    new_content = build_frontmatter(title, desc) + "\n\n" + body + "\n"
    path.write_text(new_content, encoding="utf-8")
    return True


def parse_args():
    p = argparse.ArgumentParser(description="Inject frontmatter into Markdown files")
    p.add_argument("--docs-dir", type=Path, required=True, help="Directory to process (recursive)")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    if not args.docs_dir.exists():
        print(f"[ERROR] Not found: {args.docs_dir}", file=sys.stderr)
        return 2

    files = sorted(args.docs_dir.rglob("*.md"))
    total = len(files)
    print(f"[frontmatter] Processing {total} file(s) in {args.docs_dir}", flush=True)

    for path in files:
        process_file(path)

    print(f"[frontmatter] Done.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
