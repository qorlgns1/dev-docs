---
title: "WebdriverIO 구성하기"
description: "::: info Playwright vs WebdriverIO"
---

출처 URL: https://vitest.dev/config/browser/webdriverio

# WebdriverIO 구성하기

::: info Playwright vs WebdriverIO
프로젝트에서 아직 WebdriverIO를 사용하고 있지 않다면, 설정이 더 쉽고 API가 더 유연한 [Playwright](https://vitest.dev/config/browser/playwright)로 시작하는 것을 권장합니다.
:::

WebdriverIO를 사용해 테스트를 실행하려면, [`@vitest/browser-webdriverio`](https://www.npmjs.com/package/@vitest/browser-webdriverio) npm 패키지를 설치하고, config의 `test.browser.provider` 속성에 해당 패키지의 `webdriverio` export를 지정해야 합니다:

```ts [vitest.config.js]
import { webdriverio } from "@vitest/browser-webdriverio";
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    browser: {
      provider: webdriverio(),
      instances: [{ browser: "chrome" }],
    },
  },
});
```

[`remote`](https://webdriver.io/docs/api/modules/#remoteoptions-modifier) 함수가 받을 수 있는 모든 파라미터를 설정할 수 있습니다:

```ts{8-12,19-25} [vitest.config.js]
import { webdriverio } from '@vitest/browser-webdriverio'
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    browser: {
      // shared provider options between all instances
      provider: webdriverio({
        capabilities: {
          browserVersion: '82',
        },
      }),
      instances: [
        { browser: 'chrome' },
        {
          browser: 'firefox',
          // overriding options only for a single instance
          // this will NOT merge options with the parent one
          provider: webdriverio({
            capabilities: {
              'moz:firefoxOptions': {
                args: ['--disable-gpu'],
              },
            },
          })
        },
      ],
    },
  },
})
```

대부분의 사용 가능한 옵션은 [WebdriverIO 문서](https://webdriver.io/docs/configuration/)에서 확인할 수 있습니다. Vitest는 `webdriverio`의 브라우저 기능만 사용하므로 모든 테스트 러너 옵션은 무시된다는 점에 유의하세요.

::: tip
가장 유용한 옵션은 대부분 `capabilities` 객체에 있습니다. WebdriverIO는 중첩 capabilities를 허용하지만, Vitest는 여러 브라우저를 실행할 때 다른 메커니즘에 의존하므로 해당 옵션들을 무시합니다.

또한 Vitest는 `capabilities.browserName`을 무시합니다. 대신 [`test.browser.instances.browser`](https://vitest.dev/config/browser/instances#browser)를 사용하세요.
:::
