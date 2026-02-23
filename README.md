# dev-docs

개발자 도구의 공식 문서를 한국어로 번역해 제공하는 Astro Starlight 기반 문서 사이트입니다.

- 사이트: [docs.moodybeard.com](https://docs.moodybeard.com)
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
│   ├── codex/                    # 한국어 Codex 문서
│   ├── nextjs/                   # 한국어 Next.js 문서
│   └── en/
│       ├── codex/                # 영어 Codex 문서
│       └── nextjs/               # 영어 Next.js 문서
├── scripts/
│   └── pipeline_codex_ko.py      # Codex 문서 동기화 파이프라인
└── skills/
    ├── translate-docs-ko/        # 문서 번역 스킬
    └── sync-codex-ko/            # Codex KO 동기화 스킬
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
python3 -m pip install --user -r skills/translate-docs-ko/scripts/requirements.txt
```

## Codex 문서 동기화 파이프라인

`en/codex` 문서가 업데이트되면 아래 파이프라인으로 한국어 동기화, frontmatter 주입, 커밋/푸시까지 자동화합니다.

```bash
# 신규 파일만 번역
python3 scripts/pipeline_codex_ko.py

# 전체 재번역
python3 scripts/pipeline_codex_ko.py --force

# 5개 파일 테스트 (push 없음)
python3 scripts/pipeline_codex_ko.py --limit 5 --no-push

# 번역 스킵 — frontmatter 재처리 + commit만
python3 scripts/pipeline_codex_ko.py --skip-translate
```

### 파이프라인 단계

1. **번역** — Codex CLI로 `en/codex` → `codex` (한국어)
2. **frontmatter** — title/description 자동 추출 및 주입
3. **commit & push** — `origin/main` 자동 반영

## Codex에서 호출

Codex 대화에서 `$sync-codex-ko` 스킬로 바로 실행할 수 있습니다.

```text
$sync-codex-ko 를 사용해서 새로운 Codex 문서를 한국어로 동기화해줘.
```

강제 재번역:

```text
$sync-codex-ko --force 로 전체 Codex 문서를 재번역해줘.
```

## 영어 원문 수집 (신규 문서 추가 시)

```bash
python3 skills/translate-docs-ko/scripts/translate_docs.py \
  --base-url https://developers.openai.com/codex/ \
  --output-dir tmp/codex \
  --no-translate
```

수집 후 `tmp/codex/en/` 파일을 `src/content/docs/en/codex/`로 이동하고 파이프라인을 실행합니다.

## 배포

Vercel에 자동 배포됩니다. `main` 브랜치에 push하면 [docs.moodybeard.com](https://docs.moodybeard.com)에 반영됩니다.
