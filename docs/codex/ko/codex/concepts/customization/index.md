# 맞춤화

Source URL: https://developers.openai.com/codex/concepts/customization

맞춤화는 Codex가 팀의 작업 방식에 맞춰 작동하도록 만드는 방법입니다.

Codex에서 맞춤화는 함께 작동하는 몇 가지 계층에서 나옵니다:

  * **프로젝트 가이드(`AGENTS.md`)**: 지속적인 지침
  * **스킬**: 재사용 가능한 워크플로와 도메인 전문성
  * **[MCP](https://developers.openai.com/codex/mcp)**: 외부 도구와 공유 시스템에 대한 접근
  * **[멀티 에이전트](https://developers.openai.com/codex/concepts/multi-agents)**: 특화된 하위 에이전트에 업무 위임

이 요소들은 경쟁하는 것이 아니라 서로를 보완합니다. `AGENTS.md`는 행동을 형성하고, 스킬은 반복 가능한 프로세스를 패키징하며, [MCP](https://developers.openai.com/codex/mcp)는 Codex를 로컬 워크스페이스 밖의 시스템과 연결합니다.

## AGENTS Guidance

`AGENTS.md`는 에이전트가 작업을 시작하기 전에 적용되는, 저장소에 함께 보관되는 지속적인 프로젝트 지침을 Codex에 제공합니다. 간결하게 유지하세요.

다음과 같은, 저장소에서 매번 Codex가 따라야 하는 규칙을 여기에 두세요:

  * 빌드 및 테스트 명령
  * 리뷰 기대치
  * 저장소별 규약
  * 디렉터리별 지침

에이전트가 코드베이스에 대해 잘못된 가정을 할 때는 `AGENTS.md`에서 이를 바로잡은 뒤 에이전트에 `AGENTS.md`를 업데이트하도록 요청하면 수정 사항이 지속됩니다. 피드백 루프로 활용하세요.

**Updating`AGENTS.md`:** 중요한 지침부터 시작하세요. 반복되는 리뷰 피드백을 규범화하고, 지침이 적용되는 가장 가까운 디렉터리에 배치하며, 무언가를 바로잡을 때 에이전트에 `AGENTS.md`를 업데이트하라고 알려 미래 세션이 수정 사항을 물려받도록 하세요.

### When to update `AGENTS.md`

  * **반복된 실수**: 에이전트가 같은 실수를 반복한다면 규칙을 추가하세요.
  * **과도한 읽기**: 올바른 파일을 찾지만 문서를 너무 많이 읽는다면 어떤 디렉터리/파일을 우선시해야 하는지 라우팅 지침을 추가하세요.
  * **반복되는 PR 피드백**: 같은 피드백을 두 번 이상 남긴다면 규범으로 만드세요.
  * **GitHub에서**: PR 댓글에서 `@codex`를 태그하고 요청(예: `@codex add this to AGENTS.md`)하면 업데이트를 클라우드 태스크에 위임할 수 있습니다.
  * **드리프트 검사 자동화**: [automations](https://developers.openai.com/codex/app/automations)를 사용해 정기적으로(예: 매일) 지침 격차를 찾아 `AGENTS.md`에 추가할 내용을 제안하세요.

`AGENTS.md`를 해당 규칙을 강제하는 인프라와 연결하세요. 프리커밋 훅, 린터, 타입 체커가 문제를 사전에 잡아 반복 실수를 예방하도록 시스템을 강화합니다.

Codex는 여러 위치에서 지침을 불러올 수 있습니다. 개발자 개인용 Codex 홈 디렉터리의 글로벌 파일과 팀이 체크인할 수 있는 저장소별 파일이 있으며, 작업 디렉터리에 가까울수록 우선순위가 높습니다. 글로벌 파일로는 Codex가 여러분과 소통하는 방식을(예: 리뷰 스타일, 장황함, 기본값) 정의하고, 저장소 파일은 팀과 코드베이스 규칙에 집중하세요.

  * ~/.codex/ 

    * AGENTS.md  Global (for you as a developer) 

  * repo-root/ 

    * AGENTS.md  Repo-specific (for your team) 

[AGENTS.md와 함께하는 사용자 지정 지침](https://developers.openai.com/codex/guides/agents-md)

## 스킬

스킬은 반복 가능한 워크플로를 위한 재사용 가능한 능력을 Codex에 제공합니다. 스킬은 더 풍부한 지침, 스크립트, 레퍼런스를 지원하면서도 작업 간 재사용이 가능하기 때문에 반복 워크플로에 가장 적합한 경우가 많습니다. 스킬은 에이전트에 로드되고(적어도 메타데이터는) 표시되므로 Codex가 암묵적으로 발견하고 선택할 수 있습니다. 이렇게 하면 풍부한 워크플로를 앞부분에서 컨텍스트를 부풀리지 않고도 사용할 수 있습니다.

스킬은 일반적으로 `SKILL.md` 파일과 선택적인 스크립트, 레퍼런스, 에셋으로 구성됩니다.

  * my-skill/ 

    * SKILL.md  필수: 지침 + 메타데이터 

    * scripts/  선택: 실행 가능한 코드 

    * references/  선택: 문서 

    * assets/  선택: 템플릿, 리소스

스킬 디렉터리는 워크플로우의 일부로 Codex가 호출하는 CLI 스크립트를 담은 `scripts/` 폴더를 포함할 수 있습니다(예: 시드 데이터를 준비하거나 검증을 실행). 워크플로우에 외부 시스템(이슈 트래커, 디자인 도구, 문서 서버 등)이 필요하면 해당 스킬을 [MCP](https://developers.openai.com/codex/mcp)와 함께 사용하세요.

예시 `SKILL.md`:
[code] 
    ---
    name: commit
    description: Stage and commit changes in semantic groups. Use when the user wants to commit, organize commits, or clean up a branch before pushing.
    ---
    
    1. Do not run `git add .`. Stage files in logical groups by purpose.
    2. Group into separate commits: feat → test → docs → refactor → chore.
    3. Write concise commit messages that match the change scope.
    4. Keep each commit focused and reviewable.
[/code]

다음과 같은 경우 스킬을 사용하세요:

  * 반복 가능한 워크플로우(릴리스 단계, 리뷰 루틴, 문서 업데이트)
  * 팀 특화 전문 지식
  * 예제, 참고 자료, 보조 스크립트가 필요한 절차

스킬은 글로벌(개발자인 사용자의 홈 디렉터리) 또는 리포지토리 전용(`.agents/skills`에 체크인되어 팀이 공유)일 수 있습니다. 특정 프로젝트에만 적용되는 워크플로우라면 `.agents/skills`에 저장하고, 모든 리포에서 쓰고 싶다면 사용자 디렉터리에 두세요.

레이어| 글로벌| 리포
---|---|---
AGENTS| `~/.codex/AGENTS.md`| 리포지토리 루트 또는 하위 디렉터리의 `AGENTS.md`
Skills| `$HOME/.agents/skills`| 리포지토리 안의 `.agents/skills`

Codex는 스킬에 대해 점진적 공개 방식을 사용합니다:

  * 검색을 위해 `name`, `description` 같은 메타데이터부터 살펴봅니다.
  * 스킬이 선택되었을 때만 `SKILL.md`를 읽습니다.
  * 필요할 때만 참고 자료를 열거나 스크립트를 실행합니다.

스킬은 명시적으로 호출할 수도 있고, 작업이 스킬 설명과 일치하면 Codex가 암묵적으로 선택할 수도 있습니다. 명확한 스킬 설명은 트리거 정확도를 높입니다.

[에이전트 스킬](https://developers.openai.com/codex/skills)

## MCP

MCP(Model Context Protocol)는 Codex를 외부 도구와 컨텍스트 제공자에 연결하는 표준 방식입니다. Figma, Linear, Jira, GitHub, 내부 지식 서비스처럼 원격으로 호스팅되는 시스템에 특히 유용합니다.

Codex가 이슈 트래커, 디자인 도구, 브라우저, 공유 문서 시스템처럼 로컬 리포 바깥에 있는 기능을 써야 할 때 MCP를 사용하세요.

유용한 사고 모델:

  * **호스트** : Codex
  * **클라이언트** : Codex 내부의 MCP 연결
  * **서버** : 외부 도구 또는 컨텍스트 제공자

MCP 서버가 노출할 수 있는 것:

  * **Tools** (액션)
  * **Resources** (읽기 가능한 데이터)
  * **Prompts** (재사용 가능한 프롬프트 템플릿)

이 분리는 신뢰 및 기능 경계를 파악하는 데 도움이 됩니다. 어떤 서버는 주로 컨텍스트를 제공하고, 다른 서버는 강력한 액션을 노출합니다.

실제로 MCP는 스킬과 함께 사용할 때 가장 유용한 경우가 많습니다:

  * 스킬이 워크플로우를 정의하고 사용할 MCP 도구를 지정합니다.

[Model Context Protocol](https://developers.openai.com/codex/mcp)

## 멀티 에이전트

서로 다른 역할을 가진 여러 에이전트를 만들고 각자 다른 방식으로 도구를 사용하도록 지시할 수 있습니다. 예를 들어 한 에이전트는 특정 테스트 명령과 구성을 실행하고, 다른 에이전트는 디버깅을 위해 운영 로그를 가져오는 MCP 서버를 연결할 수 있습니다. 각 하위 에이전트는 집중된 상태를 유지하며 자신의 작업에 맞는 도구를 사용합니다.

[멀티 에이전트 개념](https://developers.openai.com/codex/concepts/multi-agents)

## 스킬 + MCP 결합

스킬과 MCP를 함께 쓰면 모든 퍼즐 조각이 맞춰집니다. 스킬은 반복 가능한 워크플로우를 정의하고, MCP는 이를 외부 도구와 시스템에 연결합니다. 스킬이 MCP에 의존한다면 `agents/openai.yaml`에 해당 의존성을 선언해 Codex가 자동으로 설치하고 연결할 수 있게 하세요(참고: [Agent Skills](https://developers.openai.com/codex/skills)).

## 다음 단계

다음 순서로 구축하세요:

  1. [AGENTS.md로 커스텀 지침 설정](https://developers.openai.com/codex/guides/agents-md)을 통해 Codex가 리포 규칙을 따르도록 합니다. 그 규칙을 강제하기 위해 pre-commit 훅과 린터를 추가하세요.

2. [Skills](https://developers.openai.com/codex/skills)를 사용하면 같은 대화를 두 번 할 필요가 없습니다. Skills에는 CLI 스크립트를 담는 `scripts/` 디렉터리가 포함될 수 있고 외부 시스템을 위해 [MCP](https://developers.openai.com/codex/mcp)와 연동할 수도 있습니다.
  3. [MCP](https://developers.openai.com/codex/mcp)는 워크플로에 외부 시스템(Linear, JIRA, 문서 서버, 디자인 도구)이 필요할 때 사용합니다.
  4. [Multi-agents](https://developers.openai.com/codex/multi-agent)는 소음이 많거나 전문적인 작업을 하위 에이전트에게 위임할 준비가 되었을 때 사용합니다.
