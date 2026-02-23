---
title: 'Codex IDE 확장'
description: 'Codex는 OpenAI의 코딩 에이전트로, 코드를 읽고 수정하며 실행할 수 있습니다. 더 빠르게 개발하고 버그를 해결하며 생소한 코드를 이해하는 데 도움을 줍니다. Codex VS Code 확장 기능을 사용하면 IDE에서 Codex를 나란히 사용하거나 Codex Cl...'
---

Source URL: https://developers.openai.com/codex/ide

# Codex IDE 확장

Codex는 OpenAI의 코딩 에이전트로, 코드를 읽고 수정하며 실행할 수 있습니다. 더 빠르게 개발하고 버그를 해결하며 생소한 코드를 이해하는 데 도움을 줍니다. Codex VS Code 확장 기능을 사용하면 IDE에서 Codex를 나란히 사용하거나 Codex Cloud에 작업을 위임할 수 있습니다.

ChatGPT Plus, Pro, Business, Edu, Enterprise 플랜에는 Codex가 포함되어 있습니다. [포함 내역](https://developers.openai.com/codex/pricing)을 확인하세요.

- [Codex IDE 확장 개요](https://www.youtube.com/watch?v=sd21Igx4HtA)

## 확장 설정

Codex IDE 확장은 Cursor나 Windsurf 같은 VS Code 포크에서도 작동합니다.

[Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt)에서 Codex 확장을 받거나 다음 IDE용으로 다운로드할 수 있습니다:

- [Visual Studio Code용 다운로드](vscode:extension/openai.chatgpt)
- [Cursor용 다운로드](cursor:extension/openai.chatgpt)
- [Windsurf용 다운로드](windsurf:extension/openai.chatgpt)
- [Visual Studio Code Insiders용 다운로드](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt)
- [JetBrains IDE용 다운로드](#jetbrains-ide-integration)

Codex VS Code 확장은 macOS와 Linux에서 사용할 수 있습니다. Windows 지원은 실험적이며, Windows에서 가장 원활하게 사용하려면 WSL 작업 공간에서 Codex를 사용하고 <a href="/codex/windows">Windows 설정 가이드</a>를 따르세요.

설치 후 왼쪽 사이드바에서 다른 확장과 함께 Codex를 확인할 수 있습니다.
VS Code를 사용 중이고 Codex가 바로 보이지 않으면 에디터를 재시작하세요.

Cursor를 사용 중이라면 활동 표시줄이 기본적으로 수평으로 표시됩니다. 축소된 항목이 Codex를 숨길 수 있으니 Codex를 고정하고 확장 순서를 재조정하세요.

  <img src="https://cdn.openai.com/devhub/docs/codex-extension.webp"
    alt="Codex extension"
    class="block h-auto w-full mx-0!"
  />

## JetBrains IDE 통합

Rider, IntelliJ, PyCharm, WebStorm 같은 JetBrains IDE에서 Codex를 사용하려면 JetBrains IDE 통합을 설치하세요. ChatGPT, API 키 또는 JetBrains AI 구독으로 로그인할 수 있습니다.

[JetBrains IDE용 Codex 설치](https://blog.jetbrains.com/ai/2026/01/codex-in-jetbrains-ides/)

### Codex를 오른쪽 사이드바로 이동하기 <a id="right-sidebar"></a>

VS Code에서 Codex 아이콘을 드래그하여 에디터 오른쪽으로 옮기면 오른쪽 사이드바로 위치를 변경할 수 있습니다.

Cursor처럼 일부 IDE에서는 먼저 활동 표시줄 방향을 일시적으로 변경해야 할 수도 있습니다:

1. 에디터 설정에서 `activity bar`를 검색합니다 (Workbench 설정).
2. 방향을 `vertical`로 변경합니다.
3. 에디터를 재시작합니다.

![codex-workbench-setting](https://cdn.openai.com/devhub/docs/codex-workbench-setting.webp)

이제 Codex 아이콘을 오른쪽 사이드바(예: Cursor 채팅 옆)로 드래그하세요. Codex는 사이드바의 또 다른 탭으로 표시됩니다.

이동을 마친 후 활동 표시줄 방향을 기본값인 `horizontal`로 다시 설정하여 기본 동작을 복원하세요.

### 로그인

확장을 설치하면 ChatGPT 계정 또는 API 키로 로그인하라는 메시지가 나타납니다. ChatGPT 플랜에는 사용 크레딧이 포함되어 있으므로 별도 설정 없이 Codex를 사용할 수 있습니다. [요금 페이지](https://developers.openai.com/codex/pricing)에서 자세히 알아보세요.

### 확장 업데이트

확장은 자동으로 업데이트되며, IDE에서 확장 페이지를 열어 업데이트를 확인할 수도 있습니다.

### 키보드 단축키 설정

Codex에는 IDE 설정에서 키보드 단축키로 바인딩할 수 있는 명령이 포함되어 있습니다(예: Codex 채팅 전환 또는 Codex 컨텍스트에 항목 추가).

모든 명령을 보고 키보드 단축키로 바인딩하려면 Codex 채팅에서 설정 아이콘을 선택하고 **Keyboard shortcuts**를 선택하세요.
또한 [Codex IDE 확장 명령](https://developers.openai.com/codex/ide/commands) 페이지를 참고할 수 있습니다.
지원되는 슬래시 명령 목록은 [Codex IDE 확장 슬래시 명령](https://developers.openai.com/codex/ide/slash-commands)을 확인하세요.

---

## Codex IDE 확장 활용법

- [편집기 컨텍스트로 프롬프트 작성](https://developers.openai.com/codex/ide/features#prompting-codex)

열려 있는 파일, 선택 영역, `@file` 참조를 활용하여 더 관련성 높은 결과를 더 짧은 프롬프트로 얻어보세요.

- [모델 전환](https://developers.openai.com/codex/ide/features#switch-between-models)

기본 모델을 사용하거나 다른 모델로 전환하여 각 모델의 장점을 활용하세요.

- [추론 강도 조정](https://developers.openai.com/codex/ide/features#adjust-reasoning-effort)

작업에 따라 속도와 깊이의 균형을 맞추기 위해 `low`, `medium`, `high` 중 선택하세요.

- [승인 모드 선택](https://developers.openai.com/codex/ide/features#choose-an-approval-mode)

Codex에게 원하는 자율성 수준에 따라 `Chat`, `Agent`, `Agent (Full Access)`를 전환하세요.

- [클라우드로 위임](https://developers.openai.com/codex/ide/features#cloud-delegation)

더 긴 작업을 클라우드 환경에 맡기고 IDE를 떠나지 않고도 진행 상황을 모니터링하고 결과를 검토하세요.

- [클라우드 작업에 대한 후속 조치](https://developers.openai.com/codex/ide/features#cloud-task-follow-up)

클라우드 변경 사항을 미리 보고, 후속 요청을 하며, 결과로 나온 diff를 로컬에 적용해 테스트하고 마무리하세요.

- [IDE 확장 명령](https://developers.openai.com/codex/ide/commands)

명령 팔레트에서 실행하거나 키보드 단축키에 바인딩할 수 있는 전체 명령 목록을 둘러보세요.

- [슬래시 명령](https://developers.openai.com/codex/ide/slash-commands)

슬래시 명령을 사용하여 Codex 동작을 제어하고 채팅에서 일반 설정을 빠르게 변경하세요.

- [확장 설정](https://developers.openai.com/codex/ide/settings)

모델, 승인 및 기타 기본값에 대한 편집기 설정으로 작업 흐름에 Codex를 맞춰보세요.
