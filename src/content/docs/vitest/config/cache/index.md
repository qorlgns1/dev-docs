---
title: "cache"
description: "캐시 기능을 비활성화하려면 이 옵션을 사용하세요. 현재 Vitest는 더 오래 걸리는 테스트와 실패한 테스트를 먼저 실행하기 위해 테스트 결과 캐시를 저장합니다."
---

출처 URL: https://vitest.dev/config/cache

# cache

- **유형**: `false`
- **CLI**: `--no-cache`, `--cache=false`

캐시 기능을 비활성화하려면 이 옵션을 사용하세요. 현재 Vitest는 더 오래 걸리는 테스트와 실패한 테스트를 먼저 실행하기 위해 테스트 결과 캐시를 저장합니다.

캐시 디렉터리는 Vite의 [`cacheDir`](https://vitejs.dev/config/shared-options.html#cachedir) 옵션으로 제어됩니다:

```ts
import { defineConfig } from "vitest/config";

export default defineConfig({
  cacheDir: "custom-folder/.vitest",
});
```

`process.env.VITEST`를 사용하면 Vitest에만 디렉터리를 제한할 수 있습니다:

```ts
import { defineConfig } from "vitest/config";

export default defineConfig({
  cacheDir: process.env.VITEST ? "custom-folder/.vitest" : undefined,
});
```
