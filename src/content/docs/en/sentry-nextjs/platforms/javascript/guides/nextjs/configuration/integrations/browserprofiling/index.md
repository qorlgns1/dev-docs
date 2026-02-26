---
title: 'BrowserProfiling | Sentry for Next.js'
description: 'This integration only works inside a browser environment.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserprofiling

# BrowserProfiling | Sentry for Next.js

This integration only works inside a browser environment.

*Import name: `Sentry.browserProfilingIntegration`*

[Profiling](https://docs.sentry.io/product/explore/profiling.md) offers a deeper level of visibility on top of traditional tracing, removing the need for custom instrumentation and enabling precise code-level visibility into your application in a production environment.

The BrowserProfiling integration sets up automatic performance profiling for your frontend applications. It captures profiles via the [JS Self-Profiling API](https://wicg.github.io/js-self-profiling/) from the browser and sends them to Sentry. To use this integration, you also need to have the [BrowserTracing integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsertracing.md) enabled.

Read more about [setting up BrowserProfiling](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling.md).

```JavaScript
Sentry.init({
  integrations: [Sentry.browserProfilingIntegration()],
});
```

