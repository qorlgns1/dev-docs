---
title: "environmentOptions"
description: "이 옵션들은 현재 environment의 setup 메서드로 전달됩니다. 기본적으로 이를 테스트 환경으로 사용할 때 과 에 대해서만 옵션을 설정할 수 있습니다."
---

출처 URL: https://vitest.dev/config/environmentoptions

# environmentOptions

- **타입:** `Record<'jsdom' | 'happyDOM' | string, unknown>`
- **기본값:** `{}`

이 옵션들은 현재 [environment](https://vitest.dev/config/environment)의 setup 메서드로 전달됩니다. 기본적으로 이를 테스트 환경으로 사용할 때 `jsdom`과 `happyDOM`에 대해서만 옵션을 설정할 수 있습니다.

## 예제

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    environmentOptions: {
      jsdom: {
        url: "http://localhost:3000",
      },
      happyDOM: {
        width: 300,
        height: 400,
      },
    },
  },
});
```

::: warning
옵션은 각 환경에 범위가 한정됩니다. 예를 들어 jsdom 옵션은 `jsdom` 키 아래에, happy-dom 옵션은 `happyDOM` 키 아래에 두세요. 이렇게 하면 같은 프로젝트 내에서 여러 환경을 혼합해 사용할 수 있습니다.
:::
