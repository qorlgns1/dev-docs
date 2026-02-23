---
title: '작업 흐름'
description: 'Codex는 명확한 맥락과 “완료” 정의를 갖춘 팀원처럼 다룰 때 가장 잘 작동합니다.'
---

Source URL: https://developers.openai.com/codex/workflows

# 작업 흐름

Codex는 명확한 맥락과 “완료” 정의를 갖춘 팀원처럼 다룰 때 가장 잘 작동합니다.  
이 페이지는 Codex IDE 확장 기능, Codex CLI, Codex 클라우드에 대한 엔드투엔드 작업 흐름 예시를 제공합니다.

Codex를 처음 사용하는 경우 [Prompting](https://developers.openai.com/codex/prompting)을 먼저 읽은 뒤 여기로 돌아와 구체적인 레시피를 확인하세요.

## 이 예시들을 어떻게 읽을까요

각 워크플로에는 다음이 포함됩니다:

- **언제 사용해야 하는지**와 어떤 Codex 표면(IDE, CLI, 또는 클라우드)이 가장 적합한지.
- **단계**와 예시 사용자 프롬프트.
- **맥락 노트**: Codex가 자동으로 보는 것 vs 직접 첨부해야 하는 것.
- **검증**: 출력을 어떻게 확인할지.

> **참고:** IDE 확장은 현재 열려 있는 파일을 자동으로 맥락에 포함시킵니다. CLI에서는 일반적으로 경로를 명시하거나 `/mention`과 `@` 경로 자동완성을 이용해 파일을 첨부해야 합니다.

---

## 코드베이스 설명하기

온보딩 중이거나 서비스를 인수받거나 프로토콜/데이터 모델/요청 흐름을 이해하려는 경우 사용합니다.

### IDE 확장 워크플로 (로컬 탐색에 가장 빠름)

1. 관련 있는 파일을 엽니다.
2. 관심 있는 코드를 선택합니다(선택 사항이지만 권장).
3. Codex에 프롬프트를 입력합니다:

   ```text
   Explain how the request flows through the selected code.

   Include:
   - a short summary of the responsibilities of each module involved
   - what data is validated and where
   - one or two "gotchas" to watch for when changing this
   ```

검증:

- 빠르게 확인 가능한 다이어그램이나 체크리스트를 요청합니다:

```text
Summarize the request flow as a numbered list of steps. Then list the files involved.
```

### CLI 워크플로 (전사 기록 + 셸 명령이 필요한 경우 유용)

1. 인터랙티브 세션을 시작합니다:

   ```bash
   codex
   ```

2. 파일을 첨부(선택 사항)한 뒤 프롬프트를 입력합니다:

   ```text
   I need to understand the protocol used by this service. Read @foo.ts @schema.ts and explain the schema and request/response flow. Focus on required vs optional fields and backward compatibility rules.
   ```

맥락 노트:

- 작성기에서 `@`를 사용해 작업공간의 파일 경로를 입력하거나 `/mention`으로 특정 파일을 첨부할 수 있습니다.

---

## 버그 수정하기

지역적으로 재현 가능한 실패 동작이 있을 때 사용합니다.

### CLI 워크플로 (재현 및 검증을 위한 빠른 루프)

1. 리포지토리 루트에서 Codex를 시작합니다:

   ```bash
   codex
   ```

2. 재현 레시피와 의심되는 파일을 제공합니다:

   ```text
   Bug: Clicking "Save" on the settings screen sometimes shows "Saved" but doesn't persist the change.

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
   ```

맥락 노트:

- 제공하는 것: 재현 단계와 제약 조건(이게 고수준 설명보다 중요함).
- Codex가 제공하는 것: 커맨드 출력, 발견된 호출 지점, 발생한 스택 트레이스.

검증:

- 수정 후 Codex가 재현 단계를 다시 실행해야 합니다.
- 표준 점검 파이프라인이 있다면 실행하도록 요청합니다:

```text
After the fix, run lint + the smallest relevant test suite. Report the commands and results.
```

### IDE 확장 워크플로

1. 버그가 있을 것으로 생각되는 파일과 가장 가까운 호출자를 엽니다.
2. Codex에 프롬프트를 입력합니다:

   ```text
   Find the bug causing "Saved" to show without persisting changes. After proposing the fix, tell me how to verify it in the UI.
   ```

---

## 테스트 작성하기

검증 대상 범위를 매우 명확히 지정하고 싶을 때 사용합니다.

### IDE 확장 워크플로 (선택 기반)

1. 함수가 있는 파일을 엽니다.
2. 함수 정의 부분을 선택합니다. 커맨드 팔레트에서 "Add to Codex Thread"를 선택해 해당 줄을 맥락에 추가합니다.
3. Codex에 프롬프트를 입력합니다:

   ```text
   Write a unit test for this function. Follow conventions used in other tests.
   ```

맥락 노트:

- "Add to Codex Thread" 명령이 제공: 선택한 줄(이게 "줄 번호 범위"가 됨)과 열린 파일들.

### CLI 워크플로 (경로 + 줄 범위를 설명)

1. Codex를 시작합니다:

   ```bash
   codex
   ```

2. 함수 이름을 포함한 프롬프트를 입력합니다:

   ```text
   Add a test for the invert_list function in @transform.ts. Cover the happy path plus edge cases.
   ```

---

## 스크린샷으로 프로토타입 만들기

디자인 목업, 스크린샷, UI 참조가 있고 빠르게 작동하는 프로토타입을 원할 때 사용합니다.

### CLI 워크플로 (이미지 + 프롬프트)

1. 스크린샷을 로컬에 저장합니다(예: `./specs/ui.png`).
2. Codex를 실행합니다:

   ```bash
   codex
   ```

3. 이미지 파일을 터미널에 드래그하여 프롬프트에 첨부합니다.

4. 제약 및 구조를 덧붙입니다:

   ```text
   Create a new dashboard based on this image.

   Constraints:
   - Use react, vite, and tailwind. Write the code in typescript.
   - Match spacing, typography, and layout as closely as possible.

   Deliverables:
   - A new route/page that renders the UI
   - Any small components needed
   - README.md with instructions to run it locally
   ```

맥락 노트:

- 이미지는 시각적 요구사항을 제공하지만 구현 제약(프레임워크, 라우팅, 컴포넌트 스타일)은 직접 명시해야 합니다.
- 최상의 결과를 위해 비직관적인 동작(호버, 검증, 키보드 상호작용 등)을 텍스트로 포함하세요.

검증:

- Codex에게 개발 서버를 실행하도록 하고 정확히 어떤 로컬 URL/경로에서 프토토타입을 볼 수 있는지 알려달라고 하세요:

```text
Start the dev server and tell me the local URL/route to view the prototype.
```

### IDE 확장 워크플로 (이미지 + 기존 파일)

1. Codex 채팅에 이미지 첨부(드래그 앤 드롭 또는 붙여넣기).
2. Codex에 프롬프트:

   ```text
   Create a new settings page. Use the attached screenshot as the target UI.
   Follow design and visual patterns from other files in this project.
   ```

---

## 실시간 업데이트로 UI 반복하기

디자인 → 조정 → 새로고침 → 조정이라는 긴밀한 루프를 원할 때 사용합니다.

### CLI 워크플로 (Vite 실행 후 작은 프롬프트로 반복)

1. Codex를 실행합니다:

   ```bash
   codex
   ```

2. 별도 터미널 창에서 개발 서버 실행:

   ```bash
   npm run dev
   ```

3. Codex에 변경을 요청합니다:

   ```text
   Propose 2-3 styling improvements for the landing page.
   ```

4. 방향을 선택하고 세부적인 프롬프트로 반복합니다:

   ```text
   Go with option 2.

   Change only the header:
   - make the typography more editorial
   - increase whitespace
   - ensure it still looks good on mobile
   ```

5. 집중된 요청으로 다시 반복:

   ```text
   Next iteration: reduce visual noise.
   Keep the layout, but simplify colors and remove any redundant borders.
   ```

검증:

- 브라우저에서 코드 변경 사항을 실시간으로 확인합니다.
- 마음에 드는 변경은 커밋하고, 마음에 들지 않으면 되돌립니다.
- 되돌리거나 수정한 경우 Codex에게 알려 다음 프롬프트에서 덮어쓰지 않도록 합니다.

---

## 리팩터를 클라우드에 위임하기

신중하게 설계한 뒤 긴 구현을 병렬로 실행 가능한 클라우드 작업에 맡기고 싶을 때 사용합니다.

### 로컬 기획 (IDE)

1. 현재 작업을 커밋하거나 적어도 스태시하여 변경 사항을 깨끗하게 비교할 수 있도록 합니다.
2. Codex에게 리팩터 계획을 생성해달라고 요청합니다. `$plan` 스킬을 사용할 수 있다면 명시적으로 호출합니다:

   ```text
   $plan

   We need to refactor the auth subsystem to:
   - split responsibilities (token parsing vs session loading vs permissions)
   - reduce circular imports
   - improve testability

   Constraints:
   - No user-visible behavior changes
   - Keep public APIs stable
   - Include a step-by-step migration plan
   ```

3. 계획을 검토하고 수정 요청:

   ```text
   Revise the plan to:
   - specify exactly which files move in each milestone
   - include a rollback strategy
   ```

맥락 노트:

- Codex가 현재 코드를 로컬에서 스캔할 수 있을 때(엔트리포인트, 모듈 경계, 의존성 그래프 힌트) 계획이 가장 잘 작동합니다.

### 클라우드 위임 (IDE → 클라우드)

1. 아직 설정하지 않았다면 [Codex 클라우드 환경](https://developers.openai.com/codex/cloud/environments)을 설정합니다.
2. 프롬프트 작성기 아래 클라우드 아이콘을 클릭하고 클라우드 환경을 선택합니다.
3. 다음 프롬프트를 입력하면 Codex가 기존 스레드 맥락(계획 및 로컬 소스 변경 포함)을 이어받아 클라우드에서 새 스레드를 만듭니다.

   ```text
   Implement Milestone 1 from the plan.
   ```

4. 클라우드 diff를 검토하고 필요하면 반복합니다.
5. 클라우드에서 직접 PR을 생성하거나 로컬로 변경을 내려받아 테스트 및 마무리합니다.
6. 계획의 추가 마일스톤을 반복합니다.

---

## 로컬 코드 리뷰 수행

커밋 전에 또는 PR 생성에 앞서 두 번째 눈을 원할 때 사용합니다.

### CLI 워크플로 (작업 트리 리뷰)

1. Codex를 실행합니다:

   ```bash
   codex
   ```

2. 리뷰 명령 실행:

   ```text
   /review
   ```

3. 선택 사항: 집중할 항목 지시:

   ```text
   /review Focus on edge cases and security issues
   ```

검증:

- 리뷰 피드백을 기반으로 수정한 뒤 `/review`를 다시 실행하여 문제가 해결되었는지 확인합니다.

---

## GitHub 풀 리퀘스트 리뷰

브랜치를 로컬로 가져오지 않고 리뷰 피드백을 받을 때 사용합니다.

풀 리퀘스트를 사용하려면 먼저 리포지토리에서 Codex **Code review**를 활성화해야 합니다. 자세한 내용은 [Code review](https://developers.openai.com/codex/integrations/github)를 확인하세요.

### GitHub 워크플로 (댓글 기반)

1. GitHub에서 풀 리퀘스트를 엽니다.
2. Codex를 특정 포커스로 태그하며 댓글을 남깁니다:

   ```text
   @codex review
   ```

3. 선택 사항: 더 명확한 지시 제공:

   ```text
   @codex review for security vulnerabilities and security concerns
   ```

---

## 문서 업데이트

정확하고 명확한 문서 변경이 필요할 때 사용합니다.

### IDE 또는 CLI 워크플로 (로컬 편집 + 로컬 검증)

1. 변경할 문서 파일을 식별하여 엽니다(IDE) 또는 `@`로 언급합니다(IDE 또는 CLI).
2. 범위 및 검증 요구사항과 함께 Codex에 프롬프트:

   ```text
   Update the "advanced features" documentation to provide authentication troubleshooting guidance. Verify that all links are valid.
   ```

3. Codex가 초안을 만들면 문서를 검토하고 필요하면 반복합니다.

검증:

- 렌더링된 페이지를 읽어 확인합니다.
