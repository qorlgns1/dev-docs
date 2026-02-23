# 에이전트 스킬

출처 URL: https://developers.openai.com/codex/skills

에이전트 스킬을 사용하면 Codex를 작업별 역량으로 확장할 수 있습니다. 스킬은 지침, 리소스, 선택 스크립트를 묶어 Codex가 워크플로를 안정적으로 따르도록 합니다. 스킬은 팀 간 혹은 커뮤니티와 공유할 수 있습니다. 스킬은 [open agent skills standard](https://agentskills.io)를 기반으로 구축됩니다.

스킬은 Codex CLI, IDE 확장, Codex 앱에서 사용할 수 있습니다.

스킬은 **점진적 공개**로 컨텍스트를 효율적으로 관리합니다. Codex는 먼저 각 스킬의 메타데이터(`name`, `description`, 파일 경로, `agents/openai.yaml`의 선택 메타데이터)를 확인하고, 스킬을 사용하기로 결정했을 때만 전체 `SKILL.md` 지침을 불러옵니다.

스킬은 `SKILL.md` 파일과 선택 스크립트·참고 자료를 포함하는 디렉터리입니다. `SKILL.md` 파일에는 반드시 `name`과 `description`이 있어야 합니다.

  * my-skill/ 

    * SKILL.md  필수: 지침 + 메타데이터 

    * scripts/  선택: 실행 코드 

    * references/  선택: 문서 

    * assets/  선택: 템플릿, 리소스 

    * agents/ 

      * openai.yaml  선택: 외형 및 의존성 




## Codex가 스킬을 사용하는 방식

Codex는 두 가지 방법으로 스킬을 활성화합니다.

  1. **명시적 호출:** 프롬프트에 스킬을 직접 포함합니다. CLI/IDE에서는 `/skills`를 실행하거나 `$`로 스킬을 언급합니다.
  2. **암시적 호출:** 작업이 스킬 `description`과 일치할 때 Codex가 스킬을 선택합니다.



암시적 매칭은 `description`에 의존하므로, 범위와 경계를 명확하게 작성하세요.

## 스킬 만들기

기본 제공 크리에이터를 먼저 사용하세요.
[code] 
    $skill-creator
[/code]

크리에이터는 스킬의 기능, 트리거 조건, 지침 전용으로 둘지 스크립트를 포함할지 묻습니다. 기본값은 지침 전용입니다.

폴더와 `SKILL.md` 파일을 만들어 수동으로 스킬을 만들 수도 있습니다.
[code] 
    ---
    name: skill-name
    description: Explain exactly when this skill should and should not trigger.
    ---
    
    Skill instructions for Codex to follow.
[/code]

Codex는 스킬 변경을 자동으로 감지합니다. 업데이트가 반영되지 않으면 Codex를 재시작하세요.

## 스킬 저장 위치

Codex는 리포지토리, 사용자, 관리자, 시스템 위치에서 스킬을 읽습니다. 리포지토리의 경우 현재 작업 디렉터리에서 리포지토리 루트까지의 모든 경로에서 `.agents/skills`를 스캔합니다. 두 스킬이 동일한 `name`을 공유해도 Codex는 병합하지 않으며, 둘 다 스킬 선택기에 표시될 수 있습니다.

Skill Scope| Location| 권장 용도  
---|---|---  
`REPO`| `$CWD/.agents/skills`   
Codex를 시작하는 현재 작업 디렉터리.| 리포지토리나 코드 환경에 있을 때 팀이 특정 작업 폴더와 관련된 스킬을 체크인할 수 있습니다. 예: 특정 마이크로서비스나 모듈 전용 스킬.  
`REPO`| `$CWD/../.agents/skills`   
Git 리포지토리 내부에서 Codex를 실행할 때 CWD 위의 폴더.| 중첩 폴더가 있는 리포지토리에서 조직이 상위 폴더의 공유 영역과 관련된 스킬을 체크인할 수 있습니다.  
`REPO`| `$REPO_ROOT/.agents/skills`   
Git 리포지토리 내부에서 Codex를 실행할 때 최상위 루트 폴더.| 중첩 폴더가 있는 리포지토리에서 조직이 모든 사용자에게 해당되는 스킬을 체크인할 수 있습니다. 리포지토리의 모든 하위 폴더에서 사용할 수 있는 루트 스킬로 동작합니다.  
`USER`| `$HOME/.agents/skills`   
사용자 개인 폴더에 체크인된 스킬.| 사용자가 작업할 수 있는 모든 리포지토리에 적용되는 개인 맞춤 스킬을 큐레이션할 때 사용합니다.  
`ADMIN`| `/etc/codex/skills`   
공유 시스템 위치(머신이나 컨테이너)에 체크인된 스킬.| SDK 스크립트, 자동화, 머신의 각 사용자에게 제공되는 기본 관리자 스킬을 체크인할 때 사용합니다.  
`SYSTEM`| OpenAI가 Codex와 함께 번들 제공.| skill-creator나 plan 스킬처럼 폭넓은 사용자에게 유용한 스킬. Codex를 시작하면 모든 사용자에게 제공됩니다.

Codex는 심볼릭 링크된 스킬 폴더를 지원하며, 이러한 위치를 검사할 때 심볼릭 링크 대상 경로를 따라갑니다.

## 스킬 설치

기본 제공 스킬 외의 스킬을 설치하려면 `$skill-installer`를 사용하세요:
[code] 
    $skill-installer install the linear skill from the .experimental folder
[/code]

또한 설치 프로그램에 다른 저장소에서 스킬을 다운로드하도록 지시할 수도 있습니다. Codex는 새로 설치된 스킬을 자동으로 감지하며, 표시되지 않으면 Codex를 다시 시작하세요.

## 스킬 활성화 또는 비활성화

스킬을 삭제하지 않고 비활성화하려면 `~/.codex/config.toml`의 `[[skills.config]]` 항목을 사용하세요:
[code] 
    [[skills.config]]
    path = "/path/to/skill/SKILL.md"
    enabled = false
[/code]

`~/.codex/config.toml`을 변경한 뒤에는 Codex를 다시 시작하세요.

## 선택적 메타데이터

더 원활한 스킬 사용 경험을 위해 [Codex 앱](https://developers.openai.com/codex/app)에서 UI 메타데이터를 구성하고 호출 정책을 설정하며 도구 종속성을 선언하려면 `agents/openai.yaml`을 추가하세요.
[code] 
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
[/code]

`allow_implicit_invocation`(기본값: `true`): `false`이면 Codex는 사용자 프롬프트만으로 스킬을 암묵적으로 호출하지 않으며, 명시적인 `$skill` 호출은 계속 동작합니다.

## 모범 사례

  * 각 스킬은 하나의 작업에 집중하도록 유지하세요.
  * 결정적 동작이나 외부 도구가 필요한 경우를 제외하고 스크립트보다 지침을 우선하세요.
  * 명령형 단계로 명확한 입력과 출력을 작성하세요.
  * 올바른 트리거 동작을 확인하기 위해 스킬 설명에 대해 프롬프트를 테스트하세요.

추가 예시는 [github.com/openai/skills](https://github.com/openai/skills)와 [the agent skills specification](https://agentskills.io/specification)에서 확인하세요.
