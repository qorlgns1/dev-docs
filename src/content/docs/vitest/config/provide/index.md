---
title: "provide"
description: "메서드를 사용해 테스트 내부에서 접근할 수 있는 값을 정의합니다."
---

출처 URL: https://vitest.dev/config/provide

# provide

- **유형:** `Partial<ProvidedContext>`

`inject` 메서드를 사용해 테스트 내부에서 접근할 수 있는 값을 정의합니다.

:::code-group

```ts [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    provide: {
      API_KEY: "123",
    },
  },
});
```

```ts [api.test.js]
import { expect, inject, test } from "vitest";

test("api key is defined", () => {
  expect(inject("API_KEY")).toBe("123");
});
```

:::

::: warning
이 객체는 서로 다른 프로세스 간에 전송되므로, 프로퍼티는 문자열이어야 하고 값은 [직렬화 가능](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm#supported_types)해야 합니다.
:::

::: tip
TypeScript를 사용 중이라면 타입 안전한 접근을 위해 `ProvidedContext` 타입을 보강해야 합니다:

```ts [vitest.shims.d.ts]
declare module "vitest" {
  export interface ProvidedContext {
    API_KEY: string;
  }
}

// mark this file as a module so augmentation works correctly
export {};
```

:::
