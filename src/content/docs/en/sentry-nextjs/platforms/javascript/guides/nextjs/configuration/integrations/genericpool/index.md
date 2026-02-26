---
title: 'Generic Pool | Sentry for Next.js'
description: 'This integration only works in the Node.js and Bun runtimes. Requires SDK version  or higher.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/genericpool

# Generic Pool | Sentry for Next.js

This integration only works in the Node.js and Bun runtimes. Requires SDK version `8.29.0` or higher.

*Import name: `Sentry.genericPoolIntegration`*

This integration is enabled by default when performance monitoring is enabled. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

The `genericPoolIntegration` adds instrumentation for the `generic-pool` library to capture spans using [`@opentelemetry/instrumentation-generic-pool`](https://www.npmjs.com/package/@opentelemetry/instrumentation-generic-pool).

```JavaScript
Sentry.init({
  integrations: [Sentry.genericPoolIntegration()],
});
```

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/genericpool.md#supported-versions)

* `generic-pool`: `>=2.0.0 <4`

