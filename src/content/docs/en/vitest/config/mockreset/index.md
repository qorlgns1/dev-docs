---
title: "mockReset"
description: "Should Vitest automatically call  before each test."
---

Source URL: https://vitest.dev/config/mockreset

# mockReset

- **Type:** `boolean`
- **Default:** `false`

Should Vitest automatically call [`vi.resetAllMocks()`](https://vitest.dev/api/vi#vi-resetallmocks) before each test.

This will clear mock history and reset each implementation.

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    mockReset: true,
  },
});
```
