---
title: "Runner API 고급"
description: "이것은 고급 API입니다. 단순히 테스트를 실행하려는 경우에는 아마 필요하지 않을 것입니다. 주로 라이브러리 작성자를 위해 사용됩니다."
---

출처 URL: https://vitest.dev/api/advanced/runner

# Runner API 고급

::: warning
이것은 고급 API입니다. 단순히 [테스트를 실행](https://vitest.dev/guide/)하려는 경우에는 아마 필요하지 않을 것입니다. 주로 라이브러리 작성자를 위해 사용됩니다.
:::

구성 파일의 `runner` 옵션으로 테스트 러너 경로를 지정할 수 있습니다. 이 파일은 다음 메서드를 구현하는 클래스 생성자를 기본 export로 가져야 합니다:

```ts
export interface VitestRunner {
  /**
   * First thing that's getting called before actually collecting and running tests.
   */
  onBeforeCollect?: (paths: string[]) => unknown;
  /**
   * Called after collecting tests and before "onBeforeRun".
   */
  onCollected?: (files: File[]) => unknown;

  /**
   * Called when test runner should cancel next test runs.
   * Runner should listen for this method and mark tests and suites as skipped in
   * "onBeforeRunSuite" and "onBeforeRunTask" when called.
   */
  onCancel?: (reason: CancelReason) => unknown;

  /**
   * Called before running a single test. Doesn't have "result" yet.
   */
  onBeforeRunTask?: (test: Test) => unknown;
  /**
   * Called before actually running the test function. Already has "result" with "state" and "startTime".
   */
  onBeforeTryTask?: (
    test: Test,
    options: { retry: number; repeats: number },
  ) => unknown;
  /**
   * Called after result and state are set.
   */
  onAfterRunTask?: (test: Test) => unknown;
  /**
   * Called right after running the test function. Doesn't have new state yet. Will not be called, if the test function throws.
   */
  onAfterTryTask?: (
    test: Test,
    options: { retry: number; repeats: number },
  ) => unknown;
  /**
   * Called after the retry resolution happend. Unlike `onAfterTryTask`, the test now has a new state.
   * All `after` hooks were also called by this point.
   */
  onAfterRetryTask?: (
    test: Test,
    options: { retry: number; repeats: number },
  ) => unknown;

  /**
   * Called before running a single suite. Doesn't have "result" yet.
   */
  onBeforeRunSuite?: (suite: Suite) => unknown;
  /**
   * Called after running a single suite. Has state and result.
   */
  onAfterRunSuite?: (suite: Suite) => unknown;

  /**
   * If defined, will be called instead of usual Vitest suite partition and handling.
   * "before" and "after" hooks will not be ignored.
   */
  runSuite?: (suite: Suite) => Promise<void>;
  /**
   * If defined, will be called instead of usual Vitest handling. Useful, if you have your custom test function.
   * "before" and "after" hooks will not be ignored.
   */
  runTask?: (test: TaskPopulated) => Promise<void>;

  /**
   * Called, when a task is updated. The same as "onTaskUpdate" in a reporter, but this is running in the same thread as tests.
   */
  onTaskUpdate?: (
    task: [string, TaskResult | undefined, TaskMeta | undefined][],
  ) => Promise<void>;

  /**
   * Called before running all tests in collected paths.
   */
  onBeforeRunFiles?: (files: File[]) => unknown;
  /**
   * Called right after running all tests in collected paths.
   */
  onAfterRunFiles?: (files: File[]) => unknown;
  /**
   * Called when new context for a test is defined. Useful, if you want to add custom properties to the context.
   * If you only want to define custom context with a runner, consider using "beforeAll" in "setupFiles" instead.
   */
  extendTaskContext?: (context: TestContext) => TestContext;
  /**
   * Called when certain files are imported. Can be called in two situations: to collect tests and to import setup files.
   */
  importFile: (filepath: string, source: VitestRunnerImportSource) => unknown;
  /**
   * Function that is called when the runner attempts to get the value when `test.extend` is used with `{ injected: true }`
   */
  injectValue?: (key: string) => unknown;
  /**
   * Publicly available configuration.
   */
  config: VitestRunnerConfig;
  /**
   * The name of the current pool. Can affect how stack trace is inferred on the server side.
   */
  pool?: string;
}
```

이 클래스를 초기화할 때 Vitest는 Vitest config를 전달하므로, 이를 `config` 속성으로 노출해야 합니다:

```ts [runner.ts]
import type { RunnerTestFile } from "vitest";
import type { VitestRunner, VitestRunnerConfig } from "vitest/suite";
import { VitestTestRunner } from "vitest/runners";

class CustomRunner extends VitestTestRunner implements VitestRunner {
  public config: VitestRunnerConfig;

  constructor(config: VitestRunnerConfig) {
    this.config = config;
  }

  onAfterRunFiles(files: RunnerTestFile[]) {
    console.log("finished running", files);
  }
}

export default CustomRunner;
```

::: warning
Vitest는 또한 `vite/module-runner`의 `ModuleRunner` 인스턴스를 `moduleRunner` 속성으로 주입합니다. 이를 사용해 `importFile` 메서드에서 파일을 처리할 수 있습니다 (`TestRunner`와 `BenchmarkRunner`의 기본 동작입니다).

`ModuleRunner`는 `import` 메서드를 노출하며, 이 메서드는 Vite 친화적인 환경에서 테스트 파일을 import하는 데 사용됩니다. 즉, Node가 이해할 수 있도록 import를 해석하고 런타임에 파일 내용을 변환합니다:

```ts
export default class Runner {
  async importFile(filepath: string) {
    await this.moduleRunner.import(filepath);
  }
}
```

:::

::: warning
사용자 정의 runner가 없거나 `runTest` 메서드를 정의하지 않았다면, Vitest는 task를 자동으로 가져오려고 시도합니다. `setFn`으로 함수를 추가하지 않았다면 실패합니다.
:::

::: tip
스냅샷 지원과 일부 다른 기능은 runner에 의존합니다. 이를 잃고 싶지 않다면 `vitest/runners`에서 import한 `VitestTestRunner`를 상속해 runner를 확장할 수 있습니다. 벤치마크 기능을 확장하고 싶다면 `NodeBenchmarkRunner`도 제공합니다.
:::

## Tasks

::: warning
"Runner Tasks API"는 실험적이며, 주로 테스트 런타임에서만 사용해야 합니다. Vitest는 ["Reported Tasks API"](https://vitest.dev/api/advanced/test-module)도 제공하며, 메인 스레드에서 작업할 때(예: reporter 내부) 이것을 우선 사용하는 것이 좋습니다.

팀에서는 현재 향후 "Runner Tasks"를 "Reported Tasks"로 대체해야 할지 논의 중입니다.
:::

내부적으로 suite와 test는 `tasks`라고 불립니다. Vitest runner는 테스트를 수집하기 전에 `File` task를 초기화하며, 이는 몇 가지 추가 속성을 가진 `Suite`의 상위 집합입니다. 이는 모든 task(`File` 포함)에서 `file` 속성으로 사용할 수 있습니다.

```ts
interface File extends Suite {
  /**
   * The name of the pool that the file belongs to.
   * @default 'forks'
   */
  pool?: string;
  /**
   * The path to the file in UNIX format.
   */
  filepath: string;
  /**
   * The name of the test project the file belongs to.
   */
  projectName: string | undefined;
  /**
   * The time it took to collect all tests in the file.
   * This time also includes importing all the file dependencies.
   */
  collectDuration?: number;
  /**
   * The time it took to import the setup file.
   */
  setupDuration?: number;
}
```

모든 suite에는 수집 단계에서 채워지는 `tasks` 속성이 있습니다. task 트리를 위에서 아래로 순회할 때 유용합니다.

```ts
interface Suite extends TaskBase {
  type: "suite";
  /**
   * File task. It's the root task of the file.
   */
  file: File;
  /**
   * An array of tasks that are part of the suite.
   */
  tasks: Task[];
}
```

모든 task에는 자신이 속한 suite를 참조하는 `suite` 속성이 있습니다. `test` 또는 `describe`가 최상위 레벨에서 초기화되면 `suite` 속성이 없습니다 (`file`과 **같지 않습니다**!). 또한 `File`에는 절대 `suite` 속성이 없습니다. task를 아래에서 위로 순회할 때 유용합니다.

```ts
interface Test<ExtraContext = object> extends TaskBase {
  type: "test";
  /**
   * Test context that will be passed to the test function.
   */
  context: TestContext & ExtraContext;
  /**
   * File task. It's the root task of the file.
   */
  file: File;
  /**
   * Whether the task was skipped by calling `context.skip()`.
   */
  pending?: boolean;
  /**
   * Whether the task should succeed if it fails. If the task fails, it will be marked as passed.
   */
  fails?: boolean;
  /**
   * Store promises (from async expects) to wait for them before finishing the test
   */
  promises?: Promise<any>[];
}
```

모든 task는 `result` 필드를 가질 수 있습니다. suite는 suite 콜백 또는 `beforeAll`/`afterAll` 콜백에서 발생한 오류로 인해 테스트 수집이 막힌 경우에만 이 필드를 가질 수 있습니다. test는 콜백이 호출된 후에는 항상 이 필드를 가지며, 결과에 따라 `state`와 `errors` 필드가 존재합니다. `beforeEach` 또는 `afterEach` 콜백에서 오류가 발생했다면, 발생한 오류는 `task.result.errors`에 포함됩니다.

```ts
export interface TaskResult {
  /**
   * State of the task. Inherits the `task.mode` during collection.
   * When the task has finished, it will be changed to `pass` or `fail`.
   * - **pass**: task ran successfully
   * - **fail**: task failed
   */
  state: TaskState;
  /**
   * Errors that occurred during the task execution. It is possible to have several errors
   * if `expect.soft()` failed multiple times.
   */
  errors?: TestError[];
  /**
   * How long in milliseconds the task took to run.
   */
  duration?: number;
  /**
   * Time in milliseconds when the task started running.
   */
  startTime?: number;
  /**
   * Heap size in bytes after the task finished.
   * Only available if `logHeapUsage` option is set and `process.memoryUsage` is defined.
   */
  heap?: number;
  /**
   * State of related to this task hooks. Useful during reporting.
   */
  hooks?: Partial<
    Record<"afterAll" | "beforeAll" | "beforeEach" | "afterEach", TaskState>
  >;
  /**
   * The amount of times the task was retried. The task is retried only if it
   * failed and `retry` option is set.
   */
  retryCount?: number;
  /**
   * The amount of times the task was repeated. The task is repeated only if
   * `repeats` option is set. This number also contains `retryCount`.
   */
  repeatCount?: number;
}
```

## Your Task Function

Vitest는 자체 `test` 메서드를 만들 수 있도록 `createTaskCollector` 유틸리티를 제공합니다. 동작 방식은 test와 같지만, 수집 중에 사용자 정의 메서드를 호출합니다.

task는 suite의 일부인 객체입니다. `suite.task` 메서드를 통해 현재 suite에 자동으로 추가됩니다:

```js [custom.js]
import { createTaskCollector, getCurrentSuite } from "vitest/suite";

export { afterAll, beforeAll, describe } from "vitest";

// this function will be called during collection phase:
// don't call function handler here, add it to suite tasks
// with "getCurrentSuite().task()" method
// note: createTaskCollector provides support for "todo"/"each"/...
export const myCustomTask = createTaskCollector(function (name, fn, timeout) {
  getCurrentSuite().task(name, {
    ...this, // so "todo"/"skip"/... is tracked correctly
    meta: {
      customPropertyToDifferentiateTask: true,
    },
    handler: fn,
    timeout,
  });
});
```

```js [tasks.test.js]
import { afterAll, beforeAll, describe, myCustomTask } from "./custom.js";
import { gardener } from "./gardener.js";

describe("take care of the garden", () => {
  beforeAll(() => {
    gardener.putWorkingClothes();
  });

  myCustomTask("weed the grass", () => {
    gardener.weedTheGrass();
  });
  myCustomTask.todo("mow the lawn", () => {
    gardener.mowerTheLawn();
  });
  myCustomTask("water flowers", () => {
    gardener.waterFlowers();
  });

  afterAll(() => {
    gardener.goHome();
  });
});
```

```bash
vitest ./garden/tasks.test.js
```

sk.todo('mow the lawn', () => {
gardener.mowerTheLawn()
})
myCustomTask('water flowers', () => {
gardener.waterFlowers()
})

afterAll(() => {
gardener.goHome()
})
})

````

```bash
vitest ./garden/tasks.test.js
````
