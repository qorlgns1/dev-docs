---
title: "unstubGlobals"
description: "Should Vitest automatically call  before each test."
---

Source URL: https://vitest.dev/config/unstubglobals

# unstubGlobals

- **Type:** `boolean`
- **Default:** `false`

Should Vitest automatically call [`vi.unstubAllGlobals()`](https://vitest.dev/api/vi#vi-unstuballglobals) before each test.

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    unstubGlobals: true,
  },
});
```
