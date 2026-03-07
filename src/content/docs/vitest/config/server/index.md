---
title: "server"
description: "Vitest 4 이전에는 이 옵션이  서버의 구성을 정의하는 데 사용되었습니다."
---

# server

Vitest 4 이전에는 이 옵션이 `vite-node` 서버의 구성을 정의하는 데 사용되었습니다.

현재 이 옵션을 사용하면 모듈 러너 디버깅 구성과 함께 인라인 및 외부화 메커니즘을 설정할 수 있습니다.

::: warning
이 옵션들은 자동으로 인라인된 의존성을 외부화해 성능을 개선하거나, 잘못된 외부 의존성을 인라인해 문제를 해결해야 할 때 최후의 수단으로만 사용해야 합니다.

일반적으로 Vitest가 이를 자동으로 처리해야 합니다.
:::

## deps

### external

- **Type:** `(string | RegExp)[]`
- **Default:** [`moduleDirectories`](https://vitest.dev/config/deps#moduledirectories) 내부 파일

Vite로 변환하지 않고 엔진에서 직접 처리해야 하는 모듈을 지정합니다. 이러한 모듈은 네이티브 동적 `import`를 통해 가져오며, 변환 및 해석 단계 모두를 우회합니다.

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    server: {
      deps: {
        external: ["react"],
      },
    },
  },
});
```

외부 모듈과 그 의존성은 모듈 그래프에 포함되지 않으며, 변경되어도 테스트 재시작을 트리거하지 않습니다.

일반적으로 `node_modules` 아래의 패키지는 외부화됩니다.

::: tip
문자열이 제공되면 먼저 `/node_modules/` 또는 다른 [`moduleDirectories`](https://vitest.dev/config/deps#moduledirectories) 세그먼트를 접두사로 붙여 정규화한 뒤(예: `'react'`는 `/node_modules/react/`가 됨), 그 결과 문자열을 전체 파일 경로와 매칭합니다. 예를 들어 `packages/some-name` 안에 있는 패키지 `@company/some-name`은 `some-name`으로 지정해야 하며, `packages`는 `deps.moduleDirectories`에 포함되어야 합니다.

`RegExp`가 제공되면 전체 파일 경로를 기준으로 매칭합니다.
:::

### inline

- **Type:** `(string | RegExp)[] | true`
- **Default:** 외부화되지 않은 모든 항목

Vite에 의해 변환 및 해석되어야 하는 모듈을 지정합니다. 이러한 모듈은 Vite의 [module runner](https://vite.dev/guide/api-environment-runtimes#modulerunner)에서 실행됩니다.

일반적으로 소스 파일은 인라인됩니다.

::: tip
문자열이 제공되면 먼저 `/node_modules/` 또는 다른 [`moduleDirectories`](https://vitest.dev/config/deps#moduledirectories) 세그먼트를 접두사로 붙여 정규화한 뒤(예: `'react'`는 `/node_modules/react/`가 됨), 그 결과 문자열을 전체 파일 경로와 매칭합니다. 예를 들어 `packages/some-name` 안에 있는 패키지 `@company/some-name`은 `some-name`으로 지정해야 하며, `packages`는 `deps.moduleDirectories`에 포함되어야 합니다.

`RegExp`가 제공되면 전체 파일 경로를 기준으로 매칭합니다.
:::

### fallbackCJS

- **Type:** `boolean`
- **Default:** `false`

의존성이 유효한 ESM 패키지일 때, 경로를 기반으로 cjs 버전을 추측하도록 시도합니다. 의존성에 잘못된 ESM 파일이 있을 경우 도움이 될 수 있습니다.

패키지가 ESM 모드와 CJS 모드에서 서로 다른 로직을 갖고 있다면 잠재적으로 일부 불일치가 발생할 수 있습니다.
