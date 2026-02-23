---
title: 'Codex 앱 기능'
description: "description: 'Codex 앱은 Codex 스레드를 병렬로 작업하기 위한 데스크톱 환경입니다,'"
---

**번역**

---
title: 'Codex 앱 기능'
description: 'Codex 앱은 Codex 스레드를 병렬로 작업하기 위한 데스크톱 환경입니다,'
---

Source URL: https://developers.openai.com/codex/app/features

# Codex 앱 기능

Codex 앱은 작업 트리 지원, 자동화 및 Git 기능이 내장된 Codex 스레드를 병렬로 처리하기 위한 집중된 데스크톱 경험입니다.

- [Codex 앱 소개](https://www.youtube.com/watch?v=HFM3se4lNiw)

---

## 프로젝트 간 멀티태스킹

Codex 앱 창 하나로 여러 프로젝트에서 작업을 실행하세요. 코드베이스마다 프로젝트를 추가하고 필요에 따라 전환합니다.

[Codex CLI](https://developers.openai.com/codex/cli)를 사용한 적이 있다면, 프로젝트는 특정 디렉터리에서 세션을 시작하는 것과 비슷합니다.

하나의 리포지토리에서 두 개 이상의 앱 또는 패키지로 작업한다면, 서로 다른 프로젝트를 별도의 앱 프로젝트로 분리하여 [샌드박스](https://developers.openai.com/codex/security)가 해당 프로젝트의 파일만 포함하도록 하세요.

![Codex 앱 사이드바에 여러 프로젝트와 메인 창의 스레드 표시](https://developers.openai.com/images/codex/app/multitask-light.webp)

## 스킬 지원

Codex 앱은 CLI 및 IDE 확장과 동일한 [에이전트 스킬](https://developers.openai.com/codex/skills)을 지원합니다. 사이드바의 스킬을 클릭하면 다양한 프로젝트에서 팀이 만든 새 스킬을 확인하고 탐색할 수도 있습니다.

![Codex 앱에서 사용 가능한 스킬을 보여주는 스킬 선택기](https://developers.openai.com/images/codex/app/skill-selector-light.webp)

## 자동화

[자동화](https://developers.openai.com/codex/app/automations)와 스킬을 결합하여 텔레메트리에서 오류 평가, 수정 제출 또는 최근 코드베이스 변경 사항 보고서 작성과 같은 정기 작업을 수행할 수 있습니다.

![일정 및 프롬프트 필드가 있는 자동화 생성 양식](https://developers.openai.com/images/codex/app/create-automation-light.webp)

## 모드

각 스레드는 선택한 모드에서 실행됩니다. 스레드를 시작할 때 다음 중 하나를 선택할 수 있습니다:

- **Local**: 현재 프로젝트 디렉터리에서 직접 작업합니다.
- **Worktree**: Git worktree에서 변경 사항을 격리합니다. [자세히 알아보기](https://developers.openai.com/codex/app/worktrees).
- **Cloud**: 구성된 클라우드 환경에서 원격으로 실행합니다.

**Local**과 **Worktree** 스레드는 모두 컴퓨터에서 실행됩니다.

전체 용어집과 개념은 [concepts 섹션](https://developers.openai.com/codex/prompting)을 탐색하세요.

![Local, Worktree, Cloud 모드 옵션이 있는 새 스레드 작성기](https://developers.openai.com/images/codex/app/modes-light.webp)

## 내장 Git 도구

Codex 앱은 일반적인 Git 기능을 앱 내에서 제공합니다.

디프 창에는 로컬 프로젝트 또는 worktree 체크아웃의 변경 사항 Git diff가 표시됩니다. Codex가 처리할 수 있도록 인라인 댓글을 추가하거나 특정 청크 또는 전체 파일을 스테이징하거나 되돌릴 수도 있습니다.

또한 Codex 앱 내에서 로컬 및 worktree 작업에 대해 커밋, 푸시 및 풀 리퀘스트 생성을 할 수 있습니다.

더 고급 Git 작업은 [통합 터미널](#integrated-terminal)을 사용하세요.

![커밋 메시지 필드가 있는 Git diff 및 커밋 패널](https://developers.openai.com/images/codex/app/git-commit-light.webp)

## Worktree 지원

새 스레드를 생성할 때 **Local** 또는 **Worktree**를 선택하세요. **Local**은 프로젝트 내에서 직접 작업하며, **Worktree**는 새로운 [Git worktree](https://git-scm.com/docs/git-worktree)를 만들어 변경 사항을 일반 프로젝트와 분리합니다.

현재 작업을 건드리지 않고 새 아이디어를 시도하거나 같은 프로젝트에서 Codex가 독립 작업을 나란히 실행하도록 하려면 **Worktree**를 사용하세요.

자동화는 Git 리포지토리의 전용 백그라운드 worktree에서 실행되며, 버전 관리되지 않은 프로젝트의 경우 프로젝트 디렉터리에서 직접 실행됩니다.

[Codex 앱에서 worktree 사용에 대해 자세히 알아보기.](https://developers.openai.com/codex/app/worktrees)

![브랜치 작업 및 worktree 세부 정보를 보여주는 worktree 스레드 보기](https://developers.openai.com/images/codex/app/worktree-light.webp)

## 통합 터미널

각 스레드에는 현재 프로젝트 또는 worktree에 범위가 지정된 내장 터미널이 포함됩니다. 앱 오른쪽 상단의 터미널 아이콘을 클릭하거나 <kbd>Cmd</kbd>+<kbd>J</kbd>를 눌러 토글하세요.

터미널을 사용하여 변경 사항을 검증하고 스크립트를 실행하며 앱을 떠나지 않고 Git 작업을 수행할 수 있습니다.

일반적인 작업에는 다음이 포함됩니다:

- `git status`
- `git pull --rebase`
- `pnpm test` 또는 `npm test`
- `pnpm run lint` 또는 유사한 프로젝트 명령

정기적으로 실행하는 작업이 있다면 [로컬 환경](https://developers.openai.com/codex/app/local-environments)에서 **액션**을 정의하여 Codex 앱 창 상단에 바로 가기 버튼을 추가할 수 있습니다.

참고: <kbd>Cmd</kbd>+<kbd>K</kbd>는 Codex 앱에서 명령 팔레트를 엽니다. 터미널을 지우지는 않으므로 터미널을 지우려면 <kbd>Ctrl</kbd>+<kbd>L</kbd>을 사용하세요.

![Codex 스레드 아래에 열린 통합 터미널 서랍](https://developers.openai.com/images/codex/app/integrated-terminal-light.webp)

## 음성 받아쓰기

음성으로 Codex에 프롬프트를 제공하세요. 작성기가 표시된 상태에서 <kbd>Ctrl</kbd>+<kbd>M</kbd>을 누르고 말하기를 시작하면 음성이 전사됩니다. 전사된 프롬프트를 수정하거나 전송하여 Codex가 작업을 시작하도록 하세요.

![전사된 프롬프트가 표시된 작성기 내 음성 받아쓰기 표시기](https://developers.openai.com/images/codex/app/voice-dictation-light.webp)

## 팝아웃 창

활성 대화 스레드를 별도 창으로 팝아웃하여 작업 중인 위치로 이동하세요. 프론트엔드 작업에 이상적이며, 브라우저나 편집기 또는 디자인 미리보기 근처에 스레드를 유지하면서 빠르게 반복할 수 있습니다.

팝아웃 창이 워크플로 전체에서 계속 보이도록 하려면 항상 위에 표시되게 전환할 수도 있습니다.

![라이트 모드의 팝아웃 창 미리보기](https://developers.openai.com/images/codex/app/popover-light.webp)

---

## IDE 확장과 동기화

편집기에 [Codex IDE Extension](https://developers.openai.com/codex/ide)이 설치되어 있다면, Codex 앱과 IDE 확장은 동일한 프로젝트 내에 있는 경우 자동으로 동기화됩니다.

동기화되면 Codex 앱 작성기에서 **IDE 컨텍스트** 옵션이 표시됩니다. “Auto context”를 활성화하면 Codex 앱이 보고 있는 파일을 추적하여 간접적으로 참조할 수 있습니다(예: “이 파일이 무엇에 관한 거야?”). 또한 IDE 확장 내에서 Codex 앱에서 실행 중인 스레드를, 반대로도 볼 수 있습니다.

앱에 컨텍스트가 포함되었는지 확실하지 않다면, 끄고 동일한 질문을 다시 하여 결과를 비교해 보세요.

## 승인 및 샌드박싱

승인 및 샌드박스 설정은 Codex 작업을 제한합니다.

- 승인은 명령을 실행하기 전에 Codex가 언제 권한 요청을 중지할지를 결정합니다.
- 샌드박스는 Codex가 사용할 수 있는 디렉터리 및 네트워크 액세스를 제어합니다.

“한 번만 승인” 또는 “이 세션에 대해 승인”과 같은 프롬프트가 나타나면 다양한 범위의 도구 실행 권한을 부여하는 것입니다. 확실하지 않다면 가장 좁은 옵션을 승인하고 계속 반복하세요.

기본적으로 Codex는 작업 범위를 현재 프로젝트로 제한합니다. 대부분의 경우 이 제약이 적절합니다.

작업이 둘 이상의 리포지토리나 디렉터리를 넘긴다면, Codex가 프로젝트 루트 밖을 돌아다니도록 요청하기보다는 별도 프로젝트를 열거나 worktree를 사용하는 것이 좋습니다.

Codex의 샌드박스 처리에 대한 자세한 내용은 [보안 문서](https://developers.openai.com/codex/security)를 확인하세요.

## MCP 지원

Codex 앱, CLI, IDE 확장은 [모델 컨텍스트 프로토콜(MCP)](https://developers.openai.com/codex/mcp) 설정을 공유합니다. 이미 한 곳에서 MCP 서버를 구성했다면 다른 곳에서도 자동으로 채택됩니다. 새로운 서버를 구성하려면 앱 설정의 MCP 섹션을 열고 추천 서버를 활성화하거나 새 서버를 구성에 추가하세요.

## 웹 검색

Codex에는 자체 웹 검색 도구가 포함되어 있습니다. Codex IDE 확장의 로컬 작업에서는 Codex가 기본적으로 웹 검색을 활성화하고 웹 검색 캐시에서 결과를 제공합니다. [전체 액세스](https://developers.openai.com/codex/security)로 샌드박스를 구성하면 웹 검색이 기본적으로 최신 결과를 가져옵니다. [설정 기본](https://developers.openai.com/codex/config-basic)을 확인하여 웹 검색을 비활성화하거나 최신 데이터를 가져오는 실시간 결과로 전환하세요.

## 이미지 입력

프롬프트 작성기에 이미지를 드래그 앤 드롭하여 컨텍스트로 포함할 수 있습니다. 이미지를 추가할 때 `Shift` 키를 누르고 있으면 이미지가 컨텍스트에 추가됩니다.

시스템에 있는 이미지를 Codex에게 불러오도록 요청할 수도 있습니다. Codex에게 작업 중인 앱의 스크린샷을 찍을 수 있는 도구를 제공하면 Codex가 수행 작업을 검증할 수 있습니다.

## 알림

기본적으로 Codex 앱은 작업이 완료되거나 승인이 필요할 때 앱이 백그라운드에 있을 경우 알림을 보냅니다.

Codex 앱 설정에서 항상 보내거나 앱이 포커스 되어 있을 때도 알림을 보내도록 설정하거나, 전혀 보내지 않도록 선택할 수 있습니다.

## 컴퓨터 깨어 있도록 유지

작업이 완료될 때까지 시간이 걸릴 수 있으므로 앱 설정에서 “실행 중에는 절전 모드 방지” 토글을 활성화하여 컴퓨터가 잠들지 않도록 할 수 있습니다.

## 참고

- [설정](https://developers.openai.com/codex/app/settings)
- [자동화](https://developers.openai.com/codex/app/automations)
- [로컬 환경](https://developers.openai.com/codex/app/local-environments)
- [Worktrees](https://developers.openai.com/codex/app/worktrees)

