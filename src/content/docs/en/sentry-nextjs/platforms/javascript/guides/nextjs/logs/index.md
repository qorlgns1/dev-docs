---
title: 'Set Up Logs | Sentry for Next.js'
description: 'Sentry Logs let you send structured log data from your Next.js application. Unlike traditional string-based logging, structured logs include queryable...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/logs

# Set Up Logs | Sentry for Next.js

Sentry Logs let you send structured log data from your Next.js application. Unlike traditional string-based logging, structured logs include queryable attributes that help you debug issues faster by filtering on specific users, orders, or any business context you include.

## [Setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#setup)

- [Enable Logging](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#enable-logging)

Add `enableLogs: true` to your Sentry configuration in all three runtime files.

Logs work across all Next.js runtimes:

* **Client** — Browser-side logging
* **Server** — Node.js server-side logging
* **Edge** — Edge runtime logging

`instrumentation-client.ts`

```typescript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  enableLogs: true,
});
```

## [Send Logs](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#send-logs)

- [Log Levels](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#log-levels)

Use the appropriate level for each message:

| Level   | When to Use                      |
| ------- | -------------------------------- |
| `trace` | Fine-grained debugging           |
| `debug` | Development diagnostics          |
| `info`  | Normal operations, milestones    |
| `warn`  | Potential issues, degraded state |
| `error` | Failures that need attention     |
| `fatal` | Critical failures, system down   |

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

## [Add Context](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#add-context)

- [Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#attributes)

Pass structured data as the second argument. These attributes become queryable columns in Sentry.

Use the `fmt` helper for parameterized messages — values are extracted as searchable attributes.

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

- [Scope Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#scope-attributes)

Set attributes on a scope to automatically include them in all logs within that context.

Scopes don't propagate between Next.js runtimes. To include attributes on logs from all three runtimes, call `getIsolationScope().setAttribute()` in each (client, edge, server). Use isolation scope (not global) to prevent data leaking between concurrent requests. For server-side code, set context before any try/catch blocks so errors include it.

See [Different Kinds of Scopes](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#different-kinds-of-scopes) to learn more.

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

## [Best Practices](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#best-practices)

- [Wide Events Over Scattered Logs](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#wide-events-over-scattered-logs)

Instead of many thin logs that are hard to correlate, emit one comprehensive log per operation with all relevant context.

This makes debugging dramatically faster — one query returns everything about a specific order, user, or request.

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

- [Include Business Context](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#include-business-context)

Add attributes that help you prioritize and debug:

* **User context** — tier, account age, lifetime value
* **Transaction data** — order value, item count
* **Feature state** — active feature flags
* **Request metadata** — endpoint, method, duration

This lets you filter logs by high-value customers or specific features.

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

- [Consistent Attribute Naming](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#consistent-attribute-naming)

Pick a naming convention and stick with it across your codebase. Inconsistent names make queries impossible.

**Recommended:** Use `snake_case` for custom attributes to match common conventions.

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

## [Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#integrations)

- [Console](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#console)

Capture `console.log`, `console.warn`, and `console.error` calls as structured logs.

The integration parses multiple arguments as searchable attributes.

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

Send logs from the [Pino](https://github.com/pinojs/pino) logging library to Sentry.

Requires SDK version `10.18.0` or higher.

```typescript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  enableLogs: true,
  integrations: [Sentry.pinoIntegration()],
});
```

See [Pino integration docs](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md) for configuration options.

- [Consola](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#consola)

Send logs from the [Consola](https://github.com/unjs/consola) logging library to Sentry.

Requires SDK version `10.12.0` or higher and `enableLogs: true` in your `Sentry.init` call.

```typescript
import { consola } from "consola";

const sentryReporter = Sentry.createConsolaReporter({
  levels: ["error", "warn"], // optional filter
});

consola.addReporter(sentryReporter);
```

- [Winston](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#winston)

Send logs from the [Winston](https://github.com/winstonjs/winston) logging library to Sentry.

Requires SDK version `9.13.0` or higher and `enableLogs: true` in your `Sentry.init` call.

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

- [Upcoming Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#upcoming-integrations)

* [Node Bunyan](https://github.com/getsentry/sentry-javascript/issues/16474)

[Request an integration](https://github.com/getsentry/sentry-javascript/issues/new/choose)

## [Filter Logs](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#filter-logs)

- [beforeSendLog](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#beforesendlog)

Filter or modify logs before they're sent. Return `null` to drop a log.

Use this to:

* Remove sensitive data
* Filter noisy logs
* Add computed attributes

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

## [Default Attributes](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#default-attributes)

Sentry automatically adds these attributes to every log:

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

## [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#troubleshooting)

- [Logs not appearing](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#logs-not-appearing)

Make sure `enableLogs: true` is set in **all** Sentry config files:

* `instrumentation-client.ts` (client)
* `sentry.server.config.ts` (server)
* `sentry.edge.config.ts` (edge)

- [Logs being dropped](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#logs-being-dropped)

Logs larger than 1 MB are dropped. Check your [org stats](https://sentry.io/orgredirect/organizations/:orgslug/stats/?dataCategory=logBytes\&statsPeriod=30d) to see if logs are being rate limited or dropped.

### [Attributes showing \[Filtered\]](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#attributes-showing-filtered)

If attributes show `[Filtered]`, they're being removed by [server-side data scrubbing](https://docs.sentry.io/security-legal-pii/scrubbing/server-side-scrubbing.md). Check your project's data scrubbing settings to adjust what gets filtered.

