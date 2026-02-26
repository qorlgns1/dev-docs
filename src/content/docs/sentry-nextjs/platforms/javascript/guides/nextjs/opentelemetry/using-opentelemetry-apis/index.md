---
title: 'OpenTelemetry API 사용 | Sentry for Next.js'
description: 'Sentry는 OpenTelemetry API를 기본적으로 지원합니다. OpenTelemetry API를 사용해 시작된 모든 span은 Sentry가 자동으로 수집하며, Sentry SDK로 시작된 모든 span은 OpenTelemetry로 자동 전파됩니다.'
---

소스 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/using-opentelemetry-apis

# OpenTelemetry API 사용 | Sentry for Next.js

Sentry는 OpenTelemetry API를 기본적으로 지원합니다. OpenTelemetry API를 사용해 시작된 모든 span은 Sentry가 자동으로 수집하며, Sentry SDK로 시작된 모든 span은 OpenTelemetry로 자동 전파됩니다.

## [추가 OpenTelemetry 계측 추가하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/using-opentelemetry-apis.md#adding-additional-opentelemetry-instrumentation)

Sentry SDK에는 기본적으로 일부 OpenTelemetry 계측이 포함되어 있지만, 애플리케이션에 추가 계측을 넣고 싶을 수 있습니다. 이는 아래 예시처럼 OpenTelemetry를 통해 계측을 등록하여 수행할 수 있습니다.

```javascript
import * as Sentry from "@sentry/node";
import { GenericPoolInstrumentation } from "@opentelemetry/instrumentation-generic-pool";

Sentry.init({
  dsn: "___DSN___",

  // The SentrySampler will use this to determine which traces to sample
  tracesSampleRate: 1.0,

  // Add additional OpenTelemetry instrumentation:
  openTelemetryInstrumentations: [new GenericPoolInstrumentation()],

});
```

`@opentelemetry/instrumentation`의 `registerInstrumentations()`를 통해 계측을 추가할 수 있습니다. 다만 ESM(`import`/`export` 문법)에서는 계측 대상 모듈을 가져오기 전에 이를 실행하도록 주의해야 합니다.

경험적으로 `registerInstrumentations()`는 [ESM Loaders](https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/custom-setup.md#esm-loaders)를 등록한 직후, 그리고 동일한 컨텍스트에서 호출해야 합니다.

## [OpenTelemetry Tracer 사용하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/using-opentelemetry-apis.md#using-an-opentelemetry-tracer)

span 생성에는 `Sentry.startSpan()` 및 관련 API 사용을 권장하지만, 네이티브 OpenTelemetry API를 사용해서도 span을 생성할 수 있습니다.

아래와 같이 `client.tracer`를 통해 Sentry가 사용하는 tracer에 접근한 뒤 OpenTelemetry API로 span을 생성할 수 있습니다.

```javascript
import * as Sentry from "@sentry/node";

const tracer = Sentry.getClient()?.tracer;
// Now you can use native APIs on the tracer:
tracer.startActiveSpan("span name", () => {
  // measure something
});
```

다른 tracer를 사용해도 됩니다. 모든 OpenTelemetry span은 Sentry가 자동으로 수집합니다.

## [기본 OpenTelemetry TracerProvider 수정하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/using-opentelemetry-apis.md#modifying-the-default-opentelemetry-tracerprovider)

Sentry의 기본 OpenTelemetry 계측을 사용할 때, Sentry가 설정한 tracer provider에 접근할 수 있습니다.

```javascript
import * as Sentry from "@sentry/node";

const provider = Sentry.getClient()?.traceProvider;
```

## [추가 Span Processor 추가하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/opentelemetry/using-opentelemetry-apis.md#adding-additional-span-processors)

Sentry의 기본 OpenTelemetry 계측을 사용할 때, Sentry가 설정한 tracer provider에 추가 span processor를 더할 수 있습니다.

```javascript
import * as Sentry from "@sentry/node";

Sentry.init({
  dsn: "___DSN___",

  // The SentrySampler will use this to determine which traces to sample
  tracesSampleRate: 1.0,

  // Add additional OpenTelemetry SpanProcessors:
  openTelemetrySpanProcessors: [new MySpanProcessor()],
});
```

