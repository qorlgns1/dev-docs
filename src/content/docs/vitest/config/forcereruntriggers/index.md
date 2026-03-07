---
title: "forceRerunTriggers"
description: "전체 스위트 재실행을 트리거하는 파일 경로의 Glob 패턴입니다.  인자와 함께 사용하면, git diff에서 트리거가 발견될 때 전체 테스트 스위트를 실행합니다."
---

출처 URL: https://vitest.dev/config/forcereruntriggers

# forceRerunTriggers

- **Type**: `string[]`
- **Default:** `['**/package.json/**', '**/vitest.config.*/**', '**/vite.config.*/**']`

전체 스위트 재실행을 트리거하는 파일 경로의 Glob 패턴입니다. `--changed` 인자와 함께 사용하면, git diff에서 트리거가 발견될 때 전체 테스트 스위트를 실행합니다.

Vite는 모듈 그래프를 구성할 수 없기 때문에, CLI 명령 호출을 테스트하는 경우에 유용합니다:

```ts
test("execute a script", async () => {
  // Vitest cannot rerun this test, if content of `dist/index.js` changes
  await execa("node", ["dist/index.js"]);
});
```

::: tip
파일이 [`server.watch.ignored`](https://vitejs.dev/config/server-options.html#server-watch)에 의해 제외되지 않도록 하세요.
:::
