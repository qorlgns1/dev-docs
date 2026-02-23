---
title: '설정 기본'
description: "description: 'Codex는 여러 위치에서 구성 세부 정보를 읽습니다. 개인 기본 설정은 , 프로젝트 재정의는  파일로 추가할 수 있습니다. 보안상 Codex는인 프로젝트의 구성 파일만 로드합니다...'"
---

**번역된 기술 문서**

---
title: '설정 기본'
description: 'Codex는 여러 위치에서 구성 세부 정보를 읽습니다. 개인 기본 설정은 , 프로젝트 재정의는  파일로 추가할 수 있습니다. 보안상 Codex는인 프로젝트의 구성 파일만 로드합니다...'
---

Source URL: https://developers.openai.com/codex/config-basic

# 설정 기본

Codex는 여러 위치에서 구성 세부 정보를 읽습니다. 개인 기본 설정은 `~/.codex/config.toml`에 있고, 저장소에 `.codex/config.toml` 파일을 추가하여 프로젝트 재정의를 할 수 있습니다. 보안상 Codex는 신뢰한 프로젝트에서만 프로젝트 구성 파일을 로드합니다.

## Codex 구성 파일

Codex는 사용자 수준 구성을 `~/.codex/config.toml`에 저장합니다. 특정 프로젝트나 하위 폴더에 설정을 한정하려면 저장소에 `.codex/config.toml` 파일을 추가하세요.

Codex IDE 확장에서 구성 파일을 열려면 우측 상단의 톱니바퀴 아이콘을 선택한 다음 **Codex Settings > Open config.toml**을 선택합니다.

CLI와 IDE 확장은 동일한 구성 계층을 공유합니다. 다음을 실행할 수 있습니다:

- 기본 모델과 공급자를 설정.
- [승인 정책 및 샌드박스 설정](https://developers.openai.com/codex/security#sandbox-and-approvals) 구성.
- [MCP 서버](https://developers.openai.com/codex/mcp) 구성.

## 구성 우선 순위

Codex는 다음 순서로 값을 해석합니다 (우선 순위가 높은 항목 먼저):

1. CLI 플래그 및 `--config` 재정의
2. [프로필](https://developers.openai.com/codex/config-advanced#profiles) 값 (`--profile <name>`에서)
3. 프로젝트 구성 파일: `.codex/config.toml`, 프로젝트 루트에서 현재 작업 디렉터리까지 순서대로 (가장 가까운 것이 우선; 신뢰된 프로젝트만)
4. 사용자 구성: `~/.codex/config.toml`
5. 시스템 구성 (존재하는 경우): Unix에서는 `/etc/codex/config.toml`
6. 기본 내장값

해당 우선순위를 사용하여 최상위에서 공유 기본값을 설정하고, 프로필은 달라지는 값에 집중하세요.

프로젝트를 신뢰하지 않도록 설정하면 Codex는 `.codex/config.toml`을 포함한 프로젝트 범위 `.codex/` 계층을 건너뛰고 사용자, 시스템, 내장 기본값으로 돌아갑니다.

`-c`/`--config`를 통한 일회성 재정의(예: TOML 인용 규칙 포함)는 [고급 구성](https://developers.openai.com/codex/config-advanced#one-off-overrides-from-the-cli)을 참고하세요.

관리되는 머신에서는 조직이 `requirements.toml`을 통해 제약을 강제할 수도 있습니다(예: `approval_policy = "never"` 또는 `sandbox_mode = "danger-full-access"` 금지). [관리 구성](https://developers.openai.com/codex/security#managed-configuration) 및 [관리자 강제 요구사항](https://developers.openai.com/codex/security#admin-enforced-requirements-requirementstoml)을 참조하세요.

## 일반 구성 옵션

여기 사람들이 가장 자주 변경하는 몇 가지 옵션이 있습니다:

#### 기본 모델

CLI와 IDE에서 Codex가 기본으로 사용할 모델을 선택하세요.

```toml
model = "gpt-5.2"
```

#### 승인 프롬프트

생성된 명령을 실행하기 전에 Codex가 멈추고 묻는 시점을 제어합니다.

```toml
approval_policy = "on-request"
```

`untrusted`, `on-request`, `never` 간의 동작 차이는 [승인 프롬프트 없이 실행하기](https://developers.openai.com/codex/security#run-without-approval-prompts) 및 [일반적인 샌드박스와 승인 조합](https://developers.openai.com/codex/security#common-sandbox-and-approval-combinations)을 확인하세요.

#### 샌드박스 수준

명령을 실행할 때 Codex가 사용할 수 있는 파일 시스템 및 네트워크 접근 범위를 조절합니다.

```toml
sandbox_mode = "workspace-write"
```

모드별 동작(보호된 `.git`/`.codex` 경로 및 네트워크 기본값 포함)은 [샌드박스 및 승인](https://developers.openai.com/codex/security#sandbox-and-approvals), [쓰기 가능한 루트의 보호된 경로](https://developers.openai.com/codex/security#protected-paths-in-writable-roots), [네트워크 액세스](https://developers.openai.com/codex/security#network-access)를 참조하세요.

#### 웹 검색 모드

Codex는 로컬 작업에 대해 기본적으로 웹 검색을 활성화하며 웹 검색 캐시에서 결과를 제공합니다. 캐시는 OpenAI가 관리하는 웹 결과 인덱스로, 캐시 모드는 실시간 페이지를 가져오지 않고 미리 인덱싱된 결과를 반환합니다. 이는 임의 실시간 콘텐츠의 프롬프트 인젝션 노출을 줄이지만 웹 결과는 여전히 신뢰되지 않은 것으로 취급해야 합니다. `--yolo` 또는 다른 [전체 액세스 샌드박스 설정](https://developers.openai.com/codex/security#common-sandbox-and-approval-combinations)을 사용하는 경우 웹 검색은 실시간 결과를 기본으로 합니다. `web_search` 설정으로 모드를 선택하세요:

- `"cached"` (기본): 웹 검색 캐시에서 결과 제공.
- `"live"`: 웹에서 최신 데이터를 가져옴 (`--search`와 동일).
- `"disabled"`: 웹 검색 도구 비활성화.

```toml
web_search = "cached"  # 기본; 웹 검색 캐시에서 결과 제공
# web_search = "live"  # 웹에서 최신 데이터 가져옴 (--search와 동일)
# web_search = "disabled"
```

#### 추론 노력

지원되는 경우 모델이 얼마만큼의 추론 노력을 들일지 조정합니다.

```toml
model_reasoning_effort = "high"
```

#### 커뮤니케이션 스타일

지원되는 모델에 대한 기본 커뮤니케이션 스타일을 설정합니다.

```toml
personality = "friendly" # 또는 "pragmatic" 또는 "none"
```

활성 세션에서 `/personality`로 나중에 재정의하거나 앱 서버 API 사용 시 스레드/턴별로 설정할 수 있습니다.

#### 명령 환경

Codex가 실행한 명령에 전달할 환경 변수를 제어합니다.

```toml
[shell_environment_policy]
include_only = ["PATH", "HOME"]
```

#### 로그 디렉터리

`codex-tui.log` 같은 로컬 로그 파일을 Codex가 어디에 쓰는지 재정의합니다.

```toml
log_dir = "/absolute/path/to/codex-logs"
```

일회성 실행 시 CLI에서 다음과 같이 설정할 수도 있습니다:

```bash
codex -c log_dir=./.codex-log
```

## 기능 플래그

`config.toml`의 `[features]` 테이블을 사용하여 선택적/실험적 기능을 전환하세요.

```toml
[features]
shell_snapshot = true           # 반복 명령 속도 향상
```

### 지원되는 기능

| 키                            | 기본값 | 성숙도       | 설명                                                                                               |
| ------------------------------ | :----: | ------------ | -------------------------------------------------------------------------------------------------- |
| `apply_patch_freeform`         | false  | Experimental | 자유 형식 `apply_patch` 도구 포함                                                                  |
| `apps`                         | false  | Experimental | ChatGPT Apps/커넥터 지원 활성화                                                                    |
| `apps_mcp_gateway`             | false  | Experimental | Apps MCP 호출을 기존 라우팅 대신 `https://api.openai.com/v1/connectors/mcp/`로 라우팅 |
| `elevated_windows_sandbox`     | false  | Experimental | 고권한 Windows 샌드박스 파이프라인 사용                                                             |
| `collaboration_modes`          | true   | Stable       | 계획 모드 같은 협업 모드 활성화                                                                      |
| `experimental_windows_sandbox` | false  | Experimental | Windows 제한 토큰 샌드박스 사용                                                                    |
| `multi_agent`                  | false  | Experimental | 다중 에이전트 협업 도구 활성화                                                                     |
| `personality`                  | true   | Stable       | 성격 선택 제어 활성화                                                                               |
| `remote_models`                | false  | Experimental | 준비 상태 표시 전에 원격 모델 목록 새로 고침                                                        |
| `runtime_metrics`              | false  | Experimental | TUI 턴 구분자에 실행 시간 메트릭 요약 표시                                                          |
| `request_rule`                 | true   | Stable       | 스마트 승인(`prefix_rule` 제안) 활성화                                                              |
| `search_tool`                  | false  | Experimental | `search_tool_bm25` 활성화하여 툴 호출 전에 Apps MCP 도구 검색                                      |
| `shell_snapshot`               | false  | Beta         | 반복 명령 속도 향상을 위해 셸 환경 스냅샷                                                          |
| `shell_tool`                   | true   | Stable       | 기본 `shell` 도구 사용                                                                               |
| `use_linux_sandbox_bwrap`      | false  | Experimental | bubblewrap 기반 Linux 샌드박스 파이프라인 사용                                                      |
| `unified_exec`                 | false  | Beta         | 단일화된 PTY 기반 실행 도구 사용                                                                    |
| `undo`                         | true   | Stable       | 턴별 git 고스트 스냅샷을 통한 실행 취소 활성화                                                      |
| `web_search`                   | true   | Deprecated   | 레거시 토글; 상위 수준 `web_search` 설정 사용 권장                                                  |
| `web_search_cached`            | true   | Deprecated   | 기본 값이 설정되지 않으면 `web_search = "cached"`로 매핑되는 레거시 토글                            |
| `web_search_request`           | true   | Deprecated   | 기본 값이 설정되지 않으면 `web_search = "live"`로 매핑되는 레거시 토글                              |

성숙도 열은 Experimental, Beta, Stable 같은 기능 성숙도 레이블을 사용합니다. 이러한 레이블 해석 방법은 [기능 성숙도](https://developers.openai.com/codex/feature-maturity)를 참조하세요.

기본값을 유지하려면 기능 키를 생략하세요.

### 기능 활성화

- `config.toml`에서 `[features]` 하위에 `feature_name = true`를 추가.
- CLI에서 `codex --enable feature_name` 실행.
- 여러 기능을 활성화하려면 `codex --enable feature_a --enable feature_b` 실행.
- 기능을 비활성화하려면 `config.toml`에서 키를 `false`로 설정.

