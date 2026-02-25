---
title: 'Instrument HTTP Requests | Sentry for Next.js'
description: "As a prerequisite to setting up Requests, you'll need to first set up tracing. Once this is done, the JavaScript SDK will automatically instrument out..."
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/requests-module

# Instrument HTTP Requests | Sentry for Next.js

As a prerequisite to setting up [Requests](https://docs.sentry.io/product/insights/requests.md), you'll need to first [set up tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md). Once this is done, the JavaScript SDK will automatically instrument outgoing HTTP requests. If that doesn't fit your use case, follow this guide to manually instrument your requests.

For detailed information about which data can be set, see the [Requests Module developer specifications](https://develop.sentry.dev/sdk/performance/modules/requests/).

## [Wrap HTTP Requests in a Span](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/requests-module.md#wrap-http-requests-in-a-span)

Refer to [HTTP Span Data Conventions](https://develop.sentry.dev/sdk/performance/span-data-conventions/#http) for a full list of the span data attributes.

Here is an example of an instrumented function that makes HTTP requests:

`my-request.js`

```javascript
async function makeRequest(method, url) {
  return await Sentry.startSpan(
    { op: "http.client", name: `${method} ${url}` },
    async (span) => {
      const parsedURL = new URL(url, location.origin);

      span.setAttribute("http.request.method", method);

      span.setAttribute("server.address", parsedURL.hostname);
      span.setAttribute("server.port", parsedURL.port || undefined);

      const response = await fetch(url, {
        method,
      });

      span.setAttribute("http.response.status_code", response.status);
      span.setAttribute(
        "http.response_content_length",
        Number(response.headers.get("content-length")),
      );

      // A good place to set other span attributes

      return response;
    },
  );
}
```

