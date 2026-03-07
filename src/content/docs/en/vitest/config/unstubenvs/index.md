---
title: "unstubEnvs"
description: "Should Vitest automatically call  before each test."
---

Source URL: https://vitest.dev/config/unstubenvs

# unstubEnvs

- **Type:** `boolean`
- **Default:** `false`

Should Vitest automatically call [`vi.unstubAllEnvs()`](https://vitest.dev/api/vi#vi-unstuballenvs) before each test.

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    unstubEnvs: true,
  },
});
```
