---
title: "TestSuite"
description: '클래스는 단일 suite를 나타냅니다. 이 클래스는 메인 스레드에서만 사용할 수 있습니다. 런타임 task를 다루는 경우 "Runner API"를 참고하세요.'
---

출처 URL: https://vitest.dev/api/advanced/test-suite

# TestSuite

`TestSuite` 클래스는 단일 suite를 나타냅니다. 이 클래스는 메인 스레드에서만 사용할 수 있습니다. 런타임 task를 다루는 경우 ["Runner API"](https://vitest.dev/api/advanced/runner#tasks)를 참고하세요.

`TestSuite` 인스턴스는 항상 값이 `suite`인 `type` 속성을 가집니다. 이를 사용해 서로 다른 task 타입을 구분할 수 있습니다.

```ts
if (task.type === "suite") {
  task; // TestSuite
}
```

## project

이 테스트가 속한 [`TestProject`](https://vitest.dev/api/advanced/test-project)를 참조합니다.

## module

테스트가 정의된 [`TestModule`](https://vitest.dev/api/advanced/test-module)을 직접 참조합니다.

## name

`describe` 함수에 전달된 suite 이름입니다.

```ts
import { describe } from "vitest";

// [!code word:'the validation logic']
describe("the validation logic", () => {
  // ...
});
```

## fullName

모든 상위 suite 이름을 `>` 기호로 구분해 포함한 suite 이름입니다. 이 suite의 전체 이름은 "the validation logic > validating cities"입니다.

```ts
import { describe, test } from "vitest";

// [!code word:'the validation logic']
// [!code word:'validating cities']
describe("the validation logic", () => {
  describe("validating cities", () => {
    // ...
  });
});
```

## id

suite의 고유 식별자입니다. 이 ID는 결정론적이므로 동일한 suite에 대해 여러 번 실행해도 동일합니다. ID는 [project](https://vitest.dev/api/advanced/test-project) 이름, module ID, suite 순서를 기반으로 합니다.

ID는 다음과 같은 형태입니다.

```
1223128da3_0_0_0
^^^^^^^^^^ the file hash
           ^ suite index
             ^ nested suite index
               ^ test index
```

::: tip
Vitest 3부터는 `vitest/node`의 `generateFileHash` 함수를 사용해 파일 해시를 생성할 수 있습니다.

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

suite가 정의된 module 내 위치입니다. 위치 정보는 설정에서 [`includeTaskLocation`](https://vitest.dev/config/#includetasklocation)이 활성화된 경우에만 수집됩니다. 이 옵션은 `--reporter=html`, `--ui`, `--browser` 플래그를 사용할 때 자동으로 활성화됩니다.

이 suite의 위치는 `{ line: 3, column: 1 }`와 같습니다.

```ts:line-numbers {3}
import { describe } from 'vitest'

describe('the validation works correctly', () => {
  // ...
})
```

## parent

부모 suite입니다. [module](https://vitest.dev/api/advanced/test-module) 내부에서 suite가 직접 호출된 경우, 부모는 module 자체가 됩니다.

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

suite가 수집될 때 사용된 옵션입니다.

## children

현재 suite 내부의 모든 suite와 test에 대한 [collection](https://vitest.dev/api/advanced/test-collection)입니다.

```ts
for (const task of suite.children) {
  if (task.type === "test") {
    console.log("test", task.fullName);
  } else {
    // task is TaskSuite
    console.log("suite", task.name);
  }
}
```

::: warning
`suite.children`은 첫 번째 중첩 레벨만 순회하며, 더 깊은 레벨까지는 내려가지 않습니다. 모든 test 또는 suite를 순회해야 한다면 [`children.allTests()`](https://vitest.dev/api/advanced/test-collection#alltests) 또는 [`children.allSuites()`](https://vitest.dev/api/advanced/test-collection#allsuites)를 사용하세요. 전체를 순회해야 한다면 재귀 함수를 사용하세요.

```ts
function visit(collection: TestCollection) {
  for (const task of collection) {
    if (task.type === "suite") {
      // report a suite
      visit(task.children);
    } else {
      // report a test
    }
  }
}
```

:::

## ok

```ts
function ok(): boolean;
```

suite에 실패한 테스트가 있는지 확인합니다. 수집 중 suite가 실패한 경우에도 `false`를 반환합니다. 이 경우 발생한 오류는 [`errors()`](#errors)에서 확인하세요.

## state

```ts
function state(): TestSuiteState;
```

suite의 실행 상태를 확인합니다. 가능한 반환값은 다음과 같습니다.

- **pending**: 이 suite의 테스트가 아직 실행을 마치지 않았습니다.
- **failed**: 이 suite에 실패한 테스트가 있거나 테스트를 수집하지 못했습니다. [`errors()`](#errors)가 비어 있지 않다면 테스트 수집에 실패했다는 의미입니다.
- **passed**: 이 suite 내부의 모든 테스트가 통과했습니다.
- **skipped**: 이 suite는 수집 중 건너뛰어졌습니다.

::: warning
[test module](https://vitest.dev/api/advanced/test-module)에도 동일한 값을 반환하는 `state` 메서드가 있습니다. 다만 module이 아직 실행되지 않은 경우 추가로 `queued` 상태를 반환할 수 있습니다.
:::

## errors

```ts
function errors(): TestError[];
```

구문 오류처럼 테스트 실행이 아닌 수집 단계에서 발생한 오류입니다.

```ts {4}
import { describe } from "vitest";

describe("collection failed", () => {
  throw new Error("a custom error");
});
```

::: warning
오류는 단순 객체로 직렬화됩니다. 따라서 `instanceof Error`는 항상 `false`를 반환합니다.
:::

## meta 3.1.0 {#meta}

```ts
function meta(): TaskMeta;
```

실행 또는 수집 중 suite에 첨부된 사용자 정의 [metadata](https://vitest.dev/api/advanced/metadata)입니다. 테스트 실행 중 `suite.meta` 객체에 속성을 할당해 meta를 첨부할 수 있습니다.

```ts {7,12}
import { test } from "vitest";
import { getCurrentSuite } from "vitest/suite";

describe("the validation works correctly", () => {
  // assign "decorated" during collection
  const { suite } = getCurrentSuite();
  suite!.meta.decorated = true;

  test("some test", ({ task }) => {
    // assign "decorated" during test run, it will be available
    // only in onTestCaseReady hook
    task.suite.meta.decorated = false;
  });
});
```

:::tip
metadata가 수집 단계(`test` 함수 외부)에서 첨부되었다면, 커스텀 reporter의 [`onTestModuleCollected`](https://vitest.dev/api/advanced/reporters#ontestmodulecollected) 훅에서 사용할 수 있습니다.
:::
