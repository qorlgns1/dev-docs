---
title: Codex IDE 확장 프로그램
description: Codex는 코드를 읽고, 편집하고, 실행할 수 있는 OpenAI의 코딩 에이전트입니다. 개발 속도를 높이고 버그를 없애며, 익숙하지 않은 코드를 이해하도록 도와줍니다. Codex VS Code 확장 프로그램을 사용하면 IDE에서 Codex와 나란히 작업하거나 Code...
sidebar:
  order: 21
---

# Codex IDE 확장 프로그램

Source URL: https://developers.openai.com/codex/ide

Codex는 코드를 읽고, 편집하고, 실행할 수 있는 OpenAI의 코딩 에이전트입니다. 개발 속도를 높이고 버그를 없애며, 익숙하지 않은 코드를 이해하도록 도와줍니다. Codex VS Code 확장 프로그램을 사용하면 IDE에서 Codex와 나란히 작업하거나 Codex Cloud에 작업을 위임할 수 있습니다.

ChatGPT Plus, Pro, Business, Edu, Enterprise 요금제에는 Codex가 포함됩니다. [포함된 기능](https://developers.openai.com/codex/pricing)에 대해 자세히 알아보세요.

  


## 확장 프로그램 설정

Codex IDE 확장 프로그램은 Cursor, Windsurf 같은 VS Code 포크에서도 작동합니다.

[Visual Studio Code 마켓플레이스](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt)에서 Codex 확장 프로그램을 설치하거나 IDE별 다운로드 링크를 사용할 수 있습니다.

  * [Visual Studio Code용 다운로드](vscode:extension/openai.chatgpt)
  * [Cursor용 다운로드](cursor:extension/openai.chatgpt)
  * [Windsurf용 다운로드](windsurf:extension/openai.chatgpt)
  * [Visual Studio Code Insiders용 다운로드](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt)
  * [JetBrains IDE용 다운로드](https://developers.openai.com/codex/ide#jetbrains-ide-integration)



Codex VS Code 확장 프로그램은 macOS와 Linux에서 사용할 수 있습니다. Windows 지원은 실험적 단계입니다. Windows에서 최적의 환경을 원한다면 WSL 작업공간에서 Codex를 사용하고 [Windows 설정 가이드](https://developers.openai.com/codex/windows)를 따라주세요.

설치가 완료되면 왼쪽 사이드바의 다른 확장 프로그램 옆에서 Codex를 찾을 수 있습니다. VS Code에서 Codex가 바로 보이지 않으면 에디터를 재시작하세요.

Cursor를 사용하는 경우 기본적으로 활동 표시줄이 가로로 표시됩니다. 접힌 항목이 Codex를 숨길 수 있으니, Codex를 고정하고 확장 프로그램 순서를 재정렬하세요.

## JetBrains IDE 통합

Rider, IntelliJ, PyCharm, WebStorm 등 JetBrains IDE에서 Codex를 사용하려면 JetBrains IDE 통합을 설치하세요. ChatGPT 계정, API 키, JetBrains AI 구독 중 원하는 방식으로 로그인할 수 있습니다.

[JetBrains IDE용 Codex 설치](https://blog.jetbrains.com/ai/2026/01/codex-in-jetbrains-ides/)

### Codex를 오른쪽 사이드바로 이동하기 

VS Code에서는 Codex 아이콘을 에디터 오른쪽으로 드래그해 오른쪽 사이드바로 옮길 수 있습니다.

Cursor처럼 일부 IDE에서는 먼저 활동 표시줄 방향을 임시로 변경해야 할 수 있습니다.

  1. 에디터 설정을 열고 Workbench 설정에서 `activity bar`를 검색합니다.
  2. 방향을 `vertical`로 바꿉니다.
  3. 에디터를 재시작합니다.



이제 Codex 아이콘을 오른쪽 사이드바(예: Cursor 채팅 옆)로 드래그하세요. Codex는 사이드바의 또 다른 탭으로 표시됩니다.

이동을 마친 뒤 활동 표시줄 방향을 `horizontal`로 되돌려 기본 동작을 복원하세요.

### 로그인

확장 프로그램을 설치하면 ChatGPT 계정 또는 API 키로 로그인하라는 메시지가 표시됩니다. ChatGPT 요금제에는 사용 크레딧이 포함되어 있어 추가 설정 없이 Codex를 사용할 수 있습니다. 자세한 내용은 [요금 페이지](https://developers.openai.com/codex/pricing)를 참고하세요.

### 확장 프로그램 업데이트

확장 프로그램은 자동으로 업데이트되지만, IDE에서 확장 프로그램 페이지를 열어 직접 업데이트가 있는지 확인할 수도 있습니다.

### 키보드 단축키 설정

Codex에는 IDE 설정에서 키보드 단축키로 바인딩할 수 있는 여러 명령이 포함되어 있습니다(예: Codex 채팅 토글, Codex 컨텍스트에 항목 추가).

사용 가능한 모든 명령을 확인하고 단축키로 바인딩하려면 Codex 채팅에서 설정 아이콘을 선택하고 **Keyboard shortcuts**를 선택하세요. [Codex IDE 확장 프로그램 명령](https://developers.openai.com/codex/ide/commands) 페이지도 참고할 수 있습니다. 지원되는 슬래시 명령 목록은 [Codex IDE 확장 프로그램 슬래시 명령](https://developers.openai.com/codex/ide/slash-commands)을 확인하세요.

* * *

## Codex IDE 확장 프로그램으로 작업하기

### [에디터 컨텍스트로 프롬프트 작성 열려 있는 파일, 선택 영역, `@file` 참조를 활용해 더 짧은 프롬프트로도 더 관련성 높은 결과를 얻으세요.](https://developers.openai.com/codex/ide/features#prompting-codex)
### [모델 전환 기본 모델을 사용하거나 다른 모델로 전환해 각 모델의 강점을 활용하세요.](https://developers.openai.com/codex/ide/features#switch-between-models)
### [추론 강도 조절 작업에 따라 속도와 깊이 사이에서 균형을 맞추려면 `low`, `medium`, `high` 중에서 선택하세요.](https://developers.openai.com/codex/ide/features#adjust-reasoning-effort)
### [승인 모드 선택 Codex에 부여하고 싶은 자율성 수준에 따라 `Chat`, `Agent`, `Agent (Full Access)` 사이를 전환하세요.](https://developers.openai.com/codex/ide/features#choose-an-approval-mode)
### [클라우드에 위임 IDE를 떠나지 않고도 더 긴 작업을 클라우드 환경으로 넘기고 진행 상황을 모니터링하며 결과를 검토하세요.](https://developers.openai.com/codex/ide/features#cloud-delegation)
### [클라우드 작업 후속 조치 클라우드에서 생성된 변경 사항을 미리 보고 후속 작업을 요청한 뒤, 생성된 diff를 로컬에 적용해 테스트와 마무리를 진행하세요.](https://developers.openai.com/codex/ide/features#cloud-task-follow-up)
### [IDE 확장 명령 커맨드 팔레트에서 실행하거나 키보드 단축키에 바인딩할 수 있는 전체 명령 목록을 살펴보세요.](https://developers.openai.com/codex/ide/commands)
### [슬래시 명령 슬래시 명령으로 Codex 동작을 제어하고 채팅에서 자주 쓰는 설정을 빠르게 변경하세요.](https://developers.openai.com/codex/ide/slash-commands)
### [확장 설정 모델, 승인, 기타 기본값에 대한 에디터 설정으로 Codex를 워크플로에 맞게 조정하세요.](https://developers.openai.com/codex/ide/settings)
