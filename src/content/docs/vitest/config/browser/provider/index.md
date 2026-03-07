---
title: "browser.provider {#browser-provider}"
description: "provider 팩토리의 반환값입니다. 에서 팩토리를 가져오거나, 직접 provider를 만들 수 있습니다:"
---

출처 URL: https://vitest.dev/config/browser/provider

# browser.provider {#browser-provider}

- **타입:** `BrowserProviderOption`

provider 팩토리의 반환값입니다. `@vitest/browser-<provider-name>`에서 팩토리를 가져오거나, 직접 provider를 만들 수 있습니다:

```ts{8-10}
import { playwright } from '@vitest/browser-playwright'
import { webdriverio } from '@vitest/browser-webdriverio'
import { preview } from '@vitest/browser-preview'

export default defineConfig({
  test: {
    browser: {
      provider: playwright(),
      provider: webdriverio(),
      provider: preview(),
    },
  },
})
```

provider가 브라우저를 초기화하는 방식을 설정하려면, 팩토리 함수에 옵션을 전달할 수 있습니다:

```ts{7-13,20-26}
import { playwright } from '@vitest/browser-playwright'

export default defineConfig({
  test: {
    browser: {
      // shared provider options between all instances
      provider: playwright({
        launchOptions: {
          slowMo: 50,
          channel: 'chrome-beta',
        },
        actionTimeout: 5_000,
      }),
      instances: [
        { browser: 'chromium' },
        {
          browser: 'firefox',
          // overriding options only for a single instance
          // this will NOT merge options with the parent one
          provider: playwright({
            launchOptions: {
              firefoxUserPrefs: {
                'browser.startup.homepage': 'https://example.com',
              },
            },
          })
        }
      ],
    },
  },
})
```

## Custom Provider 고급

::: danger ADVANCED API
커스텀 provider API는 매우 실험적이며 패치 버전 사이에서도 변경될 수 있습니다. 브라우저에서 테스트를 실행하기만 하면 된다면, 대신 [`browser.instances`](#browser-instances) 옵션을 사용하세요.
:::

```ts
export interface BrowserProvider {
  name: string;
  mocker?: BrowserModuleMocker;
  readonly initScripts?: string[];
  /**
   * @experimental opt-in into file parallelisation
   */
  supportsParallelism: boolean;
  getCommandsContext: (sessionId: string) => Record<string, unknown>;
  openPage: (sessionId: string, url: string) => Promise<void>;
  getCDPSession?: (sessionId: string) => Promise<CDPSession>;
  close: () => Awaitable<void>;
}
```
