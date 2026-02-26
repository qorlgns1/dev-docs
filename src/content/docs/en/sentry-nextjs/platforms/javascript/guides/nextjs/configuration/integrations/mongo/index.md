---
title: 'MongoDB | Sentry for Next.js'
description: 'This integration only works in the Node.js and Bun runtimes.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mongo

# MongoDB | Sentry for Next.js

This integration only works in the Node.js and Bun runtimes.

*Import name: `Sentry.mongoIntegration`*

This integration is enabled by default when performance monitoring is enabled. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

The `mongoIntegration` adds instrumentation for the `mongodb` library to capture spans using [`@opentelemetry/instrumentation-mongodb`](https://www.npmjs.com/package/@opentelemetry/instrumentation-mongodb).

```JavaScript
Sentry.init({
  integrations: [Sentry.mongoIntegration()],
});
```

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mongo.md#supported-versions)

* `mongodb`: `>=3.3 <7`

