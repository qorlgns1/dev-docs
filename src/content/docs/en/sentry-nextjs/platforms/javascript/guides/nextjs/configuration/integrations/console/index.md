---
title: 'Console | Sentry for Next.js'
description: 'This integration captures console logs as breadcrumbs (great for error context!). But if you need to search and query your logs across your entire app...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/console

# Console | Sentry for Next.js

##### Did you mean logs instead?

This integration captures console logs as breadcrumbs (great for error context!). But if you need to search and query your logs across your entire application, use [Sentry Logs](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md) instead. Set `enableLogs: true`, and add the [Sentry console logging integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#integrations) in your SDK config.

*Import name: `Sentry.consoleIntegration`*

This integration is enabled by default. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/express/configuration/integrations.md#modifying-default-integrations).

The `consoleIntegration` generates breadcrumbs for console logs.

```JavaScript
Sentry.init({
  integrations: [Sentry.consoleIntegration()],
});
```

