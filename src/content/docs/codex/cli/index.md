---
title: Codex CLI
description: "출처 URL: https://developers.openai.com/codex/cli"
sidebar:
  order: 22
---

# Codex CLI

출처 URL: https://developers.openai.com/codex/cli

Codex CLI는 터미널에서 로컬로 실행할 수 있는 OpenAI의 코딩 에이전트입니다. 선택한 디렉터리의 코드를 읽고, 수정하고, 실행할 수 있습니다. Rust로 구축된 [오픈 소스](https://github.com/openai/codex) 프로젝트로 속도와 효율을 제공합니다.

Codex는 ChatGPT Plus, Pro, Business, Edu, Enterprise 플랜에 포함되어 있습니다. 어떤 항목이 포함되어 있는지는 [구성 안내](https://developers.openai.com/codex/pricing)를 참고하세요.

  


## CLI 설정

패키지 관리자를 선택하세요

npm홈브루

  1. 1

### 설치

npm으로 Codex CLI를 설치하세요.

npm 설치 명령

npm i -g @openai/codexCopy

  2. 2

### 실행

터미널에서 Codex를 실행하면 리포지토리를 살펴보고, 파일을 편집하고, 명령을 실행할 수 있습니다.

Codex 실행 명령

codexCopy

Codex를 처음 실행하면 로그인하라는 메시지가 표시됩니다. ChatGPT 계정 또는 API 키로 인증하세요.

어떤 플랜에 Codex가 포함되는지 확실하지 않다면 [가격 페이지](https://developers.openai.com/codex/pricing)를 확인하세요.

  3. 3

### 업그레이드

Codex CLI의 새 버전은 정기적으로 릴리스됩니다. 릴리스 노트는 [변경 로그](https://developers.openai.com/codex/changelog)에서 확인하세요. npm으로 업그레이드하려면 다음을 실행하세요.

npm 업그레이드 명령

npm i -g @openai/codex@latestCopy




Codex CLI는 macOS와 Linux에서 사용할 수 있습니다. Windows 지원은 실험 단계입니다. 최상의 Windows 환경을 위해서는 WSL 워크스페이스에서 Codex를 사용하고 [Windows 설정 가이드](https://developers.openai.com/codex/windows)를 따르세요.

* * *

## Codex CLI로 작업

### [Codex를 대화형으로 실행합니다. `codex`를 실행해 대화형 터미널 UI(TUI) 세션을 시작하세요.](https://developers.openai.com/codex/cli/features#running-in-interactive-mode)
### [모델과 추론을 제어합니다. `/model`을 사용해 GPT-5.3-Codex와 다른 사용 가능 모델을 전환하거나 추론 수준을 조정하세요.](https://developers.openai.com/codex/cli/features#models-reasoning)
### [이미지 입력을 사용합니다. 스크린샷이나 디자인 사양을 첨부하여 프롬프트와 함께 Codex가 읽도록 하세요.](https://developers.openai.com/codex/cli/features#image-inputs)
### [로컬 코드 리뷰를 실행합니다. 커밋이나 푸시 전에 별도의 Codex 에이전트로부터 코드를 리뷰받으세요.](https://developers.openai.com/codex/cli/features#running-local-code-review)
### [멀티 에이전트를 사용합니다. 실험적 멀티 에이전트 협업을 활성화해 복잡한 작업을 병렬화하세요.](https://developers.openai.com/codex/multi-agent)
### [웹 검색을 활용합니다. Codex로 웹을 검색해 작업에 필요한 최신 정보를 얻으세요.](https://developers.openai.com/codex/cli/features#web-search)
### [Codex Cloud 작업을 실행합니다. 터미널을 떠나지 않고 Codex Cloud 작업을 실행하고 환경을 선택한 뒤 생성된 diff를 적용하세요.](https://developers.openai.com/codex/cli/features#working-with-codex-cloud)
### [Codex 스크립팅을 활용합니다. `exec` 명령으로 Codex를 스크립팅해 반복 가능한 워크플로를 자동화하세요.](https://developers.openai.com/codex/sdk#using-codex-cli-programmatically)
### [Model Context Protocol을 사용합니다. Model Context Protocol(MCP)로 Codex에 추가 서드파티 도구와 컨텍스트에 대한 접근 권한을 부여하세요.](https://developers.openai.com/codex/mcp)
### [승인 모드를 선택합니다. Codex가 편집하거나 명령을 실행하기 전에 본인에게 맞는 승인 모드를 고르세요.](https://developers.openai.com/codex/cli/features#approval-modes)