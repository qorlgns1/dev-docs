---
title: "테스트 실행 고급 {#running-tests}"
description: "이 가이드는 Node.js 스크립트를 통해 테스트를 실행하기 위해 고급 API를 사용하는 방법을 설명합니다. 단순히 테스트를 실행하려는 경우에는 아마 이것이 필요하지 않습니다. 주로 라이브러리 작성자가 사용합니다."
---

출처 URL: https://vitest.dev/guide/advanced/tests

# 테스트 실행 고급 {#running-tests}

::: warning
이 가이드는 Node.js 스크립트를 통해 테스트를 실행하기 위해 고급 API를 사용하는 방법을 설명합니다. 단순히 [테스트를 실행](https://vitest.dev/guide/)하려는 경우에는 아마 이것이 필요하지 않습니다. 주로 라이브러리 작성자가 사용합니다.
:::

Vitest는 Vitest를 시작하기 위한 두 가지 메서드를 제공합니다:

- `startVitest`는 Vitest를 시작하고, 패키지가 설치되어 있는지 검증한 뒤 즉시 테스트를 실행합니다
- `createVitest`는 Vitest만 시작하고 어떤 테스트도 실행하지 않습니다

## `startVitest`

```ts
import { startVitest } from "vitest/node";

const vitest = await startVitest(
  "test",
  [], // CLI filters
  {}, // override test config
  {}, // override Vite config
  {}, // custom Vitest options
);
const testModules = vitest.state.getTestModules();
for (const testModule of testModules) {
  console.log(testModule.moduleId, testModule.ok() ? "passed" : "failed");
}
```

::: tip
[`TestModule`](https://vitest.dev/api/advanced/test-module), [`TestSuite`](https://vitest.dev/api/advanced/test-suite), [`TestCase`](https://vitest.dev/api/advanced/test-case) API는 실험적 기능이 아니며, Vitest 2.1부터 SemVer를 따릅니다.
:::

## `createVitest`

테스트를 실행하지 않고 [Vitest](https://vitest.dev/api/advanced/vitest) 인스턴스를 생성합니다.

`createVitest` 메서드는 필요한 패키지가 설치되어 있는지 검증하지 않습니다. 또한 `config.standalone`이나 `config.mergeReports`도 반영하지 않습니다. `watch`가 비활성화되어 있어도 Vitest는 자동으로 종료되지 않습니다.

```ts
import { createVitest } from "vitest/node";

const vitest = await createVitest(
  "test",
  {}, // override test config
  {}, // override Vite config
  {}, // custom Vitest options
);

// called when `vitest.cancelCurrentRun()` is invoked
vitest.onCancel(() => {});
// called during `vitest.close()` call
vitest.onClose(() => {});
// called when Vitest reruns test files
vitest.onTestsRerun((files) => {});

try {
  // this will set process.exitCode to 1 if tests failed,
  // and won't close the process automatically
  await vitest.start(["my-filter"]);
} catch (err) {
  // this can throw
  // "FilesNotFoundError" if no files were found
  // "GitNotFoundError" with `--changed` and repository is not initialized
} finally {
  await vitest.close();
}
```

`Vitest` 인스턴스를 유지할 계획이라면, 최소한 [`init`](https://vitest.dev/api/advanced/vitest#init)을 호출해야 합니다. 이렇게 하면 리포터와 커버리지 provider가 초기화되지만 테스트는 실행되지 않습니다. Vitest watcher를 사용할 계획이 없더라도 인스턴스를 계속 실행 상태로 유지하려면 `watch` 모드를 활성화하는 것도 권장됩니다. Vitest는 지속적으로 실행되는 프로세스에서 일부 기능이 올바르게 동작하기 위해 이 플래그에 의존합니다.

리포터가 초기화된 후, 수동 실행이 필요하다면 [`runTestSpecifications`](https://vitest.dev/api/advanced/vitest#runtestspecifications) 또는 [`rerunTestSpecifications`](https://vitest.dev/api/advanced/vitest#reruntestspecifications)를 사용해 테스트를 실행하세요:

```ts
watcher.on("change", async (file) => {
  const specifications = vitest.getModuleSpecifications(file);
  if (specifications.length) {
    vitest.invalidateFile(file);
    // you can use runTestSpecifications if "reporter.onWatcher*" hooks
    // should not be invoked
    await vitest.rerunTestSpecifications(specifications);
  }
});
```

::: warning
위 예시는 기본 watcher 동작을 비활성화했을 때의 잠재적인 사용 사례를 보여줍니다. 기본적으로 Vitest는 파일이 변경되면 이미 테스트를 다시 실행합니다.

또한 `getModuleSpecifications`는 해당 테스트 파일이 이미 `globTestSpecifications`로 처리된 경우가 아니면 테스트 파일을 해석하지 못합니다. 파일이 방금 생성된 경우에는 대신 `project.matchesGlobPattern`을 사용하세요:

```ts
watcher.on("add", async (file) => {
  const specifications = [];
  for (const project of vitest.projects) {
    if (project.matchesGlobPattern(file)) {
      specifications.push(project.createSpecification(file));
    }
  }

  if (specifications.length) {
    await vitest.rerunTestSpecifications(specifications);
  }
});
```

:::

watcher를 비활성화해야 하는 경우, Vite 5.3부터 `server.watch: null`을 전달하거나 Vite config에 `server.watch: { ignored: ['*/*'] }`를 전달할 수 있습니다:

```ts
await createVitest(
  "test",
  {},
  {
    plugins: [
      {
        name: "stop-watcher",
        async configureServer(server) {
          await server.watcher.close();
        },
      },
    ],
    server: {
      watch: null,
    },
  },
);
```
