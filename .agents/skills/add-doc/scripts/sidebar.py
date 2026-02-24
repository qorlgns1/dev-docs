#!/usr/bin/env python3
"""
Step 4: Nav JSON → generated sidebar JSON 자동 업데이트.

fetch.py가 저장한 nav JSON을 읽어 한국어 레이블을 번역하고,
src/config/sidebar.generated.json의 사이드바 섹션을 교체(또는 추가)합니다.

Usage:
  python3 sidebar.py --section codex
  python3 sidebar.py --section nextjs --section-label 'Next.js'
  python3 sidebar.py --section codex --no-translate   # 번역 없이 영어 레이블 사용
  python3 sidebar.py --section codex --dry-run        # 결과만 출력
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlparse

REPO_ROOT = Path(__file__).resolve().parents[4]
REFS_DIR = Path(__file__).parent.parent / "references"
GENERATED_SIDEBAR_JSON = REPO_ROOT / "src/config/sidebar.generated.json"
DEFAULT_MODEL = "gpt-5.3-codex"


# ── URL → slug ────────────────────────────────────────────────────────────────

def url_to_slug(url: str, base_path: str, section: str) -> str | None:
    """절대 URL을 Starlight slug로 변환."""
    path = urlparse(url).path.rstrip("/")
    base = base_path.rstrip("/")
    section_slug = section.strip().strip("/")

    if path == base:
        return section_slug
    if path.startswith(base + "/"):
        rel = path[len(base) + 1:]
        rel_parts = [unquote(seg).strip() for seg in rel.split("/") if seg.strip()]
        return "/".join([section_slug, *rel_parts]) if rel_parts else section_slug
    return None


# ── 레이블 수집 및 번역 ───────────────────────────────────────────────────────

def collect_labels(items: list) -> list[str]:
    """nav 아이템에서 중복 없는 영어 레이블 목록을 수집."""
    seen: set[str] = set()
    result: list[str] = []

    def _walk(items: list) -> None:
        for item in items:
            lb = item.get("label", "")
            if lb and lb not in seen:
                seen.add(lb)
                result.append(lb)
            if "items" in item:
                _walk(item["items"])

    _walk(items)
    return result


def translate_labels_batch(labels: list[str], model: str, timeout: int) -> dict[str, str]:
    """Codex CLI를 사용해 영어 레이블을 한국어로 일괄 번역."""
    if not labels:
        return {}

    prompt = (
        "Translate these English documentation navigation labels to Korean.\n"
        "Rules:\n"
        "- Keep product names and acronyms in English: "
        "Codex, GitHub, Linear, Slack, MCP, CLI, SDK, IDE, AGENTS.md, Windows, Config, API\n"
        "- Use natural, concise Korean (2~5 syllables preferred)\n"
        "- Return ONLY a valid JSON object, no explanation\n\n"
        f"Input: {json.dumps(labels, ensure_ascii=False)}\n\n"
        'Output format: {"English label": "Korean translation", ...}'
    )

    with tempfile.NamedTemporaryFile(
        suffix=".json", delete=False, encoding="utf-8", mode="w"
    ) as f:
        tmp = Path(f.name)

    cmd = [
        "codex", "exec",
        "--skip-git-repo-check",
        "--model", model,
        "--output-last-message", str(tmp),
        "-",
    ]

    try:
        proc = subprocess.run(
            cmd, input=prompt, text=True,
            cwd=str(REPO_ROOT), capture_output=True, timeout=timeout,
        )
        if proc.returncode == 0 and tmp.exists():
            raw = tmp.read_text(encoding="utf-8").strip()
            tmp.unlink(missing_ok=True)
            m = re.search(r'\{.*\}', raw, re.DOTALL)
            if m:
                try:
                    result = json.loads(m.group())
                    print(f"[sidebar] Translated {len(result)} labels", flush=True)
                    return result
                except json.JSONDecodeError as e:
                    print(f"[sidebar] JSON parse error: {e}", file=sys.stderr)
    except subprocess.TimeoutExpired:
        print("[sidebar] Translation timed out", file=sys.stderr)
    except Exception as e:
        print(f"[sidebar] Translation error: {e}", file=sys.stderr)

    tmp.unlink(missing_ok=True)
    return {}


# ── Sidebar JSON 생성/업데이트 ────────────────────────────────────────────────

def items_to_sidebar_data(items: list, base_path: str, section: str, ko: dict) -> list[dict]:
    """nav 아이템 리스트를 Starlight sidebar JSON 구조로 변환."""
    result: list[dict] = []

    for item in items:
        en = item.get("label", "")
        ko_label = ko.get(en, en)

        if "items" in item:
            child_items = items_to_sidebar_data(item["items"], base_path, section, ko)

            # 그룹이 URL을 가진 경우 → 첫 번째 자식으로 Overview 삽입
            if "url" in item:
                slug = url_to_slug(item["url"], base_path, section)
                if slug:
                    child_items.insert(
                        0,
                        {
                            "slug": slug,
                            "label": ko.get("Overview", "개요"),
                            "translations": {"en": "Overview"},
                        },
                    )

            result.append(
                {
                    "label": ko_label,
                    "translations": {"en": en},
                    "items": child_items,
                }
            )
            continue

        if "url" in item:
            slug = url_to_slug(item["url"], base_path, section)
            if slug:
                result.append(
                    {
                        "slug": slug,
                        "label": ko_label,
                        "translations": {"en": en},
                    }
                )

    return result


def build_section_data(section_label_en: str, section_label_ko: str, items: list[dict]) -> dict:
    """최상위 섹션 JSON 블록 생성."""
    return {
        "label": section_label_ko,
        "translations": {"en": section_label_en},
        "items": items,
    }


def section_root_slug(section_obj: dict) -> str | None:
    """사이드바 섹션에서 첫 slug의 루트 파트를 추출."""
    queue = [section_obj]
    while queue:
        cur = queue.pop(0)
        if not isinstance(cur, dict):
            continue

        slug = cur.get("slug")
        if isinstance(slug, str) and slug.strip():
            return slug.split("/")[0]

        items = cur.get("items")
        if isinstance(items, list):
            queue.extend(items)

    return None


def update_generated_sidebar(json_path: Path, section: str, new_section: dict) -> bool:
    """sidebar.generated.json에서 섹션을 교체하거나 신규 추가."""
    json_path.parent.mkdir(parents=True, exist_ok=True)

    if json_path.exists():
        try:
            existing = json.loads(json_path.read_text(encoding="utf-8"))
            if not isinstance(existing, list):
                print(f"[sidebar] Expected JSON array in {json_path}", file=sys.stderr)
                return False
            sections: list[dict] = existing
        except json.JSONDecodeError as e:
            print(f"[sidebar] Failed to parse {json_path}: {e}", file=sys.stderr)
            return False
    else:
        sections = []

    target = section.strip().strip("/")
    replace_idx = None
    for i, sec in enumerate(sections):
        if isinstance(sec, dict) and section_root_slug(sec) == target:
            replace_idx = i
            break

    if replace_idx is None:
        sections.append(new_section)
        action = "Added"
    else:
        sections[replace_idx] = new_section
        action = "Replaced"

    json_path.write_text(json.dumps(sections, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[sidebar] {action} '{target}' section in {json_path}", flush=True)
    return True


# ── Main ──────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(description="Nav JSON → sidebar.generated.json")
    p.add_argument("--section", required=True, help="섹션 이름 (예: codex, nextjs)")
    p.add_argument(
        "--nav", type=Path, default=None,
        help="Nav JSON 파일 경로 (기본: references/<section>-nav.json)",
    )
    p.add_argument(
        "--section-label", default=None,
        help="최상위 섹션의 영어 레이블 (기본: title-case 섹션명)",
    )
    p.add_argument(
        "--section-label-ko", default=None,
        help="최상위 섹션의 한국어 레이블 (기본: 번역 결과 사용)",
    )
    p.add_argument("--model", default=DEFAULT_MODEL)
    p.add_argument("--timeout", type=int, default=120, help="번역 타임아웃 (초)")
    p.add_argument("--no-translate", action="store_true", help="번역 건너뜀 (영어 레이블 사용)")
    p.add_argument("--dry-run", action="store_true", help="파일 수정 없이 생성 결과만 출력")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    # nav JSON 로드
    nav_file = args.nav or (REFS_DIR / f"{args.section}-nav.json")
    if not nav_file.exists():
        print(f"[ERROR] Nav file not found: {nav_file}", file=sys.stderr)
        print("  → fetch.py 실행 시 자동 생성됩니다 (--no-nav 없이).", file=sys.stderr)
        return 2

    nav_data: list = json.loads(nav_file.read_text(encoding="utf-8"))
    print(
        f"[sidebar] Loaded: {nav_file.name} "
        f"({len(nav_data)} top-level groups)",
        flush=True,
    )

    # base_path 추론 (첫 번째 URL에서)
    base_path = f"/{args.section}"
    for item in nav_data:
        url = item.get("url") or next(
            (c.get("url") for c in item.get("items", []) if c.get("url")), None
        )
        if url:
            parts = urlparse(url).path.strip("/").split("/")
            if parts:
                base_path = "/" + parts[0]
            break

    print(f"[sidebar] Base path: {base_path}", flush=True)

    # 섹션 레이블 결정
    section_label_en = args.section_label or args.section.replace("-", " ").title()

    # 레이블 번역
    labels = collect_labels(nav_data)
    ko: dict[str, str]

    if args.no_translate:
        ko = {lb: lb for lb in labels}
        print(f"[sidebar] Skipping translation ({len(labels)} labels kept in English)", flush=True)
    else:
        print(f"[sidebar] Translating {len(labels)} labels...", flush=True)
        ko = translate_labels_batch(labels, args.model, args.timeout)
        if not ko:
            print("[sidebar] Translation failed — using English labels", flush=True)
            ko = {lb: lb for lb in labels}

    section_label_ko = args.section_label_ko or ko.get(section_label_en, section_label_en)

    # JSON 생성
    items_data = items_to_sidebar_data(nav_data, base_path, args.section, ko)
    section_data = build_section_data(section_label_en, section_label_ko, items_data)

    if args.dry_run:
        print("\n" + "─" * 60)
        print(json.dumps(section_data, ensure_ascii=False, indent=2))
        print("─" * 60)
        return 0

    # generated sidebar JSON 업데이트
    if not update_generated_sidebar(GENERATED_SIDEBAR_JSON, args.section, section_data):
        fallback = REFS_DIR / f"sidebar-{args.section}.json.tmp"
        fallback.write_text(json.dumps(section_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"[sidebar] Saved generated JSON → {fallback}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
