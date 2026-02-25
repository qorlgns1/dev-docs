---
title: 'Filtering | Sentry for Next.js'
description: "When you add Sentry to your app, you get a lot of valuable information about errors and performance. And lots of information is good -- as long as it'..."
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering

# Filtering | Sentry for Next.js

When you add Sentry to your app, you get a lot of valuable information about errors and performance. And lots of information is good -- as long as it's the right information, at a reasonable volume.

Sentry offers [Inbound Filters](https://docs.sentry.io/concepts/data-management/filtering.md) that you can enable per project to filter out various events in sentry.io. You can use our pre-defined inbound filters (e.g. filtering known browser extensions), as well as add your own message-based filters.

However, we recommend filtering at the client-level, because it removes the overhead of sending events you don't actually want. The [Sentry SDKs](https://docs.sentry.io/platforms.md) have several configuration options, which are described in this document, to help you filter out events. To learn more about the event fields you can use for filtering, see [Event Payloads](https://develop.sentry.dev/sdk/foundations/transport/event-payloads/).

## [Filtering Error Events](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#filtering-error-events)

Configure your SDK to filter error events by using the `beforeSend` callback method and configuring, enabling, or disabling integrations.

- [Using `ignoreErrors`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-ignore-errors)

You can use the `ignoreErrors` option to filter out errors that match a certain pattern. This option receives a list of strings and regular expressions to match against the error message. When using strings, partial matches will be filtered out. If you need to filter by exact match, use regex patterns instead.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  ignoreErrors: ["fb_xd_fragment", /^Exact Match Message$/],
});
```

See [ignoreErrors](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#ignoreErrors) for details.

- [Using `beforeSend`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-before-send)

You can configure a `beforeSend` callback method to filter error events. Because it's called immediately before the event is sent to the server, this is your last chance to decide not to send data or to edit it. `beforeSend` receives the event object as a parameter and, based on custom logic and the data available on the event, you can either modify the event’s data or drop it completely by returning `null`. This hook is called for both error and message events.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  beforeSend(event) {
    if (event.user) {
      // Don't send user's email address
      delete event.user.email;
    }
    return event;
  },
});
```

See [beforeSend](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#beforeSend) for details, and [Using Hints](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-hints) for details on the `hint` object.

- [Using `allowUrls` and `denyUrls`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-allowurls-and-denyurls)

You can configure the SDK to avoid sending errors that originate in scripts from certain domains. For example, if your scripts are loaded from `cdn.example.com` and your site is `example.com`, you can can configure `allowUrls` as follows to avoid capturing errors from other domains:

```javascript
Sentry.init({
  allowUrls: [/https?:\/\/((cdn|www)\.)?example\.com/],
});
```

Note that this filters errors based on their stack frames, not the URL of the page where the error occurred.

You can also use `denyUrls` if you want to block errors created on specific URLs from being sent to Sentry.

* See [allowUrls](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#allowUrls) details
* See [denyUrls](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#denyUrls) details

- [Using `thirdPartyErrorFilterIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-thirdpartyerrorfilterintegration)

*Available in browser-based SDKs from version 8.10.0*

The `thirdPartyErrorFilterIntegration` allows you to filter out errors originating from third parties, such as browser extensions, code-injecting browsers, or widgets from third-party services that also use Sentry. This integration can be very helpful in reducing noise that's not related to your own application code.

**Prerequisite**: To use the `thirdPartyErrorFilterIntegration`, ensure you are using a bundler and one of [Sentry's bundler plugins](https://github.com/getsentry/sentry-javascript-bundler-plugins).

This integration works by "marking" your JavaScript files with an "application key" during the build process. At runtime, if an error occurs, this integration checks application keys for each stack frame in the stack trace. This allows you to filter out errors with "unmarked" stack frames, which would indicate third-party code.

To set up this integration and to mark your JavaScript files with an application key, first pass an `applicationKey` option to your Sentry bundler plugin. This can be an arbitrary string that identifies your application code:

`next.config.js`

```javascript
module.exports = withSentryConfig(nextConfig, {
  unstable_sentryWebpackPluginOptions: {

    applicationKey: "your-custom-application-key",

  },
});
```

Next, add the `thirdPartyErrorFilterIntegration` to your Sentry initialization:

```javascript
Sentry.init({
  integrations: [

    Sentry.thirdPartyErrorFilterIntegration({
      // Specify the application keys that you specified in the Sentry bundler plugin
      filterKeys: ["your-custom-application-key"],

      // Defines how to handle errors that contain third party stack frames.
      // Possible values are:
      // - 'drop-error-if-contains-third-party-frames'
      // - 'drop-error-if-exclusively-contains-third-party-frames'
      // - 'apply-tag-if-contains-third-party-frames'
      // - 'apply-tag-if-exclusively-contains-third-party-frames'
      behaviour: "drop-error-if-contains-third-party-frames",
    }),

  ],
});
```

The `filterKeys` option takes an array of strings that should be equal to the `applicationKey` value set in the bundler plugin options. Unless your website hosts files from more than one of your build-processes, this array should only contain one item.

The `behaviour` option defines what should happen with errors that contain stack frames from third-party code. There are four modes you can choose from:

* `"drop-error-if-contains-third-party-frames"`: Drop error events that contain at least one third-party stack frame.
* `"drop-error-if-exclusively-contains-third-party-frames"`: Drop error events that exclusively contain third-party stack frames.
* `"apply-tag-if-contains-third-party-frames"`: Keep all error events, but apply a `third_party_code: true` tag in case the error contains at least one third-party stack frame.
* `"apply-tag-if-exclusively-contains-third-party-frames"`: Keep all error events, but apply a `third_party_code: true` tag in case the error contains exclusively third-party stack frames.

If you choose a mode to only apply tags, the tags can then be used in Sentry to filter your issue stream with the `third_party_code` tag in the issue search bar.

The `thirdPartyErrorFilterIntegration` will not work with the [Sentry Loader Script or CDN Bundles](https://docs.sentry.io/platforms/javascript/install/loader.md). This is the case because the Sentry Loader Script and CDN Bundles are detected as "third party" by the integration. This makes it apply the chosen behavior to almost all events, since the Sentry SDK wraps many browser-native APIs.

## [Filtering Transaction Events](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#filtering-transaction-events)

To prevent certain transactions from being reported to Sentry, use the `tracesSampler` or `beforeSendTransaction` configuration option, which allows you to provide a function to evaluate the current transaction and drop it if it's not one you want.

- [Using `ignoreTransactions`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-ignore-transactions)

You can use the `ignoreTransactions` option to filter out transactions that match a certain pattern. This option receives a list of strings and regular expressions to match against the transaction name. When using strings, partial matches will be filtered out. If you need to filter by exact match, use regex patterns instead.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  ignoreTransactions: ["partial/match", /^Exact Transaction Name$/],
});
```

See [ignoreTransactions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#ignoreTransactions) for details.

- [Using `tracesSampler`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-traces-sampler)

You can also use the [tracesSampler](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#tracesSampler) option to prevent certain transactions from being reported to Sentry.

See [Sampling](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/sampling.md#setting-a-sampling-function) on information about how to use it.

- [Using `beforeSendTransaction`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-beforesendtransaction)

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  beforeSendTransaction(event) {
    if (event.transaction === "/unimportant/route") {
      // Don't send the event to Sentry
      return null;
    }
    return event;
  },
});
```

See [beforeSendTransaction](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#beforeSendTransaction) for details, and [Using Hints](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-hints) for details on the `hint` object.

## [Filtering Spans](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#filtering-spans)

Use the `beforeSendSpan` configuration option which allows you to provide a function to modify a span. This function is called for the root span and all child spans. If you want to drop the root span, including its child spans, use [`beforeSendTransaction`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-beforesendtransaction) instead. Please note that you cannot use `beforeSendSpan` to drop a span, you can only modify it and filter data on it.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  beforeSendSpan(span) {
    if (span.description === "should be renamed") {
      span.description = "renamed span";
      span.data = {
        ...span.data,
        myExtraAttribute: true,
      };
    }

    return span;
  },
});
```

See [beforeSendSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#beforeSendSpan) for details.

## [Filtering Breadcrumbs](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#filtering-breadcrumbs)

You can filter breadcrumbs by using the `beforeBreadcrumb` configuration option:

```javascript
Sentry.init({
  // ...
  beforeBreadcrumb(breadcrumb, hint) {
    return breadcrumb.category === "ui.click" ? null : breadcrumb;
  },
});
```

See [beforeBreadcrumb](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#beforeBreadcrumb) for details.

## [Using Hints](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#using-hints)

Hints are available in two places:

1. `beforeSend` / `beforeBreadcrumb`
2. Event processors added via `Sentry.addEventProcessor()`

Event and breadcrumb `hints` are objects containing various types of information used to put together an event or a breadcrumb. Typically `hints` hold the original exception so that additional data can be extracted or grouping can be affected.

For events, hints contain properties such as `event_id`, `originalException`, `syntheticException` (used internally to generate cleaner stack trace), and any other arbitrary `data` that you attach.

For breadcrumbs, the use of `hints` is implementation dependent. For XHR requests, the hint contains the xhr object itself; for user interactions the hint contains the DOM element and event name and so forth.

```javascript
Sentry.init({
  // ...
  beforeSend(event, hint) {
    const error = hint.originalException;
    if (
      error &&
      error.message &&
      error.message.match(/database unavailable/i)
    ) {
      event.fingerprint = ["database-unavailable"];
    }
    return event;
  },
});
```

- [Hints for Events](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#hints-for-events)

`originalException`

The original exception that caused the Sentry SDK to create the event. This is useful for changing how the Sentry SDK groups events or to extract additional information.

`syntheticException`

When a string or a non-error object is raised, Sentry creates a synthetic exception so you can get a basic stack trace. This exception is stored here for further data extraction.

- [Hints for Breadcrumbs](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/filtering.md#hints-for-breadcrumbs)

`event`

For breadcrumbs created from browser events, the Sentry SDK often supplies the event to the breadcrumb as a hint. This can be used to extract data from the target DOM element into a breadcrumb, for example.

`level` / `input`

For breadcrumbs created from console log interceptions. This holds the original console log level and the original input data to the log function.

`response` / `input`

For breadcrumbs created from HTTP requests. This holds the response object (from the fetch API) and the input parameters to the fetch function.

`request` / `response` / `event`

For breadcrumbs created from HTTP requests. This holds the request and response object (from the node HTTP API) as well as the node event (`response` or `error`).

`xhr`

For breadcrumbs created from HTTP requests made using the legacy `XMLHttpRequest` API. This holds the original `xhr` object.

