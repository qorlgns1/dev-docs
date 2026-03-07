---
title: "테스트 환경"
description: "Vitest는 특정 환경 내부에서 코드를 실행하기 위한  옵션을 제공합니다.  옵션으로 환경의 동작 방식을 수정할 수 있습니다."
---

출처 URL: https://vitest.dev/guide/environment

# 테스트 환경

Vitest는 특정 환경 내부에서 코드를 실행하기 위한 [`environment`](https://vitest.dev/config/#environment) 옵션을 제공합니다. [`environmentOptions`](https://vitest.dev/config/#environmentoptions) 옵션으로 환경의 동작 방식을 수정할 수 있습니다.

기본적으로 다음 환경을 사용할 수 있습니다:

- `node`는 기본 환경입니다
- `jsdom`은 Browser API를 제공해 브라우저 환경을 에뮬레이션하며, [`jsdom`](https://github.com/jsdom/jsdom) 패키지를 사용합니다
- `happy-dom`도 Browser API를 제공해 브라우저 환경을 에뮬레이션하며, jsdom보다 빠른 것으로 여겨지지만 일부 API가 부족하고, [`happy-dom`](https://github.com/capricorn86/happy-dom) 패키지를 사용합니다
- `edge-runtime`은 Vercel의 [edge-runtime](https://edge-runtime.vercel.app/)을 에뮬레이션하며, [`@edge-runtime/vm`](https://www.npmjs.com/package/@edge-runtime/vm) 패키지를 사용합니다

::: info
`jsdom` 또는 `happy-dom` 환경을 사용할 때, Vitest는 [CSS](https://vitejs.dev/guide/features.html#css)와 [assets](https://vitejs.dev/guide/features.html#static-assets)를 import할 때 Vite와 동일한 규칙을 따릅니다. 외부 의존성 import 시 `unknown extension .css` 오류가 발생하면, 모든 패키지를 [`server.deps.inline`](https://vitest.dev/config/#server-deps-inline)에 추가해 전체 import 체인을 수동으로 inline해야 합니다. 예를 들어 `source code -> package-1 -> package-2 -> package-3` import 체인에서 `package-3`에서 오류가 발생했다면, 세 패키지 모두를 `server.deps.inline`에 추가해야 합니다.

외부 의존성 내부의 CSS와 assets에 대한 `require`는 자동으로 resolve됩니다.
:::

::: warning
"Environments"는 Node.js에서 테스트를 실행할 때만 존재합니다.

Vitest에서 `browser`는 환경으로 간주되지 않습니다. 테스트 일부를 [Browser Mode](https://vitest.dev/guide/browser/)로 실행하려면 [test project](https://vitest.dev/guide/browser/#projects-config)를 생성할 수 있습니다.
:::

## 특정 파일용 환경

설정 파일에서 `environment` 옵션을 설정하면 프로젝트의 모든 테스트 파일에 적용됩니다. 더 세밀하게 제어하려면 제어 주석을 사용해 특정 파일의 환경을 지정할 수 있습니다. 제어 주석은 `@vitest-environment`로 시작하고 뒤에 환경 이름이 따라옵니다:

```ts
// @vitest-environment jsdom

import { expect, test } from "vitest";

test("test", () => {
  expect(typeof window).not.toBe("undefined");
});
```

## 커스텀 환경

Vitest 환경을 확장하기 위해 자체 패키지를 만들 수 있습니다. 이를 위해 `vitest-environment-${name}` 형식의 이름으로 패키지를 만들거나, 유효한 JS/TS 파일 경로를 지정하세요. 해당 패키지는 `Environment` 형태의 객체를 export해야 합니다:

```ts
import type { Environment } from "vitest/environments";

export default <Environment>{
  name: "custom",
  viteEnvironment: "ssr",
  // optional - only if you support "experimental-vm" pool
  async setupVM() {
    const vm = await import("node:vm");
    const context = vm.createContext();
    return {
      getVmContext() {
        return context;
      },
      teardown() {
        // called after all tests with this env have been run
      },
    };
  },
  setup() {
    // custom setup
    return {
      teardown() {
        // called after all tests with this env have been run
      },
    };
  },
};
```

::: warning
Vitest는 환경 객체에 `viteEnvironment` 옵션이 필요합니다(기본적으로는 Vitest 환경 이름으로 fallback). 이 값은 `ssr`, `client`, 또는 임의의 커스텀 [Vite environment](https://vite.dev/guide/api-environment) 이름과 같아야 합니다. 이 값은 파일을 처리할 때 어떤 환경을 사용할지 결정합니다.
:::

`vitest/environments` 엔트리를 통해 기본 Vitest 환경에도 접근할 수 있습니다:

```ts
import { builtinEnvironments, populateGlobal } from "vitest/environments";

console.log(builtinEnvironments); // { jsdom, happy-dom, node, edge-runtime }
```

Vitest는 `populateGlobal` 유틸리티 함수도 제공합니다. 이 함수는 객체의 속성을 전역 네임스페이스로 옮길 때 사용할 수 있습니다:

```ts
interface PopulateOptions {
  // should non-class functions be bind to the global namespace
  bindFunctions?: boolean;
}

interface PopulateResult {
  // a list of all keys that were copied, even if value doesn't exist on original object
  keys: Set<string>;
  // a map of original object that might have been overridden with keys
  // you can return these values inside `teardown` function
  originals: Map<string | symbol, any>;
}

export function populateGlobal(
  global: any,
  original: any,
  options: PopulateOptions,
): PopulateResult;
```
