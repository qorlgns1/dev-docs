---
title: "TestCase"
description: '클래스는 단일 테스트를 나타냅니다. 이 클래스는 메인 스레드에서만 사용할 수 있습니다. 런타임 태스크를 다루는 경우 "Runner API"를 참고하세요.'
---

출처 URL: https://vitest.dev/api/advanced/test-case

# TestCase

`TestCase` 클래스는 단일 테스트를 나타냅니다. 이 클래스는 메인 스레드에서만 사용할 수 있습니다. 런타임 태스크를 다루는 경우 ["Runner API"](https://vitest.dev/api/advanced/runner#tasks)를 참고하세요.

`TestCase` 인스턴스는 항상 값이 `test`인 `type` 속성을 가집니다. 이를 사용해 서로 다른 태스크 타입을 구분할 수 있습니다:

```ts
if (task.type === "test") {
  task; // TestCase
}
```

## project

이 테스트가 속한 [`TestProject`](https://vitest.dev/api/advanced/test-project)를 참조합니다.

## module

테스트가 정의된 [`TestModule`](https://vitest.dev/api/advanced/test-module)을 직접 참조합니다.

## name

`test` 함수에 전달된 테스트 이름입니다.

```ts
import { test } from "vitest";

// [!code word:'the validation works correctly']
test("the validation works correctly", () => {
  // ...
});
```

## fullName

`>` 기호로 구분된 모든 상위 스위트를 포함한 테스트 이름입니다. 이 테스트의 전체 이름은 "the validation logic > the validation works correctly"입니다:

```ts
import { describe, test } from "vitest";

// [!code word:'the validation works correctly']
// [!code word:'the validation logic']
describe("the validation logic", () => {
  test("the validation works correctly", () => {
    // ...
  });
});
```

## id

테스트의 고유 식별자입니다. 이 ID는 결정적(deterministic)이며, 동일한 테스트에 대해 여러 번 실행해도 동일하게 유지됩니다. ID는 [project](https://vitest.dev/api/advanced/test-project) 이름, 모듈 ID, 테스트 순서를 기반으로 합니다.

ID는 다음과 같은 형태입니다:

```
1223128da3_0_0
^^^^^^^^^^ the file hash
           ^ suite index
             ^ test index
```

::: tip
Vitest 3부터 사용 가능한 `vitest/node`의 `generateFileHash` 함수를 사용해 파일 해시를 생성할 수 있습니다:

```ts
import { generateFileHash } from "vitest/node";

const hash = generateFileHash(
  "/file/path.js", // relative path
  undefined, // the project name or `undefined` is not set
);
```

:::

::: danger
ID를 파싱하려고 하지 마세요. 시작 부분에 마이너스가 올 수 있습니다: `-1223128da3_0_0_0`.
:::

## location

테스트가 정의된 모듈 내 위치입니다. 위치 정보는 설정에서 [`includeTaskLocation`](https://vitest.dev/config/#includetasklocation)이 활성화된 경우에만 수집됩니다. 이 옵션은 `--reporter=html`, `--ui`, `--browser` 플래그를 사용하는 경우 자동으로 활성화됩니다.

이 테스트의 위치는 `{ line: 3, column: 1 }`와 같습니다:

```ts:line-numbers {3}
import { test } from 'vitest'

test('the validation works correctly', () => {
  // ...
})
```

## parent

상위 [suite](https://vitest.dev/api/advanced/test-suite)입니다. 테스트가 [module](https://vitest.dev/api/advanced/test-module) 내부에서 직접 호출된 경우, parent는 모듈 자체가 됩니다.

## options

```ts
interface TaskOptions {
  readonly each: boolean | undefined;
  readonly fails: boolean | undefined;
  readonly concurrent: boolean | undefined;
  readonly shuffle: boolean | undefined;
  readonly retry: number | undefined;
  readonly repeats: number | undefined;
  readonly mode: "run" | "only" | "skip" | "todo";
}
```

테스트가 수집될 때 사용된 옵션입니다.

## ok

```ts
function ok(): boolean;
```

테스트가 스위트를 실패시키지 않았는지 확인합니다. 테스트가 아직 완료되지 않았거나 건너뛰어진 경우 `true`를 반환합니다.

## meta

```ts
function meta(): TaskMeta;
```

테스트 실행 중 테스트에 첨부된 사용자 정의 [metadata](https://vitest.dev/api/advanced/metadata)입니다. 테스트 실행 중 `ctx.task.meta` 객체에 속성을 할당하여 meta를 첨부할 수 있습니다:

```ts {3,6}
import { test } from "vitest";

test("the validation works correctly", ({ task }) => {
  // ...

  task.meta.decorated = false;
});
```

테스트 실행이 아직 완료되지 않았다면 meta는 빈 객체입니다.

## result

```ts
function result(): TestResult;
```

테스트 결과입니다. 테스트가 아직 완료되지 않았거나 방금 수집된 상태라면 `TestResultPending`과 같습니다:

```ts
export interface TestResultPending {
  /**
   * The test was collected, but didn't finish running yet.
   */
  readonly state: "pending";
  /**
   * Pending tests have no errors.
   */
  readonly errors: undefined;
}
```

테스트가 건너뛰어진 경우 반환값은 `TestResultSkipped`입니다:

```ts
interface TestResultSkipped {
  /**
   * The test was skipped with `skip` or `todo` flag.
   * You can see which one was used in the `options.mode` option.
   */
  readonly state: "skipped";
  /**
   * Skipped tests have no errors.
   */
  readonly errors: undefined;
  /**
   * A custom note passed down to `ctx.skip(note)`.
   */
  readonly note: string | undefined;
}
```

::: tip
다른 테스트에 `only` 플래그가 있어서 테스트가 건너뛰어진 경우, `options.mode`는 `skip`과 같습니다.
:::

테스트가 실패한 경우 반환값은 `TestResultFailed`입니다:

```ts
interface TestResultFailed {
  /**
   * The test failed to execute.
   */
  readonly state: "failed";
  /**
   * Errors that were thrown during the test execution.
   */
  readonly errors: ReadonlyArray<TestError>;
}
```

테스트가 통과한 경우 반환값은 `TestResultPassed`입니다:

```ts
interface TestResultPassed {
  /**
   * The test passed successfully.
   */
  readonly state: "passed";
  /**
   * Errors that were thrown during the test execution.
   */
  readonly errors: ReadonlyArray<TestError> | undefined;
}
```

::: warning
`passed` 상태의 테스트에도 오류가 첨부될 수 있다는 점에 유의하세요. 이는 `retry`가 최소 한 번 이상 트리거된 경우 발생할 수 있습니다.
:::

## diagnostic

```ts
function diagnostic(): TestDiagnostic | undefined;
```

실행 시간, 메모리 사용량 등 테스트에 대한 유용한 정보입니다:

```ts
interface TestDiagnostic {
  /**
   * If the duration of the test is above `slowTestThreshold`.
   */
  readonly slow: boolean;
  /**
   * The amount of memory used by the test in bytes.
   * This value is only available if the test was executed with `logHeapUsage` flag.
   */
  readonly heap: number | undefined;
  /**
   * The time it takes to execute the test in ms.
   */
  readonly duration: number;
  /**
   * The time in ms when the test started.
   */
  readonly startTime: number;
  /**
   * The amount of times the test was retried.
   */
  readonly retryCount: number;
  /**
   * The amount of times the test was repeated as configured by `repeats` option.
   * This value can be lower if the test failed during the repeat and no `retry` is configured.
   */
  readonly repeatCount: number;
  /**
   * If test passed on a second retry.
   */
  readonly flaky: boolean;
}
```

::: info
테스트가 아직 실행되도록 스케줄되지 않았다면 `diagnostic()`은 `undefined`를 반환합니다.
:::

## annotations

```ts
function annotations(): ReadonlyArray<TestAnnotation>;
```

테스트 실행 중 [`task.annotate`](https://vitest.dev/guide/test-context#annotate) API를 통해 추가된 [Test annotations](https://vitest.dev/guide/test-annotations)입니다.

## artifacts 4.0.11 {#artifacts}

```ts
function artifacts(): ReadonlyArray<TestArtifact>;
```

테스트 실행 중 `recordArtifact` API를 통해 기록된 [Test artifacts](https://vitest.dev/api/advanced/artifacts)입니다.
니다.

## artifacts 4.0.11 {#artifacts}

```ts
function artifacts(): ReadonlyArray<TestArtifact>;
```

테스트 실행 중 `recordArtifact` API를 통해 기록된 [Test artifacts](https://vitest.dev/api/advanced/artifacts)입니다.
