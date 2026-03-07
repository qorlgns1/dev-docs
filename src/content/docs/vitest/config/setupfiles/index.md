---
title: "setupFiles"
description: "Vitest는 이 파일들에서 내보낸 모든 export를 무시합니다."
---

출처 URL: https://vitest.dev/config/setupfiles

# setupFiles

- **타입:** `string | string[]`

[`root`](https://vitest.dev/config/root)를 기준으로 해석되는 setup 파일 경로입니다. 이 파일들은 동일한 프로세스에서 각 *test file*보다 먼저 실행됩니다. 기본적으로 모든 테스트 파일은 병렬로 실행되지만, [`sequence.setupFiles`](https://vitest.dev/config/sequence#sequence-setupfiles) 옵션으로 이를 설정할 수 있습니다.

Vitest는 이 파일들에서 내보낸 모든 export를 무시합니다.

:::warning
setup 파일은 테스트와 동일한 프로세스에서 실행됩니다. 반면 [`globalSetup`](https://vitest.dev/config/globalsetup)은 테스트 워커가 생성되기 전에 메인 스레드에서 한 번만 실행됩니다.
:::

:::info
setup 파일을 수정하면 모든 테스트가 자동으로 다시 실행됩니다.
:::

백그라운드에서 무거운 프로세스가 실행 중이라면, 내부에서 `process.env.VITEST_POOL_ID`(정수형 문자열)를 사용해 워커를 구분하고 작업 부하를 분산할 수 있습니다.

:::warning
[isolation](https://vitest.dev/config/isolate)이 비활성화되어 있으면 import된 모듈은 캐시되지만, setup 파일 자체는 각 테스트 파일 전에 다시 실행됩니다. 즉, 각 테스트 파일 전에 동일한 전역 객체에 접근하게 됩니다. 필요한 것 이상으로 같은 작업을 반복하지 않도록 주의하세요.

예를 들어, 전역 변수에 의존할 수 있습니다:

```ts
import { config } from "@some-testing-lib";

if (!globalThis.setupInitialized) {
  config.plugins = [myCoolPlugin];
  computeHeavyThing();
  globalThis.setupInitialized = true;
}

// hooks reset before each test file
afterEach(() => {
  cleanup();
});

globalThis.resetBeforeEachTest = true;
```

:::
