---
title: 'Amqplib | Sentry for Next.js'
description: 'This integration only works in the Node.js and Bun runtimes. Requires SDK version  or higher.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/amqplib

# Amqplib | Sentry for Next.js

This integration only works in the Node.js and Bun runtimes. Requires SDK version `8.32.0` or higher.

*Import name: `Sentry.amqplibIntegration`*

This integration is enabled by default when performance monitoring is enabled. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

The `amqplibIntegration` adds instrumentation for the `amqplib` library to capture spans using [`@opentelemetry/instrumentation-amqplib`](https://www.npmjs.com/package/@opentelemetry/instrumentation-amqplib).

```JavaScript
Sentry.init({
  integrations: [Sentry.amqplibIntegration()],
});
```

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/amqplib.md#supported-versions)

* `amqplib`: `>=0.5.5 <1`

