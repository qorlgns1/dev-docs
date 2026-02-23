---
title: Codex CLI 기능
description: Codex는 채팅을 넘어서는 워크플로우를 지원합니다. 각 워크플로우가 어떤 기능을 제공하고 언제 사용해야 하는지 알아보려면 이 가이드를 참고하세요.
sidebar:
  order: 2
---

# Codex CLI 기능

Source URL: https://developers.openai.com/codex/cli/features

Codex는 채팅을 넘어서는 워크플로우를 지원합니다. 각 워크플로우가 어떤 기능을 제공하고 언제 사용해야 하는지 알아보려면 이 가이드를 참고하세요.

## 인터랙티브 모드로 실행하기

Codex는 전체 화면 터미널 UI를 통해 저장소를 읽고, 수정하고, 명령을 실행하면서 함께 반복 작업할 수 있습니다. 실시간으로 Codex의 작업을 검토할 수 있는 대화형 워크플로우가 필요할 때 사용하세요.
[code] 
    codex
[/code]

명령줄에서 초기 프롬프트를 지정할 수도 있습니다.
[code] 
    codex "Explain this codebase to me"
[/code]

세션을 열면 다음을 수행할 수 있습니다:

  * 프롬프트, 코드 스니펫, 스크린샷(예: [image inputs](https://developers.openai.com/codex/cli/features#image-inputs))을 바로 컴포저에 보낼 수 있습니다.
  * 변경 전에 Codex가 계획을 설명하는 과정을 지켜보고, 단계별로 승인하거나 거부할 수 있습니다.
  * 컴포저에서 `Up`/`Down`으로 초안 히스토리를 탐색하면 Codex가 이전 초안 텍스트와 이미지 플레이스홀더를 복원합니다.
  * 작업이 끝나면 `Ctrl`+`C`를 누르거나 `/exit`를 사용해 인터랙티브 세션을 종료합니다.



## 대화 재개

Codex는 대화 기록을 로컬에 저장하므로, 컨텍스트를 반복 설명하지 않고 이전 위치에서 다시 시작할 수 있습니다. 동일한 저장소 상태와 지시로 과거 스레드를 다시 열고 싶을 때 `resume` 서브커맨드를 사용하세요.

  * `codex resume`은 최근 인터랙티브 세션 목록을 띄웁니다. 실행을 선택해 요약을 확인한 뒤 `Enter`를 눌러 다시 열 수 있습니다.
  * `codex resume --all`은 현재 작업 디렉터리 외부의 세션까지 보여주므로, 로컬에서 실행한 어느 세션이든 다시 열 수 있습니다.
  * `codex resume --last`는 선택 화면을 건너뛰고 현재 작업 디렉터리에서 가장 최근 세션으로 바로 이동합니다(`--all`을 추가하면 작업 디렉터리 필터를 무시합니다).
  * `codex resume <SESSION_ID>`는 특정 실행을 지정합니다. ID는 선택 화면, `/status`, 또는 `~/.codex/sessions/` 아래 파일에서 복사할 수 있습니다.



비대화형 자동화 실행도 다시 시작할 수 있습니다:
[code] 
    codex exec resume --last "Fix the race conditions you found"
    codex exec resume 7f9f9a2e-1b3c-4c7a-9b0e-.... "Implement the plan"
[/code]

다시 시작된 각 실행은 원본 대화, 계획 히스토리, 승인 상태를 유지하므로, 새 지시를 제공하면서도 Codex가 이전 컨텍스트를 활용할 수 있습니다. 다시 시작하기 전에 환경을 조정하려면 `--cd`로 작업 디렉터리를 바꾸거나 `--add-dir`로 루트를 추가하세요.

## 모델과 추론

Codex에서 대부분의 코딩 작업에는 `gpt-5.3-codex` 모델이 기본 선택입니다. 이 모델은 ChatGPT 인증 Codex 세션에서 Codex 앱, CLI, IDE 확장, Codex Cloud 모두에서 사용할 수 있습니다. 더 빠른 작업을 위해 ChatGPT Pro 구독자는 연구 미리보기로 GPT-5.3-Codex-Spark 모델에 접근할 수 있습니다.

세션 도중 `/model` 명령으로 모델을 전환하거나, CLI를 시작할 때 모델을 지정하세요.
[code] 
    codex --model gpt-5.3-codex
[/code]

[Codex에서 사용 가능한 모델 더 알아보기](https://developers.openai.com/codex/models).

## 기능 플래그

Codex에는 소수의 기능 플래그가 포함되어 있습니다. `features` 서브커맨드를 사용해 사용 가능한 플래그를 확인하고 설정을 구성에 저장하세요.
[code] 
    codex features list
    codex features enable unified_exec
    codex features disable shell_snapshot
[/code]

`codex features enable <feature>`와 `codex features disable <feature>`는 `~/.codex/config.toml`에 기록됩니다. `--profile`로 Codex를 실행하면 루트 구성 대신 해당 프로필에 변경 사항을 저장합니다.

## 멀티 에이전트(실험적)

Codex 멀티 에이전트 워크플로우를 사용해 더 큰 작업을 병렬화하세요. 설정, 역할 구성(`config.toml`의 `[agents]`), 예시는 [Multi-agents](https://developers.openai.com/codex/multi-agent)를 참고하세요.

## 이미지 입력

스크린샷이나 디자인 사양을 첨부해, 프롬프트와 함께 이미지 세부 정보를 Codex가 읽을 수 있도록 하세요. 인터랙티브 컴포저에 이미지를 붙여 넣거나, 명령줄에서 파일을 제공할 수 있습니다.
[code] 
    codex -i screenshot.png "Explain this error"
[/code]
[code]

codex --image img1.png,img2.jpg "Summarize these diagrams"
[/code]

Codex는 PNG와 JPEG 같은 일반적인 형식을 지원합니다. 두 개 이상의 이미지는 파일 이름을 쉼표로 구분하고, 텍스트 지시와 함께 전달해 맥락을 보강하세요.

## 로컬 코드 리뷰 실행

CLI에서 `/review`를 입력하면 Codex의 리뷰 프리셋이 열립니다. CLI는 선택한 diff를 읽고, 워킹 트리를 건드리지 않은 채 우선순위가 높은 실행 가능한 인사이트를 보고하는 전용 리뷰어를 실행합니다. 기본적으로 현재 세션 모델을 사용하며, `config.toml`의 `review_model`을 설정해 변경할 수 있습니다.

  * **Review against a base branch**는 로컬 브랜치를 고르면 Codex가 업스트림과의 머지 베이스를 찾고, 작업 내용을 diff해서 풀 리퀘스트를 열기 전에 가장 큰 위험 요소를 강조합니다.
  * **Review uncommitted changes**는 스테이징 여부와 무관하게 모든 변경(스테이징됨/안 됨/추적되지 않음)을 검사해 커밋 전에 문제를 해결할 수 있게 합니다.
  * **Review a commit**은 최근 커밋을 나열하고, 선택한 SHA의 변경 집합을 Codex가 그대로 읽습니다.
  * **Custom review instructions**는 “접근성 회귀에 집중해 줘”처럼 원하는 문구를 입력하면 같은 리뷰어가 그 프롬프트로 실행됩니다.

각 리뷰 실행은 대화 내 별도 턴으로 기록되므로, 코드가 발전하는 동안 여러 번 리뷰를 다시 돌리고 피드백을 비교할 수 있습니다.

## 웹 검색

Codex에는 1st-party 웹 검색 도구가 포함되어 있습니다. Codex CLI의 로컬 작업에서는 기본적으로 웹 검색이 활성화되고, 웹 검색 캐시에서 결과를 제공합니다. 이 캐시는 OpenAI가 관리하는 웹 결과 인덱스이므로, 캐시 모드에서는 실시간 페이지를 가져오지 않고 사전 색인된 결과를 반환합니다. 임의의 라이브 콘텐츠로부터의 프롬프트 인젝션 노출을 줄여 주지만, 웹 결과는 여전히 신뢰할 수 없는 것으로 취급해야 합니다. `--yolo` 또는 다른 [full access sandbox setting](https://developers.openai.com/codex/security)을 사용할 때는 기본이 라이브 결과입니다. 가장 최신 데이터를 가져오려면 단일 실행에 `--search`를 전달하거나 [Config basics](https://developers.openai.com/codex/config-basic)에서 `web_search = "live"`를 설정하세요. 도구를 끄려면 `web_search = "disabled"`로 설정할 수도 있습니다.

Codex가 무언가를 조회할 때마다 대화나 `codex exec --json` 출력에 `web_search` 항목이 표시됩니다.

## 입력 프롬프트로 실행

빠른 답변만 필요할 때는 단일 프롬프트로 Codex를 실행하고 대화형 UI를 건너뛰세요.
[code] 
    codex "explain this codebase"
[/code]

Codex는 워킹 디렉터리를 읽고 플랜을 만든 뒤, 출력을 터미널로 스트리밍한 후 종료합니다. `--path` 같은 플래그로 특정 디렉터리를 지정하거나 `--model`로 선호 동작을 미리 조절해 함께 사용할 수 있습니다.

## 셸 자동 완성

사용 중인 셸에 맞는 자동 완성 스크립트를 설치해 일상적인 사용 속도를 높이세요.
[code] 
    codex completion bash
    codex completion zsh
    codex completion fish
[/code]

새 세션에서도 자동 완성이 동작하도록 셸 설정 파일에서 해당 스크립트를 실행하세요. 예를 들어 `zsh`를 사용한다면 `~/.zshrc` 끝에 다음을 추가할 수 있습니다.
[code] 
    # ~/.zshrc
    eval "$(codex completion zsh)"
[/code]

새 세션을 시작한 뒤 `codex`를 입력하고 `Tab`을 누르면 자동 완성이 보입니다. `command not found: compdef` 오류가 나타나면, `eval "$(codex completion zsh)"` 줄 앞에 `autoload -Uz compinit && compinit`을 `~/.zshrc`에 추가하고 셸을 다시 시작하세요.

## 승인 모드

승인 모드는 Codex가 확인 없이 수행할 수 있는 범위를 정의합니다. 대화형 세션에서 `/permissions`를 사용해 상황에 맞춰 모드를 전환하세요.

  * **Auto**(기본값)는 Codex가 워킹 디렉터리 내에서 파일을 읽고, 수정하고, 명령을 실행하도록 허용합니다. 그 범위를 벗어나거나 네트워크를 사용하려면 여전히 확인을 요청합니다.
  * **Read-only**는 Codex를 자문 모드로 유지합니다. 파일을 둘러볼 수는 있지만, 계획을 승인받기 전에는 변경하거나 명령을 실행하지 않습니다.

* **Full Access**는 Codex가 사용자의 기기 전반, 네트워크 접근을 포함해, 별도로 묻지 않고 작업할 수 있도록 허용합니다. 저장소와 작업을 충분히 신뢰할 때만 신중히 사용하세요.



Codex는 실행한 모든 조치를 항상 대화록으로 보여주므로, 일반적인 git 워크플로로 검토하거나 롤백할 수 있습니다.

## Scripting Codex

`exec` 하위 명령을 사용하면 Codex를 비대화식으로 실행해 워크플로를 자동화하거나 기존 스크립트에 Codex를 연결하고, 최종 계획과 결과를 `stdout`으로 전달할 수 있습니다.
[code] 
    codex exec "fix the CI failure"
[/code]

`exec`를 셸 스크립팅과 결합하면 변경 로그 자동 업데이트, 이슈 정렬, PR 출처 전 편집 검사 강제 등 맞춤 워크플로를 구축할 수 있습니다.

## Working with Codex cloud

`codex cloud` 명령을 사용하면 터미널을 벗어나지 않고 [Codex cloud tasks](https://developers.openai.com/codex/cloud)를 선별하고 실행할 수 있습니다. 인자를 생략해 실행하면 인터랙티브 피커가 열리며, 진행 중·완료된 작업을 둘러보고 변경 사항을 로컬 프로젝트에 적용할 수 있습니다.

터미널에서 바로 작업을 시작할 수도 있습니다:
[code] 
    codex cloud exec --env ENV_ID "Summarize open bugs"
[/code]

Codex cloud가 다중 해법을 생성하도록 하려면 `--attempts`(1–4)를 추가하세요. 예: `codex cloud exec --env ENV_ID --attempts 3 "Summarize open bugs"`.

Environment ID는 Codex cloud 구성에서 가져옵니다. `codex cloud` 실행 후 `Ctrl`+`O`로 환경을 선택하거나 웹 대시보드에서 정확한 값을 확인하세요. 인증은 기존 CLI 로그인을 따르며, 제출이 실패하면 명령이 비영(0)으로 종료되므로 스크립트나 CI에 연결하기 쉽습니다.

## Slash commands

Slash command를 사용하면 `/review`, `/fork` 등 특화된 워크플로 또는 재사용 가능한 프롬프트에 빠르게 접근할 수 있습니다. Codex에는 정선된 내장 명령이 포함되어 있고, 팀 전용 작업이나 개인 단축키를 위한 커스텀 명령도 만들 수 있습니다.

[slash commands guide](https://developers.openai.com/codex/guides/slash-commands)를 참고해 내장 목록을 살펴보고, 사용자 정의 명령 작성법과 디스크 상 위치를 확인하세요.

## Prompt editor

긴 프롬프트를 작성할 때는 전체 편집기로 전환한 뒤 결과를 컴포저로 다시 보내는 편이 더 쉬울 수 있습니다.

프롬프트 입력에서 `Ctrl`+`G`를 눌러 `VISUAL` 환경 변수(설정되지 않았다면 `EDITOR`)에 지정된 편집기를 엽니다.

## Model Context Protocol (MCP)

Model Context Protocol 서버를 구성해 Codex를 더 많은 도구와 연결하세요. `~/.codex/config.toml`에 STDIO 또는 스트리밍 HTTP 서버를 추가하거나 `codex mcp` CLI 명령으로 관리하면, Codex가 세션 시작 시 자동으로 서버를 실행하고 내장 도구 옆에 노출합니다. 다른 에이전트 안에서 필요할 때 Codex 자체를 MCP 서버로 실행할 수도 있습니다.

예제 구성, 지원되는 인증 흐름, 보다 자세한 가이드는 [Model Context Protocol](https://developers.openai.com/codex/mcp)에서 확인하세요.

## Tips and shortcuts

  * 컴포저에서 `@`를 입력하면 워크스페이스 루트를 기준으로 퍼지 파일 검색이 열립니다. `Tab` 또는 `Enter`로 하이라이트된 경로를 메시지에 삽입하세요.
  * Codex 실행 중 `Enter`를 눌러 현재 턴에 새 지시를 주입하거나, `Tab`을 눌러 다음 턴용 후속 프롬프트를 예약하세요.
  * 행 앞에 `!`를 붙이면 로컬 셸 명령(예: `!ls`)을 실행합니다. Codex는 출력을 사용자 제공 명령 결과처럼 다루면서도 승인·샌드박스 설정을 유지합니다.
  * 컴포저가 비어 있을 때 `Esc`를 두 번 눌러 이전 사용자 메시지를 편집하세요. 계속 `Esc`를 눌러 대화록을 더 거슬러 올라간 뒤, 해당 지점에서 분기하려면 `Enter`를 누르세요.
  * 어느 디렉터리에서든 `codex --cd <path>`로 Codex를 실행해 `cd` 없이 작업 루트를 설정합니다. 활성 경로는 TUI 헤더에 표시됩니다.

* 여러 프로젝트에서 변경을 조율해야 할 때에는 `--add-dir`를 사용해 더 많은 쓰기 가능한 루트를 노출하세요 (예: `codex --cd apps/frontend --add-dir ../backend --add-dir ../shared`).
  * Codex를 실행하기 전에 환경을 미리 설정해 두면 무엇을 활성화할지 탐색하느라 토큰을 낭비하지 않습니다. 예를 들어 Python 가상환경(또는 다른 언어 환경)을 소싱하고 필요한 데몬을 시작하며 사용할 환경 변수를 미리 export하세요.
