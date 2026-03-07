---
title: "dangerouslyIgnoreUnhandledErrors"
description: "If this option is set to , Vitest will not fail the test run if there are unhandled errors. Note that built-in reporters will still report them."
---

Source URL: https://vitest.dev/config/dangerouslyignoreunhandlederrors

# dangerouslyIgnoreUnhandledErrors

- **Type**: `boolean`
- **Default**: `false`
- **CLI:**
  - `--dangerouslyIgnoreUnhandledErrors`
  - `--dangerouslyIgnoreUnhandledErrors=false`

If this option is set to `true`, Vitest will not fail the test run if there are unhandled errors. Note that built-in reporters will still report them.

If you want to filter out certain errors conditionally, use [`onUnhandledError`](https://vitest.dev/config/onunhandlederror) callback instead.

## Example

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    dangerouslyIgnoreUnhandledErrors: true,
  },
});
```
