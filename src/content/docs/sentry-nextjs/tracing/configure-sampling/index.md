---
title: '샘플링 구성 | Sentry for Next.js'
description: 'Sentry의 tracing 기능은 분산 trace를 수집하고, 속성을 추가하고, 애플리케이션 전반의 span 성능을 추적해 애플리케이션 성능을 모니터링할 수 있도록 도와줍니다. 하지만 모든 transaction의 trace를 수집하면 상당한 양의 데이터가 생성될 수 ...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/configure-sampling

# 샘플링 구성 | Sentry for Next.js

Sentry의 tracing 기능은 분산 trace를 수집하고, 속성을 추가하고, 애플리케이션 전반의 span 성능을 추적해 애플리케이션 성능을 모니터링할 수 있도록 도와줍니다. 하지만 모든 transaction의 trace를 수집하면 상당한 양의 데이터가 생성될 수 있습니다. 샘플링을 사용하면 애플리케이션에서 Sentry로 전송되는 span의 양을 제어할 수 있습니다.

JavaScript SDK는 샘플링 비율을 제어하는 두 가지 주요 옵션을 제공합니다.

1. [균일 샘플 비율](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/configure-sampling.md#uniform-sample-rate-tracessamplerate) (권장)
2. [샘플링 함수](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/configure-sampling.md#sampling-function-tracessampler)

## [균일 샘플 비율 (`tracesSampleRate`)](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/configure-sampling.md#uniform-sample-rate-tracessamplerate)

`tracesSampleRate`는 0.0에서 1.0 사이의 부동소수점 값으로, transaction이 샘플링될 확률을 제어합니다.

```javascript
// instrumentation-client.js
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.browserTracingIntegration()],
  // Capture 25% of all transactions
  tracesSampleRate: 0.25,
});
```

`tracesSampleRate`를 `0.25`로 설정하면 애플리케이션의 각 transaction이 25% 확률로 무작위 샘플링되므로, 평균적으로 4개의 transaction 중 1개가 Sentry로 전송됩니다.

## [샘플링 함수 (`tracesSampler`)](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/configure-sampling.md#sampling-function-tracessampler)

더 세밀한 제어를 위해 `tracesSampler` 함수를 제공할 수 있습니다. 이 방식으로 다음이 가능합니다.

* transaction 유형별로 서로 다른 샘플링 비율 적용
* 특정 transaction 완전 제외
* transaction 데이터를 기반으로 샘플링 결정
* 분산 trace에서 샘플링 결정 상속 제어

```javascript
// instrumentation-client.js
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.browserTracingIntegration()],
  tracesSampler: (samplingContext) => {
    // Access transaction details from the sampling context
    const { name, attributes, inheritOrSampleWith } = samplingContext;

    // Skip health checks entirely
    if (name.includes("healthcheck")) {
      return 0;
    }

    // Capture all auth-related transactions
    if (name.includes("auth")) {
      return 1;
    }

    // Sample only 1% of comment-related transactions
    if (name.includes("comment")) {
      return 0.01;
    }

    // For everything else, inherit parent sampling decision or use 0.5
    return inheritOrSampleWith(0.5);
  },
});
```

- [샘플링 컨텍스트 객체](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/configure-sampling.md#the-sampling-context-object)

`tracesSampler` 함수가 호출되면, 샘플링 결정을 돕는 유용한 정보가 담긴 `samplingContext` 객체를 전달받습니다.

```typescript
interface SamplingContext {
  // Name of the span/transaction
  name: string;

  // Initial attributes of the span/transaction
  attributes: SpanAttributes | undefined;

  // Whether the parent span was sampled (undefined if no incoming trace)
  parentSampled: boolean | undefined;

  // Sample rate from incoming trace (undefined if no incoming trace)
  parentSampleRate: number | undefined;

  // Utility function to inherit parent decision or fallback
  inheritOrSampleWith: (fallbackRate: number) => number;
}
```

- [Traces Sampler 예제](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/configure-sampling.md#traces-sampler-examples)

1. 중요한 사용자 흐름 우선 처리

```javascript
tracesSampler: (samplingContext) => {
  const { name, attributes, inheritOrSampleWith } = samplingContext;

  // Sample all checkout transactions
  if (name.includes("/checkout") || attributes?.flow === "checkout") {
    return 1.0;
  }

  // Sample 50% of login transactions
  if (name.includes("/login") || attributes?.flow === "login") {
    return 0.5;
  }

  // Sample 10% of everything else
  return inheritOrSampleWith(0.1);
};
```

2. 환경별 처리

```javascript
tracesSampler: (samplingContext) => {
  const { inheritOrSampleWith } = samplingContext;

  // Sample all transactions in development
  if (process.env.NODE_ENV === "development") {
    return 1.0;
  }

  // Sample 5% in production
  if (process.env.NODE_ENV === "production") {
    return 0.05;
  }

  // Sample 20% in staging
  return inheritOrSampleWith(0.2);
};
```

3. 사용자 또는 Transaction 속성 기반 샘플링 제어

```javascript
tracesSampler: (samplingContext) => {
  const { attributes, inheritOrSampleWith } = samplingContext;

  // Always sample for premium users
  if (attributes?.userTier === "premium") {
    return 1.0;
  }

  // Sample more transactions for users experiencing errors
  if (attributes?.hasRecentErrors === true) {
    return 0.8;
  }

  // Sample less for high-volume, low-value paths
  if (attributes?.path?.includes("/api/metrics")) {
    return 0.01;
  }

  // Default sampling rate
  return inheritOrSampleWith(0.2);
};
```

## [샘플링 결정 우선순위](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/configure-sampling.md#sampling-decision-precedence)

여러 샘플링 메커니즘이 동시에 적용될 수 있는 경우, Sentry는 다음 우선순서를 따릅니다.

* `tracesSampler`가 정의되어 있으면 해당 결정이 사용됩니다. `tracesSampler`는 부모 샘플링 결정을 재정의할 수 있지만, 대부분의 사용자는 `tracesSampler`가 부모 샘플링 결정을 존중하도록 설정하는 것이 좋습니다.
* `tracesSampler`가 정의되어 있지 않지만 들어오는 분산 trace의 부모 샘플링 결정이 있으면, 부모 샘플링 결정을 사용합니다.
* 위 두 가지 모두 해당하지 않으면 `tracesSampleRate`를 사용합니다.
* `tracesSampleRate`가 0으로 설정되어 있으면 어떤 span도 샘플링되지 않으며, 하위 span도 부모 샘플링 결정을 상속하므로 샘플링되지 않습니다.
* 위 항목 중 어느 것도 설정되지 않으면 어떤 transaction도 샘플링되지 않으며 tracing이 비활성화됩니다.

## [결론](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/configure-sampling.md#conclusion)

효과적인 샘플링은 오버헤드를 최소화하면서 Sentry 성능 모니터링의 가치를 최대한 끌어내는 핵심입니다. `tracesSampler` 함수는 어떤 transaction을 기록할지 정밀하게 제어할 수 있게 해주므로, 애플리케이션에서 가장 중요한 부분에 집중할 수 있습니다.

