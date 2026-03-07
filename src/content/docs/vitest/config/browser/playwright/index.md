---
title: "Playwright 구성하기"
description: "playwright를 사용해 테스트를 실행하려면  npm 패키지를 설치하고, 설정의  속성에 해당 패키지의  export를 지정해야 합니다:"
---

출처 URL: https://vitest.dev/config/browser/playwright

# Playwright 구성하기

playwright를 사용해 테스트를 실행하려면 [`@vitest/browser-playwright`](https://www.npmjs.com/package/@vitest/browser-playwright) npm 패키지를 설치하고, 설정의 `test.browser.provider` 속성에 해당 패키지의 `playwright` export를 지정해야 합니다:

```ts [vitest.config.js]
import { playwright } from "@vitest/browser-playwright";
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    browser: {
      provider: playwright(),
      instances: [{ browser: "chromium" }],
    },
  },
});
```

최상위 레벨에서 `playwright`를 호출하거나 인스턴스 내부에서 호출할 때 [`launchOptions`](https://playwright.dev/docs/api/class-browsertype#browser-type-launch), [`connectOptions`](https://playwright.dev/docs/api/class-browsertype#browser-type-connect), [`contextOptions`](https://playwright.dev/docs/api/class-browser#browser-new-context)을 구성할 수 있습니다:

```ts{7-14,21-26} [vitest.config.js]
import { playwright } from '@vitest/browser-playwright'
import { defineConfig } from 'vitest/config'

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

::: warning
Playwright 테스트 러너와 달리, Vitest는 같은 파일에 정의된 모든 테스트를 실행하기 위해 _단일_ 페이지를 엽니다. 즉, 격리는 개별 테스트마다가 아니라 단일 테스트 파일 단위로만 적용됩니다.
:::

## launchOptions

이 옵션들은 `playwright[browser].launch` 명령으로 직접 전달됩니다. 명령과 사용 가능한 인자에 대한 자세한 내용은 [Playwright 문서](https://playwright.dev/docs/api/class-browsertype#browser-type-launch)에서 확인할 수 있습니다.

::: warning
Vitest는 `launch.headless` 옵션을 무시합니다. 대신 [`test.browser.headless`](https://vitest.dev/config/browser/headless)를 사용하세요.

또한 [`--inspect`](https://vitest.dev/guide/cli#inspect)가 활성화되어 있으면 Vitest가 디버깅 플래그를 `launch.args`에 추가한다는 점에 유의하세요.
:::

## connectOptions

이 옵션들은 `playwright[browser].connect` 명령으로 직접 전달됩니다. 명령과 사용 가능한 인자에 대한 자세한 내용은 [Playwright 문서](https://playwright.dev/docs/api/class-browsertype#browser-type-connect)에서 확인할 수 있습니다.

::: warning
이 명령은 기존 Playwright 서버에 연결하므로, 모든 `launch` 옵션은 무시됩니다.
:::

## contextOptions

Vitest는 각 테스트 파일마다 [`browser.newContext()`](https://playwright.dev/docs/api/class-browsercontext)를 호출해 새 context를 생성합니다. [사용자 지정 인자](https://playwright.dev/docs/api/class-browser#browser-new-context)를 지정해 이 동작을 구성할 수 있습니다.

::: tip
Playwright 테스트 러너와 달리 context는 *각 테스트*가 아니라 *각 테스트 파일*마다 생성된다는 점에 유의하세요.
:::

::: warning
Vitest는 서버가 HTTPS로 제공되는 경우를 대비해 항상 `ignoreHTTPSErrors`를 `true`로 설정하고, [MSW](https://mswjs.io)를 통한 모듈 모킹을 지원하기 위해 `serviceWorkers`를 `'allow'`로 설정합니다.

또한 헤드리스 모드에서 테스트가 실행될 때 여기서 지정한 값은 손실되므로, 여기서 지정하는 대신 [`test.browser.viewport`](https://vitest.dev/config/browser/headless)를 사용하는 것이 권장됩니다.
:::

## `actionTimeout`

- **기본값:** 타임아웃 없음

이 값은 Playwright가 모든 접근성 검사를 통과하고 [해당 action](https://vitest.dev/api/browser/interactivity)이 실제로 완료될 때까지 기다리는 기본 타임아웃을 구성합니다.

액션별로 타임아웃을 구성할 수도 있습니다:

```ts
import { page, userEvent } from "vitest/browser";

await userEvent.click(page.getByRole("button"), {
  timeout: 1_000,
});
```
