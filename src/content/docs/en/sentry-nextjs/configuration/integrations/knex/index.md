---
title: 'Knex | Sentry for Next.js'
description: 'This integration only works in the Node.js and Bun runtimes. Requires SDK version  or higher.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/knex

# Knex | Sentry for Next.js

This integration only works in the Node.js and Bun runtimes. Requires SDK version `8.38.0` or higher.

*Import name: `Sentry.knexIntegration`*

The `knexIntegration` adds instrumentation for the `knex` library to capture spans using [`@opentelemetry/instrumentation-knex`](https://www.npmjs.com/package/@opentelemetry/instrumentation-knex).

```javascript
Sentry.init({
  integrations: [Sentry.knexIntegration()],
});
```

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/knex.md#supported-versions)

* `dataloader`: `>=0.10.0 <4`

