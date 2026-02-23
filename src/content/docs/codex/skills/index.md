---
title: '에이전트 스킬'
description: 'Agent 스킬을 사용해 Codex를 작업 전용 기능으로 확장하세요. 스킬은 Codex가 워크플로를 안정적으로 따르도록 설명, 리소스, 선택적 스크립트를 꾸린 단위입니다. 스킬은 팀 간이나 커뮤니티와 공유할 수 있으며, 오픈 에이전트 스킬 표준을 기반으로 합니다.'
---

Source URL: https://developers.openai.com/codex/skills

# 에이전트 스킬

Agent 스킬을 사용해 Codex를 작업 전용 기능으로 확장하세요. 스킬은 Codex가 워크플로를 안정적으로 따르도록 설명, 리소스, 선택적 스크립트를 꾸린 단위입니다. 스킬은 팀 간이나 커뮤니티와 공유할 수 있으며, [오픈 에이전트 스킬 표준](https://agentskills.io)을 기반으로 합니다.

스킬은 Codex CLI, IDE 확장, Codex 앱에서 사용할 수 있습니다.

스킬은 **점진적 공개(progessive disclosure)**를 활용해 컨텍스트를 효율적으로 관리합니다. Codex는 각 스킬의 메타데이터(`name`, `description`, 파일 경로, `agents/openai.yaml`의 선택적 메타데이터)로 시작합니다. Codex가 스킬을 사용하기로 결정할 때만 전체 `SKILL.md` 지침을 로드합니다.

스킬은 `SKILL.md` 파일과 선택적 스크립트 및 참고 자료를 포함하는 디렉터리입니다. `SKILL.md` 파일에는 `name`과 `description`이 반드시 들어가야 합니다.

```tsx
<FileTree
  class="mt-4"
  tree={[
    {
      name: "my-skill/",
      open: true,
      children: [
        {
          name: "SKILL.md",
          comment: "Required: instructions + metadata",
        },
        {
          name: "scripts/",
          comment: "Optional: executable code",
        },
        {
          name: "references/",
          comment: "Optional: documentation",
        },
        {
          name: "assets/",
          comment: "Optional: templates, resources",
        },
        {
          name: "agents/",
          open: true,
          children: [
            {
              name: "openai.yaml",
              comment: "Optional: appearance and dependencies",
            },
          ],
        },
      ],
    },

]}
/>
```

## Codex가 스킬을 사용하는 방법

Codex는 두 가지 방식으로 스킬을 활성화할 수 있습니다:

1. **명시적 호출:** 프롬프트에 직접 스킬을 포함합니다. CLI/IDE에서는 `/skills`를 실행하거나 `$`로 스킬을 언급합니다.
2. **암시적 호출:** 작업이 스킬 `description`과 일치할 때 Codex가 스킬을 선택할 수 있습니다.

암시적 매칭은 `description`에 의존하므로, 설명은 범위와 경계를 명확히 작성하세요.

## 스킬 생성

내장 Creator를 먼저 사용합니다:

```text
$skill-creator
```

Creator는 스킬이 무엇을 하고 언제 트리거되며, 설명만 남길지 스크립트를 포함할지를 묻습니다. 기본값은 설명 전용입니다.

직접 폴더와 `SKILL.md` 파일을 만들어 수동으로 만들 수도 있습니다:

```md
---
name: skill-name
description: Explain exactly when this skill should and should not trigger.
---

Skill instructions for Codex to follow.
```

Codex는 스킬 변경을 자동으로 감지합니다. 업데이트가 나타나지 않으면 Codex를 재시작하세요.

## 스킬 저장 위치

Codex는 리포지터리, 사용자, 관리자, 시스템 위치에서 스킬을 읽습니다. 리포지터리의 경우 현재 작업 디렉터리부터 리포지터리 루트까지 모든 디렉터리에서 `.agents/skills`를 스캔합니다. 두 스킬이 같은 `name`을 공유해도 Codex는 병합하지 않으며, 둘 다 스킬 선택기에 표시될 수 있습니다.

| Skill Scope | Location                                                                                                  | Suggested use                                                                                                                                                                                        |
| :---------- | :-------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `REPO`      | `$CWD/.agents/skills` <br /> Codex를 실행하는 현재 작업 디렉터리입니다.                                   | 리포지터리나 코드 환경에 있다면, 특정 작업 폴더와 관련된 스킬을 체크인할 수 있습니다. 예: 마이크로서비스나 모듈에만 관련된 스킬.                                                               |
| `REPO`      | `$CWD/../.agents/skills` <br /> Git 리포지터리 안에서 Codex를 실행할 때 CWD 위에 있는 폴더입니다.       | 중첩된 폴더가 있는 리포지터리에서는 상위 폴더의 공유 영역에 관련된 스킬을 조직이 체크인할 수 있습니다.                                                                                    |
| `REPO`      | `$REPO_ROOT/.agents/skills` <br /> Git 리포지터리 안에서 Codex를 실행할 때 가장 상위 루트 폴더입니다.    | 중첩된 폴더가 있는 리포지터리에서는 모든 하위 폴더에서 사용할 수 있는 루트 스킬을 체크인할 수 있습니다.                                                                                     |
| `USER`      | `$HOME/.agents/skills` <br /> 사용자 개인 폴더에 체크인된 모든 스킬입니다.                              | 사용자가 어떤 리포지터리에서 작업하든 유용한 사용자 전용 스킬을 구성할 때 사용합니다.                                                                                                           |
| `ADMIN`     | `/etc/codex/skills` <br /> 공유 시스템 위치에 체크인된 스킬입니다.                                        | SDK 스크립트, 자동화, 머신의 각 사용자에게 제공할 기본 관리자 스킬에 사용합니다.                                                                                                                |
| `SYSTEM`    | OpenAI가 Codex에 번들로 포함합니다.                                                                       | skill-creator나 plan 스킬처럼 폭넓은 청중에게 유용한 스킬입니다. Codex를 시작할 때 모두 사용할 수 있습니다.                                                                                     |

Codex는 symlink된 스킬 폴더를 지원하며, 이 위치들을 스캔할 때 symlink 대상 경로를 따릅니다.

## 스킬 설치

기본 제공 스킬 외에 설치하려면 `$skill-installer`를 사용하세요:

```bash
$skill-installer install the linear skill from the .experimental folder
```

다른 리포지터리에서 스킬을 내려받도록 installer에 지시할 수도 있습니다. Codex는 새로 설치된 스킬을 자동으로 감지합니다. 나타나지 않으면 Codex를 재시작하세요.

## 스킬 활성화/비활성화

`~/.codex/config.toml`의 `[[skills.config]]` 항목을 사용해 스킬을 삭제하지 않고 비활성화할 수 있습니다:

```toml
[[skills.config]]
path = "/path/to/skill/SKILL.md"
enabled = false
```

`~/.codex/config.toml`을 변경한 후 Codex를 재시작하세요.

## 선택적 메타데이터

[Codex 앱](https://developers.openai.com/codex/app)에서 UI 메타데이터를 구성하거나 호출 정책을 설정하고, 스킬 사용 경험을 원활하게 하기 위한 도구 종속성을 선언하려면 `agents/openai.yaml`을 추가하세요.

```yaml
interface:
  display_name: "Optional user-facing name"
  short_description: "Optional user-facing description"
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
  brand_color: "#3B82F6"
  default_prompt: "Optional surrounding prompt to use the skill with"

policy:
  allow_implicit_invocation: false

dependencies:
  tools:
    - type: "mcp"
      value: "openaiDeveloperDocs"
      description: "OpenAI Docs MCP server"
      transport: "streamable_http"
      url: "https://developers.openai.com/mcp"
```

`allow_implicit_invocation` (기본값: `true`): `false`로 설정하면 Codex가 사용자 프롬프트 기반으로 스킬을 암시적으로 호출하지 않으며, 명시적인 `$skill` 호출은 여전히 작동합니다.

## 모범 사례

- 각 스킬은 하나의 작업에 집중하세요.
- 결정론적 행동이나 외부 도구가 필요하지 않다면 스크립트보다 설명을 선호하세요.
- 명확한 입력과 출력을 포함한 명령형 단계를 작성하세요.
- 스킬 설명과 프롬프트를 테스트해 적절한 트리거 행동을 확인하세요.

예시는 [github.com/openai/skills](https://github.com/openai/skills)과 [agent skills 명세](https://agentskills.io/specification)를 참조하세요.
