---
title: '기존 OpenTelemetry 설정 사용 | Next.js용 Sentry'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/custom-setup'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/custom-setup

# 기존 OpenTelemetry 설정 사용 | Next.js용 Sentry

이미 완전히 커스텀된 OpenTelemetry 설정이 있거나, Sentry SDK 옆에 커스텀 OpenTelemetry 설정을 추가하려는 경우 이 가이드를 사용하세요.

`skipOpenTelemetrySetup: true`를 설정하면 Sentry SDK의 자동 OpenTelemetry 구성이 비활성화되며, 수동 설정이 **필수**가 됩니다. 예를 들어, 오류가 해당 scope와 올바르게 연결되도록 하려면 OpenTelemetry 설정에 `SentryContextManager`를 추가해야 합니다. 필요한 수동 설정에 대한 자세한 내용은 이 페이지 아래에서 확인할 수 있습니다.

Sentry 설정에 개별 OpenTelemetry instrumentation만 추가하려는 경우에는 대신 [추가 OpenTelemetry Instrumentation 추가하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/using-opentelemetry-apis.md#adding-additional-opentelemetry-instrumentation)를 읽어야 합니다.

기존 OpenTelemetry 설정을 사용하려면 `init({})` 구성에서 `skipOpenTelemetrySetup: true`를 설정한 다음, Sentry에 필요한 모든 구성 요소를 직접 설정하세요. 마지막으로 `@sentry/opentelemetry`를 설치하고 다음을 추가합니다:

```javascript
const Sentry = require("@sentry/node");
const {
  SentrySpanProcessor,
  SentryPropagator,
  SentrySampler,
} = require("@sentry/opentelemetry");

const { NodeTracerProvider } = require("@opentelemetry/sdk-trace-node");

const sentryClient = Sentry.init({
  dsn: "___DSN___",
  skipOpenTelemetrySetup: true,

  // The SentrySampler will use this to determine which traces to sample
  tracesSampleRate: 1.0,
});

// Note: This could be BasicTracerProvider or any other provider depending on
// how you are using the OpenTelemetry SDK
const provider = new NodeTracerProvider({
  // Ensure the correct subset of traces is sent to Sentry
  // This also ensures trace propagation works as expected
  sampler: sentryClient ? new SentrySampler(sentryClient) : undefined,
  spanProcessors: [
    // Ensure spans are correctly linked & sent to Sentry
    new SentrySpanProcessor(),
    // Add additional processors here
  ],
});

provider.register({
  // Ensure trace propagation works
  // This relies on the SentrySampler for correct propagation
  propagator: new SentryPropagator(),
  // Ensure context & request isolation are correctly managed
  contextManager: new Sentry.SentryContextManager(),
});

// Validate that the setup is correct
Sentry.validateOpenTelemetrySetup();
```

모든 [필수 OpenTelemetry Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/custom-setup.md#required-instrumentation)이 올바르게 설정되어 있는지 확인하세요. 그렇지 않으면 Sentry SDK가 예상대로 작동하지 않을 수 있습니다.

## [오류 모니터링 전용으로 Sentry 사용하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/custom-setup.md#using-sentry-for-error-monitoring-only)

커스텀 OpenTelemetry 설정이 있고 오류 모니터링 용도로만 Sentry를 사용하려는 경우 `SentrySpanProcessor` 추가를 생략할 수 있습니다. Sentry로 tracing 데이터를 전송하지 않더라도 설정에 `SentryContextManager`, `SentryPropagator`, `SentrySampler`는 여전히 추가해야 합니다. 왜 이것이 필요한지는 아래 내용을 확인하세요.

Sentry SDK가 예상대로 동작하고 OpenTelemetry와 동기화되려면 몇 가지 구성 요소가 필요합니다.

**Sentry가 올바르게 동작하는 데 필요한 구성 요소:**

* **SentryContextManager**: OpenTelemetry context와 Sentry가 동기화되도록 보장합니다. 예를 들어 동시에 처리되는 요청 간 데이터가 올바르게 분리되도록 합니다.
* **SentrySampler**: Sentry의 `tracesSampleRate`가 준수되도록 보장합니다. Sentry를 tracing에 사용하지 않더라도 trace propagation이 예상대로 동작하려면 여전히 필요합니다. 커스텀 sampler를 사용하려면 [커스텀 Sampler 사용하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/custom-setup.md#using-a-custom-sampler)를 읽어보세요.
* **SentryPropagator**: trace propagation이 올바르게 동작하도록 보장합니다.
* [필수 Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/custom-setup.md#required-instrumentation): trace propagation이 올바르게 동작하도록 보장합니다.

**Sentry를 tracing에도 함께 사용하려면 추가로 필요한 구성 요소:**

* **SentrySpanProcessor**: span이 Sentry로 올바르게 전송되도록 보장합니다.

trace propagation은 Sentry가 서비스를 자동으로 서로 연결하는 데 필요합니다. (예: 프런트엔드와 백엔드, 또는 서로 다른 백엔드 서비스 연결) 이를 통해 서비스 간 관련 오류를 확인할 수 있습니다.<!-- -->

[Trace Propagation에 대해 더 알아보기](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/trace-propagation.md)

다음 코드 스니펫은 오류 모니터링 전용으로 Sentry를 설정하는 방법을 보여줍니다:

```javascript
import * as Sentry from "@sentry/node";
import { SentryPropagator, SentrySampler } from "@sentry/opentelemetry";

import { NodeTracerProvider } from "@opentelemetry/sdk-trace-node";
import { BatchSpanProcessor } from "@opentelemetry/sdk-trace-base";
import { OTLPTraceExporter } from "@opentelemetry/exporter-otlp-http";
import { registerInstrumentations } from "@opentelemetry/instrumentation";

const sentryClient = Sentry.init({
  dsn: "___DSN___",
  // Skipping the OpenTelemetry setup automatically disables emitting spans in the httpIntegration with `spans: false`
  skipOpenTelemetrySetup: true,

  // Important: We do not define a tracesSampleRate here at all!
  // This leads to tracing being disabled
});

// Create and configure e.g. NodeTracerProvider
const provider = new NodeTracerProvider({
  // This ensures trace propagation works as expected
  sampler: sentryClient ? new SentrySampler(sentryClient) : undefined,
});

provider.addSpanProcessor(
  new BatchSpanProcessor(
    new OTLPTraceExporter({
      url: "http://OTLP-ENDPOINT.com/api",
    }),
  ),
);

// Initialize the provider
provider.register({
  propagator: new SentryPropagator(),
  contextManager: new Sentry.SentryContextManager(),
});

registerInstrumentations({
  instrumentations: [
    // Add OTEL instrumentation here
  ],
});
```

## [필수 Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/custom-setup.md#required-instrumentation)

기본적으로 Sentry는 OpenTelemetry instrumentation을 등록하여, 수신/송신 HTTP 요청, DB 쿼리 등을 가로지르는 trace의 span을 자동으로 캡처합니다.

tracing이 활성화되지 않은 경우(SDK 구성에 `tracesSampleRate`가 정의되지 않음), 최소한의 OpenTelemetry instrumentation만 등록됩니다. 여기에는 다음이 포함됩니다:

* 요청 분리와 trace propagation을 처리하는 Sentry 전용 HTTP instrumentation. 등록한 경우 [@opentelemetry/instrumentation-http](https://www.npmjs.com/package/@opentelemetry/instrumentation-http)와 병렬로 동작할 수 있습니다.
* [nativeNodeFetchIntegration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodefetch.md)은 trace propagation에 필요한 [opentelemetry-instrumentation-fetch-node](https://www.npmjs.com/package/opentelemetry-instrumentation-fetch-node)를 등록합니다.

tracing이 활성화되지 않으면 성능 instrumentation은 등록되지 않지만 번들에는 계속 포함됩니다. 번들 크기나 사용 의존성을 줄이고 싶다면, 다음도 가능합니다<!-- -->

[성능 Integration 없이 Sentry 설정하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/tree-shaking.md#setting-up-sentry-without-performance-integrations)

이는 trace propagation이 올바르게 동작하도록 보장하는 데 필요합니다.

직접 http/node-fetch instrumentation을 추가하려면 다음 단계를 따라야 합니다:

- [커스텀 HTTP Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/custom-setup.md#custom-http-instrumentation)

지원 버전: `v8.35.0`

OpenTelemetry 설정에서 자체 `@opentelemetry/instrumentation-http` 인스턴스를 추가할 수 있습니다. 하지만 이 경우 Sentry의 `httpIntegration`에서 span 생성을 비활성화해야 합니다:

```javascript
const sentryClient = Sentry.init({
  dsn: "___DSN___",
  skipOpenTelemetrySetup: true,
  integrations: [Sentry.httpIntegration({ spans: false })],
});
```

예를 들어 오류를 캡처할 때 Sentry SDK가 요청을 올바르게 분리할 수 있도록, `httpIntegration`은 여전히 이 방식으로 등록되어 있어야 합니다.

- [커스텀 Node Fetch Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/custom-setup.md#custom-node-fetch-instrumentation)

tracing이 비활성화되어 있으면 Node Fetch instrumentation은 어떤 span도 내보내지 않습니다. 이 시나리오에서는 sentry 전용 trace propagation 헤더만 주입합니다. 여기에 원하는 대로 span을 내보내는 자체 Node Fetch instrumentation을 추가해도 됩니다.

## [커스텀 Sampler 사용하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/custom-setup.md#using-a-custom-sampler)

자체 sampler를 사용할 수는 있지만, `SentrySampler` 사용을 권장합니다. 이렇게 하면 `tracesSampleRate`를 기준으로 올바른 trace 하위 집합이 Sentry로 전송됩니다. 또한 trace propagation 같은 다른 Sentry 기능도 예상대로 동작하도록 보장합니다. 자체 sampler를 반드시 사용해야 한다면, 아래 예시처럼 `SamplingResult`를 `wrapSamplingDecision` 메서드로 감싸야 합니다:

```javascript
import * as Sentry from "@sentry/node";
import { wrapSamplingDecision } from "@sentry/opentelemetry";
import { NodeTracerProvider } from "@opentelemetry/sdk-trace-node";

// implements Sampler from "@opentelemetry/sdk-trace-node"
class CustomSampler {
  shouldSample(
    context,
    _traceId,
    _spanName,
    _spanKind,
    attributes,
    _links,
  ) {
    const decision = yourDecisionLogic();

    // wrap the result
    return wrapSamplingDecision({
      decision,
      context,
      spanAttributes: attributes,
    });
  }

  toString() {
    return CustomSampler.name;
  }
}

const sentryClient = Sentry.init({
  dsn: "___DSN___",
  skipOpenTelemetrySetup: true,

  // By defining any sample rate,
  // tracing integrations will be added by default
  // omit this if you do not want any performance integrations to be added
  tracesSampleRate: 0,
});

const provider = new NodeTracerProvider({
  sampler: new CustomSampler(),
});

// ...rest of your setup

// Validate that the setup is correct
Sentry.validateOpenTelemetrySetup();
```

## [ESM 로더](https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/custom-setup.md#esm-loaders)

애플리케이션이 ESM(`import`/`export` 문법)에서 실행되는 경우, OpenTelemetry는 *ESM loader hooks* 설정을 요구합니다.

Sentry SDK는 기본적으로 ESM loader hooks를 자동 등록합니다. 하지만 자체 OpenTelemetry 설정이 있다면, Sentry SDK가 이 hooks를 등록하지 않도록 구성하고 대신 직접 등록하는 것을 권장합니다. `registerEsmLoaderHooks`를 `false`로 설정하고 [ESM loader hooks 설정](https://github.com/open-telemetry/opentelemetry-js/blob/main/doc/esm-support.md#instrumentation-hook-required-for-esm)을 수행하면 됩니다:

```javascript
Sentry.init({
  dsn: "___DSN___",
  skipOpenTelemetrySetup: true,
  registerEsmLoaderHooks: false,
});
```

##### loader hooks를 직접 등록하는 것이 권장되는 이유는 무엇인가요?

완전히 커스텀된 OpenTelemetry 설정이 있다면 자체 ESM loader hooks를 등록하는 것이 권장됩니다. 무엇보다 아키텍처적으로 가장 자연스럽기 때문입니다. OpenTelemetry를 독립적으로 설정한 뒤, 그 설정을 건드리지 않고 애플리케이션에 Sentry를 추가하려는 경우가 많기 때문입니다.

또한 hooks를 직접 등록하면 다음과 같은 몇 가지 함정을 쉽게 피할 수 있습니다:

* loader hooks를 여러 번 등록하면 중복 span이 생성될 수 있습니다. [자세히 보기](https://github.com/getsentry/sentry-javascript/issues/14065#issuecomment-2435546961)
* ESM에서 OpenTelemetry instrumentation은 loader hooks 등록 시점 대비 *언제* 추가되는지에 매우 민감합니다. 이에 대한 제어권은 Sentry SDK가 아니라 OpenTelemetry 설정의 소유자에게 있어야 합니다.

