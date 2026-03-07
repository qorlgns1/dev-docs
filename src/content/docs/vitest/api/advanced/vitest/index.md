---
title: "Vitest"
description: "Vitest 인스턴스에는 현재 테스트 모드가 필요합니다. 가능한 모드는 다음과 같습니다:"
---

출처 URL: https://vitest.dev/api/advanced/vitest

# Vitest

Vitest 인스턴스에는 현재 테스트 모드가 필요합니다. 가능한 모드는 다음과 같습니다:

- 런타임 테스트를 실행할 때 `test`
- 벤치마크 experimental을 실행할 때 `benchmark`

::: details Vitest 4의 새로운 내용
Vitest 4에서는 여러 새로운 API를 추가했고(이들은 "4.0.0+" 배지로 표시됨), 더 이상 권장되지 않던 API를 제거했습니다:

- `invalidates`
- `changedTests` ([`onFilterWatchedSpecification`](#onfilterwatchedspecification) 사용)
- `server` ([`vite`](#vite) 사용)
- `getProjectsByTestFile` ([`getModuleSpecifications`](#getmodulespecifications) 사용)
- `getFileWorkspaceSpecs` ([`getModuleSpecifications`](#getmodulespecifications) 사용)
- `getModuleProjects` ([`this.projects`](#projects)로 직접 필터링)
- `updateLastChanged` ([`invalidateFile`](#invalidatefile)로 이름 변경)
- `globTestSpecs` ([`globTestSpecifications`](#globtestspecifications) 사용)
- `globTestFiles` ([`globTestSpecifications`](#globtestspecifications) 사용)
- `listFile` ([`getRelevantTestSpecifications`](#getrelevanttestspecifications) 사용)
  :::

## mode

### test

테스트 모드에서는 `test` 또는 `it` 내부의 함수만 호출하며, `bench`를 만나면 오류를 발생시킵니다. 이 모드는 테스트 파일을 찾기 위해 config의 `include` 및 `exclude` 옵션을 사용합니다.

### benchmark experimental

벤치마크 모드는 `bench` 함수를 호출하고, `test` 또는 `it`를 만나면 오류를 발생시킵니다. 이 모드는 벤치마크 파일을 찾기 위해 config의 `benchmark.include` 및 `benchmark.exclude` 옵션을 사용합니다.

## config

루트(또는 전역) config입니다. projects가 정의되어 있으면 이를 `globalConfig`로 참조합니다.

::: warning
이것은 Vitest config이며, _Vite_ config를 확장하지 않습니다. `test` 속성에서 해석된 값만 포함합니다.
:::

## vite

전역 [`ViteDevServer`](https://vite.dev/guide/api-javascript#vitedevserver)입니다.

## state experimental

::: warning
공개 `state`는 실험적 API입니다(`vitest.state.getReportedEntity` 제외). 호환성이 깨지는 변경이 SemVer를 따르지 않을 수 있으므로, 사용할 때는 Vitest 버전을 고정하세요.
:::

전역 state는 현재 테스트에 대한 정보를 저장합니다. 기본적으로 `@vitest/runner`의 동일한 API를 사용하지만, `@vitest/runner` API에서 `state.getReportedEntity()`를 호출해 [Reported Tasks API](https://vitest.dev/api/advanced/reporters#reported-tasks)를 사용하는 것을 권장합니다:

```ts
const task = vitest.state.idMap.get(taskId); // old API
const testCase = vitest.state.getReportedEntity(task); // new API
```

향후에는 기존 API가 더 이상 노출되지 않습니다.

## snapshot

전역 스냅샷 매니저입니다. Vitest는 `snapshot.add` 메서드를 사용해 모든 스냅샷을 추적합니다.

`vitest.snapshot.summary` 속성으로 최신 스냅샷 요약을 가져올 수 있습니다.

## cache

최신 테스트 결과와 테스트 파일 통계를 저장하는 캐시 매니저입니다. Vitest 자체에서는 기본 시퀀서가 테스트를 정렬할 때만 사용됩니다.

## watcher 4.0.0 {#watcher}

파일 변경을 추적하고 테스트를 다시 실행하는 데 유용한 메서드를 제공하는 Vitest watcher 인스턴스입니다. 내장 watcher가 비활성화된 경우, 자체 watcher와 함께 `onFileChange`, `onFileDelete`, `onFileCreate`를 사용할 수 있습니다.

## projects

사용자 프로젝트에 속한 [test projects](https://vitest.dev/api/advanced/test-project) 배열입니다. 사용자가 이를 지정하지 않으면, 이 배열에는 [root project](#getrootproject)만 포함됩니다.

Vitest는 이 배열에 항상 최소 하나의 project가 있도록 보장합니다. 사용자가 존재하지 않는 `--project` 이름을 지정하면, 이 배열이 정의되기 전에 Vitest가 오류를 발생시킵니다.

## getRootProject

```ts
function getRootProject(): TestProject;
```

루트 테스트 project를 반환합니다. 루트 project는 일반적으로 어떤 테스트도 실행하지 않으며, 사용자가 설정에서 루트 config를 명시적으로 포함하거나 projects가 전혀 정의되지 않은 경우가 아니면 `vitest.projects`에 포함되지 않습니다.

루트 project의 주된 목적은 전역 config를 설정하는 것입니다. 실제로 `rootProject.config`는 `rootProject.globalConfig`와 `vitest.config`를 직접 참조합니다:

```ts
(rootProject.config === rootProject.globalConfig) === rootProject.vitest.config;
```

## provide

```ts
function provide<T extends keyof ProvidedContext & string>(
  key: T,
  value: ProvidedContext[T],
): void;
```

Vitest는 `vitest.getRootProject().provide`의 단축 메서드인 `provide`를 제공합니다. 이 메서드로 메인 스레드의 값을 테스트로 전달할 수 있습니다. 저장 전에 모든 값은 `structuredClone`으로 검사되지만, 값 자체가 복제되지는 않습니다.

테스트에서 값을 받으려면 `vitest` 엔트리포인트에서 `inject` 메서드를 import해야 합니다:

```ts
import { inject } from "vitest";
const port = inject("wsPort"); // 3000
```

더 나은 타입 안전성을 위해 `ProvidedContext` 타입을 보강하는 것을 권장합니다:

```ts
import { createVitest } from "vitest/node";

const vitest = await createVitest("test", {
  watch: false,
});
vitest.provide("wsPort", 3000);

declare module "vitest" {
  export interface ProvidedContext {
    wsPort: number;
  }
}
```

::: warning
기술적으로 `provide`는 [`TestProject`](https://vitest.dev/api/advanced/test-project)의 메서드이므로 특정 project로 범위가 제한됩니다. 하지만 모든 project가 루트 project의 값을 상속하므로, `vitest.provide`는 테스트에 값을 전달하는 범용 방식입니다.
:::

## getProvidedContext

```ts
function getProvidedContext(): ProvidedContext;
```

루트 컨텍스트 객체를 반환합니다. `vitest.getRootProject().getProvidedContext`의 단축형입니다.

## getProjectByName

```ts
function getProjectByName(name: string): TestProject;
```

이 메서드는 이름으로 project를 반환합니다. `vitest.projects.find`를 호출하는 것과 유사합니다.

::: warning
project가 존재하지 않으면 이 메서드는 루트 project를 반환합니다. 반환된 project가 찾고 있던 project인지 이름을 다시 확인하세요.

사용자가 이름을 커스터마이즈하지 않았다면, Vitest는 이름으로 빈 문자열을 할당합니다.
:::

## globTestSpecifications

```ts
function globTestSpecifications(
  filters?: string[],
): Promise<TestSpecification[]>;
```

이 메서드는 모든 project에서 [`project.globTestFiles`](https://vitest.dev/api/advanced/test-project#globtestfiles)로 모든 테스트를 수집해 새로운 [test specifications](https://vitest.dev/api/advanced/test-specification)을 구성합니다. 테스트 파일을 매칭하기 위한 문자열 필터를 받으며, 이는 [CLI supports](https://vitest.dev/guide/filtering#cli)와 동일한 필터입니다.

이 메서드는 모든 test specification을 자동으로 캐시합니다. 다음에 [`getModuleSpecifications`](#getmodulespecifications)를 호출하면, 그 전에 [`clearSpecificationsCache`](#clearspecificationscache)가 호출되지 않은 한 동일한 specification을 반환합니다.

::: warning
Vitest 3부터는 `poolMatchGlob`에 여러 pool이 있거나 `typecheck`가 활성화된 경우, 동일한 module ID(파일 경로)를 갖는 여러 test specification이 존재할 수 있습니다. 이 가능성은 Vitest 4에서 제거될 예정입니다.
:::

```ts
const specifications = await vitest.globTestSpecifications(["my-filter"]);
// [TestSpecification{ moduleId: '/tests/my-filter.test.ts' }]
console.log(specifications);
```

## getRelevantTestSpecifications

```ts
function getRelevantTestSpecifications(
  filters?: string[],
): Promise<TestSpecification[]>;
```

이 메서드는 [`project.globTestFiles`](https://vitest.dev/api/advanced/test-project#globtestfiles)를 호출하여 모든 test specification을 해석합니다. 테스트 파일을 매칭하기 위한 문자열 필터를 받으며, 이는 [CLI supports](https://vitest.dev/guide/filtering#cli)와 동일한 필터입니다. `--changed` 플래그가 지정된 경우, 변경된 파일만 포함하도록 목록이 필터링됩니다. `getRelevantTestSpecifications`는 어떤 테스트 파일도 실행하지 않습니다.

::: warning
이 메서드는 `--changed` 플래그를 필터링해야 하므로 느릴 수 있습니다. 테스트 파일 목록만 필요하다면 사용하지 마세요.

- 알려진 테스트 파일에 대한 specification 목록이 필요하면 [`getModuleSpecifications`](#getmodulespecifications)를 사용하세요.
- 가능한 모든 테스트 파일 목록이 필요하면 [`globTestSpecifications`](#globtestspecifications)를 사용하세요.
  :::

## mergeReports

```ts
function mergeReports(directory?: string): Promise<TestRunResult>;
```

지정한 디렉터리에 있는 여러 실행의 리포트를 병합합니다(지정하지 않으면 `--merge-reports`의 값 사용). 이 값은 `config.mergeReports`로도 설정할 수 있습니다(기본값은 `.vitest-reports` 폴더를 읽음).

`directory`는 항상 작업 디렉터리 기준으로 해석된다는 점에 유의하세요.

`config.mergeReports`가 설정된 경우 이 메서드는 [`startVitest`](https://vitest.dev/guide/advanced/tests)에서 자동으로 호출됩니다.

## collect

```ts
function collect(filters?: string[]): Promise<TestRunResult>;
```

테스트 콜백을 실행하지 않고 테스트 파일을 실행합니다. `collect`는 처리되지 않은 오류와 [test modules](https://vitest.dev/api/advanced/test-module) 배열을 반환합니다. 테스트 파일을 매칭하기 위한 문자열 필터를 받으며, 이는 [CLI supports](https://vitest.dev/guide/filtering#cli)와 동일한 필터입니다.

이 메서드는 config의 `include`, `exclude`, `includeSource` 값을 기반으로 test specification을 해석합니다. 자세한 내용은 [`project.globTestFiles`](https://vitest.dev/api/advanced/test-project#globtestfiles)를 참고하세요. `--changed` 플래그가 지정된 경우, 변경된 파일만 포함하도록 목록이 필터링됩니다.

::: warning
Vitest는 테스트 수집에 정적 분석을 사용하지 않습니다. 일반 테스트를 실행할 때와 동일하게 모든 테스트 파일을 격리된 상태로 실행합니다.

이 때문에 테스트 수집 전에 격리를 비활성화하지 않으면 이 메서드는 매우 느립니다.
:::

## start

```ts
function start(filters?: string[]): Promise<TestRunResult>;
```

reporter와 coverage provider를 초기화하고 테스트를 실행합니다. 이 메서드는 테스트 파일을 매칭하기 위한 문자열 필터를 받으며, 이는 [CLI supports](https://vitest.dev/guide/filtering#cli)와 동일한 필터입니다.

::: warning
[`vitest.init()`](#init)도 호출되는 경우에는 이 메서드를 호출하면 안 됩니다. Vitest가 초기화된 뒤 테스트를 실행해야 한다면 [`runTestSpecifications`](#runtestspecifications) 또는 [`rerunTestSpecifications`](#reruntestspecifications)를 사용하세요.
:::

`config.mergeReports`와 `config.standalone`이 설정되지 않은 경우 이 메서드는 [`startVitest`](https://vitest.dev/guide/advanced/tests)에서 자동으로 호출됩니다.

## init

```ts
function init(): Promise<void>;
```

reporter와 coverage provider를 초기화합니다. 이 메서드는 어떤 테스트도 실행하지 않습니다. `--watch` 플래그가 제공되면, 이 메서드가 호출되지 않았더라도 Vitest는 변경된 테스트를 계속 실행합니다.

내부적으로 이 메서드는 [`--standalone`](https://vitest.dev/guide/cli#standalone) 플래그가 활성화된 경우에만 호출됩니다.

::: warning
[`vitest.start()`](#start)도 호출되는 경우에는 이 메서드를 호출하면 안 됩니다.
:::

`config.standalone`이 설정된 경우 이 메서드는 [`startVitest`](https://vitest.dev/guide/advanced/tests)에서 자동으로 호출됩니다.

## getModuleSpecifications

```ts
function getModuleSpecifications(moduleId: string): TestSpecification[];
```

module ID와 관련된 test specification 목록을 반환합니다. ID는 이미 절대 파일 경로로 해석되어 있어야 합니다. ID가 `include` 또는 `includeSource` 패턴과 일치하지 않으면 반환 배열은 비어 있습니다.

이 메서드는 `moduleId`와 `pool`을 기준으로 이미 캐시된 specification을 반환할 수 있습니다. 다만 [`project.createSpecification`](https://vitest.dev/api/advanced/test-project#createspecification)은 항상 새 인스턴스를 반환하며 자동으로 캐시되지 않습니다. 그러나 [`runTestSpecifications`](#runtestspecifications)가 호출되면 specification이 자동으로 캐시됩니다.

::: warning
Vitest 3부터 이 메서드는 해당 파일이 테스트인지 확인하기 위해 캐시를 사용합니다. 캐시가 비어 있지 않도록 하려면 최소 한 번 [`globTestSpecifications`](#globtestspecifications)를 호출하세요.
:::

## clearSpecificationsCache

```ts
function clearSpecificationsCache(moduleId?: string): void;
```

Vitest는 [`globTestSpecifications`](#globtestspecifications) 또는 [`runTestSpecifications`](#runtestspecifications)가 호출될 때 각 파일의 test specification을 자동으로 캐시합니다. 이 메서드는 첫 번째 인수에 따라 특정 파일의 캐시 또는 전체 캐시를 모두 지웁니다.

## runTestSpecifications

```ts
function runTestSpecifications(
  specifications: TestSpecification[],
  allTestsRun = false,
): Promise<TestRunResult>;
```

이 메서드는 전달받은 [specifications](https://vitest.dev/api/advanced/test-specification)을 기준으로 모든 테스트를 실행합니다. 두 번째 인수 `allTestsRun`은 coverage provider가 리포트에 미커버 파일을 포함해야 하는지 판단하는 데 사용됩니다.

::: warning
이 메서드는 `onWatcherRerun`, `onWatcherStart`, `onTestsRerun` 콜백을 트리거하지 않습니다. 파일 변경을 기준으로 테스트를 다시 실행하는 경우 [`rerunTestSpecifications`](#reruntestspecifications) 사용을 고려하세요.
:::

## rerunTestSpecifications

```ts
function rerunTestSpecifications(
  specifications: TestSpecification[],
  allTestsRun = false,
): Promise<TestRunResult>;
```

이 메서드는 `reporter.onWatcherRerun` 및 `onTestsRerun` 이벤트를 발생시킨 다음, [`runTestSpecifications`](#runtestspecifications)로 테스트를 실행합니다. 메인 프로세스에 오류가 없으면 `reporter.onWatcherStart` 이벤트를 발생시킵니다.

## updateSnapshot

```ts
function updateSnapshot(files?: string[]): Promise<TestRunResult>;
```

지정된 파일의 스냅샷을 업데이트합니다. 파일이 제공되지 않으면 실패한 테스트와 더 이상 필요 없는 스냅샷이 있는 파일을 업데이트합니다.

## collectTests

```ts
function collectTests(
  specifications: TestSpecification[],
): Promise<TestRunResult>;
```

테스트 콜백을 실행하지 않고 테스트 파일을 실행합니다. `collectTests`는 처리되지 않은 오류와 [테스트 모듈](https://vitest.dev/api/advanced/test-module) 배열을 반환합니다.

이 메서드는 [`collect`](#collect)와 완전히 동일하게 동작하지만, 테스트 스펙은 직접 제공해야 합니다.

::: warning
Vitest는 테스트를 수집할 때 정적 분석을 사용하지 않습니다. Vitest는 일반 테스트를 실행할 때와 마찬가지로 모든 테스트 파일을 격리된 상태에서 실행합니다.

따라서 테스트를 수집하기 전에 격리를 비활성화하지 않으면 이 메서드는 매우 느려집니다.
:::

## cancelCurrentRun

```ts
function cancelCurrentRun(reason: CancelReason): Promise<void>;
```

이 메서드는 진행 중인 모든 테스트를 정상적으로 취소합니다. 이미 시작된 테스트가 실행을 마칠 때까지 기다리며, 실행 예정이었지만 아직 시작되지 않은 테스트는 실행하지 않습니다.

## setGlobalTestNamePattern

```ts
function setGlobalTestNamePattern(pattern: string | RegExp): void;
```

이 메서드는 전역 [test name pattern](https://vitest.dev/config/#testnamepattern)을 재정의합니다.

::: warning
이 메서드는 어떤 테스트도 실행을 시작하지 않습니다. 업데이트된 패턴으로 테스트를 실행하려면 [`runTestSpecifications`](#runtestspecifications)를 호출하세요.
:::

## getGlobalTestNamePattern 4.0.0 {#getglobaltestnamepattern}

```ts
function getGlobalTestNamePattern(): RegExp | undefined;
```

전역 테스트 이름 패턴에 사용되는 정규식을 반환합니다.

## resetGlobalTestNamePattern

```ts
function resetGlobalTestNamePattern(): void;
```

이 메서드는 [test name pattern](https://vitest.dev/config/#testnamepattern)을 초기화합니다. 즉, 이제 Vitest는 어떤 테스트도 건너뛰지 않습니다.

::: warning
이 메서드는 어떤 테스트도 실행을 시작하지 않습니다. 패턴 없이 테스트를 실행하려면 [`runTestSpecifications`](#runtestspecifications)를 호출하세요.
:::

## enableSnapshotUpdate

```ts
function enableSnapshotUpdate(): void;
```

테스트 실행 시 스냅샷 업데이트를 허용하는 모드를 활성화합니다. 이 메서드 호출 이후 실행되는 모든 테스트는 스냅샷을 업데이트합니다. 이 모드를 비활성화하려면 [`resetSnapshotUpdate`](#resetsnapshotupdate)를 호출하세요.

::: warning
이 메서드는 어떤 테스트도 실행을 시작하지 않습니다. 스냅샷을 업데이트하려면 [`runTestSpecifications`](#runtestspecifications)로 테스트를 실행하세요.
:::

## resetSnapshotUpdate

```ts
function resetSnapshotUpdate(): void;
```

테스트 실행 시 스냅샷 업데이트를 허용하는 모드를 비활성화합니다. 이 메서드는 어떤 테스트도 실행을 시작하지 않습니다.

## invalidateFile

```ts
function invalidateFile(filepath: string): void;
```

이 메서드는 모든 프로젝트의 캐시에서 파일을 무효화합니다. Vite의 캐시는 메모리에 유지되므로, 자체 watcher에 의존하는 경우 특히 유용합니다.

::: danger
Vitest의 watcher를 비활성화했지만 Vitest 프로세스는 계속 실행 중이라면, 캐시를 비활성화할 방법이 없기 때문에 이 메서드로 캐시를 수동으로 지우는 것이 중요합니다. 이 메서드는 해당 파일의 importers도 함께 무효화합니다.
:::

## import

```ts
function import<T>(moduleId: string): Promise<T>
```

Vite module runner를 사용해 파일을 가져옵니다. 파일은 전역 config로 Vite 변환을 거친 뒤 별도의 컨텍스트에서 실행됩니다. `moduleId`는 `config.root` 기준의 상대 경로라는 점에 유의하세요.

::: danger
`project.import`는 Vite의 module graph를 재사용하므로, 동일한 모듈을 일반 import로 가져오면 다른 모듈이 반환됩니다:

```ts
import * as staticExample from "./example.js";
const dynamicExample = await vitest.import("./example.js");

dynamicExample !== staticExample; // ✅
```

:::

::: info
내부적으로 Vitest는 이 메서드를 사용해 global setup, custom coverage provider, custom reporter를 import하며, 같은 Vite 서버에 속해 있는 한 모두 동일한 module graph를 공유합니다.
:::

## close

```ts
function close(): Promise<void>;
```

모든 프로젝트와 관련 리소스를 닫습니다. 이 메서드는 한 번만 호출할 수 있으며, 서버가 재시작될 때까지 종료 promise가 캐시됩니다.

## exit

```ts
function exit(force = false): Promise<void>;
```

모든 프로젝트를 닫고 프로세스를 종료합니다. `force`가 `true`로 설정되면 프로젝트를 닫은 직후 즉시 프로세스를 종료합니다.

이 메서드는 [`config.teardownTimeout`](https://vitest.dev/config/#teardowntimeout) 밀리초 후에도 프로세스가 여전히 활성 상태이면 `process.exit()`도 강제로 호출합니다.

## shouldKeepServer

```ts
function shouldKeepServer(): boolean;
```

테스트가 끝난 뒤 서버를 계속 실행 상태로 유지해야 하는 경우 `true`를 반환합니다. 일반적으로 `watch` 모드가 활성화된 경우입니다.

## onServerRestart

```ts
function onServerRestart(fn: OnServerRestartHandler): void;
```

config 변경으로 서버가 재시작될 때 호출될 핸들러를 등록합니다.

## onCancel

```ts
function onCancel(fn: (reason: CancelReason) => Awaitable<void>): () => void;
```

[`vitest.cancelCurrentRun`](#cancelcurrentrun)으로 테스트 실행이 취소될 때 호출될 핸들러를 등록합니다.

::: warning EXPERIMENTAL
4.0.10부터 `onCancel`은 리스너를 제거하는 teardown 함수를 반환합니다.
:::

## onClose

```ts
function onClose(fn: () => Awaitable<void>): void;
```

서버가 닫힐 때 호출될 핸들러를 등록합니다.

## onTestsRerun

```ts
function onTestsRerun(fn: OnTestsRerunHandler): void;
```

테스트를 다시 실행할 때 호출될 핸들러를 등록합니다. 테스트는 [`rerunTestSpecifications`](#reruntestspecifications)가 수동으로 호출될 때 다시 실행될 수 있고, 파일이 변경되어 내장 watcher가 재실행을 예약할 때도 다시 실행될 수 있습니다.

## onFilterWatchedSpecification

```ts
function onFilterWatchedSpecification(
  fn: (specification: TestSpecification) => boolean,
): void;
```

파일이 변경될 때 호출될 핸들러를 등록합니다. 이 콜백은 테스트 파일을 다시 실행해야 하는지 여부를 나타내는 `true` 또는 `false`를 반환해야 합니다.

이 메서드를 사용하면 기본 watcher 로직에 훅을 걸어, 사용자가 현재 추적하지 않으려는 테스트를 지연시키거나 제외할 수 있습니다:

```ts
const continuesTests: string[] = [];

myCustomWrapper.onContinuesRunEnabled((testItem) =>
  continuesTests.push(item.fsPath),
);

vitest.onFilterWatchedSpecification((specification) =>
  continuesTests.includes(specification.moduleId),
);
```

Vitest는 `pool` 또는 `locations` 옵션에 따라 동일한 파일에 대해 서로 다른 specification을 만들 수 있으므로 참조 자체에 의존하면 안 됩니다. Vitest는 [`vitest.getModuleSpecifications`](#getmodulespecifications)의 캐시된 specification을 반환할 수도 있으며, 이 캐시는 `moduleId`와 `pool`을 기준으로 합니다. [`project.createSpecification`](https://vitest.dev/api/advanced/test-project#createspecification)은 항상 새 인스턴스를 반환한다는 점에 유의하세요.

## matchesProjectFilter 3.1.0 {#matchesprojectfilter}

```ts
function matchesProjectFilter(name: string): boolean;
```

이름이 현재 [project filter](https://vitest.dev/guide/cli#project)와 일치하는지 확인합니다. project filter가 없으면 항상 `true`를 반환합니다.

`--project` CLI 옵션은 프로그래밍 방식으로 변경할 수 없습니다.

## waitForTestRunEnd 4.0.0 {#waitfortestrunend}

```ts
function waitForTestRunEnd(): Promise<void>;
```

테스트 실행이 진행 중이면, 해당 테스트 실행이 끝날 때 resolve되는 promise를 반환합니다.

## createCoverageProvider 4.0.0 {#createcoverageprovider}

```ts
function createCoverageProvider(): Promise<CoverageProvider | null>;
```

config에서 `coverage`가 활성화되어 있으면 coverage provider를 생성합니다. [`start`](#start) 또는 [`init`](#init) 메서드로 테스트를 실행하는 경우 이 작업은 자동으로 수행됩니다.

::: warning
[`coverage.clean`](https://vitest.dev/config/#coverage-clean)이 `false`가 아니면 이 메서드는 이전 리포트도 모두 정리합니다.
:::

## enableCoverage 4.0.0 {#enablecoverage}

```ts
function enableCoverage(): Promise<void>;
```

이 메서드는 이 호출 이후 실행되는 테스트에 대해 coverage를 활성화합니다. `enableCoverage`는 테스트를 실행하지 않으며, Vitest가 coverage를 수집하도록 설정만 수행합니다.

coverage provider가 아직 없으면 새로 생성합니다.

## disableCoverage 4.0.0 {#disablecoverage}

```ts
function disableCoverage(): void;
```

이 메서드는 이후 실행되는 테스트의 coverage 수집을 비활성화합니다.

## getSeed 4.0.0 {#getseed}

```ts
function getSeed(): number | null;
```

테스트가 무작위 순서로 실행 중이라면 seed를 반환합니다.

## experimental_parseSpecification 4.0.0 {#parsespecification}

```ts
function experimental_parseSpecification(
  specification: TestSpecification,
): Promise<TestModule>;
```

이 함수는 파일을 실행하지 않고 파일 내부의 모든 테스트를 수집합니다. Vite의 `ssrTransform` 위에서 rollup의 `parseAst` 함수를 사용해 파일을 정적으로 분석하고 가능한 모든 테스트를 수집합니다.

::: warning
Vitest가 테스트 이름을 분석할 수 없는 경우, 테스트 또는 suite에 `dynamic: true` 속성을 주입합니다. 또한 정상적으로 수집된 테스트를 깨뜨리지 않기 위해 `id`에도 `-dynamic` 접미사가 붙습니다.

Vitest는 `for` 또는 `each` modifier가 있는 테스트, 혹은 동적 이름(예: `hello ${property}` 또는 `'hello' + ${property}`)을 가진 테스트에 항상 이 속성을 주입합니다. Vitest는 여전히 테스트 이름을 할당하지만, 이 이름은 테스트 필터링에 사용할 수 없습니다.

동적 테스트를 필터링 가능하게 만드는 방법은 없지만, `for` 또는 `each` modifier가 있는 테스트를 `escapeTestName` 함수를 사용해 이름 패턴으로 바꿀 수는 있습니다:

```ts
import { escapeTestName } from "vitest/node";

// turns into /hello, .+?/
const escapedPattern = new RegExp(escapeTestName("hello, %s", true));
```

:::

::: warning
Vitest는 파일에 정의된 테스트만 수집합니다. 다른 파일로의 import를 따라가지는 않습니다.

Vitest는 `vitest` 엔트리 포인트에서 import하지 않았더라도 모든 `it`, `test`, `suite`, `describe` 정의를 수집합니다.
:::

## experimental_parseSpecifications 4.0.0 {#parsespecifications}

```ts
function experimental_parseSpecifications(
  specifications: TestSpecification[],
  options?: {
    concurrency?: number;
  },
): Promise<TestModule[]>;
```

이 메서드는 specification 배열에서 [테스트를 수집](#parsespecification)합니다. 기본적으로 Vitest는 잠재적인 성능 저하를 줄이기 위해 한 번에 `os.availableParallelism()` 개수만큼의 specification만 실행합니다. 두 번째 인자로 다른 개수를 지정할 수 있습니다.

## experimental_clearCache 4.0.11 {#clearcache}

```ts
function experimental_clearCache(): Promise<void>;
```

[`experimental.fsModuleCache`](https://vitest.dev/config/experimental#experimental-fsmodulecache)를 포함해 모든 Vitest 캐시를 삭제합니다.

## experimental_getSourceModuleDiagnostic 4.0.15 {#getsourcemodulediagnostic}

```ts
export function experimental_getSourceModuleDiagnostic(
  moduleId: string,
  testModule?: TestModule,
): Promise<SourceModuleDiagnostic>;
```

::: details Types

```ts
export interface ModuleDefinitionLocation {
  line: number;
  column: number;
}

export interface SourceModuleLocations {
  modules: ModuleDefinitionDiagnostic[];
  untracked: ModuleDefinitionDiagnostic[];
}

export interface ModuleDefinitionDiagnostic {
  start: ModuleDefinitionLocation;
  end: ModuleDefinitionLocation;
  startIndex: number;
  endIndex: number;
  url: string;
  resolvedId: string;
}

export interface ModuleDefinitionDurationsDiagnostic extends ModuleDefinitionDiagnostic {
  selfTime: number;
  totalTime: number;
  external?: boolean;
}

export interface UntrackedModuleDefinitionDiagnostic {
  url: string;
  resolvedId: string;
  selfTime: number;
  totalTime: number;
  external?: boolean;
}

export interface SourceModuleDiagnostic {
  modules: ModuleDefinitionDurationsDiagnostic[];
  untrackedModules: UntrackedModuleDefinitionDiagnostic[];
}
```

:::

모듈의 진단 정보를 반환합니다. [`testModule`](https://vitest.dev/api/advanced/test-module)이 제공되지 않으면 `selfTime`과 `totalTime`은 마지막 실행 시점에 실행되었던 모든 테스트 기준으로 집계됩니다. 모듈이 변환되거나 실행되지 않았다면 진단 정보는 비어 있습니다.

::: warning
현재 [browser](https://vitest.dev/guide/browser/) 모듈은 지원되지 않습니다.
:::
