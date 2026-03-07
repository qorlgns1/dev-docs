---
title: "restoreMocks"
description: "Should Vitest automatically call  before each test."
---

Source URL: https://vitest.dev/config/restoremocks

# restoreMocks

- **Type:** `boolean`
- **Default:** `false`

Should Vitest automatically call [`vi.restoreAllMocks()`](https://vitest.dev/api/vi#vi-restoreallmocks) before each test.

This restores all original implementations on spies created manually with [`vi.spyOn`](https://vitest.dev/api/vi#vi-spyon).

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    restoreMocks: true,
  },
});
```
