---
title: 'Codex 앱'
description: 'Codex 앱은 병렬로 Codex 스레드 작업을 처리하기 위한 집중된 데스크톱 환경으로, 자동화, 워크트리 지원, Git 기능이 내장되어 있습니다.'
---

Source URL: https://developers.openai.com/codex/app

# Codex 앱

Codex 앱은 병렬로 Codex 스레드 작업을 처리하기 위한 집중된 데스크톱 환경으로, 자동화, 워크트리 지원, Git 기능이 내장되어 있습니다.

ChatGPT Plus, Pro, Business, Edu 및 Enterprise 플랜에는 Codex가 포함되어 있습니다. [포함된 내용](https://developers.openai.com/codex/pricing)을 자세히 확인하세요.

![Codex 앱 창에 프로젝트 사이드바, 활성 스레드, 리뷰 창이 표시된 화면](https://developers.openai.com/images/codex/app/app-screenshot-light.webp)

## 시작하기

Codex 앱은 macOS(Apple Silicon)에서 사용할 수 있습니다.

1. Codex 앱 다운로드 및 설치

    Codex 앱은 현재 macOS에서만 사용할 수 있습니다.

[macOS용 다운로드](https://persistent.oaistatic.com/codex-app-prod/Codex.dmg)

      [Windows 및 Linux 릴리스 알림 받기](https://openai.com/form/codex-app/)

2. Codex 열기 및 로그인

   Codex 앱을 다운로드하고 설치한 후 앱을 열고 ChatGPT 계정 또는 OpenAI API 키로 로그인하세요.

   OpenAI API 키로 로그인하면 [클라우드 스레드](https://developers.openai.com/codex/prompting#threads)와 같은 일부 기능을 사용할 수 없을 수 있습니다.

3. 프로젝트 선택

   Codex가 작업할 프로젝트 폴더를 선택하세요.

Codex 앱, CLI 또는 IDE 확장을 이전에 사용한 적이 있다면 이전에 작업한 프로젝트 목록이 표시됩니다.

4. 첫 번째 메시지 보내기

   프로젝트를 선택한 후 Codex가 로컬에서 작업하도록 **Local**이 선택되어 있는지 확인하고 첫 메시지를 Codex로 전송하세요.

   프로젝트 또는 컴퓨터 일반에 관해 Codex에게 무엇이든 물어볼 수 있습니다. 다음은 예시입니다:

- 이 프로젝트에 대해 알려줘
- 이 저장소에서 클래식 Snake 게임 만들어줘.
- 코드베이스에서 최소한의 자신감 높은 변경으로 버그를 찾아 고쳐줘.

   더 많은 영감이 필요하다면 [탐색 섹션](https://developers.openai.com/codex/explore)을 확인하세요.

---

## Codex 앱으로 작업하기

- [프로젝트 간 멀티태스킹](https://developers.openai.com/codex/app/features#multitask-across-projects)

여러 작업을 동시에 실행하고 빠르게 전환하세요.

- [내장 Git 툴](https://developers.openai.com/codex/app/features#built-in-git-tools)

앱을 벗어나지 않고도 diff 검토, 인라인 코멘트, 청크 스테이징/되돌림, 커밋을 수행하세요.

- [병렬 작업을 위한 워크트리](https://developers.openai.com/codex/app/worktrees)

내장 Git 워크트리 지원으로 여러 Codex 스레드의 변경 내용을 분리하세요.

- [스킬 지원](https://developers.openai.com/codex/app/features#skills-support)

Codex 에이전트에 추가 기능을 부여하고 앱, CLI, IDE 확장 간 스킬을 재사용하세요.

- [자동화](https://developers.openai.com/codex/app/automations)

스킬을 자동화와 결합해 반복 작업을 백그라운드에서 처리하세요. Codex는 발견 사항을 인박스에 추가하거나 보고할 내용이 없으면 실행을 자동으로 보관합니다.

- [내장 터미널](https://developers.openai.com/codex/app/features#integrated-terminal)

스레드별 터미널을 열어 변경 사항을 테스트하거나 개발 서버, 스크립트, 사용자 지정 명령을 실행하세요.

- [로컬 환경](https://developers.openai.com/codex/app/local-environments)

워크트리 설정 스크립트와 일반적인 프로젝트 작업을 정의해 손쉽게 접근하세요.

- [IDE 확장과 동기화](https://developers.openai.com/codex/app/features#sync-with-the-ide-extension)

auto context와 활성 스레드를 앱과 IDE 세션 간에 공유하세요.

- [MCP 지원](https://developers.openai.com/codex/app/features#mcp-support)

추가 서비스를 연결할 때 Codex 에이전트를 MCP에 연결하세요.

---

도움이 필요하신가요? [문제 해결 가이드](https://developers.openai.com/codex/app/troubleshooting)를 방문하세요.
