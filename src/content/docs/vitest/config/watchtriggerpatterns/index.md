---
title: "watchTriggerPatterns 3.2.0"
description: "Vitest는 정적 및 동적  문으로 구성된 모듈 그래프를 기반으로 테스트를 다시 실행합니다. 하지만 파일 시스템에서 읽거나 프록시에서 가져오는 경우, Vitest는 해당 의존성을 감지할 수 없습니다."
---

출처 URL: https://vitest.dev/config/watchtriggerpatterns

# watchTriggerPatterns 3.2.0

- **타입:** `WatcherTriggerPattern[]`

Vitest는 정적 및 동적 `import` 문으로 구성된 모듈 그래프를 기반으로 테스트를 다시 실행합니다. 하지만 파일 시스템에서 읽거나 프록시에서 가져오는 경우, Vitest는 해당 의존성을 감지할 수 없습니다.

이러한 테스트를 올바르게 다시 실행하려면, 정규식 패턴과 실행할 테스트 파일 목록을 반환하는 함수를 정의할 수 있습니다.

```ts
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    watchTriggerPatterns: [
      {
        pattern: /^src\/(mailers|templates)\/(.*)\.(ts|html|txt)$/,
        testsToRun: (id, match) => {
          // relative to the root value
          return `./api/tests/mailers/${match[2]}.test.ts`;
        },
      },
    ],
  },
});
```

::: warning
반환되는 파일은 절대 경로이거나 루트를 기준으로 한 상대 경로여야 합니다. 이 옵션은 전역 옵션이며 [project](https://vitest.dev/guide/projects) 구성 내부에서는 사용할 수 없습니다.
:::
