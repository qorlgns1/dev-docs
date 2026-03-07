---
title: "dangerouslyIgnoreUnhandledErrors"
description: "이 옵션을 로 설정하면, 처리되지 않은 오류가 있더라도 Vitest는 테스트 실행을 실패로 처리하지 않습니다. 내장 리포터는 여전히 해당 오류를 보고한다는 점에 유의하세요."
---

출처 URL: https://vitest.dev/config/dangerouslyignoreunhandlederrors

# dangerouslyIgnoreUnhandledErrors

- **Type**: `boolean`
- **Default**: `false`
- **CLI:**
  - `--dangerouslyIgnoreUnhandledErrors`
  - `--dangerouslyIgnoreUnhandledErrors=false`

이 옵션을 `true`로 설정하면, 처리되지 않은 오류가 있더라도 Vitest는 테스트 실행을 실패로 처리하지 않습니다. 내장 리포터는 여전히 해당 오류를 보고한다는 점에 유의하세요.

특정 오류를 조건부로 제외하고 싶다면, 대신 [`onUnhandledError`](https://vitest.dev/config/onunhandlederror) 콜백을 사용하세요.

## 예시

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    dangerouslyIgnoreUnhandledErrors: true,
  },
});
```
