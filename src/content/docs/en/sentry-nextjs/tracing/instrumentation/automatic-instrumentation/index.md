---
title: 'Automatic Instrumentation | Sentry for Next.js'
description: "Capturing spans requires that you first set up tracing in your app if you haven't already."
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation

# Automatic Instrumentation | Sentry for Next.js

Capturing spans requires that you first [set up tracing in your app](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md) if you haven't already.

`@sentry/nextjs` provides a `BrowserTracing` integration to add automatic instrumentation for monitoring the performance of browser applications, which is enabled by default once you set up tracing in your app. Further, the SDK will automatically enable error collection and tracing in your API routes and [Next.js Data Fetchers](https://nextjs.org/docs/basic-features/data-fetching/overview).

## [What's Captured Automatically](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#whats-captured-automatically)

Once you enable tracing, the SDK automatically captures performance data without additional code:

| What                  | Description                      | Metrics               |
| --------------------- | -------------------------------- | --------------------- |
| **Page loads**        | Full page load performance       | LCP, CLS, TTFB        |
| **Navigations**       | Client-side route changes        | Duration, Web Vitals  |
| **HTTP requests**     | All fetch/XHR calls              | Duration, status, URL |
| **User interactions** | Clicks, inputs that trigger work | INP (responsiveness)  |
| **Long tasks**        | Main thread blocking > 50ms      | Duration, attribution |

The `BrowserTracing` integration creates a new transaction for each pageload and navigation event, and creates a child span for every `XMLHttpRequest` or `fetch` request that occurs while those transactions are open. Additionally, the SDK creates transactions for all requests to API routes and [Next.js data fetchers](https://nextjs.org/docs/basic-features/data-fetching/overview). Learn more about [traces, transactions, and spans](https://docs.sentry.io/product/sentry-basics/tracing/distributed-tracing.md).

## [Enable Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#enable-instrumentation)

To enable tracing, simply set either a `tracesSampleRate` or a `tracesSampler` in your SDK configuration options, as detailed in [Set Up Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md).

## [Common Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#common-configuration)

Most apps only need these options:

* [Distributed Tracing Targets](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#distributed-tracing-targets) — Connect frontend and backend spans
* [Customize Span Names](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#customize-span-names) — Normalize URLs or add context
* [Filter Out Unwanted Requests](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#filter-out-unwanted-requests) — Exclude health checks, analytics

- [Distributed Tracing Targets](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#distributed-tracing-targets)

- [tracePropagationTargets](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#tracePropagationTargets)

| Type    | `Array<string \| RegExp>` |
| ------- | ------------------------- |
| Default | `['localhost', /^\/$/]`   |

Controls which outgoing requests include tracing headers (`sentry-trace` and `baggage`). **Required for connecting frontend spans to backend spans.**

By default, tracing headers are only attached to requests containing `localhost` or starting with `/`. Add your API domains to trace requests across services:

For example:

* A frontend application is served from `example.com`.
* A backend service is served from `api.example.com`.
* During development, the backend service is served from `localhost`.
* The frontend application makes API calls to the backend.
* Set the `tracePropagationTargets` option to `["localhost", /^https:\/\/api\.example\.com/]`.
* Now outgoing XHR/fetch requests to your backend service will get the `sentry-trace` and `baggage` headers attached.

```javascript
Sentry.init({
  // ...
  integrations: [Sentry.browserTracingIntegration()],

  // Set `tracePropagationTargets` to control for which URLs trace propagation should be enabled
  tracePropagationTargets: ["localhost", /^https:\/\/yourserver\.io\/api/],
});
```

Your server must allow these headers via CORS: `Access-Control-Allow-Headers: sentry-trace, baggage`

- [Customize Span Names](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#customize-span-names)

- [beforeStartSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#beforeStartSpan)

| Type | `(options: StartSpanOptions) => StartSpanOptions` |
| ---- | ------------------------------------------------- |

Modify span data before it's captured. Useful for adding context or normalizing URLs with dynamic segments:

```javascript
Sentry.init({
  // ...
  integrations: [
    Sentry.browserTracingIntegration({
      beforeStartSpan: (context) => {
        return {
          ...context,
          attributes: {
            ...context.attributes,
            resultFormat: "legacy",
          },
        };
      },
    }),
  ],
});
```

- [Filter Out Unwanted Requests](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#filter-out-unwanted-requests)

- [shouldCreateSpanForRequest](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#shouldCreateSpanForRequest)

| Type | `(url: string) => boolean` |
| ---- | -------------------------- |

Exclude requests from tracing, such as health checks or analytics pings:

```javascript
Sentry.init({
  // ...
  integrations: [
    Sentry.browserTracingIntegration({
      shouldCreateSpanForRequest: (url) => {
        // Do not create spans for outgoing requests to a `/health/` endpoint
        return !url.match(/\/health\/?$/);
      },
    }),
  ],
});
```

## [Web Vitals & Interactions](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#web-vitals--interactions)

- [Interaction to Next Paint (INP)](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#interaction-to-next-paint-inp)

- [enableInp](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#enableInp)

| Available since | `7.104.0`                         |
| --------------- | --------------------------------- |
| Type            | `boolean`                         |
| Default         | `true` (<!-- -->See note<!-- -->) |

Automatically captures [INP](https://docs.sentry.io/product/insights/web-vitals/web-vitals-concepts.md#interaction-to-next-paint-inp) events to measure responsiveness. Results appear in the [Web Vitals](https://docs.sentry.io/product/insights/web-vitals.md) module.

Default: `true` in SDK 8.x+, `false` in 7.x.

##### INP replaces FID

As of SDK version 10.0.0, First Input Delay (FID) is no longer reported. Google deprecated FID in favor of INP, which provides a more comprehensive measure of responsiveness. If you have alerts or dashboards based on FID, update them to use INP instead.

```javascript
Sentry.init({
  // ...
  integrations: [
    Sentry.browserTracingIntegration({
      enableInp: true,
    }),
  ],
});
```

- [interactionsSampleRate](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#interactionsSampleRate)

| Type    | `number` |
| ------- | -------- |
| Default | `1.0`    |

Sample rate for INP spans, applied on top of `tracesSampleRate`. For example, `interactionsSampleRate: 0.5` with `tracesSampleRate: 0.1` results in 5% of interactions captured.

## [Advanced Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#advanced-options)

Timing & Timeout Options

- [idleTimeout](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#idleTimeout)

| Type    | `number` |
| ------- | -------- |
| Default | `1000`   |

Time in ms to wait before finishing a pageload/navigation span when no unfinished child spans remain.

- [finalTimeout](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#finalTimeout)

| Type    | `number` |
| ------- | -------- |
| Default | `30000`  |

Maximum duration in ms for pageload/navigation spans. Spans exceeding this are automatically finished.

- [childSpanTimeout](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#childSpanTimeout)

| Type    | `number` |
| ------- | -------- |
| Default | `15000`  |

Maximum time in ms a child span can run before the parent pageload/navigation span is finished.

Enable/Disable Specific Instrumentation

- [instrumentPageLoad](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#instrumentPageLoad)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

Enable/disable automatic `pageload` span creation on initial page load.

- [instrumentNavigation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#instrumentNavigation)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

Enable/disable automatic `navigation` span creation on history changes.

- [enableLongTask](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#enableLongTask)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

Enable/disable automatic spans for long tasks (main thread blocking > 50ms).

- [enableLongAnimationFrame](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#enableLongAnimationFrame)

| Available since | `8.18.0`  |
| --------------- | --------- |
| Type            | `boolean` |
| Default         | `true`    |

Enable/disable spans for long animation frames. Falls back to long tasks if browser doesn't support long animation frames.

- [markBackgroundSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#markBackgroundSpan)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

Mark pageload/navigation spans as "cancelled" when the tab moves to background. Recommended to keep enabled for accurate measurements.

- [enableReportPageLoaded](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#enableReportPageLoaded)

| Available since | `10.13.0` |
| --------------- | --------- |
| Type            | `boolean` |
| Default         | `false`   |

Enable the [`Sentry.reportPageLoaded()` function](https://docs.sentry.io/platforms/javascript/guides/nextjs/apis.md#reportPageLoaded).

- [traceFetch](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#traceFetch)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

Enable/disable automatic span creation for `fetch` requests.

- [traceXHR](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#traceXHR)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

Enable/disable automatic span creation for `XMLHttpRequest` (XHR) requests.

- [enableHTTPTimings](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#enableHTTPTimings)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

Enable/disable adding detailed HTTP timing data (DNS lookup, TLS handshake, etc.) to fetch/XHR spans via the Performance Resource Timing API.

- [linkPreviousTrace](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#linkPreviousTrace)

| Type    | `'in-memory' \| 'session-storage' \| false` |
| ------- | ------------------------------------------- |
| Default | `'in-memory'`                               |

Controls how new pageload spans are linked to the previous trace. Set to `'in-memory'` to link within the same page lifecycle, `'session-storage'` to persist links across page reloads via session storage, or `false` to disable trace linking.

Filtering & Ignoring Spans

- [ignoreResourceSpans](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#ignoreResourceSpans)

| Available since | `9.23.0`        |
| --------------- | --------------- |
| Type            | `Array<string>` |
| Default         | `[]`            |

Ignore specific resource span categories by their `op` (e.g., `resource.script`, `resource.css`):

```javascript
Sentry.init({
  integrations: [
    Sentry.browserTracingIntegration({
      ignoreResourceSpans: ["resource.css", "resource.script"],
    }),
  ],
});
```

- [ignorePerformanceApiSpans](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#ignorePerformanceApiSpans)

| Available since | `9.23.0`                  |
| --------------- | ------------------------- |
| Type            | `Array<string \| RegExp>` |
| Default         | `[]`                      |

Ignore spans created from `performance.mark()` and `performance.measure()`:

```javascript
Sentry.init({
  integrations: [
    Sentry.browserTracingIntegration({
      ignorePerformanceApiSpans: ["myMeasurement", /myMark/],
    }),
  ],
});
```

- [onRequestSpanStart](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#onRequestSpanStart)

| Type | `(span: Span, requestInformation: { headers?: WebFetchHeaders }): void` |
| ---- | ----------------------------------------------------------------------- |

Callback invoked when a span starts for an outgoing fetch/XHR request. Use to annotate spans with additional attributes based on request headers.

## [Next.js Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#nextjs-configuration)

The `browserTracingIntegration` is automatically enabled in `@sentry/nextjs`. To customize options, include it explicitly in `instrumentation-client.js`:

```javascript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    Sentry.browserTracingIntegration({
      // your options here
    }),
  ],
  tracesSampleRate: 1.0,
  tracePropagationTargets: [
    "localhost",
    /^\//,
    /^https:\/\/yourserver\.io\/api/,
  ],
});
```

