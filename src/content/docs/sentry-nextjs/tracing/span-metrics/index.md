---
title: '스팬 메트릭 전송 | Next.js용 Sentry'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics

# 스팬 메트릭 전송 | Next.js용 Sentry

스팬 메트릭을 사용하려면 먼저 애플리케이션에서 [트레이싱을 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md)해야 합니다.

스팬 메트릭을 사용하면 트레이싱으로 수집되는 기본 메트릭을 확장하고, 애플리케이션 트레이스 내에서 커스텀 성능 데이터와 디버깅 정보를 추적할 수 있습니다. 메트릭을 계측하는 주요 방법은 두 가지입니다.

1. [기존 스팬에 메트릭 추가](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics.md#adding-metrics-to-existing-spans)
2. [커스텀 메트릭이 포함된 전용 스팬 생성](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics.md#creating-dedicated-metric-spans)

## [기존 스팬에 메트릭 추가](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics.md#adding-metrics-to-existing-spans)

속성을 추가해 기존 스팬에 커스텀 메트릭을 강화할 수 있습니다. 이는 자동 계측을 보강하거나 이미 생성한 스팬에 컨텍스트 데이터를 추가하려는 경우에 유용합니다.

```javascript
const span = Sentry.getActiveSpan();
if (span) {
  // Add individual metrics
  span.setAttribute("database.rows_affected", 42);
  span.setAttribute("cache.hit_rate", 0.85);

  // Add multiple metrics at once
  span.setAttributes({
    "memory.heap_used": 1024000,
    "queue.length": 15,
    "processing.duration_ms": 127,
  });
}
```

- [스팬 속성 모범 사례](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics.md#best-practices-for-span-attributes)

메트릭을 스팬 속성으로 추가할 때:

* 일관된 네이밍 규칙을 사용하세요(예: `category.metric_name`)
* 속성 이름은 간결하면서도 설명적으로 유지하세요
* 적절한 데이터 타입을 사용하세요(string, number, boolean 또는 이들 중 하나의 타입만 포함하는 배열)

## [전용 메트릭 스팬 생성](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics.md#creating-dedicated-metric-spans)

더 세부적인 작업, 태스크 또는 프로세스 추적을 위해, 추적하려는 특정 메트릭이나 속성에 집중한 커스텀 전용 스팬을 생성할 수 있습니다. 이 방식은 발견 가능성을 높이고 더 정밀한 스팬 구성을 제공하지만, 트레이스 워터폴에서 노이즈를 더 많이 만들 수도 있습니다.

```javascript
Sentry.startSpan(
  {
    name: "Database Query Metrics",
    op: "db.metrics",
    attributes: {
      "db.query_type": "SELECT",
      "db.table": "users",
      "db.execution_time_ms": 45,
      "db.rows_returned": 100,
      "db.connection_pool_size": 5,
    },
  },
  () => {
    // Your database operation here
  },
);
```

일반적인 시나리오에서 스팬 메트릭을 구현하는 자세한 예시는 [스팬 메트릭 예시](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics/examples.md) 가이드를 참고하세요.

## [모든 스팬에 메트릭 추가](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics.md#adding-metrics-to-all-spans)

애플리케이션의 모든 스팬에 일관되게 메트릭을 추가하려면 `beforeSendSpan` 콜백을 사용할 수 있습니다.

```javascript
Sentry.init({
  beforeSendSpan(span) {
    span.data = {
      ...span.data,
      "app.version": "1.2.3",
      "environment.region": "us-west-2",
    };

    return span;
  },
});
```

일반적인 시나리오에서 스팬 메트릭을 구현하는 자세한 예시는 [스팬 메트릭 예시](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics/examples.md) 가이드를 참고하세요.

## [스팬 메트릭 vs. 측정값](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics.md#span-metrics-vs-measurements)

이전에는 Sentry가 `Sentry.setMeasurement()` API를 사용해 트랜잭션에 메트릭을 추가하는 방식을 지원했습니다. 이 방식은 더 이상 권장되지 않으며, 대신 스팬 속성을 사용해야 합니다.

## 이 섹션의 페이지

- [예시 계측](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics/examples.md)

