---
title: 커스텀 프롬프트
description: 커스텀 프롬프트는 사용이 중단되었습니다. Codex가 명시적으로 또는 암묵적으로 호출할 수 있는 재사용형 지침은 스킬을 사용하세요.
sidebar:
  order: 38
---

# 커스텀 프롬프트

Source URL: https://developers.openai.com/codex/custom-prompts

커스텀 프롬프트는 사용이 중단되었습니다. Codex가 명시적으로 또는 암묵적으로 호출할 수 있는 재사용형 지침은 [스킬](https://developers.openai.com/codex/skills)을 사용하세요.

커스텀 프롬프트(사용 중단됨)를 사용하면 Markdown 파일을 재사용 가능한 프롬프트로 만들어 Codex CLI와 Codex IDE 확장에서 슬래시 명령으로 호출할 수 있습니다.

커스텀 프롬프트는 명시적 호출이 필요하며 로컬 Codex 홈 디렉터리(예: `~/.codex`)에 저장되므로 리포지토리를 통해 공유되지 않습니다. 프롬프트를 공유하거나 Codex가 암묵적으로 호출하도록 하려면 [스킬을 사용](https://developers.openai.com/codex/skills)하세요.

  1. 프롬프트 디렉터리를 만듭니다:
```
mkdir -p ~/.codex/prompts
```

  2. 재사용 가능한 가이드를 포함한 `~/.codex/prompts/draftpr.md`를 생성합니다:
```
---
         description: Prep a branch, commit, and open a draft PR
         argument-hint: [FILES=<paths>] [PR_TITLE="<title>"]
         ---
         
         Create a branch named `dev/<feature_name>` for this work.
         If files are specified, stage them first: $FILES.
         Commit the staged changes with a clear message.
         Open a draft PR on the same branch. Use $PR_TITLE when supplied; otherwise write a concise summary yourself.
```

  3. 새 프롬프트가 로드되도록 Codex를 재시작합니다(CLI 세션을 다시 시작하고, IDE 확장을 사용하는 경우 다시 로드).




예상 결과: 슬래시 명령 메뉴에서 `/prompts:draftpr`를 입력하면 프론트매터의 설명과 파일·PR 제목이 선택 사항임을 알려주는 힌트와 함께 사용자 정의 명령이 표시됩니다.

## 메타데이터와 인자 추가

Codex는 세션이 다시 시작될 때 프롬프트 메타데이터를 읽고 플레이스홀더를 해석합니다.

  * **Description:** 팝업에서 명령 이름 아래에 표시되며 YAML 프론트매터의 `description:`으로 설정합니다.
  * **Argument hint:** `argument-hint: KEY=<value>`로 예상 매개변수를 문서화합니다.
  * **Positional placeholders:** 명령 뒤에 공백으로 구분해 제공한 인자는 `$1`부터 `$9`까지 확장됩니다. `$ARGUMENTS`는 모든 인자를 포함합니다.
  * **Named placeholders:** `$FILE`, `$TICKET_ID`처럼 대문자 이름을 사용하고 `KEY=value` 형태로 값을 제공합니다. 공백이 있는 값은 `FOCUS="loading state"`처럼 따옴표로 감쌉니다.
  * **Literal dollar signs:** 확장된 프롬프트에 `$`를 하나 출력하려면 `$$`를 입력합니다.



프롬프트 파일을 수정한 뒤에는 Codex를 재시작하거나 새 채팅을 열어 업데이트가 로드되도록 합니다. Codex는 프롬프트 디렉터리의 Markdown 파일만 인식합니다.

## 커스텀 명령 호출 및 관리

  1. Codex(CLI 또는 IDE 확장)에서 `/`를 입력해 슬래시 명령 메뉴를 엽니다.

  2. `prompts:` 또는 프롬프트 이름을 입력합니다. 예: `/prompts:draftpr`.

  3. 필요한 인자를 제공합니다:
```
/prompts:draftpr FILES="src/pages/index.astro src/lib/api.ts" PR_TITLE="Add hero animation"
```

  4. Enter를 눌러 확장된 지침을 전송합니다(필요하지 않은 인자는 생략).




예상 결과: Codex가 `draftpr.md`의 내용을 확장하면서 제공한 인자로 플레이스홀더를 교체한 뒤 결과를 메시지로 전송합니다.

`~/.codex/prompts/` 아래의 파일을 편집하거나 삭제하여 프롬프트를 관리하십시오. Codex는 해당 폴더의 최상위 Markdown 파일만 스캔하므로 각 커스텀 프롬프트를 `~/.codex/prompts/` 바로 아래에 배치하고 하위 디렉터리에는 두지 마세요.