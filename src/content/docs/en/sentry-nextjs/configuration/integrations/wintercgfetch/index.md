---
title: 'WinterCGFetch | Sentry for Next.js'
description: 'This integration only works in the Edge runtime.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/wintercgfetch

# WinterCGFetch | Sentry for Next.js

This integration only works in the Edge runtime.

*Import name: `Sentry.winterCGFetchIntegration`*

This integration is enabled by default. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

The `winterCGFetchIntegration` creates spans and attaches tracing headers to fetch requests on the Edge runtime.

```JavaScript
Sentry.init({
  integrations: [Sentry.winterCGFetchIntegration()],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/wintercgfetch.md#options)

- [`breadcrumbs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/wintercgfetch.md#breadcrumbs)

*Type: `boolean`*

If set to false, no breadcrumbs will be captured.

- [`shouldCreateSpanForRequest`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/wintercgfetch.md#shouldcreatespanforrequest)

*Type: `(url: string) => boolean`*

Allows you to define a method to determine whether or not to create spans to track outgoing requests to the given URL. By default, spans will be created for all outgoing requests.

