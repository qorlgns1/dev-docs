---
title: 'index'
description: 'I would like to review the following points on the current PR (this branch vs main). Spawn one agent per point, wait for all of them, and summarize th...'
---

**다중 에이전트**

- 다중 에이전트 워크플로는 특화된 에이전트를 병렬로 실행하고 결과를 하나의 응답으로 수집하여 복잡한 작업(예: 코드베이스 탐색 또는 다단계 기능 구현)을 처리합니다.
- 에이전트마다 모델 구성과 지침을 다르게 정해 사용자 정의 세트를 구성할 수 있습니다. 개념/절충점은 [Multi-agents concepts](https://developers.openai.com/codex/concepts/multi-agents) 참조.

**다중 에이전트 활성화**

- 현재 실험적 기능이며 CLI에서 `/experimental`을 실행한 뒤 **Multi-agents**를 활성화하고 Codex를 재시작해야 합니다.
- 현재 CLI에서만 다중 에이전트 활동이 노출되며 Codex 앱·IDE 확장까지 확장될 예정입니다.
- 또는 `~/.codex/config.toml`에 [`multi_agent` 기능 플래그](https://developers.openai.com/codex/config-basic#feature-flags)를 추가할 수 있습니다.

```toml
[features]
multi_agent = true
```

**전형적인 워크플로**

- Codex는 서브 에이전트 생성, 후속 지시 전달, 결과 대기, 에이전트 종료 등 전체 오케스트레이션을 처리합니다.
- 여러 에이전트가 실행 중이면 모든 결과가 준비될 때까지 기다린 후 통합된 응답을 반환합니다.
- Codex가 자동으로 새 에이전트를 생성하거나, 명시적으로 요청할 수도 있습니다.
- 프로젝트에서 아래 프롬프트를 실행하면 확인할 수 있습니다.

```text
I would like to review the following points on the current PR (this branch vs main). Spawn one agent per point, wait for all of them, and summarize the result for each point.
1. Security issue
2. Code quality
3. Bugs
4. Race
5. Test flakiness
6. Maintainability of the code
```

**서브 에이전트 관리**

- CLI에서 `/agent`를 사용하여 활성 스레드 간 전환 및 진행 중인 스레드를 확인합니다.
- Codex에 서브 에이전트를 조종하거나 중단하거나 완료된 스레드를 종료하도록 직접 요청하세요.

**승인 및 샌드박스 제어**

- 서브 에이전트는 현재 샌드박스 정책을 상속하되, 비대화형 승인으로 실행됩니다. 새로운 승인이 필요한 작업을 시도하면 실패하고 상위 워크플로에 오류가 표시됩니다.
- 특정 [에이전트 역할](#agent-roles)에 대해 샌드박스 구성을 재정의하여 읽기 전용 모드로 지정할 수도 있습니다.

**에이전트 역할**

- `[agents]` 섹션에서 구성합니다(자세한 우선순위는 [configuration](https://developers.openai.com/codex/config-basic#configuration-precedence) 참조).
- 로컬 구성(`~/.codex/config.toml`) 또는 `.codex/config.toml`에 정의할 수 있으며, 각 역할은 Codex가 언제 해당 에이전트를 사용할지 안내하는 `description`과, 해당 역할로 에이전트를 생성할 때 로드할 선택적 `config_file`을 제공합니다.

빌트인 역할:

- `default`
- `worker`
- `explorer`

공통적으로 재정의하는 설정:

- `model`, `model_reasoning_effort`: 특정 모델 지정
- `sandbox_mode`: 에이전트를 `read-only`로 표시
- `developer_instructions`: 상위 에이전트 없이도 역할별 추가 지침 부여

**스키마**

| 필드                         | 타입           | 필수 | 용도                                                                 |
| ---------------------------- | -------------- | :--: | -------------------------------------------------------------------- |
| `agents.max_threads`         | number         |  아니오 | 동시에 열 수 있는 에이전트 스레드 최대 수                               |
| `[agents.<name>]`            | table          |  아니오 | 역할 선언. `<name>`이 에이전트 생성 시 사용되는 `agent_type`                                     |
| `agents.<name>.description`  | string         |  아니오 | Codex가 역할 선택 시 사용자에게 보여줄 설명                             |
| `agents.<name>.config_file`   | string (path)  |  아니오 | 해당 역할로 생성된 에이전트에 적용할 TOML 구성 파일 경로              |

- `[agents.<name>]`의 알 수 없는 필드는 거부됩니다.
- 상대 경로 `config_file`은 해당 역할을 정의한 `config.toml`을 기준으로 해석됩니다.
- 빌트인 역할 이름과 일치하면 사용자 정의 역할이 우선됩니다.
- 역할 구성 파일을 불러오지 못하면 에이전트 생성이 실패할 수 있습니다.
- 역할이 설정하지 않은 구성은 상위 세션에서 상속됩니다.

**예시 역할**

다음은 빌트인 `default`/`explorer` 정의를 재정의하고 `reviewer`라는 새 역할을 추가한 예입니다.

`~/.codex/config.toml` 예:

```toml
[agents.default]
description = "General-purpose helper."

[agents.reviewer]
description = "Find security, correctness, and test risks in code."
config_file = "agents/reviewer.toml"

[agents.explorer]
description = "Fast codebase explorer for read-heavy tasks."
config_file = "agents/custom-explorer.toml"
```

`reviewer` 역할 구성(`~/.codex/agents/reviewer.toml`):

```toml
model = "gpt-5.3-codex"
model_reasoning_effort = "high"
developer_instructions = "Focus on high priority issues, write tests to validate hypothesis before flagging an issue. When finding security issues give concrete steps on how to reproduce the vulnerability."
```

`explorer` 역할 구성(`~/.codex/agents/custom-explorer.toml`):

```toml
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
```

