---
title: "Test Artifacts 4.0.11"
description: "이것은 고급 API입니다. 일반 사용자라면 테스트에 메모나 컨텍스트를 추가할 때 대신 test annotations을 사용하는 것이 대부분 더 적합합니다. 이 기능은 주로 내부적으로, 그리고 라이브러리 작성자에 의해 사용됩니다."
---

출처 URL: https://vitest.dev/api/advanced/artifacts

# Test Artifacts 4.0.11

::: warning
이것은 고급 API입니다. 일반 사용자라면 테스트에 메모나 컨텍스트를 추가할 때 대신 [test annotations](https://vitest.dev/guide/test-annotations)을 사용하는 것이 대부분 더 적합합니다. 이 기능은 주로 내부적으로, 그리고 라이브러리 작성자에 의해 사용됩니다.
:::

Test artifacts를 사용하면 테스트 실행 중 구조화된 데이터, 파일 또는 메타데이터를 첨부하거나 기록할 수 있습니다. 이는 주로 다음을 위해 설계된 저수준 기능입니다.

- 내부 사용([`annotate`](https://vitest.dev/guide/test-annotations)는 artifact 시스템 위에 구축됨)
- Vitest 위에서 커스텀 테스트 도구를 만드는 프레임워크 작성자

각 artifact에는 다음이 포함됩니다.

- artifact 타입을 식별하는 고유 식별자인 type discriminator
- 관련 정보를 담을 수 있는 커스텀 데이터
- artifact와 연결된 파일 또는 인라인 콘텐츠 형태의 선택적 첨부물
- artifact가 생성된 위치를 나타내는 소스 코드 위치 정보

Vitest는 첨부물 직렬화를 자동으로 처리하고(파일은 [`attachmentsDir`](https://vitest.dev/config/#attachmentsdir)로 복사됨), 소스 위치 메타데이터를 주입하므로 기록하려는 데이터에만 집중할 수 있습니다. 내부에서 올바르게 처리되려면 모든 artifacts는 **반드시** [`TestArtifactBase`](#testartifactbase)를 확장해야 하고, 모든 attachments는 [`TestAttachment`](#testattachment)를 확장해야 합니다.

## API

### `recordArtifact` {#recordartifact}

::: warning
`recordArtifact`는 실험적 API입니다. 호환성이 깨지는 변경이 SemVer를 따르지 않을 수 있으므로, 사용할 때는 Vitest 버전을 고정하세요.

API 표면은 피드백에 따라 변경될 수 있습니다. 직접 사용해 보고 팀에 경험을 공유해 주시길 권장합니다.
:::

```ts
function recordArtifact<Artifact extends TestArtifact>(
  task: Test,
  artifact: Artifact,
): Promise<Artifact>;
```

`recordArtifact` 함수는 테스트 실행 중 artifact를 기록하고 이를 반환합니다. 첫 번째 매개변수로 [task](https://vitest.dev/api/advanced/runner#tasks), 두 번째 매개변수로 [`TestArtifact`](#testartifact)에 할당 가능한 객체를 받습니다.

이 함수는 테스트 내부에서 사용해야 하며, 해당 테스트가 아직 실행 중이어야 합니다. 테스트가 완료된 뒤에 기록하면 오류가 발생합니다.

artifact가 테스트에 기록되면 `onTestArtifactRecord` runner 이벤트와 [`onTestCaseArtifactRecord` reporter 이벤트](https://vitest.dev/api/advanced/reporters#ontestcaseartifactrecord)가 발생합니다. 테스트 케이스에서 기록된 artifacts를 가져오려면 [`artifacts()`](https://vitest.dev/api/advanced/test-case#artifacts) 메서드를 사용하세요.

참고: annotations는 [이 기능 위에 구축되어 있음에도](#relationship-with-annotations) 하위 호환성 때문에 다음 메이저 버전 전까지 `task.artifacts` 배열에 나타나지 않습니다.

### `TestArtifact`

`TestArtifact` 타입은 Vitest가 생성할 수 있는 모든 artifact(커스텀 포함)를 포함하는 union입니다. 모든 artifacts는 [`TestArtifactBase`](#testartifactbase)를 확장합니다.

### `TestArtifactBase` {#testartifactbase}

```ts
export interface TestArtifactBase {
  /** File or data attachments associated with this artifact */
  attachments?: TestAttachment[];
  /** Source location where this artifact was created */
  location?: TestArtifactLocation;
}
```

`TestArtifactBase` 인터페이스는 모든 테스트 artifact의 기반입니다.

커스텀 테스트 artifact를 만들 때 이 인터페이스를 확장하세요. Vitest는 `attachments` 배열을 자동으로 관리하고 `location` 속성을 주입해 테스트 코드에서 artifact가 생성된 위치를 나타냅니다.

### `TestAttachment`

```ts
export interface TestAttachment {
  /** MIME type of the attachment (e.g., 'image/png', 'text/plain') */
  contentType?: string;
  /** File system path to the attachment */
  path?: string;
  /** Inline attachment content as a string or raw binary data */
  body?: string | Uint8Array;
}
```

`TestAttachment` 인터페이스는 테스트 artifact와 연관된 파일 또는 데이터 첨부물을 나타냅니다.

첨부물은 파일 기반(`path`)이거나 인라인 콘텐츠(`body`)일 수 있습니다. `contentType`은 소비자 측에서 첨부물 데이터를 어떻게 해석해야 하는지 이해하는 데 도움을 줍니다.

### `TestArtifactLocation`

```ts
export interface TestArtifactLocation {
  /** Line number in the source file (1-indexed) */
  line: number;
  /** Column number in the line (1-indexed) */
  column: number;
  /** Path to the source file */
  file: string;
}
```

`TestArtifactLocation` 인터페이스는 테스트 artifact의 소스 코드 위치 정보를 나타냅니다. 즉, artifact가 소스 코드의 어디에서 생성되었는지 보여줍니다.

### `TestArtifactRegistry`

`TestArtifactRegistry` 인터페이스는 커스텀 테스트 artifact 타입을 위한 레지스트리입니다.

[TypeScript의 module augmentation 기능](https://typescriptlang.org/docs/handbook/declaration-merging#module-augmentation)으로 이 인터페이스를 보강하면 테스트에서 생성할 수 있는 커스텀 artifact 타입을 등록할 수 있습니다.

각 커스텀 artifact는 [`TestArtifactBase`](#testartifactbase)를 확장하고 고유한 `type` discriminator 속성을 포함해야 합니다.

다음은 따라야 할 몇 가지 가이드라인/모범 사례입니다.

- 고유성을 보장하기 위해 **registry key**로 `Symbol` 사용을 권장합니다.
- `type` 속성은 `'package-name:artifact-name'` 패턴을 따라야 하며, **`'internal:'`은 예약된 접두사**입니다.
- 파일 또는 데이터를 포함하려면 `attachments`를 사용하고, 커스텀 메타데이터가 필요하면 [`TestAttachment`](#testattachment)를 확장하세요.
- `location` 속성은 자동으로 주입됩니다.

## Custom Artifacts

artifact를 타입 안전하게 사용하고 관리하려면 해당 타입을 만들고 등록해야 합니다.

```ts
import type { TestArtifactBase, TestAttachment } from "vitest";

interface A11yReportAttachment extends TestAttachment {
  contentType: "text/html";
  path: string;
}

interface AccessibilityArtifact extends TestArtifactBase {
  type: "a11y:report";
  passed: boolean;
  wcagLevel: "A" | "AA" | "AAA";
  attachments: [A11yReportAttachment];
}

const a11yReportKey = Symbol("report");

declare module "vitest" {
  interface TestArtifactRegistry {
    [a11yReportKey]: AccessibilityArtifact;
  }
}
```

타입이 각 기반 타입에 할당 가능하고 오류가 없다면 정상 동작해야 하며, [`recordArtifact`](#recordartifact)를 사용해 artifact를 기록할 수 있어야 합니다.

```ts
async function toBeAccessible(
  this: MatcherState,
  actual: Element,
  wcagLevel: "A" | "AA" | "AAA" = "AA",
): AsyncExpectationResult {
  const report = await runAccessibilityAudit(actual, wcagLevel);

  await recordArtifact(this.task, {
    type: "a11y:report",
    passed: report.violations.length === 0,
    wcagLevel,
    attachments: [
      {
        contentType: "text/html",
        path: report.path,
      },
    ],
  });

  return {
    pass: violations.length === 0,
    message: () =>
      `Found ${report.violations.length} accessibility violation(s)`,
  };
}
```

## Relationship with Annotations

Test annotations는 artifact 시스템 위에 구축되어 있습니다. 테스트에서 annotations를 사용하면 내부적으로 `internal:annotation` artifact가 생성됩니다. 하지만 annotations는 다음 특성이 있습니다.

- 더 간단하게 사용할 수 있음
- 개발자가 아니라 최종 사용자를 위해 설계됨

테스트에 메모만 추가하려면 annotations를 사용하세요. 커스텀 데이터가 필요하면 artifacts를 사용하세요.
