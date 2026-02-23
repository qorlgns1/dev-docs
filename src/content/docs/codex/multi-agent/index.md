---
title: 멀티 에이전트
description: Codex는 특화된 에이전트를 병렬로 생성하고 결과를 하나의 응답으로 통합하여 멀티 에이전트 워크플로를 실행할 수 있습니다. 이는 코드베이스 탐색이나 다단계 기능 계획 구현처럼 병렬성이 높은 복잡한 작업에 특히 유용합니다.
sidebar:
  order: 10
---

# 멀티 에이전트

Source URL: https://developers.openai.com/codex/multi-agent

Codex는 특화된 에이전트를 병렬로 생성하고 결과를 하나의 응답으로 통합하여 멀티 에이전트 워크플로를 실행할 수 있습니다. 이는 코드베이스 탐색이나 다단계 기능 계획 구현처럼 병렬성이 높은 복잡한 작업에 특히 유용합니다.

멀티 에이전트 워크플로에서는 에이전트에 따라 서로 다른 모델 구성과 지침을 가진 고유한 에이전트 세트를 정의할 수도 있습니다.

멀티 에이전트 워크플로의 개념과 트레이드오프(컨텍스트 폴루션/컨텍스트 로트, 모델 선택 가이드 등)에 대해서는 [멀티 에이전트 개념](https://developers.openai.com/codex/concepts/multi-agents)을 참고하세요.

## 멀티 에이전트 활성화

멀티 에이전트 워크플로는 현재 실험 단계이며 명시적으로 활성화해야 합니다.

CLI에서 `/experimental`을 사용해 이 기능을 활성화할 수 있습니다. **Multi-agents** 를 활성화한 뒤 Codex를 다시 시작하세요.

멀티 에이전트 활동은 현재 CLI에서 노출됩니다. 다른 인터페이스(Codex 앱과 IDE 확장)에서도 곧 지원될 예정입니다.

구성 파일(`~/.codex/config.toml`)에 [`multi_agent` 기능 플래그](https://developers.openai.com/codex/config-basic#feature-flags)를 직접 추가할 수도 있습니다:
```
    [features]
    multi_agent = true
```

## 일반적인 워크플로

Codex는 에이전트 간 오케스트레이션을 처리하며, 새 하위 에이전트 생성, 후속 지침 라우팅, 결과 대기, 에이전트 스레드 종료를 모두 담당합니다.

다수의 에이전트가 실행 중일 때 Codex는 요청한 모든 결과가 준비될 때까지 기다렸다가 통합된 응답을 반환합니다.

Codex가 새로운 에이전트를 생성할지 자동으로 결정하거나, 사용자가 명시적으로 요청할 수도 있습니다.

다음 프롬프트를 프로젝트에 시도해 보세요:
```
    I would like to review the following points on the current PR (this branch vs main). Spawn one agent per point, wait for all of them, and summarize the result for each point.
    1. Security issue
    2. Code quality
    3. Bugs
    4. Race
    5. Test flakiness
    6. Maintainability of the code
```

## 하위 에이전트 관리

  * CLI에서 `/agent`를 사용해 활성 에이전트 스레드 간 전환 및 진행 중인 스레드 확인이 가능합니다.
  * 실행 중인 하위 에이전트를 직접 조정하거나 중지하거나, 완료된 에이전트 스레드를 종료하도록 Codex에 요청하세요.



## 승인 및 샌드박스 제어

하위 에이전트는 현재 사용 중인 샌드박스 정책을 상속하지만 비대화형 승인 모드로 실행됩니다. 하위 에이전트가 새 승인이 필요한 작업을 시도하면 해당 작업은 실패하고 오류가 상위 워크플로에 표시됩니다.

또한 [에이전트 역할](https://developers.openai.com/codex/multi-agent#agent-roles)별로 샌드박스 구성을 재정의하여 특정 에이전트를 읽기 전용 모드로 명시할 수 있습니다.

## 에이전트 역할

[구성](https://developers.openai.com/codex/config-basic#configuration-precedence)의 `[agents]` 섹션에서 에이전트 역할을 설정합니다.

에이전트 역할은 로컬 구성(일반적으로 `~/.codex/config.toml`)에 정의하거나 프로젝트 전용 `.codex/config.toml`에서 공유할 수 있습니다.

각 역할은 Codex가 해당 에이전트를 언제 사용해야 하는지 안내하는 `description`을 제공하고, Codex가 해당 역할의 에이전트를 생성할 때 불러올 역할별 구성 파일(`config_file`)을 선택적으로 지정할 수 있습니다.

Codex에는 기본 제공 역할이 포함되어 있습니다:

  * `default`
  * `worker`
  * `explorer`



각 에이전트 역할은 기본 구성을 재정의할 수 있습니다. 에이전트 역할에서 자주 재정의하는 설정은 다음과 같습니다:

  * 특정 모델을 선택하기 위한 `model` 및 `model_reasoning_effort`
  * 에이전트를 `read-only`로 표시하는 `sandbox_mode`
  * 상위 에이전트에 의존하지 않고 추가 지침을 제공하는 `developer_instructions`



### 스키마

Field| Type| Required| Purpose  
---|---|---|---  
`agents.max_threads`| number| No| 동시에 열 수 있는 에이전트 스레드의 최대 개수.

`[agents.<name>]`| table| No| 역할을 선언합니다. 에이전트를 생성할 때 `<name>`은 `agent_type`으로 사용됩니다.  
`agents.<name>.description`| string| No| Codex가 어떤 역할을 사용할지 결정할 때 사람에게 보여 주는 역할 안내입니다.  
`agents.<name>.config_file`| string (path)| No| 해당 역할로 생성된 에이전트에 적용할 TOML 구성 레이어 경로입니다.  
  
**참고:**

  * `[agents.<name>]`에서 알 수 없는 필드는 거부됩니다.
  * 상대 `config_file` 경로는 역할을 정의하는 `config.toml` 파일을 기준으로 해석됩니다.
  * 역할 이름이 `explorer`처럼 기본 제공 역할과 일치하면 사용자 정의 역할이 우선합니다.
  * Codex가 역할 구성 파일을 불러올 수 없으면 파일을 고칠 때까지 에이전트 생성이 실패할 수 있습니다.
  * 에이전트 역할에서 설정하지 않은 구성은 상위 세션에서 상속됩니다.



### 에이전트 역할 예시

아래 예시는 기본 제공 `default`와 `explorer` 역할 정의를 덮어쓰고 새 `reviewer` 역할을 정의합니다.

예시 `~/.codex/config.toml`:
```
    [agents.default]
    description = "General-purpose helper."
    
    [agents.reviewer]
    description = "Find security, correctness, and test risks in code."
    config_file = "agents/reviewer.toml"
    
    [agents.explorer]
    description = "Fast codebase explorer for read-heavy tasks."
    config_file = "agents/custom-explorer.toml"
```

`reviewer` 역할에 대한 예시 구성 파일 (`~/.codex/agents/reviewer.toml`):
```
    model = "gpt-5.3-codex"
    model_reasoning_effort = "high"
    developer_instructions = "Focus on high priority issues, write tests to validate hypothesis before flagging an issue. When finding security issues give concrete steps on how to reproduce the vulnerability."
```

`explorer` 역할에 대한 예시 구성 파일 (`~/.codex/agents/custom-explorer.toml`):
```
    model = "gpt-5.3-codex-spark"
    model_reasoning_effort = "medium"
    sandbox_mode = "read-only"
```