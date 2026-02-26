---
title: 'Modules | Sentry for Next.js'
description: 'This integration only works inside server environments (Node.js, Bun, Deno).'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/modules

# Modules | Sentry for Next.js

This integration only works inside server environments (Node.js, Bun, Deno).

*Import name: `Sentry.modulesIntegration`*

This integration is enabled by default. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

The `modulesIntegration` captures information about the installed node modules/packages to the event.

```JavaScript
Sentry.init({
  integrations: [Sentry.modulesIntegration()],
});
```

