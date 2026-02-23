---
title: '문제 해결'
description: '프로젝트가 Git 리포지토리 안에 있다면 리뷰 패널이 프로젝트의 Git 상태를 기반으로 변경 사항을 자동으로 표시하며 Codex가 수정하지 않은 변경도 포함됩니다.'
---

Source URL: https://developers.openai.com/codex/app/troubleshooting

# 문제 해결

## 자주 묻는 질문

### Codex가 수정하지 않은 파일이 사이드 패널에 표시됩니다

프로젝트가 Git 리포지토리 안에 있다면 리뷰 패널이 프로젝트의 Git 상태를 기반으로 변경 사항을 자동으로 표시하며 Codex가 수정하지 않은 변경도 포함됩니다.

리뷰 창에서 스테이지된 변경과 아직 스테이지되지 않은 변경을 전환하거나 현재 브랜치를 main과 비교할 수 있습니다.

최근 Codex 턴의 변경만 보고 싶다면 비교 창을 "마지막 턴 변경" 보기로 전환하세요.

[리뷰 창 사용 방법 더 알아보기](https://developers.openai.com/codex/app/review).

### 사이드바에서 프로젝트 제거

사이드바에서 프로젝트를 제거하려면 프로젝트 이름 위로 마우스를 가져간 후 점 세 개를 클릭하고 "제거"를 선택하세요. 복원하려면 **Threads** 옆의 **Add new project** 버튼을 사용하거나

<kbd>Cmd</kbd>+<kbd>O</kbd>를 사용하여 프로젝트를 다시 추가하세요.

### 보관된 스레드 찾기

보관된 스레드는 [Settings](codex://settings)에서 찾을 수 있습니다. 스레드를 다시 보관 해제하면 원래 사이드바 위치로 다시 나타납니다.

### 사이드바에 일부 스레드만 표시됩니다

사이드바는 프로젝트 상태에 따라 스레드를 필터링할 수 있습니다. 스레드가 누락되었다면 **Threads** 레이블 옆의 필터 아이콘을 클릭해 필터가 적용되어 있는지 확인하세요.

### 워크트리에서 코드가 실행되지 않습니다

워크트리는 다른 디렉터리에 생성되며 Git에 커밋된 파일만 상속합니다. 프로젝트의 종속성과 툴링을 관리하는 방식에 따라 워크트리에서 [로컬 환경](https://developers.openai.com/codex/app/local-environments)을 사용해 일부 설정 스크립트를 실행해야 할 수 있습니다. 또는 일반 로컬 프로젝트에서 변경 사항을 체크아웃할 수 있습니다. 자세한 내용은 [워크트리 문서](https://developers.openai.com/codex/app/worktrees)를 확인하세요.

### 앱이 팀원의 공유 로컬 환경을 인식하지 못합니다

로컬 환경 구성은 프로젝트 루트의 `.codex` 폴더 안에 있어야 합니다. 모노레포에서 여러 프로젝트를 다루는 경우 `.codex` 폴더가 있는 디렉터리에서 프로젝트를 열었는지 확인하세요.

### Codex가 Apple Music에 접근하길 요청합니다

작업에 따라 Codex가 파일 시스템을 탐색해야 할 수 있습니다. macOS의 특정 디렉터리(예: Music, Downloads, Desktop)는 사용자의 추가 승인 없이 접근할 수 없습니다. Codex가 홈 디렉터리를 읽어야 하면 macOS가 해당 폴더 접근을 승인하라고 요청합니다.

### 자동화가 많은 워크트리를 생성합니다

자주 실행되는 자동화는 시간이 지나면서 많은 워크트리를 만들 수 있습니다. 더 이상 필요 없는 자동화 실행을 보관하고, 워크트리를 유지하려는 목적이 아니라면 실행을 고정하지 마세요.

### 잘못된 대상 선택 후 프롬프트 복구

실수로 **Local**, **Worktree**, **Cloud** 중 잘못된 대상으로 스레드를 시작했다면 현재 실행을 취소한 뒤 컴포저에서 위쪽 화살표 키를 눌러 이전 프롬프트를 복구할 수 있습니다.

### Codex CLI에서는 작동하지만 Codex 앱에서는 작동하지 않는 기능

Codex 앱과 Codex CLI는 동일한 Codex 에이전트와 구성을 사용하지만, 시점에 따라 서로 다른 에이전트 버전을 사용할 수 있으며 일부 실험적 기능은 Codex CLI에서 먼저 제공될 수 있습니다.

시스템에 설치된 Codex CLI 버전을 확인하려면 다음을 실행하세요:

```bash
codex --version
```

Codex 앱에 번들된 Codex 버전을 확인하려면 다음을 실행하세요:

```bash
/Applications/Codex.app/Contents/Resources/codex --version
```

## 피드백 및 로그

메시지 입력창에 <kbd>/</kbd>를 입력하면 팀에 피드백을 보낼 수 있습니다. 기존 대화에서 피드백을 트리거한 경우 세션을 피드백과 함께 공유할지 선택할 수 있습니다. 피드백을 제출하면 팀과 공유할 수 있는 세션 ID가 수신됩니다.

문제를 신고하려면:

1. Codex GitHub 리포지토리에서 [기존 이슈](https://github.com/openai/codex/issues)를 찾습니다.
2. [새 GitHub 이슈 열기](https://github.com/openai/codex/issues/new?template=2-bug-report.yml&steps=Uploaded%20thread%3A%20019c0d37-d2b6-74c0-918f-0e64af9b6e14)

다음 위치에서 추가 로그를 확인할 수 있습니다:

- 앱 로그 (macOS): `~/Library/Logs/com.openai.codex/YYYY/MM/DD`
- 세션 기록: `$CODEX_HOME/sessions` (기본값: `~/.codex/sessions`)
- 보관된 세션: `$CODEX_HOME/archived_sessions` (기본값: `~/.codex/archived_sessions`)

로그를 공유할 경우 민감한 정보가 포함되어 있지 않은지 먼저 검토하세요.

## 멈춘 상태 및 복구 방법

스레드가 멈춘 것처럼 보인다면:

1. Codex가 승인을 기다리고 있는지 확인하세요.
2. 터미널을 열고 `git status`와 같은 기본 명령을 실행하세요.
3. 더 작고 집중된 프롬프트로 새 스레드를 시작하세요.

워크트리 생성을 실수로 취소하고 프롬프트를 잃었다면 컴포저에서 위쪽 화살표 키를 눌러 복구하세요.

## 터미널 문제

**터미널이 멈춘 것처럼 보일 때**

1. 터미널 패널을 닫습니다.
2. <kbd>Cmd</kbd>+<kbd>J</kbd>로 다시 엽니다.
3. `pwd` 또는 `git status`와 같은 기본 명령을 다시 실행합니다.

명령이 예상과 다르게 동작하면 터미널에서 현재 디렉터리와 브랜치를 먼저 확인하세요.

계속 멈춰 있다면 활성 Codex 스레드가 완료될 때까지 기다렸다가 앱을 재시작하세요.

**글꼴이 올바르게 렌더링되지 않을 때**

Codex는 리뷰 창, 통합 터미널 및 앱 내부에 표시되는 모든 코드에 동일한 글꼴을 사용합니다. [Settings](codex://settings) 창에서 **Code font**로 글꼴을 구성할 수 있습니다.
