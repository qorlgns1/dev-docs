---
title: "onStackTrace"
description: "오류를 처리할 때 각 스택 트레이스의 각 프레임에 필터링 함수를 적용합니다. 이는 로 출력된 스택 트레이스에는 적용되지 않습니다. 첫 번째 인수인 는 입니다."
---

출처 URL: https://vitest.dev/config/onstacktrace

# onStackTrace

- **Type**: `(error: Error, frame: ParsedStack) => boolean | void`

오류를 처리할 때 각 스택 트레이스의 각 프레임에 필터링 함수를 적용합니다. 이는 [`printConsoleTrace`](https://vitest.dev/config/printconsoletrace#printconsoletrace)로 출력된 스택 트레이스에는 적용되지 않습니다. 첫 번째 인수인 `error`는 `TestError`입니다.

서드파티 라이브러리의 스택 트레이스 프레임을 필터링하는 데 유용할 수 있습니다.

::: tip
스택 트레이스의 전체 크기는 일반적으로 V8의 [`Error.stackTraceLimit`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stackTraceLimit) 값에 의해서도 제한됩니다. 스택이 잘리지 않도록 테스트 설정 함수에서 이 값을 크게 설정할 수 있습니다.
:::

```ts
import type { ParsedStack, TestError } from "vitest";
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    onStackTrace(error: TestError, { file }: ParsedStack): boolean | void {
      // If we've encountered a ReferenceError, show the whole stack.
      if (error.name === "ReferenceError") {
        return;
      }

      // Reject all frames from third party libraries.
      if (file.includes("node_modules")) {
        return false;
      }
    },
  },
});
```
