---
title: 'MySQL | Sentry for Next.js'
description: 'This integration only works in the Node.js and Bun runtimes.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mysql

# MySQL | Sentry for Next.js

This integration only works in the Node.js and Bun runtimes.

*Import name: `Sentry.mysqlIntegration`*

This integration is enabled by default when performance monitoring is enabled. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

The `mysqlIntegration` adds instrumentation for the `mysql` library to capture spans using [`@opentelemetry/instrumentation-mysql`](https://www.npmjs.com/package/@opentelemetry/instrumentation-mysql).

```JavaScript
Sentry.init({
  integrations: [Sentry.mysqlIntegration()],
});
```

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mysql.md#supported-versions)

* `mysql`: `2.x`

