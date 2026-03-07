---
title: "allowOnly"
description: "기본적으로 Vitest는 Continuous Integration (CI) 환경에서  플래그가 지정된 테스트를 허용하지 않습니다. 반대로 로컬 개발 환경에서는 이러한 테스트의 실행을 허용합니다."
---

출처 URL: https://vitest.dev/config/allowonly

# allowOnly

- **타입**: `boolean`
- **기본값**: `!process.env.CI`
- **CLI:** `--allowOnly`, `--allowOnly=false`

기본적으로 Vitest는 Continuous Integration (CI) 환경에서 [`only`](https://vitest.dev/api/#test-only) 플래그가 지정된 테스트를 허용하지 않습니다. 반대로 로컬 개발 환경에서는 이러한 테스트의 실행을 허용합니다.

::: info
Vitest는 환경을 감지하기 위해 [`std-env`](https://www.npmjs.com/package/std-env) 패키지를 사용합니다.
:::

`allowOnly` 옵션을 `true` 또는 `false`로 명시적으로 설정하여 이 동작을 사용자 지정할 수 있습니다.

::: code-group

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    allowOnly: true,
  },
});
```

```bash [CLI]
vitest --allowOnly
```

:::

활성화하면, CI 환경을 포함해 [`only`](https://vitest.dev/api/#test-only)로 표시된 테스트가 감지되더라도 Vitest는 테스트 스위트를 실패 처리하지 않습니다.

비활성화하면, 로컬 개발 환경을 포함해 [`only`](https://vitest.dev/api/#test-only)로 표시된 테스트가 감지될 경우 Vitest는 테스트 스위트를 실패 처리합니다.
