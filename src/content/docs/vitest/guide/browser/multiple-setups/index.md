---
title: "여러 설정"
description: "필드를 사용해 서로 다른 브라우저의 옵션을 지정할 수 있습니다. 예를 들어, 동일한 테스트를 여러 브라우저에서 실행하려면 최소 구성은 다음과 같습니다:"
---

출처 URL: https://vitest.dev/guide/browser/multiple-setups

# 여러 설정

[`browser.instances`](https://vitest.dev/config/browser/instances) 옵션을 사용하면 서로 다른 여러 브라우저 설정을 지정할 수 있습니다.

[test projects](https://vitest.dev/guide/projects)보다 `browser.instances`를 사용하는 가장 큰 장점은 캐싱 향상입니다. 모든 프로젝트가 동일한 Vite 서버를 사용하므로 파일 변환과 [dependency pre-bundling](https://vite.dev/guide/dep-pre-bundling.html)은 한 번만 수행하면 됩니다.

## 여러 브라우저

`browser.instances` 필드를 사용해 서로 다른 브라우저의 옵션을 지정할 수 있습니다. 예를 들어, 동일한 테스트를 여러 브라우저에서 실행하려면 최소 구성은 다음과 같습니다:

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";
import { playwright } from "@vitest/browser-playwright";

export default defineConfig({
  test: {
    browser: {
      enabled: true,
      provider: playwright(),
      headless: true,
      instances: [
        { browser: "chromium" },
        { browser: "firefox" },
        { browser: "webkit" },
      ],
    },
  },
});
```

## 서로 다른 설정

브라우저와는 독립적으로 다른 config 옵션도 지정할 수 있습니다(물론 인스턴스에 `browser` 필드를 포함할 수도 있습니다):

::: code-group

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";
import { playwright } from "@vitest/browser-playwright";

export default defineConfig({
  test: {
    browser: {
      enabled: true,
      provider: playwright(),
      headless: true,
      instances: [
        {
          browser: "chromium",
          name: "chromium-1",
          setupFiles: ["./ratio-setup.ts"],
          provide: {
            ratio: 1,
          },
        },
        {
          browser: "chromium",
          name: "chromium-2",
          provide: {
            ratio: 2,
          },
        },
      ],
    },
  },
});
```

```ts [example.test.ts]
import { expect, inject, test } from "vitest";
import { globalSetupModifier } from "./example.js";

test("ratio works", () => {
  expect(inject("ratio") * globalSetupModifier).toBe(14);
});
```

:::

이 예시에서 Vitest는 모든 테스트를 `chromium` 브라우저에서 실행하지만, 첫 번째 구성에서만 `'./ratio-setup.ts'` 파일을 실행하고 [`provide` field](https://vitest.dev/config/#provide)에 따라 다른 `ratio` 값을 주입합니다.

::: warning
같은 브라우저 이름을 사용하는 경우 사용자 정의 `name` 값을 반드시 정의해야 합니다. 그렇지 않으면 Vitest가 `browser`를 프로젝트 이름으로 할당합니다.
:::

## 필터링

[`--project` flag](https://vitest.dev/guide/cli#project)로 실행할 프로젝트를 필터링할 수 있습니다. 수동으로 지정하지 않으면 Vitest가 브라우저 이름을 프로젝트 이름으로 자동 할당합니다. 루트 config에 이미 이름이 있으면 Vitest가 이를 병합합니다: `custom` -> `custom (browser)`.

```shell
$ vitest --project=chromium
```

::: code-group

```ts{6,8} [default]
export default defineConfig({
  test: {
    browser: {
      instances: [
        // name: chromium
        { browser: 'chromium' },
        // name: custom
        { browser: 'firefox', name: 'custom' },
      ]
    }
  }
})
```

```ts{3,7,9} [custom]
export default defineConfig({
  test: {
    name: 'custom',
    browser: {
      instances: [
        // name: custom (chromium)
        { browser: 'chromium' },
        // name: manual
        { browser: 'firefox', name: 'manual' },
      ]
    }
  }
})
```

:::
