---
title: 'Mongoose | Sentry for Next.js'
description: 'This integration only works in the Node.js and Bun runtimes.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mongoose

# Mongoose | Sentry for Next.js

This integration only works in the Node.js and Bun runtimes.

*Import name: `Sentry.mongooseIntegration`*

This integration is enabled by default when performance monitoring is enabled. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

The `mongooseIntegration` adds instrumentation for the `mongoose` library to capture spans using [`@opentelemetry/instrumentation-mongoose`](https://www.npmjs.com/package/@opentelemetry/instrumentation-mongoose).

```JavaScript
Sentry.init({
  integrations: [Sentry.mongooseIntegration()],
});
```

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mongoose.md#supported-versions)

* `mongoose`: `>=5.9.7 <9`

