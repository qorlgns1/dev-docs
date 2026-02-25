---
title: 'Metrics 설정 | Next.js용 Sentry'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics

# Metrics 설정 | Next.js용 Sentry

[Sentry Metrics](https://docs.sentry.io/product/explore/metrics.md)를 사용하면 애플리케이션에서 카운터, 게이지, 분포 지표를 Sentry로 전송할 수 있습니다. Sentry에 들어온 후에는 관련 에러와 함께 이 메트릭을 확인하고, 각 메트릭의 개별 속성으로 검색할 수 있습니다.

이 기능은 현재 오픈 베타입니다. 피드백이나 질문이 있다면 [GitHub](https://github.com/getsentry/sentry/discussions/102275)로 알려주세요. 베타 기능은 아직 개발 진행 중이며 버그가 있을 수 있습니다. 이 아이러니함은 저희도 알고 있습니다.

## [사전 요구사항](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#prerequisites)

Metrics는 버전 `10.25.0` 이상인 모든 Sentry JavaScript SDK에서 지원됩니다.

진행하기 전에 [SDK 설정이 완료되었는지 확인하세요](https://docs.sentry.io/platforms/javascript/guides/nextjs.md).

## [사용법](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#usage)

- [메트릭 유형](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#metric-types)

| 유형           | 사용 목적                                     |
| -------------- | -------------------------------------------- |
| `count`        | 이벤트 (주문, 클릭, API 호출)                 |
| `gauge`        | 현재 값 (큐 깊이, 연결 수)                    |
| `distribution` | 값 범위 (응답 시간, 페이로드 크기)            |

SDK 초기화 외에 추가 설정은 필요하지 않습니다.

```javascript
import * as Sentry from "@sentry/browser";

// Count occurrences
Sentry.metrics.count("orders_created", 1);

// Track current values
Sentry.metrics.gauge("active_connections", 42);

// Track distributions
Sentry.metrics.distribution("api_latency", 187, {
  unit: "millisecond",
});
```

- [속성](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#attributes)

#
- [필터링 및 그룹화](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#filtering-and-grouping)

속성을 사용하면 Sentry에서 메트릭을 필터링하고 그룹화할 수 있습니다. 다음과 같은 용도로 사용하세요.

* 환경 분할
* 기능 플래그 추적
* 사용자 티어 분석

각 메트릭에는 **2KB 크기 제한**이 있습니다. 이를 초과하면 해당 메트릭은 삭제됩니다.

```javascript
Sentry.metrics.count("api_calls", 1, {
  attributes: {
    endpoint: "/api/orders",
    user_tier: "pro",
    region: "us-west",
    user_id: user.id,
    order_id: order.id,
  },
});
```

#
- [스코프 속성](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#scope-attributes)

버전 `10.33.0`+에서는 스코프가 활성화되어 있는 동안 모든 메트릭에 적용되는 속성을 설정하기 위해 스코프 API를 사용할 수 있습니다.

지원 타입: `string`, `number`, `boolean`

```javascript
Sentry.getGlobalScope().setAttributes({
  is_admin: true,
  auth_provider: "google",
});

Sentry.withScope((scope) => {
  scope.setAttribute("step", "authentication");

  // All scope attributes are added
  Sentry.metrics.count("clicks", 1);
  Sentry.metrics.gauge("time_since_refresh", 4, { unit: "hour" });
});
```

#
- [단위](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#units)

`gauge` 및 `distribution` 메트릭의 경우, Sentry가 값을 사람이 읽기 쉬운 형식으로 표시하도록 단위를 지정하세요.

일반적인 단위: `millisecond`, `second`, `byte`, `kilobyte`, `megabyte`. 전체 목록은 [지원 단위](https://develop.sentry.dev/sdk/foundations/data-model/attributes/#units)를 참고하세요.

```javascript
Sentry.metrics.distribution("response_time", 187.5, {
  unit: "millisecond",
});

Sentry.metrics.gauge("memory_usage", 1024, {
  unit: "byte",
});
```

## [Next.js 패턴](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#nextjs-patterns)

- [API Routes](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#api-routes)

라우트 핸들러에서 요청 타이밍과 비즈니스 이벤트를 추적합니다.

`app/api/orders/route.ts`

```typescript
import * as Sentry from "@sentry/nextjs";

export async function POST(request: Request) {
  const start = Date.now();

  try {
    const order = await createOrder(request);

    Sentry.metrics.count("orders_created", 1, {
      attributes: { status: "success" },
    });

    return Response.json(order);
  } catch (error) {
    Sentry.metrics.count("orders_created", 1, {
      attributes: { status: "failed" },
    });
    throw error;
  } finally {
    Sentry.metrics.distribution("order_latency", Date.now() - start, {
      unit: "millisecond",
    });
  }
}
```

- [Server Actions](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#server-actions)

폼 제출과 변이를 추적합니다.

`app/actions.ts`

```typescript
"use server";

import * as Sentry from "@sentry/nextjs";

export async function submitCheckout(formData: FormData) {
  Sentry.metrics.count("checkout_attempts", 1);

  try {
    const result = await processCheckout(formData);
    Sentry.metrics.count("checkout_success", 1);
    return result;
  } catch (error) {
    Sentry.metrics.count("checkout_failures", 1);
    throw error;
  }
}
```

- [Proxy / Middleware](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#proxy--middleware)

엣지에서 요청 패턴을 추적합니다.

Next.js 16+는 `proxy.ts`를 사용하고, 이전 버전은 `middleware.ts`를 사용합니다. 패턴은 동일합니다.

`proxy.ts`

```typescript
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";
import * as Sentry from "@sentry/nextjs";

export function proxy(request: NextRequest) {
  Sentry.metrics.count("requests", 1, {
    attributes: {
      path: request.nextUrl.pathname,
      method: request.method,
    },
  });

  return NextResponse.next();
}
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#options)

- [beforeSendMetric](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#beforesendmetric)

전송 전에 메트릭을 필터링하거나 수정합니다. 메트릭을 삭제하려면 `null`을 반환하세요.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  beforeSendMetric: (metric) => {
    // Drop specific metrics
    if (metric.name === "debug_metric") {
      return null;
    }

    // Add attributes
    metric.attributes = {
      ...metric.attributes,
      processed: true,
    };

    return metric;
  },
});
```

- [Metrics 비활성화](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#disable-metrics)

메트릭 수집을 완전히 비활성화하려면 `enableMetrics: false`로 설정하세요.

- [Metrics 플러시](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#flush-metrics)

메트릭은 버퍼링되어 주기적으로 전송됩니다. 즉시 플러시하려면 다음 스니펫을 사용하세요.

```javascript
// Disable metrics
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  enableMetrics: false,
});

// Flush all pending metrics
await Sentry.flush();
```

## [기본 속성](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#default-attributes)

Sentry는 모든 메트릭에 다음 속성을 자동으로 추가합니다.

| 속성                                 | 설명                            | 컨텍스트      |
| ------------------------------------ | ------------------------------- | ----------- |
| `sentry.environment`                 | SDK 설정의 환경 값               | 항상         |
| `sentry.release`                     | SDK 설정의 릴리스 버전            | 항상         |
| `sentry.sdk.name`                    | SDK 이름                         | 항상         |
| `sentry.sdk.version`                 | SDK 버전                         | 항상         |
| `user.id`, `user.name`, `user.email` | 사용자 식별자                    | 사용자 설정 시 |
| `browser.name`, `browser.version`    | 브라우저 정보                    | 클라이언트 측  |
| `sentry.replay_id`                   | 세션 리플레이 ID                  | 클라이언트 측  |
| `server.address`                     | 서버 호스트명                     | 서버 측       |

## [관련 기능](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#related-features)

* [Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md) — 메트릭에서 관련 트레이스로 드릴다운해 성능 패턴을 파악합니다.

* [Logs](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md) — 메트릭과 로그를 결합해 애플리케이션 동작에 대한 완전한 가시성을 확보합니다.

* [Error Monitoring](https://docs.sentry.io/platforms/javascript/guides/nextjs/usage.md) — 에러 추적과 함께 메트릭을 사용해 이슈의 영향을 파악합니다.

