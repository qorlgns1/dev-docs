---
title: '고급 구성'
description: '프로바이더, 정책, 통합을 더 세밀하게 제어하려면 이러한 옵션을 사용하세요. 빠른 시작은 Config basics를 참고하세요.'
---

Source URL: https://developers.openai.com/codex/config-advanced

# 고급 구성

프로바이더, 정책, 통합을 더 세밀하게 제어하려면 이러한 옵션을 사용하세요. 빠른 시작은 [Config basics](https://developers.openai.com/codex/config-basic)를 참고하세요.

프로젝트 가이던스, 재사용 가능한 기능, 사용자 정의 슬래시 명령, 다중 에이전트 워크플로우 및 통합에 대한 배경은 [Customization](https://developers.openai.com/codex/concepts/customization)을 참조하세요. 구성 키 전체는 [Configuration Reference](https://developers.openai.com/codex/config-reference)를 확인하세요.

## 프로필

프로필은 명명된 구성값 세트를 저장하고 CLI에서 전환할 수 있게 해줍니다.

프로필은 실험적 기능이며 향후 릴리스에서 변경되거나 제거될 수 있습니다.

Codex IDE 확장에서는 현재 프로필을 지원하지 않습니다.

`config.toml`의 `[profiles.<name>]` 아래에 프로필을 정의한 다음 `codex --profile <name>`을 실행하세요:

```toml
model = "gpt-5-codex"
approval_policy = "on-request"

[profiles.deep-review]
model = "gpt-5-pro"
model_reasoning_effort = "high"
approval_policy = "never"

[profiles.lightweight]
model = "gpt-4.1"
approval_policy = "untrusted"
```

프로필을 기본값으로 만들려면 `config.toml` 최상단에 `profile = "deep-review"`를 추가하세요. Codex는 명령줄에서 덮어쓰기 전까지 해당 프로필을 로드합니다.

## CLI에서의 일회성 재정의

`~/.codex/config.toml`을 편집하는 것 외에도 CLI에서 단일 실행에 대한 구성을 재정의할 수 있습니다:

- 전용 플래그가 있는 경우 이를 우선 사용하세요(예: `--model`).
- 임의 키를 재정의해야 할 경우 `-c` / `--config`를 사용하세요.

예시:

```shell
# 전용 플래그
codex --model gpt-5.2

# 일반 키/값 재정의 (값은 JSON이 아닌 TOML)
codex --config model='"gpt-5.2"'
codex --config sandbox_workspace_write.network_access=true
codex --config 'shell_environment_policy.include_only=["PATH","HOME"]'
```

참고:

- 키는 중첩 값을 설정할 때 점 표기법을 사용할 수 있습니다(예: `mcp_servers.context7.enabled=false`).
- `--config` 값은 TOML로 파싱됩니다. 의심스러우면 값에 따옴표를 씌워 셸이 공백으로 나누지 않게 하세요.
- 값이 TOML로 파싱되지 않으면 Codex는 이를 문자열로 처리합니다.

## 구성 및 상태 위치

Codex는 로컬 상태를 `CODEX_HOME` 아래에 저장합니다(기본값은 `~/.codex`).

자주 보게 되는 파일:

- `config.toml` (로컬 구성)
- `auth.json` (파일 기반 자격 증명 저장소를 사용할 경우) 또는 OS 키체인/키링
- `history.jsonl` (히스토리 지속성이 활성화된 경우)
- 로그 및 캐시 같은 기타 사용자별 상태

인증 세부 정보(자격 증명 저장 모드를 포함)는 [Authentication](https://developers.openai.com/codex/auth)을 참조하세요. 구성 키 전체 목록은 [Configuration Reference](https://developers.openai.com/codex/config-reference)를 확인하세요.

저장소 또는 시스템 경로에 체크인된 공유 기본값, 규칙, 기능은 [Team Config](https://developers.openai.com/codex/enterprise/admin-setup#team-config)를 참조하세요.

내장 OpenAI 프로바이더를 LLM 프록시, 라우터, 또는 데이터 지역성 활성화 프로젝트로 지정하려면 새 프로바이더를 정의하지 말고 환경 변수 `OPENAI_BASE_URL`을 설정하세요. 이는 `config.toml` 변경 없이 기본 OpenAI 엔드포인트를 재정의합니다.

```shell
export OPENAI_BASE_URL="https://api.openai.com/v1"
codex
```

## 프로젝트 구성 파일 (`.codex/config.toml`)

사용자 구성 외에 Codex는 저장소 내 `.codex/config.toml` 파일에서 프로젝트 범위 재정의를 읽습니다. Codex는 프로젝트 루트에서 현재 작업 디렉토리까지 이동하며 발견되는 모든 `.codex/config.toml`을 로드합니다. 동일 키를 여러 파일에서 정의하면 작업 디렉토리에 가장 가까운 파일이 우선합니다.

보안을 위해 Codex는 프로젝트가 신뢰되는 경우에만 프로젝트 범위 구성 파일을 로드합니다. 프로젝트가 신뢰되지 않으면 Codex는 프로젝트 내 `.codex/config.toml`을 무시합니다.

프로젝트 구성 내 상대 경로(예: `experimental_instructions_file`)는 해당 `config.toml`을 포함한 `.codex/` 폴더를 기준으로 해석됩니다.

## 에이전트 역할 (`config.toml`의 `[agents]`)

다중 에이전트 역할 구성(`[agents]` in `config.toml`)은 [Multi-agents](https://developers.openai.com/codex/multi-agent)를 참조하세요.

## 프로젝트 루트 감지

Codex는 작업 디렉토리에서 위로 올라가며 프로젝트 구성을 발견합니다(예: `.codex/` 레이어와 `AGENTS.md`).

기본적으로 Codex는 `.git`을 포함한 디렉토리를 프로젝트 루트로 간주합니다. 이 동작을 사용자화하려면 `config.toml`에서 `project_root_markers`를 설정하세요:

```toml
# 다음 마커 중 하나를 포함한 디렉토리를 프로젝트 루트로 취급합니다.
project_root_markers = [".git", ".hg", ".sl"]
```

`project_root_markers = []`를 설정하면 상위 디렉토리 검색을 건너뛰고 현재 작업 디렉토리를 프로젝트 루트로 봅니다.

## 사용자 정의 모델 프로바이더

모델 프로바이더는 Codex가 모델에 연결하는 방법(기본 URL, 와이어 API, 선택적 HTTP 헤더)을 정의합니다.

추가 프로바이더를 정의하고 `model_provider`로 지정하세요:

```toml
model = "gpt-5.1"
model_provider = "proxy"

[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "http://proxy.example.com"
env_key = "OPENAI_API_KEY"

[model_providers.ollama]
name = "Ollama"
base_url = "http://localhost:11434/v1"

[model_providers.mistral]
name = "Mistral"
base_url = "https://api.mistral.ai/v1"
env_key = "MISTRAL_API_KEY"
```

필요할 경우 요청 헤더를 추가하세요:

```toml
[model_providers.example]
http_headers = { "X-Example-Header" = "example-value" }
env_http_headers = { "X-Example-Features" = "EXAMPLE_FEATURES" }
```

## OSS 모드(로컬 프로바이더)

Codex는 `--oss`를 전달하면 로컬 “오픈 소스” 프로바이더(예: Ollama 또는 LM Studio)에서 실행할 수 있습니다. 프로바이더를 지정하지 않고 `--oss`만 전달하면 Codex는 기본값으로 `oss_provider`를 사용합니다.

```toml
# `--oss`와 함께 사용하는 기본 로컬 프로바이더
oss_provider = "ollama" # 또는 "lmstudio"
```

## Azure 프로바이더 및 프로바이더별 조정

```toml
[model_providers.azure]
name = "Azure"
base_url = "https://YOUR_PROJECT_NAME.openai.azure.com/openai"
env_key = "AZURE_OPENAI_API_KEY"
query_params = { api-version = "2025-04-01-preview" }
wire_api = "responses"

[model_providers.openai]
request_max_retries = 4
stream_max_retries = 10
stream_idle_timeout_ms = 300000
```

## 데이터 지역성을 사용하는 ChatGPT 고객

[데이터 지역성](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt)이 활성화된 프로젝트는 모델 프로바이더를 만들어 [올바른 접두사](https://platform.openai.com/docs/guides/your-data#which-models-and-features-are-eligible-for-data-residency)로 base_url을 업데이트할 수 있습니다.

```toml
model_provider = "openaidr"
[model_providers.openaidr]
name = "OpenAI Data Residency"
base_url = "https://us.api.openai.com/v1" # 'us'를 도메인 접두사로 교체
```

## 모델 추론, 자세함, 제한

```toml
model_reasoning_summary = "none"          # 요약 비활성화
model_verbosity = "low"                   # 응답 간결화
model_supports_reasoning_summaries = true # 추론 강제
model_context_window = 128000             # 컨텍스트 창 크기
```

`model_verbosity`는 Responses API를 사용하는 프로바이더에만 적용됩니다. 채팅 완료 프로바이더는 이 설정을 무시합니다.

## 승인 정책 및 샌드박스 모드

승인 엄격도(언제 Codex가 일시 중지되는지)와 샌드박스 수준(파일/네트워크 액세스에 영향)을 선택하세요.

`config.toml` 작성 중 놓치기 쉬운 운영 세부 정보는 [Common sandbox and approval combinations](https://developers.openai.com/codex/security#common-sandbox-and-approval-combinations), [Protected paths in writable roots](https://developers.openai.com/codex/security#protected-paths-in-writable-roots), [Network access](https://developers.openai.com/codex/security#network-access)을 참조하세요.

```toml
approval_policy = "untrusted"   # 기타 옵션: on-request, never
sandbox_mode = "workspace-write"

[sandbox_workspace_write]
exclude_tmpdir_env_var = false  # $TMPDIR 허용
exclude_slash_tmp = false       # /tmp 허용
writable_roots = ["/Users/YOU/.pyenv/shims"]
network_access = false          # 외부 네트워크 허용 옵트인
```

전체 키 목록(프로필 범위 재정의 및 요구사항 제약 포함)이 필요하신가요? [Configuration Reference](https://developers.openai.com/codex/config-reference) 및 [Managed configuration](https://developers.openai.com/codex/security#managed-configuration)를 참조하세요.

workspace-write 모드에서는 일부 환경이 작업 공간의 나머지가 쓰기 가능하더라도 `.git/` 및 `.codex/`를 읽기 전용으로 유지합니다. 따라서 `git commit`과 같은 명령은 샌드박스 외부에서 실행 시 여전히 승인이 필요할 수 있습니다. 특정 명령을 건너뛰고 싶으면(예: 샌드박스 외부에서 `git commit` 차단) <a href="/codex/rules">rules</a>를 사용하세요.

샌드박스를 완전히 비활성화합니다(환경이 이미 프로세스를 격리하는 경우에만 사용).

```toml
sandbox_mode = "danger-full-access"
```

## 셸 환경 정책

`shell_environment_policy`는 Codex가 서브프로세스를 실행할 때(예: 모델이 제안한 도구 명령 실행) 전달하는 환경 변수를 제어합니다. 깔끔한 시작(`inherit = "none"`) 또는 정제된 집합(`inherit = "core"`)에서 시작한 뒤, 제외, 포함, 오버라이드를 적층하여 비밀 정보 유출을 방지하면서 작업에 필요한 경로, 키 또는 플래그를 제공합니다.

```toml
[shell_environment_policy]
inherit = "none"
set = { PATH = "/usr/bin", MY_FLAG = "1" }
ignore_default_excludes = false
exclude = ["AWS_*", "AZURE_*"]
include_only = ["PATH", "HOME"]
```

패턴은 대소문자 구분 없는 글로브(`*`, `?`, `[A-Z]`)입니다; `ignore_default_excludes = false`는 자동 KEY/SECRET/TOKEN 필터가 포함/제외 규칙 전에 실행되도록 유지합니다.

## MCP 서버

구성 세부 정보는 전용 [MCP 문서](https://developers.openai.com/codex/mcp)를 참조하세요.

## 관측 가능성과 텔레메트리

OpenTelemetry(OTel) 로그 내보내기를 활성화하여 Codex 실행(API 요청, SSE/이벤트, 프롬프트, 도구 승인/결과)을 추적하세요. 기본값은 비활성; `[otel]`로 옵트인합니다:

```toml
[otel]
environment = "staging"   # 기본값은 "dev"
exporter = "none"         # 이벤트 전송을 원하면 otlp-http 또는 otlp-grpc 설정
log_user_prompt = false   # 명시적으로 활성화하지 않으면 사용자 프롬프트를 마스킹
```

내보내기기를 선택하세요:

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

`exporter = "none"`이면 Codex는 이벤트를 기록만 하고 전송하지 않습니다. 내보내기기는 비동기적으로 배치하고 종료 시 플러시합니다. 이벤트 메타데이터에는 서비스 이름, CLI 버전, 환경 태그, 대화 ID, 모델, 샌드박스/승인 설정 및 이벤트별 필드가 포함됩니다([Config Reference](https://developers.openai.com/codex/config-reference) 참조).

### 어떤 항목이 전송되는가

Codex는 실행 및 도구 사용에 대한 구조화된 로그 이벤트를 전송합니다. 대표적인 이벤트 유형:

- `codex.conversation_starts` (모델, 추론 설정, 샌드박스/승인 정책)
- `codex.api_request` (시도, 상태/성공, 기간, 오류 세부 정보)
- `codex.sse_event` (스트림 이벤트 종류, 성공/실패, 기간, `response.completed`의 토큰 수)
- `codex.websocket_request` 및 `codex.websocket_event` (요청 기간 및 메시지 종류/성공/오류)
- `codex.user_prompt` (길이; 명시적 활성화가 없으면 내용은 마스킹됨)
- `codex.tool_decision` (승인/거부 및 설정 기반 결정 여부)
- `codex.tool_result` (기간, 성공, 출력 스니펫)

### 내보내는 OTel 메트릭

OTel 메트릭 파이프라인이 활성화되면 Codex는 API, 스트림, 도구 활동에 대한 카운터 및 기간 히스토그램을 전송합니다.

아래 각 지표에는 기본 메타데이터 태그인 `auth_mode`, `originator`, `session_source`, `model`, `app.version`도 포함됩니다.

| Metric                                | Type      | Fields              | Description                                                       |
| ------------------------------------- | --------- | ------------------- | ----------------------------------------------------------------- |
| `codex.api_request`                   | counter   | `status`, `success` | HTTP 상태 및 성공/실패 기준 API 요청 수.                          |
| `codex.api_request.duration_ms`       | histogram | `status`, `success` | 밀리초 단위 API 요청 처리 시간.                                   |
| `codex.sse_event`                     | counter   | `kind`, `success`   | 이벤트 종류 및 성공/실패 기준 SSE 이벤트 수.                      |
| `codex.sse_event.duration_ms`         | histogram | `kind`, `success`   | 밀리초 단위 SSE 이벤트 처리 시간.                                 |
| `codex.websocket.request`             | counter   | `success`           | 성공/실패 기준 WebSocket 요청 횟수.                               |
| `codex.websocket.request.duration_ms` | histogram | `success`           | 밀리초 단위 WebSocket 요청 처리 시간.                             |
| `codex.websocket.event`               | counter   | `kind`, `success`   | 종류 및 성공/실패 기준 WebSocket 메시지/이벤트 수.               |
| `codex.websocket.event.duration_ms`   | histogram | `kind`, `success`   | 밀리초 단위 WebSocket 메시지/이벤트 처리 시간.                    |
| `codex.tool.call`                     | counter   | `tool`, `success`   | 도구 이름 및 성공/실패 기준 도구 호출 횟수.                       |
| `codex.tool.call.duration_ms`         | histogram | `tool`, `success`   | 도구 이름과 결과별 밀리초 단위 도구 실행 시간.                   |

텔레메트리에 대한 보안 및 프라이버시 지침은 [Security](https://developers.openai.com/codex/security#monitoring-and-telemetry)를 참고하세요.

### 메트릭

기본적으로 Codex는 익명 사용량 및 상태 데이터를 정기적으로 OpenAI로 전송합니다. 이는 Codex가 제대로 작동하지 않을 때를 감지하고 어떤 기능과 설정이 사용되는지를 보여 줌으로써 Codex 팀이 가장 중요한 부분에 집중할 수 있게 합니다. 이 메트릭에는 개인 식별 정보(PII)가 포함되지 않습니다. 메트릭 수집은 OTel 로그/트레이스 내보내기와 별개입니다.

머신에서 Codex 전체에서 메트릭 수집을 완전히 비활성화하려면 설정 파일에서 analytics 플래그를 다음과 같이 설정하세요:

```toml
[analytics]
enabled = false
```

각 메트릭은 고유한 필드와 아래 기본 컨텍스트 필드를 포함합니다.

#### 기본 컨텍스트 필드 (모든 이벤트/메트릭에 적용)

- `auth_mode`: 현재 인증 모드(`swic`, `api`, `unknown`).
- `model`: 사용된 모델 이름.
- `app.version`: Codex 버전.

#### 메트릭 카탈로그

각 메트릭은 필수 필드와 위 기본 컨텍스트 필드를 포함하며 모든 메트릭 이름은 `codex.`로 시작합니다. 메트릭에 `tool` 필드가 포함된 경우 내부에서 사용한 도구(예: `apply_patch` 또는 `shell`)를 나타내며 실제 셸 명령어나 `codex`가 적용하려는 패치를 포함하지 않습니다.

| Metric                                   | Type      | Fields             | Description                                                                                                                   |
| ---------------------------------------- | --------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| `feature.state`                          | counter   | `feature`, `value` | 기본값과 다른 기능 값(기본이 아닌 항목마다 한 행을 전송).                                                                     |
| `thread.started`                         | counter   | `is_git`           | 새 스레드 생성.                                                                                                               |
| `thread.fork`                            | counter   |                    | 기존 스레드를 포크하여 새 스레드 생성.                                                                                        |
| `thread.rename`                          | counter   |                    | 스레드 이름 변경.                                                                                                             |
| `task.compact`                           | counter   | `type`             | 수동 및 자동을 포함한 유형별(`remote` 또는 `local`) 컴팩션 횟수.                                                              |
| `task.user_shell`                        | counter   |                    | 사용자 셸 동작 수(예: TUI에서 `!`).                                                                                           |
| `task.review`                            | counter   |                    | 트리거된 리뷰 횟수.                                                                                                           |
| `task.undo`                              | counter   |                    | 실행된 실행 취소 횟수.                                                                                                        |
| `approval.requested`                     | counter   | `tool`, `approved` | 도구 승인 요청 결과(`approved`, `approved_with_amendment`, `approved_for_session`, `denied`, `abort`).                        |
| `conversation.turn.count`                | counter   |                    | 스레드 종료 시 기록되는 사용자/도우미 턴 수.                                                                                  |
| `turn.e2e_duration_ms`                   | histogram |                    | 전체 턴에 걸린 엔드 투 엔드 시간.                                                                                             |
| `mcp.call`                               | counter   | `status`           | MCP 도구 호출 결과(`ok` 또는 오류 문자열).                                                                                   |
| `model_warning`                          | counter   |                    | 모델에 전달된 경고.                                                                                                           |
| `tool.call`                              | counter   | `tool`, `success`  | 도구 호출 결과(`success`: `true` 또는 `false`).                                                                              |
| `tool.call.duration_ms`                  | histogram | `tool`, `success`  | 도구 실행 시간.                                                                                                               |
| `remote_models.fetch_update.duration_ms` | histogram |                    | 원격 모델 정의를 가져오는 데 걸린 시간.                                                                                       |
| `remote_models.load_cache.duration_ms`   | histogram |                    | 원격 모델 캐시를 로드하는 데 걸린 시간.                                                                                        |
| `shell_snapshot`                         | counter   | `success`          | 셸 스냅샷을 성공적으로 찍었는지 여부.                                                                                          |
| `shell_snapshot.duration_ms`             | histogram | `success`          | 셸 스냅샷을 찍는 데 걸린 시간.                                                                                                |
| `db.init`                                | counter   | `status`           | 상태 DB 초기화 결과(`opened`, `created`, `open_error`, `init_error`).                                                        |
| `db.backfill`                            | counter   | `status`           | 초기 상태 DB 백필 결과(`upserted`, `failed`).                                                                                 |
| `db.backfill.duration_ms`                | histogram | `status`           | 초기 상태 DB 백필 시간(태그: `success`, `failed`, `partial_failure`).                                                         |
| `db.error`                               | counter   | `stage`            | 상태 DB 작업 중 오류(예: `extract_metadata_from_rollout`, `backfill_sessions`, `apply_rollout_items`).                         |
| `db.compare_error`                       | counter   | `stage`, `reason`  | 조정 중 감지된 상태 DB 불일치.                                                                                                 |

### 피드백 제어

기본적으로 Codex는 `/feedback`에서 사용자 피드백을 보낼 수 있게 합니다. 머신 전체에서 Codex 피드백 수집을 비활성화하려면 설정을 다음과 같이 업데이트하세요:

```toml
[feedback]
enabled = false
```

비활성화하면 `/feedback`는 비활성화 메시지를 표시하고 Codex는 피드백 제출을 거부합니다.

### 추론 이벤트 숨기기 또는 표시하기

노이즈가 많은 "추론" 출력을 줄이고 싶다면(예: CI 로그) 다음 설정으로 억제할 수 있습니다:

```toml
hide_agent_reasoning = true
```

모델이 원시 추론 콘텐츠를 내보낼 때 이를 표시하고 싶다면:

```toml
show_raw_agent_reasoning = true
```

워크플로에 문제가 없다면 원시 추론을 활성화하세요. 일부 모델/제공자(예: `gpt-oss`)는 원시 추론을 내보내지 않으므로 이 설정은 아무런 영향이 없습니다.

## 알림

`notify`를 사용하면 Codex가 지원하는 이벤트(현재는 `agent-turn-complete`만)를 발생시킬 때마다 외부 프로그램을 실행할 수 있습니다. 데스크톱 토스트, 채팅 웹훅, CI 업데이트, 또는 내장 TUI 알림이 다루지 않는 보조 알림에 유용합니다.

```toml
notify = ["python3", "/path/to/notify.py"]
```

다음은 `agent-turn-complete`에 반응하는 `notify.py` 예시(생략됨):

```python
#!/usr/bin/env python3
import json, subprocess, sys

def main() -> int:
    notification = json.loads(sys.argv[1])
    if notification.get("type") != "agent-turn-complete":
        return 0
    title = f"Codex: {notification.get('last-assistant-message', 'Turn Complete!')}"
    message = " ".join(notification.get("input-messages", []))
    subprocess.check_output([
        "terminal-notifier",
        "-title", title,
        "-message", message,
        "-group", "codex-" + notification.get("thread-id", ""),
        "-activate", "com.googlecode.iterm2",
    ])
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

스크립트에는 하나의 JSON 인수가 전달됩니다. 일반적인 필드는 다음과 같습니다:

- `type` (현재 `agent-turn-complete`)
- `thread-id` (세션 식별자)
- `turn-id` (턴 식별자)
- `cwd` (작업 디렉터리)
- `input-messages` (턴을 발생시킨 사용자 메시지)
- `last-assistant-message` (마지막 도우미 메시지 텍스트)

스크립트를 적절한 경로에 두고 `notify`에 해당 경로를 지정하세요.

#### `notify`와 `tui.notifications` 비교

- `notify`는 외부 프로그램을 실행합니다(웹훅, 데스크톱 알림, CI 훅에 적합).
- `tui.notifications`는 TUI에 내장되어 있으며 이벤트 유형(예: `agent-turn-complete`, `approval-requested`)으로 선택 필터링할 수 있습니다.
- `tui.notification_method`는 TUI가 터미널 알림을 내보내는 방식을 제어합니다(`auto`, `osc9`, `bel`).

`auto` 모드에서 Codex는 OSC 9 알림(일부 터미널이 데스크톱 알림으로 해석하는 터미널 이스케이프 시퀀스)을 우선 사용하고, 그렇지 않으면 BEL(`\x07`)로 대체합니다.

정확한 키는 [Configuration Reference](https://developers.openai.com/codex/config-reference)를 참고하세요.

## 기록 지속성

기본적으로 Codex는 로컬 세션 기록을 `CODEX_HOME`에 저장합니다(예: `~/.codex/history.jsonl`). 로컬 기록 지속성을 비활성화하려면:

```toml
[history]
persistence = "none"
```

기록 파일 크기를 제한하려면 `history.max_bytes`를 설정하세요. 파일이 제한을 초과하면 Codex는 가장 오래된 항목을 삭제하고 최신 항목을 유지하면서 파일을 압축합니다.

```toml
[history]
max_bytes = 104857600 # 100 MiB
```

## 클릭 가능한 인용

Codex는 터미널/편집기 통합에서 지원하는 경우 파일 인용을 클릭 가능한 링크로 렌더링할 수 있습니다. Codex가 사용하는 URI 스킴을 지정하려면 `file_opener`를 구성하세요.

```toml
file_opener = "vscode" # or cursor, windsurf, vscode-insiders, none
```

예: `/home/user/project/main.py:42` 같은 인용은 클릭 가능한 `vscode://file/...:42` 링크로 다시 작성될 수 있습니다.

## 프로젝트 지침 탐색

Codex는 `AGENTS.md`(및 관련 파일)를 읽고 세션의 첫 번째 턴에서 프로젝트 안내를 일부 포함합니다. 이 동작은 두 가지 설정으로 제어됩니다.

- `project_doc_max_bytes`: 각 `AGENTS.md` 파일에서 읽을 최대 바이트 수
- `project_doc_fallback_filenames`: 해당 디렉터리 수준에서 `AGENTS.md`가 없을 때 시도할 추가 파일 이름

자세한 안내는 [Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md)를 참조하세요.

## TUI 옵션

`codex`를 서브커맨드 없이 실행하면 대화형 터미널 UI(TUI)가 시작됩니다. Codex는 `[tui]` 아래에 몇 가지 TUI 전용 설정을 제공합니다.

- `tui.notifications`: 알림 활성화/비활성화(또는 특정 유형으로 제한)
- `tui.notification_method`: 터미널 알림에 `auto`, `osc9`, `bel` 중 선택
- `tui.animations`: ASCII 애니메이션 및 반짝임 효과 활성화/비활성화
- `tui.alternate_screen`: 대체 화면 사용 제어(터미널 스크롤백을 유지하려면 `never`로 설정)
- `tui.show_tooltips`: 환영 화면에서 온보딩 툴팁 표시 여부

`tui.notification_method`의 기본값은 `auto`입니다. `auto` 모드에서는 터미널이 지원하는 것으로 보일 때 Codex가 OSC 9 알림(일부 터미널이 데스크톱 알림으로 해석하는 에스케이프 시퀀스)을 우선 사용하고, 그렇지 않으면 BEL(`\x07`)로 대체합니다.

전체 키 목록은 [Configuration Reference](https://developers.openai.com/codex/config-reference)를 확인하세요.
