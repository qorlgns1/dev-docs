# 워크플로우

Source URL: https://developers.openai.com/codex/workflows

Codex는 명시적인 컨텍스트와 명확한 "완료" 정의를 갖춘 팀원처럼 대할 때 가장 잘 작동합니다. 이 페이지는 Codex IDE 확장, Codex CLI, Codex Cloud에 대한 엔드투엔드 워크플로우 예시를 제공합니다.

Codex가 처음이라면 먼저 [Prompting](https://developers.openai.com/codex/prompting)을 읽고, 이후 여기에 돌아와 구체적인 레시피를 확인하세요.

## 이 예시를 읽는 방법

각 워크플로우는 다음을 포함합니다:

  * **언제 사용할지**와 어떤 Codex 환경(IDE, CLI, 또는 클라우드)이 가장 적합한지.
  * 예시 사용자 프롬프트가 있는 **단계**.
  * **컨텍스트 메모**: Codex가 자동으로 보는 것과 사용자가 첨부해야 하는 것.
  * **검증**: 출력을 확인하는 방법.



> **참고:** IDE 확장은 열려 있는 파일을 자동으로 컨텍스트에 포함합니다. CLI에서는 보통 경로를 명시적으로 언급하거나 `/mention`과 `@` 경로 자동 완성을 사용해 파일을 첨부해야 합니다.

* * *

## 코드베이스 설명하기

온보딩 중이거나 서비스를 인계받거나 프로토콜, 데이터 모델, 요청 흐름을 이해하려 할 때 사용하세요.

### IDE 확장 워크플로우(로컬 탐색에 가장 빠름)

  1. 가장 관련 있는 파일을 엽니다.

  2. 관심 있는 코드를 선택합니다(선택 사항이지만 권장).

  3. Codex에 다음과 같이 프롬프트를 입력합니다:
[code] Explain how the request flows through the selected code.
         
         Include:
         - a short summary of the responsibilities of each module involved
         - what data is validated and where
         - one or two "gotchas" to watch for when changing this
[/code]




검증:

  * 빠르게 검증할 수 있는 다이어그램이나 체크리스트를 요청하세요:


[code] 
    Summarize the request flow as a numbered list of steps. Then list the files involved.
[/code]

### CLI 워크플로우(대화 기록과 셸 명령이 필요할 때 적합)

  1. 대화형 세션을 시작합니다:
[code] codex
[/code]

  2. 파일을 첨부(선택)하고 다음과 같이 프롬프트를 입력합니다:
[code] I need to understand the protocol used by this service. Read @foo.ts @schema.ts and explain the schema and request/response flow. Focus on required vs optional fields and backward compatibility rules.
[/code]




컨텍스트 메모:

  * 작곡기에서 `@`를 사용해 워크스페이스의 파일 경로를 삽입하거나 `/mention`으로 특정 파일을 첨부할 수 있습니다.



* * *

## 버그 수정

로컬에서 재현 가능한 실패 동작이 있을 때 사용하세요.

### CLI 워크플로우(재현과 검증을 빠르게 반복)

  1. 저장소 루트에서 Codex를 시작합니다:
[code] codex
[/code]

  2. Codex에 재현 절차와 의심되는 파일을 전달합니다:
[code] Bug: Clicking "Save" on the settings screen sometimes shows "Saved" but doesn't persist the change.
         
         Repro:
         1) Start the app: npm run dev
         2) Go to /settings
         3) Toggle "Enable alerts"
         4) Click Save
         5) Refresh the page: the toggle resets
         
         Constraints:
         - Do not change the API shape.
         - Keep the fix minimal and add a regression test if feasible.
         
         Start by reproducing the bug locally, then propose a patch and run checks.
[/code]




컨텍스트 메모:

  * 사용자가 제공: 재현 단계와 제약(상위 수준 설명보다 중요).
  * Codex가 제공: 명령 출력, 발견된 호출 지점, 발생한 스택 트레이스.



검증:

  * 수정 후 Codex가 재현 단계를 다시 실행해야 합니다.
  * 표준 검사 파이프라인이 있다면 실행을 요청하세요:


[code] 
    After the fix, run lint + the smallest relevant test suite. Report the commands and results.
[/code]

### IDE 확장 워크플로우

  1. 버그가 있다고 생각하는 파일과 가장 가까운 호출자를 엽니다.

  2. Codex에 프롬프트를 입력합니다:
[code] Find the bug causing "Saved" to show without persisting changes. After proposing the fix, tell me how to verify it in the UI.
[/code]




* * *

## 테스트 작성

테스트 범위를 매우 명확히 지정하고 싶을 때 사용하세요.

### IDE 확장 워크플로우(선택 기반)

1. 함수가 포함된 파일을 엽니다.

  2. 함수를 정의하는 줄을 선택합니다. 커맨드 팔레트에서 “Add to Codex Thread”를 선택해 이 줄을 컨텍스트에 추가합니다.

  3. Codex에 다음을 프롬프트합니다:
[code] Write a unit test for this function. Follow conventions used in other tests.
[/code]




컨텍스트 메모:

  * “Add to Codex Thread” 명령으로 제공: 선택한 줄(“line number” 범위)과 열려 있는 파일들.



### CLI 워크플로(프롬프트에 경로 + 줄 범위 설명)

  1. Codex를 시작합니다:
[code] codex
[/code]

  2. 함수 이름으로 프롬프트합니다:
[code] Add a test for the invert_list function in @transform.ts. Cover the happy path plus edge cases.
[/code]




* * *

## 스크린샷 기반 프로토타입

디자인 목업, 스크린샷, UI 레퍼런스를 기반으로 빠르게 동작하는 프로토타입이 필요할 때 사용합니다.

### CLI 워크플로(이미지 + 프롬프트)

  1. 스크린샷을 로컬에 저장합니다(예: `./specs/ui.png`).

  2. Codex를 실행합니다:
[code] codex
[/code]

  3. 이미지 파일을 터미널에 드래그하여 프롬프트에 첨부합니다.

  4. 제약과 구조를 이어서 전달합니다:
[code] Create a new dashboard based on this image.
         
         Constraints:
         - Use react, vite, and tailwind. Write the code in typescript.
         - Match spacing, typography, and layout as closely as possible.
         
         Deliverables:
         - A new route/page that renders the UI
         - Any small components needed
         - README.md with instructions to run it locally
[/code]




컨텍스트 메모:

  * 이미지는 시각적 요구사항을 제공하지만, 구현 제약(프레임워크, 라우팅, 컴포넌트 스타일)은 여전히 텍스트로 지정해야 합니다.
  * 최상의 결과를 위해, 명확하지 않은 동작(호버 상태, 검증 규칙, 키보드 상호작용 등)은 텍스트에 포함하세요.



검증:

  * Codex에 dev 서버를 실행하도록 요청하고, 확인해야 할 정확한 위치를 알려 달라고 합니다:


[code] 
    Start the dev server and tell me the local URL/route to view the prototype.
[/code]

### IDE 확장 워크플로(이미지 + 기존 파일)

  1. Codex 채팅에 이미지를 첨부합니다(드래그 앤드 드롭 또는 붙여넣기).

  2. Codex에 프롬프트합니다:
[code] Create a new settings page. Use the attached screenshot as the target UI.
         Follow design and visual patterns from other files in this project.
[/code]




* * *

## 라이브 업데이트로 UI 반복

Codex가 코드를 편집하는 동안 “디자인 → 수정 → 새로 고침 → 수정” 반복 루프가 필요할 때 사용합니다.

### CLI 워크플로(Vite 실행 후 작은 프롬프트로 반복)

  1. Codex를 시작합니다:
[code] codex
[/code]

  2. 별도의 터미널 창에서 dev 서버를 시작합니다:
[code] npm run dev
[/code]

  3. Codex에 변경 요청을 합니다:
[code] Propose 2-3 styling improvements for the landing page.
[/code]

  4. 방향을 선택하고 작은, 구체적인 프롬프트로 반복합니다:
[code] Go with option 2.
         
         Change only the header:
         - make the typography more editorial
         - increase whitespace
         - ensure it still looks good on mobile
[/code]

  5. 집중된 요청으로 반복합니다:
[code] Next iteration: reduce visual noise.
         Keep the layout, but simplify colors and remove any redundant borders.
[/code]




검증:

  * 코드가 업데이트되는 동안 브라우저에서 변경 사항을 “라이브”로 확인합니다.
  * 마음에 드는 변경 사항을 커밋하고, 마음에 들지 않는 변경 사항은 되돌립니다.
  * 변경을 되돌리거나 수정했다면, Codex에 알려서 이후 작업에서 해당 변경을 덮어쓰지 않도록 합니다.



* * *

## 리팩터링을 클라우드에 위임

로컬에서 신중하게 설계(로컬 컨텍스트, 빠른 확인)한 뒤, 긴 구현을 병렬로 실행 가능한 클라우드 작업에 맡기고 싶을 때 사용합니다.

### 로컬 계획(IDE)

  1. 현재 작업을 커밋하거나 최소한 스태시하여 변경 사항을 깔끔하게 비교할 수 있게 합니다.

  2. Codex에 리팩터 계획을 작성해 달라고 요청합니다. `$plan` 스킬을 사용할 수 있다면 명시적으로 호출합니다:
[code] $plan
         
         We need to refactor the auth subsystem to:
[/code]

- 책임을 분리합니다 (토큰 파싱 vs 세션 로딩 vs 권한)
         - 순환 import를 줄입니다
         - 테스트 용이성을 높입니다
         
         제약 조건:
         - 사용자에게 보이는 동작 변경 금지
         - 공개 API는 안정적으로 유지
         - 단계별 마이그레이션 계획 포함
[/code]

  3. 계획을 검토하고 변경 사항을 협의하세요:
[code] Revise the plan to:
         - specify exactly which files move in each milestone
         - include a rollback strategy
[/code]

컨텍스트 메모:

  * Codex가 현재 코드를 로컬에서 스캔할 수 있을 때(엔트리포인트, 모듈 경계, 의존성 그래프 힌트) 계획 수립이 가장 잘 동작합니다.

### 클라우드 위임 (IDE → Cloud)

  1. 아직 하지 않았다면 [Codex cloud environment](https://developers.openai.com/codex/cloud/environments)를 설정하세요.

  2. 프롬프트 컴포저 아래의 클라우드 아이콘을 클릭하고 클라우드 환경을 선택하세요.

  3. 다음 프롬프트를 입력하면 Codex가 기존 스레드 컨텍스트(계획과 로컬 소스 변경 사항 포함)를 그대로 가져오는 새로운 클라우드 스레드를 만듭니다.
[code] Implement Milestone 1 from the plan.
[/code]

  4. 클라우드 diff를 검토하고 필요하면 반복하세요.

  5. 클라우드에서 바로 PR을 만들거나 변경 사항을 로컬로 가져와 테스트하고 마무리하세요.

  6. 계획의 추가 마일스톤을 계속 반복하세요.

* * *

## 로컬 코드 리뷰 수행

커밋하거나 PR을 만들기 전에 두 번째 검토가 필요할 때 사용하세요.

### CLI 워크플로(작업 중인 트리 리뷰)

  1. Codex를 시작하세요:
[code] codex
[/code]

  2. 리뷰 명령을 실행하세요:
[code] /review
[/code]

  3. 선택 사항: 맞춤 초점을 제공하세요:
[code] /review Focus on edge cases and security issues
[/code]

검증:

  * 리뷰 피드백을 기반으로 수정한 다음 `/review`를 다시 실행해 문제가 해결되었는지 확인하세요.

* * *

## GitHub 풀 리퀘스트 리뷰

브랜치를 로컬로 가져오지 않고 리뷰 피드백이 필요할 때 사용하세요.

이 기능을 사용하기 전에 저장소에서 Codex **Code review**를 활성화하세요. [Code review](https://developers.openai.com/codex/integrations/github)를 참고하세요.

### GitHub 워크플로(코멘트 기반)

  1. GitHub에서 풀 리퀘스트를 엽니다.

  2. 명시적인 초점 영역을 포함해 Codex를 태그하는 코멘트를 남깁니다:
[code] @codex review
[/code]

  3. 선택 사항: 더 구체적인 지침을 제공합니다.
[code] @codex review for security vulnerabilities and security concerns
[/code]

* * *

## 문서 업데이트

정확하고 명확한 문서 변경이 필요할 때 사용하세요.

### IDE 또는 CLI 워크플로(로컬 편집 + 로컬 검증)

  1. 변경할 문서 파일을 식별하고 엽니다(IDE) 또는 `@`로 언급합니다(IDE 또는 CLI).

  2. 범위와 검증 요구 사항과 함께 Codex에 프롬프트를 제공합니다:
[code] Update the "advanced features" documentation to provide authentication troubleshooting guidance. Verify that all links are valid.
[/code]

  3. Codex가 초안을 작성한 후 문서를 검토하고 필요에 따라 반복합니다.

검증:

  * 렌더링된 페이지를 읽어보세요.
