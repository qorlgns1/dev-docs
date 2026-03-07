---
title: "onUnhandledError 4.0.0"
description: "function onUnhandledError("
---

출처 URL: https://vitest.dev/config/onunhandlederror

# onUnhandledError 4.0.0

- **타입:**

```ts
function onUnhandledError(
  error: (TestError | Error) & { type: string },
): boolean | void;
```

보고되면 안 되는 처리되지 않은 오류를 필터링하기 위한 사용자 정의 콜백입니다. 오류가 필터링되면 더 이상 테스트 실행 결과에 영향을 주지 않습니다.

테스트 결과에 영향을 주지 않으면서 처리되지 않은 오류를 보고하려면 [`dangerouslyIgnoreUnhandledErrors`](https://vitest.dev/config/dangerouslyignoreunhandlederrors) 옵션을 대신 사용하세요.

::: tip
이 콜백은 메인 스레드에서 호출되므로 테스트 컨텍스트에 접근할 수 없습니다.
:::

## 예시

```ts
import type { ParsedStack } from "vitest";
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    onUnhandledError(error): boolean | void {
      // Ignore all errors with the name "MySpecialError".
      if (error.name === "MySpecialError") {
        return false;
      }
    },
  },
});
```
