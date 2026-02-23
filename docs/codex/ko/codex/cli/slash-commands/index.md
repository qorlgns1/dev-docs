# Codex CLI의 슬래시 명령

출처 URL: https://developers.openai.com/codex/cli/slash-commands

슬래시 명령은 Codex를 빠르고 키보드 중심으로 제어할 수 있게 합니다. 컴포저에서 `/`를 입력해 슬래시 팝업을 열고 명령을 선택하면, Codex는 터미널을 벗어나지 않고도 모델 전환, 권한 조정, 긴 대화 요약 같은 작업을 수행합니다.

이 가이드는 다음 내용을 다룹니다:

  * 작업에 알맞은 기본 제공 슬래시 명령 찾기
  * `/model`, `/personality`, `/permissions`, `/experimental`, `/agent`, `/status` 등으로 활성 세션을 조정하기



## 기본 제공 슬래시 명령

Codex에는 다음 명령이 포함되어 있습니다. 슬래시 팝업을 열고 명령 이름을 입력해 목록을 필터링하세요.

명령| 목적| 사용 시점  
---|---|---  
[`/permissions`](https://developers.openai.com/codex/cli/slash-commands#update-permissions-with-permissions)| Codex가 사전 승인 없이 수행할 수 있는 작업을 설정합니다.| 세션 도중 Auto와 Read Only 사이를 전환하는 등 승인 요구 수준을 완화하거나 강화할 때.  
[`/sandbox-add-read-dir`](https://developers.openai.com/codex/cli/slash-commands#grant-sandbox-read-access-with-sandbox-add-read-dir)| 샌드박스에 추가 디렉터리 읽기 권한을 부여합니다(Windows 전용).| 현재 읽기 가능 루트 밖의 절대 경로를 읽어야 하는 명령의 차단을 해제할 때.  
[`/agent`](https://developers.openai.com/codex/cli/slash-commands#switch-agent-threads-with-agent)| 활성 에이전트 스레드를 전환합니다.| 생성된 하위 에이전트 스레드에서 작업을 살펴보거나 이어갈 때.  
[`/apps`](https://developers.openai.com/codex/cli/slash-commands#browse-apps-with-apps)| 앱(커넥터)을 찾아보고 프롬프트에 삽입합니다.| Codex에 사용을 요청하기 전에 앱을 `$app-slug`로 첨부할 때.  
[`/compact`](https://developers.openai.com/codex/cli/slash-commands#keep-transcripts-lean-with-compact)| 보이는 대화를 요약해 토큰을 확보합니다.| 긴 실행 이후 컨텍스트 창을 넘기지 않고 Codex가 핵심을 유지하도록 할 때.  
[`/diff`](https://developers.openai.com/codex/cli/slash-commands#review-changes-with-diff)| Git이 아직 추적하지 않는 파일까지 포함해 Git diff를 보여줍니다.| 커밋하거나 테스트하기 전에 Codex의 수정을 검토할 때.  
[`/exit`](https://developers.openai.com/codex/cli/slash-commands#exit-the-cli-with-quit-or-exit)| CLI를 종료합니다(`/quit`과 동일).| 다른 표기일 뿐이며 두 명령 모두 세션을 종료합니다.  
[`/experimental`](https://developers.openai.com/codex/cli/slash-commands#toggle-experimental-features-with-experimental)| 실험적 기능을 전환합니다.| CLI에서 하위 에이전트 같은 선택적 기능을 활성화할 때.  
[`/feedback`](https://developers.openai.com/codex/cli/slash-commands#send-feedback-with-feedback)| Codex 관리 팀에 로그를 보냅니다.| 지원팀에 문제를 보고하거나 진단 정보를 공유할 때.  
[`/init`](https://developers.openai.com/codex/cli/slash-commands#generate-agentsmd-with-init)| 현재 디렉터리에 `AGENTS.md` 스캐폴드를 생성합니다.| 작업 중인 저장소나 하위 디렉터리에 대한 지속 지침을 남길 때.  
[`/logout`](https://developers.openai.com/codex/cli/slash-commands#sign-out-with-logout)| Codex에서 로그아웃합니다.| 공용 기기를 사용할 때 로컬 자격 증명을 지울 때.  
[`/mcp`](https://developers.openai.com/codex/cli/slash-commands#list-mcp-tools-with-mcp)| 구성된 Model Context Protocol(MCP) 도구를 나열합니다.| 세션 중 Codex가 호출할 수 있는 외부 도구를 확인할 때.  
[`/mention`](https://developers.openai.com/codex/cli/slash-commands#highlight-files-with-mention)| 대화에 파일을 첨부합니다.| Codex에 다음으로 살펴볼 특정 파일이나 폴더를 지정할 때.  
[`/model`](https://developers.openai.com/codex/cli/slash-commands#set-the-active-model-with-model)| 활성 모델(가능할 경우 reasoning effort 포함)을 선택합니다.| 작업 실행 전에 범용 모델(`gpt-4.1-mini`)과 고심도 추론 모델 사이를 전환할 때.

[`/plan`](https://developers.openai.com/codex/cli/slash-commands#switch-to-plan-mode-with-plan)| 플랜 모드로 전환하고 필요하면 프롬프트를 함께 보냅니다.| 구현 작업을 시작하기 전에 Codex에게 실행 계획을 제안하도록 요청합니다.  
[`/personality`](https://developers.openai.com/codex/cli/slash-commands#set-a-communication-style-with-personality)| 응답에 사용할 커뮤니케이션 스타일을 선택합니다.| 지침을 바꾸지 않고 Codex가 더 간결하거나 설명적이거나 협업적으로 응답하도록 설정합니다.  
[`/ps`](https://developers.openai.com/codex/cli/slash-commands#check-background-terminals-with-ps)| 실험적 백그라운드 터미널과 최신 출력을 표시합니다.| 주 대화 기록을 떠나지 않고 장시간 실행 중인 명령을 확인합니다.  
[`/fork`](https://developers.openai.com/codex/cli/slash-commands#fork-the-current-conversation-with-fork)| 현재 대화를 새 스레드로 포크합니다.| 활성 세션을 분기해 현재 대화 기록을 잃지 않고 새로운 접근을 탐색합니다.  
[`/resume`](https://developers.openai.com/codex/cli/slash-commands#resume-a-saved-conversation-with-resume)| 세션 목록에서 저장된 대화를 다시 엽니다.| 처음부터 다시 시작하지 않고 이전 CLI 세션에서의 작업을 이어갑니다.  
[`/new`](https://developers.openai.com/codex/cli/slash-commands#start-a-new-conversation-with-new)| 동일한 CLI 세션 안에서 새 대화를 시작합니다.| CLI를 떠나지 않고 동일한 리포지토리에서 새 프롬프트가 필요할 때 대화 맥락을 초기화합니다.  
[`/quit`](https://developers.openai.com/codex/cli/slash-commands#exit-the-cli-with-quit-or-exit)| CLI를 종료합니다.| 세션을 즉시 종료합니다.  
[`/review`](https://developers.openai.com/codex/cli/slash-commands#ask-for-a-working-tree-review-with-review)| Codex에게 작업 트리를 검토해 달라고 요청합니다.| Codex가 작업을 마치거나 로컬 변경 사항에 대해 두 번째 시각이 필요할 때 실행합니다.  
[`/status`](https://developers.openai.com/codex/cli/slash-commands#inspect-the-session-with-status)| 세션 구성과 토큰 사용량을 표시합니다.| 활성 모델, 승인 정책, 쓰기 가능한 루트, 남은 컨텍스트 용량을 확인합니다.  
[`/debug-config`](https://developers.openai.com/codex/cli/slash-commands#inspect-config-layers-with-debug-config)| 구성 레이어와 요구 사항 진단을 출력합니다.| 우선순위와 정책 요구 사항, 실험적 네트워크 제약을 디버그합니다.  
[`/statusline`](https://developers.openai.com/codex/cli/slash-commands#configure-footer-items-with-statusline)| TUI 상태줄 필드를 대화형으로 구성합니다.| 푸터 항목(모델/컨텍스트/제한/깃/토큰/세션)을 선택해 재정렬하고 config.toml에 저장합니다.  
  
`/quit`과 `/exit`는 모두 CLI를 종료합니다. 중요한 작업을 저장하거나 커밋한 뒤에만 사용하세요.

`/approvals` 명령은 여전히 별칭으로 동작하지만, 이제 슬래시 팝업 목록에는 표시되지 않습니다.

## 슬래시 명령으로 세션 제어

다음 워크플로는 Codex를 다시 시작하지 않고도 세션을 올바르게 유지하도록 돕습니다.

### `/model`로 활성 모델 설정

  1. Codex를 시작하고 컴포저를 엽니다.
  2. `/model`을 입력하고 Enter를 누릅니다.
  3. 팝업에서 `gpt-4.1-mini`나 `gpt-4.1`과 같은 모델을 선택합니다.

예상 결과: Codex가 대화에 새 모델을 확인하고, 변경을 검증하려면 `/status`를 실행합니다.

### `/personality`로 커뮤니케이션 스타일 설정

`/personality`를 사용하면 프롬프트를 다시 작성하지 않고 Codex의 대화 방식을 바꿀 수 있습니다.

  1. 활성 대화에서 `/personality`를 입력하고 Enter를 누릅니다.
  2. 팝업에서 원하는 스타일을 선택합니다.

예상 결과: Codex가 대화에 새 스타일을 확인하고 이후 응답에서 이를 적용합니다.

Codex는 `friendly`, `pragmatic`, `none` 퍼스낼리티를 지원합니다. `none`을 사용하면 퍼스낼리티 지침을 비활성화합니다.

활성 모델이 퍼스낼리티별 지침을 지원하지 않으면 Codex가 이 명령을 숨깁니다.

### `/plan`으로 플랜 모드 전환

  1. `/plan`을 입력하고 Enter를 눌러 활성 대화를 플랜 모드로 전환합니다.

2. 선택 사항: 인라인 프롬프트 텍스트를 제공합니다(예: `/plan Propose a migration plan for this service`).
  3. 인라인 `/plan` 인수를 사용하는 동안 콘텐츠를 붙여 넣거나 이미지를 첨부할 수 있습니다.

예상 결과: Codex가 플랜 모드로 들어가며 선택적으로 입력한 인라인 프롬프트를 첫 번째 플랜 요청으로 사용합니다.

작업이 이미 실행 중일 때는 `/plan`을 잠시 사용할 수 없습니다.

### `/experimental`로 실험적 기능 전환

  1. `/experimental`을 입력하고 Enter를 누릅니다.
  2. 원하는 기능(예: **Multi-agents**)을 토글한 뒤 Codex를 다시 시작합니다.

예상 결과: Codex가 선택한 기능 구성을 저장하고 재시작 시 적용합니다.

### `/permissions`로 권한 업데이트

  1. `/permissions`를 입력하고 Enter를 누릅니다.
  2. 편안한 수준에 맞는 승인 프리셋을 선택합니다. 예를 들어 완전 자동 실행에는 `Auto`, 편집 내용을 직접 검토하려면 `Read Only`를 선택합니다.

예상 결과: Codex가 업데이트된 정책을 알리고, 다시 변경할 때까지 이후 동작은 새 승인 모드를 따릅니다.

### `/sandbox-add-read-dir`로 샌드박스 읽기 권한 부여

이 명령은 Windows에서 CLI를 네이티브로 실행할 때만 사용할 수 있습니다.

  1. `/sandbox-add-read-dir C:\absolute\directory\path`를 입력하고 Enter를 누릅니다.
  2. 해당 경로가 존재하는 절대 디렉터리인지 확인합니다.

예상 결과: Codex가 Windows 샌드박스 정책을 새로 고치고, 이후 샌드박스에서 실행되는 명령이 해당 디렉터리를 읽을 수 있게 합니다.

### `/status`로 세션 점검

  1. 어떤 대화에서도 `/status`를 입력합니다.
  2. 활성 모델, 승인 정책, 쓰기 가능한 루트, 현재 토큰 사용량을 출력에서 확인합니다.

예상 결과: 셸에서 `codex status`가 보여 주는 것과 비슷한 요약을 확인하여 Codex가 기대한 환경에서 동작하는지 검증합니다.

### `/debug-config`로 구성 레이어 확인

  1. `/debug-config`를 입력합니다.
  2. 출력에서 구성 레이어 순서(우선순위가 낮은 것부터), 온/오프 상태, 정책 소스를 확인합니다.

예상 결과: Codex가 레이어 진단과 함께 `allowed_approval_policies`, `allowed_sandbox_modes`, `mcp_servers`, `rules`, `enforce_residency`, `experimental_network` 등 구성된 정책 세부정보를 출력합니다.

이 정보를 활용해 실제 설정이 `config.toml`과 다른 이유를 디버깅합니다.

### `/statusline`으로 푸터 항목 구성

  1. `/statusline`을 입력합니다.
  2. 선택기를 사용해 항목을 토글하거나 순서를 조정한 뒤 확인합니다.

예상 결과: 푸터 상태 줄이 즉시 업데이트되며 `config.toml`의 `tui.status_line`에 저장됩니다.

사용 가능한 상태 줄 항목에는 모델, 모델+추론, 컨텍스트 통계, 레이트 제한, Git 브랜치, 토큰 카운터, 세션 ID, 현재 디렉터리/프로젝트 루트, Codex 버전이 포함됩니다.

### `/ps`로 백그라운드 터미널 확인

  1. `/ps`를 입력합니다.
  2. 백그라운드 터미널 목록과 상태를 검토합니다.

예상 결과: Codex가 각 백그라운드 터미널의 명령과 최대 최근 3개의 비어 있지 않은 출력 줄을 보여 주어 진행 상황을 한눈에 파악할 수 있습니다.

`unified_exec`를 사용하는 경우에만 백그라운드 터미널이 나타나며, 그렇지 않으면 목록이 비어 있을 수 있습니다.

### `/compact`으로 대화 압축

  1. 긴 대화 이후 `/compact`를 입력합니다.
  2. Codex가 지금까지의 대화를 요약하겠냐고 묻는다면 확인합니다.

예상 결과: Codex가 이전 턴을 간결한 요약으로 대체하여 중요한 세부정보를 유지하면서 컨텍스트를 확보합니다.

### `/diff`로 변경 사항 검토

  1. 변경 사항을 확인하려면 `/diff`를 입력합니다.
  2. CLI에서 출력되는 내용을 스크롤하며 수정 및 추가된 파일을 검토합니다.

예상 결과: Git에 스테이징한 변경 사항, 아직 스테이징하지 않은 변경 사항, 새로 추적되지 않은 파일을 Codex가 보여 주어 유지할 내용을 결정할 수 있습니다.

### `/mention`으로 파일 강조 표시

  1. `/mention` 다음에 경로를 입력합니다. 예: `/mention src/lib/api.ts`.
  2. 팝업에서 일치 항목을 선택합니다.

예상 결과: Codex가 해당 파일을 대화에 추가하여 후속 턴에서 직접 참조할 수 있게 합니다.

### `/new`로 새 대화 시작

  1. `/new`를 입력하고 Enter를 누릅니다.

예상됨: Codex는 동일한 CLI 세션에서 새 대화를 시작하므로 터미널을 떠나지 않고도 작업을 전환할 수 있습니다.

### `/resume`로 저장된 대화 다시 불러오기

  1. `/resume`를 입력하고 Enter를 누릅니다.
  2. 저장된 세션 선택기에서 원하는 세션을 고릅니다.

예상됨: Codex가 선택한 대화의 전체 기록을 다시 불러와, 원본 히스토리를 유지한 채로 이전 지점부터 이어서 작업할 수 있습니다.

### `/fork`로 현재 대화 분기하기

  1. `/fork`를 입력하고 Enter를 누릅니다.

예상됨: Codex가 현재 대화를 새 ID의 스레드로 복제하여, 원본 기록은 그대로 두고 병렬로 다른 접근을 탐색할 수 있습니다.

저장된 세션을 분기해야 한다면 현재 세션 대신 터미널에서 `codex fork`를 실행해 세션 선택기를 열어 주세요.

### `/init`으로 `AGENTS.md` 생성하기

  1. Codex가 지속 지침을 찾길 원하는 디렉터리에서 `/init`을 실행합니다.
  2. 생성된 `AGENTS.md`를 검토한 뒤, 저장소 규칙에 맞게 수정합니다.

예상됨: Codex가 다듬고 커밋할 수 있는 `AGENTS.md` 골격을 만들어 주므로 이후 세션에서 재사용할 수 있습니다.

### `/review`로 작업 트리 리뷰 요청하기

  1. `/review`를 입력합니다.
  2. 정확한 파일 변경 사항을 보고 싶다면 이어서 `/diff`를 실행합니다.

예상됨: Codex가 작업 트리에서 발견한 이슈를 정리하여 동작 변화와 누락된 테스트에 집중해 알려 줍니다. `config.toml`에서 `review_model`을 설정하지 않았다면 현재 세션 모델을 사용합니다.

### `/mcp`로 MCP 도구 목록 확인하기

  1. `/mcp`를 입력합니다.
  2. 목록을 살펴보고 사용할 수 있는 MCP 서버와 도구를 확인합니다.

예상됨: Codex가 이 세션에서 호출 가능한 Model Context Protocol(MCP) 도구 구성을 보여 줍니다.

### `/apps`로 앱 둘러보기

  1. `/apps`를 입력합니다.
  2. 목록에서 앱을 선택합니다.

예상됨: Codex가 선택한 앱을 `$app-slug` 형태로 작성창에 바로 삽입하므로 즉시 해당 앱 사용을 요청할 수 있습니다.

### `/agent`로 에이전트 스레드 전환하기

  1. `/agent`를 입력하고 Enter를 누릅니다.
  2. 선택기에서 원하는 스레드를 고릅니다.

예상됨: Codex가 활성 스레드를 전환하여 해당 에이전트의 작업을 확인하거나 계속 이어갈 수 있습니다.

### `/feedback`으로 피드백 보내기

  1. `/feedback`을 입력하고 Enter를 누릅니다.
  2. 로그나 진단 정보를 포함하려면 안내에 따라 진행합니다.

예상됨: Codex가 필요한 진단 정보를 수집해 유지관리자에게 전송합니다.

### `/logout`으로 로그아웃하기

  1. `/logout`을 입력하고 Enter를 누릅니다.

예상됨: Codex가 현재 사용자 세션의 로컬 자격 증명을 삭제합니다.

### `/quit` 또는 `/exit`으로 CLI 종료하기

  1. `/quit`(또는 `/exit`)를 입력하고 Enter를 누릅니다.

예상됨: Codex가 즉시 종료됩니다. 종료 전에 중요한 작업을 저장하거나 커밋해 두세요.
