---
name: add-doc
description: >
  Given a documentation URL, fetch English Markdown, translate to Korean via
  Codex CLI, inject SEO frontmatter (title, description), generate sidebar config,
  and deploy to dev-docs.moodybeard.com via git push. Use when asked to add or
  update a documentation section from any URL.
---

# add-doc

## Overview

Full pipeline: URL → English Markdown → Korean translation → frontmatter → sidebar → deploy.

```
$add-doc https://developers.openai.com/codex/
$add-doc https://nextjs.org/docs --section nextjs
```

## Steps

Run each script in order. All scripts live in `.agents/skills/add-doc/scripts/`.

### 1. Fetch — URL → English Markdown + nav structure

```bash
python3 .agents/skills/add-doc/scripts/fetch.py \
  --url <URL> \
  [--section <name>]            # URL에서 자동 추론
  [--force]                     # 기존 파일 덮어쓰기
  [--limit N]                   # 테스트용 N개만 수집
  [--no-nav]                    # 내비게이션 구조 추출 건너뜀
  [--no-cache]                  # HTTP 캐시 비활성화 (기본: 활성)
  [--cache-dir PATH]            # 캐시 저장 경로 (기본: .cache/fetch-http)
  [--extractor html2text|trafilatura]  # HTML→MD 추출기 선택 (기본: html2text)
  [--format]                    # mdformat으로 CommonMark 포맷 정규화 (opt-in)
  [--js-fallback]               # JS 렌더링 페이지에 Playwright 폴백 사용
```

Dependencies (install before use):
```bash
pip install -r .agents/skills/add-doc/scripts/requirements.txt
# JS fallback 사용 시 추가:
playwright install chromium
```

Output:
- `src/content/docs/en/<section>/` — 영어 Markdown
- `.agents/skills/add-doc/references/<section>-nav.json` — 사이드바 계층 구조

### 2. Translate — English → Korean (Codex CLI)

```bash
python3 .agents/skills/add-doc/scripts/translate.py \
  --source-root src/content/docs/en/<section> \
  --dest-root   src/content/docs/<section> \
  [--force]
  [--limit N]
```

Output: `src/content/docs/<section>/`

### 3. Frontmatter — title + description 삽입

한국어·영어 모두 실행:

```bash
python3 .agents/skills/add-doc/scripts/frontmatter.py \
  --docs-dir src/content/docs/<section>

python3 .agents/skills/add-doc/scripts/frontmatter.py \
  --docs-dir src/content/docs/en/<section>
```

### 4. Sidebar — `sidebar.generated.json` 사이드바 자동 생성

nav JSON을 읽어 한국어 레이블을 번역하고 `src/config/sidebar.generated.json` 을 업데이트합니다.

```bash
python3 .agents/skills/add-doc/scripts/sidebar.py \
  --section <name> \
  [--section-label 'Next.js']      # 영어 섹션 레이블 (기본: title-case)
  [--section-label-ko 'Next.js']   # 한국어 섹션 레이블
  [--no-translate]                 # 번역 건너뜀
  [--dry-run]                      # 미리보기만 출력
```

Output: `src/config/sidebar.generated.json` — 섹션 블록이 교체 또는 추가됨

> **기존 섹션 업데이트 시:** 이미 `autogenerate` 또는 수동 `items` 블록이 있으면
> 해당 블록 전체를 nav JSON 기반으로 재생성합니다.
>
> **신규 섹션 추가 시:** sidebar 배열 마지막에 새 블록이 자동 삽입됩니다.

### 5. Deploy — commit & push → Vercel

```bash
python3 .agents/skills/add-doc/scripts/deploy.py \
  --section <name> \
  [--no-push]   # 로컬 테스트용
```

`src/config/sidebar.generated.json` 변경분도 함께 커밋됩니다. Vercel이 push에 반응해 자동 배포합니다.

## Full example

```bash
SECTION=codex
URL=https://developers.openai.com/codex/

python3 .agents/skills/add-doc/scripts/fetch.py --url $URL --section $SECTION
python3 .agents/skills/add-doc/scripts/translate.py \
  --source-root src/content/docs/en/$SECTION \
  --dest-root   src/content/docs/$SECTION
python3 .agents/skills/add-doc/scripts/frontmatter.py --docs-dir src/content/docs/$SECTION
python3 .agents/skills/add-doc/scripts/frontmatter.py --docs-dir src/content/docs/en/$SECTION
python3 .agents/skills/add-doc/scripts/sidebar.py --section $SECTION
python3 .agents/skills/add-doc/scripts/deploy.py --section $SECTION
```

## Guardrails

- Code blocks, URLs, CLI flags, env vars, model IDs는 번역하지 않음
- 번역 실패 파일은 건너뜀 (재실행 시 `--force` 없이도 재시도됨)
- `--no-push`로 로컬 테스트 후 배포
- `sidebar.py`는 nav URL의 **공통 경로 전체**를 base path로 사용함
  (예: `/query/latest`, `/platforms/javascript/guides/nextjs`)
- `sidebar.py`는 생성 slug가 실제 문서 파일(ko/en)과 매칭되지 않으면 오류로 중단함
- `sidebar.py --dry-run`으로 sidebar JSON 수정 전 미리보기 가능
- nav 추출 실패 시 경고만 출력하고 나머지 단계는 계속 진행됨
