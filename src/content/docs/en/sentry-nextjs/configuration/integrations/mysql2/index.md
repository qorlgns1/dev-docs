---
title: 'MySQL2 | Sentry for Next.js'
description: 'This integration only works in the Node.js and Bun runtimes.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mysql2

# MySQL2 | Sentry for Next.js

This integration only works in the Node.js and Bun runtimes.

*Import name: `Sentry.mysql2Integration`*

This integration is enabled by default when performance monitoring is enabled. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

The `mysql2Integration` adds instrumentation for the `mysql2` library to capture spans using [`@opentelemetry/instrumentation-mysql2`](https://www.npmjs.com/package/@opentelemetry/instrumentation-mysql2).

```JavaScript
Sentry.init({
  integrations: [Sentry.mysql2Integration()],
});
```

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mysql2.md#supported-versions)

* `mysql2`: `>= 1.4.2, < 4.0`

