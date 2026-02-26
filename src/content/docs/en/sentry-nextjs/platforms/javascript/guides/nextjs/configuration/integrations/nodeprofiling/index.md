---
title: 'NodeProfiling | Sentry for Next.js'
description: 'This integration only works in the Node.js runtime.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodeprofiling

# NodeProfiling | Sentry for Next.js

This integration only works in the Node.js runtime.

`nodeProfilingIntegration` must be imported from the `@sentry/profiling-node` package.

[Profiling](https://docs.sentry.io/product/explore/profiling.md) offers a deeper level of visibility on top of traditional tracing, removing the need for custom instrumentation and enabling precise code-level visibility into your application in a production environment.

The NodeProfiling integration sets up automatic performance profiling for your Node.js applications. It captures profiles via v8 and sends them to Sentry. To use this integration, you also need to have the performance monitoring enabled.

Read more about [setting up NodeProfiling](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling.md).

```JavaScript
const Sentry = require("@sentry/node");
const { nodeProfilingIntegration } = require("@sentry/profiling-node");

Sentry.init({
  integrations: [nodeProfilingIntegration()],
});
```

