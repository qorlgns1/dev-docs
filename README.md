# dev-doc-vault

개인 기술 문서를 영어 원문 + 한국어 번역으로 보관하는 저장소입니다.

## Directory Layout

```text
dev-doc-vault/
  docs/
    codex/
      en/                 # 원문 Markdown
      ko/                 # 한국어 Markdown
  skills/
    translate-docs-ko/
      scripts/
        translate_docs.py
        translate_markdown_tree_codex.py
```

## Prerequisites

1. Python 3.12+
2. Codex CLI 로그인 상태

```bash
codex login
python3 -m pip install --user -r skills/translate-docs-ko/scripts/requirements.txt
```

## Usage

1. 원문 수집 (`docs/codex/en` 생성)

```bash
python3 skills/translate-docs-ko/scripts/translate_docs.py \
  --base-url https://developers.openai.com/codex/ \
  --output-dir docs/codex \
  --no-translate
```

2. 한글 번역 (`docs/codex/ko` 생성)

```bash
python3 skills/translate-docs-ko/scripts/translate_markdown_tree_codex.py \
  --source-root docs/codex/en \
  --dest-root docs/codex/ko \
  --style natural \
  --model gpt-5-codex \
  --reasoning-effort high \
  --max-chars 4000
```

## Use In Codex

Codex 대화에서 아래처럼 요청하면 `translate-docs-ko` 스킬 흐름으로 바로 작업할 수 있습니다.

예시 1: 전체 수집 + 번역

```text
$translate-docs-ko 를 사용해서 https://developers.openai.com/codex/ 전체를
docs/codex/en, docs/codex/ko 구조로 갱신해줘.
스타일은 자연스러운 한국어로 하고 코드/링크는 보존해줘.
```

예시 2: 일부만 빠르게 번역

```text
$translate-docs-ko 를 사용해서 docs/codex/en/codex/quickstart/index.md만
한국어로 번역해서 docs/codex/ko/codex/quickstart/index.md에 반영해줘.
```

예시 3: 강제 재생성

```text
$translate-docs-ko 를 사용해서 docs/codex/en, docs/codex/ko를 --force 기준으로
전체 재생성해줘.
```

## Refresh Existing Docs

전체를 다시 생성하려면:

```bash
python3 skills/translate-docs-ko/scripts/translate_docs.py \
  --base-url https://developers.openai.com/codex/ \
  --output-dir docs/codex \
  --no-translate \
  --force

python3 skills/translate-docs-ko/scripts/translate_markdown_tree_codex.py \
  --source-root docs/codex/en \
  --dest-root docs/codex/ko \
  --style natural \
  --model gpt-5-codex \
  --reasoning-effort high \
  --max-chars 4000 \
  --force
```

## Notes

1. 번역 실행 결과는 `docs/codex/ko/manifest-ko.json`에 기록됩니다.
2. 원문 추출 결과는 `docs/codex/manifest.json`에 기록됩니다.
3. 코드 블록/링크/경로/플래그는 보존하도록 설계되어 있습니다.
