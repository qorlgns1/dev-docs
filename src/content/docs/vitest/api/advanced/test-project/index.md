---
title: "TestProject 3.0.0 {#testproject}"
description: '이 가이드는 고급 Node.js API를 설명합니다. 프로젝트만 정의하려면 "Test Projects" 가이드를 따르세요.'
---

출처 URL: https://vitest.dev/api/advanced/test-project

# TestProject 3.0.0 {#testproject}

::: warning
이 가이드는 고급 Node.js API를 설명합니다. 프로젝트만 정의하려면 ["Test Projects"](https://vitest.dev/guide/projects) 가이드를 따르세요.
:::

## name

`name`은 사용자가 할당하거나 Vitest가 해석한 고유 문자열입니다. 사용자가 이름을 제공하지 않으면, Vitest는 프로젝트 루트에서 `package.json`을 로드해 그 안의 `name` 속성을 가져오려고 시도합니다. `package.json`이 없으면 기본적으로 폴더 이름을 사용합니다. 인라인 프로젝트는 숫자를 이름으로 사용합니다(문자열로 변환됨).

::: code-group

```ts [node.js]
import { createVitest } from "vitest/node";

const vitest = await createVitest("test");
vitest.projects.map((p) => p.name) === ["@pkg/server", "utils", "2", "custom"];
```

```ts [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    projects: [
      "./packages/server", // has package.json with "@pkg/server"
      "./utils", // doesn't have a package.json file
      {
        // doesn't customize the name
        test: {
          pool: "threads",
        },
      },
      {
        // customized the name
        test: {
          name: "custom",
        },
      },
    ],
  },
});
```

:::

::: info
[루트 프로젝트](https://vitest.dev/api/advanced/vitest#getroottestproject)가 사용자 프로젝트에 포함되어 있지 않다면, 해당 `name`은 해석되지 않습니다.
:::

## vitest

`vitest`는 전역 [`Vitest`](https://vitest.dev/api/advanced/vitest) 프로세스를 참조합니다.

## serializedConfig

이는 테스트 프로세스가 받는 config입니다. Vitest는 직렬화할 수 없는 모든 함수와 속성을 제거하여 config를 수동으로 [직렬화](https://github.com/vitest-dev/vitest/blob/main/packages/vitest/src/node/config/serializeConfig.ts)합니다. 이 값은 테스트와 node 양쪽에서 모두 사용 가능하므로, 타입이 메인 엔트리 포인트에서 export됩니다.

```ts
import type { SerializedConfig } from "vitest";

const config: SerializedConfig = vitest.projects[0].serializedConfig;
```

::: warning
`serializedConfig` 속성은 getter입니다. 접근할 때마다 config가 변경되었을 가능성을 고려해 Vitest가 다시 직렬화합니다. 즉, 항상 서로 다른 참조를 반환합니다:

```ts
project.serializedConfig === project.serializedConfig; // ❌
```

:::

## globalConfig

[`Vitest`](https://vitest.dev/api/advanced/vitest)가 초기화될 때 사용된 테스트 config입니다. 이것이 [루트 프로젝트](https://vitest.dev/api/advanced/vitest#getroottestproject)라면 `globalConfig`와 `config`는 동일한 객체를 참조합니다. 이 config는 `coverage`나 `reporters`처럼 프로젝트 레벨에서 설정할 수 없는 값에 유용합니다.

```ts
import type { ResolvedConfig } from "vitest/node";

vitest.config === vitest.projects[0].globalConfig;
```

## config

이는 프로젝트의 해석된 테스트 config입니다.

## hash 3.2.0 {#hash}

이 프로젝트의 고유 해시입니다. 이 값은 재실행 간에도 일관됩니다.

프로젝트 루트와 이름을 기반으로 생성됩니다. 루트 경로는 OS마다 일관되지 않으므로, 해시도 달라집니다.

## vite

이는 프로젝트의 [`ViteDevServer`](https://vite.dev/guide/api-javascript#vitedevserver)입니다. 모든 프로젝트는 자체 Vite 서버를 가집니다.

## browser

이 값은 테스트가 브라우저에서 실행될 때만 설정됩니다. `browser`가 활성화되어 있어도 테스트가 아직 실행되지 않았다면 `undefined`입니다. 프로젝트가 브라우저 테스트를 지원하는지 확인하려면 `project.isBrowserEnabled()` 메서드를 사용하세요.

::: warning
브라우저 API는 더 실험적이며 SemVer를 따르지 않습니다. 브라우저 API는 나머지 API와 별도로 표준화될 예정입니다.
:::

## provide

```ts
function provide<T extends keyof ProvidedContext & string>(
  key: T,
  value: ProvidedContext[T],
): void;
```

[`config.provide`](https://vitest.dev/config/#provide) 필드에 더해 테스트에 커스텀 값을 제공하는 방법입니다. 저장 전에 모든 값은 [`structuredClone`](https://developer.mozilla.org/en-US/docs/Web/API/Window/structuredClone)으로 검증되지만, `providedContext`의 값 자체가 클론되지는 않습니다.

::: code-group

```ts [node.js]
import { createVitest } from "vitest/node";

const vitest = await createVitest("test");
const project = vitest.projects.find((p) => p.name === "custom");
project.provide("key", "value");
await vitest.start();
```

```ts [test.spec.js]
import { inject } from "vitest";
const value = inject("key");
```

:::

값은 동적으로 제공할 수 있습니다. 테스트에서 제공된 값은 다음 실행 시 업데이트됩니다.

::: tip
공개 API를 사용할 수 없는 경우를 위해, 이 메서드는 [global setup files](https://vitest.dev/config/#globalsetup)에서도 사용할 수 있습니다:

```js
export default function setup({ provide }) {
  provide("wsPort", 3000);
}
```

:::

## getProvidedContext

```ts
function getProvidedContext(): ProvidedContext;
```

컨텍스트 객체를 반환합니다. 모든 프로젝트는 `vitest.provide`로 설정된 전역 컨텍스트도 상속합니다.

```ts
import { createVitest } from "vitest/node";

const vitest = await createVitest("test");
vitest.provide("global", true);
const project = vitest.projects.find((p) => p.name === "custom");
project.provide("key", "value");

// { global: true, key: 'value' }
const context = project.getProvidedContext();
```

::: tip
프로젝트 컨텍스트 값은 항상 루트 프로젝트의 컨텍스트를 덮어씁니다.
:::

## createSpecification

```ts
function createSpecification(
  moduleId: string,
  locations?: number[],
): TestSpecification;
```

[`vitest.runTestSpecifications`](https://vitest.dev/api/advanced/vitest#runtestspecifications)에서 사용할 수 있는 [test specification](https://vitest.dev/api/advanced/test-specification)을 생성합니다. specification은 테스트 파일을 특정 `project`와 테스트 `locations`(선택 사항)으로 한정합니다. 테스트 [locations](https://vitest.dev/api/advanced/test-case#location)은 소스 코드에서 테스트가 정의된 코드 라인입니다. locations가 제공되면 Vitest는 해당 라인에 정의된 테스트만 실행합니다. [`testNamePattern`](https://vitest.dev/config/#testnamepattern)이 정의되어 있다면 그것도 함께 적용됩니다.

```ts
import { createVitest } from "vitest/node";
import { resolve } from "node:path/posix";

const vitest = await createVitest("test");
const project = vitest.projects[0];
const specification = project.createSpecification(
  resolve("./example.test.ts"),
  [20, 40], // optional test lines
);
await vitest.runTestSpecifications([specification]);
```

::: warning
`createSpecification`은 해석된 [module ID](https://vitest.dev/api/advanced/test-specification#moduleid)를 기대합니다. 파일을 자동으로 해석하거나 파일 시스템에 존재하는지 확인하지 않습니다.

또한 `project.createSpecification`은 항상 새 인스턴스를 반환합니다.
:::

## isRootProject

```ts
function isRootProject(): boolean;
```

현재 프로젝트가 루트 프로젝트인지 확인합니다. [`vitest.getRootProject()`](#getrootproject)를 호출해서도 루트 프로젝트를 가져올 수 있습니다.

## globTestFiles

```ts
function globTestFiles(filters?: string[]): {
  /**
   * Test files that match the filters.
   */
  testFiles: string[];
  /**
   * Typecheck test files that match the filters. This will be empty unless `typecheck.enabled` is `true`.
   */
  typecheckTestFiles: string[];
};
```

모든 테스트 파일을 glob으로 찾습니다. 이 함수는 일반 테스트와 typecheck 테스트를 포함한 객체를 반환합니다.

이 메서드는 `filters`를 받습니다. `filters`는 [`Vitest`](https://vitest.dev/api/advanced/vitest) 인스턴스의 다른 메서드와 달리 파일 경로의 일부만 사용할 수 있습니다:

```js
project.globTestFiles(["foo"]); // ✅
project.globTestFiles(["basic/foo.js:10"]); // ❌
```

::: tip
Vitest는 테스트 파일을 찾기 위해 [fast-glob](https://www.npmjs.com/package/fast-glob)을 사용합니다. `test.dir`, `test.root`, `root` 또는 `process.cwd()`가 `cwd` 옵션을 정의합니다.

이 메서드는 여러 config 옵션을 확인합니다:

- 일반 테스트 파일 탐색: `test.include`, `test.exclude`
- in-source 테스트 탐색: `test.includeSource`, `test.exclude`
- typecheck 테스트 탐색: `test.typecheck.include`, `test.typecheck.exclude`
  :::

## matchesTestGlob

```ts
function matchesTestGlob(moduleId: string, source?: () => string): boolean;
```

이 메서드는 파일이 일반 테스트 파일인지 확인합니다. 검증에는 `globTestFiles`와 동일한 config 속성을 사용합니다.

이 메서드는 두 번째 매개변수로 소스 코드도 받을 수 있습니다. 이는 파일이 in-source 테스트인지 검증하는 데 사용됩니다. 여러 프로젝트에 대해 이 메서드를 여러 번 호출한다면, 파일을 한 번만 읽고 직접 전달하는 것을 권장합니다. 파일이 테스트 파일은 아니지만 `includeSource` glob과 일치하면, `source`가 제공되지 않은 경우 Vitest가 파일을 동기적으로 읽습니다.

```ts
import { createVitest } from "vitest/node";
import { resolve } from "node:path/posix";

const vitest = await createVitest("test");
const project = vitest.projects[0];

project.matchesTestGlob(resolve("./basic.test.ts")); // true
project.matchesTestGlob(resolve("./basic.ts")); // false
project.matchesTestGlob(
  resolve("./basic.ts"),
  () => `
if (import.meta.vitest) {
  // ...
}
`,
); // true if `includeSource` is set
```

## import

```ts
function import<T>(moduleId: string): Promise<T>
```

Vite 모듈 러너를 사용해 파일을 import합니다. 파일은 제공된 프로젝트 config로 Vite에서 변환된 뒤 별도 컨텍스트에서 실행됩니다. `moduleId`는 `config.root`를 기준으로 상대 경로가 됩니다.

::: danger
`project.import`는 Vite의 모듈 그래프를 재사용하므로, 같은 모듈을 일반 import로 가져오면 다른 모듈이 반환됩니다:

```ts
import * as staticExample from "./example.js";
const dynamicExample = await project.import("./example.js");

dynamicExample !== staticExample; // ✅
```

:::

::: info
내부적으로 Vitest는 global setup, 커스텀 coverage provider, 커스텀 reporter를 import할 때 이 메서드를 사용합니다. 즉, 같은 Vite 서버에 속해 있는 한 이들 모두 동일한 모듈 그래프를 공유합니다.
:::

## onTestsRerun

```ts
function onTestsRerun(cb: OnTestsRerunHandler): void;
```

[`project.vitest.onTestsRerun`](https://vitest.dev/api/advanced/vitest#ontestsrerun)의 축약형입니다. 테스트가 재실행되도록 스케줄된 시점(보통 파일 변경으로 인해)에 await되는 콜백을 받습니다.

```ts
project.onTestsRerun((specs) => {
  console.log(specs);
});
```

## isBrowserEnabled

```ts
function isBrowserEnabled(): boolean;
```

이 프로젝트가 브라우저에서 테스트를 실행하면 `true`를 반환합니다.

## close

```ts
function close(): Promise<void>;
```

프로젝트와 관련된 모든 리소스를 닫습니다. 이 메서드는 한 번만 호출할 수 있으며, 서버가 다시 시작될 때까지 종료 Promise가 캐시됩니다. 리소스를 다시 사용해야 하면 새 프로젝트를 생성하세요.

구체적으로 이 메서드는 Vite 서버를 닫고, typechecker 서비스를 중지하고, 브라우저가 실행 중이면 종료하고, 소스 코드를 담는 임시 디렉터리를 삭제하며, 제공된 컨텍스트를 초기화합니다.
