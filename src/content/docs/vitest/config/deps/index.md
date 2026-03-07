---
title: "deps"
description: "의존성 최적화를 활성화합니다. 테스트가 많다면 성능이 향상될 수 있습니다."
---

출처 URL: https://vitest.dev/config/deps

# deps

- **Type:** `{ optimizer?, ... }`

의존성 해석 처리 방식입니다.

## deps.optimizer {#deps-optimizer}

- **Type:** `{ ssr?, client? }`
- **See also:** [Dep Optimization Options](https://vitejs.dev/config/dep-optimization-options.html)

의존성 최적화를 활성화합니다. 테스트가 많다면 성능이 향상될 수 있습니다.

Vitest가 `include`에 나열된 외부 라이브러리를 만나면, esbuild를 사용해 단일 파일로 번들링하고 전체 모듈로 가져옵니다. 이는 다음과 같은 여러 이유로 유리합니다.

- import가 많은 패키지를 가져오는 작업은 비용이 큽니다. 하나의 파일로 번들링하면 많은 시간을 절약할 수 있습니다.
- UI 라이브러리는 Node.js 내부에서 실행되도록 만들어진 것이 아니므로 가져오는 비용이 큽니다.
- 이제 번들된 패키지 내부에서도 `alias` 설정이 적용됩니다.
- 테스트 코드가 브라우저에서 실행되는 방식에 더 가깝게 실행됩니다.

`deps.optimizer?.[mode].include` 옵션에 포함된 패키지만 번들링된다는 점에 유의하세요(일부 플러그인, 예: Svelte, 은 이를 자동으로 채웁니다). 사용 가능한 옵션은 [Vite](https://vitejs.dev/config/dep-optimization-options.html) 문서에서 더 확인할 수 있습니다(Vitest는 `disable` 및 `noDiscovery` 옵션을 지원하지 않음). 기본적으로 Vitest는 `jsdom` 및 `happy-dom` 환경에서 `optimizer.client`를, `node` 및 `edge` 환경에서 `optimizer.ssr`를 사용합니다.

이 옵션은 `optimizeDeps` 설정도 상속합니다(웹에서는 Vitest가 `optimizeDeps`를 확장하고, ssr에서는 `ssr.optimizeDeps`를 확장). `deps.optimizer`에서 `include`/`exclude` 옵션을 재정의하면 테스트 실행 시 `optimizeDeps`를 확장합니다. `exclude`에 같은 항목이 있으면 Vitest가 `include`에서 해당 항목을 자동으로 제거합니다.

::: tip
실제 코드는 `cacheDir` 또는 `test.cache.dir` 디렉터리에 있기 때문에 디버깅을 위해 `node_modules` 코드를 수정할 수 없습니다. `console.log`로 디버깅하려면 해당 코드를 직접 수정하거나 `deps.optimizer?.[mode].force` 옵션으로 강제로 다시 번들링하세요.
:::

### deps.optimizer.{mode}.enabled

- **Type:** `boolean`
- **Default:** `false`

의존성 최적화를 활성화합니다.

## deps.client {#deps-client}

- **Type:** `{ transformAssets?, ... }`

환경이 `client`로 설정되었을 때 외부 파일에 적용되는 옵션입니다. 기본적으로 `jsdom`과 `happy-dom`은 `client` 환경을 사용하고, `node`와 `edge` 환경은 `ssr`을 사용하므로, 이 옵션은 해당 환경 내부 파일에는 영향을 주지 않습니다.

일반적으로 `node_modules` 내부 파일은 externalize되지만, 이 옵션은 [`server.deps.external`](#server-deps-external)의 파일에도 영향을 줍니다.

### deps.client.transformAssets

- **Type:** `boolean`
- **Default:** `true`

Vitest가 에셋(.png, .svg, .jpg 등) 파일을 처리하고 브라우저에서의 Vite처럼 해석할지 여부입니다.

쿼리가 지정되지 않은 경우, 이 모듈의 default export는 에셋 경로와 동일합니다.

::: warning
현재 이 옵션은 [`vmThreads`](#vmthreads) 및 [`vmForks`](#vmforks) 풀에서만 동작합니다.
:::

### deps.client.transformCss

- **Type:** `boolean`
- **Default:** `true`

Vitest가 CSS(.css, .scss, .sass 등) 파일을 처리하고 브라우저에서의 Vite처럼 해석할지 여부입니다.

[`css`](#css) 옵션으로 CSS 파일이 비활성화된 경우, 이 옵션은 `ERR_UNKNOWN_FILE_EXTENSION` 오류를 숨기는 역할만 합니다.

::: warning
현재 이 옵션은 [`vmThreads`](#vmthreads) 및 [`vmForks`](#vmforks) 풀에서만 동작합니다.
:::

### deps.client.transformGlobPattern

- **Type:** `RegExp | RegExp[]`
- **Default:** `[]`

변환되어야 하는 외부 파일을 매칭하기 위한 정규식 패턴입니다.

기본적으로 `node_modules` 내부 파일은 externalize되어 변환되지 않습니다. 단, CSS 또는 에셋 파일이고 해당 옵션이 비활성화되지 않은 경우는 예외입니다.

::: warning
현재 이 옵션은 [`vmThreads`](#vmthreads) 및 [`vmForks`](#vmforks) 풀에서만 동작합니다.
:::

## deps.interopDefault

- **Type:** `boolean`
- **Default:** `true`

CJS 모듈의 default를 named exports로 해석합니다. 일부 의존성은 CJS 모듈만 번들링하며, 패키지를 `require` 대신 `import` 문법으로 가져올 때 Node.js가 정적으로 분석할 수 있는 named exports를 사용하지 않습니다. 이러한 의존성을 Node 환경에서 named exports로 import하면 다음 오류가 표시됩니다.

```
import { read } from 'fs-jetpack';
         ^^^^
SyntaxError: Named export 'read' not found. The requested module 'fs-jetpack' is a CommonJS module, which may not support all module.exports as named exports.
CommonJS modules can always be imported via the default export.
```

Vitest는 정적 분석을 수행하지 않으므로 코드 실행 전에 실패시킬 수 없습니다. 따라서 이 기능이 비활성화되어 있으면 테스트 실행 중 다음 오류를 보게 될 가능성이 큽니다.

```
TypeError: createAsyncThunk is not a function
TypeError: default is not a function
```

기본적으로 Vitest는 이 문제를 우회하기 위해 번들러를 사용한다고 가정하고 실패하지 않지만, 코드가 처리되지 않는 경우 이 동작을 수동으로 비활성화할 수 있습니다.

## deps.moduleDirectories

- **Type:** `string[]`
- **Default**: `['node_modules']`

모듈 디렉터리로 취급할 디렉터리 목록입니다. 이 설정 옵션은 [`vi.mock`](https://vitest.dev/api/vi#vi-mock)의 동작에 영향을 줍니다. factory를 제공하지 않았고 mock 대상 경로가 `moduleDirectories` 값 중 하나와 일치하면, Vitest는 프로젝트의 [root](#root)에서 `__mocks__` 폴더를 찾아 mock을 해석하려고 시도합니다.

이 옵션은 의존성을 externalize할 때 파일을 모듈로 취급할지에도 영향을 줍니다. 기본적으로 Vitest는 외부 모듈을 Vite 변환 단계를 우회해 네이티브 Node.js로 import합니다.

이 옵션을 설정하면 기본값을 *override*합니다. 패키지 검색 시에도 `node_modules`를 계속 사용하려면 다른 옵션과 함께 포함하세요.

```ts
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    deps: {
      moduleDirectories: ["node_modules", path.resolve("../../packages")],
    },
  },
});
```
