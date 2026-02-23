---
title: 고급 구성
description: 제공업체, 정책, 통합을 더 세밀하게 제어해야 할 때 이 옵션을 사용하세요. 빠른 시작은 Config basics를 참고하세요.
sidebar:
  order: 31
---

# 고급 구성

Source URL: https://developers.openai.com/codex/config-advanced

제공업체, 정책, 통합을 더 세밀하게 제어해야 할 때 이 옵션을 사용하세요. 빠른 시작은 [Config basics](https://developers.openai.com/codex/config-basic)를 참고하세요.

프로젝트 가이드, 재사용 가능한 기능, 커스텀 슬래시 명령, 멀티 에이전트 워크플로, 통합에 대한 배경은 [Customization](https://developers.openai.com/codex/concepts/customization)을, 구성 키는 [Configuration Reference](https://developers.openai.com/codex/config-reference)를 참조하세요.

## Profiles

프로파일은 구성 값을 이름 붙인 세트로 저장해 CLI에서 손쉽게 전환할 수 있도록 합니다.

프로파일은 실험적 기능이므로 향후 릴리스에서 변경되거나 제거될 수 있습니다.

프로파일은 현재 Codex IDE 확장에서 지원되지 않습니다.

`config.toml`의 `[profiles.<name>]` 아래에 프로파일을 정의한 뒤 `codex --profile <name>`을 실행하세요:
```
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

기본으로 사용할 프로파일을 지정하려면 `config.toml` 최상위에 `profile = "deep-review"`를 추가하세요. 이렇게 하면 커맨드 라인에서 다른 값을 지정하지 않는 한 Codex가 해당 프로파일을 로드합니다.

## CLI에서 1회성 덮어쓰기

`~/.codex/config.toml`을 편집하는 것과 별도로, CLI에서 단일 실행에만 적용되는 구성을 덮어쓸 수 있습니다.

  * 가능하면 전용 플래그(예: `--model`)를 우선 사용하세요.
  * 임의의 키를 덮어써야 할 때는 `-c` / `--config`를 사용하세요.



예시:
```
    # Dedicated flag
    codex --model gpt-5.2
    
    # Generic key/value override (value is TOML, not JSON)
    codex --config model='"gpt-5.2"'
    codex --config sandbox_workspace_write.network_access=true
    codex --config 'shell_environment_policy.include_only=["PATH","HOME"]'
```

참고:

  * 키는 도트 표기법을 사용해 중첩 값을 설정할 수 있습니다(예: `mcp_servers.context7.enabled=false`).
  * `--config` 값은 TOML로 파싱됩니다. 공백으로 잘리지 않도록 확신이 서지 않을 때는 값을 따옴표로 감싸세요.
  * 값이 TOML로 파싱되지 않으면 Codex는 문자열로 취급합니다.



## 구성 및 상태 위치

Codex는 로컬 상태를 `CODEX_HOME`(기본값 `~/.codex`)에 저장합니다.

그곳에서 자주 보게 되는 파일:

  * `config.toml` (로컬 구성)
  * `auth.json` (파일 기반 자격 증명 저장을 사용할 때) 또는 OS 키체인/키링
  * `history.jsonl` (기록 유지가 활성화된 경우)
  * 로그와 캐시 같은 기타 사용자별 상태



인증 세부 정보(자격 증명 저장 방식 포함)는 [Authentication](https://developers.openai.com/codex/auth), 전체 구성 키 목록은 [Configuration Reference](https://developers.openai.com/codex/config-reference)를 참고하세요.

리포지토리나 시스템 경로에 커밋된 공유 기본값, 규칙, 스킬은 [Team Config](https://developers.openai.com/codex/enterprise/admin-setup#team-config)를 확인하세요.

기본 OpenAI 제공업체를 LLM 프록시·라우터·데이터 거주성 프로젝트에만 지정하면 된다면, 새 제공업체를 정의하지 말고 환경 변수 `OPENAI_BASE_URL`을 설정하세요. `config.toml`을 수정하지 않고도 기본 OpenAI 엔드포인트를 덮어씁니다.
```
    export OPENAI_BASE_URL="https://api.openai.com/v1"
    codex
```

## 프로젝트 구성 파일(`.codex/config.toml`)

사용자 구성 외에도, Codex는 리포 내부의 `.codex/config.toml`에서 프로젝트 범위 덮어쓰기를 읽습니다. Codex는 프로젝트 루트에서 현재 작업 디렉터리까지 탐색하며 발견한 모든 `.codex/config.toml`을 로드합니다. 여러 파일이 동일한 키를 정의하면, 현재 작업 디렉터리에 가장 가까운 파일이 우선합니다.

보안을 위해, 프로젝트가 신뢰된 경우에만 Codex가 프로젝트 범위 구성 파일을 로드합니다. 프로젝트가 신뢰되지 않으면 Codex는 프로젝트 내 `.codex/config.toml` 파일을 무시합니다.

프로젝트 구성에서 사용되는 상대 경로(예: `experimental_instructions_file`)는 `config.toml`을 포함하는 `.codex/` 폴더를 기준으로 해석됩니다.

## 에이전트 역할 (`config.toml`의 `[agents]`)

다중 에이전트 역할 구성(`config.toml`의 `[agents]`)에 대해서는 [Multi-agents](https://developers.openai.com/codex/multi-agent)를 참고하세요.

## 프로젝트 루트 감지

Codex는 작업 디렉터리에서 위쪽으로 올라가면서 프로젝트 루트에 도달할 때까지 프로젝트 구성(예: `.codex/` 계층과 `AGENTS.md`)을 탐색합니다.

기본적으로 Codex는 `.git`이 포함된 디렉터리를 프로젝트 루트로 간주합니다. 이 동작을 커스터마이즈하려면 `config.toml`에서 `project_root_markers`를 설정하세요:
```
    # Treat a directory as the project root when it contains any of these markers.
    project_root_markers = [".git", ".hg", ".sl"]
```

부모 디렉터리 검색을 건너뛰고 현재 작업 디렉터리를 프로젝트 루트로 취급하려면 `project_root_markers = []`로 설정하세요.

## 맞춤형 모델 제공자

모델 제공자는 Codex가 모델에 연결하는 방식을 정의합니다(기본 URL, wire API, 선택적 HTTP 헤더).

추가 제공자를 정의하고 `model_provider`가 이를 가리키도록 설정하세요:
```
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

필요할 때 요청 헤더를 추가하세요:
```
    [model_providers.example]
    http_headers = { "X-Example-Header" = "example-value" }
    env_http_headers = { "X-Example-Features" = "EXAMPLE_FEATURES" }
```

## OSS 모드(로컬 제공자)

`--oss`를 전달하면 Codex는 로컬 “오픈 소스” 제공자(예: Ollama 또는 LM Studio)에 대해 실행할 수 있습니다. 제공자를 지정하지 않고 `--oss`를 전달하면 Codex는 기본값으로 `oss_provider`를 사용합니다.
```
    # Default local provider used with `--oss`
    oss_provider = "ollama" # or "lmstudio"
```

## Azure 제공자 및 제공자별 튜닝
```
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

## 데이터 레지던시를 사용하는 ChatGPT 고객

[data residency](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt)를 활성화하여 생성한 프로젝트는 [올바른 프리픽스](https://platform.openai.com/docs/guides/your-data#which-models-and-features-are-eligible-for-data-residency)를 사용하도록 base_url을 업데이트하는 모델 제공자를 만들 수 있습니다.
```
    model_provider = "openaidr"
    [model_providers.openaidr]
    name = "OpenAI Data Residency"
    base_url = "https://us.api.openai.com/v1" # Replace 'us' with domain prefix
```

## 모델 추론, 상세도, 제한
```
    model_reasoning_summary = "none"          # Disable summaries
    model_verbosity = "low"                   # Shorten responses
    model_supports_reasoning_summaries = true # Force reasoning
    model_context_window = 128000             # Context window size
```

`model_verbosity`는 Responses API를 사용하는 제공자에만 적용됩니다. Chat Completions 제공자는 이 설정을 무시합니다.

## 승인 정책과 샌드박스 모드

승인 엄격도(Codex가 일시 중지되는 시점에 영향)와 샌드박스 수준(파일/네트워크 접근에 영향)을 선택하세요.

편집 중 `config.toml`에서 놓치기 쉬운 운영 세부 정보는 [Common sandbox and approval combinations](https://developers.openai.com/codex/security#common-sandbox-and-approval-combinations), [Protected paths in writable roots](https://developers.openai.com/codex/security#protected-paths-in-writable-roots), [Network access](https://developers.openai.com/codex/security#network-access)를 참고하세요.
```
    approval_policy = "untrusted"   # Other options: on-request, never
    sandbox_mode = "workspace-write"
    
    [sandbox_workspace_write]
    exclude_tmpdir_env_var = false  # Allow $TMPDIR
    exclude_slash_tmp = false       # Allow /tmp
    writable_roots = ["/Users/YOU/.pyenv/shims"]
    network_access = false          # Opt in to outbound network
```

전체 키 목록(프로필 범위 재정의와 요구사항 제약 포함)이 필요하다면 [Configuration Reference](https://developers.openai.com/codex/config-reference)와 [Managed configuration](https://developers.openai.com/codex/security#managed-configuration)을 확인하세요.

워크스페이스 쓰기 모드에서도 일부 환경은 `.git/`과 `.codex/`를 읽기 전용으로 유지해 나머지 워크스페이스만 쓰기 가능하게 합니다. 이 때문에 `git commit` 같은 명령이 샌드박스 밖에서 실행될 때 여전히 승인이 필요할 수 있습니다. 특정 명령을 Codex가 건너뛰게 하고 싶다면(예: 샌드박스 밖 `git commit` 차단) [rules](https://developers.openai.com/codex/rules)를 사용하세요.

샌드박싱을 완전히 비활성화하려면(환경이 이미 프로세스를 격리하는 경우에만 사용):
```
    sandbox_mode = "danger-full-access"
```

## Shell environment policy

`shell_environment_policy`는 Codex가 실행하는 하위 프로세스(예: 모델이 제안한 도구 명령)를 어떤 환경 변수와 함께 실행할지 제어합니다. 깨끗한 시작점(`inherit = "none"`)이나 축약된 집합(`inherit = "core"`)에서 시작한 뒤, 비밀이 새지 않으면서 작업에 필요한 경로·키·플래그를 제공하도록 exclude/include/override를 순차적으로 추가하세요.
```
    [shell_environment_policy]
    inherit = "none"
    set = { PATH = "/usr/bin", MY_FLAG = "1" }
    ignore_default_excludes = false
    exclude = ["AWS_*", "AZURE_*"]
    include_only = ["PATH", "HOME"]
```

패턴은 대소문자를 구분하지 않는 glob(`*`, `?`, `[A-Z]`)이며, `ignore_default_excludes = false`로 설정하면 include/exclude가 적용되기 전에 KEY/SECRET/TOKEN 자동 필터가 유지됩니다.

## MCP servers

구성 세부 정보는 전용 [MCP documentation](https://developers.openai.com/codex/mcp)를 참고하세요.

## Observability and telemetry

Codex 실행(API 요청, SSE/이벤트, 프롬프트, 도구 승인/결과)을 추적하려면 OpenTelemetry(OTel) 로그 내보내기를 활성화하세요. 기본은 비활성화이며 `[otel]`을 통해 옵트인합니다:
```
    [otel]
    environment = "staging"   # defaults to "dev"
    exporter = "none"         # set to otlp-http or otlp-grpc to send events
    log_user_prompt = false   # redact user prompts unless explicitly enabled
```

내보내기 방식을 선택하세요:
```
    [otel]
    exporter = { otlp-http = {
      endpoint = "https://otel.example.com/v1/logs",
      protocol = "binary",
      headers = { "x-otlp-api-key" = "${OTLP_TOKEN}" }
    }}
```
```
    [otel]
    exporter = { otlp-grpc = {
      endpoint = "https://otel.example.com:4317",
      headers = { "x-otlp-meta" = "abc123" }
    }}
```

`exporter = "none"`이면 Codex는 이벤트를 기록하지만 전송하지 않습니다. 내보내기는 비동기식으로 배치되며 종료 시 플러시됩니다. 이벤트 메타데이터에는 서비스 이름, CLI 버전, 환경 태그, 대화 ID, 모델, 샌드박스/승인 설정, 이벤트별 필드가 포함됩니다(자세한 내용은 [Config Reference](https://developers.openai.com/codex/config-reference) 참조).

### 기록 항목

Codex는 실행 및 도구 사용에 대한 구조화된 로그 이벤트를 내보냅니다. 대표 이벤트 유형은 다음과 같습니다:

  * `codex.conversation_starts` (모델, 추론 설정, 샌드박스/승인 정책)
  * `codex.api_request` (시도 횟수, 상태/성공 여부, 기간, 오류 세부 정보)

* `codex.sse_event` (`response.completed`에서 토큰 수를 포함해 스트림 이벤트 종류, 성공/실패, 지속 시간)
  * `codex.websocket_request` 및 `codex.websocket_event` (요청 지속 시간과 메시지별 종류/성공/오류)
  * `codex.user_prompt` (길이; 명시적으로 활성화하지 않으면 콘텐츠는 마스킹됨)
  * `codex.tool_decision` (승인/거부 여부와 결정이 설정에 의한 것인지 사용자에 의한 것인지)
  * `codex.tool_result` (지속 시간, 성공 여부, 출력 스니펫)



### 방출되는 OTel 메트릭

OTel 메트릭 파이프라인을 활성화하면 Codex는 API, 스트림, 도구 활동에 대한 카운터와 지속 시간 히스토그램을 내보냅니다.

아래의 각 메트릭에는 기본 메타데이터 태그 `auth_mode`, `originator`, `session_source`, `model`, `app.version`이 포함됩니다.

Metric| Type| Fields| Description  
---|---|---|---  
`codex.api_request`| counter| `status`, `success`| HTTP 상태와 성공/실패별 API 요청 수.  
`codex.api_request.duration_ms`| histogram| `status`, `success`| 밀리초 단위 API 요청 지속 시간.  
`codex.sse_event`| counter| `kind`, `success`| 이벤트 종류와 성공/실패별 SSE 이벤트 수.  
`codex.sse_event.duration_ms`| histogram| `kind`, `success`| 밀리초 단위 SSE 이벤트 처리 지속 시간.  
`codex.websocket.request`| counter| `success`| 성공/실패별 WebSocket 요청 수.  
`codex.websocket.request.duration_ms`| histogram| `success`| 밀리초 단위 WebSocket 요청 지속 시간.  
`codex.websocket.event`| counter| `kind`, `success`| 유형과 성공/실패별 WebSocket 메시지/이벤트 수.  
`codex.websocket.event.duration_ms`| histogram| `kind`, `success`| 밀리초 단위 WebSocket 메시지/이벤트 처리 지속 시간.  
`codex.tool.call`| counter| `tool`, `success`| 도구 이름과 성공/실패별 도구 호출 수.  
`codex.tool.call.duration_ms`| histogram| `tool`, `success`| 도구 이름과 결과별 밀리초 단위 도구 실행 지속 시간.  
  
텔레메트리 관련 보안 및 프라이버시 지침은 [Security](https://developers.openai.com/codex/security#monitoring-and-telemetry)를 참조하세요.

### Metrics

기본적으로 Codex는 OpenAI로 소량의 익명 사용량 및 상태 데이터를 주기적으로 전송합니다. 이는 Codex가 제대로 작동하지 않는 상황을 감지하고 어떤 기능과 구성 옵션이 사용되는지 파악해 Codex 팀이 중요한 영역에 집중하도록 돕습니다. 이 메트릭에는 개인 식별 정보(PII)가 포함되지 않습니다. 메트릭 수집은 OTel 로그/트레이스 내보내기와 독립적입니다.

기기에서 Codex 전반의 메트릭 수집을 완전히 비활성화하려면 구성에서 analytics 플래그를 설정하세요:
```
    [analytics]
    enabled = false
```

각 메트릭에는 자체 필드와 아래의 기본 컨텍스트 필드가 포함됩니다.

#### 기본 컨텍스트 필드(모든 이벤트/메트릭에 적용)

  * `auth_mode`: `swic` | `api` | `unknown`.
  * `model`: 사용된 모델 이름.
  * `app.version`: Codex 버전.



#### 메트릭 카탈로그

각 메트릭에는 필수 필드와 위의 기본 컨텍스트 필드가 포함됩니다. 모든 메트릭은 `codex.` 접두사를 가집니다. 메트릭에 `tool` 필드가 포함된 경우 내부적으로 사용된 도구(예: `apply_patch` 또는 `shell`)를 나타내며 Codex가 실행하려는 실제 셸 명령이나 패치를 포함하지 않습니다.

Metric| Type| Fields| Description  
---|---|---|---  
`feature.state`| counter| `feature`, `value`| 기본값과 다른 기능 값(비기본 항목마다 한 행).  
`thread.started`| counter| `is_git`| 새 스레드 생성.  
`thread.fork`| counter| | 기존 스레드를 포크하여 새 스레드 생성.  
`thread.rename`| counter| | 스레드 이름 변경.  
`task.compact`| counter| `type`| 유형(`remote` 또는 `local`)별 컴팩션 수, 수동 및 자동 포함.  
`task.user_shell`| counter| | 사용자 셸 작업 수(예: TUI에서 `!`).  
`task.review`| counter| | 트리거된 리뷰 수.  
`task.undo`| counter| | 실행 취소 작업 수.

`approval.requested`| counter| `tool`, `approved`| 도구 승인 요청 결과 (`approved`, `approved_with_amendment`, `approved_for_session`, `denied`, `abort`).  
`conversation.turn.count`| counter| | 스레드당 사용자/어시스턴트 턴 수(스레드 종료 시 기록).  
`turn.e2e_duration_ms`| histogram| | 전체 턴의 엔드 투 엔드 시간.  
`mcp.call`| counter| `status`| MCP 도구 호출 결과(`ok` 또는 오류 문자열).  
`model_warning`| counter| | 모델에 전송된 경고.  
`tool.call`| counter| `tool`, `success`| 도구 호출 결과(`success`: `true` 또는 `false`).  
`tool.call.duration_ms`| histogram| `tool`, `success`| 도구 실행 시간.  
`remote_models.fetch_update.duration_ms`| histogram| | 원격 모델 정의를 가져오는 데 걸린 시간.  
`remote_models.load_cache.duration_ms`| histogram| | 원격 모델 캐시를 로드하는 데 걸린 시간.  
`shell_snapshot`| counter| `success`| 셸 스냅샷 획득 성공 여부.  
`shell_snapshot.duration_ms`| histogram| `success`| 셸 스냅샷 획득 시간.  
`db.init`| counter| `status`| 상태 DB 초기화 결과(`opened`, `created`, `open_error`, `init_error`).  
`db.backfill`| counter| `status`| 초기 상태 DB 백필 결과(`upserted`, `failed`).  
`db.backfill.duration_ms`| histogram| `status`| 초기 상태 DB 백필 소요 시간(`success`, `failed`, `partial_failure` 태그).  
`db.error`| counter| `stage`| 상태 DB 작업 중 오류(예: `extract_metadata_from_rollout`, `backfill_sessions`, `apply_rollout_items`).  
`db.compare_error`| counter| `stage`, `reason`| 상태 DB 정합성 검사에서 감지된 불일치.  
  
### 피드백 제어

기본적으로 Codex는 `/feedback`에서 사용자가 피드백을 보낼 수 있도록 허용합니다. 모든 Codex 인터페이스에서 피드백 수집을 비활성화하려면 구성 파일을 업데이트하세요:
```
    [feedback]
    enabled = false
```

비활성화되면 `/feedback`은 비활성화 메시지를 표시하며 Codex는 피드백 제출을 거부합니다.

### 추론 이벤트 숨김/표시

시끄러운 “reasoning” 출력(예: CI 로그)을 줄이고 싶다면 다음 설정으로 억제할 수 있습니다:
```
    hide_agent_reasoning = true
```

모델이 내보내는 원시 추론 내용을 노출하고 싶다면:
```
    show_raw_agent_reasoning = true
```

워크플로에서 허용되는 경우에만 원시 추론을 활성화하세요. 일부 모델/제공자(예: `gpt-oss`)는 원시 추론을 내보내지 않으므로 이 경우 해당 설정은 효과가 없습니다.

## 알림

Codex가 지원되는 이벤트(현재는 `agent-turn-complete`만) 발생 시 외부 프로그램을 트리거하려면 `notify`를 사용하세요. 이는 데스크톱 토스트, 채팅 웹훅, CI 업데이트 또는 기본 TUI 알림이 다루지 않는 기타 사이드 채널 알림에 유용합니다.
```
    notify = ["python3", "/path/to/notify.py"]
```

`agent-turn-complete`에 반응하는 예시 `notify.py`(일부 생략):
```
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

스크립트는 단일 JSON 인자를 받습니다. 공통 필드는 다음과 같습니다:

  * `type` (현재 `agent-turn-complete`)
  * `thread-id` (세션 식별자)
  * `turn-id` (턴 식별자)
  * `cwd` (작업 디렉터리)
  * `input-messages` (해당 턴을 유발한 사용자 메시지)
  * `last-assistant-message` (마지막 어시스턴트 메시지 텍스트)



스크립트를 디스크의 적절한 위치에 두고 `notify`가 해당 경로를 가리키도록 설정하세요.

#### `notify` vs `tui.notifications`

  * `notify`는 외부 프로그램을 실행하며(웹훅, 데스크톱 알림기, CI 훅에 적합).
  * `tui.notifications`는 TUI에 내장되어 있으며 필요하면 이벤트 유형(예: `agent-turn-complete`, `approval-requested`)별로 필터링할 수 있습니다.
  * `tui.notification_method`는 TUI가 터미널 알림을 내보내는 방식(`auto`, `osc9`, `bel`)을 제어합니다.

`auto` 모드에서 Codex는 가능하면 OSC 9 알림(일부 터미널이 데스크톱 알림으로 해석하는 이스케이프 시퀀스)을 선호하고, 그렇지 않으면 BEL(`\x07`)로 폴백합니다.

정확한 키는 [Configuration Reference](https://developers.openai.com/codex/config-reference)를 참고하세요.

## 기록 지속성

기본적으로 Codex는 로컬 세션 대화록을 `CODEX_HOME`(예: `~/.codex/history.jsonl`) 아래에 저장합니다. 로컬 기록 저장을 비활성화하려면:
```
    [history]
    persistence = "none"
```

기록 파일 크기에 상한을 두려면 `history.max_bytes`를 설정하세요. 파일이 상한을 초과하면 Codex가 가장 오래된 항목을 제거하고 최신 기록을 유지한 채로 파일을 압축합니다.
```
    [history]
    max_bytes = 104857600 # 100 MiB
```

## 클릭 가능한 인용

해당 기능을 지원하는 터미널/에디터 통합을 사용한다면, Codex는 파일 인용을 클릭 가능한 링크로 렌더링할 수 있습니다. Codex가 사용할 URI 스킴을 선택하려면 `file_opener`를 설정하세요:
```
    file_opener = "vscode" # or cursor, windsurf, vscode-insiders, none
```

예시: `/home/user/project/main.py:42` 같은 인용은 클릭 가능한 `vscode://file/...:42` 링크로 다시 쓸 수 있습니다.

## 프로젝트 지침 탐색

Codex는 `AGENTS.md`(및 관련 파일)를 읽고 세션 첫 턴에 제한된 프로젝트 지침을 포함합니다. 이를 제어하는 두 가지 설정은 다음과 같습니다.

  * `project_doc_max_bytes`: 각 `AGENTS.md`에서 읽을 분량
  * `project_doc_fallback_filenames`: 디렉터리 수준에서 `AGENTS.md`가 없을 때 추가로 확인할 파일명

자세한 워크스루는 [Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md)를 확인하세요.

## TUI 옵션

서브커맨드 없이 `codex`를 실행하면 인터랙티브 터미널 UI(TUI)가 실행됩니다. Codex는 `[tui]` 아래에 몇 가지 TUI 전용 설정을 제공합니다:

  * `tui.notifications`: 알림 활성/비활성 또는 특정 유형으로 제한
  * `tui.notification_method`: 터미널 알림용 `auto`, `osc9`, `bel` 선택
  * `tui.animations`: ASCII 애니메이션과 반짝임 효과 활성/비활성
  * `tui.alternate_screen`: 대체 화면 사용 제어(`never`로 설정하면 터미널 스크롤백 유지)
  * `tui.show_tooltips`: 환영 화면 온보딩 툴팁 표시 여부

`tui.notification_method`의 기본값은 `auto`입니다. `auto` 모드에서 Codex는 터미널이 지원하는 것으로 보이면 OSC 9 알림을 우선 사용하고, 그렇지 않으면 BEL(`\x07`)로 폴백합니다.

전체 키 목록은 [Configuration Reference](https://developers.openai.com/codex/config-reference)를 참고하세요.