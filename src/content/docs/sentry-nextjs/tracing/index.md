---
title: '트레이싱 설정 | Next.js용 Sentry'
description: '트레이싱은 Next.js 애플리케이션을 통과하는 요청의 타이밍과 흐름을 캡처합니다. tracing과 Sentry가 서비스 전반의 성능을 추적하기 위해 트레이스를 사용하는 방법을 자세히 알아보세요.'
---

소스 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing

# 트레이싱 설정 | Next.js용 Sentry

트레이싱은 Next.js 애플리케이션을 통과하는 요청의 타이밍과 흐름을 캡처합니다. [tracing](https://docs.sentry.io/concepts/key-terms/tracing.md)과 Sentry가 서비스 전반의 성능을 추적하기 위해 트레이스를 사용하는 방법을 자세히 알아보세요.

Sentry는 대부분의 작업을 자동으로 계측하지만, Server Action은 수동 설정이 필요합니다.

## [사전 요구사항](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#prerequisites)

트레이싱을 활성화하기 전에 다음을 확인하세요.

* Next.js 애플리케이션에 [Sentry SDK 설치](https://docs.sentry.io/platforms/javascript/guides/nextjs.md)
* 세 가지 설정 파일(`instrumentation-client.ts`, `sentry.server.config.ts`, `sentry.edge.config.ts`) 모두에서 Sentry 초기화

## [트레이싱 활성화](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#enable-tracing)

- [샘플링 비율 구성](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#configure-sample-rate)

세 가지 런타임 파일 모두의 Sentry 설정에 `tracesSampleRate`를 추가하세요.

**개발 환경에서는 100%, 운영 환경에서는 10-20%로 시작하세요.** 트래픽 규모와 예산에 맞춰 조정하세요.

`instrumentation-client.ts`

```typescript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  tracesSampleRate: process.env.NODE_ENV === "development" ? 1.0 : 0.1,
});
```

## [자동으로 트레이싱되는 항목](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#whats-traced-automatically)

- [런타임별](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#by-runtime)

SDK는 코드가 실행되는 위치에 따라 서로 다른 작업을 계측합니다.

| Runtime    | 자동 계측 항목                                       |
| ---------- | ---------------------------------------------------- |
| **Client** | 페이지 로드, 내비게이션, fetch 요청, Web Vitals      |
| **Server** | API 라우트, Server Components, `getServerSideProps` |
| **Edge**   | Middleware, edge API 라우트                          |

```tsx
// All of these create spans automatically

// Client: navigation creates a span
<Link href="/dashboard">Dashboard</Link>;

// Server: API route creates a span
export async function GET() {
  return Response.json({ data });
}

// Server Component: creates a span
export default async function Page() {
  const data = await fetchData();
  return <div>{data}</div>;
}
```

타임아웃, INP 설정, span 필터링 같은 구성 옵션은 [Automatic Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md)을 참고하세요.

## [Server Actions](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#server-actions)

- [왜 수동 계측이 필요한가요?](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#why-manual-instrumentation)

Server Action은 자동으로 계측되지 **않습니다**. 래핑하지 않으면 타이밍이나 컨텍스트 없이 익명 서버 작업으로 표시됩니다.

`withServerActionInstrumentation`을 사용하면 다음이 가능합니다.

* 각 액션에 대해 이름 있는 span 생성
* 타이밍 및 오류 캡처
* `headers`를 통해 클라이언트와 서버 트레이스 연결
* `formData`를 통해 Sentry 이벤트에 폼 데이터 첨부

`app/actions.ts`

```tsx
"use server";

import * as Sentry from "@sentry/nextjs";

export async function createOrder(formData: FormData) {
  return Sentry.withServerActionInstrumentation(
    "createOrder",
    async () => {
      // Your action logic
      const order = await db.orders.create({
        data: { items: formData.get("items") },
      });
      return { success: true, orderId: order.id };
    },
  );
}
```

- [헤더와 폼 데이터 함께 사용](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#with-headers-and-form-data)

`headers`를 전달해 클라이언트 측 트레이스와 서버 측 span을 연결하면 브라우저-서버 경계를 넘는 전체 분산 트레이싱이 가능합니다. `formData`를 전달하면 제출된 폼 데이터를 Sentry 이벤트에 첨부해 디버깅을 더 쉽게 할 수 있습니다.

`app/actions.ts`

```tsx
"use server";

import * as Sentry from "@sentry/nextjs";
import { headers } from "next/headers";

export async function submitForm(formData: FormData) {
  return Sentry.withServerActionInstrumentation(
    "submitForm",
    {
      headers: await headers(), // Connect client and server traces
      formData, // Attach form data to events
      recordResponse: true, // Include response data
    },
    async () => {
      // Action logic with full trace context
    },
  );
}
```

## [Web Vitals](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#web-vitals)

SDK는 모든 페이지 로드에서 [Web Vitals](https://docs.sentry.io/product/insights/web-vitals.md)를 자동으로 캡처합니다. 이 지표는 실제 사용자 경험을 측정합니다.

| Metric   | 측정 대상                                      | 기준값(좋음) |
| -------- | ---------------------------------------------- | ------------ |
| **LCP**  | Largest Contentful Paint — 로딩 성능           | ≤ 2.5s       |
| **INP**  | Interaction to Next Paint — 반응성             | ≤ 200ms      |
| **CLS**  | Cumulative Layout Shift — 시각적 안정성        | ≤ 0.1        |
| **FCP**  | First Contentful Paint — 초기 렌더링           | ≤ 1s         |
| **TTFB** | Time to First Byte — 서버 응답                 | ≤ 100ms      |

Web Vitals는 페이지 로드 트랜잭션의 measurement로 표시되며 [Performance Score](https://docs.sentry.io/product/insights/web-vitals.md#performance-score)에 반영됩니다. 각 지표에 대한 자세한 설명은 [Web Vitals Concepts](https://docs.sentry.io/product/insights/web-vitals/web-vitals-concepts.md)를 참고하세요.

## [커스텀 계측](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#custom-instrumentation)

- [`startSpan`을 사용해야 하는 경우](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#when-to-use-startspan)

다음을 측정하고 싶다면 커스텀 span을 추가하세요.

* 비즈니스 작업(체크아웃 플로우, 다단계 위저드)
* 별도로 추적하려는 외부 API 호출
* 자동 캡처되지 않는 데이터베이스 작업
* 비용이 큰 계산 작업

`startSpanManual`, `startInactiveSpan`을 포함한 전체 span API는 [Custom Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md)을 참고하세요.

`app/api/checkout/route.ts`

```tsx
import * as Sentry from "@sentry/nextjs";

export async function POST(request: Request) {
  return Sentry.startSpan(
    { name: "checkout.process", op: "checkout" },
    async () => {
      // Nested spans for sub-operations
      const cart = await Sentry.startSpan(
        { name: "checkout.validate_cart", op: "validation" },
        () => validateCart(request),
      );

      const payment = await Sentry.startSpan(
        { name: "checkout.process_payment", op: "payment" },
        () => processPayment(cart),
      );

      return Response.json({ orderId: payment.orderId });
    },
  );
}
```

- [속성 추가](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#add-attributes)

Sentry에서 필터링과 디버깅을 위해 span에 데이터를 첨부하세요.

```tsx
Sentry.startSpan(
  {
    name: "order.process",
    op: "order",
    attributes: {
      "order.id": orderId,
      "order.value": cart.total,
      "order.item_count": cart.items.length,
    },
  },
  async () => {
    // Operation logic
  },
);
```

## [분산 트레이싱](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#distributed-tracing)

- [자동 전파](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#automatic-propagation)

SDK는 다음에 대해 트레이스 컨텍스트를 자동 전파합니다.

* 자체 도메인으로의 `fetch()` 요청
* Server Actions(`withServerActionInstrumentation`을 headers와 함께 사용할 때)

외부 API의 경우 `tracePropagationTargets`를 구성하세요.

`instrumentation-client.ts`

```typescript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  tracesSampleRate: 0.1,

  // Propagate traces to these external services
  tracePropagationTargets: [
    "localhost",
    /^https:\/\/api\.yourcompany\.com/,
    /^https:\/\/payments\.stripe\.com/,
  ],
});
```

CORS 구성 및 수동 트레이스 전파(WebSockets 등)는 [Distributed Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md)을 참고하세요.

## [빠른 참조](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#quick-reference)

| 시나리오                     | 자동 계측 여부      | 조치                                  |
| ---------------------------- | ------------------- | ------------------------------------- |
| 페이지 로드 및 내비게이션    | Yes                 | 없음                                  |
| API 라우트 (`route.ts`)      | Yes                 | 없음                                  |
| Server Components            | Yes                 | 없음                                  |
| `getServerSideProps`         | Yes                 | 없음                                  |
| **Server Actions**           | **No**              | `withServerActionInstrumentation` 사용 |
| 외부 API 호출                | Partial             | `tracePropagationTargets` 구성        |
| 커스텀 비즈니스 로직         | No                  | `startSpan` 사용                      |

## [문제 해결](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#troubleshooting)

- [트레이스 볼륨이 높은 경우](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#high-trace-volume)

트레이스를 너무 많이 전송하고 있다면 샘플링 비율을 낮추거나, 라우트 기반 동적 샘플링을 위해 `tracesSampler`를 사용하세요.

더 많은 옵션은 [Configure Sampling](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/configure-sampling.md)을 참고하세요.

```typescript
Sentry.init({
  tracesSampler: ({ name }) => {
    // Sample 5% of health checks
    if (name.includes("health")) return 0.05;
    // Sample 50% of API routes
    if (name.includes("/api/")) return 0.5;
    // Default 10%
    return 0.1;
  },
});
```

## 이 섹션의 페이지

- [Sending Span Metrics](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics.md)
- [Set Up Distributed Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md)
- [Configure Sampling](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/configure-sampling.md)
- [Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/troubleshooting.md)

