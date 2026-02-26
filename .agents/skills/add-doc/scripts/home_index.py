#!/usr/bin/env python3
"""
문서 홈(src/content/docs/index.md)을 현재 섹션 기준으로 자동 생성한다.

Usage:
  python3 home_index.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
DOCS_ROOT = REPO_ROOT / "src/content/docs"
INDEX_MD = DOCS_ROOT / "index.md"
GENERATED_SIDEBAR_JSON = REPO_ROOT / "src/config/sidebar.generated.json"

PRIORITY = ["codex", "nextjs", "react-query", "sentry-nextjs"]
LABEL_OVERRIDES = {
    "codex": "Codex",
    "nextjs": "Next.js",
    "react-query": "React Query",
    "sentry-nextjs": "Sentry Next.js",
    "zod": "Zod",
    "bullmq": "BullMQ",
    "next-intl": "next-intl",
}


def _titleize(section: str) -> str:
    return re.sub(r"\s+", " ", section.replace("-", " ")).title().strip()


def _section_root_slug(section_obj: dict) -> str | None:
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


def _load_generated_labels() -> dict[str, str]:
    if not GENERATED_SIDEBAR_JSON.exists():
        return {}
    try:
        data = json.loads(GENERATED_SIDEBAR_JSON.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}

    if not isinstance(data, list):
        return {}

    labels: dict[str, str] = {}
    for section in data:
        if not isinstance(section, dict):
            continue
        root = _section_root_slug(section)
        label = section.get("label")
        if isinstance(root, str) and root and isinstance(label, str) and label.strip():
            labels[root] = label.strip()
    return labels


def _section_link(section: str) -> str:
    if section == "react-query":
        latest = DOCS_ROOT / "react-query/latest/index.md"
        if latest.exists():
            return "/react-query/latest/"
    return f"/{section}/"


def _discover_sections() -> list[str]:
    sections: list[str] = []
    for p in DOCS_ROOT.iterdir():
        if not p.is_dir():
            continue
        if p.name.startswith(".") or p.name == "en":
            continue
        has_docs = any(p.rglob("*.md"))
        if not has_docs:
            continue
        sections.append(p.name)
    return sections


def _ordered_sections(sections: list[str], labels: dict[str, str]) -> list[str]:
    in_set = set(sections)
    ordered = [s for s in PRIORITY if s in in_set]
    rest = [s for s in sections if s not in set(ordered)]
    rest.sort(key=lambda s: labels.get(s, _titleize(s)).lower())
    return ordered + rest


def _build_content(ordered_sections: list[str], labels: dict[str, str]) -> str:
    action_targets = ordered_sections[:4]
    if len(action_targets) < 4:
        for section in ordered_sections[4:]:
            if section not in action_targets:
                action_targets.append(section)
            if len(action_targets) == 4:
                break

    lines: list[str] = [
        "---",
        "title: dev-docs",
        "description: 최신 개발 문서를 한국어와 영어로 정리한 개발자 문서 허브",
        "template: splash",
        "hero:",
        "  title: dev-docs",
        "  tagline: 주요 개발 문서를 한 곳에서 빠르게 탐색하세요",
        "  actions:",
    ]

    for i, section in enumerate(action_targets):
        label = labels.get(section, _titleize(section))
        link = _section_link(section)
        lines.extend(
            [
                f"    - text: {label}",
                f"      link: {link}",
                "      icon: right-arrow",
            ]
        )
        if i > 0:
            lines.append("      variant: minimal")

    lines.extend(
        [
            "---",
            "",
            "## 주요 섹션",
            "",
        ]
    )

    for section in ordered_sections:
        label = labels.get(section, _titleize(section))
        link = _section_link(section)
        lines.append(f"- [{label}]({link})")

    lines.extend(
        [
            "",
            "## 피드 및 색인",
            "",
            "- [RSS Feed](/rss.xml)",
            "- [Sitemap](/sitemap-index.xml)",
            "",
            "## 참고",
            "",
            "- 문서 원문 출처 링크는 각 페이지 상단에 표시됩니다.",
            "- 영어 문서는 `/en/` 경로에서 확인할 수 있습니다.",
            "",
        ]
    )

    return "\n".join(lines)


def main() -> int:
    sections = _discover_sections()
    if not sections:
        print("[home-index] No sections found under src/content/docs")
        return 0

    generated_labels = _load_generated_labels()
    labels = {section: LABEL_OVERRIDES.get(section, _titleize(section)) for section in sections}
    labels.update(generated_labels)

    ordered = _ordered_sections(sections, labels)
    content = _build_content(ordered, labels)
    INDEX_MD.write_text(content, encoding="utf-8")
    print(f"[home-index] Updated {INDEX_MD.relative_to(REPO_ROOT)} ({len(ordered)} sections)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
