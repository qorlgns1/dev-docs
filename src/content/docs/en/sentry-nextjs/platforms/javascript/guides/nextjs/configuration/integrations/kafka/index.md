---
title: 'Kafka | Sentry for Next.js'
description: 'This integration only works in the Node.js and Bun runtimes. Requires SDK version  or higher.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/kafka

# Kafka | Sentry for Next.js

This integration only works in the Node.js and Bun runtimes. Requires SDK version `8.30.0` or higher.

*Import name: `Sentry.kafkaIntegration`*

This integration is enabled by default when performance monitoring is enabled. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

The `kafkaIntegration` adds instrumentation for the `kafkajs` library to capture spans using [`@opentelemetry/instrumentation-kafkajs`](https://www.npmjs.com/package/@opentelemetry/instrumentation-kafkajs).

```JavaScript
Sentry.init({
  integrations: [Sentry.kafkaIntegration()],
});
```

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/kafka.md#supported-versions)

* `kafkajs`: `>=0.1.0 <3`

