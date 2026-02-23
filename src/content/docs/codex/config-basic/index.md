---
title: 구성 기본 사항
description: Codex는 구성 세부 정보를 여러 위치에서 읽습니다. 개인 기본값은 에 있으며,  파일로 프로젝트별 재정의를 추가할 수 있습니다. 보안을 위해 신뢰한 프로젝트에서만 Codex가 프로젝트 구성 파일을 불러옵니다.
---

# 구성 기본 사항

Source URL: https://developers.openai.com/codex/config-basic

Codex는 구성 세부 정보를 여러 위치에서 읽습니다. 개인 기본값은 `~/.codex/config.toml`에 있으며, `.codex/config.toml` 파일로 프로젝트별 재정의를 추가할 수 있습니다. 보안을 위해 신뢰한 프로젝트에서만 Codex가 프로젝트 구성 파일을 불러옵니다.

## Codex 구성 파일

Codex는 사용자 수준 구성을 `~/.codex/config.toml`에 저장합니다. 특정 프로젝트나 하위 폴더에만 설정을 적용하려면 저장소에 `.codex/config.toml` 파일을 추가하십시오.

Codex IDE 확장 프로그램에서 구성 파일을 열려면 오른쪽 상단의 기어 아이콘을 선택한 후 **Codex Settings > Open config.toml**을 선택합니다.

CLI와 IDE 확장 프로그램은 동일한 구성 계층을 공유합니다. 이를 사용하여 다음을 수행할 수 있습니다:

  * 기본 모델과 공급자를 설정합니다.
  * [승인 정책 및 샌드박스 설정](https://developers.openai.com/codex/security#sandbox-and-approvals)을 구성합니다.
  * [MCP 서버](https://developers.openai.com/codex/mcp)를 구성합니다.



## 구성 우선순위

Codex는 값을 다음 순서로 해결합니다(우선순위가 높은 순):

  1. CLI 플래그와 `--config` 재정의
  2. [프로필](https://developers.openai.com/codex/config-advanced#profiles) 값(`--profile <name>`에서 가져옴)
  3. 프로젝트 구성 파일: 프로젝트 루트에서 현재 작업 디렉터리까지의 `.codex/config.toml`(가장 가까운 것이 우선, 신뢰한 프로젝트만)
  4. 사용자 구성: `~/.codex/config.toml`
  5. 시스템 구성(있는 경우): Unix의 `/etc/codex/config.toml`
  6. 기본 내장값



이 우선순위를 활용해 상위 수준에서 공유 기본값을 설정하고, 프로필은 서로 다른 값에 집중하도록 유지하십시오.

프로젝트를 신뢰하지 않는 것으로 표시하면, Codex는 프로젝트 범위의 `.codex/` 계층(예: `.codex/config.toml`)을 건너뛰고 사용자, 시스템, 기본 내장값으로 돌아갑니다.

`-c`/`--config`를 통한 1회성 재정의(TOML 인용 규칙 포함)는 [Advanced Config](https://developers.openai.com/codex/config-advanced#one-off-overrides-from-the-cli)를 참고하십시오.

관리형 머신에서는 조직이 `requirements.toml`을 통해 추가 제약을 강제할 수 있습니다(예: `approval_policy = "never"`나 `sandbox_mode = "danger-full-access"`를 허용하지 않음). [Managed configuration](https://developers.openai.com/codex/security#managed-configuration)과 [Admin-enforced requirements](https://developers.openai.com/codex/security#admin-enforced-requirements-requirementstoml)를 참조하십시오.

## 일반적인 구성 옵션

많은 사용자가 자주 변경하는 옵션은 다음과 같습니다:

#### 기본 모델

CLI와 IDE에서 Codex가 기본으로 사용할 모델을 선택합니다.
[code] 
    model = "gpt-5.2"
[/code]

#### 승인 프롬프트

Codex가 생성된 명령을 실행하기 전에 멈추고 물어볼 시점을 제어합니다.
[code] 
    approval_policy = "on-request"
[/code]

`untrusted`, `on-request`, `never` 간 동작 차이는 [Run without approval prompts](https://developers.openai.com/codex/security#run-without-approval-prompts)와 [Common sandbox and approval combinations](https://developers.openai.com/codex/security#common-sandbox-and-approval-combinations)을 참조하십시오.

#### 샌드박스 수준

명령을 실행할 때 Codex가 갖는 파일 시스템 및 네트워크 접근 범위를 조정합니다.
[code] 
    sandbox_mode = "workspace-write"
[/code]

모드별 동작(`.git`/`.codex` 보호 경로 및 네트워크 기본값 포함)은 [Sandbox and approvals](https://developers.openai.com/codex/security#sandbox-and-approvals), [Protected paths in writable roots](https://developers.openai.com/codex/security#protected-paths-in-writable-roots), [Network access](https://developers.openai.com/codex/security#network-access)를 참고하십시오.

#### 웹 검색 모드

Codex는 로컬 작업에 대해 기본적으로 웹 검색을 활성화하고 웹 검색 캐시에서 결과를 제공합니다. 이 캐시는 OpenAI가 관리하는 웹 결과 인덱스이므로, 캐시 모드에서는 실시간 페이지를 가져오는 대신 사전 색인된 결과를 반환합니다. 이 방식은 임의의 실시간 콘텐츠로부터의 프롬프트 주입 노출을 줄이지만, 여전히 웹 결과를 신뢰할 수 없는 정보로 취급해야 합니다. `--yolo`나 다른 [full access sandbox setting](https://developers.openai.com/codex/security#common-sandbox-and-approval-combinations)을 사용하는 경우에는 웹 검색이 실시간 결과를 기본값으로 사용합니다. `web_search`로 모드를 선택하세요:

  * `"cached"`(기본값)은 웹 검색 캐시에서 결과를 제공합니다.
  * `"live"`는 웹에서 최신 데이터를 가져옵니다(`--search`와 동일).
  * `"disabled"`는 웹 검색 도구를 끕니다.

[code] 
    web_search = "cached"  # default; serves results from the web search cache
    # web_search = "live"  # fetch the most recent data from the web (same as --search)
    # web_search = "disabled"
[/code]

#### Reasoning effort

지원되는 경우, 모델이 투입하는 추론 노력을 조정합니다.
[code] 
    model_reasoning_effort = "high"
[/code]

#### Communication style

지원되는 모델의 기본 소통 스타일을 설정합니다.
[code] 
    personality = "friendly" # or "pragmatic" or "none"
[/code]

나중에 `/personality`로 활성 세션에서 덮어쓰거나, 앱 서버 API를 사용할 때 스레드/턴 단위로 개별 설정할 수 있습니다.

#### Command environment

Codex가 생성한 명령에 전달할 환경 변수를 제어합니다.
[code] 
    [shell_environment_policy]
    include_only = ["PATH", "HOME"]
[/code]

#### Log directory

`codex-tui.log` 같은 로컬 로그 파일을 Codex가 저장할 경로를 재정의합니다.
[code] 
    log_dir = "/absolute/path/to/codex-logs"
[/code]

단발 실행에서는 CLI에서 바로 설정할 수도 있습니다:
[code] 
    codex -c log_dir=./.codex-log
[/code]

## Feature flags

선택적·실험적 기능을 토글하려면 `config.toml`의 `[features]` 테이블을 사용하세요.
[code] 
    [features]
    shell_snapshot = true           # Speed up repeated commands
[/code]

### Supported features

Key| Default| Maturity| Description  
---|---|---|---  
`apply_patch_freeform`| false| Experimental| Include the freeform `apply_patch` tool  
`apps`| false| Experimental| Enable ChatGPT Apps/connectors support  
`apps_mcp_gateway`| false| Experimental| Route Apps MCP calls through `https://api.openai.com/v1/connectors/mcp/` instead of legacy routing  
`elevated_windows_sandbox`| false| Experimental| Use the elevated Windows sandbox pipeline  
`collaboration_modes`| true| Stable| Enable collaboration modes such as plan mode  
`experimental_windows_sandbox`| false| Experimental| Use the Windows restricted-token sandbox  
`multi_agent`| false| Experimental| Enable multi-agent collaboration tools  
`personality`| true| Stable| Enable personality selection controls  
`remote_models`| false| Experimental| Refresh remote model list before showing readiness  
`runtime_metrics`| false| Experimental| Show runtime metrics summaries in TUI turn separators  
`request_rule`| true| Stable| Enable Smart approvals (`prefix_rule` suggestions)  
`search_tool`| false| Experimental| Enable `search_tool_bm25` so Codex discovers Apps MCP tools via search before tool calls  
`shell_snapshot`| false| Beta| Snapshot your shell environment to speed up repeated commands  
`shell_tool`| true| Stable| Enable the default `shell` tool  
`use_linux_sandbox_bwrap`| false| Experimental| Use the bubblewrap-based Linux sandbox pipeline  
`unified_exec`| false| Beta| Use the unified PTY-backed exec tool  
`undo`| true| Stable| Enable undo via per-turn git ghost snapshots  
`web_search`| true| Deprecated| Legacy toggle; prefer the top-level `web_search` setting  
`web_search_cached`| true| Deprecated| Legacy toggle that maps to `web_search = "cached"` when unset  
`web_search_request`| true| Deprecated| Legacy toggle that maps to `web_search = "live"` when unset

성숙도(Maturity) 열에서는 Experimental, Beta, Stable과 같은 기능 성숙도 레이블을 사용합니다. 이러한 레이블을 해석하는 방법은 [Feature Maturity](https://developers.openai.com/codex/feature-maturity)를 참고하세요.

기능 키를 생략하면 기본값이 유지됩니다.

### 기능 활성화

  * `config.toml`의 `[features]` 아래에 `feature_name = true`를 추가합니다.
  * CLI에서 `codex --enable feature_name`을 실행합니다.
  * 여러 기능을 활성화하려면 `codex --enable feature_a --enable feature_b`를 실행합니다.
  * 기능을 비활성화하려면 `config.toml`에서 해당 키를 `false`로 설정합니다.
