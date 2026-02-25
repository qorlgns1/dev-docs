---
title: 'Anr | Sentry for Next.js'
description: 'This integration only works in the Node.js runtime.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anr

# Anr | Sentry for Next.js

**Deprecated**: This integration is deprecated. Please use the [`eventLoopBlockIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anr/event-loop-block.md) instead for better performance and more comprehensive monitoring.

This integration only works in the Node.js runtime.

*Import name: `Sentry.anrIntegration`*

The `anrIntegration` captures Application Not Responding (ANR)/Event Loop Stall errors and reports them as Sentry events. For more details, see the documentation on [Event Loop Block Detection](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/event-loop-block.md).

```JavaScript
Sentry.init({
  integrations: [Sentry.anrIntegration({ captureStackTrace: true })],
});
```

