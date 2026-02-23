---
title: 'Codex 앱 명령'
description: '이 명령어와 키보드 단축키를 사용해 Codex 앱을 탐색하세요.'
---

Source URL: https://developers.openai.com/codex/app/commands

# Codex 앱 명령

이 명령어와 키보드 단축키를 사용해 Codex 앱을 탐색하세요.

## 키보드 단축키

|             | 동작               | macOS 단축키                                                                      |
| ----------- | ------------------ | --------------------------------------------------------------------------------- |
| **일반**    |                    |                                                                                   |
|             | 명령 메뉴          | <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> 또는 <kbd>Cmd</kbd> + <kbd>K</kbd> |
|             | 설정               | <kbd>Cmd</kbd> + <kbd>,</kbd>                                                     |
|             | 폴더 열기          | <kbd>Cmd</kbd> + <kbd>O</kbd>                                                     |
|             | 뒤로 이동          | <kbd>Cmd</kbd> + <kbd>[</kbd>                                                     |
|             | 앞으로 이동        | <kbd>Cmd</kbd> + <kbd>]</kbd>                                                     |
|             | 글꼴 크기 키우기   | <kbd>Cmd</kbd> + <kbd>+</kbd> 또는 <kbd>Cmd</kbd> + <kbd>=</kbd>                    |
|             | 글꼴 크기 줄이기   | <kbd>Cmd</kbd> + <kbd>-</kbd> 또는 <kbd>Cmd</kbd> + <kbd>\_</kbd>                   |
|             | 사이드바 토글      | <kbd>Cmd</kbd> + <kbd>B</kbd>                                                     |
|             | 변경 사항 패널 토글 | <kbd>Cmd</kbd> + <kbd>Option</kbd> + <kbd>B</kbd>                                 |
|             | 터미널 토글        | <kbd>Cmd</kbd> + <kbd>J</kbd>                                                     |
|             | 터미널 초기화       | <kbd>Ctrl</kbd> + <kbd>L</kbd>                                                    |
| **스레드**  |                    |                                                                                   |
|             | 새 스레드          | <kbd>Cmd</kbd> + <kbd>N</kbd> 또는 <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>O</kbd> |
|             | 스레드 내 검색     | <kbd>Cmd</kbd> + <kbd>F</kbd>                                                     |
|             | 이전 스레드        | <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>[</kbd>                                  |
|             | 다음 스레드        | <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>]</kbd>                                  |
|             | 받아쓰기           | <kbd>Ctrl</kbd> + <kbd>M</kbd>                                                    |

## 슬래시 명령

슬래시 명령을 사용하면 스레드 작성기에서 벗어나지 않고 Codex를 제어할 수 있습니다. 사용 가능한 명령은 환경과 권한에 따라 달라집니다.

### 슬래시 명령 사용법

1. 스레드 작성기에서 `/`를 입력합니다.
2. 목록에서 명령을 선택하거나 (예: `/status`) 계속 입력하여 필터링합니다.

스레드 작성기에서 `$`를 입력하면 스킬을 명시적으로 호출할 수도 있습니다. [스킬](https://developers.openai.com/codex/skills)을 참조하세요.

활성화된 스킬은 슬래시 명령 목록에도 표시됩니다 (예: `/imagegen`).

### 사용 가능한 슬래시 명령

| 슬래시 명령     | 설명                                                                                 |
| --------------- | ------------------------------------------------------------------------------------ |
| `/feedback`     | 피드백 대화 상자를 열어 피드백을 제출하고 로그를 선택적으로 포함합니다.              |
| `/mcp`          | 연결된 서버를 확인하려면 MCP 상태를 엽니다.                                          |
| `/plan-mode`    | 다단계 계획을 위한 플랜 모드를 토글합니다.                                           |
| `/review`       | 커밋되지 않은 변경사항을 검토하거나 기준 브랜치와 비교할 수 있는 코드 리뷰 모드를 시작합니다. |
| `/status`       | 스레드 ID, 컨텍스트 사용량, 속도 제한을 표시합니다.                                  |

## 참고

- [기능](https://developers.openai.com/codex/app/features)
- [설정](https://developers.openai.com/codex/app/settings)
