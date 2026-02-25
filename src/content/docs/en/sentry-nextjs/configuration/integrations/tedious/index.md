---
title: 'Tedious | Sentry for Next.js'
description: 'This integration only works in the Node.js and Bun runtimes. Requires SDK version  or higher.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/tedious

# Tedious | Sentry for Next.js

This integration only works in the Node.js and Bun runtimes. Requires SDK version `8.38.0` or higher.

*Import name: `Sentry.tediousIntegration`*

This integration is enabled by default when performance monitoring is enabled. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

The `tediousIntegration` adds instrumentation for the `tedious` library to capture spans using [`@opentelemetry/instrumentation-tedious`](https://www.npmjs.com/package/@opentelemetry/instrumentation-tedious).

```javascript
Sentry.init({
  integrations: [Sentry.tediousIntegration()],
});
```

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/tedious.md#supported-versions)

* `tedious`: `>=1.11.0 <20`

