---
title: 'NodeFetch | Sentry for Next.js'
description: 'This integration only works in the Node.js and Bun runtimes.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodefetch

# NodeFetch | Sentry for Next.js

This integration only works in the Node.js and Bun runtimes.

*Import name: `Sentry.nativeNodeFetchIntegration`*

This integration is enabled by default starting in v8.0.0. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nuxt/configuration/integrations.md#modifying-default-integrations).

The `nativeNodeFetchIntegration` does two things:

1. It captures spans for fetch requests.
2. It captures breadcrumbs for fetch requests.

```JavaScript
Sentry.init({
  integrations: [Sentry.nativeNodeFetchIntegration()],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nuxt/configuration/integrations/nodefetch.md#options)

- [`breadcrumbs`](https://docs.sentry.io/platforms/javascript/guides/nuxt/configuration/integrations/nodefetch.md#breadcrumbs)

*Type: `boolean`*

If set to false, no breadcrumbs will be captured.

- [`ignoreOutgoingRequests`](https://docs.sentry.io/platforms/javascript/guides/nuxt/configuration/integrations/nodefetch.md#ignoreoutgoingrequests)

*Type: `(url: string) => boolean`*

Allows you to define a method to filter out outgoing requests based on the URL. If the method returns `true`, the request will be ignored.

- [`spans`](https://docs.sentry.io/platforms/javascript/guides/nuxt/configuration/integrations/nodefetch.md#spans)

*Type: `boolean`*

If set to false, no spans will be captured.

- [`requestHook`](https://docs.sentry.io/platforms/javascript/guides/nuxt/configuration/integrations/nodefetch.md#requesthook)

*Type: `(span: Span, request: Request) => void`*

A callback function that allows you to add custom attributes or modify the span for outgoing fetch requests. The function is called with the span and the native fetch `Request` object.

- [`responseHook`](https://docs.sentry.io/platforms/javascript/guides/nuxt/configuration/integrations/nodefetch.md#responsehook)

*Type: `(span: Span, response: Response) => void`*

A callback function that allows you to add custom attributes or modify the span based on the response of outgoing fetch requests. The function is called with the span and the native fetch `Response` object.

