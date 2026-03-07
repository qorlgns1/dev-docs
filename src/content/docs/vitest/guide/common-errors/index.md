---
title: "일반적인 오류"
description: "모듈을 찾을 수 없다는 오류가 발생하면 여러 가지 원인일 수 있습니다:"
---

출처 URL: https://vitest.dev/guide/common-errors

# 일반적인 오류

## Cannot find module './relative-path'

모듈을 찾을 수 없다는 오류가 발생하면 여러 가지 원인일 수 있습니다:

- 1. 경로에 오타가 있습니다. 경로가 올바른지 확인하세요.
- 2. `tsconfig.json`의 `baseUrl`에 의존하고 있을 수 있습니다. 기본적으로 Vite는 `tsconfig.json`을 고려하지 않으므로, 이 동작에 의존한다면 [`vite-tsconfig-paths`](https://www.npmjs.com/package/vite-tsconfig-paths)를 직접 설치해야 할 수 있습니다.

```ts
import { defineConfig } from "vitest/config";
import tsconfigPaths from "vite-tsconfig-paths";

export default defineConfig({
  plugins: [tsconfigPaths()],
});
```

또는 루트 기준 상대 경로를 사용하지 않도록 경로를 다시 작성하세요:

```diff
- import helpers from 'src/helpers'
+ import helpers from '../src/helpers'
```

- 3. 상대 [aliases](https://vitest.dev/config/#alias)를 사용하고 있지 않은지 확인하세요. Vite는 이를 루트가 아니라 import가 있는 파일 기준의 상대 경로로 처리합니다.

```ts
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    alias: {
      "@/": "./src/", // [!code --]
      "@/": new URL("./src/", import.meta.url).pathname, // [!code ++]
    },
  },
});
```

## Failed to Terminate Worker

이 오류는 NodeJS의 `fetch`를 기본 [`pool: 'threads'`](https://vitest.dev/config/#threads)와 함께 사용할 때 발생할 수 있습니다. 이 이슈는 [Timeout abort can leave process(es) running in the background #3077](https://github.com/vitest-dev/vitest/issues/3077)에서 추적되고 있습니다.

우회 방법으로 [`pool: 'forks'`](https://vitest.dev/config/#forks) 또는 [`pool: 'vmForks'`](https://vitest.dev/config/#vmforks)로 전환할 수 있습니다.

::: code-group

```ts [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    pool: "forks",
  },
});
```

```bash [CLI]
vitest --pool=forks
```

:::

## Custom package conditions are not resolved

`package.json`의 [exports](https://nodejs.org/api/packages.html#package-entry-points) 또는 [subpath imports](https://nodejs.org/api/packages.html#subpath-imports)에서 사용자 정의 조건을 사용하고 있다면, Vitest가 기본적으로 이러한 조건을 반영하지 않는 것을 확인할 수 있습니다.

예를 들어, `package.json`에 다음이 있다고 가정해 보겠습니다:

```json
{
  "exports": {
    ".": {
      "custom": "./lib/custom.js",
      "import": "./lib/index.js"
    }
  },
  "imports": {
    "#internal": {
      "custom": "./src/internal.js",
      "default": "./lib/internal.js"
    }
  }
}
```

기본적으로 Vitest는 `import`와 `default` 조건만 사용합니다. Vitest가 사용자 정의 조건을 반영하도록 하려면 Vitest 설정에서 [`ssr.resolve.conditions`](https://vite.dev/config/ssr-options#ssr-resolve-conditions)를 구성해야 합니다:

```ts [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  ssr: {
    resolve: {
      conditions: ["custom", "import", "default"],
    },
  },
});
```

::: tip 왜 `resolve.conditions`가 아니라 `ssr.resolve.conditions`인가요?
Vitest는 Vite의 설정 규칙을 따릅니다:

- [`resolve.conditions`](https://vite.dev/config/shared-options#resolve-conditions)는 Vite의 `client` 환경에 적용되며, 이는 Vitest의 browser mode, jsdom, happy-dom 또는 `viteEnvironment: 'client'`를 사용하는 custom environments에 해당합니다.
- [`ssr.resolve.conditions`](https://vite.dev/config/ssr-options#ssr-resolve-conditions)는 Vite의 `ssr` 환경에 적용되며, 이는 Vitest의 node environment 또는 `viteEnvironment: 'ssr'`를 사용하는 custom environments에 해당합니다.

Vitest는 기본적으로 `node` environment(즉 `viteEnvironment: 'ssr'` 사용)를 사용하므로, 모듈 해석에는 `ssr.resolve.conditions`가 사용됩니다. 이는 package exports와 subpath imports 모두에 적용됩니다.

Vite environments와 Vitest environments에 대한 자세한 내용은 [`environment`](https://vitest.dev/config/environment)에서 확인할 수 있습니다.
:::

## Segfaults and Native Code Errors

[native NodeJS modules](https://nodejs.org/api/addons.html)를 `pool: 'threads'`에서 실행하면 네이티브 코드에서 비롯된 해석하기 어려운 오류가 발생할 수 있습니다.

- `Segmentation fault (core dumped)`
- `thread '<unnamed>' panicked at 'assertion failed`
- `Abort trap: 6`
- `internal error: entered unreachable code`

이 경우 해당 네이티브 모듈이 멀티스레드 안전하게 빌드되지 않았을 가능성이 큽니다. 우회 방법으로 `pool: 'forks'`로 전환할 수 있으며, 이 방식은 여러 `node:worker_threads` 대신 여러 `node:child_process`에서 테스트 케이스를 실행합니다.

::: code-group

```ts [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    pool: "forks",
  },
});
```

```bash [CLI]
vitest --pool=forks
```

:::
