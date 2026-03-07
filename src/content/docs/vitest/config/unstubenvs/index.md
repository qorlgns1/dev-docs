---
title: "unstubEnvs"
description: "Vitest가 각 테스트 전에 를 자동으로 호출할지 여부입니다."
---

출처 URL: https://vitest.dev/config/unstubenvs

# unstubEnvs

- **Type:** `boolean`
- **Default:** `false`

Vitest가 각 테스트 전에 [`vi.unstubAllEnvs()`](https://vitest.dev/api/vi#vi-unstuballenvs)를 자동으로 호출할지 여부입니다.

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    unstubEnvs: true,
  },
});
```
