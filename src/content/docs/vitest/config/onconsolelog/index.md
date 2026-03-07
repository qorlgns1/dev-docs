---
title: "onConsoleLog"
description: "function onConsoleLog("
---

출처 URL: https://vitest.dev/config/onconsolelog

# onConsoleLog

```ts
function onConsoleLog(
  log: string,
  type: "stdout" | "stderr",
  entity: TestModule | TestSuite | TestCase | undefined,
): boolean | void;
```

테스트에서 `console` 메서드에 대한 커스텀 핸들러입니다. `false`를 반환하면 Vitest는 해당 로그를 콘솔에 출력하지 않습니다. Vitest는 그 외의 다른 falsy 값은 모두 무시합니다.

서드파티 라이브러리에서 발생하는 로그를 필터링할 때 유용할 수 있습니다.

```ts
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    onConsoleLog(log: string, type: "stdout" | "stderr"): boolean | void {
      return !(log === "message from third party library" && type === "stdout");
    },
  },
});
```
