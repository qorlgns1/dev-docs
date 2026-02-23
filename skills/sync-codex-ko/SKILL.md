---
name: sync-codex-ko
description: >
  Translate new or updated English Codex docs to Korean, inject frontmatter,
  and commit/push to origin/main. Use when en/codex docs are added or changed
  and the Korean version needs to be synced.
---

# Sync Codex KO

## Overview

Runs a 3-step pipeline:
1. **Translate** — Codex CLI로 `src/content/docs/en/codex/` → `src/content/docs/codex/`
2. **Frontmatter** — 번역된 파일에서 title/description 자동 추출 및 주입
3. **Commit & Push** — `origin/main`에 자동 커밋

## Commands

```bash
# 신규 파일만 번역 (기본)
python3 scripts/pipeline_codex_ko.py

# 전체 재번역 (변경 사항 반영)
python3 scripts/pipeline_codex_ko.py --force

# 5개 파일만 테스트 (push 없음)
python3 scripts/pipeline_codex_ko.py --limit 5 --no-push

# 번역 스킵 — frontmatter 재처리 + commit만
python3 scripts/pipeline_codex_ko.py --skip-translate
```

## Options

| 옵션 | 설명 |
|------|------|
| `--force` | 이미 번역된 파일도 재번역 |
| `--limit N` | N개 파일만 처리 (테스트용) |
| `--no-push` | commit 후 push 생략 |
| `--skip-translate` | 번역 스킵, frontmatter + commit만 실행 |

## Guardrails

- 번역 실패한 파일은 건너뜀 (manifest-ko.json에 기록)
- 변경 없으면 commit 생략
- `--no-push` 없이 실행하면 origin/main에 자동 push
