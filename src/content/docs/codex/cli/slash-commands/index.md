---
title: 'Codex CLI의 슬래시 명령어'
description: '슬래시 명령어를 사용하면 Codex를 빠르고 키보드 중심으로 제어할 수 있습니다. 작성기에서 를 입력해 슬래시 팝업을 열고 명령어를 선택하면, Codex가 모델 전환, 권한 조정, 긴 대화 요약 등 터미널을 벗어나지 않고 작업을 수행합니다.'
---

Source URL: https://developers.openai.com/codex/cli/slash-commands

# Codex CLI의 슬래시 명령어

슬래시 명령어를 사용하면 Codex를 빠르고 키보드 중심으로 제어할 수 있습니다. 작성기에서 `/`를 입력해 슬래시 팝업을 열고 명령어를 선택하면, Codex가 모델 전환, 권한 조정, 긴 대화 요약 등 터미널을 벗어나지 않고 작업을 수행합니다.

이 가이드는 다음 내용을 안내합니다:

- 작업에 적합한 기본 제공 슬래시 명령어 찾기
- `/model`, `/personality`, `/permissions`, `/experimental`, `/agent`, `/status` 등의 명령어로 활성 세션 제어하기

## 기본 제공 슬래시 명령어

Codex에는 다음과 같은 명령어들이 포함되어 있습니다. 슬래시 팝업을 열고 명령어 이름을 입력하면 목록을 필터링할 수 있습니다.

| Command                                                                         | Purpose                                                         | When to use it                                                                                            |
| ------------------------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| [`/permissions`](#update-permissions-with-permissions)                          | 질문 없이 Codex가 할 수 있는 작업 범위를 설정합니다.               | Auto와 Read Only를 오가며 세션 중간에 결재 요구사항을 완화하거나 강화할 때.                              |
| [`/sandbox-add-read-dir`](#grant-sandbox-read-access-with-sandbox-add-read-dir) | 추가 디렉터리에 대한 샌드박스 읽기 권한을 부여합니다 (Windows 전용). | 현재 읽기 가능한 루트 바깥에 있는 절대 디렉터리 경로를 읽어야 하는 명령어의 차단을 해제하려 할 때.        |
| [`/agent`](#switch-agent-threads-with-agent)                                    | 활성 에이전트 스레드를 전환합니다.                                | 생성된 서브 에이전트 스레드를 검사하거나 작업을 계속할 때.                                               |
| [`/apps`](#browse-apps-with-apps)                                               | 앱(커넥터)을 찾아서 프롬프트에 삽입합니다.                         | Codex에게 앱 사용을 요청하기 전에 `$app-slug`로 앱을 연결할 때.                                           |
| [`/compact`](#keep-transcripts-lean-with-compact)                               | 보이는 대화를 요약해서 토큰을 절약합니다.                          | 긴 실행 후에도 주요 내용을 유지하면서 컨텍스트 창이 과도하게 커지는 것을 방지하려 할 때.                  |
| [`/diff`](#review-changes-with-diff)                                            | Git diff를 표시하며 Git이 아직 추적하지 않는 파일도 포함합니다.     | 커밋하거나 테스트하기 전에 Codex 편집 내용을 리뷰하려 할 때.                                            |
| [`/exit`](#exit-the-cli-with-quit-or-exit)                                      | CLI를 종료합니다 (`/quit`과 동일).                                | 두 명령어 모두 세션을 종료하므로 작업을 저장하거나 커밋한 뒤 사용합니다.                                  |
| [`/experimental`](#toggle-experimental-features-with-experimental)              | 실험 기능을 토글합니다.                                            | CLI에서 서브 에이전트 같은 선택적 기능을 활성화할 때.                                                     |
| [`/feedback`](#send-feedback-with-feedback)                                     | Codex 유지보수팀에 로그를 전송합니다.                              | 문제를 보고하거나 진단 정보를 공유할 때.                                                                 |
| [`/init`](#generate-agentsmd-with-init)                                         | 현재 디렉터리에 `AGENTS.md` 템플릿을 생성합니다.                   | 작업 중인 리포지토리 또는 하위 디렉터리에 지속적인 지침을 캡처하려 할 때.                                   |
| [`/logout`](#sign-out-with-logout)                                              | Codex에서 로그아웃합니다.                                          | 공유 기기를 사용할 때 로컬 자격증명을 정리하려 할 때.                                                     |
| [`/mcp`](#list-mcp-tools-with-mcp)                                              | 구성된 Model Context Protocol(MCP) 도구를 나열합니다.               | 세션 동안 Codex가 호출할 수 있는 외부 도구를 확인하려 할 때.                                             |
| [`/mention`](#highlight-files-with-mention)                                     | 대화에 파일을 첨부합니다.                                           | Codex가 다음에 검사하길 원하는 특정 파일이나 폴더를 지정할 때.                                           |
| [`/model`](#set-the-active-model-with-model)                                    | 활성 모델(및 가능한 경우 추론 노력)을 선택합니다.                   | 작업을 수행하기 전에 일반 목적 모델(`gpt-4.1-mini`)과 깊은 추론 모델을 오갈 때.                              |
| [`/plan`](#switch-to-plan-mode-with-plan)                                       | 계획 모드로 전환하고 선택적으로 프롬프트를 보냅니다.                 | 구현 작업을 시작하기 전에 Codex에게 실행 계획을 제안하도록 요청할 때.                                     |
| [`/personality`](#set-a-communication-style-with-personality)                   | 응답의 소통 스타일을 설정합니다.                                  | 지침을 바꾸지 않고 Codex를 보다 간결하게, 설명적으로 또는 협력적으로 만들고 싶을 때.                         |
| [`/ps`](#check-background-terminals-with-ps)                                    | 실험적 백그라운드 터미널과 최근 출력 상태를 표시합니다.              | 주요 대화창을 벗어나지 않고 장시간 실행 중인 명령어를 확인할 때.                                          |
| [`/fork`](#fork-the-current-conversation-with-fork)                             | 현재 대화를 새 스레드로 포크합니다.                                 | 활성 세션을 분기하여 현재 기록을 잃지 않고 새로운 접근을 탐색하려 할 때.                                   |
| [`/resume`](#resume-a-saved-conversation-with-resume)                           | 세션 목록에서 저장한 대화를 재개합니다.                              | 이전 CLI 세션을 다시 시작하지 않고 작업을 계속하려 할 때.                                                 |
| [`/new`](#start-a-new-conversation-with-new)                                    | 같은 CLI 세션 내에서 새 대화를 시작합니다.                           | 동일한 리포에서 새 프롬프트로 채팅 컨텍스트를 리셋하려 할 때.                                               |
| [`/quit`](#exit-the-cli-with-quit-or-exit)                                      | CLI를 종료합니다.                                                   | 세션을 즉시 종료합니다.                                                                                  |
| [`/review`](#ask-for-a-working-tree-review-with-review)                         | Codex에게 작업 트리를 리뷰해 달라고 요청합니다.                        | Codex가 작업을 완료한 후나 로컬 변경 사항에 다른 눈을 더하고 싶을 때 실행합니다.                            |
| [`/status`](#inspect-the-session-with-status)                                   | 세션 구성과 토큰 사용량을 표시합니다.                                | 활성 모델, 승인 정책, 쓰기 가능한 루트, 남은 컨텍스트 용량을 확인할 때.                                   |
| [`/debug-config`](#inspect-config-layers-with-debug-config)                     | 구성 계층 및 요구 사항 진단을 출력합니다.                              | 우선순위와 정책 요구 사항, 실험적 네트워크 제한 등을 디버그할 때.                                          |
| [`/statusline`](#configure-footer-items-with-statusline)                        | TUI 상태줄 항목을 대화형으로 구성합니다.                              | 푸터 항목(모델/컨텍스트/제한/깃/토큰/세션 등)을 선택하고 순서를 정한 뒤 `config.toml`에 영구 저장합니다.    |

`/quit`과 `/exit`은 모두 CLI를 종료합니다. 중요한 작업은 저장하거나 커밋한 뒤에만 사용하세요.

`/approvals` 명령도 여전히 작동하지만 슬래시 팝업 목록에는 더 이상 표시되지 않습니다.

## 슬래시 명령어로 세션 제어하기

다음 워크플로우는 Codex를 다시 시작하지 않고도 세션을 관리할 수 있게 해줍니다.

### `/model`로 활성 모델 설정하기

1. Codex를 시작하고 작성기를 엽니다.
2. `/model`을 입력하고 Enter 키를 누릅니다.
3. 팝업에서 `gpt-4.1-mini` 또는 `gpt-4.1` 같은 모델을 선택합니다.

예상 결과: Codex가 대화에 새로운 모델을 확인합니다. `/status`를 실행해 변경 사항을 확인하세요.

### `/personality`로 소통 스타일 설정하기

프롬프트를 다시 작성하지 않고 Codex의 소통 방식을 바꾸려면 `/personality`를 사용하세요.

1. 활성 대화에서 `/personality`를 입력하고 Enter 키를 누릅니다.
2. 팝업에서 스타일을 선택합니다.

예상 결과: Codex가 대화에서 새 스타일을 확인하고 이후 응답에 이를 반영합니다.

Codex는 `friendly`, `pragmatic`, `none` 성격을 지원합니다. `none`을 선택하면 성격 지시를 끕니다.

활성 모델이 성격 특정 지시를 지원하지 않으면 명령어가 숨겨집니다.

### `/plan`으로 계획 모드로 전환하기

1. `/plan`을 입력하고 Enter 키를 눌러 활성 대화를 계획 모드로 전환합니다.
2. 선택 사항: `/plan Propose a migration plan for this service`처럼 인라인 프롬프트 텍스트를 제공합니다.
3. 인라인 `/plan` 인수와 함께 콘텐츠를 붙여넣거나 이미지를 첨부할 수 있습니다.

예상 결과: Codex가 계획 모드에 들어가고 선택적으로 제공한 인라인 프롬프트를 첫 번째 계획 요청으로 사용합니다.

이미 작업이 진행 중일 때 `/plan`은 일시적으로 사용할 수 없습니다.

### `/experimental`로 실험 기능 토글하기

1. `/experimental`을 입력하고 Enter 키를 누릅니다.
2. 원하는 기능(예: **Multi-agents**)을 토글한 다음 Codex를 다시 시작합니다.

예상 결과: Codex가 구성에 기능 선택을 저장하고 재시작 후 적용합니다.

### `/permissions`로 권한 업데이트하기

1. `/permissions`를 입력하고 Enter 키를 누릅니다.
2. `Auto`처럼 자동 실행을 위한 설정이나 `Read Only`처럼 편집을 검토하기 위한 승인 사전 설정을 선택합니다.

예상 결과: Codex가 업데이트된 정책을 알립니다. 이후 작업은 다시 변경할 때까지 새로운 승인 모드를 따릅니다.

### `/sandbox-add-read-dir`로 샌드박스 읽기 권한 부여하기

이 명령어는 Windows에서 CLI를 직접 실행할 때만 사용할 수 있습니다.

1. `/sandbox-add-read-dir C:\absolute\directory\path`를 입력하고 Enter 키를 누릅니다.
2. 경로가 존재하는 절대 디렉터리인지 확인합니다.

예상 결과: Codex가 Windows 샌드박스 정책을 새로 고치고 이후 샌드박스에서 실행되는 명령어가 해당 디렉터리를 읽을 수 있도록 권한을 부여합니다.

### `/status`로 세션 검사하기

1. 어느 대화에서든 `/status`를 입력합니다.
2. 활성 모델, 승인 정책, 쓰기 가능한 루트, 현재 토큰 사용량 출력을 검토합니다.

예상 결과: `codex status`가 셸에 출력하는 요약과 비슷한 내용을 보고 Codex가 예상 위치에서 작동하고 있는지 확인합니다.

### `/debug-config`로 구성 계층 검사하기

1. `/debug-config`를 입력합니다.
2. 출력된 구성 계층 순서(낮은 우선순위부터), 활성/비활성 상태, 정책 소스를 검토합니다.

예상 결과: Codex가 계층 진단과 함께 `allowed_approval_policies`, `allowed_sandbox_modes`, `mcp_servers`, `rules`, `enforce_residency`, `experimental_network` 같은 정책 세부정보를 구성에 따라 출력합니다.

이 출력을 사용해 `config.toml`과 다른 방식으로 작동하는 설정을 디버그합니다.

### `/statusline`로 푸터 항목 구성하기

1. `/statusline`을 입력합니다.
2. 선택기에서 항목을 토글하고 순서를 바꾼 다음 확인합니다.

예상 결과: 푸터 상태줄이 즉시 업데이트되며 `config.toml`의 `tui.status_line`에 저장됩니다.

사용 가능한 상태줄 항목에는 모델, 모델+추론, 컨텍스트 통계, 속도 제한, Git 브랜치, 토큰 카운터, 세션 ID, 현재 디렉터리/프로젝트 루트, Codex 버전 등이 포함됩니다.

### `/ps`로 백그라운드 터미널 확인하기

1. `/ps`를 입력합니다.
2. 백그라운드 터미널 목록과 상태를 검토합니다.

기대: Codex가 각 백그라운드 터미널의 명령과 최대 세 줄의 최근 비어 있지 않은 출력만 표시하여 진행 상황을 한눈에 파악할 수 있도록 합니다.

`unified_exec`를 사용할 때 백그라운드 터미널이 나타납니다. 그렇지 않으면 목록이 비어 있을 수 있습니다.

### `/compact`으로 기록 간결하게 유지

1. 긴 대화가 끝난 뒤 `/compact`를 입력합니다.
2. Codex가 지금까지의 대화를 요약해주겠다고 제안하면 확인합니다.

기대: Codex가 이전 턴을 간결한 요약으로 대체하여 핵심 정보를 유지하면서 컨텍스트 공간을 확보합니다.

### `/diff`로 변경 내용 검토

1. `/diff`를 입력하여 Git diff를 확인합니다.
2. CLI 내부에서 출력 내용을 스크롤하며 편집 및 추가된 파일을 살펴봅니다.

기대: Codex가 스테이징한 변경, 아직 스테이징하지 않은 변경, Git이 아직 추적하지 않은 파일을 모두 표시하여 유지할 내용을 결정할 수 있도록 합니다.

### `/mention`으로 파일 강조

1. `/mention src/lib/api.ts`처럼 `/mention` 뒤에 경로를 입력합니다.
2. 팝업에서 일치하는 결과를 선택합니다.

기대: Codex가 해당 파일을 대화에 추가하여 이후 턴에서 직접 참조할 수 있도록 합니다.

### `/new`로 새 대화 시작

1. `/new`를 입력하고 Enter를 누릅니다.

기대: Codex가 동일한 CLI 세션에서 새로운 대화를 시작하여 터미널을 벗어나지 않고도 작업 전환이 가능합니다.

### `/resume`로 저장된 대화 이어서 사용

1. `/resume`를 입력하고 Enter를 누릅니다.
2. 저장된 세션 선택기에서 원하는 세션을 선택합니다.

기대: Codex가 선택한 대화 기록을 다시 로드하여 원래의 기록을 유지하면서 이어서 작업할 수 있게 합니다.

### `/fork`로 현재 대화 분기

1. `/fork`를 입력하고 Enter를 누릅니다.

기대: Codex가 현재 대화를 새로운 ID의 새 스레드로 복제하여 원본 기록은 그대로 두고 병렬로 다른 접근을 탐색할 수 있게 합니다.

저장된 세션을 분기하려면 터미널에서 `codex fork`를 실행하여 세션 선택기를 열면 됩니다.

### `/init`으로 `AGENTS.md` 생성

1. Codex가 지속 지침을 찾을 디렉터리에서 `/init`을 실행합니다.
2. 생성된 `AGENTS.md`를 검토한 뒤 리포지터리 규칙에 맞게 수정합니다.

기대: Codex가 향후 세션을 위해 정제 및 커밋할 수 있는 `AGENTS.md` 기본 틀을 생성합니다.

### `/review`로 작업 트리 검토 요청

1. `/review`를 입력합니다.
2. 구체적인 파일 변경을 확인하려면 이어서 `/diff`를 사용합니다.

기대: Codex가 작업 트리에서 발견한 문제를 요약하며, 동작 변경 및 누락된 테스트에 중점을 둡니다. `config.toml`에서 `review_model`을 설정하지 않았다면 현재 세션 모델을 사용합니다.

### `/mcp`로 MCP 도구 목록 보기

1. `/mcp`를 입력합니다.
2. 사용 가능한 MCP 서버 및 도구 목록을 확인합니다.

기대: 현재 세션에서 Codex가 호출할 수 있는 Model Context Protocol 도구들을 확인할 수 있습니다.

### `/apps`로 앱 탐색

1. `/apps`를 입력합니다.
2. 목록에서 앱을 선택합니다.

기대: Codex가 작곡기 창에 `$app-slug` 형태로 앱 언급을 삽입하여 바로 Codex에게 해당 앱을 사용하도록 요청할 수 있습니다.

### `/agent`로 에이전트 스레드 전환

1. `/agent`를 입력하고 Enter를 누릅니다.
2. 선택기에서 원하는 스레드를 선택합니다.

기대: Codex가 활성 스레드를 전환하여 해당 에이전트의 작업을 살펴보거나 계속할 수 있게 합니다.

### `/feedback`로 피드백 전송

1. `/feedback`을 입력하고 Enter를 누릅니다.
2. 로그나 진단 정보를 포함하도록 안내에 따라 입력합니다.

기대: Codex가 요청된 진단 정보를 수집하여 유지보수 담당자에게 제출합니다.

### `/logout`으로 로그아웃

1. `/logout`을 입력하고 Enter를 누릅니다.

기대: Codex가 현재 사용자 세션의 로컬 자격 증명을 삭제합니다.

### `/quit` 또는 `/exit`로 CLI 종료

1. `/quit`(또는 `/exit`)를 입력하고 Enter를 누릅니다.

기대: Codex가 즉시 종료합니다. 중요 작업은 먼저 저장하거나 커밋해야 합니다.
