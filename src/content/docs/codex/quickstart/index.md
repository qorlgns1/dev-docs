---
title: 빠른 시작
description: ChatGPT Plus, Pro, Business, Edu, 그리고 Enterprise 요금제에는 Codex가 포함됩니다. ChatGPT 구독과 함께 Codex를 사용하면 최신 Codex 모델과 기능에 접근할 수 있습니다.
sidebar:
  order: 3
---

# 빠른 시작

Source URL: https://developers.openai.com/codex/quickstart

ChatGPT Plus, Pro, Business, Edu, 그리고 Enterprise 요금제에는 Codex가 포함됩니다. ChatGPT 구독과 함께 Codex를 사용하면 최신 Codex 모델과 기능에 접근할 수 있습니다.

OpenAI API 키로 로그인하여 API 크레딧으로 Codex를 사용할 수도 있습니다.

한시적으로 **ChatGPT Free 및 Go에서 무료로 Codex를 사용해 보고**, Plus, Pro, Business, Enterprise 구독에서는 **2배 Codex 속도 제한**을 즐겨보세요.

## 설정

옵션을 선택하세요 

App추천 (macOS only)IDE 확장IDE에서 CodexCLICodex 터미널Cloud브라우저에서 Codex

Codex 앱은 macOS(Apple Silicon)에서 사용할 수 있습니다.

  1. Codex 앱을 다운로드하여 설치하세요

Codex 앱은 현재 macOS에서만 사용할 수 있습니다.

[ Download for macOS ](https://persistent.oaistatic.com/codex-app-prod/Codex.dmg)

[Get notified for Windows and Linux](https://openai.com/form/codex-app/)

  2. Codex를 열고 로그인하세요

Codex 앱을 다운로드하고 설치한 후 실행하여 ChatGPT 계정이나 OpenAI API 키로 로그인하세요.

OpenAI API 키로 로그인하면 [cloud threads](https://developers.openai.com/codex/prompting#threads)와 같은 일부 기능을 사용할 수 없을 수 있습니다.

  3. 프로젝트를 선택하세요

Codex가 작업할 프로젝트 폴더를 선택하세요.




이전에 Codex 앱, CLI 또는 IDE 확장을 사용한 적이 있다면 작업했던 과거 프로젝트가 표시됩니다.

  4. 첫 메시지를 보내세요

프로젝트를 선택한 후 Codex가 로컬에서 작업하도록 **Local**을 선택하고 Codex에 첫 메시지를 보내세요.

프로젝트나 컴퓨터 전반에 대해 Codex에 무엇이든 질문할 수 있습니다. 예시는 다음과 같습니다:

이 저장소에서 클래식 Snake 게임을 만들어줘.최소한의 고신뢰 변경으로 코드베이스의 버그를 찾아 고쳐줘.

더 많은 영감을 얻고 싶다면 [explore 섹션](https://developers.openai.com/codex/explore)을 확인하세요.

[ Learn more about the Codex app ](https://developers.openai.com/codex/app)




IDE용 Codex 확장을 설치하세요.

  1. Codex 확장을 설치하세요

에디터용 다운로드:

     * [Download for Visual Studio Code](vscode:extension/openai.chatgpt)
     * [Download for Cursor](cursor:extension/openai.chatgpt)
     * [Download for Windsurf](windsurf:extension/openai.chatgpt)
     * [Download for Visual Studio Code Insiders](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt)
  2. Codex 패널을 여세요

설치하면 Codex 확장이 다른 확장들과 함께 사이드바에 나타납니다. 접힌 섹션에 숨겨져 있을 수 있습니다. 원한다면 Codex 패널을 에디터 오른쪽으로 옮길 수 있습니다.

  3. 로그인하고 첫 작업을 시작하세요

시작하려면 ChatGPT 계정이나 API 키로 로그인하세요.

Codex는 기본적으로 Agent 모드에서 시작하며, 프로젝트 디렉터리에서 파일을 읽고, 명령을 실행하며, 변경 사항을 작성할 수 있습니다.

이 프로젝트에 대해 알려줘이 저장소에서 클래식 Snake 게임을 만들어줘최소한의 고신뢰 변경으로 코드베이스의 버그를 찾아 고쳐줘.

  4. Git 체크포인트를 사용하세요

Codex는 코드베이스를 변경할 수 있으므로 필요하면 쉽게 되돌릴 수 있도록 각 작업 전후로 Git 체크포인트를 생성하는 것을 고려하세요.

[ Learn more about the Codex IDE extension ](https://developers.openai.com/codex/ide)




Codex CLI는 macOS, Windows, Linux에서 지원됩니다.

  1. Codex CLI를 설치하세요

npm으로 설치:
```
npm install -g @openai/codex
```

Homebrew로 설치:
```
brew install codex
```

  2. `codex`를 실행하고 로그인하세요

터미널에서 `codex`를 실행하면 시작할 수 있습니다. ChatGPT 계정 또는 API 키로 로그인하라는 메시지가 표시됩니다.

  3. 현재 디렉터리에서 Codex가 작업하도록 요청하세요

인증이 완료되면 현재 디렉터리에서 Codex가 작업을 수행하도록 요청할 수 있습니다.

이 프로젝트에 대해 알려줘이 저장소에서 클래식 Snake 게임을 만들어줘최소한의 고신뢰 변경으로 코드베이스의 버그를 찾아 고쳐줘.

  4. Git 체크포인트를 사용하세요

Codex는 코드베이스를 수정할 수 있으므로, 필요 시 변경 사항을 쉽게 되돌릴 수 있도록 각 작업 전후에 Git 체크포인트를 생성하는 것을 고려하세요.




[ Codex CLI에 대해 더 알아보기 ](https://developers.openai.com/codex/cli)

[chatgpt.com/codex](https://chatgpt.com/codex)에서 클라우드용 Codex를 사용하세요.

  1. 브라우저에서 Codex 열기

[chatgpt.com/codex](https://chatgpt.com/codex)로 이동하세요. GitHub 풀 리퀘스트 댓글에서 `@codex`를 태그해 Codex에 작업을 위임할 수도 있습니다(ChatGPT 로그인 필요).

  2. 환경 설정

첫 작업을 시작하기 전에 Codex용 환경을 설정하세요. [chatgpt.com/codex](https://chatgpt.com/codex/settings/environments)에서 환경 설정을 열고 GitHub 리포지토리를 연결하는 단계를 따르세요.

  3. 작업 실행 및 진행 상황 모니터링

환경이 준비되면 [Codex 인터페이스](https://chatgpt.com/codex)에서 코딩 작업을 실행하세요. 로그를 보며 실시간으로 진행 상황을 모니터링하거나 백그라운드에서 작업을 실행할 수 있습니다.

이 프로젝트에 대해 알려 주세요애플리케이션 아키텍처의 주요 실패 모드를 설명해 주세요.최소한의, 높은 확신을 주는 변경으로 코드베이스의 버그를 찾아 수정해 주세요.

  4. 변경 사항 검토 및 풀 리퀘스트 생성

작업이 완료되면 diff 뷰에서 제안된 변경 사항을 검토하세요. 결과를 반복하거나 GitHub 리포지토리에서 바로 풀 리퀘스트를 생성할 수 있습니다.

Codex는 변경 사항 미리 보기 역시 제공합니다. 그대로 PR을 수락하거나 브랜치를 로컬에 체크아웃해 변경 사항을 테스트할 수 있습니다:
```
git fetch
         git checkout <branch-name>
```

[ Codex 클라우드에 대해 더 알아보기 ](https://developers.openai.com/codex/cloud)