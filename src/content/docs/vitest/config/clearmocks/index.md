---
title: "clearMocks"
description: "각 테스트 전에 Vitest가 를 자동으로 호출할지 여부를 설정합니다."
---

출처 URL: https://vitest.dev/config/clearmocks

# clearMocks

- **타입:** `boolean`
- **기본값:** `false`

각 테스트 전에 Vitest가 [`vi.clearAllMocks()`](https://vitest.dev/api/vi#vi-clearallmocks)를 자동으로 호출할지 여부를 설정합니다.

이 설정은 mock 구현에는 영향을 주지 않고 mock 히스토리만 지웁니다.

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    clearMocks: true,
  },
});
```
