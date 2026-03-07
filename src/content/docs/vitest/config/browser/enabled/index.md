---
title: "browser.enabled"
description: "이 플래그를 활성화하면 Vitest가 기본적으로 모든 테스트를 browser에서 실행합니다. CLI를 통해 다른 browser 옵션도 함께 설정하는 경우,  대신 를 함께 사용할 수 있습니다:"
---

출처 URL: https://vitest.dev/config/browser/enabled

# browser.enabled

- **Type:** `boolean`
- **Default:** `false`
- **CLI:** `--browser`, `--browser.enabled=false`

이 플래그를 활성화하면 Vitest가 기본적으로 모든 테스트를 [browser](https://vitest.dev/guide/browser/)에서 실행합니다. CLI를 통해 다른 browser 옵션도 함께 설정하는 경우, `--browser` 대신 `--browser.enabled`를 함께 사용할 수 있습니다:

```sh
vitest --browser.enabled --browser.headless
```

::: warning
[Browser Mode](https://vitest.dev/guide/browser/)를 활성화하려면 [`provider`](https://vitest.dev/config/browser/provider)와 최소 하나의 [`instance`](https://vitest.dev/config/browser/instances)도 지정해야 합니다. 사용 가능한 provider는 다음과 같습니다.

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

TypeScript를 사용하는 경우 `instances`의 `browser` 필드는 provider에 따라 자동 완성을 제공합니다.
