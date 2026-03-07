---
title: "experimental"
description: "이 기능에 대한 피드백을 GitHub Discussion에 남겨 주세요."
---

출처 URL: https://vitest.dev/config/experimental

# experimental

## experimental.fsModuleCache 4.0.11 {#experimental-fsmodulecache}

::: tip FEEDBACK
이 기능에 대한 피드백을 [GitHub Discussion](https://github.com/vitest-dev/vitest/discussions/9221)에 남겨 주세요.
:::

- **Type:** `boolean`
- **Default:** `false`

이 옵션을 활성화하면 Vitest가 모듈 캐시를 파일 시스템에 유지할 수 있어, 재실행 사이의 테스트 실행 속도가 더 빨라집니다.

기존 캐시는 [`vitest --clearCache`](https://vitest.dev/guide/cli#clearcache)를 실행해 삭제할 수 있습니다.

::: warning BROWSER SUPPORT
현재 이 옵션은 [the browser](https://vitest.dev/guide/browser/)에 영향을 주지 않습니다.
:::

모듈이 캐시되고 있는지 확인하려면 `DEBUG=vitest:cache:fs` 환경 변수를 설정해 vitest를 실행해 디버그할 수 있습니다:

```shell
DEBUG=vitest:cache:fs vitest --experimental.fsModuleCache
```

### 알려진 문제

Vitest는 파일 내용, 파일 id, vite의 환경 설정, 커버리지 상태를 기반으로 영구 파일 해시를 생성합니다. Vitest는 설정에 대해 가능한 많은 정보를 사용하려고 하지만, 아직 완전하지는 않습니다. 현재로서는 이를 위한 표준 인터페이스가 없기 때문에 플러그인 옵션을 추적할 수 없습니다.

플러그인이 파일 내용이나 공개 설정 외부의 요소(예: 다른 파일이나 폴더 읽기)에 의존한다면 캐시가 오래된 상태가 될 수 있습니다. 이를 우회하려면 [cache key generator](https://vitest.dev/api/advanced/plugin#definecachekeygenerator)를 정의해 동적 옵션을 지정하거나, 해당 모듈의 캐싱을 비활성화할 수 있습니다:

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  plugins: [
    {
      name: "vitest-cache",
      configureVitest({ experimental_defineCacheKeyGenerator }) {
        experimental_defineCacheKeyGenerator(({ id, sourceCode }) => {
          // never cache this id
          if (id.includes("do-not-cache")) {
            return false;
          }

          // cache this file based on the value of a dynamic variable
          if (sourceCode.includes("myDynamicVar")) {
            return process.env.DYNAMIC_VAR_VALUE;
          }
        });
      },
    },
  ],
  test: {
    experimental: {
      fsModuleCache: true,
    },
  },
});
```

플러그인 작성자라면, 변환 결과에 영향을 주는 서로 다른 옵션으로 플러그인이 등록될 수 있는 경우 플러그인에 [cache key generator](https://vitest.dev/api/advanced/plugin#definecachekeygenerator)를 정의하는 것을 고려하세요.

반대로 플러그인이 캐시 키에 영향을 주지 않아야 한다면 `api.vitest.experimental.ignoreFsModuleCache`를 `true`로 설정해 비활성화할 수 있습니다:

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  plugins: [
    {
      name: "vitest-cache",
      api: {
        vitest: {
          experimental: {
            ignoreFsModuleCache: true,
          },
        },
      },
    },
  ],
  test: {
    experimental: {
      fsModuleCache: true,
    },
  },
});
```

플러그인이 모듈 캐싱을 비활성화하더라도 cache key generator는 여전히 정의할 수 있습니다.

## experimental.fsModuleCachePath 4.0.11 {#experimental-fsmodulecachepath}

- **Type:** `string`
- **Default:** `'node_modules/.experimental-vitest-cache'`

파일 시스템 캐시가 위치한 디렉터리입니다.

기본적으로 Vitest는 워크스페이스 루트를 찾아 `node_modules` 폴더 내부에 캐시를 저장하려고 시도합니다. 루트는 패키지 매니저의 lockfile(예: `.package-lock.json`, `.yarn-state.yml`, `.pnpm/lock.yaml` 등)을 기준으로 결정됩니다.

현재 Vitest는 [test.cache.dir](https://vitest.dev/config/cache) 또는 [cacheDir](https://vite.dev/config/shared-options#cachedir) 옵션을 완전히 무시하고 별도의 폴더를 생성합니다.

## experimental.openTelemetry 4.0.11 {#experimental-opentelemetry}

::: tip FEEDBACK
이 기능에 대한 피드백을 [GitHub Discussion](https://github.com/vitest-dev/vitest/discussions/9222)에 남겨 주세요.
:::

- **Type:**

```ts
interface OpenTelemetryOptions {
  enabled: boolean;
  /**
   * A path to a file that exposes an OpenTelemetry SDK for Node.js.
   */
  sdkPath?: string;
  /**
   * A path to a file that exposes an OpenTelemetry SDK for the browser.
   */
  browserSdkPath?: string;
}
```

- **Default:** `{ enabled: false }`

이 옵션은 [OpenTelemetry](https://opentelemetry.io/) 지원을 제어합니다. `enabled`가 `true`로 설정되면 Vitest는 메인 스레드와 각 테스트 파일 실행 전에 SDK 파일을 import합니다.

::: danger PERFORMANCE CONCERNS
OpenTelemetry는 Vitest 성능에 상당한 영향을 줄 수 있으므로, 로컬 디버깅에서만 활성화하세요.
:::

Vitest와 함께 [custom service](https://vitest.dev/guide/open-telemetry)를 사용하면 어떤 테스트나 파일이 테스트 스위트를 느리게 만드는지 정확히 파악할 수 있습니다.

브라우저 모드에 대해서는 OpenTelemetry 가이드의 [Browser Mode](https://vitest.dev/guide/open-telemetry#browser-mode) 섹션을 참고하세요.

`sdkPath`는 프로젝트의 [`root`](https://vitest.dev/config/root)를 기준으로 해석되며, 시작된 SDK 인스턴스를 기본 export로 노출하는 모듈을 가리켜야 합니다. 예를 들어:

::: code-group

```js [otel.js]
import { getNodeAutoInstrumentations } from "@opentelemetry/auto-instrumentations-node";
import { OTLPTraceExporter } from "@opentelemetry/exporter-trace-otlp-proto";
import { NodeSDK } from "@opentelemetry/sdk-node";

const sdk = new NodeSDK({
  serviceName: "vitest",
  traceExporter: new OTLPTraceExporter(),
  instrumentations: [getNodeAutoInstrumentations()],
});

sdk.start();
export default sdk;
```

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    experimental: {
      openTelemetry: {
        enabled: true,
        sdkPath: "./otel.js",
      },
    },
  },
});
```

:::

::: warning
`sdkPath` 콘텐츠는 Vitest가 변환하지 않기 때문에 Node가 이를 처리할 수 있어야 한다는 점이 중요합니다. Vitest 내부에서 OpenTelemetry를 사용하는 방법은 [the guide](https://vitest.dev/guide/open-telemetry)를 참고하세요.
:::

## experimental.printImportBreakdown 4.0.15 {#experimental-printimportbreakdown}

::: tip FEEDBACK
이 기능에 대한 피드백을 [GitHub Discussion](https://github.com/vitest-dev/vitest/discussions/9224)에 남겨 주세요.
:::

- **Type:** `boolean`
- **Default:** `false`

테스트 실행이 끝난 후 import 소요 시간 분석을 표시합니다. 이 옵션은 [`default`](https://vitest.dev/guide/reporters#default), [`verbose`](https://vitest.dev/guide/reporters#verbose), [`tree`](https://vitest.dev/guide/reporters#tree) 리포터에서만 동작합니다.

- Self: 정적 import를 제외하고 모듈을 import하는 데 걸린 시간
- Total: 정적 import를 포함해 모듈을 import하는 데 걸린 시간. 현재 모듈의 `transform` 시간은 포함되지 않습니다.

파일 경로가 너무 길면 45자 제한에 맞을 때까지 Vitest가 앞부분을 잘라낸다는 점에 유의하세요.

::: info
[Vitest UI](https://vitest.dev/guide/ui#import-breakdown)는 로드에 500밀리초 이상 걸린 파일이 하나라도 있으면 import 분석을 자동으로 표시합니다. 이를 비활성화하려면 이 옵션을 수동으로 `false`로 설정할 수 있습니다.
:::
