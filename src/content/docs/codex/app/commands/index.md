---
title: Codex 앱 명령어
description: 이 명령어와 키보드 단축키를 사용해 Codex 앱을 탐색하세요.
---

# Codex 앱 명령어

Source URL: https://developers.openai.com/codex/app/commands

이 명령어와 키보드 단축키를 사용해 Codex 앱을 탐색하세요.

## 키보드 단축키

| 동작| macOS 단축키  
---|---|---  
**일반**| |   
|  명령 메뉴| `Cmd` \+ `Shift` \+ `P` 또는 `Cmd` \+ `K`  
| 설정| `Cmd` \+ `,`  
| 폴더 열기| `Cmd` \+ `O`  
| 뒤로 이동| `Cmd` \+ `[`  
| 앞으로 이동| `Cmd` \+ `]`  
| 글꼴 크기 키우기| `Cmd` \+ `+` 또는 `Cmd` \+ `=`  
| 글꼴 크기 줄이기| `Cmd` \+ `-` 또는 `Cmd` \+ `_`  
| 사이드바 토글| `Cmd` \+ `B`  
| diff 패널 토글| `Cmd` \+ `Option` \+ `B`  
| 터미널 토글| `Cmd` \+ `J`  
| 터미널 지우기| `Ctrl` \+ `L`  
**스레드**| |   
|  새 스레드| `Cmd` \+ `N` 또는 `Cmd` \+ `Shift` \+ `O`  
| 스레드에서 찾기| `Cmd` \+ `F`  
| 이전 스레드| `Cmd` \+ `Shift` \+ `[`  
| 다음 스레드| `Cmd` \+ `Shift` \+ `]`  
| 받아쓰기| `Ctrl` \+ `M`  
  
## 슬래시 명령어

슬래시 명령어를 사용하면 스레드 컴포저를 벗어나지 않고 Codex를 제어할 수 있습니다. 사용 가능한 명령어는 환경과 접근 권한에 따라 달라집니다.

### 슬래시 명령어 사용하기

  1. 스레드 컴포저에서 `/`를 입력합니다.
  2. 목록에서 명령어를 선택하거나, 계속 입력해 필터링합니다(예: `/status`).



스레드 컴포저에서 `$`를 입력해 스킬을 명시적으로 호출할 수도 있습니다. [Skills](https://developers.openai.com/codex/skills)를 참고하세요.

활성화된 스킬은 슬래시 명령어 목록에도 표시됩니다(예: `/imagegen`).

### 사용 가능한 슬래시 명령어

슬래시 명령어| 설명  
---|---  
`/feedback`| 피드백을 제출하고 필요 시 로그를 포함할 수 있는 피드백 대화상자를 엽니다.  
`/mcp`| 연결된 서버를 확인할 수 있도록 MCP 상태를 엽니다.  
`/plan-mode`| 다단계 계획을 위한 계획 모드를 전환합니다.  
`/review`| 커밋되지 않은 변경 사항을 검토하거나 기준 브랜치와 비교하는 코드 리뷰 모드를 시작합니다.  
`/status`| 스레드 ID, 컨텍스트 사용량, 속도 제한을 표시합니다.  
  
## 함께 보기

  * [기능](https://developers.openai.com/codex/app/features)
  * [설정](https://developers.openai.com/codex/app/settings)
