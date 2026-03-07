---
title: "environment"
description: "테스트에 사용될 환경입니다. Vitest의 기본 환경은 Node.js 환경입니다. 웹 애플리케이션을 빌드하는 경우, 대신  또는 을 통해 브라우저와 유사한 환경을 사용할 수 있습니다."
---

출처 URL: https://vitest.dev/config/environment

# environment

- **Type:** `'node' | 'jsdom' | 'happy-dom' | 'edge-runtime' | string`
- **Default:** `'node'`
- **CLI:** `--environment=<env>`

테스트에 사용될 환경입니다. Vitest의 기본 환경은 Node.js 환경입니다. 웹 애플리케이션을 빌드하는 경우, 대신 [`jsdom`](https://github.com/jsdom/jsdom) 또는 [`happy-dom`](https://github.com/capricorn86/happy-dom)을 통해 브라우저와 유사한 환경을 사용할 수 있습니다.
엣지 함수를 빌드하는 경우 [`edge-runtime`](https://edge-runtime.vercel.app/packages/vm) 환경을 사용할 수 있습니다.

::: tip
환경을 mocking하지 않고 브라우저에서 통합 테스트 또는 단위 테스트를 실행하려면 [Browser Mode](https://vitest.dev/guide/browser/)를 사용할 수도 있습니다.
:::

환경에 대한 사용자 정의 옵션을 정의하려면 [`environmentOptions`](https://vitest.dev/config/environmentoptions)를 사용하세요.

파일 상단에 `@vitest-environment` docblock 또는 주석을 추가하면,
해당 파일의 모든 테스트에 사용할 다른 환경을 지정할 수 있습니다:

Docblock 스타일:

```js
/**
 * @vitest-environment jsdom
 */

test("use jsdom in this test file", () => {
  const element = document.createElement("div");
  expect(element).not.toBeNull();
});
```

주석 스타일:

```js
// @vitest-environment happy-dom

test("use happy-dom in this test file", () => {
  const element = document.createElement("div");
  expect(element).not.toBeNull();
});
```

Jest 호환성을 위해 `@jest-environment`도 지원됩니다:

```js
/**
 * @jest-environment jsdom
 */

test("use jsdom in this test file", () => {
  const element = document.createElement("div");
  expect(element).not.toBeNull();
});
```

사용자 정의 환경도 정의할 수 있습니다. 내장되지 않은 환경을 사용할 때, 이름이 상대 또는 절대 경로라면 Vitest는 해당 파일을 로드하려고 시도하고, 이름이 bare specifier라면 `vitest-environment-${name}` 패키지를 로드하려고 시도합니다.

사용자 정의 환경 파일은 `Environment` 형태의 객체를 export해야 합니다:

```ts [environment.js]
import type { Environment } from "vitest";

export default <Environment>{
  name: "custom",
  viteEnvironment: "ssr",
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

::: tip
`viteEnvironment` 필드는 [Vite Environment API](https://vite.dev/guide/api-environment#environment-api)에서 정의한 환경에 해당합니다. 기본적으로 Vite는 `client`(브라우저용)와 `ssr`(서버용) 환경을 노출합니다.
:::

Vitest는 단순히 확장만 하고 싶을 때를 위해 `vitest/environments` 엔트리를 통해 `builtinEnvironments`도 제공합니다. 환경 확장에 대한 자세한 내용은 [가이드](https://vitest.dev/guide/environment)에서 확인할 수 있습니다.

::: tip
jsdom 환경은 현재 [JSDOM](https://github.com/jsdom/jsdom) 인스턴스와 동일한 `jsdom` 전역 변수를 노출합니다. 이 환경을 사용할 때 TypeScript가 이를 인식하게 하려면 `tsconfig.json`에 `vitest/jsdom`을 추가할 수 있습니다:

```json [tsconfig.json]
{
  "compilerOptions": {
    "types": ["vitest/jsdom"]
  }
}
```

:::
