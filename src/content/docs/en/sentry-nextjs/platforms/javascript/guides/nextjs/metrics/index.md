---
title: 'Set Up Metrics | Sentry for Next.js'
description: 'With Sentry Metrics, you can send counters, gauges, and distributions from your applications to Sentry. Once in Sentry, these metrics can be viewed al...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics

# Set Up Metrics | Sentry for Next.js

With [Sentry Metrics](https://docs.sentry.io/product/explore/metrics.md), you can send counters, gauges, and distributions from your applications to Sentry. Once in Sentry, these metrics can be viewed alongside relevant errors, and searched using their individual attributes.

This feature is currently in open beta. Please reach out on [GitHub](https://github.com/getsentry/sentry/discussions/102275) if you have feedback or questions. Features in beta are still in-progress and may have bugs. We recognize the irony.

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#prerequisites)

Metrics are supported in all Sentry JavaScript SDKs version `10.25.0` and above.

[Make sure you have the SDK set up](https://docs.sentry.io/platforms/javascript/guides/nextjs.md) before proceeding.

## [Usage](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#usage)

- [Metric Types](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#metric-types)

| Type           | Use For                                      |
| -------------- | -------------------------------------------- |
| `count`        | Events (orders, clicks, API calls)           |
| `gauge`        | Current values (queue depth, connections)    |
| `distribution` | Value ranges (response times, payload sizes) |

No setup required beyond SDK initialization.

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

- [Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#attributes)

#
- [Filtering and Grouping](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#filtering-and-grouping)

Attributes let you filter and group metrics in Sentry. Use them for:

* Environment segmentation
* Feature flag tracking
* User tier analysis

Each metric has a **2KB size limit**. If you exceed this, the metric will be dropped.

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
- [Scope Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#scope-attributes)

With version `10.33.0`+, use scope APIs to set attributes that apply to all metrics while the scope is active.

Supported types: `string`, `number`, `boolean`

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
- [Units](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#units)

For `gauge` and `distribution` metrics, specify a unit to help Sentry display values in a human-readable format.

Common units: `millisecond`, `second`, `byte`, `kilobyte`, `megabyte`. See [supported units](https://develop.sentry.dev/sdk/foundations/data-model/attributes/#units) for the full list.

```javascript
Sentry.metrics.distribution("response_time", 187.5, {
  unit: "millisecond",
});

Sentry.metrics.gauge("memory_usage", 1024, {
  unit: "byte",
});
```

## [Next.js Patterns](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#nextjs-patterns)

- [API Routes](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#api-routes)

Track request timing and business events in your route handlers.

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

Track form submissions and mutations.

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

Track request patterns at the edge.

Next.js 16+ uses `proxy.ts`, while earlier versions use `middleware.ts`. The pattern is the same.

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

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#options)

- [beforeSendMetric](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#beforesendmetric)

Filter or modify metrics before sending. Return `null` to drop a metric.

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

- [Disable Metrics](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#disable-metrics)

Set `enableMetrics: false` to disable metrics collection entirely.

- [Flush Metrics](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#flush-metrics)

Metrics are buffered and sent periodically. Use this snippet to flush immediately:

```javascript
// Disable metrics
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  enableMetrics: false,
});

// Flush all pending metrics
await Sentry.flush();
```

## [Default Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#default-attributes)

Sentry automatically attaches these attributes to every metric:

| Attribute                            | Description                     | Context     |
| ------------------------------------ | ------------------------------- | ----------- |
| `sentry.environment`                 | Environment from SDK config     | Always      |
| `sentry.release`                     | Release version from SDK config | Always      |
| `sentry.sdk.name`                    | SDK name                        | Always      |
| `sentry.sdk.version`                 | SDK version                     | Always      |
| `user.id`, `user.name`, `user.email` | User identifiers                | If user set |
| `browser.name`, `browser.version`    | Browser info                    | Client-side |
| `sentry.replay_id`                   | Session replay ID               | Client-side |
| `server.address`                     | Server hostname                 | Server-side |

## [Related Features](https://docs.sentry.io/platforms/javascript/guides/nextjs/metrics.md#related-features)

* [Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md) — Drill down from metrics into related traces to understand performance patterns.

* [Logs](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md) — Combine metrics with logs for full observability into your application's behavior.

* [Error Monitoring](https://docs.sentry.io/platforms/javascript/guides/nextjs/usage.md) — Use metrics alongside error tracking to understand the impact of issues.

