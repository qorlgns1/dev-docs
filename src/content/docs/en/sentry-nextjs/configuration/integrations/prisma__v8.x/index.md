---
title: 'Prisma | Sentry for Next.js'
description: 'This integration only works in the Node.js and Bun runtimes.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma__v8.x

# Prisma | Sentry for Next.js

This integration only works in the Node.js and Bun runtimes.

*Import name: `Sentry.prismaIntegration`*

Sentry supports tracing [Prisma ORM](https://www.prisma.io/) queries with the Prisma integration.

The Prisma Integrations creates a spans for each query and reports to Sentry with relevant details inside `description` if available.

## [Prisma Version 6](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma__v8.x/#prisma-version-6)

The Sentry Prisma Integration comes with Prisma version 5 support by default. For Prisma version 6 compatibility we need to pass a specific version of the Prisma instrumentation to the Sentry Prisma integration.

To use the integration with Prisma version 6, first install the `@prisma/instrumentation` package on version 6 (ideally the exact same version as your `prisma` and `@prisma/client` packages).

Then, add the `prismaIntegration` to your Sentry initialization as follows:

```javascript
import { PrismaInstrumentation } from "@prisma/instrumentation";

Sentry.init({
  tracesSampleRate: 1.0,
  integrations: [

    Sentry.prismaIntegration({
      // Override the default instrumentation that Sentry uses
      prismaInstrumentation: new PrismaInstrumentation(),
    }),

  ],
});
```

## [Prisma Version 5](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma__v8.x/#prisma-version-5)

To configure the integration for Prisma version 5, first add the `tracing` feature flag to the `generator` block of your Prisma schema:

`schema.prisma`

```txt
generator client {
  provider        = "prisma-client-js"

  previewFeatures = ["tracing"]

}
```

Then, add the `prismaIntegration` to your Sentry initialization as follows:

```javascript
Sentry.init({
  tracesSampleRate: 1.0,

  integrations: [Sentry.prismaIntegration()],

});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma__v8.x/#options)

- [`prismaInstrumentation`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma__v8.x/#prismainstrumentation)

*Type: `Instrumentation`* (An OpenTelemetry type)

Overrides the instrumentation used by the Sentry SDK with the passed in instrumentation instance.

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma__v8.x/#supported-versions)

* `prisma`: `>=5`

