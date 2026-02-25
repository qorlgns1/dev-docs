---
title: '로그 설정 | Next.js용 Sentry'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/logs'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/logs

# 로그 설정 | Next.js용 Sentry

Sentry Logs를 사용하면 Next.js 애플리케이션에서 구조화된 로그 데이터를 전송할 수 있습니다. 기존의 문자열 기반 로깅과 달리, 구조화된 로그에는 쿼리 가능한 속성이 포함되어 있어 특정 사용자, 주문 또는 포함한 비즈니스 컨텍스트로 필터링하여 문제를 더 빠르게 디버깅할 수 있습니다.

## [설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#setup)

- [로깅 활성화](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#enable-logging)

세 가지 런타임 파일 모두의 Sentry 설정에 `enableLogs: true`를 추가하세요.

로그는 모든 Next.js 런타임에서 동작합니다.

* **Client** — 브라우저 측 로깅
* **Server** — Node.js 서버 측 로깅
* **Edge** — Edge 런타임 로깅

`instrumentation-client.ts`

```typescript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  enableLogs: true,
});
```

## [로그 전송](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#send-logs)

- [로그 레벨](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#log-levels)

각 메시지에 맞는 적절한 레벨을 사용하세요.

| 레벨    | 사용 시점                         |
| ------- | --------------------------------- |
| `trace` | 세밀한 디버깅                     |
| `debug` | 개발 진단                         |
| `info`  | 일반 동작, 마일스톤               |
| `warn`  | 잠재적 문제, 성능 저하 상태       |
| `error` | 대응이 필요한 실패                |
| `fatal` | 치명적 실패, 시스템 다운          |

```typescript
import * as Sentry from "@sentry/nextjs";

// Different log levels
Sentry.logger.trace("Entering function", { fn: "processOrder" });
Sentry.logger.debug("Cache lookup", { key: "user:123" });
Sentry.logger.info("Order created", { orderId: "order_456" });
Sentry.logger.warn("Rate limit approaching", { current: 95, max: 100 });
Sentry.logger.error("Payment failed", { reason: "card_declined" });
Sentry.logger.fatal("Database unavailable", { host: "primary" });
```

## [컨텍스트 추가](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#add-context)

- [속성](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#attributes)

두 번째 인수로 구조화된 데이터를 전달하세요. 이 속성들은 Sentry에서 쿼리 가능한 컬럼이 됩니다.

파라미터화된 메시지에는 `fmt` 헬퍼를 사용하세요. 값이 검색 가능한 속성으로 추출됩니다.

```typescript
// Pass attributes directly
Sentry.logger.info("User signed up", {
  userId: user.id,
  plan: "pro",
  referrer: "google",
});

// Use fmt for parameterized messages
Sentry.logger.info(
  Sentry.logger.fmt`User ${userId} purchased ${productName}`,
);
```

- [스코프 속성](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#scope-attributes)

스코프에 속성을 설정하면 해당 컨텍스트 내 모든 로그에 자동으로 포함됩니다.

스코프는 Next.js 런타임 간에 전파되지 않습니다. 세 런타임 모두에서 생성되는 로그에 속성을 포함하려면 각 런타임(client, edge, server)에서 `getIsolationScope().setAttribute()`를 호출하세요. 동시 요청 간 데이터 누수를 방지하려면 전역 스코프가 아니라 격리 스코프를 사용해야 합니다. 서버 측 코드에서는 오류에도 컨텍스트가 포함되도록 모든 try/catch 블록 이전에 컨텍스트를 설정하세요.

자세한 내용은 [다양한 스코프 종류](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#different-kinds-of-scopes)를 참고하세요.

```typescript
// setAttribute() or setAttributes()
// Global scope - shared across entire app
Sentry.getGlobalScope().setAttributes({
  service: "checkout",
  version: "2.1.0",
});

// Isolation scope - unique per request
Sentry.getIsolationScope().setAttributes({
  org_id: user.orgId,
  user_tier: user.tier,
});

// Current scope - single operation
Sentry.withScope((scope) => {
  scope.setAttribute("request_id", req.id);
  Sentry.logger.info("Processing order");
});
```

## [모범 사례](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#best-practices)

- [흩어진 로그보다 포괄적 이벤트](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#wide-events-over-scattered-logs)

상호 연관시키기 어려운 얇은 로그를 많이 남기는 대신, 관련 컨텍스트를 모두 담은 포괄적인 로그를 작업 단위로 하나씩 내보내세요.

이렇게 하면 디버깅 속도가 크게 빨라집니다. 쿼리 한 번으로 특정 주문, 사용자 또는 요청에 대한 모든 정보를 확인할 수 있습니다.

```typescript
// ❌ Scattered thin logs
Sentry.logger.info("Starting checkout");
Sentry.logger.info("Validating cart");
Sentry.logger.info("Processing payment");
Sentry.logger.info("Checkout complete");

// ✅ One wide event with full context
Sentry.logger.info("Checkout completed", {
  orderId: order.id,
  userId: user.id,
  userTier: user.subscription,
  cartValue: cart.total,
  itemCount: cart.items.length,
  paymentMethod: "stripe",
  duration: Date.now() - startTime,
});
```

- [비즈니스 컨텍스트 포함](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#include-business-context)

우선순위 지정과 디버깅에 도움이 되는 속성을 추가하세요.

* **사용자 컨텍스트** — 티어, 계정 사용 기간, 생애 가치
* **트랜잭션 데이터** — 주문 금액, 품목 수
* **기능 상태** — 활성화된 feature flag
* **요청 메타데이터** — endpoint, method, duration

이렇게 하면 고가치 고객이나 특정 기능 기준으로 로그를 필터링할 수 있습니다.

```typescript
Sentry.logger.info("API request completed", {
  // User context
  userId: user.id,
  userTier: user.plan, // "free" | "pro" | "enterprise"
  accountAgeDays: user.ageDays,

  // Request data
  endpoint: "/api/orders",
  method: "POST",
  duration: 234,

  // Business context
  orderValue: 149.99,
  featureFlags: ["new-checkout", "discount-v2"],
});
```

- [일관된 속성 네이밍](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#consistent-attribute-naming)

코드베이스 전반에서 일관된 네이밍 규칙을 정하고 유지하세요. 이름이 일관되지 않으면 쿼리가 사실상 불가능해집니다.

**권장:** 일반적인 관례에 맞게 커스텀 속성에는 `snake_case`를 사용하세요.

```typescript
// ❌ Inconsistent naming
{ user: "123" }
{ userId: "123" }
{ user_id: "123" }
{ UserID: "123" }

// ✅ Consistent snake_case
{
  user_id: "123",
  order_id: "456",
  cart_value: 99.99,
  item_count: 3,
}
```

## [통합](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#integrations)

- [Console](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#console)

`console.log`, `console.warn`, `console.error` 호출을 구조화된 로그로 수집합니다.

이 통합은 여러 인수를 검색 가능한 속성으로 파싱합니다.

```typescript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  enableLogs: true,
  integrations: [
    Sentry.consoleLoggingIntegration({
      levels: ["log", "warn", "error"],
    }),
  ],
});

// Arguments become searchable attributes
console.log("User action:", userId, success);
// -> message.parameter.0: userId
// -> message.parameter.1: success
```

- [Pino](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#pino)

[Pino](https://github.com/pinojs/pino) 로깅 라이브러리의 로그를 Sentry로 전송합니다.

SDK 버전 `10.18.0` 이상이 필요합니다.

```typescript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  enableLogs: true,
  integrations: [Sentry.pinoIntegration()],
});
```

구성 옵션은 [Pino integration docs](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md)를 참고하세요.

- [Consola](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#consola)

[Consola](https://github.com/unjs/consola) 로깅 라이브러리의 로그를 Sentry로 전송합니다.

SDK 버전 `10.12.0` 이상과 `Sentry.init` 호출의 `enableLogs: true` 설정이 필요합니다.

```typescript
import { consola } from "consola";

const sentryReporter = Sentry.createConsolaReporter({
  levels: ["error", "warn"], // optional filter
});

consola.addReporter(sentryReporter);
```

- [Winston](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#winston)

[Winston](https://github.com/winstonjs/winston) 로깅 라이브러리의 로그를 Sentry로 전송합니다.

SDK 버전 `9.13.0` 이상과 `Sentry.init` 호출의 `enableLogs: true` 설정이 필요합니다.

```typescript
import winston from "winston";
import Transport from "winston-transport";

const SentryTransport = Sentry.createSentryWinstonTransport(Transport, {
  levels: ["error", "warn"], // optional filter
});

const logger = winston.createLogger({
  transports: [new SentryTransport()],
});
```

- [예정된 통합](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#upcoming-integrations)

* [Node Bunyan](https://github.com/getsentry/sentry-javascript/issues/16474)

[통합 요청하기](https://github.com/getsentry/sentry-javascript/issues/new/choose)

## [로그 필터링](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#filter-logs)

- [beforeSendLog](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#beforesendlog)

전송 전에 로그를 필터링하거나 수정합니다. 로그를 버리려면 `null`을 반환하세요.

다음과 같은 용도로 사용하세요.

* 민감한 데이터 제거
* 노이즈성 로그 필터링
* 계산된 속성 추가

`instrumentation-client.ts`

```typescript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  enableLogs: true,

  beforeSendLog(log) {
    // Drop debug logs in production
    if (log.level === "debug") {
      return null;
    }

    // Remove sensitive attributes
    if (log.attributes?.password) {
      delete log.attributes.password;
    }

    return log;
  },
});
```

## [기본 속성](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#default-attributes)

Sentry는 모든 로그에 다음 속성을 자동으로 추가합니다.

```json
{
  "message": "Order completed",
  "level": "info",
  "attributes": {
    // Your custom attributes
    "order_id": "order_123",
    "user_tier": "pro",

    // Core (always present)

    "sentry.environment": "production",
    "sentry.release": "my-app@1.2.3",
    "sentry.sdk.name": "sentry.javascript.nextjs",
    "sentry.sdk.version": "9.0.0",

    // User (if set via Sentry.setUser)

    "user.id": "user_456",
    "user.email": "jane@example.com",
    "user.name": "Jane",

    // Browser (client-side only)

    "browser.name": "Chrome",
    "browser.version": "120.0.0",

    // Server (server-side only)

    "server.address": "api-server-1",

    // Trace (if tracing enabled)

    "sentry.trace.parent_span_id": "abc123",
    "sentry.replay_id": "def456",

    // Message (when using fmt)

    "sentry.message.template": "Order {} completed",
    "sentry.message.parameter.0": "order_123",

    // Payload

    "payload_size": 342

  }
}
```

## [문제 해결](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#troubleshooting)

- [로그가 표시되지 않음](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#logs-not-appearing)

모든 Sentry 설정 파일에 `enableLogs: true`가 설정되어 있는지 확인하세요.

* `instrumentation-client.ts` (client)
* `sentry.server.config.ts` (server)
* `sentry.edge.config.ts` (edge)

- [로그가 드롭됨](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#logs-being-dropped)

1 MB보다 큰 로그는 드롭됩니다. 로그가 rate limit에 걸리거나 드롭되는지 확인하려면 [org stats](https://sentry.io/orgredirect/organizations/:orgslug/stats/?dataCategory=logBytes\&statsPeriod=30d)를 확인하세요.

### [\[Filtered\]로 표시되는 속성](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#attributes-showing-filtered)

속성이 `[Filtered]`로 표시된다면 [server-side data scrubbing](https://docs.sentry.io/security-legal-pii/scrubbing/server-side-scrubbing.md)에 의해 제거되고 있는 것입니다. 무엇을 필터링할지 조정하려면 프로젝트의 data scrubbing 설정을 확인하세요.

