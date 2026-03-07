---
title: "globals"
description: "기본적으로 는 명시성을 위해 전역 API를 제공하지 않습니다. Jest처럼 API를 전역으로 사용하고 싶다면, CLI에  옵션을 전달하거나 설정에 를 추가할 수 있습니다."
---

출처 URL: https://vitest.dev/config/globals

# globals

- **타입:** `boolean`
- **기본값:** `false`
- **CLI:** `--globals`, `--no-globals`, `--globals=false`

기본적으로 `vitest`는 명시성을 위해 전역 API를 제공하지 않습니다. Jest처럼 API를 전역으로 사용하고 싶다면, CLI에 `--globals` 옵션을 전달하거나 설정에 `globals: true`를 추가할 수 있습니다.

```js
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    globals: true,
  },
});
```

::: tip
`@testing-library/react` 같은 일부 라이브러리는 자동 정리를 수행하기 위해 전역이 존재하는 것에 의존한다는 점에 유의하세요.
:::

전역 API와 함께 TypeScript가 동작하도록 하려면, `tsconfig.json`의 `types` 필드에 `vitest/globals`를 추가하세요:

```json [tsconfig.json]
{
  "compilerOptions": {
    "types": ["vitest/globals"]
  }
}
```

컴파일에 추가 타입을 포함하도록 [`typeRoots`](https://www.typescriptlang.org/tsconfig/#typeRoots)를 재정의한 경우, `vitest/globals`를 찾을 수 있도록 `node_modules`를 다시 추가해야 합니다:

```json [tsconfig.json]
{
  "compilerOptions": {
    "typeRoots": ["./types", "./node_modules/@types", "./node_modules"],
    "types": ["vitest/globals"]
  }
}
```
