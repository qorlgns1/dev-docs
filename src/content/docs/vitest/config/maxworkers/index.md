---
title: "maxWorkers"
description: "테스트 워커의 최대 동시성을 정의합니다. 숫자 또는 퍼센트 문자열을 받을 수 있습니다."
---

출처 URL: https://vitest.dev/config/maxworkers

# maxWorkers

- **유형:** `number | string`
- **기본값:**
  - [`watch`](https://vitest.dev/config/watch)가 비활성화된 경우, 사용 가능한 모든 병렬성을 사용합니다.
  - [`watch`](https://vitest.dev/config/watch)가 활성화된 경우, 사용 가능한 전체 병렬성의 절반을 사용합니다.

테스트 워커의 최대 동시성을 정의합니다. 숫자 또는 퍼센트 문자열을 받을 수 있습니다.

- 숫자: 지정한 수만큼 워커를 생성합니다.
- 퍼센트 문자열(예: "50%"): 머신에서 사용 가능한 병렬성에 해당 퍼센트를 적용해 워커 수를 계산합니다.

## 예시

### 숫자

::: code-group

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    maxWorkers: 4,
  },
});
```

```bash [CLI]
vitest --maxWorkers=4
```

:::

### 퍼센트

::: code-group

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    maxWorkers: "50%",
  },
});
```

```bash [CLI]
vitest --maxWorkers=50%
```

:::

Vitest는 사용 가능한 최대 병렬성 양을 파악하기 위해 [`os.availableParallelism`](https://nodejs.org/api/os.html#osavailableparallelism)을 사용합니다.
