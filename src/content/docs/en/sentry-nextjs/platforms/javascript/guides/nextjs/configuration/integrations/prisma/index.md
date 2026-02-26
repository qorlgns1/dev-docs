---
title: 'Prisma | Sentry for Next.js'
description: 'This integration only works in the Node.js and Bun runtimes.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma

# Prisma | Sentry for Next.js

This integration only works in the Node.js and Bun runtimes.

*Import name: `Sentry.prismaIntegration`*

Sentry supports tracing [Prisma ORM](https://www.prisma.io/) queries with the Prisma integration.

The Prisma Integrations creates a spans for each query and reports to Sentry with relevant details inside the`description` if available.

This integration is enabled by default and supports Prisma versions 5, 6 & 7. In Prisma v5, you need to follow the instructions below to enable tracing.

If you'd like to learn how to modify your default integrations, visit the docs on [Modifying Default Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

## [Prisma Version 6 & 7](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma.md#prisma-version-6--7)

To use the integration with Prisma version 6 or 7, no configuration is required - tracing is enabled by default.

```javascript
Sentry.init({
  tracesSampleRate: 1.0,

  integrations: [Sentry.prismaIntegration()],

});
```

## [Prisma Version 5](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma.md#prisma-version-5)

To configure the integration for Prisma version 5, first add the `tracing` feature flag to the `generator` block of your Prisma schema:

`schema.prisma`

```txt
generator client {
  provider        = "prisma-client-js"

  previewFeatures = ["tracing"]

}
```

Then, the `prismaIntegration` will automatically capture spans for Prisma queries.

```javascript
Sentry.init({
  tracesSampleRate: 1.0,

  integrations: [Sentry.prismaIntegration()],

});
```

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma.md#supported-versions)

* `prisma`: `5.x`, `6.x`, `7.x`

## [Learn More](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma.md#learn-more)

For details on the span structure that Prisma's OpenTelemetry tracing produces (e.g., `prisma:client:operation`, `prisma:engine:db_query`), see the [Prisma trace output documentation](https://www.prisma.io/docs/orm/prisma-client/observability-and-logging/opentelemetry-tracing#trace-output).

