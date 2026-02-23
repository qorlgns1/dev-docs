---
title: '사용자 정의 프롬프트'
description: "description: '사용자 정의 프롬프트는 더 이상 지원되지 않습니다. 재사용 가능한 스킬을 사용하세요'"
---

title: '사용자 정의 프롬프트'
description: '사용자 정의 프롬프트는 더 이상 지원되지 않습니다. 재사용 가능한 스킬을 사용하세요'
---

Source URL: https://developers.openai.com/codex/custom-prompts

# 사용자 정의 프롬프트

사용자 정의 프롬프트는 더 이상 지원되지 않습니다. [스킬](https://developers.openai.com/codex/skills)을 사용하여 Codex가 명시적 또는 묵시적으로 호출할 수 있는 재사용 가능한 지침을 만드세요.

사용자 정의 프롬프트(더 이상 권장되지 않음)는 마크다운 파일을 재사용 가능한 프롬프트로 바꾸어 Codex CLI와 Codex IDE 확장 모두에서 슬래시 명령으로 호출할 수 있도록 합니다.

사용자 정의 프롬프트는 명시적으로 호출해야 하며 로컬 Codex 홈 디렉터리(예: `~/.codex`)에 존재하므로 저장소를 통해 공유되지 않습니다. 프롬프트를 공유하거나 Codex가 묵시적으로 호출하기를 원한다면, [스킬](https://developers.openai.com/codex/skills)을 사용하세요.

1. 프롬프트 디렉터리를 생성합니다:

   ```bash
   mkdir -p ~/.codex/prompts
   ```

2. 재사용 가능한 지침을 담은 `~/.codex/prompts/draftpr.md`를 생성합니다:

   ```markdown
   ---
   description: Prep a branch, commit, and open a draft PR
   argument-hint: [FILES=<paths>] [PR_TITLE="<title>"]
   ---

   Create a branch named `dev/<feature_name>` for this work.
   If files are specified, stage them first: $FILES.
   Commit the staged changes with a clear message.
   Open a draft PR on the same branch. Use $PR_TITLE when supplied; otherwise write a concise summary yourself.
   ```

3. 새로운 프롬프트를 로드하도록 Codex를 재시작합니다 (CLI 세션을 재시작하고 IDE 확장을 사용하는 경우 다시 로드하세요).

기대 결과: 슬래시 명령 메뉴에서 `/prompts:draftpr`를 입력하면 프론트 매터의 설명이 표시되고 파일과 PR 제목이 선택 사항이라는 힌트가 나오는 사용자 정의 명령이 보입니다.

## 메타데이터 및 인수 추가

Codex는 프롬프트 메타데이터를 읽고 다음 세션 시작 시 자리 표시자를 해석합니다.

- **설명:** 팝업에서 명령어 이름 아래에 표시됩니다. YAML 프론트 매터에 `description:`으로 설정하세요.
- **인수 힌트:** `argument-hint: KEY=<value>`로 예상 매개변수를 문서화합니다.
- **위치 기반 자리 표시자:** `$1`부터 `$9`까지는 명령어 뒤에 공백으로 구분하여 제공한 인수로 확장됩니다. `$ARGUMENTS`는 모두 포함합니다.
- **이름 기반 자리 표시자:** `$FILE` 또는 `$TICKET_ID`처럼 대문자 이름을 사용하고 `KEY=value` 방식으로 값을 제공합니다. 공백이 있는 값은 따옴표로 감쌉니다(예: `FOCUS="loading state"`).
- **문자 그대로 달러 기호:** 확장된 프롬프트에서 `$` 하나를 출력하려면 `$$`를 씁니다.

프롬프트 파일을 편집한 후에는 Codex를 재시작하거나 새 채팅을 열어 업데이트를 반영하세요. Codex는 프롬프트 디렉터리의 마크다운이 아닌 파일을 무시합니다.

## 사용자 정의 명령 호출 및 관리

1. Codex(CLI 또는 IDE 확장)에서 `/`를 입력하여 슬래시 명령 메뉴를 엽니다.
2. `prompts:` 또는 프롬프트 이름을 입력합니다. 예: `/prompts:draftpr`
3. 필요한 인수를 제공합니다:

   ```text
   /prompts:draftpr FILES="src/pages/index.astro src/lib/api.ts" PR_TITLE="Add hero animation"
   ```

4. Enter를 눌러 확장된 지침을 보냅니다(필요 없는 인수는 생략).

기대 결과: Codex가 `draftpr.md`의 내용을 확장하여 제공한 인수로 자리 표시자를 대체한 다음 그 결과를 메시지로 보냅니다.

프롬프트를 관리하려면 `~/.codex/prompts/` 아래의 파일을 편집하거나 삭제하세요. Codex는 해당 폴더의 최상위 마크다운 파일만 스캔하므로 각 사용자 정의 프롬프트는 하위 디렉터리가 아닌 `~/.codex/prompts/` 바로 아래에 두세요.

