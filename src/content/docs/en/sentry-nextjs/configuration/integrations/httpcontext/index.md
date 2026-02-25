---
title: 'HttpContext | Sentry for Next.js'
description: 'This integration only works inside a browser environment.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpcontext

# HttpContext | Sentry for Next.js

This integration only works inside a browser environment.

*Import name: `Sentry.httpContextIntegration`*

This integration is enabled by default. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

This integration attaches HTTP request information, such as URL, user-agent, referrer, and other headers, to the event. It allows us to correctly catalog and tag events with specific OS, browser, and version information.

```JavaScript
Sentry.init({
  integrations: [Sentry.httpContextIntegration()],
});
```

