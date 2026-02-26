---
title: 'Postgres | Sentry for Next.js'
description: 'This integration only works in the Node.js and Bun runtimes.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/postgres

# Postgres | Sentry for Next.js

This integration only works in the Node.js and Bun runtimes.

*Import name: `Sentry.postgresIntegration`*

This integration is enabled by default when performance monitoring is enabled. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

The `postgresIntegration` adds instrumentation for the `pg` library to capture spans using [`@opentelemetry/instrumentation-pg`](https://www.npmjs.com/package/@opentelemetry/instrumentation-pg).

```JavaScript
Sentry.init({
  integrations: [Sentry.postgresIntegration()],
});
```

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/postgres.md#supported-versions)

* `pg`: `>=8 <9`

