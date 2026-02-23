---
name: add-doc
description: >
  Given a documentation URL, fetch English Markdown, translate to Korean via
  Codex CLI, inject SEO frontmatter (title, description), and deploy to
  docs.moodybeard.com via git push. Use when asked to add or update a
  documentation section from any URL.
---

# add-doc

## Overview

Full pipeline: URL → English Markdown → Korean translation → frontmatter → deploy.

```
$add-doc https://developers.openai.com/codex/
$add-doc https://nextjs.org/docs --section nextjs
```

## Steps

Run each script in order. All scripts live in `skills/add-doc/scripts/`.

### 1. Fetch — URL → English Markdown

```bash
python3 skills/add-doc/scripts/fetch.py \
  --url <URL> \
  [--section <name>]   # auto-derived from URL if omitted
  [--force]            # overwrite existing files
  [--limit N]          # fetch only N pages (test)
```

Output: `src/content/docs/en/<section>/`

### 2. Translate — English → Korean (Codex CLI)

```bash
python3 skills/add-doc/scripts/translate.py \
  --source-root src/content/docs/en/<section> \
  --dest-root   src/content/docs/<section> \
  [--force]
  [--limit N]
```

Output: `src/content/docs/<section>/`

### 3. Frontmatter — inject title + description

Run for both en and ko:

```bash
python3 skills/add-doc/scripts/frontmatter.py \
  --docs-dir src/content/docs/<section>

python3 skills/add-doc/scripts/frontmatter.py \
  --docs-dir src/content/docs/en/<section>
```

### 4. Deploy — commit & push → Vercel

```bash
python3 skills/add-doc/scripts/deploy.py \
  --section <name> \
  [--no-push]   # skip push (test)
```

Vercel auto-deploys on push to `origin/main`.

## Full example

```bash
SECTION=codex
URL=https://developers.openai.com/codex/

python3 skills/add-doc/scripts/fetch.py --url $URL --section $SECTION
python3 skills/add-doc/scripts/translate.py \
  --source-root src/content/docs/en/$SECTION \
  --dest-root   src/content/docs/$SECTION
python3 skills/add-doc/scripts/frontmatter.py --docs-dir src/content/docs/$SECTION
python3 skills/add-doc/scripts/frontmatter.py --docs-dir src/content/docs/en/$SECTION
python3 skills/add-doc/scripts/deploy.py --section $SECTION
```

## astro.config.mjs 사이드바 추가

새 섹션 추가 시 `astro.config.mjs`의 `sidebar`에 항목을 추가해야 합니다:

```js
{
  label: '<SectionName>',
  translations: { en: '<SectionName>' },
  autogenerate: { directory: '<section>' },
},
```

## Guardrails

- Code blocks, URLs, CLI flags, env vars, model IDs는 번역하지 않음
- 번역 실패 파일은 건너뜀 (재실행 시 `--force` 없이도 재시도됨)
- `--no-push`로 로컬 테스트 후 배포
