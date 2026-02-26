---
title: 'LRU Memoizer | Sentry for Next.js'
description: 'This integration only works in the Node.js and Bun runtimes. Requires SDK version  or higher.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/lrumemoizer

# LRU Memoizer | Sentry for Next.js

This integration only works in the Node.js and Bun runtimes. Requires SDK version `8.33.0` or higher.

*Import name: `Sentry.lruMemoizerIntegration`*

This integration is enabled by default when performance monitoring is enabled. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

The `lruMemoizerIntegration` adds instrumentation for the `lru-memoizer` library to capture spans using [`@opentelemetry/instrumentation-lru-memoizer`](https://www.npmjs.com/package/@opentelemetry/instrumentation-lru-memoizer).

```javascript
Sentry.init({
  integrations: [Sentry.lruMemoizerIntegration()],
});
```

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/lrumemoizer.md#supported-versions)

* `lru-memoizer`: `>=1.3.0 <3`

