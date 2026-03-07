---
title: "unstubGlobals"
description: "각 테스트 전에 Vitest가 를 자동으로 호출할지 여부입니다."
---

출처 URL: https://vitest.dev/config/unstubglobals

# unstubGlobals

- **타입:** `boolean`
- **기본값:** `false`

각 테스트 전에 Vitest가 [`vi.unstubAllGlobals()`](https://vitest.dev/api/vi#vi-unstuballglobals)를 자동으로 호출할지 여부입니다.

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    unstubGlobals: true,
  },
});
```
