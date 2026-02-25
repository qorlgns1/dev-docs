---
title: 'Redis | Sentry for Next.js'
description: 'This integration only works in the Node.js and Bun runtimes.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/redis

# Redis | Sentry for Next.js

This integration only works in the Node.js and Bun runtimes.

*Import name: `Sentry.redisIntegration`*

This integration is enabled by default when performance monitoring is enabled. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

The `redisIntegration` adds instrumentation for the `ioredis` and `redis` library to capture spans using [`@opentelemetry/instrumentation-ioredis`](https://www.npmjs.com/package/@opentelemetry/instrumentation-ioredis) and [`@opentelemetry/instrumentation-redis-4`](https://www.npmjs.com/package/@opentelemetry/instrumentation-redis-4).

```JavaScript
Sentry.init({
  integrations: [Sentry.redisIntegration()],
});
```

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/redis.md#supported-versions)

* `ioredis`: `>=2.0.0 <6`
* `redis`: `>=4.0.0`

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/redis.md#options)

- [`cachePrefixes`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/redis.md#cacheprefixes)

*Type: `(string)[]`*

Define cache prefixes for cache keys that should be captured as a cache span. Setting this to, for example, `['user:']` will capture cache keys that start with `user:`.

