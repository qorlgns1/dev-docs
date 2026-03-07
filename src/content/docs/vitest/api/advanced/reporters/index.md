---
title: "Reporters"
description: '이것은 고급 API입니다. 내장 리포터를 설정하려는 목적이라면 "Reporters" 가이드를 읽어보세요.'
---

출처 URL: https://vitest.dev/api/advanced/reporters

# Reporters

::: warning
이것은 고급 API입니다. 내장 리포터를 설정하려는 목적이라면 ["Reporters"](https://vitest.dev/guide/reporters) 가이드를 읽어보세요.
:::

Vitest에는 자체 테스트 실행 생명주기가 있습니다. 이는 리포터 메서드로 표현됩니다.

- [`onInit`](#oninit)
- [`onTestRunStart`](#ontestrunstart)
  - [`onTestModuleQueued`](#ontestmodulequeued)
  - [`onTestModuleCollected`](#ontestmodulecollected)
  - [`onTestModuleStart`](#ontestmodulestart)
    - [`onTestSuiteReady`](#ontestsuiteready)
      - [`onHookStart(beforeAll)`](#onhookstart)
      - [`onHookEnd(beforeAll)`](#onhookend)
        - [`onTestCaseReady`](#ontestcaseready)
          - [`onTestAnnotate`](#ontestannotate) 3.2.0
          - [`onTestCaseArtifactRecord`](#ontestcaseartifactrecord) 4.0.11
          - [`onHookStart(beforeEach)`](#onhookstart)
          - [`onHookEnd(beforeEach)`](#onhookend)
          - [`onHookStart(afterEach)`](#onhookstart)
          - [`onHookEnd(afterEach)`](#onhookend)
        - [`onTestCaseResult`](#ontestcaseresult)
      - [`onHookStart(afterAll)`](#onhookstart)
      - [`onHookEnd(afterAll)`](#onhookend)
    - [`onTestSuiteResult`](#ontestsuiteresult)
  - [`onTestModuleEnd`](#ontestmoduleend)
  - [`onCoverage`](#oncoverage)
- [`onTestRunEnd`](#ontestrunend)

단일 모듈 내의 테스트와 스위트는 skip되지 않은 한 순서대로 보고됩니다. skip된 모든 테스트는 스위트/모듈의 마지막에 보고됩니다.

테스트 모듈은 병렬로 실행될 수 있으므로, Vitest도 이를 병렬로 보고한다는 점에 유의하세요.

이 가이드는 지원되는 모든 리포터 메서드를 나열합니다. 다만 자체 리포터를 만드는 대신 [기존 리포터를 확장](https://vitest.dev/guide/advanced/reporters)할 수도 있다는 점을 잊지 마세요.

```ts [custom-reporter.js]
import { BaseReporter } from "vitest/reporters";

export default class CustomReporter extends BaseReporter {
  onTestRunEnd(testModules, errors) {
    console.log(testModule.length, "tests finished running");
    super.onTestRunEnd(testModules, errors);
  }
}
```

## onInit

```ts
function onInit(vitest: Vitest): Awaitable<void>;
```

이 메서드는 [Vitest](https://vitest.dev/api/advanced/vitest)가 초기화되거나 시작되었지만 테스트가 필터링되기 전에 호출됩니다.

::: info
내부적으로 이 메서드는 [`vitest.start`](https://vitest.dev/api/advanced/vitest#start), [`vitest.init`](https://vitest.dev/api/advanced/vitest#init), [`vitest.mergeReports`](https://vitest.dev/api/advanced/vitest#mergereports) 내부에서 호출됩니다. 예를 들어 programmatic API를 사용 중이라면 필요에 따라 이들 중 하나를 [`vitest.runTestSpecifications`](https://vitest.dev/api/advanced/vitest#runtestspecifications) 호출 전에 먼저 호출해야 합니다. 내장 CLI는 항상 올바른 순서로 메서드를 실행합니다.
:::

테스트 케이스, 스위트, 테스트 모듈에서도 [`project`](https://vitest.dev/api/advanced/test-project) 속성을 통해 `vitest` 인스턴스에 접근할 수 있지만, 이 메서드에서 `vitest` 참조를 저장해 두는 것도 유용할 수 있습니다.

::: details 예시

```ts
import type { Reporter, TestSpecification, Vitest } from "vitest/node";

class MyReporter implements Reporter {
  private vitest!: Vitest;

  onInit(vitest: Vitest) {
    this.vitest = vitest;
  }

  onTestRunStart(specifications: TestSpecification[]) {
    console.log(
      specifications.length,
      "test files will run in",
      this.vitest.config.root,
    );
  }
}

export default new MyReporter();
```

:::

## onBrowserInit {#onbrowserinit}

```ts
function onBrowserInit(project: TestProject): Awaitable<void>;
```

이 메서드는 브라우저 인스턴스가 초기화될 때 호출됩니다. 브라우저가 초기화되는 대상 project 인스턴스를 인자로 받습니다. 이 메서드가 호출될 때 `project.browser`는 항상 정의되어 있습니다.

## onTestRunStart

```ts
function onTestRunStart(specifications: TestSpecification[]): Awaitable<void>;
```

이 메서드는 새 테스트 실행이 시작될 때 호출됩니다. 실행 예정인 [test specifications](https://vitest.dev/api/advanced/test-specification) 배열을 인자로 받습니다. 이 배열은 readonly이며 정보 제공 목적에서만 사용할 수 있습니다.

Vitest가 실행할 테스트 파일을 찾지 못한 경우, 이 이벤트는 빈 배열과 함께 호출되고 직후 [`onTestRunEnd`](#ontestrunend)가 호출됩니다.

::: details 예시

```ts
import type { Reporter, TestSpecification } from "vitest/node";

class MyReporter implements Reporter {
  onTestRunStart(specifications: TestSpecification[]) {
    console.log(specifications.length, "test files will run");
  }
}

export default new MyReporter();
```

:::

::: tip DEPRECATION NOTICE
이 메서드는 Vitest 3에서 추가되었으며, 현재 deprecated된 `onPathsCollected`와 `onSpecsCollected`를 대체합니다.
:::

## onTestRunEnd

```ts
function onTestRunEnd(
  testModules: ReadonlyArray<TestModule>,
  unhandledErrors: ReadonlyArray<SerializedError>,
  reason: TestRunEndReason,
): Awaitable<void>;
```

이 메서드는 모든 테스트 실행이 완료되고(활성화된 경우) 커버리지가 모든 리포트를 병합한 뒤 호출됩니다. 커버리지 정보는 [`onCoverage`](#oncoverage) 훅에서 얻을 수 있습니다.

이 메서드는 테스트 모듈의 readonly 목록을 받습니다. 필요하다면 [`testModule.children`](https://vitest.dev/api/advanced/test-collection) 속성을 통해 상태와 오류를 보고할 수 있습니다.

두 번째 인자는 Vitest가 어떤 테스트에도 귀속시키지 못한 처리되지 않은 오류(unhandled errors)의 readonly 목록입니다. 이는 플러그인 오류로 인해 테스트 실행 외부에서 발생하거나, await되지 않은 함수의 부작용으로 테스트 실행 내부에서 발생할 수 있습니다(예: 테스트가 끝난 뒤 에러를 던진 timeout).

세 번째 인자는 테스트 실행이 종료된 이유를 나타냅니다.

- `passed`: 테스트 실행이 정상 종료되었고 오류가 없음
- `failed`: 테스트 실행에 하나 이상의 오류가 있음(수집 중 문법 오류 또는 테스트 실행 중 실제 오류)
- `interrupted`: [`vitest.cancelCurrentRun`](https://vitest.dev/api/advanced/vitest#cancelcurrentrun) 호출 또는 터미널에서 `Ctrl+C` 입력으로 테스트가 중단됨(이 경우에도 실패한 테스트가 있을 수 있음)

Vitest가 실행할 테스트 파일을 찾지 못한 경우, 이 이벤트는 모듈/오류가 빈 배열인 상태로 호출되며 상태는 [`config.passWithNoTests`](https://vitest.dev/config/#passwithnotests) 값에 따라 달라집니다.

::: details 예시

```ts
import type {
  Reporter,
  SerializedError,
  TestModule,
  TestRunEndReason,
  TestSpecification,
} from "vitest/node";

class MyReporter implements Reporter {
  onTestRunEnd(
    testModules: ReadonlyArray<TestModule>,
    unhandledErrors: ReadonlyArray<SerializedError>,
    reason: TestRunEndReason,
  ) {
    if (reason === "passed") {
      testModules.forEach((module) =>
        console.log(module.moduleId, "succeeded"),
      );
    } else if (reason === "failed") {
      // note that this will skip possible errors in suites
      // you can get them from testSuite.errors()
      for (const testCase of testModules.children.allTests()) {
        if (testCase.result().state === "failed") {
          console.log(
            testCase.fullName,
            "in",
            testCase.module.moduleId,
            "failed",
          );
          console.log(testCase.result().errors);
        }
      }
    } else {
      console.log("test run was interrupted, skipping report");
    }
  }
}

export default new MyReporter();
```

:::

::: tip DEPRECATION NOTICE
이 메서드는 Vitest 3에서 추가되었으며, 현재 deprecated된 `onFinished`를 대체합니다.
:::

## onCoverage

```ts
function onCoverage(coverage: unknown): Awaitable<void>;
```

이 훅은 커버리지 결과 처리가 끝난 뒤 호출됩니다. 커버리지 provider의 리포터는 이 훅 이후에 호출됩니다. `coverage`의 타입은 `coverage.provider`에 따라 달라집니다. Vitest의 기본 내장 provider를 사용하는 경우 `istanbul-lib-coverage` 패키지에서 타입을 import할 수 있습니다.

```ts
import type { CoverageMap } from "istanbul-lib-coverage";

declare function onCoverage(coverage: CoverageMap): Awaitable<void>;
```

Vitest가 커버리지를 수행하지 않은 경우 이 훅은 호출되지 않습니다.

## onTestModuleQueued

```ts
function onTestModuleQueued(testModule: TestModule): Awaitable<void>;
```

이 메서드는 Vitest가 setup 파일과 테스트 모듈 자체를 import하기 직전에 호출됩니다. 즉, 이 시점의 `testModule`에는 아직 [`children`](https://vitest.dev/api/advanced/test-suite#children)이 없지만, 다음에 실행될 테스트로 보고를 시작할 수 있습니다.

## onTestModuleCollected

```ts
function onTestModuleCollected(testModule: TestModule): Awaitable<void>;
```

이 메서드는 파일 내부의 모든 테스트 수집이 완료되었을 때 호출됩니다. 즉, [`testModule.children`](https://vitest.dev/api/advanced/test-suite#children) 컬렉션은 채워졌지만 테스트 결과는 아직 없습니다.

## onTestModuleStart

```ts
function onTestModuleStart(testModule: TestModule): Awaitable<void>;
```

이 메서드는 Vitest가 수집 모드([`vitest.collect()`](https://vitest.dev/api/advanced/vitest#collect) 또는 CLI의 `vitest collect`)로 실행되는 경우를 제외하고 [`onTestModuleCollected`](#ontestmodulecollected) 직후 호출됩니다. 수집 모드에서는 실행할 테스트가 없으므로 전혀 호출되지 않습니다.

## onTestModuleEnd

```ts
function onTestModuleEnd(testModule: TestModule): Awaitable<void>;
```

이 메서드는 모듈 내 모든 테스트 실행이 끝났을 때 호출됩니다. 즉, [`testModule.children`](https://vitest.dev/api/advanced/test-suite#children) 내부의 모든 테스트에서 `test.result()`가 `pending`이 아닌 상태가 됩니다.

## onHookStart

```ts
function onHookStart(context: ReportedHookContext): Awaitable<void>;
```

이 메서드는 다음 훅 중 하나의 실행이 시작될 때 호출됩니다.

- `beforeAll`
- `afterAll`
- `beforeEach`
- `afterEach`

`beforeAll` 또는 `afterAll`이 시작되면 `entity`는 [`TestSuite`](https://vitest.dev/api/advanced/test-suite) 또는 [`TestModule`](https://vitest.dev/api/advanced/test-module)입니다.

`beforeEach` 또는 `afterEach`가 시작되면 `entity`는 항상 [`TestCase`](https://vitest.dev/api/advanced/test-case)입니다.

::: warning
`onHookStart` 메서드는 테스트 실행 중 해당 훅이 실행되지 않았다면 호출되지 않습니다.
:::

## onHookEnd

```ts
function onHookEnd(context: ReportedHookContext): Awaitable<void>;
```

이 메서드는 다음 훅 중 하나의 실행이 끝났을 때 호출됩니다.

- `beforeAll`
- `afterAll`
- `beforeEach`
- `afterEach`

`beforeAll` 또는 `afterAll`이 끝나면 `entity`는 [`TestSuite`](https://vitest.dev/api/advanced/test-suite) 또는 [`TestModule`](https://vitest.dev/api/advanced/test-module)입니다.

`beforeEach` 또는 `afterEach`가 끝나면 `entity`는 항상 [`TestCase`](https://vitest.dev/api/advanced/test-case)입니다.

::: warning
`onHookEnd` 메서드는 테스트 실행 중 해당 훅이 실행되지 않았다면 호출되지 않습니다.
:::

## onTestSuiteReady

```ts
function onTestSuiteReady(testSuite: TestSuite): Awaitable<void>;
```

이 메서드는 스위트가 테스트 실행을 시작하기 전에 호출됩니다. 스위트가 skip된 경우에도 이 메서드는 호출됩니다.

파일에 스위트가 하나도 없으면 이 메서드는 호출되지 않습니다. 이 경우를 다루려면 `onTestModuleStart` 사용을 고려하세요.

## onTestSuiteResult

```ts
function onTestSuiteResult(testSuite: TestSuite): Awaitable<void>;
```

이 메서드는 스위트의 테스트 실행이 끝난 뒤 호출됩니다. 스위트가 skip된 경우에도 이 메서드는 호출됩니다.

파일에 스위트가 하나도 없으면 이 메서드는 호출되지 않습니다. 이 경우를 다루려면 `onTestModuleEnd` 사용을 고려하세요.

## onTestCaseReady

```ts
function onTestCaseReady(testCase: TestCase): Awaitable<void>;
```

이 메서드는 테스트 실행이 시작되기 전 또는 테스트가 skip되었을 때 호출됩니다. `beforeEach`와 `afterEach` 훅은 결과에 영향을 줄 수 있으므로 테스트의 일부로 간주됩니다.

::: warning
`onTestCaseReady`가 호출될 때 이미 [`testCase.result()`](https://vitest.dev/api/advanced/test-case#result)이 `passed` 또는 `failed` 상태일 수 있다는 점에 유의하세요. 테스트가 매우 빠르게 실행된 경우 `onTestCaseReady`와 `onTestCaseResult`가 동일한 microtask에서 실행되도록 예약될 수 있기 때문입니다.
:::

## onTestCaseResult

```ts
function onTestCaseResult(testCase: TestCase): Awaitable<void>;
```

이 메서드는 테스트 실행이 끝났거나 테스트가 skip되었을 때 호출됩니다. `afterEach` 훅이 있다면 해당 훅이 끝난 뒤에 호출됩니다.

이 시점에서 [`testCase.result()`](https://vitest.dev/api/advanced/test-case#result)은 non-pending 상태입니다.

## onTestAnnotate 3.2.0 {#ontestannotate}

```ts
function onTestAnnotate(
  testCase: TestCase,
  annotation: TestAnnotation,
): Awaitable<void>;
```

`onTestAnnotate` 훅은 [`context.annotate`](https://vitest.dev/guide/test-context#annotate) 메서드와 연관되어 있습니다. `annotate`가 호출되면 Vitest가 이를 직렬화하여 메인 스레드로 같은 첨부를 전송하고, 리포터는 이를 상호작용할 수 있습니다.

경로가 지정된 경우 Vitest는 이를 별도 디렉터리([`attachmentsDir`](https://vitest.dev/config/#attachmentsdir)로 설정)에 저장하고 `path` 속성을 해당 경로를 참조하도록 수정합니다.

## onTestCaseArtifactRecord 4.0.11 {#ontestcaseartifactrecord}

```ts
function onTestCaseArtifactRecord(
  testCase: TestCase,
  artifact: TestArtifact,
): Awaitable<void>;
```

`onTestCaseArtifactRecord` 훅은 [`recordArtifact`](https://vitest.dev/api/advanced/artifacts#recordartifact) 유틸리티와 연관되어 있습니다. `recordArtifact`가 호출되면 Vitest가 이를 직렬화하여 메인 스레드로 같은 첨부를 전송하고, 리포터는 이를 상호작용할 수 있습니다.

경로가 지정된 경우 Vitest는 이를 별도 디렉터리([`attachmentsDir`](https://vitest.dev/config/#attachmentsdir)로 설정)에 저장하고 `path` 속성을 해당 경로를 참조하도록 수정합니다.

참고: annotations는 [이 기능 위에 구축되어 있음에도](https://vitest.dev/api/advanced/artifacts#relationship-with-annotations), 하위 호환성 이유로 다음 메이저 버전 전까지는 이 훅을 거치지 않으며 `task.artifacts` 배열에도 나타나지 않습니다.
ith-annotations), 하위 호환성 이유로 다음 메이저 버전 전까지는 이 훅을 거치지 않으며 `task.artifacts` 배열에도 나타나지 않습니다.
