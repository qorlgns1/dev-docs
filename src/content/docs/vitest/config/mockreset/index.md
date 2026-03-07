---
title: "mockReset"
description: "Vitest가 각 테스트 전에 를 자동으로 호출할지 여부를 설정합니다."
---

출처 URL: https://vitest.dev/config/mockreset

# mockReset

- **Type:** `boolean`
- **Default:** `false`

Vitest가 각 테스트 전에 [`vi.resetAllMocks()`](https://vitest.dev/api/vi#vi-resetallmocks)를 자동으로 호출할지 여부를 설정합니다.

이 옵션을 활성화하면 mock 기록이 지워지고 각 구현이 초기화됩니다.

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    mockReset: true,
  },
});
```
