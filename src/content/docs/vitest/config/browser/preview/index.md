---
title: "Preview 구성하기"
description: "provider의 주요 기능은 실제 브라우저 환경에서 테스트를 보여주는 것입니다. 하지만 여러 브라우저 인스턴스나 headless mode 같은 고급 브라우저 자동화 기능은 지원하지 않습니다. 더 복잡한 시나리오에서는 Playwright 또는 WebdriverIO 사용..."
---

출처 URL: https://vitest.dev/config/browser/preview

# Preview 구성하기

::: warning
`preview` provider의 주요 기능은 실제 브라우저 환경에서 테스트를 보여주는 것입니다. 하지만 여러 브라우저 인스턴스나 headless mode 같은 고급 브라우저 자동화 기능은 지원하지 않습니다. 더 복잡한 시나리오에서는 [Playwright](https://vitest.dev/config/browser/playwright) 또는 [WebdriverIO](https://vitest.dev/config/browser/webdriverio) 사용을 고려하세요.
:::

실제 브라우저에서 실행되는 테스트를 보려면 [`@vitest/browser-preview`](https://www.npmjs.com/package/@vitest/browser-preview) npm package를 설치하고, config의 `test.browser.provider` 속성에 해당 package의 `preview` export를 지정해야 합니다.

```ts [vitest.config.js]
import { preview } from "@vitest/browser-preview";
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    browser: {
      provider: preview(),
      instances: [{ browser: "chromium" }],
    },
  },
});
```

이렇게 하면 기본 브라우저를 사용해 테스트를 실행하는 새 브라우저 창이 열립니다. `instances` 배열의 `browser` 속성을 설정해 사용할 브라우저를 구성할 수 있습니다. Vitest가 해당 브라우저를 자동으로 열려고 시도하지만, 일부 환경에서는 동작하지 않을 수 있습니다. 그런 경우 제공된 URL을 원하는 브라우저에서 직접 열 수 있습니다.

## 다른 Providers와의 차이점

preview provider는 [Playwright](https://vitest.dev/config/browser/playwright) 또는 [WebdriverIO](https://vitest.dev/config/browser/webdriverio) 같은 다른 providers와 비교해 몇 가지 제한 사항이 있습니다.

- headless mode를 지원하지 않으므로 브라우저 창은 항상 표시됩니다.
- 동일한 브라우저의 여러 인스턴스를 지원하지 않으므로 각 인스턴스는 서로 다른 브라우저를 사용해야 합니다.
- 고급 브라우저 기능이나 옵션을 지원하지 않으므로 브라우저 이름만 지정할 수 있습니다.
- CDP (Chrome DevTools Protocol) 명령이나 기타 저수준 브라우저 상호작용을 지원하지 않습니다. Playwright나 WebdriverIO와 달리 [`userEvent`](https://vitest.dev/api/browser/interactivity) API는 [`@testing-library/user-event`](https://www.npmjs.com/package/@testing-library/user-event)에서 다시 export된 것일 뿐이며 브라우저와의 특별한 통합은 없습니다.
