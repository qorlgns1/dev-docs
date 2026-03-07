---
title: "restoreMocks"
description: "각 테스트 전에 Vitest가 를 자동으로 호출할지 여부를 설정합니다."
---

출처 URL: https://vitest.dev/config/restoremocks

# restoreMocks

- **유형:** `boolean`
- **기본값:** `false`

각 테스트 전에 Vitest가 [`vi.restoreAllMocks()`](https://vitest.dev/api/vi#vi-restoreallmocks)를 자동으로 호출할지 여부를 설정합니다.

이 옵션은 [`vi.spyOn`](https://vitest.dev/api/vi#vi-spyon)으로 수동 생성한 spy의 모든 원래 구현을 복원합니다.

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    restoreMocks: true,
  },
});
```
