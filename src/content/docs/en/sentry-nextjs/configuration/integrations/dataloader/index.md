---
title: 'Dataloader | Sentry for Next.js'
description: 'This integration only works in the Node.js and Bun runtimes. Requires SDK version  or higher.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/dataloader

# Dataloader | Sentry for Next.js

This integration only works in the Node.js and Bun runtimes. Requires SDK version `8.31.0` or higher.

*Import name: `Sentry.dataloaderIntegration`*

The `dataloaderIntegration` adds instrumentation for the `dataloader` library to capture spans using [`@opentelemetry/instrumentation-dataloader`](https://www.npmjs.com/package/@opentelemetry/instrumentation-dataloader).

```javascript
Sentry.init({
  integrations: [Sentry.dataloaderIntegration()],
});
```

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/dataloader.md#supported-versions)

* `dataloader`: `>=2.0.0 <3`

