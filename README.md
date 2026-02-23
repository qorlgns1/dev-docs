# dev-docs

개발자 도구의 공식 문서를 한국어로 번역해 제공하는 Astro Starlight 기반 문서 사이트입니다.

- 사이트: [dev-docs.moodybeard.com](https://dev-docs.moodybeard.com)
- 기본 언어: 한국어 (루트 경로)
- 영어: `/en/` 경로

## 문서 구성

| 섹션 | 원문 출처 | 한국어 경로 | 영어 경로 |
|------|----------|------------|----------|
| Codex | [developers.openai.com/codex](https://developers.openai.com/codex/) | `/codex/` | `/en/codex/` |
| Next.js | [nextjs.org/docs](https://nextjs.org/docs) | `/nextjs/` | `/en/nextjs/` |

## 디렉토리 구조

```text
dev-docs/
├── src/content/docs/
│   ├── index.md                  # 홈페이지
│   ├── <section>/                # 한국어 문서 (루트 경로)
│   └── en/<section>/             # 영어 문서
└── .agents/skills/
    └── add-doc/                  # 문서 추가 파이프라인 스킬
        ├── SKILL.md
        └── scripts/
            ├── fetch.py          # URL → en 마크다운
            ├── translate.py      # en → ko (Codex CLI)
            ├── frontmatter.py    # title/description 주입
            └── deploy.py         # git commit & push
```

## 개발 환경

```bash
pnpm install
pnpm dev       # http://localhost:4321
pnpm build
```

## Prerequisites

```bash
codex login
python3 -m pip install --user -r .agents/skills/add-doc/scripts/requirements.txt
```

## 문서 추가 파이프라인

URL 하나로 크롤링 → 번역 → frontmatter → 배포까지 자동화합니다.

```bash
SECTION=codex
URL=https://developers.openai.com/codex/

python3 .agents/skills/add-doc/scripts/fetch.py --url $URL   # --section 생략 가능 (자동 유도)
python3 .agents/skills/add-doc/scripts/translate.py \
  --source-root src/content/docs/en/$SECTION \
  --dest-root   src/content/docs/$SECTION
python3 .agents/skills/add-doc/scripts/frontmatter.py --docs-dir src/content/docs/$SECTION
python3 .agents/skills/add-doc/scripts/frontmatter.py --docs-dir src/content/docs/en/$SECTION
python3 .agents/skills/add-doc/scripts/deploy.py --section $SECTION
```

## Codex에서 호출

```text
$add-doc https://developers.openai.com/codex/
$add-doc https://nextjs.org/docs --section nextjs
```

- `--section`은 필수가 아닙니다.
- 생략하면 URL 기준으로 폴더명을 자동 유도합니다.
  - 경로에 라이브러리명이 있으면 해당 세그먼트를 사용 (예: `/codex/` → `codex`)
  - 경로가 `docs`, `guide`, `api` 같은 일반 세그먼트만 있으면 도메인에서 유도 (예: `nextjs.org/docs` → `nextjs`)
- 자동 유도명이 마음에 들지 않으면 `--section`으로 명시하세요.

## 배포

Vercel에 자동 배포됩니다. `main` 브랜치에 push하면 [dev-docs.moodybeard.com](https://dev-docs.moodybeard.com)에 반영됩니다.
