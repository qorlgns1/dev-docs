---
title: 'Set Up Distributed Tracing | Sentry for Next.js'
description: 'Distributed tracing connects and records the path of requests as they travel through the different tiers of your application architecture. If your arc...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing

# Set Up Distributed Tracing | Sentry for Next.js

Distributed tracing connects and records the path of requests as they travel through the different tiers of your application architecture. If your architecture consists of multiple services that live on different sub-domains (e.g. `fe.example.com` and `api.example.com`), distributed tracing will help you follow the path of events as they move from one service to another.

This end-to-end visibility allows developers to identify bottlenecks, pinpoint the root cause of errors, and understand component interactions—turning what would be a complex debugging nightmare into a manageable process that improves system reliability and performance.

## [Basic Example](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md#basic-example)

Here's an example showing a distributed trace in Sentry:

This distributed trace shows a Vue app's `pageload` making a request to a Python backend, which then calls the `/api` endpoint of a Ruby microservice.

What happens in the background is that Sentry uses reads and further propagates two HTTP headers between your applications:

* `sentry-trace`
* `baggage`

If you run any JavaScript applications in your distributed system, make sure that those two headers are added to your CORS allowlist and won't be blocked or stripped by your proxy servers, gateways, or firewalls.

## [How to Use Distributed Tracing?](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md#how-to-use-distributed-tracing)

If you're using the current version of our Next.js SDK, distributed tracing will work out of the box for the client, server, and edge runtimes.

Additional Configuration for App Router on Next.js 14

In order to enable distributed tracing for App Router on Next.js 14 you need to add or modify the `generateMetadata` function of your root layout:

`app/layout.tsx`

```typescript
import * as Sentry from "@sentry/nextjs";
import type { Metadata } from "next";

export function generateMetadata(): Metadata {
  return {
    // ... your existing metadata
    other: {
      ...Sentry.getTraceData(),
    },
  };
}
```

For client-side, when you are interacting with other external API systems, you might have to define `tracePropagationTargets` to get around possible [Browser CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) issues.

Note: port numbers are relevant for trace propagation and the origin. You may need to configure the `tracePropagationTargets` to ensure that traces are propagated across your services if they run on different ports.

For example, if you have a Node.js backend running locally on port 3000, that destination (`http://localhost:3000`) should be added to the `tracePropagationTargets` array on your frontend to ensure that CORS doesn't restrict the propagation of traces.

```javascript
// instrumentation-client.js
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.browserTracingIntegration()],
  tracePropagationTargets: ["https://myproject.org", /^\/api\//],
});
```

If you're using version `7.57.x` or below, you'll need to have our [tracing feature enabled](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md) in order for distributed tracing to work.

- [Trace Propagation Examples](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md#trace-propagation-examples)

#
- [Example 1: Microservices E-commerce Platform](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md#example-1-microservices-e-commerce-platform)

```javascript
// instrumentation-client.js
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.browserTracingIntegration()],
  tracePropagationTargets: [
    "https://api.myecommerce.com",
    "https://auth.myecommerce.com",
  ],
});
```

This tells Sentry to pass trace headers across the following paths:

* Your main API server (where product data comes from)
* Your authentication server (where logins happen)

This way, if a customer experiences an error during checkout, or you want to check the performance of a specific endpoint, you can see the complete path their request took across these different services.

#
- [Example 2: Mobile App with Backend Services](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md#example-2-mobile-app-with-backend-services)

```javascript
// instrumentation-client.js
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.browserTracingIntegration()],
  // Capture 100% of spans. This is useful for development and debugging. Consider reducing in production or using traceSampler
  tracesSampleRate: 1.0,
  tracePropagationTargets: [
    "https://api.myapp.com",
    "https://media.myapp.com",
    /^\/local-api\//,
  ],
});
```

This configuration lets your app track user actions across:

* Your main API server (handles most app functions)
* Your media server (handles images, videos, etc.)
* Any local API endpoints in your app

If your app crashes while a user is uploading a photo, you can trace exactly where the problem occurred - in the app itself, the main API, or the media service.

- [Strict Trace Continuation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md#strict-trace-continuation)

Available since: `v10`

\_

When your application receives requests, they might include `sentry-trace` and `baggage` headers from an upstream service that is also using Sentry. By default, the SDK will continue the trace from these incoming headers. However, this behavior can be undesirable if the requests are from a third-party service, as it can lead to unwanted traces, increased billing, and skewed performance data.

To prevent this, you can enable `strictTraceContinuation`. When this option is set to `true`, the SDK checks the incoming request for Sentry trace information and only continues the trace if it belongs to the same Sentry organization. Otherwise, it starts a new trace. This is useful if your application is a public API or receives requests from services outside your organization.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  tracesSampleRate: 1.0,
  // Ensure that only traces from your own organization are continued

  strictTraceContinuation: true,

});
```

The SDK automatically parses the organization ID from your DSN. If you use a DSN format that doesn't include the organization ID (number followed by the letter `"o"`), or if you need to override it, you can provide it manually using the `orgId` option:

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  tracesSampleRate: 1.0,
  strictTraceContinuation: true,
  // Manually provide your organization ID (overrides organization ID parsed from DSN)

  orgId: 12345,

});
```

- [Disabling Distributed Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md#disabling-distributed-tracing)

If you want to disable distributed tracing and ensure no Sentry trace headers are sent, you can configure your SDK like this:

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  // Overwrite the defaults to ensure no trace headers are sent
  tracePropagationTargets: [],
});
```

Remember that in order to propagate trace information through your whole distributed system, you have to use Sentry in all of the involved services and applications. Take a look at the respective SDK documentation to learn how distributed tracing can be enabled for each platform.

## [Trace Duration](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md#trace-duration)

In the browser, the SDK automatically starts a new trace in the following situations:

* On page load: Whenever the page is (re-)loaded, a new trace is started. At the same time, a `pageload` span is created (see [Performance Monitoring](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md)). Once this span ends, the trace remains until the next navigation or page load. In case the server serving the initial page already started a trace and sent the necessary [HTML tags](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#extract-tracing-information-from-html-meta-tags) to the browser, the SDK will continue this trace instead of starting a new one.
* On navigation: Whenever a user navigates (for example in a single-page application), a new trace is started. At the same time, a `navigation` span is created (see [Performance Monitoring](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md)). Once this span ends, the trace remains until the next navigation or page load.

In both cases, this means that if you start spans after the automatic `pageload` and `navigation` spans ended, they will still be part of the same trace. This makes it easy to connect what happened before and after your span.

Server-side SDKs handle traces automatically on a per-request basis. This means that SDKs will:

* Continue an existing trace if the incoming request contains a trace header.
* Start a new trace if the incoming request does not contain a trace header. This trace stays active until the response is sent.

If necessary, you can override the default trace duration by [manually starting a new trace](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md#starting-a-new-trace).

## [How Sampling Propagates in Distributed Traces](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing.md#how-sampling-propagates-in-distributed-traces)

Sentry uses a "head-based" sampling approach:

* A sampling decision is made in the originating service (the "head")
* This decision is propagated to all downstream services

The two key headers are:

* `sentry-trace`: Contains trace ID, span ID, and sampling decision
* `baggage`: Contains additional trace metadata including sample rate

Sentry automatically attaches these headers to outgoing HTTP requests when using the `browserTracingIntegration`. For other communication channels like WebSockets, you can manually propagate trace information:

```javascript
// Extract trace data from the current scope
const traceData = Sentry.getTraceData();
const sentryTraceHeader = traceData["sentry-trace"];
const sentryBaggageHeader = traceData["baggage"];

// Add to your custom request (example using WebSocket)
webSocket.send(
  JSON.stringify({
    message: "Your data here",
    metadata: {
      sentryTrace: sentryTraceHeader,
      baggage: sentryBaggageHeader,
    },
  }),
);
```

## Pages in this section

- [Custom Trace Propagation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/custom-instrumentation.md)
- [Dealing with CORS Issues](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/dealing-with-cors-issues.md)

