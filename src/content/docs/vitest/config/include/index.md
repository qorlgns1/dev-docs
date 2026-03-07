---
title: "include"
description: "테스트 파일과 일치하는 glob 패턴 목록입니다. 이 패턴들은 를 기준으로 해석됩니다(기본값은 )."
---

출처 URL: https://vitest.dev/config/include

# include

- **유형:** `string[]`
- **기본값:** `['**/*.{test,spec}.?(c|m)[jt]s?(x)']`
- **CLI:** `vitest [...include]`, `vitest **/*.test.js`

테스트 파일과 일치하는 [glob 패턴](https://superchupu.dev/tinyglobby/comparison) 목록입니다. 이 패턴들은 [`root`](https://vitest.dev/config/root)를 기준으로 해석됩니다(기본값은 [`process.cwd()`](https://nodejs.org/api/process.html#processcwd)).

Vitest는 glob을 해석하기 위해 [`tinyglobby`](https://www.npmjs.com/package/tinyglobby) 패키지를 사용합니다.

::: tip 참고
coverage를 사용할 때 Vitest는 테스트 파일의 `include` 패턴을 coverage의 기본 `exclude` 패턴에 자동으로 추가합니다. [`coverage.exclude`](https://vitest.dev/config/coverage#exclude)를 참고하세요.
:::

## 예시

```js
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    include: ["./test", "./**/*.{test,spec}.tsx?"],
  },
});
```

Vitest는 합리적인 기본값을 제공하므로, 일반적으로 이를 재정의할 필요가 없습니다. `include`를 정의하는 좋은 예시는 [test projects](https://vitest.dev/guide/projects)입니다:

```js{8,12} [vitest.config.js]
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    projects: [
      {
        name: 'unit',
        include: ['./test/unit/*.test.js'],
      },
      {
        name: 'e2e',
        include: ['./test/e2e/*.test.js'],
      },
    ],
  },
})
```

::: warning
이 옵션은 Vitest 기본값을 덮어씁니다. 기본값을 단순히 확장하고 싶다면 `vitest/config`의 `configDefaults`를 사용하세요:

```js{6}
import { configDefaults, defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    include: [
      ...configDefaults.include,
      './test',
      './**/*.{test,spec}.tsx?',
    ],
  },
})
```

:::
