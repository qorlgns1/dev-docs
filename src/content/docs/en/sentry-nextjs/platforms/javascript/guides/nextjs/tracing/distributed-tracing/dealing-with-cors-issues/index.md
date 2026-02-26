---
title: 'Dealing with CORS Issues | Sentry for Next.js'
description: 'If your frontend and backend are hosted on different domains (for example, your frontend is on  and your backend is on ), you need to configure your b...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/dealing-with-cors-issues

# Dealing with CORS Issues | Sentry for Next.js

If your frontend and backend are hosted on different domains (for example, your frontend is on `https://example.com` and your backend is on `https://api.example.com`), you need to configure your backend [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Headers) headers to prevent requests from being blocked by the browser.

## [Understanding Trace Propagation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/dealing-with-cors-issues.md#understanding-trace-propagation)

Sentry doesn't attach the `sentry-trace` and `baggage` (and optionally `traceparent`) headers to every outgoing request. Instead, it only attaches these headers to requests whose URLs match the patterns specified in the `tracePropagationTargets` configuration option.

By default, `tracePropagationTargets` is set to `['localhost', /^\//]`, which means trace headers are only attached to:

* Requests containing `localhost` in their URL (e.g., `http://localhost:3000/api`)
* Requests whose URL starts with `/` (e.g., `/api/users`, `/graphql`)

This default behavior helps prevent sending trace data to third-party services and avoids potential CORS issues.

## [Configuring Trace Propagation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/dealing-with-cors-issues.md#configuring-trace-propagation)

To enable distributed tracing across different domains, you need to configure `tracePropagationTargets` to include the URLs of your backend services:

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.browserTracingIntegration()],
  tracePropagationTargets: [
    "localhost", // For local development
    /^\/api\//, // For same-origin API calls
    "https://api.example.com", // For your backend domain
    "https://auth.example.com", // For additional services
  ],
});
```

## [Configuring CORS Headers](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/dealing-with-cors-issues.md#configuring-cors-headers)

Once you've configured `tracePropagationTargets` to include your backend domains, you need to configure your backend to allow the trace headers:

```bash
Access-Control-Allow-Headers: sentry-trace, baggage
```

Your server's exact configuration will depend on your setup, but the important part is allowing both the `sentry-trace` and `baggage` headers.

- [W3C traceparent header](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/dealing-with-cors-issues.md#w3c-traceparent-header)

If you set [`propagateTraceparent` option](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#propagateTraceparent) to `true`, you also need to allow the `traceparent` header:

```bash
Access-Control-Allow-Headers: sentry-trace, baggage, traceparent
```

## [Disabling Trace Propagation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/dealing-with-cors-issues.md#disabling-trace-propagation)

If you want to disable distributed tracing entirely and ensure no trace headers are sent:

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  // Empty array prevents all trace header propagation
  tracePropagationTargets: [],
});
```

