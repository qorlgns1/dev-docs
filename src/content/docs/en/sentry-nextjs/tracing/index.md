---
title: 'Set Up Tracing | Sentry for Next.js'
description: 'Tracing captures the timing and flow of requests through your Next.js application. Learn more about tracing and how Sentry uses traces to track perfor...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing

# Set Up Tracing | Sentry for Next.js

Tracing captures the timing and flow of requests through your Next.js application. Learn more about [tracing](https://docs.sentry.io/concepts/key-terms/tracing.md) and how Sentry uses traces to track performance across services.

Sentry automatically instruments most operations, but Server Actions require manual setup.

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#prerequisites)

Before enabling tracing, ensure you have:

* [Installed the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/nextjs.md) in your Next.js application
* Initialized Sentry in all three config files (`instrumentation-client.ts`, `sentry.server.config.ts`, `sentry.edge.config.ts`)

## [Enable Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#enable-tracing)

- [Configure Sample Rate](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#configure-sample-rate)

Add `tracesSampleRate` to your Sentry configuration in all three runtime files.

**Start with 100% in development, and 10-20% in production.** Adjust based on traffic volume and budget.

`instrumentation-client.ts`

```typescript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  tracesSampleRate: process.env.NODE_ENV === "development" ? 1.0 : 0.1,
});
```

## [What's Traced Automatically](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#whats-traced-automatically)

- [By Runtime](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#by-runtime)

The SDK instruments different operations depending on where your code runs:

| Runtime    | Auto-Instrumented                                   |
| ---------- | --------------------------------------------------- |
| **Client** | Page loads, navigations, fetch requests, Web Vitals |
| **Server** | API routes, Server Components, `getServerSideProps` |
| **Edge**   | Middleware, edge API routes                         |

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

For configuration options like timeouts, INP settings, and filtering spans, see [Automatic Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md).

## [Server Actions](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#server-actions)

- [Why Manual Instrumentation?](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#why-manual-instrumentation)

Server Actions are **not** automatically instrumented. Without wrapping, they appear as anonymous server operations with no timing or context.

Use `withServerActionInstrumentation` to:

* Create named spans for each action
* Capture timing and errors
* Connect client and server traces via `headers`
* Attach form data to Sentry events via `formData`

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

- [With Headers and Form Data](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#with-headers-and-form-data)

Pass `headers` to connect client-side traces with server-side spans for full distributed tracing across the browser-to-server boundary. Pass `formData` to attach submitted form data to Sentry events for easier debugging.

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

The SDK automatically captures [Web Vitals](https://docs.sentry.io/product/insights/web-vitals.md) on every page load. These metrics measure real user experience:

| Metric   | What It Measures                               | Threshold (Good) |
| -------- | ---------------------------------------------- | ---------------- |
| **LCP**  | Largest Contentful Paint — loading performance | ≤ 2.5s           |
| **INP**  | Interaction to Next Paint — responsiveness     | ≤ 200ms          |
| **CLS**  | Cumulative Layout Shift — visual stability     | ≤ 0.1            |
| **FCP**  | First Contentful Paint — initial render        | ≤ 1s             |
| **TTFB** | Time to First Byte — server response           | ≤ 100ms          |

Web Vitals appear as measurements on page load transactions and feed into your [Performance Score](https://docs.sentry.io/product/insights/web-vitals.md#performance-score). See [Web Vitals Concepts](https://docs.sentry.io/product/insights/web-vitals/web-vitals-concepts.md) for detailed explanations of each metric.

## [Custom Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#custom-instrumentation)

- [When to Use `startSpan`](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#when-to-use-startspan)

Add custom spans when you want to measure:

* Business operations (checkout flow, multi-step wizards)
* External API calls you want to track separately
* Database operations not auto-captured
* Expensive computations

For the full span API including `startSpanManual` and `startInactiveSpan`, see [Custom Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md).

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

- [Add Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#add-attributes)

Attach data to spans for filtering and debugging in Sentry.

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

## [Distributed Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#distributed-tracing)

- [Automatic Propagation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#automatic-propagation)

The SDK automatically propagates trace context for:

* `fetch()` requests to your own domain
* Server Actions (when using `withServerActionInstrumentation` with headers)

For external APIs, configure `tracePropagationTargets`:

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

For CORS configuration and manual trace propagation (WebSockets, etc.), see [Distributed Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md).

## [Quick Reference](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#quick-reference)

| Scenario                   | Auto-Instrumented? | Action                                |
| -------------------------- | ------------------ | ------------------------------------- |
| Page loads and navigations | Yes                | None                                  |
| API routes (`route.ts`)    | Yes                | None                                  |
| Server Components          | Yes                | None                                  |
| `getServerSideProps`       | Yes                | None                                  |
| **Server Actions**         | **No**             | Use `withServerActionInstrumentation` |
| External API calls         | Partial            | Configure `tracePropagationTargets`   |
| Custom business logic      | No                 | Use `startSpan`                       |

## [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#troubleshooting)

- [High trace volume](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md#high-trace-volume)

If you're sending too many traces, lower your sample rate or use `tracesSampler` for dynamic sampling based on route.

See [Configure Sampling](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/configure-sampling.md) for more options.

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

## Pages in this section

- [Sending Span Metrics](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/span-metrics.md)
- [Set Up Distributed Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md)
- [Configure Sampling](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/configure-sampling.md)
- [Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/troubleshooting.md)

