---
title: '커스터마이제이션'
description: '커스터마이제이션은 Codex를 팀의 작업 방식대로 작동하게 만드는 방법입니다.'
---

Source URL: https://developers.openai.com/codex/concepts/customization

# 커스터마이제이션

커스터마이제이션은 Codex를 팀의 작업 방식대로 작동하게 만드는 방법입니다.

Codex에서는 다음이 함께 작동하는 여러 계층에서 커스터마이징이 이루어집니다:

- **지속적인 지침을 위한 프로젝트 안내(`AGENTS.md`)**
- **재사용 가능한 워크플로와 도메인 전문성을 위한 스킬**
- **외부 도구와 공유 시스템 접근을 위한 [MCP](https://developers.openai.com/codex/mcp)**
- **특화된 하위 에이전트에 작업을 위임하는 [멀티 에이전트](https://developers.openai.com/codex/concepts/multi-agents)**

이들은 경쟁 관계가 아니라 상호 보완 관계입니다. `AGENTS.md`는 행동을 형성하고, 스킬은 반복 가능한 프로세스를 패키징하며, [MCP](https://developers.openai.com/codex/mcp)는 Codex를 로컬 작업 영역 외부 시스템과 연결합니다.

## AGENTS 안내

`AGENTS.md`는 Codex에게 리포지토리와 함께 따라다니며 작업 시작 전에 적용되는 지속적인 프로젝트 지침을 제공합니다. 간결하게 유지하세요.

리포지토리에서 Codex가 항상 따라야 할 규칙(예: 다음)을 여기에 작성하세요:

- 빌드 및 테스트 명령
- 리뷰 기대치
- 리포지토리 특정 관습
- 디렉터리별 지침

에이전트가 코드를 잘못 추측한다면 `AGENTS.md`에서 바로잡고, 수정을 지속시키기 위해 에이전트에게 `AGENTS.md`를 업데이트하라고 요청하세요. 피드백 루프로 다루세요.

**`AGENTS.md` 업데이트:** 중요 지침만 먼저 작성하세요. 반복되는 리뷰 피드백을 공식화하고, 적용 범위가 좁은 지침은 가장 가까운 디렉터리에 두며, 수정할 때 에이전트에게 `AGENTS.md` 업데이트를 요청해 향후 세션이 수정사항을 상속하도록 하세요.

### `AGENTS.md`를 언제 업데이트해야 하나요

- **반복 실수**: 에이전트가 같은 실수를 반복할 경우 규칙을 추가하세요.
- **과도한 탐색**: 적절한 파일을 찾지만 너무 많은 문서를 읽는다면, 어떤 디렉터리/파일을 우선하면 되는지 안내하세요.
- **반복되는 PR 피드백**: 같은 피드백을 여러 번 남긴다면 문서화하세요.
- **GitHub에서**: PR 코멘트에 `@codex`를 태그하고 요청(ex. `@codex add this to AGENTS.md`)하여 클라우드 작업으로 업데이트를 위임하세요.
- **드리프트 검사 자동화**: [자동화](https://developers.openai.com/codex/app/automations)를 사용해(예: 매일) 지침 누락을 검색하고 `AGENTS.md`에 무엇을 추가할지 제안하세요.

`AGENTS.md`를 사전 커밋 훅, 린터, 타입 검사기 같은 인프라와 함께 사용하면 규칙을 사전에 적용해 반복 실수를 줄일 수 있습니다.

Codex는 여러 위치에서 지침을 불러올 수 있습니다: Codex 홈 디렉터리의 글로벌 파일(개인 개발자용)과 팀이 체킹하는 리포지토리별 파일이 있습니다. 워킹 디렉터리에 더 가까운 파일이 우선합니다.
전역 파일은 Codex와의 커뮤니케이션(예: 리뷰 스타일, 자세함, 기본값)을 제어하고, 리포지토리 파일은 팀과 코드베이스 규칙에 집중하세요.

```tsx
<FileTree
  class="mt-4"
  tree={[
    {
      name: "~/.codex/",
      open: true,
      children: [
        { name: "AGENTS.md", comment: "Global (for you as a developer)" },
      ],
    },
    {
      name: "repo-root/",
      open: true,
      children: [
        { name: "AGENTS.md", comment: "Repo-specific (for your team)" },
      ],
    },
  ]}
/>
```

[AGENTS.md로 사용자 지침 만들기](https://developers.openai.com/codex/guides/agents-md)

## 스킬

스킬은 Codex에게 반복 가능한 워크플로를 위한 재사용 가능한 역량을 제공합니다.
스킬은 리치한 지침, 스크립트, 참고 자료를 지원하면서도 여러 작업에서 재사용할 수 있기 때문에 반복 워크플로에 가장 적합한 경우가 많습니다.
스킬은 메타데이터(적어도)를 에이전트가 로드하고 볼 수 있으므로 Codex가 암묵적으로 발견하고 선택할 수 있습니다. 이렇게 하면 초기 컨텍스트를 과도하게 채우지 않고도 리치한 워크플로를 유지할 수 있습니다.

스킬은 일반적으로 `SKILL.md` 파일과 선택적인 스크립트, 참고 자료, 자산으로 구성됩니다.

```tsx
<FileTree
  class="mt-4"
  tree={[
    {
      name: "my-skill/",
      open: true,
      children: [
        { name: "SKILL.md", comment: "Required: instructions + metadata" },
        { name: "scripts/", comment: "Optional: executable code" },
        { name: "references/", comment: "Optional: documentation" },
        { name: "assets/", comment: "Optional: templates, resources" },
      ],
    },
  ]}
/>
```

스킬 디렉터리는 워크플로 일부로 Codex가 실행하는 CLI 스크립트를 포함하는 `scripts/` 폴더를 포함할 수 있습니다(예: 시드 데이터 생성 또는 유효성 검사 실행). 워크플로가 이슈 트래커, 디자인 도구, 문서 서버 같은 외부 시스템을 필요로 한다면 스킬을 [MCP](https://developers.openai.com/codex/mcp)와 결합하세요.

예시 `SKILL.md`:

```md
---
name: commit
description: Stage and commit changes in semantic groups. Use when the user wants to commit, organize commits, or clean up a branch before pushing.
---

1. Do not run `git add .`. Stage files in logical groups by purpose.
2. Group into separate commits: feat → test → docs → refactor → chore.
3. Write concise commit messages that match the change scope.
4. Keep each commit focused and reviewable.
```

다음 용도로 스킬을 사용하세요:

- 반복 가능한 워크플로(릴리스 단계, 리뷰 루틴, 문서 업데이트)
- 팀별 전문 지식
- 예시, 참고 자료 또는 헬퍼 스크립트가 필요한 절차

스킬은 전역(개인 사용자 디렉터리, 개인 개발자용) 또는 리포지토리별(`.agents/skills`에 커밋된 팀용)로 존재할 수 있습니다. 워크플로가 특정 프로젝트에 적용된다면 리포지토리 스킬을 `.agents/skills`에 두고, 모든 리포지토리에서 쓰고 싶은 스킬은 사용자 디렉터리에 두세요.

| Layer  | Global                 | Repo                                    |
| :----- | :--------------------- | :-------------------------------------- |
| AGENTS | `~/.codex/AGENTS.md`   | `AGENTS.md` in repo root or nested dirs |
| Skills | `$HOME/.agents/skills` | `.agents/skills` in repo                |

Codex는 스킬에 대해 점진적 공개 방식을 사용합니다:

- 발견을 위해 메타데이터(`name`, `description`)부터 시작합니다
- 스킬이 선택되었을 때만 `SKILL.md`를 로드합니다
- 참고 자료를 읽거나 스크립트를 실행할 때만 불러옵니다

스킬은 명시적으로 호출할 수도 있고, 작업이 스킬 설명에 맞을 때 Codex가 암묵적으로 선택할 수도 있습니다. 명확한 스킬 설명은 트리거 신뢰도를 높입니다.

[Agent Skills](https://developers.openai.com/codex/skills)

## MCP

MCP(Model Context Protocol)는 Codex를 외부 도구 및 컨텍스트 제공자에 연결하는 표준 방법입니다.
Figma, Linear, Jira, GitHub 또는 팀이 의존하는 내부 지식 서비스 같은 원격 호스팅 시스템에 특히 유용합니다.

Codex가 로컬 리포지토리 외부에 있는 기능(예: 이슈 트래커, 디자인 도구, 브라우저, 공유 문서 시스템)이 필요할 때 MCP를 사용하세요.

유용한 사고 모델:

- **Host**: Codex
- **Client**: Codex 내부의 MCP 연결
- **Server**: 외부 도구나 컨텍스트 제공자

MCP 서버는 다음을 노출할 수 있습니다:

- **Tools** (액션)
- **Resources** (읽을 수 있는 데이터)
- **Prompts** (재사용 가능한 프롬프트 템플릿)

이 분리는 신뢰와 기능 경계를 이해하는 데 도움이 됩니다. 일부 서버는 주로 컨텍스트를 제공하고, 다른 서버는 강력한 액션을 노출합니다.

실무에서는 MCP가 종종 스킬과 함께 가장 유용합니다:

- 스킬은 워크플로를 정의하고 사용할 MCP 도구를 지정합니다

[Model Context Protocol](https://developers.openai.com/codex/mcp)

## 멀티 에이전트

역할이 다른 다양한 에이전트를 생성하고 도구를 다르게 사용하도록 지시할 수 있습니다. 예를 들어 특정 테스트 명령과 구성을 실행하는 에이전트가 있는가 하면, 다른 에이전트는 프로덕션 로그를 가져오는 MCP 서버를 사용할 수 있습니다. 각 하위 에이전트는 집중된 상태를 유지하고 자신의 작업에 적합한 도구를 사용합니다.

[멀티 에이전트 개념](https://developers.openai.com/codex/concepts/multi-agents)

## 스킬 + MCP 함께 쓰기

스킬과 MCP를 결합하면 모든 것이 연결됩니다: 스킬은 반복 가능한 워크플로를 정의하고, MCP는 그것을 외부 도구와 시스템에 연결합니다.
스킬이 MCP에 의존한다면 `agents/openai.yaml`에 해당 의존성을 선언하여 Codex가 자동으로 설치하고 연결할 수 있게 하세요([Agent Skills](https://developers.openai.com/codex/skills) 참조).

## 다음 단계

다음 순서로 구축하세요:

1. [AGENTS.md로 사용자 지침 만들기](https://developers.openai.com/codex/guides/agents-md) – Codex가 리포지토리 관습을 따르도록 하고, 해당 규칙을 적용하기 위해 pre-commit 훅과 린터를 추가하세요.
2. [스킬](https://developers.openai.com/codex/skills) – 같은 대화를 다시 하지 않도록 합니다. 스킬은 CLI 스크립트를 포함한 `scripts/` 디렉터리를 가질 수 있고, 외부 시스템을 위해 [MCP](https://developers.openai.com/codex/mcp)와 결합할 수도 있습니다.
3. [MCP](https://developers.openai.com/codex/mcp) – 워크플로에 Linear, JIRA, 문서 서버, 디자인 도구 같은 외부 시스템이 필요할 때 사용하세요.
4. [멀티 에이전트](https://developers.openai.com/codex/multi-agent) – 소음이 많거나 전문화된 작업을 하위 에이전트에 위임할 준비가 되었을 때 사용하세요.
