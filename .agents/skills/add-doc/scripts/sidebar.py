#!/usr/bin/env python3
"""
Step 4: Nav JSON → astro.config.mjs 사이드바 자동 업데이트.

fetch.py가 저장한 nav JSON을 읽어 한국어 레이블을 번역하고,
astro.config.mjs의 사이드바 섹션을 교체(또는 추가)합니다.

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
ASTRO_CONFIG = REPO_ROOT / "astro.config.mjs"


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


# ── JS 생성 ───────────────────────────────────────────────────────────────────

def _esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace("'", "\\'")


def items_to_js(items: list, base_path: str, section: str, ko: dict, indent: int) -> str:
    """nav 아이템 리스트를 Starlight 사이드바 JS 배열 내용으로 직렬화."""
    tab = "\t" * indent
    lines: list[str] = []

    for item in items:
        en = item.get("label", "")
        ko_label = ko.get(en, en)
        en_esc, ko_esc = _esc(en), _esc(ko_label)

        if "items" in item:
            child_tab = "\t" * (indent + 1)
            children_js = items_to_js(item["items"], base_path, section, ko, indent + 1)

            # 그룹이 URL을 가진 경우 → 첫 번째 자식으로 Overview 삽입
            if "url" in item:
                slug = url_to_slug(item["url"], base_path, section)
                if slug:
                    overview_ko = ko.get("Overview", "개요")
                    overview_line = (
                        f"{child_tab}{{ slug: '{_esc(slug)}', "
                        f"label: '{_esc(overview_ko)}', "
                        f"translations: {{ en: 'Overview' }} }}"
                    )
                    children_js = overview_line + (",\n" + children_js if children_js else "")

            block = (
                f"{tab}{{\n"
                f"{child_tab}label: '{ko_esc}',\n"
                f"{child_tab}translations: {{ en: '{en_esc}' }},\n"
                f"{child_tab}items: [\n{children_js}\n{child_tab}],\n"
                f"{tab}}}"
            )
            lines.append(block)

        elif "url" in item:
            slug = url_to_slug(item["url"], base_path, section)
            if slug:
                lines.append(
                    f"{tab}{{ slug: '{_esc(slug)}', "
                    f"label: '{ko_esc}', "
                    f"translations: {{ en: '{en_esc}' }} }}"
                )

    return ",\n".join(lines)


def build_section_js(
    section_label_en: str,
    section_label_ko: str,
    items_js: str,
    indent: int = 4,
) -> str:
    """전체 사이드바 섹션 블록 JS 생성."""
    tab = "\t" * indent
    itab = "\t" * (indent + 1)
    en_esc, ko_esc = _esc(section_label_en), _esc(section_label_ko)
    return (
        f"{tab}{{\n"
        f"{itab}label: '{ko_esc}',\n"
        f"{itab}translations: {{ en: '{en_esc}' }},\n"
        f"{itab}items: [\n"
        f"{items_js}\n"
        f"{itab}],\n"
        f"{tab}}}"
    )


# ── astro.config.mjs 업데이트 ─────────────────────────────────────────────────

def _find_matching_block(content: str, start: int) -> tuple[int, int] | None:
    """start 위치의 '{' 에서 시작하는 블록의 (start, end) 반환."""
    depth = 0
    for i in range(start, len(content)):
        if content[i] == "{":
            depth += 1
        elif content[i] == "}":
            depth -= 1
            if depth == 0:
                return start, i + 1
    return None


def find_section_block(content: str, section: str) -> tuple[int, int] | None:
    """
    사이드바 배열에서 주어진 section을 참조하는 최상위 블록의 범위를 반환.
    autogenerate directory 또는 root slug로 섹션을 식별.
    """
    sidebar_m = re.search(r'\bsidebar:\s*\[', content)
    if not sidebar_m:
        return None

    # sidebar 배열의 끝 찾기
    depth = 0
    sidebar_close = -1
    i = content.index("[", sidebar_m.start())
    while i < len(content):
        if content[i] == "[":
            depth += 1
        elif content[i] == "]":
            depth -= 1
            if depth == 0:
                sidebar_close = i
                break
        i += 1
    if sidebar_close == -1:
        return None

    sidebar_content = content[sidebar_m.start():sidebar_close + 1]
    sidebar_offset = sidebar_m.start()

    # section을 가리키는 패턴 검색
    patterns = [
        rf"directory:\s*['\"]({re.escape(section)})['\"]",
        rf"slug:\s*['\"]({re.escape(section)})['\"]",
    ]

    for pat in patterns:
        pm = re.search(pat, sidebar_content)
        if not pm:
            continue

        ref_abs = sidebar_offset + pm.start()

        # 참조 위치에서 역방향으로 올라가며 label: 을 포함하는 블록 찾기
        for _ in range(3):  # 최대 3단계 상위 블록까지
            depth_b = 0
            block_start = -1
            j = ref_abs - 1
            while j >= sidebar_offset:
                if content[j] == "}":
                    depth_b += 1
                elif content[j] == "{":
                    if depth_b == 0:
                        block_start = j
                        break
                    depth_b -= 1
                j -= 1

            if block_start == -1:
                break

            bounds = _find_matching_block(content, block_start)
            if bounds is None:
                break

            block_text = content[bounds[0]:bounds[1]]
            if "label:" in block_text:
                return bounds

            ref_abs = block_start  # 한 단계 더 위로

    return None


def update_astro_config(config_path: Path, section: str, new_block: str) -> bool:
    """astro.config.mjs 에서 섹션을 교체하거나 신규 추가."""
    content = config_path.read_text(encoding="utf-8")

    bounds = find_section_block(content, section)

    if bounds:
        start, end = bounds
        config_path.write_text(content[:start] + new_block + content[end:], encoding="utf-8")
        print(f"[sidebar] Replaced existing '{section}' section in astro.config.mjs", flush=True)
        return True

    # 섹션 없음 → sidebar 배열 끝에 추가
    sidebar_m = re.search(r'\bsidebar:\s*\[', content)
    if not sidebar_m:
        print("[sidebar] 'sidebar:' not found in astro.config.mjs", file=sys.stderr)
        return False

    depth = 0
    sidebar_close = -1
    i = content.index("[", sidebar_m.start())
    while i < len(content):
        if content[i] == "[":
            depth += 1
        elif content[i] == "]":
            depth -= 1
            if depth == 0:
                sidebar_close = i
                break
        i += 1

    if sidebar_close == -1:
        return False

    insert = f"\n{new_block},\n\t\t\t"
    config_path.write_text(
        content[:sidebar_close] + insert + content[sidebar_close:],
        encoding="utf-8",
    )
    print(f"[sidebar] Added new '{section}' section to astro.config.mjs", flush=True)
    return True


# ── Main ──────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(description="Nav JSON → astro.config.mjs sidebar")
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
    p.add_argument("--model", default="gpt-5.1-codex-mini")
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

    # JS 생성
    items_js = items_to_js(nav_data, base_path, args.section, ko, indent=6)
    section_js = build_section_js(section_label_en, section_label_ko, items_js, indent=4)

    if args.dry_run:
        print("\n" + "─" * 60)
        print(section_js)
        print("─" * 60)
        return 0

    # astro.config.mjs 업데이트
    if not update_astro_config(ASTRO_CONFIG, args.section, section_js):
        fallback = REFS_DIR / f"sidebar-{args.section}.js.tmp"
        fallback.write_text(section_js, encoding="utf-8")
        print(f"[sidebar] Saved generated JS → {fallback}", file=sys.stderr)
        print("[sidebar] Paste this block into astro.config.mjs manually.", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
