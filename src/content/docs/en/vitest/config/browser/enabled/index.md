---
title: "browser.enabled"
description: "Enabling this flag makes Vitest run all tests in a browser by default. If you are configuring other browser options via the CLI, you can use  alongsid..."
---

Source URL: https://vitest.dev/config/browser/enabled

# browser.enabled

- **Type:** `boolean`
- **Default:** `false`
- **CLI:** `--browser`, `--browser.enabled=false`

Enabling this flag makes Vitest run all tests in a [browser](https://vitest.dev/guide/browser/) by default. If you are configuring other browser options via the CLI, you can use `--browser.enabled` alongside them instead of `--browser`:

```sh
vitest --browser.enabled --browser.headless
```

::: warning
To enable [Browser Mode](https://vitest.dev/guide/browser/), you must also specify the [`provider`](https://vitest.dev/config/browser/provider) and at least one [`instance`](https://vitest.dev/config/browser/instances). Available providers:

- playwright
- webdriverio
- preview
  :::

## Example

```js{7} [vitest.config.js]
import { defineConfig } from 'vitest/config'
import { playwright } from '@vitest/browser-playwright'

export default defineConfig({
  test: {
    browser: {
      enabled: true,
      provider: playwright(),
      instances: [
        { browser: 'chromium' },
      ],
    },
  },
})
```

If you use TypeScript, the `browser` field in `instances` provides autocompletion based on your provider.
