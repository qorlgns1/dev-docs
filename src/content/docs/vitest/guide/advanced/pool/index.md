---
title: "커스텀 풀 고급 {#custom-pool}"
description: "이것은 고급, 실험적이며 매우 저수준 API입니다. 단순히 테스트를 실행하려는 경우라면, 아마 이것이 필요하지 않을 것입니다. 이 기능은 주로 라이브러리 작성자가 사용합니다."
---

출처 URL: https://vitest.dev/guide/advanced/pool

# 커스텀 풀 고급 {#custom-pool}

::: warning
이것은 고급, 실험적이며 매우 저수준 API입니다. 단순히 [테스트를 실행](https://vitest.dev/guide/)하려는 경우라면, 아마 이것이 필요하지 않을 것입니다. 이 기능은 주로 라이브러리 작성자가 사용합니다.
:::

Vitest는 풀(pool)에서 테스트를 실행합니다. 기본적으로 여러 풀 러너가 있습니다:

- `threads`: `node:worker_threads`를 사용해 테스트를 실행합니다 (격리는 새 worker 컨텍스트로 제공됨)
- `forks`: `node:child_process`를 사용해 테스트를 실행합니다 (격리는 새 `child_process.fork` 프로세스로 제공됨)
- `vmThreads`: `node:worker_threads`를 사용해 테스트를 실행합니다 (단, 격리는 새 worker 컨텍스트 대신 `vm` 모듈로 제공됨)
- `browser`: 브라우저 프로바이더를 사용해 테스트를 실행합니다
- `typescript`: 테스트에 대해 타입 체크를 실행합니다

::: tip
커스텀 풀 러너 구현 예시는 [`vitest-pool-example`](https://www.npmjs.com/package/vitest-pool-example)을 참고하세요.
:::

## 사용법

`PoolRunnerInitializer`를 반환하는 함수를 통해 자체 풀 러너를 제공할 수 있습니다.

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";
import customPool from "./my-custom-pool.ts";

export default defineConfig({
  test: {
    // will run every file with a custom pool by default
    pool: customPool({
      customProperty: true,
    }),
  },
});
```

서로 다른 풀에서 테스트를 실행해야 한다면 [`projects`](https://vitest.dev/guide/projects) 기능을 사용하세요:

```ts [vitest.config.ts]
import customPool from "./my-custom-pool.ts";

export default defineConfig({
  test: {
    projects: [
      {
        extends: true,
        test: {
          pool: "threads",
        },
      },
      {
        extends: true,
        test: {
          pool: customPool({
            customProperty: true,
          }),
        },
      },
    ],
  },
});
```

## API

`pool` 옵션은 커스텀 풀 러너에 사용할 수 있는 `PoolRunnerInitializer`를 받습니다. `name` 속성은 커스텀 풀 러너의 이름을 나타내야 하며, 워커의 `name` 속성과 동일해야 합니다.

```ts [my-custom-pool.ts]
import type { PoolRunnerInitializer } from "vitest/node";

export function customPool(
  customOptions: CustomOptions,
): PoolRunnerInitializer {
  return {
    name: "custom-pool",
    createPoolWorker: (options) => new CustomPoolWorker(options, customOptions),
  };
}
```

`CustomPoolWorker`에서는 필요한 모든 메서드를 정의해야 합니다:

```ts [my-custom-pool.ts]
import type { PoolOptions, PoolWorker, WorkerRequest } from "vitest/node";

class CustomPoolWorker implements PoolWorker {
  name = "custom-pool";
  private customOptions: CustomOptions;

  constructor(options: PoolOptions, customOptions: CustomOptions) {
    this.customOptions = customOptions;
  }

  send(message: WorkerRequest): void {
    // Provide way to send your worker a message
  }

  on(event: string, callback: (arg: any) => void): void {
    // Provide way to listen to your workers events, e.g. message, error, exit
  }

  off(event: string, callback: (arg: any) => void): void {
    // Provide way to unsubscribe `on` listeners
  }

  async start() {
    // do something when the worker is started
  }

  async stop() {
    // cleanup the state
  }

  deserialize(data) {
    return data;
  }
}
```

`CustomPoolRunner`는 커스텀 테스트 러너 워커의 생명주기와 통신 채널 동작 방식을 제어합니다. 예를 들어, `CustomPoolRunner`는 `node:worker_threads`의 `Worker`를 실행하고, `Worker.postMessage`와 `parentPort`를 통해 통신을 제공할 수 있습니다.

워커 파일에서는 `vitest/worker`에서 헬퍼 유틸리티를 import할 수 있습니다:

```ts [my-worker.ts]
import { init, runBaseTests, setupEnvironment } from "vitest/worker";

init({
  post: (response) => {
    // Provide way to send this message to CustomPoolRunner's onWorker as message event
  },
  on: (callback) => {
    // Provide a way to listen CustomPoolRunner's "postMessage" calls
  },
  off: (callback) => {
    // Optional, provide a way to remove listeners added by "on" calls
  },
  teardown: () => {
    // Optional, provide a way to teardown worker, e.g. unsubscribe all the `on` listeners
  },
  serialize: (value) => {
    // Optional, provide custom serializer for `post` calls
  },
  deserialize: (value) => {
    // Optional, provide custom deserializer for `on` callbacks
  },
  runTests: (state, traces) => runBaseTests("run", state, traces),
  collectTests: (state, traces) => runBaseTests("collect", state, traces),
  setup: setupEnvironment,
});
```
