---
title: 샘플 구성
description: 이 예제 구성을 시작점으로 사용하세요. Codex가 에서 읽어들이는 대부분의 키와 기본값, 짧은 설명이 포함되어 있습니다.
sidebar:
  order: 33
---

# 샘플 구성

Source URL: https://developers.openai.com/codex/config-sample

이 예제 구성을 시작점으로 사용하세요. Codex가 `config.toml`에서 읽어들이는 대부분의 키와 기본값, 짧은 설명이 포함되어 있습니다.

자세한 설명과 가이드:

  * [Config basics](https://developers.openai.com/codex/config-basic)
  * [Advanced Config](https://developers.openai.com/codex/config-advanced)
  * [Config Reference](https://developers.openai.com/codex/config-reference)
  * [Sandbox and approvals](https://developers.openai.com/codex/security#sandbox-and-approvals)
  * [Managed configuration](https://developers.openai.com/codex/security#managed-configuration)



아래 스니펫을 참조로 사용하세요. 필요한 키와 섹션만 `~/.codex/config.toml`(또는 프로젝트 범위의 `.codex/config.toml`)에 복사한 뒤, 환경에 맞게 값을 조정하면 됩니다.
```
    # Codex example configuration (config.toml)
    #
    # This file lists all keys Codex reads from config.toml, their default values,
    # and concise explanations. Values here mirror the effective defaults compiled
    # into the CLI. Adjust as needed.
    #
    # Notes
    # - Root keys must appear before tables in TOML.
    # - Optional keys that default to "unset" are shown commented out with notes.
    # - MCP servers, profiles, and model providers are examples; remove or edit.
    
    ################################################################################
    # Core Model Selection
    ################################################################################
    
    # Primary model used by Codex. Default: "gpt-5.2-codex" on all platforms.
    model = "gpt-5.2-codex"
    
    # Default communication style for supported models. Default: "friendly".
    # Allowed values: none | friendly | pragmatic
    # personality = "friendly"
    
    # Optional model override for /review. Default: unset (uses current session model).
    # review_model = "gpt-5.2-codex"
    
    # Provider id selected from [model_providers]. Default: "openai".
    model_provider = "openai"
    
    # Default OSS provider for --oss sessions. When unset, Codex prompts. Default: unset.
    # oss_provider = "ollama"
    
    # Optional manual model metadata. When unset, Codex auto-detects from model.
    # Uncomment to force values.
    # model_context_window = 128000       # tokens; default: auto for model
    # model_auto_compact_token_limit = 0  # tokens; unset uses model defaults
    # tool_output_token_limit = 10000     # tokens stored per tool output; default: 10000 for gpt-5.2-codex
    # log_dir = "/absolute/path/to/codex-logs" # directory for Codex logs; default: "$CODEX_HOME/log"
    
    ################################################################################
    # Reasoning & Verbosity (Responses API capable models)
    ################################################################################
    
    # Reasoning effort: minimal | low | medium | high | xhigh (default: medium; xhigh on gpt-5.2-codex and gpt-5.2)
    model_reasoning_effort = "medium"
    
    # Reasoning summary: auto | concise | detailed | none (default: auto)
    # model_reasoning_summary = "auto"
    
    # Text verbosity for GPT-5 family (Responses API): low | medium | high (default: medium)
    # model_verbosity = "medium"
    
    # Force enable or disable reasoning summaries for current model
    # model_supports_reasoning_summaries = true
    
    ################################################################################
    # Instruction Overrides
    ################################################################################
    
    # Additional user instructions are injected before AGENTS.md. Default: unset.
    # developer_instructions = ""
    
    # (Ignored) Optional legacy base instructions override (prefer AGENTS.md). Default: unset.
    # instructions = ""
    
    # Inline override for the history compaction prompt. Default: unset.

# compact_prompt = ""
    
    # 내장 기본 지침을 파일 경로로 재정의합니다. 기본값: unset.
    # model_instructions_file = "/absolute/or/relative/path/to/instructions.txt"
    
    # 마이그레이션 참고: experimental_instructions_file이 model_instructions_file로 이름이 변경되었으며(사용 중단됨).
    
    # 파일에서 compact prompt 재정의 값을 불러옵니다. 기본값: unset.
    # experimental_compact_prompt_file = "/absolute/or/relative/path/to/compact_prompt.txt"
    
    # apply_patch_freeform의 이전 이름입니다. 기본값: false
include_apply_patch_tool = false
    
    
    ################################################################################
    # 알림
    ################################################################################
    
    # 외부 알림 프로그램(argv 배열)입니다. 설정되지 않으면 비활성화됩니다.
    # 예시: notify = ["notify-send", "Codex"]
notify = [ ]
    
    
    ################################################################################
    # 승인 및 샌드박스
    ################################################################################
    
    # 명령 승인 요청 시점:
    # - untrusted: 알려진 안전한 읽기 전용 명령만 자동 실행되고, 나머지는 확인을 요청합니다.
    # - on-request: 모델이 요청 시점을 결정합니다(기본값).
    # - never: 확인을 요청하지 않습니다(위험).
approval_policy = "on-request"
    
    # 도구 호출에 대한 파일 시스템/네트워크 샌드박스 정책:
    # - read-only (기본)
    # - workspace-write
    # - danger-full-access (샌드박스 없음; 매우 위험)
sandbox_mode = "read-only"
    
    ################################################################################
    # 인증 및 로그인
    ################################################################################
    
    # CLI 로그인 자격 증명을 저장할 위치: file(기본값) | keyring | auto
cli_auth_credentials_store = "file"
    
    # ChatGPT 인증 흐름(OpenAI API 아님)의 기본 URL입니다. 기본값:
chatgpt_base_url = "https://chatgpt.com/backend-api/"
    
    # ChatGPT 로그인을 특정 워크스페이스 ID로 제한합니다. 기본값: unset.
    # forced_chatgpt_workspace_id = ""
    
    # Codex가 일반적으로 자동 선택하는 로그인 메커니즘을 강제로 지정합니다. 기본값: unset.
    # 허용 값: chatgpt | api
    # forced_login_method = "chatgpt"
    
    # MCP OAuth 자격 증명의 기본 저장소: auto(기본값) | file | keyring
mcp_oauth_credentials_store = "auto"
    
    # MCP OAuth 콜백용 고정 포트(선택 사항): 1-65535. 기본값: unset.
    # mcp_oauth_callback_port = 4321
    
    ################################################################################
    # 프로젝트 문서 제어
    ################################################################################
    
    # 첫 번째 턴 지침에 포함할 AGENTS.md의 최대 바이트 수입니다. 기본값: 32768
project_doc_max_bytes = 32768
    
    # 디렉터리 수준에서 AGENTS.md가 없을 때 사용할 순차적 폴백 목록입니다. 기본값: []
project_doc_fallback_filenames = []
    
    # 상위 디렉터리를 검색할 때 사용하는 프로젝트 루트 마커 파일 이름입니다. 기본값: [".git"]
    # project_root_markers = [".git"]
    
    ################################################################################
    # 히스토리 및 파일 열기
    ################################################################################
    
    # 클릭 가능한 인용에 사용할 URI 스킴: vscode(기본값) | vscode-insiders | windsurf | cursor | none
file_opener = "vscode"
    
    ################################################################################
    # UI, 알림 및 기타
    ################################################################################
    
    # 출력에서 내부 추론 이벤트를 숨깁니다. 기본값: false
hide_agent_reasoning = false
    
    # 가능하면 원시 추론 내용을 표시합니다. 기본값: false
show_raw_agent_reasoning = false
    
    # TUI에서 burst-paste 감지를 비활성화합니다. 기본값: false
disable_paste_burst = false

# Windows 온보딩 확인 상태 추적(Windows 전용). 기본값: false
    windows_wsl_setup_acknowledged = false
    
    # Check for updates on startup. Default: true
    check_for_update_on_startup = true
    
    ################################################################################
    # Web Search
    ################################################################################
    
    # Web search mode: disabled | cached | live. Default: "cached"
    # cached serves results from a web search cache (an OpenAI-maintained index).
    # cached returns pre-indexed results; live fetches the most recent data.
    # If you use --yolo or another full access sandbox setting, web search defaults to live.
    web_search = "cached"
    
    ################################################################################
    # Profiles (named presets)
    ################################################################################
    
    # Active profile name. When unset, no profile is applied.
    # profile = "default"
    
    ################################################################################
    # Skills (per-skill overrides)
    ################################################################################
    
    # Disable or re-enable a specific skill without deleting it.
    [[skills.config]]
    # path = "/path/to/skill"
    # enabled = false
    
    ################################################################################
    # Experimental toggles (legacy; prefer [features])
    ################################################################################
    
    experimental_use_unified_exec_tool = false
    
    # Include apply_patch via freeform editing path (affects default tool set). Default: false
    experimental_use_freeform_apply_patch = false
    
    ################################################################################
    # Sandbox settings (tables)
    ################################################################################
    
    # Extra settings used only when sandbox_mode = "workspace-write".
    [sandbox_workspace_write]
    # Additional writable roots beyond the workspace (cwd). Default: []
    writable_roots = []
    # Allow outbound network access inside the sandbox. Default: false
    network_access = false
    # Exclude $TMPDIR from writable roots. Default: false
    exclude_tmpdir_env_var = false
    # Exclude /tmp from writable roots. Default: false
    exclude_slash_tmp = false
    
    ################################################################################
    # Shell Environment Policy for spawned processes (table)
    ################################################################################
    
    [shell_environment_policy]
    # inherit: all (default) | core | none
    inherit = "all"
    # Skip default excludes for names containing KEY/SECRET/TOKEN (case-insensitive). Default: true
    ignore_default_excludes = true
    # Case-insensitive glob patterns to remove (e.g., "AWS_*", "AZURE_*"). Default: []
    exclude = []
    # Explicit key/value overrides (always win). Default: {}
    set = {}
    # Whitelist; if non-empty, keep only matching vars. Default: []
    include_only = []
    # Experimental: run via user shell profile. Default: false
    experimental_use_profile = false
    
    ################################################################################
    # History (table)
    ################################################################################
    
    [history]
    # save-all (default) | none
    persistence = "save-all"
    # Maximum bytes for history file; oldest entries are trimmed when exceeded. Example: 5242880
    # max_bytes = 0
    
    ################################################################################
    # UI, Notifications, and Misc (tables)
    ################################################################################
    
    [tui]

# TUI 데스크톱 알림: 불리언 또는 필터 목록. 기본값: true
    # Examples: false | ["agent-turn-complete", "approval-requested"]
    notifications = false
    
    # Notification mechanism for terminal alerts: auto | osc9 | bel. Default: "auto"
    # notification_method = "auto"
    
    # Enables welcome/status/spinner animations. Default: true
    animations = true
    
    # Show onboarding tooltips in the welcome screen. Default: true
    show_tooltips = true
    
    # Control alternate screen usage (auto skips it in Zellij to preserve scrollback).
    # alternate_screen = "auto"
    
    # Ordered list of footer status-line item IDs. Default: null (disabled).
    # status_line = ["model", "context-remaining", "git-branch"]
    
    # Control whether users can submit feedback from `/feedback`. Default: true
    [feedback]
    enabled = true
    
    # In-product notices (mostly set automatically by Codex).
    [notice]
    # hide_full_access_warning = true
    # hide_world_writable_warning = true
    # hide_rate_limit_model_nudge = true
    # hide_gpt5_1_migration_prompt = true
    # "hide_gpt-5.1-codex-max_migration_prompt" = true
    # model_migrations = { "gpt-4.1" = "gpt-5.1" }
    
    # Suppress the warning shown when under-development feature flags are enabled.
    # suppress_unstable_features_warning = true
    
    ################################################################################
    # Centralized Feature Flags (preferred)
    ################################################################################
    
    [features]
    # Leave this table empty to accept defaults. Set explicit booleans to opt in/out.
    shell_tool = true
    # apps = false
    # apps_mcp_gateway = false
    # Deprecated legacy toggles; prefer the top-level `web_search` setting.
    # web_search = false
    # web_search_cached = false
    # web_search_request = false
    unified_exec = false
    shell_snapshot = false
    apply_patch_freeform = false
    # search_tool = false
    # personality = true
    request_rule = true
    collaboration_modes = true
    use_linux_sandbox_bwrap = false
    experimental_windows_sandbox = false
    elevated_windows_sandbox = false
    remote_models = false
    runtime_metrics = false
    powershell_utf8 = true
    child_agents_md = false
    
    ################################################################################
    # Define MCP servers under this table. Leave empty to disable.
    ################################################################################
    
    [mcp_servers]
    
    # --- Example: STDIO transport ---
    # [mcp_servers.docs]
    # enabled = true                       # optional; default true
    # required = true                      # optional; fail startup/resume if this server cannot initialize
    # command = "docs-server"                 # required
    # args = ["--port", "4000"]               # optional
    # env = { "API_KEY" = "value" }           # optional key/value pairs copied as-is
    # env_vars = ["ANOTHER_SECRET"]            # optional: forward these from the parent env
    # cwd = "/path/to/server"                 # optional working directory override
    # startup_timeout_sec = 10.0               # optional; default 10.0 seconds
    # # startup_timeout_ms = 10000              # optional alias for startup timeout (milliseconds)
    # tool_timeout_sec = 60.0                  # optional; default 60.0 seconds
    # enabled_tools = ["search", "summarize"]  # optional allow-list
    # disabled_tools = ["slow-tool"]           # optional deny-list (applied after allow-list)
    
    # --- Example: Streamable HTTP transport ---
    # [mcp_servers.github]
    # enabled = true                          # optional; default true
    # required = true                         # optional; fail startup/resume if this server cannot initialize
    # url = "https://github-mcp.example.com/mcp"  # required

# bearer_token_env_var = "GITHUB_TOKEN"        # 선택 사항; Authorization: Bearer <token>
    # http_headers = { "X-Example" = "value" }    # 선택적 정적 헤더
    # env_http_headers = { "X-Auth" = "AUTH_ENV" } # 환경 변수에서 채워지는 선택적 헤더
    # startup_timeout_sec = 10.0                   # 선택 사항
    # tool_timeout_sec = 60.0                      # 선택 사항
    # enabled_tools = ["list_issues"]             # 선택 사항 허용 목록
    
    ################################################################################
    # 모델 제공자
    ################################################################################
    
    # 기본 제공:
    # - openai (Responses API; 로그인 또는 인증 흐름을 통한 OPENAI_API_KEY 필요)
    # - oss (Chat Completions API; 기본값은 http://localhost:11434/v1)
    
    [model_providers]
    
    # --- 예시: 명시적 base URL 또는 헤더를 사용하는 OpenAI 데이터 레지던시 ---
    # [model_providers.openaidr]
    # name = "OpenAI Data Residency"
    # base_url = "https://us.api.openai.com/v1"        # 'us' 도메인 접두사를 사용하는 예
    # wire_api = "responses"                           # "responses" | "chat" (기본값은 상황별)
    # # requires_openai_auth = true                    # 기본 OpenAI 설정은 true
    # # request_max_retries = 4                        # 기본 4; 최대 100
    # # stream_max_retries = 5                         # 기본 5;  최대 100
    # # stream_idle_timeout_ms = 300000                # 기본 300_000 (5분)
    # # experimental_bearer_token = "sk-example"       # 선택적 개발 전용 직접 베어러 토큰
    # # http_headers = { "X-Example" = "value" }
    # # env_http_headers = { "OpenAI-Organization" = "OPENAI_ORGANIZATION", "OpenAI-Project" = "OPENAI_PROJECT" }
    
    # --- 예시: Azure (엔드포인트에 따라 Chat/Responses) ---
    # [model_providers.azure]
    # name = "Azure"
    # base_url = "https://YOUR_PROJECT_NAME.openai.azure.com/openai"
    # wire_api = "responses"                          # 또는 엔드포인트에 따라 "chat"
    # query_params = { api-version = "2025-04-01-preview" }
    # env_key = "AZURE_OPENAI_API_KEY"
    # # env_key_instructions = "환경에 AZURE_OPENAI_API_KEY를 설정하세요"
    
    # --- 예시: 로컬 OSS (예: Ollama 호환) ---
    # [model_providers.ollama]
    # name = "Ollama"
    # base_url = "http://localhost:11434/v1"
    # wire_api = "chat"
    
    ################################################################################
    # 프로필(이름이 있는 프리셋)
    ################################################################################
    
    [profiles]
    
    # [profiles.default]
    # model = "gpt-5.2-codex"
    # model_provider = "openai"
    # approval_policy = "on-request"
    # sandbox_mode = "read-only"
    # oss_provider = "ollama"
    # model_reasoning_effort = "medium"
    # model_reasoning_summary = "auto"
    # model_verbosity = "medium"
    # personality = "friendly" # 혹은 "pragmatic" 또는 "none"
    # chatgpt_base_url = "https://chatgpt.com/backend-api/"
    # experimental_compact_prompt_file = "./compact_prompt.txt"
    # include_apply_patch_tool = false
    # experimental_use_unified_exec_tool = false
    # experimental_use_freeform_apply_patch = false
    # tools.web_search = false             # 더 이상 사용되지 않는 레거시 별칭; 최상위 `web_search` 사용 권장
    # features = { unified_exec = false }
    
    ################################################################################
    # 앱 / 커넥터
    ################################################################################
    
    # 앱별 선택적 제어.
    [apps]
    # [apps.google_drive]
    # enabled = false
    # disabled_reason = "user" # 또는 "unknown"
    
    ################################################################################
    # 프로젝트(신뢰 수준)
    ################################################################################

# 특정 워크트리를 신뢰 또는 비신뢰 대상으로 표시하기.
    [projects]
    # [projects."/absolute/path/to/project"]
    # trust_level = "trusted"  # or "untrusted"
    
    ################################################################################
    # OpenTelemetry (OTEL) - disabled by default
    ################################################################################
    
    [otel]
    # Include user prompt text in logs. Default: false
    log_user_prompt = false
    # Environment label applied to telemetry. Default: "dev"
    environment = "dev"
    # Exporter: none (default) | otlp-http | otlp-grpc
    exporter = "none"
    # Trace exporter: none (default) | otlp-http | otlp-grpc
    trace_exporter = "none"
    
    # Example OTLP/HTTP exporter configuration
    # [otel.exporter."otlp-http"]
    # endpoint = "https://otel.example.com/v1/logs"
    # protocol = "binary"                         # "binary" | "json"
    
    # [otel.exporter."otlp-http".headers]
    # "x-otlp-api-key" = "${OTLP_TOKEN}"
    
    # Example OTLP/gRPC exporter configuration
    # [otel.exporter."otlp-grpc"]
    # endpoint = "https://otel.example.com:4317",
    # headers = { "x-otlp-meta" = "abc123" }
    
    # Example OTLP exporter with mutual TLS
    # [otel.exporter."otlp-http"]
    # endpoint = "https://otel.example.com/v1/logs"
    # protocol = "binary"
    
    # [otel.exporter."otlp-http".headers]
    # "x-otlp-api-key" = "${OTLP_TOKEN}"
    
    # [otel.exporter."otlp-http".tls]
    # ca-certificate = "certs/otel-ca.pem"
    # client-certificate = "/etc/codex/certs/client.pem"
    # client-private-key = "/etc/codex/certs/client-key.pem"
```