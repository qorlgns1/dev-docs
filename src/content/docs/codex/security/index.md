---
title: '샌드박스 및 승인'
description: 'Codex는 코드와 데이터를 보호하고 오용 위험을 줄입니다.'
---

소스 URL: https://developers.openai.com/codex/security

# 보안

Codex는 코드와 데이터를 보호하고 오용 위험을 줄입니다.

기본적으로 에이전트는 네트워크 액세스를 끈 상태로 실행됩니다. 로컬에서는 Codex가 OS에서 강제하는 샌드박스를 사용해 접근할 수 있는 영역을 제한(일반적으로 현재 작업 공간)하며, 실행 전에 중단하고 사용자의 승인을 요청해야 하는 시점을 제어하는 승인 정책도 적용됩니다.

## 샌드박스 및 승인

Codex 보안 통제는 함께 작동하는 두 계층에서 나옵니다:

- **Sandbox mode**: Codex가 모델이 생성한 명령을 실행할 때 기술적으로 무엇을 할 수 있는지를 나타냅니다(예: 어디에 쓸 수 있는지, 네트워크에 접근할 수 있는지).
- **Approval policy**: Codex가 특정 동작을 실행하기 전에 언제 사용자에게 확인을 요청해야 하는지를 규정합니다(예: 샌드박스를 벗어나거나 네트워크에 접속하거나 신뢰되지 않은 명령을 실행하려 할 때).

Codex는 실행 위치에 따라 다른 샌드박스 모드를 사용합니다:

- **Codex cloud**: OpenAI가 관리하는 격리된 컨테이너에서 실행되어 호스트 시스템이나 관련 없는 데이터에 접근하지 못하게 합니다. 필요하다면 의도적으로 접근을 확장할 수 있습니다(예: 의존성 설치, 특정 도메인 허용). 에이전트가 코드에 접근하기 전에 실행되는 설정 단계에서는 항상 네트워크 액세스가 활성화됩니다.
- **Codex CLI / IDE extension**: OS 수준 메커니즘으로 샌드박스 정책을 적용합니다. 기본 설정은 네트워크 접근 금지와 활성 작업 공간에 대한 쓰기 권한만 허용합니다. 위험 감수 수준에 맞춰 샌드박스, 승인 정책, 네트워크 설정을 조정할 수 있습니다.

`Auto` 프리셋(예: `--full-auto`)에서는 Codex가 작업 디렉토리에서 파일을 읽고, 편집하고, 명령을 자동으로 실행할 수 있습니다.

Codex는 작업 공간 외부의 파일을 편집하려 하거나 네트워크 액세스가 필요한 명령을 실행할 때 승인 요청을 합니다. 변경 없이 대화하거나 계획만 하고 싶다면 `/permissions` 명령으로 `read-only` 모드로 전환하세요.

Codex는 셸 명령이나 파일 변경이 아니더라도 부작용을 안내하는 앱(커넥터) 도구 호출에 대해서 승인을 요청할 수 있습니다.

## 네트워크 액세스

Codex 클라우드의 경우 전체 인터넷 접근이나 도메인 허용 목록을 활성화하려면 [agent internet access](https://developers.openai.com/codex/cloud/internet-access)를 확인하세요.

Codex 앱, CLI, IDE 확장에서는 기본 `workspace-write` 샌드박스 모드가 설정에서 활성화하지 않는 이상 네트워크 액세스를 끕니다:

```toml
[sandbox_workspace_write]
network_access = true
```

전체 네트워크 액세스를 제공하지 않고도 [web search tool](https://platform.openai.com/docs/guides/tools-web-search)을 제어할 수 있습니다. Codex는 기본적으로 웹 검색 캐시를 사용해 결과를 얻습니다. 캐시는 OpenAI가 유지하는 웹 결과 인덱스이므로 캐시 모드는 실시간 페이지를 가져오는 대신 미리 인덱싱된 결과를 반환합니다. 이 설정은 임의 실시간 콘텐츠로부터의 프롬프트 인젝션 노출을 줄이지만, 웹 결과는 여전히 신뢰되지 않은 것으로 다뤄야 합니다. `--yolo` 또는 다른 [full access sandbox setting](#common-sandbox-and-approval-combinations)을 사용하는 경우 웹 검색은 기본적으로 실시간 결과를 사용합니다. 실시간 브라우징을 허용하려면 `--search`를 사용하거나 `web_search = "live"`로 설정하고, 도구를 끄려면 `"disabled"`로 설정하세요:

```toml
web_search = "cached"  # default
# web_search = "disabled"
# web_search = "live"  # same as --search
```

Codex에서 네트워크 액세스나 웹 검색을 활성화할 때는 주의하세요. 프롬프트 인젝션으로 인해 에이전트가 신뢰할 수 없는 지침을 가져와 따르게 될 수 있습니다.

## 기본값 및 권장사항

- 시작 시 Codex는 폴더가 버전 관리되는지를 감지하고 다음을 권장합니다:
  - 버전 관리 폴더: `Auto`(`workspace-write` + 요청 시 승인)
  - 버전 관리되지 않은 폴더: `read-only`
- 설정에 따라 Codex가 작업 디렉토리를 명시적으로 신뢰하기 전까지(예: 온보딩 프롬프트 또는 `/permissions`를 통해) `read-only`로 시작할 수도 있습니다.
- 작업 공간은 현재 디렉토리와 `/tmp` 같은 임시 디렉토리를 포함합니다. 어떤 디렉토리가 작업 공간에 포함되어 있는지 확인하려면 `/status` 명령을 사용하세요.
- 기본값을 수락하려면 `codex`를 실행하세요.
- 다음 명령으로 명시적으로 설정할 수도 있습니다:
  - `codex --sandbox workspace-write --ask-for-approval on-request`
  - `codex --sandbox read-only --ask-for-approval on-request`

### 쓰기 가능한 루트의 보호된 경로

기본 `workspace-write` 샌드박스 정책에서도 쓰기 가능한 루트에는 보호된 경로가 포함됩니다:

- `<writable_root>/.git`은 디렉토리든 파일이든 읽기 전용으로 보호됩니다.
- `<writable_root>/.git`이 포인터 파일(`gitdir: ...`)이라면, 해석된 Git 디렉토리 경로 역시 읽기 전용으로 보호됩니다.
- `<writable_root>/.agents`가 디렉토리로 존재하면 읽기 전용으로 보호됩니다.
- `<writable_root>/.codex`가 디렉토리로 존재하면 읽기 전용으로 보호됩니다.
- 보호는 재귀적으로 적용되므로 해당 경로 아래 모든 항목이 읽기 전용입니다.

### 승인 프롬프트 없이 실행하기

`--ask-for-approval never` 또는 약식 `-a never`을 사용하면 승인 프롬프트를 비활성화할 수 있습니다.

이 옵션은 모든 `--sandbox` 모드에서 작동하므로 Codex의 자율성 수준을 계속 제어할 수 있습니다. 설정한 제약 내에서 최선을 다해 실행합니다.

승인 프롬프트 없이 파일을 읽고, 편집하고, 명령을 실행하며 네트워크 액세스를 허용하려면 `--sandbox danger-full-access`(또는 `--dangerously-bypass-approvals-and-sandbox` 플래그)를 사용하세요. 적용 전에 주의를 기울이세요.

### 일반적인 샌드박스 및 승인 조합

| 의도                                                         | 플래그                                                             | 효과                                                                                                                                       |
| ------------------------------------------------------------ | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Auto (프리셋)                                                 | _플래그 불필요_ 또는 `--full-auto`                                | Codex가 작업 공간에서 파일을 읽고 편집하며 명령을 실행할 수 있습니다. 작업 공간 밖을 편집하거나 네트워크에 접근하려면 승인이 필요합니다. |
| 안전한 읽기 전용 브라우징                                     | `--sandbox read-only --ask-for-approval on-request`              | Codex가 파일을 읽고 질문에 답할 수 있습니다. 편집, 명령 실행, 네트워크 접근에는 승인이 필요합니다.                                     |
| 비대화형 읽기 전용(CI)                                       | `--sandbox read-only --ask-for-approval never`                   | Codex는 파일만 읽을 수 있으며 절대 승인을 묻지 않습니다.                                                                                   |
| 자동 수정하되 신뢰되지 않은 명령에 대해 승인 요청            | `--sandbox workspace-write --ask-for-approval untrusted`         | Codex가 파일을 읽고 수정할 수 있지만, 상태를 변경하거나 외부 실행 경로를 촉발할 수 있는 명령에 대해서는 승인 요청을 합니다.        |
| 위험한 전체 접근                                             | `--dangerously-bypass-approvals-and-sandbox`(별칭: `--yolo`)      | 샌드박스 없음; 승인 없음 _(권장되지 않음)_                                                                                                         |

`--full-auto`는 `--sandbox workspace-write --ask-for-approval on-request`의 편의용 별칭입니다.

`--ask-for-approval untrusted`를 사용하면 Codex는 알려진 안전한 읽기 작업만 자동 실행합니다. 상태를 변형하거나 외부 실행을 발생시킬 가능성이 있는 명령(예: 파괴적인 Git 작업이나 Git 출력/구성 무시 플래그)에는 승인이 필요합니다.

#### `config.toml`에서의 구성

전체 구성 워크플로에 대해서는 [Config basics](https://developers.openai.com/codex/config-basic), [Advanced Config](https://developers.openai.com/codex/config-advanced#approval-policies-and-sandbox-modes), 그리고 [Configuration Reference](https://developers.openai.com/codex/config-reference)를 참조하세요.

```toml
# Always ask for approval mode
approval_policy = "untrusted"
sandbox_mode    = "read-only"

# Optional: Allow network in workspace-write mode
[sandbox_workspace_write]
network_access = true
```

프리셋을 프로필로 저장한 다음 `codex --profile <name>`으로 선택할 수도 있습니다:

```toml
[profiles.full_auto]
approval_policy = "on-request"
sandbox_mode    = "workspace-write"

[profiles.readonly_quiet]
approval_policy = "never"
sandbox_mode    = "read-only"
```

### 로컬에서 샌드박스 테스트하기

Codex 샌드박스에서 명령이 어떻게 실행되는지 확인하려면 다음 Codex CLI 명령을 사용하세요:

```bash
# macOS
codex sandbox macos [--full-auto] [--log-denials] [COMMAND]...
# Linux
codex sandbox linux [--full-auto] [COMMAND]...
```

`sandbox` 명령은 `codex debug`로도 사용할 수 있으며, 플랫폼 도우미는 별칭을 가집니다(예: `codex sandbox seatbelt`, `codex sandbox landlock`).

## OS 수준 샌드박스

Codex는 OS에 따라 샌드박스를 다르게 적용합니다:

- **macOS**는 Seatbelt 정책을 사용하고, 선택한 `--sandbox` 모드에 대응하는 프로파일(`-p`)로 `sandbox-exec`을 통해 명령을 실행합니다.
- **Linux**는 기본적으로 `Landlock`과 `seccomp`를 사용합니다. `features.use_linux_sandbox_bwrap = true`(또는 `-c use_linux_sandbox_bwrap=true`)로 대안 Linux 샌드박스 파이프라인을 선택할 수 있습니다.
- **Windows**는 [Windows Subsystem for Linux (WSL)](https://developers.openai.com/codex/windows#windows-subsystem-for-linux)에서 실행할 때 Linux 샌드박스 구현을 사용합니다. Windows 네이티브에서 실행할 때는 [실험적 샌드박스](https://developers.openai.com/codex/windows#windows-experimental-sandbox) 구현을 활성화할 수 있습니다.

Windows에서 Codex IDE 확장을 사용하면 WSL을 직접 지원합니다. 다음을 VS Code 설정에 추가하면 WSL이 사용 가능한 경우 에이전트가 항상 WSL 안에 있도록 유지합니다:

```json
{
  "chatgpt.runCodexInWindowsSubsystemForLinux": true
}
```

이 설정은 호스트 OS가 Windows여도 IDE 확장이 명령, 승인, 파일 시스템 접근 모두 Linux 샌드박스 의미론을 상속하도록 합니다. 자세한 내용은 [Windows setup guide](https://developers.openai.com/codex/windows)를 참고하세요.

기본 Windows 샌드박스는 실험적이며 중요한 제약이 존재합니다. 예를 들어 `Everyone` SID가 이미 쓰기 권한을 가진 디렉토리(예: 모두에게 쓰기 가능한 폴더)에 대한 쓰기를 방지할 수 없습니다. 자세한 내용과 완화 방법은 [Windows setup guide](https://developers.openai.com/codex/windows#windows-experimental-sandbox)를 참고하세요.

Docker 같은 컨테이너형 환경에서 Linux를 실행하는 경우, 호스트나 컨테이너 구성이 필수 `Landlock` 및 `seccomp` 기능을 지원하지 않으면 샌드박스가 작동하지 않을 수 있습니다.

그런 경우 Docker 컨테이너를 필요한 수준의 격리로 구성한 다음, 컨테이너 안에서 `--sandbox danger-full-access`(또는 `--dangerously-bypass-approvals-and-sandbox` 플래그)와 함께 `codex`를 실행하세요.

## 버전 관리

Codex는 버전 관리 워크플로와 함께 사용할 때 가장 효과적입니다:

- 기능 브랜치에서 작업하고 위임하기 전에 `git status`를 정리하세요. 그래야 Codex 패치를 더 쉽게 분리하고 되돌릴 수 있습니다.
- 추적된 파일을 직접 편집하기보다 패치 기반 워크플로(예: `git diff`/`git apply`)를 선호하세요. 자주 커밋하면 작은 단위로 롤백하기 쉽습니다.
- Codex 제안을 다른 PR처럼 다루세요: 타깃 검증 실행, diff 검토, 커밋 메시지에 결정 사항 문서화를 통해 감사를 지원하세요.

## 모니터링 및 텔레메트리

Codex는 OpenTelemetry(OTel)를 통한 옵트인 모니터링을 지원하여 팀이 사용 현황을 감사하고 이슈를 조사하며 지역 보안 기본값을 약화시키지 않고도 컴플라이언스를 충족할 수 있도록 합니다. 텔레메트리는 기본적으로 꺼져 있으며, 구성에서 명시적으로 활성화해야 합니다.

### 개요

- Codex는 로컬 실행이 자급자족 형식을 유지하도록 기본적으로 OTel 내보내기를 끕니다.

- 활성화하면 Codex는 대화, API 요청, SSE/WebSocket 스트림 활동, 사용자 프롬프트(기본적으로 삭제 처리됨), 도구 승인 결정, 도구 결과를 포함한 구조화된 로그 이벤트를 출력합니다.
- Codex는 내보낸 이벤트에 `service.name`(발신자), CLI 버전, 개발/스테이징/프로덕션 트래픽을 구분하는 환경 레이블을 태그합니다.

### OTel 활성화(옵트인)

Codex 구성(`~/.codex/config.toml`이 일반적)에 `[otel]` 블록을 추가하고, 익스포터와 프롬프트 텍스트 기록 여부를 선택합니다.

```toml
[otel]
environment = "staging"   # dev | staging | prod
exporter = "none"          # none | otlp-http | otlp-grpc
log_user_prompt = false     # 정책이 허용하지 않는 한 프롬프트 텍스트를 삭제 처리
```

- `exporter = "none"`은 계측을 유지하지만 데이터를 전송하지 않습니다.
- 자체 수집기로 이벤트를 보내려면 다음 중 하나를 선택하세요:

```toml
[otel]
exporter = { otlp-http = {
  endpoint = "https://otel.example.com/v1/logs",
  protocol = "binary",
  headers = { "x-otlp-api-key" = "${OTLP_TOKEN}" }
}}
```

```toml
[otel]
exporter = { otlp-grpc = {
  endpoint = "https://otel.example.com:4317",
  headers = { "x-otlp-meta" = "abc123" }
}}
```

Codex는 이벤트를 배치하고 종료 시 플러시합니다. Codex는 OTel 모듈에서 생성한 텔레메트리만 내보냅니다.

### 이벤트 범주

대표적인 이벤트 유형은 다음과 같습니다:

- `codex.conversation_starts`(모델, 추론 설정, 샌드박스/승인 정책)
- `codex.api_request`(시도, 상태/성공 여부, 지속시간, 오류 세부 정보)
- `codex.sse_event`(스트림 이벤트 종류, 성공/실패, 지속시간, `response.completed`에서 토큰 수)
- `codex.websocket_request` 및 `codex.websocket_event`(요청 지속시간과 메시지별 종류/성공/오류)
- `codex.user_prompt`(길이; 명시적으로 활성화하지 않는 한 내용은 삭제)
- `codex.tool_decision`(승인/거부, 소스: 구성 vs. 사용자)
- `codex.tool_result`(지속시간, 성공 여부, 출력 스니펫)

관련된 OTel 메트릭(카운터와 지속시간 히스토그램 쌍)은 `codex.api_request`, `codex.sse_event`, `codex.websocket.request`, `codex.websocket.event`, `codex.tool.call`(해당 `.duration_ms` 계측 포함)이 있습니다.

전체 이벤트 카탈로그와 구성 참고는 [GitHub의 Codex 구성 문서](https://github.com/openai/codex/blob/main/docs/config.md#otel)를 참고하세요.

### 보안 및 개인정보 보호 지침

- 정책이 명시적으로 프롬프트 내용을 저장하는 것을 허용하지 않는 한 `log_user_prompt = false`를 유지하세요. 프롬프트에는 소스 코드나 민감한 데이터가 포함될 수 있습니다.
- 텔레메트리는 직접 제어하는 수집기로만 라우팅하고, 보관 제한과 액세스 제어를 준수 요구 사항에 맞게 적용하세요.
- 도구 인수와 출력은 민감한 정보로 취급하세요. 가능하면 수집기나 SIEM에서 삭제 처리하는 것이 좋습니다.
- 세션 전사를 `CODEX_HOME` 아래에 저장하지 않으려면 로컬 데이터 보존 설정(예: `history.persistence` / `history.max_bytes`)을 검토하세요. [고급 구성](https://developers.openai.com/codex/config-advanced#history-persistence) 및 [구성 참조](https://developers.openai.com/codex/config-reference)를 확인하세요.
- 네트워크 액세스를 끈 상태로 CLI를 실행하면 OTel 익스포트가 수집기에 도달하지 못합니다. 익스포트하려면 OTel 엔드포인트에 대해 `workspace-write` 모드에서 네트워크 액세스를 허용하거나 승인된 도메인 목록에 있는 수집기로 Codex 클라우드에서 내보내세요.
- 승인/샌드박스 변경이나 예기치 않은 도구 실행을 점검할 수 있도록 이벤트를 주기적으로 검토하세요.

OTel은 선택 사항이며 위에서 설명한 샌드박스 및 승인 보호 기능을 대체하지 않고 보완하도록 설계되었습니다.

## 관리 구성

엔터프라이즈 관리자는 두 가지 방법으로 로컬 Codex 동작을 제어할 수 있습니다. 정확한 키 목록은 [구성 참조의 `requirements.toml` 섹션](https://developers.openai.com/codex/config-reference#requirementstoml)을 참고하세요:

- **요구 사항**: 사용자가 재정의할 수 없는 관리자 강제 제약.
- **관리 기본값**: Codex가 시작할 때 적용되는 초기값. 사용자는 세션 중 설정을 바꿀 수 있지만 다음 시작 시 관리 기본값이 다시 적용됩니다.

### 관리자 강제 요구 사항(requirements.toml)

요구 사항은 보안에 민감한 설정(승인 정책, 샌드박스 모드, 웹 검색 모드, 선택적으로 활성화할 수 있는 MCP 서버)을 제한합니다. 사용자가 명시적으로 허용되지 않은 값을 선택하면(`config.toml`, CLI 플래그, 프로필, 세션 UI 등), Codex는 변경을 거부합니다. 값이 명시되지 않았고 기본값이 요구 사항과 충돌하면 요구 사항에 부합하는 기본값으로 되돌립니다. `mcp_servers` 승인 목록을 구성하면 이름과 ID가 승인 항목과 모두 일치할 때에만 MCP 서버를 활성화하고, 그렇지 않으면 비활성화합니다.

#### 위치

- Linux/macOS(Unix): `/etc/codex/requirements.toml`
- macOS MDM: 기본 도메인 `com.openai.codex`, 키 `requirements_toml_base64`

#### 클라우드 요구 사항(Business 및 Enterprise)

ChatGPT Business 또는 Enterprise 플랜으로 로그인하면 Codex가 Codex 서비스에서 관리자 강제 요구 사항을 가져올 수도 있습니다. 이는 TUI, `codex exec`, `codex app-server` 등 모든 Codex 표면에 적용됩니다.

클라우드 요구 사항은 현재 최선의 노력으로 처리됩니다. 가져오기가 실패하거나 시간 초과되면 Codex는 클라우드 계층 없이 계속 실행합니다.

요구 사항은 다음 순서로 레이어링됩니다(우선순위가 높은 것이 적용됨):

- macOS 관리 환경설정(MDM; 가장 높은 우선순위)
- 클라우드 요구 사항(ChatGPT Business 또는 Enterprise)
- `/etc/codex/requirements.toml`

클라우드 요구 사항은 설정되지 않은 필드만 채우므로, 동일한 제약을 지정한 경우 우선순위가 더 높은 관리 계층이 여전히 적용됩니다.

하위 호환성을 위해 Codex는 이전 `managed_config.toml`의 `approval_policy`와 `sandbox_mode` 필드를 요구 사항으로 해석하여(해당 값만 허용) 처리합니다.

#### 예시 requirements.toml

이 예시는 `--ask-for-approval never`와 `--sandbox danger-full-access`(및 `--yolo`)를 차단합니다:

```toml
allowed_approval_policies = ["untrusted", "on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]
```

웹 검색 모드를 제한할 수도 있습니다:

```toml
allowed_web_search_modes = ["cached"] # "disabled"는 암묵적으로 여전히 허용됨
```

`allowed_web_search_modes = []`는 사실상 `"disabled"`만 허용합니다. 예를 들어 `allowed_web_search_modes = ["cached"]`로 설정하면 `danger-full-access` 세션에서도 라이브 웹 검색을 금지합니다.

#### requirements로 명령 규칙 적용

관리자는 `[rules]` 테이블을 사용하여 `requirements.toml`에서 제한적인 명령 규칙을 적용할 수 있습니다. 이 규칙은 일반 `.rules` 파일과 병합되며, 가장 제한적인 결정이 적용됩니다.

`.rules`와 달리 요구 사항 규칙은 `decision`을 반드시 지정해야 하며, `"prompt"` 또는 `"forbidden"`이어야 하고 `"allow"`는 사용할 수 없습니다.

```toml
[rules]
prefix_rules = [
  { pattern = [{ token = "rm" }], decision = "forbidden", justification = "Use git clean -fd instead." },
  { pattern = [{ token = "git" }, { any_of = ["push", "commit"] }], decision = "prompt", justification = "Require review before mutating history." },
]
```

Codex가 활성화할 수 있는 MCP 서버를 제한하려면 `mcp_servers` 승인 목록을 추가합니다. stdio 서버는 `command`, 스트리밍 HTTP 서버는 `url`로 일치시킵니다:

```toml
[mcp_servers.docs]
identity = { command = "codex-mcp" }

[mcp_servers.remote]
identity = { url = "https://example.com/mcp" }
```

`mcp_servers`가 존재하지만 비어 있으면 Codex는 모든 MCP 서버를 비활성화합니다.

### 관리 기본값(managed_config.toml)

관리 기본값은 사용자의 로컬 `config.toml` 위에 병합되며, CLI `--config` 재정의를 포함한 어떤 값보다 우선하여 Codex가 시작할 때 초기값을 설정합니다. 사용자는 여전히 세션 중에 설정을 변경할 수 있으며, 다음 실행 시 관리 기본값이 다시 적용됩니다.

관리 기본값이 요구 사항을 충족하도록 구성하세요. Codex는 허용되지 않은 값을 거부합니다.

#### 우선순위 및 계층화

Codex는 다음 순서로 최종 구성을 구성합니다(위에서 아래로 덮어쓰기):

- 관리 환경설정(macOS MDM; 가장 높은 우선순위)
- `managed_config.toml`(시스템/관리 파일)
- `config.toml`(사용자 기본 구성)

CLI `--config key=value` 재정의는 기본 구성에 적용되지만, 관리 계층이 이를 덮어씁니다. 즉, 로컬 플래그를 제공하더라도 각 실행은 관리 기본값에서 시작합니다.

클라우드 요구 사항은 관리 기본값이 아니라 요구 사항 계층에 영향을 줍니다. 우선순위는 [관리자 강제 요구 사항](https://developers.openai.com/codex/security#admin-enforced-requirements-requirementstoml)을 확인하세요.

#### 위치

- Linux/macOS(Unix): `/etc/codex/managed_config.toml`
- Windows/비유닉스: `~/.codex/managed_config.toml`

파일이 없으면 Codex는 관리 계층을 건너뜁니다.

#### macOS 관리 환경설정(MDM)

macOS에서 관리자는 다음 위치에 base64로 인코딩된 TOML 페이로드를 제공하는 디바이스 프로필을 배포할 수 있습니다:

- 기본 도메인: `com.openai.codex`
- 키:
  - `config_toml_base64` (관리 기본값)
  - `requirements_toml_base64` (요구 사항)

Codex는 이러한 “관리 환경설정” 페이로드를 TOML로 파싱하여 가장 높은 우선순위로 적용합니다.

### MDM 설정 워크플로우

Codex는 표준 macOS MDM 페이로드를 따르므로 `Jamf Pro`, `Fleet`, `Kandji` 등의 도구로 설정을 배포할 수 있습니다. 경량 배포 절차는 다음과 같습니다:

1. 관리 페이로드 TOML을 작성한 뒤 `base64`(줄 바꿈 없이)로 인코딩합니다.
2. 문자열을 MDM 프로필의 `com.openai.codex` 도메인 하위 `config_toml_base64`(관리 기본값) 또는 `requirements_toml_base64`(요구 사항)에 넣습니다.
3. 프로필을 푸시한 후 사용자에게 Codex를 재시작하고 시작 구성 요약에 관리 값이 반영되는지 확인하도록 요청합니다.
4. 정책을 철회하거나 변경할 때는 관리 페이로드를 업데이트하고 CLI는 다음 실행 시 갱신된 설정을 읽습니다.

페이로드에 비밀이나 자주 바뀌는 동적 값을 포함하지 마세요. 관리 TOML을 다른 MDM 설정처럼 변경 제어 하에 다루십시오.

### 관리 `managed_config.toml` 예시

```toml
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
```

### 권장 보호 조치

- 대부분 사용자에게는 `workspace-write`와 승인을 우선 적용하고, 전체 액세스는 통제된 컨테이너로 제한하세요.
- 보안 검토에서 수집기나 워크플로우에 필요한 도메인을 허용하지 않는 한 `network_access = false`를 유지하세요.
- OTel 설정(익스포터, 환경)을 고정하려면 관리 구성을 사용하되, 정책이 명시적으로 프롬프트 내용을 저장할 수 있게 허용하지 않는 이상 `log_user_prompt = false`를 유지하세요.
- 로컬 `config.toml`과 관리 정책 사이의 차이를 주기적으로 감사하여 편차를 확인하세요; 관리 계층이 로컬 플래그와 파일보다 우선합니다.
