---
title: Codex 앱 기능
description: Codex 앱은 Codex 스레드를 병렬로 작업할 수 있도록 설계된 집중형 데스크톱 환경으로, 기본 제공 worktree 지원, 자동화, Git 기능을 제공합니다.
sidebar:
  order: 2
---

# Codex 앱 기능

원문 URL: https://developers.openai.com/codex/app/features

Codex 앱은 Codex 스레드를 병렬로 작업할 수 있도록 설계된 집중형 데스크톱 환경으로, 기본 제공 worktree 지원, 자동화, Git 기능을 제공합니다.

* * *

## 프로젝트 전반에서 멀티태스킹

하나의 Codex 앱 창에서 여러 프로젝트의 작업을 실행할 수 있습니다. 코드베이스마다 프로젝트를 추가하고 필요에 따라 전환하세요.

[Codex CLI](https://developers.openai.com/codex/cli)를 사용해봤다면, 프로젝트는 특정 디렉터리에서 세션을 시작하는 것과 비슷합니다.

하나의 리포지토리에서 둘 이상의 앱이나 패키지를 작업한다면, 서로 다른 프로젝트를 앱 내에서 별도 프로젝트로 나눠 [sandbox](https://developers.openai.com/codex/security)가 해당 프로젝트 파일만 포함하도록 하세요.

## Skills 지원

Codex 앱은 CLI 및 IDE Extension과 동일한 [agent skills](https://developers.openai.com/codex/skills)를 지원합니다. 또한 사이드바의 Skills를 클릭하면 여러 프로젝트 전반에서 팀이 만든 새로운 스킬을 확인하고 탐색할 수 있습니다.

## Automations

스킬을 [automations](https://developers.openai.com/codex/app/automations)와 결합해 텔레메트리 오류 평가 및 수정 제출, 최근 코드베이스 변경 보고서 생성 같은 반복 작업을 수행할 수 있습니다.

## 모드

각 스레드는 선택한 모드에서 실행됩니다. 스레드를 시작할 때 다음을 선택할 수 있습니다.

  * **Local** : 현재 프로젝트 디렉터리에서 직접 작업합니다.
  * **Worktree** : Git worktree에서 변경 사항을 격리합니다. [자세히 보기](https://developers.openai.com/codex/app/worktrees).
  * **Cloud** : 구성된 클라우드 환경에서 원격으로 실행합니다.



**Local** 및 **Worktree** 스레드는 모두 사용자 컴퓨터에서 실행됩니다.

전체 용어집과 개념은 [concepts section](https://developers.openai.com/codex/prompting)에서 확인하세요.

## 내장 Git 도구

Codex 앱은 일반적인 Git 기능을 앱 내에서 직접 제공합니다.

diff 패널은 로컬 프로젝트 또는 worktree checkout에서의 변경 사항을 Git diff로 보여줍니다. 또한 Codex가 처리할 수 있도록 인라인 코멘트를 추가하고, 특정 청크 또는 전체 파일을 스테이징하거나 되돌릴 수 있습니다.

로컬 및 worktree 작업에 대해 Codex 앱 안에서 바로 커밋, 푸시, 풀 리퀘스트 생성도 가능합니다.

더 고급 Git 작업은 [integrated terminal](https://developers.openai.com/codex/app/features#integrated-terminal)을 사용하세요.

## Worktree 지원

새 스레드를 만들 때 **Local** 또는 **Worktree**를 선택합니다. **Local**은 프로젝트 내부에서 직접 작업합니다. **Worktree**는 새 [Git worktree](https://git-scm.com/docs/git-worktree)를 생성해 변경 사항이 기존 프로젝트와 분리되도록 합니다.

현재 작업을 건드리지 않고 새 아이디어를 시도하거나, 같은 프로젝트에서 Codex가 독립적인 작업을 나란히 실행하게 하고 싶다면 **Worktree**를 사용하세요.

자동화는 Git 리포지토리의 경우 전용 백그라운드 worktree에서 실행되고, 버전 관리가 없는 프로젝트에서는 프로젝트 디렉터리에서 직접 실행됩니다.

[Codex 앱에서 worktree를 사용하는 방법 자세히 보기](https://developers.openai.com/codex/app/worktrees)

## 통합 터미널

각 스레드에는 현재 프로젝트 또는 worktree 범위로 제한된 내장 터미널이 포함됩니다. 앱 오른쪽 상단의 터미널 아이콘이나 `Cmd`+`J`로 토글할 수 있습니다.

앱을 벗어나지 않고 터미널에서 변경 사항 검증, 스크립트 실행, Git 작업을 수행하세요.

일반적인 작업 예시는 다음과 같습니다.

  * `git status`
  * `git pull --rebase`
  * `pnpm test` 또는 `npm test`
  * `pnpm run lint` 또는 유사한 프로젝트 명령



정기적으로 실행하는 작업이 있다면 [local environment](https://developers.openai.com/codex/app/local-environments) 안에 **action**을 정의해 Codex 앱 창 상단에 바로가기 버튼을 추가할 수 있습니다.

`Cmd`+`K`는 Codex 앱에서 command palette를 열며, 터미널을 지우지는 않습니다. 터미널을 지우려면 `Ctrl`+`L`을 사용하세요.

## 음성 받아쓰기

음성으로 Codex에 프롬프트를 입력할 수 있습니다. composer가 보이는 상태에서 `Ctrl`+`M`을 누른 채 말하기를 시작하면 음성이 전사됩니다. 전사된 프롬프트를 편집하거나 전송해 Codex가 작업을 시작하게 할 수 있습니다.

## 플로팅 팝아웃 창

활성 대화 스레드를 별도 창으로 분리해 현재 작업 중인 위치로 옮길 수 있습니다. 프런트엔드 작업에 특히 유용하며, 브라우저, 에디터, 디자인 미리보기 근처에 스레드를 두고 빠르게 반복 작업할 수 있습니다.

팝아웃 창을 항상 위에 표시하도록 전환해 워크플로 전반에서 계속 보이게 할 수도 있습니다.

* * *

## IDE Extension과 동기화

에디터에 [Codex IDE Extension](https://developers.openai.com/codex/ide)이 설치되어 있다면, Codex 앱과 IDE Extension은 둘 다 같은 프로젝트에 있을 때 자동으로 동기화됩니다.

동기화되면 Codex 앱 composer에 **IDE context** 옵션이 표시됩니다. “Auto context”를 활성화하면 Codex 앱이 현재 보고 있는 파일을 추적하므로, 이를 간접적으로 참조할 수 있습니다(예: “What’s this file about?”). IDE Extension에서 Codex 앱의 실행 중인 스레드를 볼 수 있고, 그 반대도 가능합니다.

앱이 컨텍스트를 포함하는지 확신이 없으면 해당 옵션을 끄고 같은 질문을 다시 해 결과를 비교하세요.

## 승인 및 샌드박싱

승인 및 sandbox 설정은 Codex의 동작을 제한합니다.

  * Approvals는 명령 실행 전에 Codex가 권한 확인을 위해 언제 멈출지 결정합니다.
  * sandbox는 Codex가 사용할 수 있는 디렉터리와 네트워크 접근 범위를 제어합니다.



“approve once” 또는 “approve for this session” 같은 프롬프트가 표시되면, 도구 실행에 대해 서로 다른 범위의 권한을 부여하는 것입니다. 확신이 없다면 가장 좁은 옵션으로 승인하고 계속 반복하세요.

기본적으로 Codex는 현재 프로젝트 범위에서 작업합니다. 대부분의 경우 이것이 적절한 제약입니다.

작업에 둘 이상의 리포지토리 또는 디렉터리가 필요하다면, Codex가 프로젝트 루트 밖을 돌아다니도록 하기보다 별도 프로젝트를 열거나 worktree를 사용하는 편이 좋습니다.

Codex의 샌드박싱 처리 방식에 대한 자세한 내용은 [security documentation](https://developers.openai.com/codex/security)을 확인하세요.

## MCP 지원

Codex 앱, CLI, IDE Extension은 [Model Context Protocol (MCP)](https://developers.openai.com/codex/mcp) 설정을 공유합니다. 하나에서 MCP 서버를 이미 구성했다면 다른 곳에도 자동으로 적용됩니다. 새 서버를 구성하려면 앱 설정의 MCP 섹션을 열고, 권장 서버를 활성화하거나 구성에 새 서버를 추가하세요.

## 웹 검색

Codex에는 자체 제공 웹 검색 도구가 포함되어 있습니다. Codex IDE Extension의 로컬 작업에서는 기본적으로 웹 검색이 활성화되며, 웹 검색 캐시의 결과를 제공합니다. sandbox를 [full access](https://developers.openai.com/codex/security)로 구성하면 웹 검색 기본값이 라이브 결과로 바뀝니다. 웹 검색을 비활성화하거나 최신 데이터를 가져오는 라이브 결과로 전환하려면 [Config basics](https://developers.openai.com/codex/config-basic)를 참고하세요.

## 이미지 입력

프롬프트 composer에 이미지를 드래그 앤 드롭해 컨텍스트로 포함할 수 있습니다. 이미지를 드롭할 때 `Shift`를 누르고 있으면 해당 이미지를 컨텍스트에 추가합니다.

Codex에 시스템의 이미지를 보게 할 수도 있습니다. 작업 중인 앱의 스크린샷을 찍는 도구를 Codex에 제공하면, Codex가 자신이 수행한 작업을 검증할 수 있습니다.

## 알림

기본적으로 Codex 앱은 앱이 백그라운드에 있을 때 작업이 완료되거나 승인이 필요하면 알림을 보냅니다.

Codex 앱 설정에서, 알림을 전혀 보내지 않거나 앱이 포커스 상태여도 항상 보내도록 선택할 수 있습니다.

## 컴퓨터 절전 방지

작업 완료에 시간이 걸릴 수 있으므로, 앱 설정의 “Prevent sleep while running” 토글을 활성화해 Codex 앱이 컴퓨터 절전을 방지하도록 설정할 수 있습니다.

## 함께 보기

  * [Settings](https://developers.openai.com/codex/app/settings)
  * [Automations](https://developers.openai.com/codex/app/automations)
  * [Local environments](https://developers.openai.com/codex/app/local-environments)
  * [Worktrees](https://developers.openai.com/codex/app/worktrees)
