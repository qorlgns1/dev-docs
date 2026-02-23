# 보안

Source URL: https://developers.openai.com/codex/security

Codex는 코드와 데이터를 보호하고 오용 위험을 낮추는 데 도움을 줍니다.

기본적으로 에이전트는 네트워크 액세스가 꺼진 상태로 실행됩니다. 로컬에서는 Codex가 OS에서 강제하는 샌드박스를 사용하여 접근 범위를 제한하며(일반적으로 현재 워크스페이스), 행동 전에 중단하고 확인을 요청해야 하는 시점을 제어하는 승인 정책이 함께 적용됩니다.

## 샌드박스와 승인

Codex 보안 제어는 함께 동작하는 두 가지 계층에서 제공됩니다.

  * **Sandbox mode** : 모델이 생성한 명령을 실행할 때 Codex가 기술적으로 할 수 있는 작업(예: 작성 가능한 위치, 네트워크 도달 여부)을 정의합니다.
  * **Approval policy** : Codex가 어떤 행동을 실행하기 전에 사용자의 승인을 받아야 하는 시점(예: 샌드박스 이탈, 네트워크 사용, 신뢰된 집합 밖의 명령 실행)을 규정합니다.



Codex는 실행 위치에 따라 서로 다른 샌드박스 모드를 사용합니다.

  * **Codex cloud** : OpenAI가 관리하는 격리된 컨테이너에서 실행되어 호스트 시스템이나 무관한 데이터에 접근하지 못하도록 합니다. 필요할 경우(예: 종속성 설치, 특정 도메인 허용) 의도적으로 접근 범위를 확장할 수 있습니다. 코드에 접근하기 전 실행되는 설정 단계에서는 네트워크 액세스가 항상 활성화됩니다.
  * **Codex CLI / IDE extension** : OS 수준 메커니즘이 샌드박스 정책을 강제합니다. 기본값은 네트워크 액세스 비활성화와 활성 워크스페이스로 제한된 쓰기 권한입니다. 위험 허용도에 맞춰 샌드박스, 승인 정책, 네트워크 설정을 구성할 수 있습니다.



`Auto` 프리셋(예: `--full-auto`)에서는 Codex가 작업 디렉터리에서 파일을 읽고, 수정하고, 명령을 자동으로 실행할 수 있습니다.

워크스페이스 밖의 파일을 수정하거나 네트워크 액세스가 필요한 명령을 실행할 때는 Codex가 승인을 요청합니다. 변경 없이 대화하거나 계획만 세우려면 `/permissions` 명령으로 `read-only` 모드로 전환하십시오.

Codex는 셸 명령이나 파일 변경이 아닌 앱(커넥터) 도구 호출이라도 부작용이 있다고 표시되면 승인을 요청할 수 있습니다.

## 네트워크 액세스 [ Elevated Risk ](https://help.openai.com/articles/20001061)

Codex cloud에서는 [agent internet access](https://developers.openai.com/codex/cloud/internet-access)를 참고해 전체 인터넷 액세스나 도메인 허용 목록을 활성화하십시오.

Codex 앱, CLI, IDE Extension에서는 기본 `workspace-write` 샌드박스 모드가 설정에서 활성화하지 않는 한 네트워크 액세스를 꺼 둡니다:
[code] 
    [sandbox_workspace_write]
    network_access = true
[/code]

전체 네트워크 액세스를 부여하지 않고도 [web search tool](https://platform.openai.com/docs/guides/tools-web-search)을 제어할 수 있습니다. Codex는 결과에 접근할 때 기본적으로 웹 검색 캐시를 사용합니다. 이 캐시는 OpenAI가 관리하는 웹 결과 인덱스로, 캐시 모드에서는 실시간 페이지를 가져오는 대신 사전 색인된 결과를 반환합니다. 이는 임의의 실시간 콘텐츠에서 오는 프롬프트 인젝션 노출을 줄이지만, 웹 결과는 여전히 신뢰하지 않는 것이 좋습니다. `--yolo` 또는 다른 [full access sandbox setting](https://developers.openai.com/codex/security#common-sandbox-and-approval-combinations)을 사용할 경우 웹 검색 기본값이 실시간 결과가 됩니다. 실시간 탐색을 허용하려면 `--search`를 사용하거나 `web_search = "live"`로 설정하고, 도구를 끄려면 `"disabled"`로 설정하십시오:
[code] 
    web_search = "cached"  # default
    # web_search = "disabled"
    # web_search = "live"  # same as --search
[/code]

Codex에서 네트워크 액세스나 웹 검색을 활성화할 때는 주의하십시오. 프롬프트 인젝션이 에이전트로 하여금 신뢰할 수 없는 지시를 가져오고 따르도록 만들 수 있습니다.

## 기본값과 권장 사항

  * 시작 시 Codex는 폴더가 버전 관리되는지 감지하고 다음을 권장합니다.
    * 버전 관리된 폴더: `Auto` (workspace write + 요청 시 승인)
    * 버전 미관리 폴더: `read-only`
  * 설정에 따라 Codex는 작업 디렉터리를 명시적으로 신뢰할 때까지(예: 온보딩 프롬프트 또는 `/permissions`를 통해) `read-only`로 시작할 수도 있습니다.

* 작업 공간에는 현재 디렉터리와 `/tmp`와 같은 임시 디렉터리가 포함됩니다. 작업 공간에 어떤 디렉터리가 포함되어 있는지 확인하려면 `/status` 명령을 사용하세요.
  * 기본값을 그대로 사용하려면 `codex`를 실행하세요.
  * 다음과 같이 명시적으로 설정할 수 있습니다: 
    * `codex --sandbox workspace-write --ask-for-approval on-request`
    * `codex --sandbox read-only --ask-for-approval on-request`



### 쓰기 가능 루트의 보호 경로

기본 `workspace-write` 샌드박스 정책에서도 쓰기 가능 루트에는 여전히 보호 경로가 포함됩니다:

  * `<writable_root>/.git`은 디렉터리이든 파일이든 관계없이 읽기 전용으로 보호됩니다.
  * `<writable_root>/.git`이 포인터 파일(`gitdir: ...`)인 경우, 해석된 Git 디렉터리 경로 역시 읽기 전용으로 보호됩니다.
  * `<writable_root>/.agents`가 디렉터리로 존재하면 읽기 전용으로 보호됩니다.
  * `<writable_root>/.codex`가 디렉터리로 존재하면 읽기 전용으로 보호됩니다.
  * 보호는 재귀적으로 적용되어 해당 경로 아래의 모든 항목이 읽기 전용입니다.



### 승인 프롬프트 없이 실행

승인 프롬프트는 `--ask-for-approval never` 또는 약식 `-a never`로 비활성화할 수 있습니다.

이 옵션은 모든 `--sandbox` 모드에서 동작하므로 Codex의 자율성 수준은 여전히 사용자가 제어합니다. Codex는 사용자가 설정한 제약 내에서 최선을 다합니다.

Codex가 승인 요청 없이 파일을 읽고, 수정하고, 네트워크 액세스가 필요한 명령을 실행해야 한다면 `--sandbox danger-full-access`(또는 `--dangerously-bypass-approvals-and-sandbox` 플래그)를 사용하세요. 사용 전 주의가 필요합니다.

### 일반적인 샌드박스와 승인 조합

의도| 플래그| 효과  
---|---|---  
Auto (기본값)| _플래그 불필요_ 또는 `--full-auto`| Codex가 워크스페이스에서 파일을 읽고, 수정하고, 명령을 실행할 수 있습니다. 워크스페이스 밖을 수정하거나 네트워크에 접근하려면 승인이 필요합니다.  
안전한 읽기 전용 탐색| `--sandbox read-only --ask-for-approval on-request`| Codex가 파일을 읽고 질문에 답할 수 있습니다. 수정, 명령 실행, 네트워크 접근에는 승인이 필요합니다.  
읽기 전용 비대화식(CI)| `--sandbox read-only --ask-for-approval never`| Codex가 파일만 읽을 수 있으며 승인 요청을 하지 않습니다.  
자동 수정 + 신뢰되지 않은 명령 승인 필요| `--sandbox workspace-write --ask-for-approval untrusted`| Codex가 파일을 읽고 수정할 수 있지만, 신뢰되지 않은 명령을 실행하기 전에는 승인을 요청합니다.  
위험한 전체 액세스| `--dangerously-bypass-approvals-and-sandbox` (별칭: `--yolo`)| [위험 상승](https://help.openai.com/articles/20001061) 샌드박스 없음; 승인 없음 _(권장되지 않음)_  
  
`--full-auto`는 `--sandbox workspace-write --ask-for-approval on-request`의 편의용 별칭입니다.

`--ask-for-approval untrusted`를 사용하면 Codex는 알려진 안전한 읽기 작업만 자동으로 실행합니다. 상태를 변경하거나 외부 실행 경로를 트리거할 수 있는 명령(예: 파괴적인 Git 작업 또는 Git 출력/설정 덮어쓰기 플래그)은 승인이 필요합니다.

#### `config.toml`에서의 구성

더 폭넓은 구성 워크플로는 [구성 기본](https://developers.openai.com/codex/config-basic), [고급 구성](https://developers.openai.com/codex/config-advanced#approval-policies-and-sandbox-modes), [구성 레퍼런스](https://developers.openai.com/codex/config-reference)를 참조하세요.
[code] 
    # Always ask for approval mode
    approval_policy = "untrusted"
    sandbox_mode    = "read-only"
    
    # Optional: Allow network in workspace-write mode
    [sandbox_workspace_write]
    network_access = true
[/code]

프리셋을 프로파일로 저장한 뒤 `codex --profile <name>`으로 불러올 수도 있습니다:
[code] 
    [profiles.full_auto]
    approval_policy = "on-request"
    sandbox_mode    = "workspace-write"
    
    [profiles.readonly_quiet]
    approval_policy = "never"
    sandbox_mode    = "read-only"
[/code]

### 로컬에서 샌드박스를 테스트

Codex 샌드박스에서 명령이 실행될 때 어떤 일이 발생하는지 확인하려면 다음 Codex CLI 명령을 사용하세요:
[code] 
    # macOS
    codex sandbox macos [--full-auto] [--log-denials] [COMMAND]...
    # Linux
[/code]

codex sandbox linux [--full-auto] [COMMAND]...
[/code]

`sandbox` 명령은 `codex debug` 이름으로도 제공되며, 플랫폼 헬퍼에도 별칭이 있습니다(예: `codex sandbox seatbelt`, `codex sandbox landlock`).

## OS-level sandbox

Codex는 사용하는 OS에 따라 샌드박스를 다르게 적용합니다:

  * **macOS**: Seatbelt 정책을 사용하며, 선택한 `--sandbox` 모드에 해당하는 프로필(`-p`)을 붙인 `sandbox-exec`으로 명령을 실행합니다.
  * **Linux**: 기본적으로 `Landlock`과 `seccomp`를 함께 사용합니다. 대체 Linux 샌드박스 파이프라인을 사용하려면 `features.use_linux_sandbox_bwrap = true`(또는 `-c use_linux_sandbox_bwrap=true`)로 옵트인하십시오.
  * **Windows**: [Windows Subsystem for Linux (WSL)](https://developers.openai.com/codex/windows#windows-subsystem-for-linux)에서 실행할 때는 Linux 샌드박스 구현을 사용합니다. Windows에 네이티브로 실행할 때는 [experimental sandbox](https://developers.openai.com/codex/windows#windows-experimental-sandbox)를 활성화할 수 있습니다.



Codex IDE 확장을 Windows에서 사용할 경우 WSL을 직접 지원합니다. WSL이 있을 때마다 에이전트가 그 안에 머무르도록 VS Code 설정에 다음을 지정하세요:
[code] 
    {
      "chatgpt.runCodexInWindowsSubsystemForLinux": true
    }
[/code]

이렇게 하면 호스트 OS가 Windows일 때도 IDE 확장이 명령, 승인, 파일 시스템 접근에 대해 Linux 샌드박스 의미 체계를 상속합니다. 자세한 내용은 [Windows setup guide](https://developers.openai.com/codex/windows)를 참조하십시오.

네이티브 Windows 샌드박스는 실험적이며 중요한 제한이 있습니다. 예를 들어 `Everyone` SID에 이미 쓰기 권한이 있는 디렉터리(예: 모든 사용자가 쓸 수 있는 폴더)에서는 쓰기를 차단할 수 없습니다. 세부 사항과 완화 단계는 [Windows setup guide](https://developers.openai.com/codex/windows#windows-experimental-sandbox)에서 확인하세요.

Docker 같은 컨테이너 환경에서 Linux를 실행할 때 호스트나 컨테이너 설정이 필요한 `Landlock` 및 `seccomp` 기능을 지원하지 않으면 샌드박스가 동작하지 않을 수 있습니다.

그 경우에는 필요한 격리를 제공하도록 Docker 컨테이너를 구성한 뒤, 컨테이너 내부에서 `--sandbox danger-full-access`(또는 `--dangerously-bypass-approvals-and-sandbox`) 플래그와 함께 `codex`를 실행하세요.

## Version control

Codex는 다음과 같은 버전 관리 워크플로에서 가장 잘 동작합니다:

  * 기능 브랜치에서 작업하고 위임 전에 `git status`를 깨끗하게 유지하세요. 이렇게 하면 Codex 패치를 분리하고 되돌리기 쉽습니다.
  * 추적 중인 파일을 직접 편집하기보다 `git diff`/`git apply` 같은 패치 기반 워크플로를 선호하세요. 자주 커밋해 작은 단위로 롤백할 수 있게 하십시오.
  * Codex 제안을 다른 PR처럼 다루세요: 대상 검증을 실행하고, diff를 검토하며, 감사를 위해 커밋 메시지에 결정을 기록합니다.



## Monitoring and telemetry

Codex는 OpenTelemetry(OTel)를 통한 옵트인 모니터링을 지원하여 팀이 사용 내역을 감사하고, 문제를 조사하며, 로컬 보안 기본값을 약화시키지 않고 규정 준수를 충족하도록 돕습니다. 텔레메트리는 기본적으로 비활성화되어 있으므로 구성에서 명시적으로 켜야 합니다.

### Overview

  * Codex는 로컬 실행을 독립적으로 유지하기 위해 기본적으로 OTel 내보내기를 끕니다.
  * 활성화하면 Codex는 대화, API 요청, SSE/WebSocket 스트림 활동, 사용자 프롬프트(기본적으로 마스킹), 도구 승인 결정, 도구 결과를 포괄하는 구조화된 로그 이벤트를 내보냅니다.
  * Codex는 내보낸 이벤트에 `service.name`(발신자), CLI 버전, 환경 라벨을 붙여 개발/스테이징/프로덕션 트래픽을 구분합니다.



### Enable OTel (opt-in)

Codex 구성(일반적으로 `~/.codex/config.toml`)에 `[otel]` 블록을 추가하고, 내보내기 대상 및 프롬프트 텍스트 기록 여부를 선택하세요.
[code] 
    [otel]
    environment = "staging"   # dev | staging | prod
    exporter = "none"          # none | otlp-http | otlp-grpc
    log_user_prompt = false     # redact prompt text unless policy allows
[/code]

  * `exporter = "none"`이면 계측은 활성 상태로 두되 데이터를 어디에도 보내지 않습니다.

* 자체 수집기로 이벤트를 전송하려면 다음 옵션 중 하나를 선택하세요:


[code] 
    [otel]
    exporter = { otlp-http = {
      endpoint = "https://otel.example.com/v1/logs",
      protocol = "binary",
      headers = { "x-otlp-api-key" = "${OTLP_TOKEN}" }
    }}
[/code]
[code] 
    [otel]
    exporter = { otlp-grpc = {
      endpoint = "https://otel.example.com:4317",
      headers = { "x-otlp-meta" = "abc123" }
    }}
[/code]

Codex는 이벤트를 배치 처리하고 종료 시 플러시합니다. Codex는 OTel 모듈이 생성한 텔레메트리만 내보냅니다.

### 이벤트 범주

대표적인 이벤트 유형은 다음과 같습니다:

  * `codex.conversation_starts` (모델, 추론 설정, sandbox/approval 정책)
  * `codex.api_request` (시도, 상태/성공 여부, 기간, 오류 세부 정보)
  * `codex.sse_event` (스트림 이벤트 종류, 성공/실패, 기간, `response.completed` 시 토큰 수)
  * `codex.websocket_request` 및 `codex.websocket_event` (요청 기간과 메시지별 종류/성공/오류)
  * `codex.user_prompt` (길이; 명시적으로 활성화하지 않으면 콘텐츠는 마스킹됨)
  * `codex.tool_decision` (승인/거부, 소스: 구성 vs. 사용자)
  * `codex.tool_result` (기간, 성공, 출력 스니펫)



연관된 OTel 메트릭(카운터와 기간 히스토그램 쌍)에는 `codex.api_request`, `codex.sse_event`, `codex.websocket.request`, `codex.websocket.event`, `codex.tool.call`(해당 `.duration_ms` 계측 포함)이 있습니다.

전체 이벤트 카탈로그와 구성 레퍼런스는 [GitHub의 Codex 구성 문서](https://github.com/openai/codex/blob/main/docs/config.md#otel)를 참조하세요.

### 보안 및 프라이버시 지침

  * 정책이 명시적으로 프롬프트 내용 저장을 허용하지 않는 한 `log_user_prompt = false`로 유지하세요. 프롬프트에는 소스 코드나 민감한 데이터가 포함될 수 있습니다.
  * 텔레메트리는 제어 가능한 수집기로만 전달하고, 규정 준수 요구에 맞춘 보존 한도와 접근 제어를 적용하세요.
  * 도구 인수와 출력을 민감 데이터로 취급하고, 가능하면 수집기나 SIEM에서 마스킹하세요.
  * `CODEX_HOME` 아래에 Codex가 세션 기록을 저장하지 않길 원한다면 로컬 데이터 보존 설정(예: `history.persistence` / `history.max_bytes`)을 검토하세요. [Advanced Config](https://developers.openai.com/codex/config-advanced#history-persistence)와 [Configuration Reference](https://developers.openai.com/codex/config-reference)를 참조하세요.
  * CLI를 네트워크 비활성화 상태로 실행하면 OTel 내보내기가 수집기에 도달할 수 없습니다. 내보내려면 OTel 엔드포인트에 대해 `workspace-write` 모드에서 네트워크 접근을 허용하거나, 승인된 목록에 해당 수집기 도메인이 포함된 Codex Cloud에서 내보내세요.
  * 승인/샌드박스 변경 사항과 예상치 못한 도구 실행을 주기적으로 검토하세요.



OTel은 선택 사항이며, 위에서 설명한 샌드박스 및 승인 보호를 대체하지 않고 보완하도록 설계되었습니다.

## 관리형 구성

엔터프라이즈 관리자는 두 가지 방식으로 로컬 Codex 동작을 제어할 수 있습니다. 정확한 키 목록은 [Configuration Reference의 `requirements.toml` 섹션](https://developers.openai.com/codex/config-reference#requirementstoml)을 확인하세요:

  * **요구 사항**: 사용자가 재정의할 수 없는 관리자 강제 제약입니다.
  * **관리형 기본값**: Codex가 시작될 때 적용되는 초기 값입니다. 사용자는 세션 중 설정을 변경할 수 있으며, Codex는 다시 시작될 때 관리형 기본값을 재적용합니다.



### 관리자 강제 요구 사항 (requirements.toml)

요구 사항은 보안에 민감한 설정(승인 정책, 샌드박스 모드, 웹 검색 모드, 선택적으로 활성화할 수 있는 MCP 서버)을 제한합니다. 사용자가 `config.toml`, CLI 플래그, 프로필, 세션 UI를 통해 허용되지 않은 값을 명시적으로 선택하면 Codex는 해당 변경을 거부합니다. 값이 명시적으로 설정되지 않았고 기본값이 요구 사항과 충돌하는 경우 Codex는 요구 사항을 준수하는 기본값으로 대체합니다. `mcp_servers` 승인 목록을 구성하면 Codex는 MCP 서버 이름과 ID가 승인 엔트리와 모두 일치할 때만 서버를 활성화하며, 그렇지 않으면 비활성화합니다.

#### 위치

  * Linux/macOS (Unix): `/etc/codex/requirements.toml`
  * macOS MDM: 환경설정 도메인 `com.openai.codex`, 키 `requirements_toml_base64`



#### 클라우드 요구 사항 (Business 및 Enterprise)

Business 또는 Enterprise 플랜에서 ChatGPT로 로그인하면 Codex가 Codex 서비스에서 관리자가 강제한 요구 사항도 가져옵니다. 이는 TUI, `codex exec`, `codex app-server`를 포함한 모든 Codex 인터페이스에 적용됩니다.

클라우드 요구 사항은 현재 최선의 시도로 처리됩니다. 가져오기가 실패하거나 시간 초과되면 Codex는 클라우드 레이어 없이 계속 실행됩니다.

요구 사항 레이어는 다음 순서로 적용됩니다(상위가 우선):

  * macOS 관리형 환경설정(MDM; 최고 우선순위)
  * 클라우드 요구 사항(ChatGPT Business 또는 Enterprise)
  * `/etc/codex/requirements.toml`



클라우드 요구 사항은 설정되지 않은 필드만 채우므로, 동일한 제약을 모두 지정하더라도 상위 관리 레이어가 우선합니다.

하위 호환성을 위해 Codex는 레거시 `managed_config.toml`의 `approval_policy` 및 `sandbox_mode` 필드도 단일 값만 허용하는 요구 사항으로 해석합니다.

#### 예시 requirements.toml

다음 예시는 `--ask-for-approval never`와 `--sandbox danger-full-access`(`--yolo` 포함)를 차단합니다:
[code] 
    allowed_approval_policies = ["untrusted", "on-request"]
    allowed_sandbox_modes = ["read-only", "workspace-write"]
[/code]

웹 검색 모드도 제한할 수 있습니다:
[code] 
    allowed_web_search_modes = ["cached"] # "disabled" remains implicitly allowed
[/code]

`allowed_web_search_modes = []`는 사실상 `"disabled"`만 허용합니다. 예를 들어 `allowed_web_search_modes = ["cached"]`는 `danger-full-access` 세션에서도 실시간 웹 검색을 막습니다.

#### requirements에서 명령 규칙 강제

관리자는 `[rules]` 테이블을 사용해 `requirements.toml`에서 제한적인 명령 규칙을 강제할 수 있습니다. 이러한 규칙은 기존 `.rules` 파일과 병합되며, 가장 제한적인 결정이 최종적으로 적용됩니다.

`.rules`와 달리 요구 사항 규칙에는 반드시 `decision`을 지정해야 하며, 값은 `"prompt"` 또는 `"forbidden"`이어야 합니다(`"allow"` 불가).
[code] 
    [rules]
    prefix_rules = [
      { pattern = [{ token = "rm" }], decision = "forbidden", justification = "Use git clean -fd instead." },
      { pattern = [{ token = "git" }, { any_of = ["push", "commit"] }], decision = "prompt", justification = "Require review before mutating history." },
    ]
[/code]

Codex가 활성화할 수 있는 MCP 서버를 제한하려면 승인 목록 `mcp_servers`를 추가합니다. stdio 서버는 `command`로, 스트리밍 가능한 HTTP 서버는 `url`로 매칭합니다:
[code] 
    [mcp_servers.docs]
    identity = { command = "codex-mcp" }
    
    [mcp_servers.remote]
    identity = { url = "https://example.com/mcp" }
[/code]

`mcp_servers`가 존재하지만 비어 있으면 Codex는 모든 MCP 서버를 비활성화합니다.

### 관리형 기본값(managed_config.toml)

관리형 기본값은 사용자의 로컬 `config.toml` 위에 병합되고, Codex가 시작될 때 기준값을 설정하며 모든 CLI `--config` 오버라이드를 우선합니다. 세션 중에는 사용자가 해당 설정을 변경할 수 있고, Codex는 다음 시작 시 다시 관리형 기본값을 적용합니다.

관리형 기본값이 요구 사항을 충족하는지 확인하세요. 허용되지 않는 값을 지정하면 Codex가 거부합니다.

#### 우선순위와 레이어링

Codex는 다음 순서로 최종 구성을 조립합니다(상위가 하위를 덮어씀):

  * 관리형 환경설정(macOS MDM; 최고 우선순위)
  * `managed_config.toml`(시스템/관리 파일)
  * `config.toml`(사용자 기본 구성)



CLI `--config key=value` 오버라이드는 기본 구성에 적용되지만, 관리 레이어가 다시 이를 덮어씁니다. 즉, 로컬 플래그를 제공해도 각 실행은 관리형 기본값에서 시작합니다.

클라우드 요구 사항은 요구 사항 레이어에만 영향을 주며 관리형 기본값에는 영향을 주지 않습니다. 우선순위는 [Admin-enforced requirements](https://developers.openai.com/codex/security#admin-enforced-requirements-requirementstoml)를 참조하세요.

#### 위치

  * Linux/macOS (Unix): `/etc/codex/managed_config.toml`
  * Windows/non-Unix: `~/.codex/managed_config.toml`

파일이 없으면 Codex는 관리 계층을 건너뜁니다.

#### macOS 관리 환경설정(MDM)

macOS에서 관리자는 다음 위치에 base64로 인코딩된 TOML 페이로드를 제공하는 기기 프로필을 배포할 수 있습니다.

  * 선호 도메인: `com.openai.codex`
  * 키:
    * `config_toml_base64` (관리 기본값)
    * `requirements_toml_base64` (요구 사항)

Codex는 이러한 “관리 환경설정” 페이로드를 TOML로 파싱하며, 가장 높은 우선순위로 적용합니다.

### MDM 설정 워크플로

Codex는 표준 macOS MDM 페이로드를 준수하므로 `Jamf Pro`, `Fleet`, `Kandji` 같은 도구로 설정을 배포할 수 있습니다. 간단한 배포 절차는 다음과 같습니다.

  1. 관리 페이로드 TOML을 작성하고 줄 바꿈 없이 `base64`로 인코딩합니다.
  2. `com.openai.codex` 도메인의 `config_toml_base64`(관리 기본값) 또는 `requirements_toml_base64`(요구 사항) 항목에 문자열을 넣습니다.
  3. 프로필을 푸시한 뒤, 사용자에게 Codex를 재시작하도록 안내하고 시작 구성 요약에 관리 값이 반영됐는지 확인합니다.
  4. 정책을 취소하거나 변경할 때는 관리 페이로드를 업데이트하면 되며, CLI는 다음 실행 시 갱신된 환경설정을 읽습니다.

페이로드에 비밀 정보나 변동성이 큰 동적 값을 포함하지 마세요. 관리 TOML은 변경 관리 대상인 다른 MDM 설정과 동일하게 취급해야 합니다.

### Example managed_config.toml
[code] 
    # Set conservative defaults
    approval_policy = "on-request"
    sandbox_mode    = "workspace-write"
    
    [sandbox_workspace_write]
    network_access = false             # keep network disabled unless explicitly allowed
    
    [otel]
    environment = "prod"
    exporter = "otlp-http"            # point at your collector
    log_user_prompt = false            # keep prompts redacted
    # exporter details live under exporter tables; see Monitoring and telemetry above
[/code]

### 권장 가드레일

  * 대부분의 사용자에 대해서는 승인 기반 `workspace-write`를 우선 사용하고, 완전한 액세스는 통제된 컨테이너에만 허용하세요.
  * 보안 검토에서 워크플로에 필요한 수집기나 도메인을 허용하지 않는 한 `network_access = false`로 유지하세요.
  * 관리 구성을 사용해 OTel 설정(내보내기 대상, 환경)을 고정하되, 정책에서 프롬프트 콘텐츠 저장을 명시적으로 허용하지 않는 이상 `log_user_prompt = false`를 유지하세요.
  * 로컬 `config.toml`과 관리 정책 간의 차이를 주기적으로 감사해 드리프트를 잡으세요. 관리 계층이 로컬 플래그와 파일보다 우선해야 합니다.
