---
title: AGENTS.md와 함께하는 맞춤 지침
description: Codex는 어떤 작업을 시작하기 전에  파일을 읽습니다. 전역 지침과 프로젝트별 오버라이드를 겹겹이 쌓으면, 어떤 저장소를 열어도 일관된 기대치를 갖고 각 작업을 시작할 수 있습니다.
sidebar:
  order: 1
---

# AGENTS.md와 함께하는 맞춤 지침

Source URL: https://developers.openai.com/codex/guides/agents-md

Codex는 어떤 작업을 시작하기 전에 `AGENTS.md` 파일을 읽습니다. 전역 지침과 프로젝트별 오버라이드를 겹겹이 쌓으면, 어떤 저장소를 열어도 일관된 기대치를 갖고 각 작업을 시작할 수 있습니다.

## Codex가 지침을 찾는 방법

Codex는 시작 시(실행마다 한 번, TUI에서는 세션당 한 번) 지침 체인을 구성합니다. 검색 순서는 다음 우선순위를 따릅니다.

  1. **전역 범위:** Codex 홈 디렉터리(기본값 `~/.codex`, 또는 `CODEX_HOME` 설정값)에 있는 `AGENTS.override.md`가 존재하면 그 파일을, 없으면 `AGENTS.md`를 읽습니다. 이 수준에서는 처음으로 비어 있지 않은 파일 하나만 사용합니다.
  2. **프로젝트 범위:** 프로젝트 루트(일반적으로 Git 루트)에서 시작해 현재 작업 디렉터리까지 내려갑니다. 프로젝트 루트를 찾지 못하면 현재 디렉터리만 확인합니다. 경로상의 각 디렉터리에서 `AGENTS.override.md`, `AGENTS.md`, 그리고 `project_doc_fallback_filenames`에 지정된 예비 이름 순으로 확인하며, 디렉터리마다 최대 한 파일만 포함합니다.
  3. **병합 순서:** 루트에서 시작해 아래로 내려오면서 파일을 빈 줄로 이어 붙입니다. 현재 디렉터리에 가까운 파일이 더 뒤에 나타나므로 앞선 지침을 덮어씁니다.

Codex는 비어 있는 파일을 건너뛰며, 합쳐진 크기가 `project_doc_max_bytes`(기본 32 KiB) 한도에 도달하면 추가 파일을 멈춥니다. 이 설정에 대한 자세한 내용은 [Project instructions discovery](https://developers.openai.com/codex/config-advanced#project-instructions-discovery)를 참고하세요. 한도에 걸리면 제한을 높이거나 하위 디렉터리로 지침을 분할하세요.

## 전역 지침 만들기

모든 저장소가 기본 작업 합의를 상속하도록 Codex 홈 디렉터리에 지속적인 기본값을 만드세요.

  1. 디렉터리가 존재하는지 확인합니다:
[code] mkdir -p ~/.codex
[/code]

  2. 재사용 가능한 환경설정을 담은 `~/.codex/AGENTS.md`를 작성합니다:
[code] # ~/.codex/AGENTS.md
         
         ## Working agreements
         
         - Always run `npm test` after modifying JavaScript files.
         - Prefer `pnpm` when installing dependencies.
         - Ask for confirmation before adding new production dependencies.
[/code]

  3. 어떤 위치에서든 Codex를 실행해 파일이 로드되는지 확인합니다:
[code] codex --ask-for-approval never "Summarize the current instructions."
[/code]

예상 결과: Codex가 작업을 제안하기 전에 `~/.codex/AGENTS.md`에 있는 항목을 인용합니다.

`~/.codex/AGENTS.override.md`를 사용하면 기본 파일을 삭제하지 않고 임시 전역 오버라이드를 적용할 수 있습니다. 공유 지침을 복원하려면 오버라이드를 제거하세요.

## 프로젝트 지침 계층화

저장소 단위 파일은 전역 기본값을 상속하면서도 Codex가 프로젝트 규범을 인지하도록 유지합니다.

  1. 저장소 루트에 기본 설정을 다루는 `AGENTS.md`를 추가합니다:
[code] # AGENTS.md
         
         ## Repository expectations
         
         - Run `npm run lint` before opening a pull request.
         - Document public utilities in `docs/` when you change behavior.
[/code]

  2. 특정 팀에 다른 규칙이 필요할 때 하위 디렉터리에 오버라이드를 추가합니다. 예를 들어 `services/payments/` 내부에 `AGENTS.override.md`를 생성합니다:
[code] # services/payments/AGENTS.override.md
         
         ## Payments service rules
         
         - Use `make test-payments` instead of `npm test`.
         - Never rotate API keys without notifying the security channel.
[/code]

  3. payments 디렉터리에서 Codex를 시작합니다:
[code] codex --cd services/payments --ask-for-approval never "List the instruction sources you loaded."
[/code]

예상 결과: Codex가 전역 파일을 먼저, 저장소 루트의 `AGENTS.md`를 두 번째, payments 오버라이드를 마지막으로 보고합니다.

Codex는 현재 디렉터리에 도달하면 검색을 멈추므로, 특화된 작업에는 가능한 한 가까운 위치에 오버라이드를 배치하세요.

전역 파일과 결제 전용 오버라이드를 추가한 뒤의 샘플 리포지토리는 다음과 같습니다:

  * AGENTS.md  리포지토리 기대사항

  * services/

    * payments/

      * AGENTS.md  오버라이드가 존재하므로 무시됨

      * AGENTS.override.md  결제 서비스 규칙

      * README.md

    * search/

      * AGENTS.md

      * …

## 폴백 파일 이름 사용자 지정

이미 다른 파일 이름(예: `TEAM_GUIDE.md`)을 사용하는 리포지토리라면, 폴백 목록에 추가하여 Codex가 지침 파일로 인식하도록 하세요.

  1. Codex 구성을 편집합니다:
[code] # ~/.codex/config.toml
         project_doc_fallback_filenames = ["TEAM_GUIDE.md", ".agents.md"]
         project_doc_max_bytes = 65536
[/code]

  2. 업데이트된 구성이 로드되도록 Codex를 재시작하거나 새 명령을 실행합니다.

이제 Codex는 각 디렉터리를 `AGENTS.override.md`, `AGENTS.md`, `TEAM_GUIDE.md`, `.agents.md` 순서로 확인합니다. 이 목록에 없는 파일 이름은 지침 발견 대상으로 무시됩니다. 더 큰 바이트 제한 덕분에 잘리지 않고 더 많은 지침을 결합해 둘 수 있습니다.

폴백 목록을 구성하면 Codex가 대체 파일도 지침으로 취급합니다:

  * TEAM_GUIDE.md  폴백 목록을 통해 감지됨

  * .agents.md  루트의 폴백 파일

  * support/

    * AGENTS.override.md  폴백 지침을 대체

    * playbooks/

      * …

다른 프로필(예: 프로젝트 전용 자동화 사용자)이 필요할 때는 `CODEX_HOME` 환경 변수를 설정하세요:
[code] 
    CODEX_HOME=$(pwd)/.codex codex exec "List active instruction sources"
[/code]

예상 결과: 출력에는 사용자 지정 `.codex` 디렉터리를 기준으로 한 파일 경로가 표시됩니다.

## 설정 확인

  * 리포지토리 루트에서 `codex --ask-for-approval never "Summarize the current instructions."`를 실행합니다. Codex는 전역 및 프로젝트 파일의 지침을 우선순위대로 출력해야 합니다.
  * `codex --cd subdir --ask-for-approval never "Show which instruction files are active."`를 사용해 하위 디렉터리의 오버라이드가 상위 규칙을 대체하는지 확인합니다.
  * 세션 후 감사가 필요하면 `~/.codex/log/codex-tui.log`(또는 세션 로깅을 켰다면 최신 `session-*.jsonl`)을 확인하여 Codex가 어떤 지침 파일을 로드했는지 살펴보세요.
  * 지침이 오래된 것처럼 보이면 대상 디렉터리에서 다시 Codex를 시작하세요. Codex는 실행마다(및 각 TUI 세션 시작 시) 지침 체인을 다시 구축하므로 수동으로 캐시를 비울 필요가 없습니다.

## 발견 문제 해결

  * **아무것도 로드되지 않음:** 현재 리포지토리가 맞는지, `codex status`가 기대한 워크스페이스 루트를 보고하는지 확인하세요. 지침 파일에 내용이 있는지도 점검하세요. 빈 파일은 무시됩니다.
  * **잘못된 지침 표시:** 디렉터리 트리 상위나 Codex 홈 아래에 `AGENTS.override.md`가 있는지 찾으세요. 기본 파일로 돌아가려면 해당 오버라이드를 이름 변경하거나 제거하세요.
  * **폴백 이름을 Codex가 무시함:** `project_doc_fallback_filenames`에 오탈자 없이 이름을 넣었는지 확인한 뒤, 변경 사항을 적용하려면 Codex를 재시작하세요.
  * **지침이 잘림:** `project_doc_max_bytes` 값을 높이거나 중요한 지침을 중첩 디렉터리로 나눠 보존하세요.
  * **프로필 혼동:** Codex를 실행하기 전에 `echo $CODEX_HOME`을 실행하세요. 기본이 아닌 값이라면 수정한 홈 디렉터리와 다른 곳을 가리키고 있을 수 있습니다.

## 다음 단계

  * 공식 [AGENTS.md](https://agents.md) 웹사이트에서 추가 정보를 확인하세요.
  * [Prompting Codex](https://developers.openai.com/codex/prompting)를 검토하여 지속적인 지침과 잘 맞는 대화 패턴을 익히세요.
