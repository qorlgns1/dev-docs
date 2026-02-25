---
title: 'Breadcrumbs | Sentry for Next.js'
description: 'This integration captures console logs as breadcrumbs (great for error context!). But if you need to search and query your logs across your entire app...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs

# Breadcrumbs | Sentry for Next.js

##### Did you mean logs instead?

This integration captures console logs as breadcrumbs (great for error context!). But if you need to search and query your logs across your entire application, use [Sentry Logs](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md) instead. Set `enableLogs: true`, and add the [Sentry console logging integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#integrations) in your SDK config.

This integration only works inside a browser environment.

*Import name: `Sentry.breadcrumbsIntegration`*

This integration is enabled by default. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

The `breadcrumbsIntegration` wraps native APIs to capture breadcrumbs.

By default, the Sentry SDK wraps the `console`, `dom`, `fetch`, `history`, and `xhr` browser APIs to add breadcrumbs. You can opt out of capturing breadcrumbs for specific parts of your application (for example, you could say don't capture `console.log` calls as breadcrumbs) via the options below.

```JavaScript
Sentry.init({
  integrations: [
    Sentry.breadcrumbsIntegration({
      console: true,
      dom: true,
      fetch: true,
      history: true,
      xhr: true,
    }),
  ],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md#options)

- [`console`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md#console)

*Type: `boolean`*

Log calls to `console.log`, `console.debug`, and so on.

- [`dom`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md#dom)

*Type: `boolean` | `{ serializeAttribute: string | string[] }`*

Log all click and keypress events.

When an object with a `serializeAttribute` key is provided, the Breadcrumbs integration will look for given attribute(s) in DOM elements while generating the breadcrumb trails. Matched elements will be followed by their custom attributes, instead of their `id`s or `class` names.

- [`fetch`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md#fetch)

*Type: `boolean`*

Log HTTP requests done with the Fetch API.

- [`history`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md#history)

*Type: `boolean`*

Log calls to `history.pushState` and related APIs.

- [`sentry`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md#sentry)

*Type: `boolean`*

Log whenever we send an event to the server.

- [`xhr`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md#xhr)

*Type: `boolean`*

Log HTTP requests done with the XHR API.

