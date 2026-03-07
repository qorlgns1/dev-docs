---
title: "인소스 테스트"
description: "Vitest는 Rust의 모듈 테스트와 유사하게, 구현 코드와 함께 소스 코드 내부에서 테스트를 실행하는 방법을 제공합니다."
---

출처 URL: https://vitest.dev/guide/in-source

# 인소스 테스트

Vitest는 [Rust의 모듈 테스트](https://doc.rust-lang.org/book/ch11-03-test-organization.html#the-tests-module-and-cfgtest)와 유사하게, 구현 코드와 함께 소스 코드 내부에서 테스트를 실행하는 방법을 제공합니다.

이 방식은 테스트가 구현과 동일한 클로저를 공유하므로 export 없이도 private 상태를 대상으로 테스트할 수 있습니다. 동시에 개발 피드백 루프도 더 짧아집니다.

::: warning
이 가이드는 소스 코드 내부에 테스트를 작성하는 방법을 설명합니다. 별도의 테스트 파일에 테스트를 작성해야 한다면 ["Writing Tests" 가이드](https://vitest.dev/guide/#writing-tests)를 따르세요.
:::

## 설정

시작하려면 소스 파일의 끝에 `if (import.meta.vitest)` 블록을 두고 그 안에 테스트를 작성하세요. 예를 들면:

```ts [src/index.ts]
// the implementation
export function add(...args: number[]) {
  return args.reduce((a, b) => a + b, 0);
}

// in-source test suites
if (import.meta.vitest) {
  const { it, expect } = import.meta.vitest;
  it("add", () => {
    expect(add()).toBe(0);
    expect(add(1)).toBe(1);
    expect(add(1, 2, 3)).toBe(6);
  });
}
```

Vitest가 `src/` 아래 파일을 가져오도록 `includeSource` 설정을 업데이트하세요:

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    includeSource: ["src/**/*.{js,ts}"], // [!code ++]
  },
});
```

이제 테스트를 시작할 수 있습니다!

```bash
$ npx vitest
```

## 프로덕션 빌드

프로덕션 빌드에서는 번들러가 dead code elimination을 수행할 수 있도록 설정 파일에서 `define` 옵션을 지정해야 합니다. 예를 들어 Vite에서는 다음과 같습니다.

```ts [vite.config.ts]
/// <reference types="vitest/config" />

import { defineConfig } from "vite";

export default defineConfig({
  test: {
    includeSource: ["src/**/*.{js,ts}"],
  },
  define: {
    // [!code ++]
    "import.meta.vitest": "undefined", // [!code ++]
  }, // [!code ++]
});
```

### 기타 번들러

::: details Rolldown

```js [rolldown.config.js]
import { defineConfig } from "rolldown/config";

export default defineConfig({
  transform: {
    define: {
      // [!code ++]
      "import.meta.vitest": "undefined", // [!code ++]
    }, // [!code ++]
  },
});
```

더 알아보기: [Rolldown](https://rolldown.rs/)
:::

::: details Rollup

```js [rollup.config.js]
import replace from "@rollup/plugin-replace"; // [!code ++]

export default {
  plugins: [
    replace({
      // [!code ++]
      "import.meta.vitest": "undefined", // [!code ++]
    }), // [!code ++]
  ],
  // other options
};
```

더 알아보기: [Rollup](https://rollupjs.org/)
:::

::: details unbuild

```js [build.config.js]
import { defineBuildConfig } from "unbuild";

export default defineBuildConfig({
  replace: {
    // [!code ++]
    "import.meta.vitest": "undefined", // [!code ++]
  }, // [!code ++]
  // other options
});
```

더 알아보기: [unbuild](https://github.com/unjs/unbuild)
:::

::: details webpack

```js [webpack.config.js]
const webpack = require("webpack");

module.exports = {
  plugins: [
    new webpack.DefinePlugin({
      // [!code ++]
      "import.meta.vitest": "undefined", // [!code ++]
    }), // [!code ++]
  ],
};
```

더 알아보기: [webpack](https://webpack.js.org/plugins/define-plugin/)
:::

## TypeScript

`import.meta.vitest`에 대한 TypeScript 지원을 활성화하려면 `tsconfig.json`에 `vitest/importMeta`를 추가하세요:

```json [tsconfig.json]
{
  "compilerOptions": {
    "types": [
      "vitest/importMeta" // [!code ++]
    ]
  }
}
```

전체 예시는 [`examples/in-source-test`](https://github.com/vitest-dev/vitest/tree/main/examples/in-source-test)를 참고하세요.

## 참고

이 기능은 다음과 같은 경우에 유용할 수 있습니다:

- 범위가 작은 함수 또는 유틸리티의 단위 테스트
- 프로토타이핑
- 인라인 Assertion

컴포넌트 테스트나 E2E 테스트처럼 더 복잡한 테스트의 경우에는 **대신 별도의 테스트 파일을 사용하는 것**을 권장합니다.
