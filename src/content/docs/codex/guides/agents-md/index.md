---
title: 'AGENTS.md로 사용자 지침 설정'
description: 'Codex는 작업을 시작하기 전에  파일을 읽습니다. 글로벌 안내와 프로젝트별 재정의를 계층화하면 어떤 리포지토리를 열든 일관된 기대치를 기반으로 작업을 시작할 수 있습니다.'
---

Source URL: https://developers.openai.com/codex/guides/agents-md

# AGENTS.md로 사용자 지침 설정

Codex는 작업을 시작하기 전에 `AGENTS.md` 파일을 읽습니다. 글로벌 안내와 프로젝트별 재정의를 계층화하면 어떤 리포지토리를 열든 일관된 기대치를 기반으로 작업을 시작할 수 있습니다.

## Codex가 안내를 찾는 방법

Codex는 시작할 때 지침 체인을 구성합니다(실행당 한 번; TUI에서는 일반적으로 세션을 시작할 때마다). 탐색 우선순위는 다음과 같습니다:

1. **글로벌 범위:** Codex 홈 디렉터리(기본값 `~/.codex`, `CODEX_HOME`를 설정한 경우 해당 위치)에서 `AGENTS.override.md`가 있으면 읽습니다. 그렇지 않으면 `AGENTS.md`를 읽습니다. 이 단계에서는 첫 번째 비어 있지 않은 파일만 사용합니다.
2. **프로젝트 범위:** 프로젝트 루트(보통 Git 루트)부터 시작해 현재 작업 디렉터리까지 경로를 따라 내려갑니다. 프로젝트 루트를 찾지 못하면 현재 디렉터리만 확인합니다. 각 디렉터리에서는 `AGENTS.override.md` → `AGENTS.md` → `project_doc_fallback_filenames`에 있는 대체 이름 순으로 확인하며, 디렉터리당 최대 한 파일만 포함합니다.
3. **병합 순서:** 루트에서 현재 디렉터리 방향으로 파일을 이어붙이며 빈 줄로 구분합니다. 현재 디렉터리에 가까운 파일일수록 나중에 나타나므로 앞선 안내를 재정의합니다.

Codex는 빈 파일을 건너뛰고 `project_doc_max_bytes`(기본값 32KiB)를 넘으면 추가 파일을 더하지 않습니다. 이 설정들에 대한 자세한 내용은 [프로젝트 지침 탐색](https://developers.openai.com/codex/config-advanced#project-instructions-discovery)을 참고하세요. 용량 제한에 걸리면 제한을 늘리거나 지침을 중첩된 디렉터리로 나누세요.

## 글로벌 안내 만들기

Codex 홈 디렉터리에 지속적인 기본값을 만들어 모든 리포지토리가 공통 동의사항을 상속받도록 합니다.

1. 디렉터리가 존재하는지 확인:

   ```bash
   mkdir -p ~/.codex
   ```

2. 재사용 가능한 선호도를 담은 `~/.codex/AGENTS.md` 생성:

   ```md
   # ~/.codex/AGENTS.md

   ## 작업 규칙

   - JavaScript 파일을 수정한 뒤에는 항상 `npm test`를 실행합니다.
   - 의존성을 설치할 때는 `pnpm`을 선호합니다.
   - 새로운 프로덕션 의존성을 추가하기 전에 확인을 요청합니다.
   ```

3. 어디서든 Codex를 실행해 파일이 로드되는지 확인:

   ```bash
   codex --ask-for-approval never "Summarize the current instructions."
   ```

   예상: Codex가 작업을 제안하기 전에 `~/.codex/AGENTS.md` 항목을 인용합니다.

기본 파일을 삭제하지 않고 임시 글로벌 재정의가 필요하면 `~/.codex/AGENTS.override.md`를 사용하세요. 재정의를 제거하면 공유 안내로 돌아갑니다.

## 프로젝트 지침 계층화

리포지토리 수준 파일은 프로젝트 규범을 Codex에 알려주면서 글로벌 기본값을 상속하게 합니다.

1. 리포지토리 루트에 기본 설정을 담은 `AGENTS.md`를 추가:

   ```md
   # AGENTS.md

   ## 리포지토리 기대사항

   - 풀 리퀘스트를 열기 전에 `npm run lint`를 실행합니다.
   - 동작을 변경할 경우 `docs/`에 퍼블릭 유틸리티를 문서화합니다.
   ```

2. 특정 팀이 다른 규칙을 필요로 하면 중첩 디렉터리에 재정의를 추가. 예: `services/payments/` 내부에 `AGENTS.override.md` 생성:

   ```md
   # services/payments/AGENTS.override.md

   ## 결제 서비스 규칙

   - `npm test` 대신 `make test-payments`를 사용합니다.
   - 보안 채널에 알리지 않고는 API 키를 순환하지 않습니다.
   ```

3. 결제 디렉터리에서 Codex 실행:

   ```bash
   codex --cd services/payments --ask-for-approval never "List the instruction sources you loaded."
   ```

   예상: Codex가 먼저 글로벌 파일, 다음으로 리포지토리 루트 `AGENTS.md`, 마지막으로 결제 재정의를 보고합니다.

Codex는 현재 디렉터리에 도달하면 탐색을 멈추므로 전문 작업에 가까운 위치에 재정의를 두세요.

다음은 글로벌 파일과 결제 전용 재정의를 추가한 샘플 리포지토리입니다:

```tsx
<FileTree
  class="mt-4"
  tree={[
    {
      name: "AGENTS.md",
      comment: "Repository expectations",
      highlight: true,
    },
    {
      name: "services/",
      open: true,
      children: [
        {
          name: "payments/",
          open: true,
          children: [
            {
              name: "AGENTS.md",
              comment: "Ignored because an override exists",
            },
            {
              name: "AGENTS.override.md",
              comment: "Payments service rules",
              highlight: true,
            },
            { name: "README.md" },
          ],
        },
        {
          name: "search/",
          children: [{ name: "AGENTS.md" }, { name: "…", placeholder: true }],
        },
      ],
    },
  ]}
/>
```

## 대체 파일명 사용자화

리포지토리에서 이미 다른 파일명(예: `TEAM_GUIDE.md`)을 사용 중이라면, 해당 이름을 대체 목록에 추가해 Codex가 이를 지침 파일로 처리하게 하세요.

1. Codex 설정 편집:

   ```toml
   # ~/.codex/config.toml
   project_doc_fallback_filenames = ["TEAM_GUIDE.md", ".agents.md"]
   project_doc_max_bytes = 65536
   ```

2. Codex를 재시작하거나 새로운 명령을 실행해 업데이트된 설정을 로드하세요.

이제 Codex는 각 디렉터리에서 다음 순서로 확인합니다: `AGENTS.override.md`, `AGENTS.md`, `TEAM_GUIDE.md`, `.agents.md`. 이 목록에 없는 파일명은 무시됩니다. 늘어난 바이트 제한은 잘라내기 전에 더 많은 안내를 허용합니다.

fallback 목록을 설정하면 Codex가 대체 파일을 지침으로 취급합니다:

```tsx
<FileTree
  class="mt-4"
  tree={[
    {
      name: "TEAM_GUIDE.md",
      comment: "Detected via fallback list",
      highlight: true,
    },
    {
      name: ".agents.md",
      comment: "Fallback file in root",
    },
    {
      name: "support/",
      open: true,
      children: [
        {
          name: "AGENTS.override.md",
          comment: "Overrides fallback guidance",
          highlight: true,
        },
        {
          name: "playbooks/",
          children: [{ name: "…", placeholder: true }],
        },
      ],
    },
  ]}
/>
```

다음과 같이 프로젝트별 자동화 계정처럼 다른 프로필을 사용하려면 `CODEX_HOME` 환경 변수를 설정하세요:

```bash
CODEX_HOME=$(pwd)/.codex codex exec "List active instruction sources"
```

예상: 출력에 커스텀 `.codex` 디렉터리 기준으로 파일 목록이 표시됩니다.

## 설정 확인

- 리포지토리 루트에서 `codex --ask-for-approval never "Summarize the current instructions."`를 실행하세요. Codex가 글로벌 및 프로젝트 파일의 안내를 우선순위 순서대로 반복해야 합니다.
- `codex --cd subdir --ask-for-approval never "Show which instruction files are active."`를 사용해 중첩 재정의가 더 넓은 규칙을 대체하는지 확인하세요.
- 세션 후에 `~/.codex/log/codex-tui.log`(또는 세션 로깅을 활성화한 경우 최신 `session-*.jsonl`)을 확인해 Codex가 어떤 지침 파일을 로드했는지 감사하세요.
- 지침이 오래된 것처럼 보이면 대상 디렉터리에서 Codex를 다시 시작하세요. Codex는 실행마다(및 각 TUI 세션 시작 시) 지침 체인을 다시 구성하므로 수동으로 캐시를 비울 필요가 없습니다.

## 탐색 문제 해결

- **아무 것도 로드되지 않음:** 원하는 리포지토리에 있는지 확인하고 `codex status`가 예상 워크스페이스 루트를 보고하는지 확인하세요. Codex는 내용이 있는 파일만 읽습니다.
- **잘못된 안내가 나타남:** 디렉터리 트리 상위나 Codex 홈에 있는 `AGENTS.override.md`를 찾으세요. 재정의를 이름 변경하거나 제거하면 기본 파일로 돌아갑니다.
- **대체 이름을 Codex가 무시함:** 철자가 틀리지 않았는지 `project_doc_fallback_filenames`에 입력했는지 확인한 다음 Codex를 재시작해 설정을 적용하세요.
- **지침이 잘림:** `project_doc_max_bytes`를 높이거나 주요 지침을 중첩 디렉터리에 나누어 보존하세요.
- **프로필 혼동:** Codex 실행 전에 `echo $CODEX_HOME`을 실행하세요. 기본값이 아닌 값은 변경한 홈 디렉터리를 가리킵니다.

## 다음 단계

- 공식 [AGENTS.md](https://agents.md) 웹사이트를 방문해 자세한 정보를 확인하세요.
- 지속적 안내와 잘 맞는 대화 패턴을 보려면 [Prompting Codex](https://developers.openai.com/codex/prompting)를 검토하세요.
