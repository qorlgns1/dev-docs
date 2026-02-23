---
title: 'Codex CLI'
description: 'description: "Codex CLI는 터미널에서 로컬로 실행할 수 있는 OpenAI의 코딩 에이전트입니다. 선택한 디렉터리에서 머신의 코드를 읽고, 변경하고, 실행할 수 있습니다..."'
---

title: 'Codex CLI'
description: "Codex CLI는 터미널에서 로컬로 실행할 수 있는 OpenAI의 코딩 에이전트입니다. 선택한 디렉터리에서 머신의 코드를 읽고, 변경하고, 실행할 수 있습니다..."

Source URL: https://developers.openai.com/codex/cli

# Codex CLI

Codex CLI는 터미널에서 로컬로 실행할 수 있는 OpenAI의 코딩 에이전트입니다. 선택한 디렉터리에서 머신의 코드를 읽고, 변경하고, 실행할 수 있습니다.
빠르고 효율적인 실행을 위해 Rust로 작성되었으며 [오픈 소스](https://github.com/openai/codex)입니다.

Codex는 ChatGPT Plus, Pro, Business, Edu, Enterprise 플랜에 포함되어 있습니다. 포함된 내용은 [여기](https://developers.openai.com/codex/pricing)에서 확인하세요.

- [Codex CLI 개요](https://www.youtube.com/watch?v=iqNzfK4_meQ)

## CLI 설정

Codex CLI는 macOS와 Linux에서 사용할 수 있습니다. Windows 지원은
  실험적입니다. Windows에서 최적의 경험을 얻으려면 WSL 작업 공간에서 Codex를 사용하고
  우리의 <a href="/codex/windows">Windows 설정 가이드</a>를 따르세요.

---

## Codex CLI로 작업하기

- [Codex 대화형 실행](https://developers.openai.com/codex/cli/features#running-in-interactive-mode)

`codex`를 실행하여 대화형 터미널 UI(TUI) 세션을 시작하세요.

- [모델 및 추론 제어](https://developers.openai.com/codex/cli/features#models-reasoning)

`/model`을 사용하여 GPT-5.3-Codex 및 사용 가능한 다른 모델 사이를 전환하거나 추론 수준을 조정하세요.

- [이미지 입력](https://developers.openai.com/codex/cli/features#image-inputs)

스크린샷이나 디자인 명세서를 첨부하여 Codex가 프롬프트와 함께 읽을 수 있게 하세요.

- [로컬 코드 리뷰 실행](https://developers.openai.com/codex/cli/features#running-local-code-review)

변경 사항을 커밋하거나 푸시하기 전에 별도의 Codex 에이전트로 코드 리뷰를 받으세요.

- [멀티 에이전트 사용](https://developers.openai.com/codex/multi-agent)

실험적인 멀티 에이전트 협업을 활성화하여 복잡한 작업을 병렬화하세요.

- [웹 검색](https://developers.openai.com/codex/cli/features#web-search)

Codex를 사용하여 웹을 검색하고 작업에 최신 정보를 가져오세요.

- [Codex Cloud 작업](https://developers.openai.com/codex/cli/features#working-with-codex-cloud)

Codex Cloud 작업을 시작하고, 환경을 선택하고, 터미널을 떠나지 않고 결과 diff를 적용하세요.

- [Codex 스크립팅](https://developers.openai.com/codex/sdk#using-codex-cli-programmatically)

`exec` 명령으로 Codex를 스크립팅하여 반복 가능한 워크플로를 자동화하세요.

- [모델 컨텍스트 프로토콜](https://developers.openai.com/codex/mcp)

Model Context Protocol(MCP)을 통해 Codex에 추가 서드파티 도구와 컨텍스트 접근을 제공하세요.

- [승인 모드](https://developers.openai.com/codex/cli/features#approval-modes)

Codex가 명령을 편집하거나 실행하기 전에 자신의 편안한 수준에 맞는 승인 모드를 선택하세요.

