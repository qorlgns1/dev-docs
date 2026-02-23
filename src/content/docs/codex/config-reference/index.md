---
title: Configuration Reference
description: Codex 구성 파일에 대한 검색 가능한 참고 자료로 이 페이지를 활용하세요. 개념적 안내와 예제는 Config basics와 Advanced Config에서 시작하세요.
sidebar:
  order: 32
---

# Configuration Reference

Source URL: https://developers.openai.com/codex/config-reference

Codex 구성 파일에 대한 검색 가능한 참고 자료로 이 페이지를 활용하세요. 개념적 안내와 예제는 [Config basics](https://developers.openai.com/codex/config-basic)와 [Advanced Config](https://developers.openai.com/codex/config-advanced)에서 시작하세요.

## `config.toml`

사용자 수준 구성은 `~/.codex/config.toml`에 저장됩니다. 프로젝트 범위 재정의를 `.codex/config.toml` 파일에 추가할 수도 있습니다. Codex는 프로젝트를 신뢰할 때만 프로젝트 범위 구성 파일을 로드합니다.

샌드박스 및 승인 키(`approval_policy`, `sandbox_mode`, `sandbox_workspace_write.*`)의 경우 [Sandbox and approvals](https://developers.openai.com/codex/security#sandbox-and-approvals), [Protected paths in writable roots](https://developers.openai.com/codex/security#protected-paths-in-writable-roots), [Network access](https://developers.openai.com/codex/security#network-access)와 함께 참고하세요.

Key| Type / Values| Details  
---|---|---  
`agents.<name>.config_file`| `string (path)`| 해당 역할용 TOML 구성 레이어 경로; 상대 경로는 역할을 선언한 구성 파일을 기준으로 해석됩니다.  
`agents.<name>.description`| `string`| 해당 에이전트 타입을 선택하고 생성할 때 Codex에 표시되는 역할 가이드입니다.  
`agents.max_threads`| `number`| 동시에 열 수 있는 에이전트 스레드의 최대 수입니다.  
`approval_policy`| `untrusted | on-request | never`| Codex가 명령을 실행하기 전에 승인을 위해 일시 중지하는 시점을 제어합니다. `on-failure`는 더 이상 사용되지 않으므로 대화형 실행에는 `on-request`, 비대화형 실행에는 `never`를 사용하세요.  
`apps.<id>.disabled_reason`| `unknown | user`| 앱/커넥터가 비활성화될 때 선택적으로 첨부되는 이유입니다.  
`apps.<id>.enabled`| `boolean`| 특정 앱/커넥터를 ID별로 활성화하거나 비활성화합니다(기본값: true).  
`chatgpt_base_url`| `string`| ChatGPT 로그인 흐름에서 사용하는 기본 URL을 재정의합니다.  
`check_for_update_on_startup`| `boolean`| 시작 시 Codex 업데이트를 확인합니다(업데이트를 중앙에서 관리하는 경우에만 false로 설정하세요).  
`cli_auth_credentials_store`| `file | keyring | auto`| CLI가 캐시된 자격 증명을 저장하는 위치를 제어합니다(file 기반 auth.json vs OS 키체인).  
`compact_prompt`| `string`| 히스토리 압축 프롬프트에 대한 인라인 재정의입니다.  
`developer_instructions`| `string`| 세션에 주입하는 추가 개발자 지침(선택 사항)입니다.  
`disable_paste_burst`| `boolean`| TUI에서 폭풍 붙여넣기 감지를 비활성화합니다.  
`experimental_compact_prompt_file`| `string (path)`| 파일에서 압축 프롬프트 재정의를 로드합니다(실험적).  
`experimental_use_freeform_apply_patch`| `boolean`| freeform apply_patch를 활성화하는 레거시 이름입니다; `[features].apply_patch_freeform` 또는 `codex --enable apply_patch_freeform`을 사용하는 것이 좋습니다.  
`experimental_use_unified_exec_tool`| `boolean`| unified exec를 활성화하는 레거시 이름입니다; `[features].unified_exec` 또는 `codex --enable unified_exec`을 사용하는 것이 좋습니다.  
`features.apply_patch_freeform`| `boolean`| freeform `apply_patch` 도구를 노출합니다(실험적).  
`features.apps`| `boolean`| ChatGPT Apps/커넥터 지원을 활성화합니다(실험적).  
`features.apps_mcp_gateway`| `boolean`| Apps MCP 호출을 레거시 라우팅 대신 OpenAI 커넥터 MCP 게이트웨이(`https://api.openai.com/v1/connectors/mcp/`)를 통해 라우팅합니다(실험적).  
`features.child_agents_md`| `boolean`| AGENTS.md가 없어도 AGENTS.md 범위/우선순위 가이드를 추가합니다(실험적).  
`features.collaboration_modes`| `boolean`| 플랜 모드 등 협업 모드를 활성화합니다(안정적; 기본 활성).  
`features.elevated_windows_sandbox`| `boolean`| 향상된 Windows 샌드박스 파이프라인을 활성화합니다(실험적).  
`features.experimental_windows_sandbox`| `boolean`| Windows 제한 토큰 샌드박스를 실행합니다(실험적).  
`features.multi_agent`| `boolean`| 멀티 에이전트 협업 도구(`spawn_agent`, `send_input`, `resume_agent`, `wait`, `close_agent`)를 활성화합니다(실험적; 기본 비활성).

`features.personality`| `boolean`| 퍼스널리티 선택 컨트롤을 활성화합니다 (안정적; 기본적으로 켜짐).  
`features.powershell_utf8`| `boolean`| PowerShell 출력이 UTF-8을 사용하도록 강제합니다 (기본값 true).  
`features.remote_models`| `boolean`| 준비 상태를 표시하기 전에 원격 모델 목록을 새로 고칩니다 (실험적).  
`features.request_rule`| `boolean`| 에스컬레이션 요청에서 `prefix_rule` 제안을 제공하는 Smart 승인을 활성화합니다 (안정적; 기본적으로 켜짐).  
`features.runtime_metrics`| `boolean`| TUI 턴 구분선에 런타임 메트릭 요약을 표시합니다 (실험적).  
`features.search_tool`| `boolean`| 앱 MCP 도구를 호출하기 전에 앱 도구를 탐색하도록 `search_tool_bm25`를 활성화합니다 (실험적).  
`features.shell_snapshot`| `boolean`| 반복 명령을 빠르게 실행하도록 셸 환경을 스냅샷합니다 (베타).  
`features.shell_tool`| `boolean`| 명령 실행을 위한 기본 `shell` 도구를 활성화합니다 (안정적; 기본적으로 켜짐).  
`features.unified_exec`| `boolean`| 통합 PTY 기반 exec 도구를 사용합니다 (베타).  
`features.use_linux_sandbox_bwrap`| `boolean`| bubblewrap 기반 Linux 샌드박스 파이프라인을 사용합니다 (실험적; 기본적으로 꺼짐).  
`features.web_search`| `boolean`| 더 이상 사용되지 않는 레거시 토글입니다; 상위 `web_search` 설정을 사용하세요.  
`features.web_search_cached`| `boolean`| 더 이상 사용되지 않는 레거시 토글입니다. `web_search`가 설정되지 않으면 true가 `web_search = "cached"`로 매핑됩니다.  
`features.web_search_request`| `boolean`| 더 이상 사용되지 않는 레거시 토글입니다. `web_search`가 설정되지 않으면 true가 `web_search = "live"`로 매핑됩니다.  
`feedback.enabled`| `boolean`| Codex 전반에서 `/feedback`을 통해 피드백 제출을 활성화합니다 (기본값: true).  
`file_opener`| `vscode | vscode-insiders | windsurf | cursor | none`| Codex 출력에서 인용을 열 때 사용하는 URI 스킴입니다 (기본값: `vscode`).  
`forced_chatgpt_workspace_id`| `string (uuid)`| ChatGPT 로그인을 특정 워크스페이스 식별자로 제한합니다.  
`forced_login_method`| `chatgpt | api`| Codex를 특정 인증 방식으로 제한합니다.  
`hide_agent_reasoning`| `boolean`| TUI와 `codex exec` 출력에서 추론 이벤트를 숨깁니다.  
`history.max_bytes`| `number`| 설정하면 가장 오래된 항목을 삭제하여 history 파일 크기를 바이트 단위로 제한합니다.  
`history.persistence`| `save-all | none`| Codex가 history.jsonl에 세션 기록을 저장할지 제어합니다.  
`include_apply_patch_tool`| `boolean`| 프리폼 apply_patch를 활성화하는 레거시 이름입니다; `[features].apply_patch_freeform`을 사용하세요.  
`instructions`| `string`| 향후 사용을 위해 예약되어 있습니다; `model_instructions_file` 또는 `AGENTS.md`를 권장합니다.  
`log_dir`| `string (path)`| Codex가 로그 파일(예: `codex-tui.log`)을 기록하는 디렉터리입니다; 기본값은 `$CODEX_HOME/log`입니다.  
`mcp_oauth_callback_port`| `integer`| MCP OAuth 로그인 중 사용되는 로컬 HTTP 콜백 서버의 선택적 고정 포트입니다. 설정하지 않으면 Codex가 OS가 선택한 임시 포트에 바인딩합니다.  
`mcp_oauth_credentials_store`| `auto | file | keyring`| MCP OAuth 자격 증명을 저장할 위치를 지정합니다.  
`mcp_servers.<id>.args`| `array<string>`| MCP stdio 서버 명령에 전달되는 인수입니다.  
`mcp_servers.<id>.bearer_token_env_var`| `string`| MCP HTTP 서버용 베어러 토큰을 제공하는 환경 변수를 지정합니다.  
`mcp_servers.<id>.command`| `string`| MCP stdio 서버를 실행하는 명령입니다.  
`mcp_servers.<id>.cwd`| `string`| MCP stdio 서버 프로세스의 작업 디렉터리입니다.  
`mcp_servers.<id>.disabled_tools`| `array<string>`| MCP 서버에서 `enabled_tools` 이후에 적용되는 거부 목록입니다.  
`mcp_servers.<id>.enabled`| `boolean`| 구성을 삭제하지 않고 MCP 서버를 비활성화합니다.  
`mcp_servers.<id>.enabled_tools`| `array<string>`| MCP 서버가 노출하는 도구 이름의 허용 목록입니다.  
`mcp_servers.<id>.env`| `map<string,string>`| MCP stdio 서버로 전달되는 환경 변수입니다.  
`mcp_servers.<id>.env_http_headers`| `map<string,string>`| MCP HTTP 서버를 위해 환경 변수에서 채워지는 HTTP 헤더입니다.  
`mcp_servers.<id>.env_vars`| `array<string>`| MCP stdio 서버에 대해 허용 목록에 추가할 추가 환경 변수입니다.

`mcp_servers.<id>.http_headers`| `map<string,string>`| 각 MCP HTTP 요청에 포함되는 정적 HTTP 헤더입니다.  
`mcp_servers.<id>.required`| `boolean`| true이면 활성화된 해당 MCP 서버가 초기화되지 못할 때 시작/재개에 실패합니다.  
`mcp_servers.<id>.startup_timeout_ms`| `number`| 밀리초 단위의 `startup_timeout_sec` 별칭입니다.  
`mcp_servers.<id>.startup_timeout_sec`| `number`| MCP 서버의 기본 10초 시작 제한 시간을 재정의합니다.  
`mcp_servers.<id>.tool_timeout_sec`| `number`| MCP 서버의 도구별 기본 60초 제한 시간을 재정의합니다.  
`mcp_servers.<id>.url`| `string`| MCP 스트리머블 HTTP 서버의 엔드포인트입니다.  
`model`| `string`| 사용할 모델입니다(예: `gpt-5-codex`).  
`model_auto_compact_token_limit`| `number`| 자동 기록 압축을 트리거하는 토큰 임계값입니다(미설정 시 모델 기본값 사용).  
`model_context_window`| `number`| 현재 모델에서 사용할 수 있는 컨텍스트 윈도 토큰 수입니다.  
`model_instructions_file`| `string (path)`| `AGENTS.md` 대신 사용할 내장 지침 대체 파일입니다.  
`model_provider`| `string`| `model_providers`에 정의된 공급자 ID입니다(기본값: `openai`).  
`model_providers.<id>.base_url`| `string`| 모델 공급자의 API 기본 URL입니다.  
`model_providers.<id>.env_http_headers`| `map<string,string>`| 존재할 경우 환경 변수에서 채워지는 HTTP 헤더입니다.  
`model_providers.<id>.env_key`| `string`| 공급자 API 키를 제공하는 환경 변수입니다.  
`model_providers.<id>.env_key_instructions`| `string`| 공급자 API 키에 대한 선택적 설정 안내입니다.  
`model_providers.<id>.experimental_bearer_token`| `string`| 공급자에 직접 사용하는 베어러 토큰입니다(권장하지 않음; `env_key` 사용).  
`model_providers.<id>.http_headers`| `map<string,string>`| 공급자 요청에 추가되는 정적 HTTP 헤더입니다.  
`model_providers.<id>.name`| `string`| 사용자 정의 모델 공급자의 표시 이름입니다.  
`model_providers.<id>.query_params`| `map<string,string>`| 공급자 요청에 추가되는 추가 쿼리 매개변수입니다.  
`model_providers.<id>.request_max_retries`| `number`| 공급자에 대한 HTTP 요청 재시도 횟수입니다(기본값: 4).  
`model_providers.<id>.requires_openai_auth`| `boolean`| 공급자가 OpenAI 인증을 사용합니다(기본값: false).  
`model_providers.<id>.stream_idle_timeout_ms`| `number`| 밀리초 단위 SSE 스트림 유휴 제한 시간입니다(기본값: 300000).  
`model_providers.<id>.stream_max_retries`| `number`| SSE 스트림 중단 시 재시도 횟수입니다(기본값: 5).  
`model_providers.<id>.wire_api`| `chat | responses`| 공급자가 사용하는 프로토콜입니다(생략 시 기본값 `chat`).  
`model_reasoning_effort`| `minimal | low | medium | high | xhigh`| 지원되는 모델의 추론 노력을 조정합니다(Responses API 한정; `xhigh`는 모델에 따라 다름).  
`model_reasoning_summary`| `auto | concise | detailed | none`| 추론 요약의 상세 수준을 선택하거나 요약을 완전히 비활성화합니다.  
`model_supports_reasoning_summaries`| `boolean`| Codex가 추론 메타데이터를 전송할지 여부를 강제로 지정합니다.  
`model_verbosity`| `low | medium | high`| GPT-5 Responses API의 상세도를 제어합니다(기본값: `medium`).  
`notice.hide_full_access_warning`| `boolean`| 전체 액세스 경고 프롬프트에 대한 확인 여부를 추적합니다.  
`notice.hide_gpt-5.1-codex-max_migration_prompt`| `boolean`| gpt-5.1-codex-max 마이그레이션 프롬프트 확인 여부를 추적합니다.  
`notice.hide_gpt5_1_migration_prompt`| `boolean`| GPT-5.1 마이그레이션 프롬프트 확인 여부를 추적합니다.  
`notice.hide_rate_limit_model_nudge`| `boolean`| 레이트 리밋 모델 전환 알림의 수신 거부 상태를 추적합니다.  
`notice.hide_world_writable_warning`| `boolean`| Windows 전역 쓰기 가능 디렉터리 경고 확인 여부를 추적합니다.  
`notice.model_migrations`| `map<string,string>`| 기존 모델에서 새 모델로의 매핑을 확인된 마이그레이션으로 추적합니다.  
`notify`| `array<string>`| 알림에 사용되는 명령입니다; Codex에서 JSON 페이로드를 전달받습니다.  
`oss_provider`| `lmstudio | ollama`| `--oss`로 실행할 때 사용하는 기본 로컬 공급자입니다(미설정 시 프롬프트로 선택).

`otel.environment`| `string`| 발생한 OpenTelemetry 이벤트에 적용되는 환경 태그(기본값: `dev`).  
`otel.exporter`| `none | otlp-http | otlp-grpc`| OpenTelemetry 내보내기를 선택하고 필요한 엔드포인트 메타데이터를 제공합니다.  
`otel.exporter.<id>.endpoint`| `string`| OTEL 로그용 내보내기 엔드포인트입니다.  
`otel.exporter.<id>.headers`| `map<string,string>`| OTEL 내보내기 요청에 포함되는 정적 헤더입니다.  
`otel.exporter.<id>.protocol`| `binary | json`| OTLP/HTTP 내보내기가 사용하는 프로토콜입니다.  
`otel.exporter.<id>.tls.ca-certificate`| `string`| OTEL 내보내기 TLS에 사용할 CA 인증서 경로입니다.  
`otel.exporter.<id>.tls.client-certificate`| `string`| OTEL 내보내기 TLS에 사용할 클라이언트 인증서 경로입니다.  
`otel.exporter.<id>.tls.client-private-key`| `string`| OTEL 내보내기 TLS에 사용할 클라이언트 개인 키 경로입니다.  
`otel.log_user_prompt`| `boolean`| OpenTelemetry 로그와 함께 원본 사용자 프롬프트를 내보내도록 옵트인합니다.  
`otel.trace_exporter`| `none | otlp-http | otlp-grpc`| OpenTelemetry 트레이스 내보내기를 선택하고 필요한 엔드포인트 메타데이터를 제공합니다.  
`otel.trace_exporter.<id>.endpoint`| `string`| OTEL 로그용 트레이스 내보내기 엔드포인트입니다.  
`otel.trace_exporter.<id>.headers`| `map<string,string>`| OTEL 트레이스 내보내기 요청에 포함되는 정적 헤더입니다.  
`otel.trace_exporter.<id>.protocol`| `binary | json`| OTLP/HTTP 트레이스 내보내기가 사용하는 프로토콜입니다.  
`otel.trace_exporter.<id>.tls.ca-certificate`| `string`| OTEL 트레이스 내보내기 TLS에 사용할 CA 인증서 경로입니다.  
`otel.trace_exporter.<id>.tls.client-certificate`| `string`| OTEL 트레이스 내보내기 TLS에 사용할 클라이언트 인증서 경로입니다.  
`otel.trace_exporter.<id>.tls.client-private-key`| `string`| OTEL 트레이스 내보내기 TLS에 사용할 클라이언트 개인 키 경로입니다.  
`personality`| `none | friendly | pragmatic`| `supportsPersonality`를 광고하는 모델의 기본 의사소통 스타일이며, 스레드나 턴별 또는 `/personality`로 재정의할 수 있습니다.  
`profile`| `string`| 시작 시 적용되는 기본 프로필입니다(`--profile`과 동일).  
`profiles.<name>.*`| `various`| 지원되는 구성 키에 대한 프로필 범위 재정의입니다.  
`profiles.<name>.experimental_use_freeform_apply_patch`| `boolean`| 자유형 apply_patch를 활성화하는 레거시 이름으로, `[features].apply_patch_freeform`을 사용하는 것이 좋습니다.  
`profiles.<name>.experimental_use_unified_exec_tool`| `boolean`| unified exec를 활성화하는 레거시 이름으로, `[features].unified_exec`을 사용하는 것이 좋습니다.  
`profiles.<name>.include_apply_patch_tool`| `boolean`| 자유형 apply_patch를 활성화하는 레거시 이름으로, `[features].apply_patch_freeform`을 사용하는 것이 좋습니다.  
`profiles.<name>.oss_provider`| `lmstudio | ollama`| `--oss` 세션에 사용할 프로필 범위 OSS 공급자입니다.  
`profiles.<name>.personality`| `none | friendly | pragmatic`| 지원되는 모델에 대한 프로필 범위 의사소통 스타일 재정의입니다.  
`profiles.<name>.web_search`| `disabled | cached | live`| 프로필 범위 웹 검색 모드 재정의입니다(기본값: `"cached"`).  
`project_doc_fallback_filenames`| `array<string>`| `AGENTS.md`가 없을 때 추가로 시도할 파일 이름 목록입니다.  
`project_doc_max_bytes`| `number`| 프로젝트 지침을 생성할 때 `AGENTS.md`에서 읽을 최대 바이트 수입니다.  
`project_root_markers`| `array<string>`| 프로젝트 루트 마커 파일 이름 목록으로, 상위 디렉터리에서 프로젝트 루트를 찾을 때 사용됩니다.  
`projects.<path>.trust_level`| `string`| 프로젝트 또는 작업 트리를 `"trusted"` 또는 `"untrusted"`로 표시합니다. 신뢰되지 않는 프로젝트는 프로젝트 범위 `.codex/` 레이어를 건너뜁니다.  
`review_model`| `string`| `/review`에 사용되는 선택적 모델 재정의이며, 기본값은 현재 세션 모델입니다.  
`sandbox_mode`| `read-only | workspace-write | danger-full-access`| 명령 실행 중 파일 시스템 및 네트워크 액세스를 위한 샌드박스 정책입니다.  
`sandbox_workspace_write.exclude_slash_tmp`| `boolean`| workspace-write 모드에서 `/tmp`를 쓰기 가능 루트에서 제외합니다.  
`sandbox_workspace_write.exclude_tmpdir_env_var`| `boolean`| workspace-write 모드에서 `$TMPDIR`를 쓰기 가능 루트에서 제외합니다.

`sandbox_workspace_write.network_access`| `boolean`| workspace-write 샌드박스 내부에서 아웃바운드 네트워크 액세스를 허용합니다.  
`sandbox_workspace_write.writable_roots`| `array<string>`| `sandbox_mode = "workspace-write"`일 때 추가로 쓸 수 있는 루트 목록입니다.  
`shell_environment_policy.exclude`| `array<string>`| 기본 제외 이후 환경 변수를 제거하기 위한 글롭 패턴입니다.  
`shell_environment_policy.experimental_use_profile`| `boolean`| 하위 프로세스를 생성할 때 사용자 셸 프로필을 사용합니다.  
`shell_environment_policy.ignore_default_excludes`| `boolean`| 다른 필터가 실행되기 전에 KEY/SECRET/TOKEN을 포함하는 변수를 유지합니다.  
`shell_environment_policy.include_only`| `array<string>`| 패턴 화이트리스트입니다; 설정되면 일치하는 변수만 유지됩니다.  
`shell_environment_policy.inherit`| `all | core | none`| 하위 프로세스를 생성할 때 기본 환경 상속 수준을 지정합니다.  
`shell_environment_policy.set`| `map<string,string>`| 모든 하위 프로세스에 주입되는 명시적 환경 재정의입니다.  
`show_raw_agent_reasoning`| `boolean`| 활성 모델이 원시 추론 내용을 내보낼 때 이를 노출합니다.  
`skills.config`| `array<object>`| config.toml에 저장된 스킬별 활성화 재정의입니다.  
`skills.config.<index>.enabled`| `boolean`| 참조된 스킬을 활성화하거나 비활성화합니다.  
`skills.config.<index>.path`| `string (path)`| `SKILL.md`가 포함된 스킬 폴더의 경로입니다.  
`suppress_unstable_features_warning`| `boolean`| 개발 중인 기능 플래그가 활성화될 때 표시되는 경고를 숨깁니다.  
`tool_output_token_limit`| `number`| 히스토리에 개별 도구/함수 출력을 저장할 때 사용할 토큰 한도입니다.  
`tools.web_search`| `boolean`| 웹 검색을 위한 더 이상 사용되지 않는 레거시 토글입니다; 최상위 `web_search` 설정을 사용하는 것이 좋습니다.  
`tui`| `table`| 인라인 데스크톱 알림 활성화와 같은 TUI 전용 옵션입니다.  
`tui.alternate_screen`| `auto | always | never`| TUI의 대체 화면 사용을 제어합니다(기본값: auto; auto는 스크롤백을 유지하기 위해 Zellij에서는 건너뜁니다).  
`tui.animations`| `boolean`| 터미널 애니메이션(환영 화면, 반짝임, 스피너)을 활성화합니다(기본값: true).  
`tui.notification_method`| `auto | osc9 | bel`| 포커스 밖 터미널 알림에 사용할 알림 방식을 지정합니다(기본값: auto).  
`tui.notifications`| `boolean | array<string>`| TUI 알림을 활성화하고 필요하면 특정 이벤트 유형으로 제한합니다.  
`tui.show_tooltips`| `boolean`| TUI 환영 화면에서 온보딩 툴팁을 표시합니다(기본값: true).  
`tui.status_line`| `array<string> | null`| TUI 하단 상태줄 항목 식별자의 순서 목록입니다. `null`은 상태줄을 비활성화합니다.  
`web_search`| `disabled | cached | live`| 웹 검색 모드입니다(기본값: `"cached"`; cached는 OpenAI 관리 인덱스를 사용하며 실시간 페이지를 가져오지 않습니다; `--yolo` 또는 다른 전체 액세스 샌드박스 설정에서는 기본값이 `"live"`입니다). 최신 데이터를 가져오려면 `"live"`를 사용하고, 도구를 제거하려면 `"disabled"`를 사용하세요.  
`windows_wsl_setup_acknowledged`| `boolean`| Windows 온보딩 확인 여부를 추적합니다(Windows 전용).  

키

`agents.<name>.config_file`

유형 / 값

`string (path)`

세부 정보

해당 역할에 대한 TOML 구성 레이어 경로입니다. 상대 경로는 역할을 선언한 구성 파일 기준으로 해석됩니다.

키

`agents.<name>.description`

유형 / 값

`string`

세부 정보

해당 에이전트 유형을 선택하고 생성할 때 Codex에 표시되는 역할 안내입니다.

키

`agents.max_threads`

유형 / 값

`number`

세부 정보

동시에 열 수 있는 에이전트 스레드의 최대 개수입니다.

키

`approval_policy`

유형 / 값

`untrusted | on-request | never`

세부 정보

Codex가 명령을 실행하기 전에 승인을 위해 중지하는 시점을 제어합니다. `on-failure`는 더 이상 사용되지 않으므로 대화형 실행에는 `on-request`, 비대화형 실행에는 `never`를 사용하세요.

키

`apps.<id>.disabled_reason`

유형 / 값

`unknown | user`

세부 정보

앱/커넥터가 비활성화될 때 선택적으로 첨부되는 이유입니다.

키

`apps.<id>.enabled`

유형 / 값

`boolean`

세부 정보

특정 앱/커넥터(식별자는 id 기준)를 활성화하거나 비활성화합니다(기본값: true).

키

`chatgpt_base_url`

유형 / 값

`string`

세부 정보

ChatGPT 로그인 흐름에 사용되는 기본 URL을 재정의합니다.

키

`check_for_update_on_startup`

유형 / 값

`boolean`

세부 정보

시작 시 Codex 업데이트를 확인합니다(업데이트를 중앙에서 관리하는 경우에만 false로 설정).

키

`cli_auth_credentials_store`

유형 / 값

`file | keyring | auto`

세부 정보

CLI가 캐시된 자격 증명을 저장하는 위치를 제어합니다(auth.json 파일 기반 대 OS 키체인).

키

`compact_prompt`

유형 / 값

`string`

세부 정보

히스토리 압축 프롬프트를 인라인으로 재정의합니다.

키

`developer_instructions`

유형 / 값

`string`

세부 정보

세션에 주입되는 추가 개발자 지침(선택 사항)입니다.

키

`disable_paste_burst`

유형 / 값

`boolean`

세부 정보

TUI에서 버스트 붙여넣기 감지를 비활성화합니다.

키

`experimental_compact_prompt_file`

유형 / 값

`string (path)`

세부 정보

파일에서 압축 프롬프트 재정의를 로드합니다(실험적).

키

`experimental_use_freeform_apply_patch`

유형 / 값

`boolean`

세부 정보

freeform apply_patch를 활성화하기 위한 이전 이름입니다. `[features].apply_patch_freeform` 또는 `codex --enable apply_patch_freeform` 사용을 권장합니다.

키

`experimental_use_unified_exec_tool`

유형 / 값

`boolean`

세부 정보

unified exec를 활성화하기 위한 이전 이름입니다. `[features].unified_exec` 또는 `codex --enable unified_exec` 사용을 권장합니다.

키

`features.apply_patch_freeform`

유형 / 값

`boolean`

세부 정보

freeform `apply_patch` 도구를 노출합니다(실험적).

키

`features.apps`

유형 / 값

`boolean`

세부 정보

ChatGPT Apps/커넥터 지원을 활성화합니다(실험적).

키

`features.apps_mcp_gateway`

유형 / 값

`boolean`

세부 정보

Apps MCP 호출을 기존 라우팅 대신 OpenAI 커넥터 MCP 게이트웨이(`https://api.openai.com/v1/connectors/mcp/`)로 라우팅합니다(실험적).

키

`features.child_agents_md`

유형 / 값

`boolean`

세부 정보

AGENTS.md가 없어도 AGENTS.md 범위/우선순위 가이던스를 추가합니다(실험적).

키

`features.collaboration_modes`

유형 / 값

`boolean`

세부 정보

플랜 모드와 같은 협업 모드를 활성화합니다(안정적; 기본적으로 켜짐).

키

`features.elevated_windows_sandbox`

유형 / 값

`boolean`

세부 정보

상승된 Windows 샌드박스 파이프라인을 활성화합니다(실험적).

키

`features.experimental_windows_sandbox`

유형 / 값

`boolean`

세부 정보

Windows 제한 토큰 샌드박스를 실행합니다(실험적).

키

`features.multi_agent`

유형 / 값

`boolean`

세부 정보

`spawn_agent`, `send_input`, `resume_agent`, `wait`, `close_agent`와 같은 다중 에이전트 협업 도구를 활성화합니다(실험적; 기본적으로 꺼짐).

키

`features.personality`

유형 / 값

`boolean`

세부 정보

개인화 선택 컨트롤을 활성화합니다(안정적; 기본적으로 켜짐).

키

`features.powershell_utf8`

유형 / 값

`boolean`

세부 정보

PowerShell UTF-8 출력을 강제합니다(기본값 true).

키

`features.remote_models`

유형 / 값

`boolean`

세부 정보

준비 상태를 표시하기 전에 원격 모델 목록을 새로 고칩니다(실험적).

키

`features.request_rule`

유형 / 값

`boolean`

세부 정보

에스컬레이션 요청 시 `prefix_rule` 제안을 제공하는 Smart approvals를 활성화합니다(안정적; 기본적으로 켜짐).

키

`features.runtime_metrics`

유형 / 값

`boolean`

세부 정보

TUI 턴 구분자에 런타임 메트릭 요약을 표시합니다(실험적).

키

`features.search_tool`

유형 / 값

`boolean`

세부 정보

앱 MCP 도구를 호출하기 전에 Apps 도구 검색용 `search_tool_bm25`를 활성화합니다(실험적).

키

`features.shell_snapshot`

유형 / 값

`boolean`

세부 정보

반복 명령을 가속하기 위해 셸 환경을 스냅샷합니다(베타).

키

`features.shell_tool`

유형 / 값

`boolean`

세부 정보

명령 실행을 위한 기본 `shell` 도구를 활성화합니다(안정적; 기본적으로 켜짐).

키

`features.unified_exec`

유형 / 값

`boolean`

세부 정보

통합 PTY 기반 exec 도구를 사용합니다(베타).

키

`features.use_linux_sandbox_bwrap`

유형 / 값

`boolean`

세부 정보

bubblewrap 기반 Linux 샌드박스 파이프라인을 사용합니다(실험적; 기본적으로 꺼짐).

키

`features.web_search`

유형 / 값

`boolean`

세부 정보

더 이상 사용되지 않는 레거시 토글입니다. 상위 수준의 `web_search` 설정을 사용하는 편이 좋습니다.

키

`features.web_search_cached`

유형 / 값

`boolean`

세부 정보

더 이상 사용되지 않는 레거시 토글입니다. `web_search` 가 설정되지 않은 경우, true 는 `web_search = "cached"` 로 매핑됩니다.

키

`features.web_search_request`

유형 / 값

`boolean`

세부 정보

더 이상 사용되지 않는 레거시 토글입니다. `web_search` 가 설정되지 않은 경우, true 는 `web_search = "live"` 로 매핑됩니다.

키

`feedback.enabled`

유형 / 값

`boolean`

세부 정보

Codex 전반에서 `/feedback` 을 통한 피드백 제출을 활성화합니다(기본값: true).

키

`file_opener`

유형 / 값

`vscode | vscode-insiders | windsurf | cursor | none`

세부 정보

Codex 출력에서 인용을 열 때 사용하는 URI 스킴입니다(기본값: `vscode`).

키

`forced_chatgpt_workspace_id`

유형 / 값

`string (uuid)`

세부 정보

ChatGPT 로그인을 특정 워크스페이스 식별자로 제한합니다.

키

`forced_login_method`

유형 / 값

`chatgpt | api`

세부 정보

Codex 를 특정 인증 방법으로 제한합니다.

키

`hide_agent_reasoning`

유형 / 값

`boolean`

세부 정보

TUI 와 `codex exec` 출력 모두에서 추론 이벤트를 숨깁니다.

키

`history.max_bytes`

유형 / 값

`number`

세부 정보

설정된 경우, 가장 오래된 항목을 삭제해 기록 파일 크기를 바이트 단위로 제한합니다.

키

`history.persistence`

유형 / 값

`save-all | none`

세부 정보

Codex 가 session transcripts 를 history.jsonl 에 저장할지 제어합니다.

키

`include_apply_patch_tool`

유형 / 값

`boolean`

세부 정보

자유 형식 apply_patch 를 활성화하는 레거시 이름입니다. `[features].apply_patch_freeform` 을 사용하는 편이 좋습니다.

키

`instructions`

유형 / 값

`string`

세부 정보

향후 사용을 위해 예약되어 있습니다. `model_instructions_file` 또는 `AGENTS.md` 를 권장합니다.

키

`log_dir`

유형 / 값

`string (path)`

세부 정보

Codex 가 로그 파일을 저장하는 디렉터리입니다(예: `codex-tui.log`); 기본값은 `$CODEX_HOME/log` 입니다.

키

`mcp_oauth_callback_port`

유형 / 값

`integer`

세부 정보

MCP OAuth 로그인 중 사용하는 로컬 HTTP 콜백 서버의 선택적 고정 포트입니다. 설정되지 않으면 Codex 는 OS 가 선택한 임의 포트에 바인딩합니다.

키

`mcp_oauth_credentials_store`

유형 / 값

`auto | file | keyring`

세부 정보

MCP OAuth 자격 증명의 기본 저장소입니다.

키

`mcp_servers.<id>.args`

유형 / 값

`array<string>`

세부 정보

MCP stdio 서버 명령에 전달되는 인수입니다.

키

`mcp_servers.<id>.bearer_token_env_var`

유형 / 값

`string`

세부 정보

MCP HTTP 서버의 bearer 토큰을 제공하는 환경 변수입니다.

키

`mcp_servers.<id>.command`

유형 / 값

`string`

세부 정보

MCP stdio 서버의 실행 명령입니다.

키

`mcp_servers.<id>.cwd`

유형 / 값

`string`

세부 정보

MCP stdio 서버 프로세스의 작업 디렉터리입니다.

키

`mcp_servers.<id>.disabled_tools`

유형 / 값

`array<string>`

세부 정보

MCP 서버에 대해 `enabled_tools` 이후 적용되는 거부 목록입니다.

키

`mcp_servers.<id>.enabled`

유형 / 값

`boolean`

세부 정보

구성을 제거하지 않고 MCP 서버를 비활성화합니다.

키

`mcp_servers.<id>.enabled_tools`

유형 / 값

`array<string>`

세부 정보

MCP 서버가 노출하는 도구 이름의 허용 목록입니다.

키

`mcp_servers.<id>.env`

유형 / 값

`map<string,string>`

세부 정보

MCP stdio 서버로 전달되는 환경 변수입니다.

키

`mcp_servers.<id>.env_http_headers`

유형 / 값

`map<string,string>`

세부 정보

환경 변수에서 채워져 MCP HTTP 서버에 사용되는 HTTP 헤더입니다.

키

`mcp_servers.<id>.env_vars`

유형 / 값

`array<string>`

세부 정보

MCP stdio 서버에 대해 화이트리스트에 추가할 추가 환경 변수입니다.

키

`mcp_servers.<id>.http_headers`

유형 / 값

`map<string,string>`

세부 정보

각 MCP HTTP 요청에 포함되는 정적 HTTP 헤더입니다.

키

`mcp_servers.<id>.required`

유형 / 값

`boolean`

세부 정보

true 인 경우, 이 활성화된 MCP 서버를 초기화하지 못하면 시작/재개가 실패합니다.

키

`mcp_servers.<id>.startup_timeout_ms`

유형 / 값

`number`

세부 정보

밀리초 단위의 `startup_timeout_sec` 별칭입니다.

키

`mcp_servers.<id>.startup_timeout_sec`

유형 / 값

`number`

세부 정보

MCP 서버의 기본 10초 시작 제한 시간을 재정의합니다.

Key

`mcp_servers.<id>.tool_timeout_sec`

유형 / 값

`number`

세부 정보

MCP 서버의 도구별 기본 60초 제한 시간을 재정의합니다.

Key

`mcp_servers.<id>.url`

유형 / 값

`string`

세부 정보

MCP 스트리밍 HTTP 서버의 엔드포인트입니다.

Key

`model`

유형 / 값

`string`

세부 정보

사용할 모델입니다(예: `gpt-5-codex`).

Key

`model_auto_compact_token_limit`

유형 / 값

`number`

세부 정보

자동 기록 압축을 트리거하는 토큰 임계값입니다(설정하지 않으면 모델 기본값 사용).

Key

`model_context_window`

유형 / 값

`number`

세부 정보

활성 모델에 제공되는 컨텍스트 윈도 토큰 수입니다.

Key

`model_instructions_file`

유형 / 값

`string (path)`

세부 정보

`AGENTS.md` 대신 사용할 내장 지침 대체 파일입니다.

Key

`model_provider`

유형 / 값

`string`

세부 정보

`model_providers`에 정의된 공급자 ID입니다(기본값: `openai`).

Key

`model_providers.<id>.base_url`

유형 / 값

`string`

세부 정보

모델 공급자의 API 기본 URL입니다.

Key

`model_providers.<id>.env_http_headers`

유형 / 값

`map<string,string>`

세부 정보

환경 변수에서 존재할 경우 채워지는 HTTP 헤더입니다.

Key

`model_providers.<id>.env_key`

유형 / 값

`string`

세부 정보

공급자 API 키를 제공하는 환경 변수입니다.

Key

`model_providers.<id>.env_key_instructions`

유형 / 값

`string`

세부 정보

공급자 API 키 설정에 대한 선택적 안내입니다.

Key

`model_providers.<id>.experimental_bearer_token`

유형 / 값

`string`

세부 정보

공급자용 직접 Bearer 토큰입니다(권장되지 않으며 `env_key` 사용 권장).

Key

`model_providers.<id>.http_headers`

유형 / 값

`map<string,string>`

세부 정보

공급자 요청에 추가되는 정적 HTTP 헤더입니다.

Key

`model_providers.<id>.name`

유형 / 값

`string`

세부 정보

사용자 지정 모델 공급자의 표시 이름입니다.

Key

`model_providers.<id>.query_params`

유형 / 값

`map<string,string>`

세부 정보

공급자 요청에 추가되는 추가 쿼리 매개변수입니다.

Key

`model_providers.<id>.request_max_retries`

유형 / 값

`number`

세부 정보

공급자에 대한 HTTP 요청 재시도 횟수입니다(기본값: 4).

Key

`model_providers.<id>.requires_openai_auth`

유형 / 값

`boolean`

세부 정보

공급자가 OpenAI 인증을 사용합니다(기본값은 false).

Key

`model_providers.<id>.stream_idle_timeout_ms`

유형 / 값

`number`

세부 정보

밀리초 단위 SSE 스트림 유휴 제한 시간입니다(기본값: 300000).

Key

`model_providers.<id>.stream_max_retries`

유형 / 값

`number`

세부 정보

SSE 스트리밍 중단에 대한 재시도 횟수입니다(기본값: 5).

Key

`model_providers.<id>.wire_api`

유형 / 값

`chat | responses`

세부 정보

공급자가 사용하는 프로토콜입니다(생략 시 기본값 `chat`).

Key

`model_reasoning_effort`

유형 / 값

`minimal | low | medium | high | xhigh`

세부 정보

지원되는 모델의 추론 노력을 조정합니다(Responses API 전용; `xhigh`는 모델별로 다름).

Key

`model_reasoning_summary`

유형 / 값

`auto | concise | detailed | none`

세부 정보

추론 요약 상세 수준을 선택하거나 요약을 완전히 비활성화합니다.

Key

`model_supports_reasoning_summaries`

유형 / 값

`boolean`

세부 정보

Codex가 추론 메타데이터를 전송할지 여부를 강제합니다.

Key

`model_verbosity`

유형 / 값

`low | medium | high`

세부 정보

GPT-5 Responses API의 장황함을 제어합니다(기본값: `medium`).

Key

`notice.hide_full_access_warning`

유형 / 값

`boolean`

세부 정보

풀 액세스 경고 프롬프트에 대한 확인 여부를 추적합니다.

Key

`notice.hide_gpt-5.1-codex-max_migration_prompt`

유형 / 값

`boolean`

세부 정보

gpt-5.1-codex-max 마이그레이션 프롬프트에 대한 확인 여부를 추적합니다.

Key

`notice.hide_gpt5_1_migration_prompt`

유형 / 값

`boolean`

세부 정보

GPT-5.1 마이그레이션 프롬프트에 대한 확인 여부를 추적합니다.

Key

`notice.hide_rate_limit_model_nudge`

유형 / 값

`boolean`

세부 정보

요금 제한 모델 전환 알림에 대한 옵트아웃 여부를 추적합니다.

Key

`notice.hide_world_writable_warning`

유형 / 값

`boolean`

세부 정보

Windows 전역-쓰기 가능 디렉터리 경고에 대한 확인 여부를 추적합니다.

키

`notice.model_migrations`

유형 / 값

`map<string,string>`

세부 정보

승인된 모델 마이그레이션을 old->new 매핑으로 추적합니다.

키

`notify`

유형 / 값

`array<string>`

세부 정보

알림을 위해 호출되는 명령으로, Codex에서 전달되는 JSON 페이로드를 수신합니다.

키

`oss_provider`

유형 / 값

`lmstudio | ollama`

세부 정보

`--oss` 로 실행할 때 사용하는 기본 로컬 프로바이더입니다(설정되지 않은 경우 프롬프트로 기본값).

키

`otel.environment`

유형 / 값

`string`

세부 정보

발행되는 OpenTelemetry 이벤트에 적용되는 환경 태그입니다(기본값: `dev`).

키

`otel.exporter`

유형 / 값

`none | otlp-http | otlp-grpc`

세부 정보

OpenTelemetry 익스포터를 선택하고 필요한 엔드포인트 메타데이터를 제공합니다.

키

`otel.exporter.<id>.endpoint`

유형 / 값

`string`

세부 정보

OTEL 로그용 익스포터 엔드포인트입니다.

키

`otel.exporter.<id>.headers`

유형 / 값

`map<string,string>`

세부 정보

OTEL 익스포터 요청에 포함되는 정적 헤더입니다.

키

`otel.exporter.<id>.protocol`

유형 / 값

`binary | json`

세부 정보

OTLP/HTTP 익스포터가 사용하는 프로토콜입니다.

키

`otel.exporter.<id>.tls.ca-certificate`

유형 / 값

`string`

세부 정보

OTEL 익스포터 TLS용 CA 인증서 경로입니다.

키

`otel.exporter.<id>.tls.client-certificate`

유형 / 값

`string`

세부 정보

OTEL 익스포터 TLS용 클라이언트 인증서 경로입니다.

키

`otel.exporter.<id>.tls.client-private-key`

유형 / 값

`string`

세부 정보

OTEL 익스포터 TLS용 클라이언트 개인 키 경로입니다.

키

`otel.log_user_prompt`

유형 / 값

`boolean`

세부 정보

OpenTelemetry 로그와 함께 원본 사용자 프롬프트를 내보내도록 옵트인합니다.

키

`otel.trace_exporter`

유형 / 값

`none | otlp-http | otlp-grpc`

세부 정보

OpenTelemetry 트레이스 익스포터를 선택하고 필요한 엔드포인트 메타데이터를 제공합니다.

키

`otel.trace_exporter.<id>.endpoint`

유형 / 값

`string`

세부 정보

OTEL 로그용 트레이스 익스포터 엔드포인트입니다.

키

`otel.trace_exporter.<id>.headers`

유형 / 값

`map<string,string>`

세부 정보

OTEL 트레이스 익스포터 요청에 포함되는 정적 헤더입니다.

키

`otel.trace_exporter.<id>.protocol`

유형 / 값

`binary | json`

세부 정보

OTLP/HTTP 트레이스 익스포터가 사용하는 프로토콜입니다.

키

`otel.trace_exporter.<id>.tls.ca-certificate`

유형 / 값

`string`

세부 정보

OTEL 트레이스 익스포터 TLS용 CA 인증서 경로입니다.

키

`otel.trace_exporter.<id>.tls.client-certificate`

유형 / 값

`string`

세부 정보

OTEL 트레이스 익스포터 TLS용 클라이언트 인증서 경로입니다.

키

`otel.trace_exporter.<id>.tls.client-private-key`

유형 / 값

`string`

세부 정보

OTEL 트레이스 익스포터 TLS용 클라이언트 개인 키 경로입니다.

키

`personality`

유형 / 값

`none | friendly | pragmatic`

세부 정보

`supportsPersonality` 를 지원한다고 알리는 모델의 기본 소통 스타일이며, 스레드·턴별 또는 `/personality` 로 재정의할 수 있습니다.

키

`profile`

유형 / 값

`string`

세부 정보

초기 구동 시 적용되는 기본 프로필로, `--profile` 과 동일합니다.

키

`profiles.<name>.*`

유형 / 값

`various`

세부 정보

지원되는 어떤 구성 키에도 적용할 수 있는 프로필 범위의 재정의입니다.

키

`profiles.<name>.experimental_use_freeform_apply_patch`

유형 / 값

`boolean`

세부 정보

자유 형식 apply_patch 를 활성화하던 구식 이름이며, `[features].apply_patch_freeform` 을 권장합니다.

키

`profiles.<name>.experimental_use_unified_exec_tool`

유형 / 값

`boolean`

세부 정보

unified exec 를 활성화하던 구식 이름이며, `[features].unified_exec` 을 권장합니다.

키

`profiles.<name>.include_apply_patch_tool`

유형 / 값

`boolean`

세부 정보

자유 형식 apply_patch 를 활성화하던 구식 이름이며, `[features].apply_patch_freeform` 을 권장합니다.

키

`profiles.<name>.oss_provider`

유형 / 값

`lmstudio | ollama`

세부 정보

`--oss` 세션에 대한 프로필 범위 OSS 프로바이더입니다.

키

`profiles.<name>.personality`

유형 / 값

`none | friendly | pragmatic`

세부 정보

지원되는 모델에 대한 프로필 범위 소통 스타일 재정의입니다.

키

`profiles.<name>.web_search`

유형 / 값

`disabled | cached | live`

세부 정보

프로필 범위의 웹 검색 모드 재정의 (기본값: `"cached"`).

키

`project_doc_fallback_filenames`

유형 / 값

`array<string>`

세부 정보

`AGENTS.md`가 없을 때 추가로 시도할 파일 이름.

키

`project_doc_max_bytes`

유형 / 값

`number`

세부 정보

프로젝트 지침을 구성할 때 `AGENTS.md`에서 읽을 최대 바이트 수.

키

`project_root_markers`

유형 / 값

`array<string>`

세부 정보

프로젝트 루트 표시 파일 이름 목록; 상위 디렉터리에서 프로젝트 루트를 검색할 때 사용.

키

`projects.<path>.trust_level`

유형 / 값

`string`

세부 정보

프로젝트 또는 작업 트리를 신뢰/불신으로 표시 (`"trusted"` | `"untrusted"`). 신뢰하지 않는 프로젝트는 프로젝트 범위의 `.codex/` 계층을 건너뜀.

키

`review_model`

유형 / 값

`string`

세부 정보

`/review`에서 사용할 선택적 모델 재정의(기본값은 현재 세션 모델).

키

`sandbox_mode`

유형 / 값

`read-only | workspace-write | danger-full-access`

세부 정보

명령 실행 중 파일 시스템 및 네트워크 액세스를 위한 샌드박스 정책.

키

`sandbox_workspace_write.exclude_slash_tmp`

유형 / 값

`boolean`

세부 정보

workspace-write 모드에서 `/tmp`를 쓰기 가능 루트에서 제외.

키

`sandbox_workspace_write.exclude_tmpdir_env_var`

유형 / 값

`boolean`

세부 정보

workspace-write 모드에서 `$TMPDIR`를 쓰기 가능 루트에서 제외.

키

`sandbox_workspace_write.network_access`

유형 / 값

`boolean`

세부 정보

workspace-write 샌드박스 내부에서 아웃바운드 네트워크 액세스 허용.

키

`sandbox_workspace_write.writable_roots`

유형 / 값

`array<string>`

세부 정보

`sandbox_mode = "workspace-write"`일 때 추가 쓰기 가능 루트.

키

`shell_environment_policy.exclude`

유형 / 값

`array<string>`

세부 정보

기본값 이후 제거할 환경 변수에 대한 glob 패턴.

키

`shell_environment_policy.experimental_use_profile`

유형 / 값

`boolean`

세부 정보

하위 프로세스를 생성할 때 사용자 셸 프로필을 사용.

키

`shell_environment_policy.ignore_default_excludes`

유형 / 값

`boolean`

세부 정보

다른 필터가 실행되기 전에 KEY/SECRET/TOKEN을 포함한 변수를 유지.

키

`shell_environment_policy.include_only`

유형 / 값

`array<string>`

세부 정보

화이트리스트 패턴; 설정되면 일치하는 변수만 유지.

키

`shell_environment_policy.inherit`

유형 / 값

`all | core | none`

세부 정보

하위 프로세스를 생성할 때 기본 환경 상속 수준.

키

`shell_environment_policy.set`

유형 / 값

`map<string,string>`

세부 정보

모든 하위 프로세스에 주입되는 명시적 환경 재정의.

키

`show_raw_agent_reasoning`

유형 / 값

`boolean`

세부 정보

활성 모델이 원시 추론을 출력하면 이를 노출.

키

`skills.config`

유형 / 값

`array<object>`

세부 정보

config.toml에 저장된 스킬별 활성화 재정의.

키

`skills.config.<index>.enabled`

유형 / 값

`boolean`

세부 정보

참조된 스킬을 활성화하거나 비활성화.

키

`skills.config.<index>.path`

유형 / 값

`string (path)`

세부 정보

`SKILL.md`가 포함된 스킬 폴더 경로.

키

`suppress_unstable_features_warning`

유형 / 값

`boolean`

세부 정보

개발 중인 기능 플래그가 활성화될 때 표시되는 경고를 숨김.

키

`tool_output_token_limit`

유형 / 값

`number`

세부 정보

히스토리에 개별 도구/함수 출력을 저장하기 위한 토큰 예산.

키

`tools.web_search`

유형 / 값

`boolean`

세부 정보

더 이상 사용되지 않는 레거시 웹 검색 토글; 최상위 `web_search` 설정을 권장.

키

`tui`

유형 / 값

`table`

세부 정보

인라인 데스크톱 알림 활성화 등 TUI 전용 옵션.

키

`tui.alternate_screen`

유형 / 값

`auto | always | never`

세부 정보

TUI의 대체 화면 사용 제어(기본값: auto; Zellij에서는 스크롤백을 유지하기 위해 자동으로 비활성화).

키

`tui.animations`

유형 / 값

`boolean`

세부 정보

터미널 애니메이션(환영 화면, 반짝임, 스피너) 활성화(기본값: true).

키

`tui.notification_method`

유형 / 값

`auto | osc9 | bel`

세부 정보

포커스를 잃은 터미널 알림에 사용할 알림 방식입니다(기본값: auto).

키

`tui.notifications`

유형 / 값

`boolean | array<string>`

세부 정보

TUI 알림을 활성화하며, 필요하다면 특정 이벤트 유형으로 제한할 수 있습니다.

키

`tui.show_tooltips`

유형 / 값

`boolean`

세부 정보

TUI 환영 화면에서 온보딩 툴팁을 표시합니다(기본값: true).

키

`tui.status_line`

유형 / 값

`array<string> | null`

세부 정보

TUI 하단 상태줄 항목 식별자를 순서대로 지정합니다. `null`은 상태줄을 비활성화합니다.

키

`web_search`

유형 / 값

`disabled | cached | live`

세부 정보

웹 검색 모드입니다(기본값: `"cached"`; cached는 OpenAI에서 관리하는 인덱스를 사용하며 실시간 페이지를 가져오지 않습니다. `--yolo` 또는 다른 전체 액세스 샌드박스 설정을 사용하면 기본값이 `"live"`가 됩니다). 최신 데이터를 가져오려면 `"live"`를, 도구를 제거하려면 `"disabled"`를 사용하세요.

키

`windows_wsl_setup_acknowledged`

유형 / 값

`boolean`

세부 정보

Windows 온보딩 확인 여부를 추적합니다(Windows 전용).

모두 보려면 펼치기

`config.toml`용 최신 JSON 스키마는 [여기](https://developers.openai.com/codex/config-schema.json)에서 확인할 수 있습니다.

VS Code나 Cursor에서 `config.toml`을 편집할 때 자동 완성과 진단을 받으려면 [Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml) 확장을 설치하고 `config.toml` 맨 위에 다음 줄을 추가하세요:
[code] 
    #:schema https://developers.openai.com/codex/config-schema.json
[/code]

참고: `experimental_instructions_file`을 `model_instructions_file`로 변경하세요. Codex는 이전 키를 더 이상 사용하지 않으므로 기존 구성을 새 이름으로 업데이트해야 합니다.

## `requirements.toml`

`requirements.toml`은 사용자가 재정의할 수 없는 보안 민감 설정을 제한하는 관리자 강제 구성 파일입니다. 자세한 내용, 위치, 예시는 [Admin-enforced requirements](https://developers.openai.com/codex/security#admin-enforced-requirements-requirementstoml)를 참조하세요.

ChatGPT Business 및 Enterprise 사용자의 경우 Codex가 클라우드에서 가져온 요구 사항을 적용할 수도 있습니다. 우선순위에 대한 자세한 내용은 보안 페이지를 확인하세요.

Key| Type / Values| Details  
---|---|---  
`allowed_approval_policies`| `array<string>`| `approval_policy`에 허용되는 값입니다.  
`allowed_sandbox_modes`| `array<string>`| `sandbox_mode`에 허용되는 값입니다.  
`allowed_web_search_modes`| `array<string>`| `web_search`에 허용되는 값입니다(`disabled`, `cached`, `live`). `disabled`는 항상 허용되며, 목록이 비어 있으면 사실상 `disabled`만 허용합니다.  
`mcp_servers`| `table`| 활성화할 수 있는 MCP 서버 허용 목록입니다. MCP 서버를 활성화하려면 서버 이름(`<id>`)과 해당 정체성이 모두 일치해야 합니다. 허용 목록에 없거나 정체성이 맞지 않는 MCP 서버는 비활성화됩니다.  
`mcp_servers.<id>.identity`| `table`| 단일 MCP 서버에 대한 정체성 규칙입니다. `command`(stdio) 또는 `url`(스트리밍 HTTP) 중 하나를 설정하세요.  
`mcp_servers.<id>.identity.command`| `string`| `mcp_servers.<id>.command`가 이 명령과 일치할 때 MCP stdio 서버를 허용합니다.  
`mcp_servers.<id>.identity.url`| `string`| `mcp_servers.<id>.url`이 이 URL과 일치할 때 MCP 스트리밍 HTTP 서버를 허용합니다.  
`rules`| `table`| `.rules` 파일과 병합되는 관리자 강제 명령 규칙입니다. 요구 사항 규칙은 제한적이어야 합니다.  
`rules.prefix_rules`| `array<table>`| 강제 프리픽스 규칙 목록입니다. 각 규칙에는 `pattern`과 `decision`이 포함되어야 합니다.  
`rules.prefix_rules[].decision`| `prompt | forbidden`| 필수 항목입니다. 요구 사항 규칙은 prompt 또는 forbidden만 지정할 수 있으며 allow는 사용할 수 없습니다.  
`rules.prefix_rules[].justification`| `string`| 승인 프롬프트나 거부 메시지에 표시되는 선택적 비어 있지 않은 근거입니다.  
`rules.prefix_rules[].pattern`| `array<table>`| 패턴 토큰으로 표현된 명령 프리픽스입니다. 각 토큰은 `token` 또는 `any_of` 중 하나를 설정합니다.  
`rules.prefix_rules[].pattern[].any_of`| `array<string>`| 해당 위치에서 허용되는 대체 토큰 목록입니다.

`rules.prefix_rules[].pattern[].token`| `string`| 이 위치에 단일 리터럴 토큰입니다.  
  
키

`allowed_approval_policies`

유형 / 값

`array<string>`

세부 정보

`approval_policy`에 허용되는 값입니다.

키

`allowed_sandbox_modes`

유형 / 값

`array<string>`

세부 정보

`sandbox_mode`에 허용되는 값입니다.

키

`allowed_web_search_modes`

유형 / 값

`array<string>`

세부 정보

`web_search`(`disabled`, `cached`, `live`)에 허용되는 값입니다. `disabled`는 항상 허용되며, 빈 목록은 사실상 `disabled`만 허용합니다.

키

`mcp_servers`

유형 / 값

`table`

세부 정보

활성화할 수 있는 MCP 서버 허용 목록입니다. 서버 이름(`<id>`)과 아이덴티티가 모두 일치해야 MCP 서버를 활성화할 수 있습니다. 허용 목록에 없거나 아이덴티티가 일치하지 않는 MCP 서버는 비활성화됩니다.

키

`mcp_servers.<id>.identity`

유형 / 값

`table`

세부 정보

단일 MCP 서버에 대한 아이덴티티 규칙입니다. `command`(stdio) 또는 `url`(스트리밍 HTTP) 중 하나를 설정합니다.

키

`mcp_servers.<id>.identity.command`

유형 / 값

`string`

세부 정보

`mcp_servers.<id>.command`가 이 명령과 일치할 때 MCP stdio 서버를 허용합니다.

키

`mcp_servers.<id>.identity.url`

유형 / 값

`string`

세부 정보

`mcp_servers.<id>.url`이 이 URL과 일치할 때 MCP 스트리밍 HTTP 서버를 허용합니다.

키

`rules`

유형 / 값

`table`

세부 정보

`.rules` 파일과 병합된 관리자 강제 명령 규칙입니다. 요구 사항 규칙은 제한적이어야 합니다.

키

`rules.prefix_rules`

유형 / 값

`array<table>`

세부 정보

강제 프리픽스 규칙 목록입니다. 각 규칙에는 `pattern`과 `decision`이 포함되어야 합니다.

키

`rules.prefix_rules[].decision`

유형 / 값

`prompt | forbidden`

세부 정보

필수입니다. 요구 사항 규칙은 허용이 아닌 prompt 또는 forbid만 가능합니다.

키

`rules.prefix_rules[].justification`

유형 / 값

`string`

세부 정보

승인 프롬프트나 거부 메시지에 표시되는 선택적 비어 있지 않은 근거입니다.

키

`rules.prefix_rules[].pattern`

유형 / 값

`array<table>`

세부 정보

패턴 토큰으로 표현된 명령 프리픽스입니다. 각 토큰은 `token` 또는 `any_of`를 설정합니다.

키

`rules.prefix_rules[].pattern[].any_of`

유형 / 값

`array<string>`

세부 정보

이 위치에서 허용되는 대체 토큰 목록입니다.

키

`rules.prefix_rules[].pattern[].token`

유형 / 값

`string`

세부 정보

이 위치에 단일 리터럴 토큰입니다.

전체 보기를 위해 확장
