---
title: "TestModule"
description: '클래스는 단일 프로젝트의 단일 모듈을 나타냅니다. 이 클래스는 메인 스레드에서만 사용할 수 있습니다. 런타임 task로 작업 중이라면 "Runner API"를 참고하세요.'
---

출처 URL: https://vitest.dev/api/advanced/test-module

# TestModule

`TestModule` 클래스는 단일 프로젝트의 단일 모듈을 나타냅니다. 이 클래스는 메인 스레드에서만 사용할 수 있습니다. 런타임 task로 작업 중이라면 ["Runner API"](https://vitest.dev/api/advanced/runner#tasks)를 참고하세요.

`TestModule` 인스턴스에는 항상 값이 `module`인 `type` 속성이 있습니다. 이를 사용해 서로 다른 task 타입을 구분할 수 있습니다:

```ts
if (task.type === "module") {
  task; // TestModule
}
```

::: warning Suite 메서드 확장
`TestModule` 클래스는 [`TestSuite`](https://vitest.dev/api/advanced/test-suite)의 모든 메서드와 속성을 상속합니다. 이 가이드에서는 `TestModule`에만 고유한 메서드와 속성만 나열합니다.
:::

## moduleId

일반적으로 절대 unix 파일 경로입니다(Windows에서도 동일). 파일이 디스크에 없으면 가상 id일 수 있습니다. 이 값은 Vite의 `ModuleGraph` id에 해당합니다.

```ts
"C:/Users/Documents/project/example.test.ts"; // ✅
"/Users/mac/project/example.test.ts"; // ✅
"C:\\Users\\Documents\\project\\example.test.ts"; // ❌
```

## relativeModuleId

프로젝트 기준의 상대 모듈 id입니다. 이는 deprecated API의 `task.name`과 동일합니다.

```ts
"project/example.test.ts"; // ✅
"example.test.ts"; // ✅
"project\\example.test.ts"; // ❌
```

## state

```ts
function state(): TestModuleState;
```

[`testSuite.state()`](https://vitest.dev/api/advanced/test-suite#state)와 동일하게 동작하지만, 모듈이 아직 실행되지 않았다면 `queued`를 반환할 수도 있습니다.

## meta 3.1.0 {#meta}

```ts
function meta(): TaskMeta;
```

실행 또는 수집 중 모듈에 첨부된 사용자 정의 [metadata](https://vitest.dev/api/advanced/metadata)입니다. 테스트 실행 중 `task.meta` 객체에 속성을 할당하여 meta를 첨부할 수 있습니다:

```ts {5,10}
import { test } from "vitest";

describe("the validation works correctly", (task) => {
  // assign "decorated" during collection
  task.file.meta.decorated = false;

  test("some test", ({ task }) => {
    // assign "decorated" during test run, it will be available
    // only in onTestCaseReady hook
    task.file.meta.decorated = false;
  });
});
```

:::tip
수집 단계(`test` 함수 외부)에서 metadata가 첨부되었다면, 커스텀 리포터의 [`onTestModuleCollected`](https://vitest.dev/api/advanced/reporters#ontestmodulecollected) 훅에서 사용할 수 있습니다.
:::

## diagnostic

```ts
function diagnostic(): ModuleDiagnostic;
```

지속 시간, 메모리 사용량 등 모듈에 대한 유용한 정보입니다. 모듈이 아직 실행되지 않았다면 모든 diagnostic 값은 `0`을 반환합니다.

```ts
interface ModuleDiagnostic {
  /**
   * The time it takes to import and initiate an environment.
   */
  readonly environmentSetupDuration: number;
  /**
   * The time it takes Vitest to setup test harness (runner, mocks, etc.).
   */
  readonly prepareDuration: number;
  /**
   * The time it takes to import the test module.
   * This includes importing everything in the module and executing suite callbacks.
   */
  readonly collectDuration: number;
  /**
   * The time it takes to import the setup module.
   */
  readonly setupDuration: number;
  /**
   * Accumulated duration of all tests and hooks in the module.
   */
  readonly duration: number;
  /**
   * The amount of memory used by the module in bytes.
   * This value is only available if the test was executed with `logHeapUsage` flag.
   */
  readonly heap: number | undefined;
  /**
   * The time spent importing every non-externalized dependency that Vitest has processed.
   */
  readonly importDurations: Record<string, ImportDuration>;
}

/** The time spent importing & executing a non-externalized file. */
interface ImportDuration {
  /** The time spent importing & executing the file itself, not counting all non-externalized imports that the file does. */
  selfTime: number;

  /** The time spent importing & executing the file and all its imports. */
  totalTime: number;
}
```

## viteEnvironment 4.0.15 {#viteenvironment}

이는 테스트 모듈 내부의 모든 파일을 변환하는 Vite의 [`DevEnvironment`](https://vite.dev/guide/api-environment)입니다.
