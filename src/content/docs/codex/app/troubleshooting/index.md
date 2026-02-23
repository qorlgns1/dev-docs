---
title: 문제 해결
description: "원본 URL: https://developers.openai.com/codex/app/troubleshooting"
sidebar:
  order: 9
---

# 문제 해결

원본 URL: https://developers.openai.com/codex/app/troubleshooting

## 자주 묻는 질문

### Codex가 수정하지 않은 파일이 사이드 패널에 표시됩니다

프로젝트가 Git 리포지토리 안에 있으면, 리뷰 패널은 프로젝트의 Git 상태를 기준으로 변경사항을 자동 표시하며, 여기에는 Codex가 만들지 않은 변경도 포함됩니다.

리뷰 패널에서는 staged 변경과 아직 staged되지 않은 변경 사이를 전환할 수 있고, 현재 브랜치를 main과 비교할 수 있습니다.

마지막 Codex 턴의 변경사항만 보고 싶다면, diff 패널을 “Last turn changes” 보기로 전환하세요.

[review pane 사용법 자세히 보기](https://developers.openai.com/codex/app/review).

### 사이드바에서 프로젝트 제거하기

사이드바에서 프로젝트를 제거하려면 프로젝트 이름 위에 마우스를 올리고 점 3개를 클릭한 뒤 “Remove”를 선택하세요. 복원하려면 **Threads** 옆의 **Add new project** 버튼으로 프로젝트를 다시 추가하거나

`Cmd`+`O`

를 사용하세요.

### 아카이브된 스레드 찾기

아카이브된 스레드는 [Settings](codex://settings)에서 찾을 수 있습니다. 스레드의 아카이브를 해제하면 사이드바의 원래 위치에 다시 나타납니다.

### 사이드바에 일부 스레드만 표시됩니다

사이드바는 프로젝트 상태에 따라 스레드를 필터링할 수 있습니다. 스레드가 보이지 않는다면 **Threads** 라벨 옆 필터 아이콘을 클릭해 필터가 적용되어 있는지 확인하세요.

### worktree에서 코드가 실행되지 않습니다

Worktree는 다른 디렉터리에 생성되며 Git에 체크인된 파일만 상속합니다. 프로젝트의 의존성 및 도구 관리 방식에 따라 [local environment](https://developers.openai.com/codex/app/local-environments)를 사용해 worktree에서 일부 설정 스크립트를 실행해야 할 수 있습니다. 또는 일반 로컬 프로젝트에서 변경사항을 체크아웃할 수도 있습니다. 자세한 내용은 [worktrees documentation](https://developers.openai.com/codex/app/worktrees)을 확인하세요.

### 앱이 팀원의 공유 local environment를 인식하지 못합니다

local environment 설정은 프로젝트 루트의 `.codex` 폴더 안에 있어야 합니다. 여러 프로젝트가 있는 모노레포에서 작업 중이라면, `.codex` 폴더가 있는 디렉터리에서 프로젝트를 열었는지 확인하세요.

### Codex가 Apple Music 접근을 요청합니다

작업에 따라 Codex가 파일 시스템을 탐색해야 할 수 있습니다. macOS의 Music, Downloads, Desktop 같은 특정 디렉터리는 사용자 추가 승인이 필요합니다. Codex가 홈 디렉터리를 읽어야 하면 macOS가 해당 폴더 접근 승인을 요청합니다.

### 자동화로 worktree가 많이 생성됩니다

자동화를 자주 실행하면 시간이 지나면서 worktree가 많이 생성될 수 있습니다. 더 이상 필요 없는 자동화 실행은 아카이브하고, worktree를 유지할 의도가 없다면 실행을 pin하지 마세요.

### 잘못된 대상 선택 후 프롬프트 복구하기

실수로 잘못된 대상(**Local** , **Worktree** , 또는 **Cloud**)으로 스레드를 시작했다면, 현재 실행을 취소하고 composer에서 위쪽 화살표 키를 눌러 이전 프롬프트를 복구할 수 있습니다.

### Codex CLI에서는 되는데 Codex 앱에서는 기능이 동작하지 않습니다

Codex 앱과 Codex CLI는 동일한 기반 Codex 에이전트와 설정을 사용하지만, 시점에 따라 서로 다른 에이전트 버전에 의존할 수 있으며 일부 실험적 기능은 Codex CLI에 먼저 적용될 수 있습니다.

시스템에 설치된 Codex CLI 버전을 확인하려면 다음을 실행하세요:
[code] 
    codex --version
[/code]

Codex 앱에 번들된 Codex 버전을 확인하려면 다음을 실행하세요:
[code] 
    /Applications/Codex.app/Contents/Resources/codex --version
[/code]

## 피드백 및 로그

메시지 composer에 `/`를 입력해 팀에 피드백을 보낼 수 있습니다. 기존 대화에서 피드백을 트리거하면 기존 세션을 피드백과 함께 공유할지 선택할 수 있습니다. 피드백을 제출하면 팀과 공유할 수 있는 세션 ID를 받게 됩니다.

이슈를 보고하려면:

  1. Codex GitHub 리포지토리에서 [existing issues](https://github.com/openai/codex/issues)를 확인합니다.
  2. [Open a new GitHub issue](https://github.com/openai/codex/issues/new?template=2-bug-report.yml&steps=Uploaded%20thread%3A%20019c0d37-d2b6-74c0-918f-0e64af9b6e14)



추가 로그는 다음 위치에서 확인할 수 있습니다:

  * 앱 로그(macOS): `~/Library/Logs/com.openai.codex/YYYY/MM/DD`
  * 세션 기록: `$CODEX_HOME/sessions` (기본값: `~/.codex/sessions`)
  * 아카이브된 세션: `$CODEX_HOME/archived_sessions` (기본값: `~/.codex/archived_sessions`)



로그를 공유하기 전에 민감한 정보가 포함되어 있지 않은지 먼저 확인하세요.

## 멈춤 상태와 복구 패턴

스레드가 멈춘 것처럼 보이면:

  1. Codex가 승인을 기다리는지 확인합니다.
  2. 터미널을 열고 `git status` 같은 기본 명령을 실행합니다.
  3. 더 작고 집중된 프롬프트로 새 스레드를 시작합니다.



실수로 worktree 생성을 취소해 프롬프트를 잃어버렸다면, composer에서 위쪽 화살표 키를 눌러 복구하세요.

## 터미널 문제

**터미널이 멈춘 것처럼 보입니다**

  1. 터미널 패널을 닫습니다.
  2. `Cmd`+`J`로 다시 엽니다.
  3. `pwd` 또는 `git status` 같은 기본 명령을 다시 실행합니다.



명령 동작이 예상과 다르다면 먼저 터미널에서 현재 디렉터리와 브랜치를 확인하세요.

계속 멈춰 있다면 활성 Codex 스레드가 모두 완료될 때까지 기다린 뒤 앱을 재시작하세요.

**폰트가 올바르게 렌더링되지 않습니다**

Codex는 review pane, 통합 터미널, 그리고 앱 내부에 표시되는 기타 코드에 동일한 폰트를 사용합니다. [Settings](codex://settings) 패널의 **Code font**에서 폰트를 설정할 수 있습니다.
