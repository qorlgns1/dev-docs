---
title: 'BrowserTracing | Sentry for Next.js'
description: 'This integration only works inside a browser environment.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsertracing

# BrowserTracing | Sentry for Next.js

This integration only works inside a browser environment.

*Import name: `Sentry.browserTracingIntegration`*

With [tracing](https://docs.sentry.io/product/insights/overview.md), Sentry tracks your software performance, measuring metrics like throughput and latency, and displaying the impact of errors across multiple systems. Sentry captures distributed traces consisting of transactions and spans, which measure individual services and individual operations within those services.

The BrowserTracing integration sets up automatic tracing for your frontend applications. It captures transactions and spans from the browser and sends them to Sentry.

Read more about [setting up BrowserTracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md).

```JavaScript
Sentry.init({
  integrations: [Sentry.browserTracingIntegration()],
});
```

See [Configuration Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#configuration-options) for a full list of available options for `browserTracingIntegration`

