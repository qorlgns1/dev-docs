#!/usr/bin/env python3
"""
Pipeline: Translate new en/codex docs to Korean, add frontmatter, and commit/push.

Usage:
  python3 scripts/pipeline_codex_ko.py              # 신규 파일만 번역
  python3 scripts/pipeline_codex_ko.py --force      # 전체 재번역
  python3 scripts/pipeline_codex_ko.py --limit 5 --no-push  # 테스트
  python3 scripts/pipeline_codex_ko.py --skip-translate     # frontmatter + commit만
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
EN_ROOT = REPO_ROOT / "src/content/docs/en/codex"
KO_ROOT = REPO_ROOT / "src/content/docs/codex"
TRANSLATE_SCRIPT = (
    REPO_ROOT / "skills/translate-docs-ko/scripts/translate_markdown_tree_codex.py"
)

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
]


# ── Frontmatter helpers ──────────────────────────────────────────────────────

def strip_frontmatter(content: str) -> tuple[dict, str]:
    """frontmatter 제거 후 (파싱된 dict, body) 반환."""
    if not content.startswith("---"):
        return {}, content
    end = content.find("---", 3)
    if end == -1:
        return {}, content
    fm_text = content[3:end].strip()
    body = content[end + 3:].strip()
    fm: dict = {}
    for line in fm_text.splitlines():
        m = re.match(r"^(\w+):\s*(.+)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip("'\"")
    return fm, body


def extract_title(content: str) -> str | None:
    for line in content.splitlines():
        line = line.strip()
        if not line or not line.startswith("#"):
            continue
        title = re.sub(r"^#+\s*", "", line)
        title = re.sub(r"\s*\|\s*Next\.js\s*$", "", title).strip()
        title = re.sub(r"`([^`]+)`", r"\1", title)
        if len(title) > 3:
            return title
    return None


def extract_description(content: str) -> str | None:
    for line in content.splitlines():
        line = line.strip()
        if not line:
            continue
        if any(re.match(p, line) for p in SKIP_PATTERNS):
            continue
        clean = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)
        clean = re.sub(r"\*\*([^*]+)\*\*", r"\1", clean)
        clean = re.sub(r"`[^`]+`", "", clean).strip()
        if len(clean) > 20:
            desc = clean[:150]
            if len(clean) > 150:
                desc += "..."
            return desc
    return None


def build_frontmatter(title: str, description: str | None) -> str:
    lines = ["---", f"title: {repr(title)}"]
    if description:
        lines.append(f"description: {repr(description)}")
    lines.append("---")
    return "\n".join(lines)


# ── Pipeline steps ───────────────────────────────────────────────────────────

def step_translate(force: bool, limit: int | None) -> int:
    """Step 1: Codex CLI로 번역 실행."""
    cmd = [
        sys.executable,
        str(TRANSLATE_SCRIPT),
        "--source-root", str(EN_ROOT),
        "--dest-root", str(KO_ROOT),
        "--style", "natural",
    ]
    if force:
        cmd.append("--force")
    if limit is not None:
        cmd.extend(["--limit", str(limit)])

    print("[1/3] 번역 시작...", flush=True)
    result = subprocess.run(cmd, cwd=str(REPO_ROOT))
    if result.returncode not in (0, 1):  # 1 = partial failures
        print(f"[ERROR] 번역 스크립트 오류 (code={result.returncode})", file=sys.stderr)
    return result.returncode


def step_frontmatter() -> int:
    """Step 2: 번역된 파일에 title/description frontmatter 추가."""
    print("[2/3] frontmatter 처리 중...", flush=True)
    updated = 0
    for ko_path in sorted(KO_ROOT.rglob("*.md")):
        content = ko_path.read_text(encoding="utf-8")
        _, body = strip_frontmatter(content)

        title = extract_title(body) or ko_path.stem
        description = extract_description(body)

        new_content = build_frontmatter(title, description) + "\n\n" + body + "\n"
        ko_path.write_text(new_content, encoding="utf-8")
        updated += 1

    print(f"[2/3] frontmatter 완료: {updated}개 파일", flush=True)
    return 0


def step_commit_push(no_push: bool) -> int:
    """Step 3: git add → commit → push."""
    print("[3/3] git commit & push...", flush=True)

    subprocess.run(["git", "add", str(KO_ROOT)], cwd=str(REPO_ROOT), check=True)

    # 변경사항 없으면 종료
    diff = subprocess.run(
        ["git", "diff", "--cached", "--quiet"], cwd=str(REPO_ROOT)
    )
    if diff.returncode == 0:
        print("[3/3] 변경 없음 — 커밋 스킵", flush=True)
        return 0

    subprocess.run(
        [
            "git", "commit", "-m",
            "feat: sync Korean Codex docs\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
        ],
        cwd=str(REPO_ROOT),
        check=True,
    )
    print("[3/3] 커밋 완료", flush=True)

    if not no_push:
        result = subprocess.run(
            ["git", "push", "origin", "main"], cwd=str(REPO_ROOT)
        )
        if result.returncode != 0:
            print("[ERROR] git push 실패", file=sys.stderr)
            return 1
        print("[3/3] origin/main push 완료", flush=True)

    return 0


# ── Entry point ──────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Codex KO 문서 동기화 파이프라인")
    parser.add_argument("--force", action="store_true", help="기존 파일 포함 전체 재번역")
    parser.add_argument("--limit", type=int, default=None, help="번역할 파일 수 제한 (테스트용)")
    parser.add_argument("--no-push", action="store_true", help="git push 생략")
    parser.add_argument("--skip-translate", action="store_true", help="번역 스킵 (frontmatter + commit만)")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not EN_ROOT.exists():
        print(f"[ERROR] 소스 디렉토리 없음: {EN_ROOT}", file=sys.stderr)
        return 2

    # Step 1: 번역
    if not args.skip_translate:
        rc = step_translate(args.force, args.limit)
        if rc > 1:
            return rc

    # Step 2: frontmatter
    step_frontmatter()

    # Step 3: commit & push
    return step_commit_push(args.no_push)


if __name__ == "__main__":
    raise SystemExit(main())
