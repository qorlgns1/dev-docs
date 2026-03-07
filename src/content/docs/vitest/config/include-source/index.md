---
title: "includeSource"
description: "정의하면, Vitest는 내부에 가 있는 일치 파일을 모두 실행합니다."
---

출처 URL: https://vitest.dev/config/include-source

# includeSource

- **타입:** `string[]`
- **기본값:** `[]`

[인소스 테스트 파일](https://vitest.dev/guide/in-source)과 일치하는 [glob 패턴](https://superchupu.dev/tinyglobby/comparison) 목록입니다. 이 패턴들은 [`root`](https://vitest.dev/config/root)를 기준으로 해석됩니다(기본값은 [`process.cwd()`](https://nodejs.org/api/process.html#processcwd)).

정의하면, Vitest는 내부에 `import.meta.vitest`가 있는 일치 파일을 모두 실행합니다.

::: warning
Vitest는 소스 파일에 대해 단순한 텍스트 기반 포함 검사를 수행합니다. 파일에 주석 안이라도 `import.meta.vitest`가 포함되어 있으면 인소스 테스트 파일로 매칭됩니다.
:::

Vitest는 glob을 해석하기 위해 [`tinyglobby`](https://www.npmjs.com/package/tinyglobby) 패키지를 사용합니다.

## 예시

```js
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    includeSource: ["src/**/*.{js,ts}"],
  },
});
```

그다음 소스 파일 안에 테스트를 작성할 수 있습니다:

```ts [src/index.ts]
export function add(...args: number[]) {
  return args.reduce((a, b) => a + b, 0);
}

// #region in-source test suites
if (import.meta.vitest) {
  const { it, expect } = import.meta.vitest;
  it("add", () => {
    expect(add()).toBe(0);
    expect(add(1)).toBe(1);
    expect(add(1, 2, 3)).toBe(6);
  });
}
// #endregion
```

프로덕션 빌드에서는 `import.meta.vitest`를 `undefined`로 치환해야 하며, 이렇게 하면 번들러가 dead code elimination을 수행할 수 있습니다.

::: code-group

```js [vite.config.ts]
import { defineConfig } from "vite";

export default defineConfig({
  define: {
    // [!code ++]
    "import.meta.vitest": "undefined", // [!code ++]
  }, // [!code ++]
});
```

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

:::

::: tip
`import.meta.vitest`에 대한 TypeScript 지원을 받으려면 `tsconfig.json`에 `vitest/importMeta`를 추가하세요:

```json [tsconfig.json]
{
  "compilerOptions": {
    "types": ["vitest/importMeta"]
  }
}
```

:::
