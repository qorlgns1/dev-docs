---
title: 'Http | Sentry for Next.js'
description: 'This integration only works inside server environments (Node.js, Bun, Deno).'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http

# Http | Sentry for Next.js

This integration only works inside server environments (Node.js, Bun, Deno).

*Import name: `Sentry.httpIntegration`*

This integration is enabled by default. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

The `httpIntegration` does two things:

1. It captures breadcrumbs for HTTP requests.
2. It captures spans for outgoing HTTP requests.

```JavaScript
Sentry.init({
  integrations: [Sentry.httpIntegration()],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#options)

- [`breadcrumbs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#breadcrumbs)

*Type: `boolean`* (Defaults to `true`)

If set to false, no breadcrumbs will be captured.

- [`spans`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#spans)

*Type: `boolean`* (Defaults to `false`)

If set to true, spans will be created for outgoing HTTP requests.

- [`maxIncomingRequestBodySize`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#maxincomingrequestbodysize)

*Type: `'none' | 'small' | 'medium' | 'always'`* (Defaults to `'medium'`)

Controls the maximum size of incoming HTTP request bodies attached to events.

Available options:

* 'none': No request bodies will be attached
* 'small': Request bodies up to 1,000 bytes will be attached
* 'medium': Request bodies up to 10,000 bytes will be attached (default)
* 'always': Request bodies will always be attached

Note that even with the `'always'` setting, bodies exceeding 1 MB will never be attached for performance and security reasons.

- [`ignoreIncomingRequestBody`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#ignoreincomingrequestbody)

*Type: `(url: string, request: RequestOptions) => boolean`*

Allows you to ignore the request body for incoming HTTP requests to URLs where the given callback returns `true`. This can be useful for long running requests where the body is not needed and we want to avoid capturing it.

The callback function receives two arguments:

* `url`: The full URL of the incoming request, including the protocol, host, port, path and query string. For example: `https://example.com/users?name=John`.
* `request`: An object of type `RequestOptions` containing the incoming request's options. You can use this to filter on properties like the request method or headers.

- [`ignoreOutgoingRequests`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#ignoreoutgoingrequests)

*Type: `(url: string, request: RequestOptions) => boolean`*

Allows you to define a method to filter out outgoing requests based on the URL. If the method returns `true`, no spans or breadcrumbs will be captured for the outgoing request.

The callback function receives two arguments:

* `url`: The full URL of the outgoing request, including the protocol, host, port, path and query string. For example: `https://example.com/users?name=John`.
* `request`: An object of type `RequestOptions` containing the outgoing request's options. You can use this to filter on properties like the request method or headers.

- [`ignoreIncomingRequests`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#ignoreincomingrequests)

*Type: `(urlPath: string, request: IncomingMessage) => boolean`*

Allows you to define a method to filter out incoming requests based on the URL. If the method returns `true`, no span or transaction will be captured for the incoming request.

The callback function receives two arguments:

* `urlPath`: The URL path of the incoming request, including the query string if available. For example: `/users?name=John`.
* `request`: An object of type `IncomingMessage` containing the incoming request. You can use this to filter on properties like the request method or headers.

- [`ignoreStaticAssets`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#ignorestaticassets)

*Type: `boolean`* (Defaults to `true`)

If set to true, no spans will be captured for static assets like images, fonts, and other files.

- [`disableIncomingRequestSpans`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#disableincomingrequestspans)

*Type: `boolean`*

If set to true, no spans will be generated for incoming requests.

- [`dropSpansForIncomingRequestStatusCodes`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#dropspansforincomingrequeststatuscodes)

*Type: `(number | [number, number])[]`* (Defaults to `[[401, 404], [301, 303], [305, 399]]`)

Do not capture spans for incoming HTTP requests with the given status codes. By default, spans with some 3xx and 4xx status codes are ignored. Expects an array that can contain individual status codes (numbers) or ranges (2-element arrays of `[start, end]` where both start and end are inclusive).

For example, `[[300, 399], 404]` would ignore all 3xx status codes (300-399 inclusive) and 404 status codes.

- [`trackIncomingRequestsAsSessions`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#trackincomingrequestsassessions)

*Type: `boolean`* (Defaults to `true`)

Determines whether the integration should create [Sessions](https://docs.sentry.io/product/releases/health.md#sessions) for incoming requests to track the health and crash-free rate of your releases in Sentry. Read more about [Release Health](https://docs.sentry.io/product/releases/health.md).

- [`sessionFlushingDelayMS`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#sessionflushingdelayms)

*Type: `number`* (Defaults to `60000`)

The delay in milliseconds before sessions are flushed as a session aggregate. This controls how frequently session data is sent to Sentry.

- [`instrumentation`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#instrumentation)

You can also pass some hooks through to the [underlying OpenTelemetry Instrumentation](https://www.npmjs.com/package/@opentelemetry/instrumentation-http):

```typescript
httpIntegration({
  instrumentation?: {
    requestHook?: (span: Span, req: ClientRequest | HTTPModuleRequestIncomingMessage) => void;
    responseHook?: (span: Span, response: HTTPModuleRequestIncomingMessage | ServerResponse) => void;
    applyCustomAttributesOnSpan?: (
      span: Span,
      request: ClientRequest | HTTPModuleRequestIncomingMessage,
      response: HTTPModuleRequestIncomingMessage | ServerResponse,
    ) => void;
});
```

