---
title: 'BrowserSession | Sentry for Next.js'
description: 'This integration only works inside a browser environment.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsersession

# BrowserSession | Sentry for Next.js

This integration only works inside a browser environment.

*Import name: `Sentry.browserSessionIntegration`*

Sentry's [Release Health](https://docs.sentry.io/product/releases/health.md) feature allows you to track user adoption and your application's crash-free rate. When the BrowserSession integration is enabled, it automatically creates a session each time a user loads your page or application. These sessions are used to track your release health. If an error is captured during an active session, the session will be flagged as faulty. Read more about [Sessions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/releases.md#sessions).

```JavaScript
Sentry.init({
  integrations: [Sentry.browserSessionIntegration()],
});
```

## [Configuration Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsersession.md#configuration-options)

- [lifecycle](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsersession.md#lifecycle)

| Available since | `10.39.0`           |
| --------------- | ------------------- |
| Type            | `'route' \| 'page'` |
| Default         | `'route'`           |

Controls how long one session lasts and when a new session is started.

* `'route'`: A new session is started when the route changes, based on the [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API). This is the default behavior. If you're building a single-page application (SPA), this will result in one session being created per soft navigation.
* `'page'`: A new session is started when the page changes on a hard page reload or navigation. This is useful if you're building a single-page application (SPA) and want to track one session across multiple routes as users navigate through your application.

