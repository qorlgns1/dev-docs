---
title: 'index'
description: 'git checkout <branch-name>'
---

**Quickstart 번역**

- ChatGPT Plus, Pro, Business, Edu, Enterprise 요금제에는 Codex가 포함되어 있습니다. ChatGPT 구독으로 Codex를 사용하면 최신 Codex 모델 및 기능에 접근할 수 있습니다.
- OpenAI API 키로 로그인하면 API 크레딧으로 Codex도 사용할 수 있습니다.
- 현재 기간 한정으로 **ChatGPT Free와 Go에서 Codex를 무료로 사용**하거나 Plus, Pro, Business, Enterprise 구독으로 **2배 Codex 속도 제한**을 활용할 수 있습니다.

**Setup**

- Codex 앱은 macOS(Apple Silicon)에서 사용할 수 있습니다.

1. Codex 앱 다운로드 및 설치

    - Codex 앱은 현재 macOS에서만 사용할 수 있습니다.

[Download for macOS](https://persistent.oaistatic.com/codex-app-prod/Codex.dmg)

      [Get notified for Windows and Linux](https://openai.com/form/codex-app/)

2. Codex 열기 및 로그인

   - Codex 앱을 다운로드하고 설치한 후 열어서 ChatGPT 계정 또는 OpenAI API 키로 로그인합니다.
   - OpenAI API 키로 로그인하면 [cloud threads](https://developers.openai.com/codex/prompting#threads)와 같은 일부 기능을 사용할 수 없을 수 있습니다.

3. 프로젝트 선택

   - Codex가 작업할 프로젝트 폴더를 선택합니다.
   - 이전에 Codex 앱, CLI, IDE 확장을 사용했다면 작업했던 이전 프로젝트가 표시됩니다.

4. 첫 메시지 보내기

   - 프로젝트를 선택한 후 Codex가 로컬에서 작업하도록 **Local**이 선택되어 있는지 확인하고 첫 메시지를 보냅니다.
   - 프로젝트나 컴퓨터 전반에 대해 Codex에게 무엇이든 물어볼 수 있습니다. 예시:
     - Tell me about this project
     - Build a classic Snake game in this repo.
     - Find and fix bugs in my codebase with minimal, high-confidence changes.
   - 추가 아이디어가 필요하면 [explore section](https://developers.openai.com/codex/explore)을 참고하세요.

[Learn more about the Codex app](https://developers.openai.com/codex/app)

**IDE용 Codex 확장 설치**

1. Codex 확장 설치

    - 사용 중인 에디터용으로 다운로드합니다:
      - [Download for Visual Studio Code](vscode:extension/openai.chatgpt)
      - [Download for Cursor](cursor:extension/openai.chatgpt)
      - [Download for Windsurf](windsurf:extension/openai.chatgpt)
      - [Download for Visual Studio Code Insiders](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt)

2. Codex 패널 열기

    - 설치 후 Codex 확장이 다른 확장과 함께 사이드바에 나타납니다. 축소된 섹션에 숨겨져 있을 수 있습니다. 원하는 경우 Codex 패널을 에디터 오른쪽으로 이동할 수 있습니다.

3. 로그인하고 첫 작업 시작

    - ChatGPT 계정 또는 API 키로 로그인하면 시작할 수 있습니다.
    - Codex는 기본적으로 Agent 모드로 시작하여 파일을 읽고, 명령을 실행하고, 프로젝트 디렉터리에 변경사항을 작성합니다.

- Tell me about this project
- Build a classic Snake game in this repo.
- Find and fix bugs in my codebase with minimal, high-confidence changes.

4. Git 체크포인트 사용

    - Codex는 코드베이스를 수정할 수 있으므로 작업 전후에 Git 체크포인트를 생성하여 필요 시 쉽게 변경 내용을 되돌릴 수 있도록 고려하세요.

[Learn more about the Codex IDE extension](https://developers.openai.com/codex/ide)

**Codex CLI**

- Codex CLI는 macOS, Windows, Linux에서 지원됩니다.

1. Codex CLI 설치

    - npm으로 설치:
      ```bash
      npm install -g @openai/codex
      ```
    - Homebrew로 설치:
      ```bash
      brew install codex
      ```

2. `codex` 실행 및 로그인

    - 터미널에서 `codex`를 실행하여 시작합니다. ChatGPT 계정 또는 API 키로 로그인하라는 메시지가 나타납니다.

3. 현재 디렉터리에서 작업 요청

    - 인증이 완료되면 현재 디렉터리에서 작업을 수행하도록 Codex에 요청할 수 있습니다.

- Tell me about this project
- Build a classic Snake game in this repo.
- Find and fix bugs in my codebase with minimal, high-confidence changes.

4. Git 체크포인트 사용

    - Codex가 코드베이스를 수정할 수 있으므로 작업 전후에 Git 체크포인트를 만들어 변경 내용을 쉽게 되돌릴 수 있도록 하세요.

[Learn more about the Codex CLI](https://developers.openai.com/codex/cli)

**클라우드에서 Codex 사용**

- [chatgpt.com/codex](https://chatgpt.com/codex)에서 Codex를 사용할 수 있습니다.

1. 브라우저에서 Codex 열기

    - [chatgpt.com/codex](https://chatgpt.com/codex)로 이동하세요. GitHub 풀 리퀘스트 댓글에서 `@codex`를 태그하면 작업을 Codex에 맡길 수도 있습니다(이 경우 ChatGPT에 로그인해야 합니다).

2. 환경 설정

    - 첫 작업을 시작하기 전에 Codex 환경을 설정합니다. [chatgpt.com/codex](https://chatgpt.com/codex/settings/environments)에서 환경 설정을 열고 GitHub 리포지토리를 연결하는 단계를 따르세요.

3. 작업 시작 및 진행 상황 모니터링

    - 환경 준비가 완료되면 [Codex 인터페이스](https://chatgpt.com/codex)에서 코딩 작업을 시작하세요. 로그를 보면서 실시간 진행 상황을 확인하거나 백그라운드에서 작업을 실행하도록 둘 수 있습니다.

- Tell me about this project
- Explain the top failure modes of my application's architecture.
- Find and fix bugs in my codebase with minimal, high-confidence changes.

4. 변경 사항 검토 및 Pull Request 생성

    - 작업이 완료되면 diff 보기에서 제안된 변경 사항을 검토합니다. 결과를 반복하거나 GitHub 리포지토리에 직접 Pull Request를 만들 수 있습니다.
    - Codex는 변경 사항 미리보기도 제공합니다. PR을 그대로 수락하거나 로컬에서 브랜치를 체크아웃하여 변경 사항을 테스트하세요:
      ```bash
      git fetch
      git checkout <branch-name>
      ```

[Learn more about Codex cloud](https://developers.openai.com/codex/cloud)

