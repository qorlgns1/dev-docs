---
title: "Open Telemetry 지원 {#open-telemetry-support}"
description: "이 기능에 대한 피드백은 GitHub Discussion에 남겨주세요."
---

출처 URL: https://vitest.dev/guide/open-telemetry

# Open Telemetry 지원 {#open-telemetry-support}

::: tip FEEDBACK
이 기능에 대한 피드백은 [GitHub Discussion](https://github.com/vitest-dev/vitest/discussions/9222)에 남겨주세요.
:::

::: tip Example Project
[GitHub](https://github.com/vitest-dev/vitest/tree/main/examples/opentelemetry)
:::

테스트 내부에서 애플리케이션의 성능과 동작을 디버깅할 때 [OpenTelemetry](https://opentelemetry.io/) 트레이스는 유용한 도구가 될 수 있습니다.

활성화하면 Vitest 통합은 테스트의 worker 범위로 한정된 span을 생성합니다.

::: warning
Vitest가 [isolation](https://vitest.dev/config/isolate) 없이 실행되지 않는 한, OpenTelemetry 초기화는 모든 테스트의 시작 시간을 증가시킵니다. 이는 `vitest.worker.start` 내부의 `vitest.runtime.traces` span에서 확인할 수 있습니다.
:::

Vitest에서 OpenTelemetry 사용을 시작하려면 [`experimental.openTelemetry.sdkPath`](https://vitest.dev/config/experimental#experimental-opentelemetry)를 통해 SDK 모듈 경로를 지정하고 `experimental.openTelemetry.enabled`를 `true`로 설정하세요. Vitest는 전체 프로세스와 각 개별 테스트 worker를 자동으로 계측합니다.

프로세스가 종료되기 전에 Vitest가 네트워크 요청을 flush할 수 있도록, SDK를 default export로 내보내야 합니다. Vitest는 `start`를 자동으로 호출하지 않는다는 점에 유의하세요.

## 빠른 시작

애플리케이션 트레이스를 미리 보기 전에 필요한 패키지를 설치하고 설정에서 계측 파일 경로를 지정하세요.

```shell
npm i @opentelemetry/sdk-node @opentelemetry/auto-instrumentations-node @opentelemetry/exporter-trace-otlp-proto
```

::: code-group

```js{12} [otel.js]
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node'
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-proto'
import { NodeSDK } from '@opentelemetry/sdk-node'

const sdk = new NodeSDK({
  serviceName: 'vitest',
  traceExporter: new OTLPTraceExporter(),
  instrumentations: [getNodeAutoInstrumentations()],
})

sdk.start()
export default sdk
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

::: danger FAKE TIMERS
fake timer를 사용하는 경우 테스트가 끝나기 전에 반드시 리셋해야 합니다. 그렇지 않으면 트레이스가 올바르게 추적되지 않을 수 있습니다.
:::

Vitest는 `sdkPath` 모듈을 처리하지 않으므로, SDK를 Node.js 환경에서 import할 수 있어야 합니다. 이 파일에는 `.js` 확장자를 사용하는 것이 가장 좋습니다. 다른 확장자를 사용하면 테스트가 느려질 수 있고 추가 Node.js 인자를 제공해야 할 수 있습니다.

TypeScript 파일을 제공하려면 Node.js 문서의 [TypeScript](https://nodejs.org/api/typescript.html#type-stripping) 페이지를 먼저 숙지하세요.

## 커스텀 트레이스

코드 내 특정 작업을 추적하기 위해 OpenTelemetry API를 직접 사용할 수 있습니다. 커스텀 트레이스는 Vitest OpenTelemetry 컨텍스트를 자동으로 상속합니다.

```ts
import { trace } from "@opentelemetry/api";
import { test } from "vitest";
import { db } from "./src/db";

const tracer = trace.getTracer("vitest");

test("db connects properly", async () => {
  // this is shown inside `vitest.test.runner.test.callback` span
  await tracer.startActiveSpan("db.connect", () => db.connect());
});
```

## 브라우저 모드

[browser mode](https://vitest.dev/guide/browser/)에서 테스트를 실행할 때 Vitest는 Node.js와 브라우저 사이에서 트레이스 컨텍스트를 전파합니다. Node.js 측 트레이스(테스트 오케스트레이션, 브라우저 드라이버 통신)는 추가 설정 없이 사용할 수 있습니다.

브라우저 런타임의 트레이스를 수집하려면 `browserSdkPath`를 통해 브라우저 호환 SDK를 제공하세요.

```shell
npm i @opentelemetry/sdk-trace-web @opentelemetry/exporter-trace-otlp-proto
```

::: code-group

```js [otel-browser.js]
import {
  BatchSpanProcessor,
  WebTracerProvider,
} from "@opentelemetry/sdk-trace-web";
import { OTLPTraceExporter } from "@opentelemetry/exporter-trace-otlp-proto";

const provider = new WebTracerProvider({
  spanProcessors: [new BatchSpanProcessor(new OTLPTraceExporter())],
});

provider.register();
export default provider;
```

```js [vitest.config.js]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    browser: {
      enabled: true,
      provider: "playwright",
      instances: [{ browser: "chromium" }],
    },
    experimental: {
      openTelemetry: {
        enabled: true,
        sdkPath: "./otel.js",
        browserSdkPath: "./otel-browser.js",
      },
    },
  },
});
```

:::

::: warning ASYNC CONTEXT
Node.js와 달리 브라우저에는 자동 비동기 컨텍스트 전파가 없습니다. Vitest는 테스트 실행에 대해 이를 내부적으로 처리하지만, 깊게 중첩된 비동기 코드의 커스텀 span은 컨텍스트가 자동으로 전파되지 않을 수 있습니다.
:::

## 트레이스 보기

트레이스를 생성하려면 평소처럼 Vitest를 실행하세요. watch mode 또는 run mode 중 어느 쪽으로도 실행할 수 있습니다. 모든 작업이 끝나면 트레이스가 올바르게 처리되도록 Vitest가 `sdk.shutdown()`을 수동으로 호출합니다.

OpenTelemetry API를 지원하는 오픈소스 또는 상용 제품으로 트레이스를 볼 수 있습니다. OpenTelemetry를 처음 사용한다면 설정이 매우 쉬운 [Jaeger](https://www.jaegertracing.io/docs/2.11/getting-started/#all-in-one)부터 시작하는 것을 권장합니다.

## `@opentelemetry/api`

Vitest는 `@opentelemetry/api`를 선택적 peer dependency로 선언하며, 내부적으로 span 생성에 사용합니다. 트레이스 수집이 활성화되지 않은 경우 Vitest는 이 의존성을 사용하려고 시도하지 않습니다.

Vitest를 OpenTelemetry와 함께 사용하도록 구성할 때는 일반적으로 `@opentelemetry/sdk-node`를 설치하며, 이 패키지는 `@opentelemetry/api`를 전이 의존성으로 포함하므로 Vitest의 peer dependency 요구 사항을 충족합니다. `@opentelemetry/api`를 찾을 수 없다는 오류가 발생하면, 보통 트레이스 수집이 활성화되지 않았음을 의미합니다. 올바르게 구성한 뒤에도 오류가 계속되면 `@opentelemetry/api`를 명시적으로 설치해야 할 수 있습니다.

## 프로세스 간 컨텍스트 전파

Vitest는 [OpenTelemetry specification](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/context/env-carriers.md)에 정의된 `TRACEPARENT` 및 `TRACESTATE` 환경 변수를 통해 부모 프로세스에서의 자동 컨텍스트 전파를 지원합니다. 이는 더 큰 분산 트레이싱 시스템의 일부로 Vitest를 실행할 때(예: OpenTelemetry 계측이 적용된 CI/CD 파이프라인) 특히 유용합니다.
