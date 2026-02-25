---
title: 'Context | Sentry for Next.js'
description: 'This integration only works in the Node.js runtime.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodecontext

# Context | Sentry for Next.js

This integration only works in the Node.js runtime.

*Import name: `Sentry.nodeContextIntegration`*

This integration is enabled by default. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

The `nodeContextIntegration` captures context about the environment and the device that the SDK is running on, and attaches this information to events.

```JavaScript
Sentry.init({
  integrations: [Sentry.nodeContextIntegration()],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodecontext.md#options)

- [`app`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodecontext.md#app)

*Type: `boolean`*

If set to false, no app context will be captured.

- [`os`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodecontext.md#os)

*Type: `boolean`*

If set to false, no OS context will be captured.

- [`device`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodecontext.md#device)

*Type: `boolean | { cpu?: boolean; memory?: boolean; }`*

If set to false, no device context will be captured.

- [`culture`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodecontext.md#culture)

*Type: `boolean`*

If set to false, no culture context will be captured.

- [`cloudResource`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodecontext.md#cloudresource)

*Type: `boolean`*

If set to false, no cloud resource context will be captured.

