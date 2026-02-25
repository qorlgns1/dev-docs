---
title: 'GlobalHandlers | Sentry for Next.js'
description: 'This integration only works in the Browser and Deno runtimes.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/globalhandlers

# GlobalHandlers | Sentry for Next.js

This integration only works in the Browser and Deno runtimes.

*Import name: `Sentry.globalHandlersIntegration`*

This integration is enabled by default. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

This integration attaches global handlers to capture uncaught exceptions and unhandled rejections. It captures errors and unhandled promise rejections by default.

```JavaScript
Sentry.init({
  integrations: [Sentry.globalHandlersIntegration({ onerror: true, onunhandledrejection: true })],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/globalhandlers.md#options)

- [`onerror`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/globalhandlers.md#onerror)

*Type: `boolean`*

Capture errors bubbled to `onerror`.

- [`onunhandledrejection`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/globalhandlers.md#onunhandledrejection)

*Type: `boolean`*

Capture unhandled promise rejections.

