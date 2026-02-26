---
title: 'Migrate from 7.x to 8.x | Sentry for Next.js'
description: 'The main goal of version 8 is to improve our performance monitoring APIs, integrations API, and ESM support. This version is breaking because we remov...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8

# Migrate from 7.x to 8.x | Sentry for Next.js

The main goal of version 8 is to improve our performance monitoring APIs, integrations API, and ESM support. This version is breaking because we removed deprecated APIs, restructured npm package contents, and introduced new dependencies on OpenTelemetry.

## [Migration Codemod](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#migration-codemod)

Before updating to `8.x` of the SDK, we recommend upgrading to the latest version of `7.x`. To fix most of the deprecations on `7.x`, you can use the [`@sentry/migr8`](https://www.npmjs.com/package/@sentry/migr8) codemod to automatically update your SDK usage. `@sentry/migr8` requires Node 18+.

```bash
npx @sentry/migr8@latest
```

Our migration tool will let you select which updates to run, and automatically update your code. In some cases, we cannot automatically change code for you. These will be marked with a `TODO(sentry)` comment instead. Make sure to review all code changes after running `@sentry/migr8`! For more details on the deprecations, see our docs on [Deprecations in 7.x](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md). Despite having `@sentry/migr8`, we still recommend reading the migration guide, since `@sentry/migr8` does not cover all of the changes needed to migrate.

## [Upgrading to `8.x`](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#upgrading-to-8x)

`8.x` simplifies Sentry Next.js SDK initialization and leverages Next.js OpenTelemetry instrumentation for tracing.

We recommend you read through all the [Important Changes](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#important-changes) as they affect all SDK users. The [Other Changes](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#other-changes) linked below only affect users who have more customized instrumentation. There is also a [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#troubleshooting) section for common issues.

We also have a [detailed migration guide](https://github.com/getsentry/sentry-javascript/blob/develop/MIGRATION.md#upgrading-from-7x-to-8x) on GitHub, which has a comprehensive list of all changes alongside the source code of the SDK.

## [Important Changes](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#important-changes)

- [Supported versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#supported-versions)

Sentry Next.js SDK `8.x` supports:

* Next.js version `13.2.0` or higher
* Webpack `5.0.0` or higher
* Node `14.18.0` or higher

If you need to support older versions of Node.js or Next.js, please use Sentry Next.js SDK `7.x`.

The SDK now requires ES2018 compatibility plus support for [`globalThis`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis). The minimum supported browser versions are:

* Chrome 71
* Edge 79
* Safari 12.1, iOS Safari 12.2
* Firefox 65
* Opera 58
* Samsung Internet 10

For IE11 support please transpile your code to ES5 using babel or similar and add required polyfills.

- [Updated SDK initialization](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#updated-sdk-initialization)

With `8.x` the Next.js SDK will require an additional `instrumentation.ts` file to execute the `sentry.server.config.js|ts` and `sentry.edge.config.js|ts` modules to initialize the SDK for the server-side. The `instrumentation.ts` file is a Next.js native API called [instrumentation hook](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation).

To start using the Next.js instrumentation hook, follow these steps:

1. First, enable the Next.js instrumentation hook by setting the [`experimental.instrumentationHook`](https://nextjs.org/docs/app/api-reference/next-config-js/instrumentationHook) to true in your `next.config.js`. (This step is no longer required with Next.js 15)

`next.config.js`

```JavaScript
module.exports = {

  experimental: {
    instrumentationHook: true, // Not required on Next.js 15+
  },

}
```

2. Next, create a `instrumentation.ts|js` file in the root directory of your project (or in the src folder if you have have one).

3. Now, export a register function from the `instrumentation.ts|js` file and import your `sentry.server.config.js|ts` and `sentry.edge.config.js|ts` modules:

`instrumentation.js`

```JavaScript
import * as Sentry from '@sentry/nextjs';

export async function register() {
  if (process.env.NEXT_RUNTIME === 'nodejs') {
    await import('./sentry.server.config');
  }

  if (process.env.NEXT_RUNTIME === 'edge') {
    await import('./sentry.edge.config');
  }
}
```

If you are using a [Next.js custom server](https://nextjs.org/docs/pages/building-your-application/configuring/custom-server), the `instrumentation.ts|js` hook is not called by Next.js so SDK instrumentation will not work as expected. See the [troubleshooting section](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#nextjs-custom-server) for more information.

With 8.x, `@sentry/nextjs` on the server has been completely overhauled. It is now powered by [OpenTelemetry](https://opentelemetry.io/) under the hood. You do not need to know or understand what OpenTelemetry is in order to use Sentry. We set up OpenTelemetry under the hood. If you use OpenTelemetry-native APIs to start spans, Sentry will pick up everything automatically.

We now support the following integrations out of the box with 0 configuration:

* `httpIntegration`: Automatically instruments Node http and https standard libraries
* `nativeNodeFetchIntegration`: Automatically instruments top level fetch and undici
* `graphqlIntegration`: Automatically instruments GraphQL
* `mongoIntegration`: Automatically instruments MongoDB
* `mongooseIntegration`: Automatically instruments Mongoose
* `mysqlIntegration`: Automatically instruments MySQL
* `mysql2Integration`: Automatically instruments MySQL2
* `postgresIntegration`: Automatically instruments PostgreSQL

- [Updated `withSentryConfig` Usage](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#updated-withsentryconfig-usage)

With `8.x` of the Sentry Next.js SDK, `withSentryConfig` will no longer accept 3 arguments. The second argument (holding options for the Sentry Webpack plugin) and the third argument (holding options for SDK build-time configuration) should now be passed as one:

`next.config.js`

```JavaScript
const nextConfig = {
  // Your Next.js options...
};

-module.exports = withSentryConfig(
-  nextConfig,
-  {
-    // Your Sentry Webpack Plugin Options...
-  },
-  {
-    // Your Sentry SDK options...
-  },
-);
+module.exports = withSentryConfig(nextConfig, {
+  // Your Sentry Webpack Plugin Options...
+  // AND your Sentry SDK options...
+});
```

As part of this change the SDK will no longer support passing Next.js options with a `sentry` property to `withSentryConfig`. Please use the second argument of `withSentryConfig` to configure the SDK instead.

`next.config.js`

```JavaScript
 const nextConfig = {
   // Your Next.js options...
-
-  sentry: {
-    // Your Sentry SDK options...
-  },
 };

 module.exports = withSentryConfig(nextConfig, {
   // Your Sentry Webpack Plugin Options...
+  // AND your Sentry SDK options...
 });
```

- [New Tracing APIs](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#new-tracing-apis)

The Custom Instrumentation API for Tracing has been revamped in `8.x`. New methods have been introduced, and `startTransaction` and `span.startChild` has been removed. See the [new Tracing APIs docs](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v8-new-performance-api.md) for more information.

## [Other Changes](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#other-changes)

- [Improved Source Map Uploading](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#improved-source-map-uploading)

Under the hood, the Next.js SDK uses [Sentry Webpack Plugin](https://www.npmjs.com/package/@sentry/webpack-plugin) to upload sourcemaps and automatically associate add releases to your events. In `8.x`, the SDK now uses `2.x` of the Sentry Webpack Plugin which brings many improvements and bug fixes. Sourcemaps uploading with the Next.js SDK now uses [Debug IDs](https://docs.sentry.io/platforms/javascript/sourcemaps/troubleshooting_js/debug-ids.md).

- [Removal of deprecated API](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-deprecated-api)

The following previously deprecated API has been removed from the `@sentry/nextjs` package:

* `nextRouterInstrumentation` has been removed in favour of `browserTracingIntegration`.

`sentry.client.config.js`

```JavaScript
 import * as Sentry from '@sentry/nextjs';

 Sentry.init({
   dsn: '___PUBLIC_DSN___',
   integrations: [
-    new Sentry.Integrations.BrowserTracing({
-      routingInstrumentation: Sentry.nextRouterInstrumentation
-    }),
+    Sentry.browserTracingIntegration(),
   ]
 });
```

* `withSentryApi` has been removed in favour of `wrapApiHandlerWithSentry`.

`pages/api/*`

```JavaScript
-import { withSentryApi } from "@sentry/nextjs";
+import { wrapApiHandlerWithSentry } from "@sentry/nextjs";

 const handler = (req, res) => {
   res.status(200).json({ name: "John Doe" });
 };

-export default withSentryApi(handler, "/api/myRoute");
+export default wrapApiHandlerWithSentry(handler, "/api/myRoute");
```

* `withSentryGetServerSideProps` has been removed in favour of `wrapGetServerSidePropsWithSentry`.

`pages/index.js`

```JavaScript
-import { withSentryGetServerSideProps } from "@sentry/nextjs";
+import { wrapGetServerSidePropsWithSentry } from "@sentry/nextjs";

 export async function _getServerSideProps() {
   // Fetch data from external API
 }

-export const getServerSideProps = withSentryGetServerSideProps(_getServerSideProps);
+export const getServerSideProps = wrapGetServerSidePropsWithSentry(_getServerSideProps);
```

* `withSentryGetStaticProps` has been removed in favour of `wrapGetStaticPropsWithSentry`.

`pages/index.js`

```JavaScript
-import { withSentryGetStaticProps } from "@sentry/nextjs";
+import { wrapGetStaticPropsWithSentry } from "@sentry/nextjs";

 export async function _getStaticProps() {
   // Fetch data from external API
 }

-export const getStaticProps = withSentryGetStaticProps(_getServerSideProps);
+export const getStaticProps = wrapGetStaticPropsWithSentry(_getServerSideProps);
```

* `withSentryServerSideGetInitialProps` has been removed in favour of `wrapGetInitialPropsWithSentry`.

`pages/index.js`

```JavaScript
-import { withSentryServerSideGetInitialProps } from "@sentry/nextjs";
+import { wrapGetInitialPropsWithSentry } from "@sentry/nextjs";

 async function getInitialProps() {
   // Fetch data from external API
   return { data }
 }

-Page.getInitialProps = withSentryServerSideGetInitialProps(getInitialProps);
+Page.getInitialProps = wrapGetInitialPropsWithSentry(getInitialProps);

 export default function Page({ data }) {
   return data
 }
```

Similar to the above changes, the following API has been removed:

* `withSentryServerSideAppGetInitialProps` has been removed in favour of `wrapAppGetInitialPropsWithSentry`.
* `withSentryServerSideDocumentGetInitialProps` has been removed in favour of `wrapDocumentGetInitialPropsWithSentry`.
* `withSentryServerSideErrorGetInitialProps` has been removed in favour of `wrapErrorGetInitialPropsWithSentry`.

The `IS_BUILD` and `isBuild` exports have been removed. There is no replacement for these exports.

- [OpenTelemetry Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#opentelemetry-instrumentation)

The Next.js SDK now leverages Next.js OpenTelemetry instrumentation for tracing. This means that the SDK will automatically capture OpenTelemetry data for your Next.js application without any additional configuration.

If you were previously using the `@sentry/opentelemetry-node`, it is no longer required and can be removed from your project. To migrate from using `@sentry/opentelemetry-node` to the Next.js SDK, follow these steps:

1. Make sure you've updated your SDK initialization as per the [Updated SDK initialization](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#updated-sdk-initialization) section above.

2. Remove `instrumenter: "otel",` from your `Sentry.init` call for your server-side SDK initialization.

`sentry.server.config.js`

```JavaScript
 import * as Sentry from '@sentry/nextjs';

 Sentry.init({
   dsn: '___PUBLIC_DSN___',
-  instrumenter: 'otel',
 });
```

3. Remove the `@sentry/opentelemetry-node` package and the `instrumentation.node.js|ts` file in your project. Make sure `instrumentation.js|ts` no longer imports the `instrumentation.node.js|ts` file.

- [Revamped Application Not Responding Detection](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#revamped-application-not-responding-detection)

The `enableAnrDetection` and `Anr` class exports have been removed the SDK. Instead you can now use the `Sentry.anrIntegration` to enable [Application Not Responding detection](https://docs.sentry.io/platforms/javascript/guides/node/configuration/application-not-responding.md)

```JavaScript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [

    Sentry.anrIntegration({ captureStackTrace: true })

  ],
});
```

- [Behaviour in combination with `onUncaughtException` handlers in Node.js](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#behaviour-in-combination-with-onuncaughtexception-handlers-in-nodejs)

Previously the SDK exited the process by default, even though additional `onUncaughtException` may have been registered, that would have prevented the process from exiting. You could opt out of this behaviour by setting the `exitEvenIfOtherHandlersAreRegistered: false` in the `onUncaughtExceptionIntegration` options. Up until now the value for this option defaulted to `true`.

Going forward, the default value for `exitEvenIfOtherHandlersAreRegistered` will be `false`, meaning that the SDK will not exit your process when you have registered other `onUncaughtException` handlers.

- [Removal of `deepReadDirSync` method](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-deepreaddirsync-method)

The `deepReadDirSync` method has been removed as an export from the SDK. There is no replacement API.

- [Removal of `Sentry.Handlers.trpcMiddleware()` in favor of `Sentry.trpcMiddleware()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-sentryhandlerstrpcmiddleware-in-favor-of-sentrytrpcmiddleware)

The Sentry tRPC middleware got moved from `Sentry.Handlers.trpcMiddleware()` to `Sentry.trpcMiddleware()`.

#
- [Removal of Client-Side health check transaction filters](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-client-side-health-check-transaction-filters)

The SDK no longer filters out health check transactions by default. Instead, they are sent to Sentry but still dropped by the Sentry backend by default. You can disable dropping them in your Sentry project settings. If you still want to drop specific transactions within the SDK you can either use the `ignoreTransactions` SDK option.

- [Removal of `@sentry/replay` package](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-sentryreplay-package)

The `@sentry/replay` package is no longer required. Instead you can import the relevant methods directly from your SDK. In addition to this, the integration is now functional instead of class-based.

```JavaScript
-import { Replay } from '@sentry/replay';
-
 Sentry.init({
   dsn: '___PUBLIC_DSN___',
   integrations: [
-    new Replay(),
+    Sentry.replayIntegration(),
   ],
 });
```

- [Change of Replay default options (`unblock` and `unmask`)](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#change-of-replay-default-options-unblock-and-unmask)

The Replay options `unblock` and `unmask` now have `[]` as default value. This means that if you want to use these options, you have to explicitly set them like this:

```JavaScript
Sentry.init({
  integrations: [
    Sentry.replayIntegration({
      unblock: [".sentry-unblock, [data-sentry-unblock]"],
      unmask: [".sentry-unmask, [data-sentry-unmask]"],
    }),
  ],
});
```

- [Removal of makeXHRTransport transport](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-makexhrtransport-transport)

The xhr transport via `makeXHRTransport` transport has been removed. Only `makeFetchTransport` is available now. This means that the Sentry SDK requires the `fetch` API to be available in the environment.

- [Removal of the `Offline` integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-the-offline-integration)

The `Offline` integration has been removed in favor of the [offline transport wrapper](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/transports.md#makebrowserofflinetransport)

- [Removal of `wrap` export](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-wrap-export)

The `Sentry.wrap` export has been removed. There is no replacement API.

- [Updated behaviour of `tracePropagationTargets` in the browser](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#updated-behaviour-of-tracepropagationtargets-in-the-browser)

We updated the behaviour of the SDKs when no `tracePropagationTargets` option was defined. As a reminder, you can provide a list of strings or RegExes that will be matched against URLs to tell the SDK, to which outgoing requests tracing HTTP headers should be attached to. These tracing headers are used for distributed tracing.

Previously, on the browser, when `tracePropagationTargets` were not defined, they defaulted to the following: `['localhost', /^\/(?!\/)/]`. This meant that all request targets to that had "localhost" in the URL, or started with a `/` were equipped with tracing headers. This default was chosen to prevent CORS errors in your browser applications. However, this default had a few flaws.

Going forward, when the `tracePropagationTargets` option is not set, tracing headers will be attached to all outgoing requests on the same origin. For example, if you're on `https://example.com/` and you send a request to `https://example.com/api`, the request will be traced (ie. will have trace headers attached). Requests to `https://api.example.com/` will not, because it is on a different origin. The same goes for all applications running on `localhost`.

When you provide a `tracePropagationTargets` option, all of the entries you defined will now be matched be matched against the full URL of the outgoing request. Previously, it was only matched against what you called request APIs with. For example, if you made a request like `fetch("/api/posts")`, the provided `tracePropagationTargets` were only compared against `"/api/posts"`.

- [Deprecation of `Hub` and `getCurrentHub()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#deprecation-of-hub-and-getcurrenthub)

The `Hub` has been a very important part of the Sentry SDK API up until now. Hubs were the SDK's "unit of concurrency" to keep track of data across threads and to scope data to certain parts of your code. Because it is overly complicated and confusing to power users, it is going to be replaced by a set of new APIs: the "new Scope API". For now `Hub` and `getCurrentHub` are still available, but it will be removed in the next major version.

See [Deprecate Hub](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-hub) for details on how to replace existing usage of the Hub APIs.

- [Removal of class-based integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-class-based-integrations)

In v7, integrations are classes and can be added as e.g. `integrations: [new Sentry.Replay()]`. In v8, integrations will not be classes anymore, but instead functions. Both the use as a class, as well as accessing integrations from the `Integrations.XXX` hash, is deprecated in favor of using the new functional integrations. For example, `new Integrations.LinkedErrors()` becomes `linkedErrorsIntegration()`.

For a list of integrations and their replacements, see [the `7.x` deprecation documentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-class-based-integrations).

- [Removal of `Sentry.configureScope` method](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-sentryconfigurescope-method)

The top level `Sentry.configureScope` function has been removed. Instead, you should use the `Sentry.getCurrentScope()` to access and mutate the current scope.

```JavaScript
- Sentry.configureScope((scope) => {
-  scope.setTag("key", "value");
- });
+ Sentry.getCurrentScope().setTag("key", "value");
```

- [`tracingOrigins` has been replaced by `tracePropagationTargets`](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#tracingorigins-has-been-replaced-by-tracepropagationtargets)

`tracingOrigins` is now removed in favor of the `tracePropagationTargets` option. The `tracePropagationTargets` option should be set in the `Sentry.init()` options, or in your custom `Client`s option if you create them.

```TypeScript
Sentry.init({
  dsn: "___DSN___",
  integrations: [Sentry.browserTracingIntegration()],
  tracePropagationTargets: ["localhost", "example.com"],
});
```

- [Simplification of Metrics Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#simplification-of-metrics-configuration)

In `7.x`, you had to enable the metrics aggregator by setting the `_experiments` option to `{ metricsAggregator: true }`. In addition for browser environments you had to add the `metricsAggregatorIntegration` to the `integrations` array.

```TypeScript
// v7 - Server (Node/Deno/Bun)
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  _experiments: {
    metricsAggregator: true,
  },
});

// v7 - Browser
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.metricsAggregatorIntegration()],
});

Sentry.metrics.increment("my_metric");
```

In `8.x` no additional configuration is needed to use metrics APIs.

```ts
// v8
Sentry.init({
  dsn: "___PUBLIC_DSN___",
});

Sentry.metrics.increment("my_metric");
```

- [Removal of Severity Enum](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-severity-enum)

In `7.x` we deprecated the `Severity` enum in favor of using the `SeverityLevel` type as this helps save bundle size, and this has been removed in `8.x`. You should now use the `SeverityLevel` type directly.

```JavaScript
- import { Severity } from '@sentry/types';
+ import { SeverityLevel } from '@sentry/types';

- const level = Severity.error;
+ const level: SeverityLevel = "error";
```

#
- [Removal of `spanStatusfromHttpCode` in favour of `getSpanStatusFromHttpCode`](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-spanstatusfromhttpcode-in-favour-of-getspanstatusfromhttpcode)

In `8.x`, we are removing the `spanStatusfromHttpCode` function in favor of `getSpanStatusFromHttpCode`.

```JavaScript
- const spanStatus = spanStatusfromHttpCode(200);
+ const spanStatus = getSpanStatusFromHttpCode(200);
```

- [`framesToPop` applies to parsed frames](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#framestopop-applies-to-parsed-frames)

Errors with `framesToPop` property will have the specified number of frames removed from the top of the stack. This changes compared to the v7 where the property `framesToPop` was used to remove top n lines from the stack string.

- [Removal of `Span` class export from SDK packages](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-span-class-export-from-sdk-packages)

In `8.x`, we are no longer exporting the `Span` class from SDK packages. Internally, this class is now called `SentrySpan`, and it is no longer meant to be used by users directly.

- [Removal of `void` from transport return types](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-void-from-transport-return-types)

The `send` method on the `Transport` interface now always requires a `TransportMakeRequestResponse` to be returned in the promise. This means that the `void` return type is no longer allowed.

```TypeScript
// v7
 interface Transport {
-  send(event: Event): Promise<void | TransportMakeRequestResponse>;
+  send(event: Event): Promise<TransportMakeRequestResponse>;
 }
```

- [`extraErrorDataIntegration` changes](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#extraerrordataintegration-changes)

The `extraErrorDataIntegration` integration now looks at [`error.cause`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause) by default.

- [`transactionContext` no longer passed to `tracesSampler`](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#transactioncontext-no-longer-passed-to-tracessampler)

Instead of an `transactionContext` being passed to the `tracesSampler` callback, the callback will directly receive `name` and `attributes` going forward. Note that the `attributes` are only the attributes at span creation time, and some attributes may only be set later during the span lifecycle (and thus not be available during sampling).

- [`getClient()` always returns a client](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#getclient-always-returns-a-client)

`getClient()` now always returns a client if `Sentry.init()` was called. For cases where this may be used to check if Sentry was actually initialized, using `getClient()` will thus not work anymore. Instead, you should use the new `Sentry.isInitialized()` utility to check this.

- [Removal of `addGlobalEventProcessor` in favour of `addEventProcessor`](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-addglobaleventprocessor-in-favour-of-addeventprocessor)

In `8.x`, we are removing the `addGlobalEventProcessor` function in favor of `addEventProcessor`.

```JavaScript
- Sentry.addGlobalEventProcessor((event) => {
+ Sentry.getGlobalScope().addEventProcessor((event) => {
   delete event.extra;
   return event;
 });
```

- [Removal of `@sentry/integrations` package](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-sentryintegrations-package)

`@sentry/integrations` has been removed and will no longer be published. We moved pluggable integrations from their own package (`@sentry/integrations`) to `@sentry/nextjs`. In addition they are now functions instead of classes.

Integrations that are now exported from `@sentry/nextjs` for client-side init:

* `httpClientIntegration` (`HTTPClient`)
* `contextLinesIntegration` (`ContextLines`)
* `reportingObserverIntegration` (`ReportingObserver`)

Integrations that are now exported from `@sentry/nextjs` for client-side and server-side init:

* `captureConsoleIntegration` (`CaptureConsole`)
* `debugIntegration` (`Debug`)
* `extraErrorDataIntegration` (`ExtraErrorData`)
* `rewriteFramesIntegration` (`RewriteFrames`)
* `sessionTimingIntegration` (`SessionTiming`)
* `dedupeIntegration` (`Dedupe`) - Note: enabled by default, not pluggable

The `Transaction` integration has been removed from `@sentry/integrations`. There is no replacement API.

## [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#troubleshooting)

- [Removal of `sentry.server.config.js|ts` and `sentry.edge.config.js|ts`](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#removal-of-sentryserverconfigjsts-and-sentryedgeconfigjsts)

`8.x` of the Next.js SDK updates enforces usage of the `instrumentation.ts` file because it is a more flexible and powerful way to initialize the SDK, and allows us to use the Next.js built-in hooks and OpenTelemetry instrumentation. In addition it helps the SDK to be more compatible with the [Turbopack](https://turbo.build/pack) which is not supported in Next.js SDK `7.x`. The Next.js team recommends to use the `instrumentation.ts` file for SDK initialization, and we are working closely with them to ensure that the SDK works seamlessly with Next.js.

- [Next.js Custom server](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8.md#nextjs-custom-server)

If you are using a [Next.js custom server](https://nextjs.org/docs/pages/building-your-application/configuring/custom-server), the `instrumentation.ts|js` hook is not called by Next.js so you need to manually call it yourself from within your server code. It is recommended to do so as early as possible in your application lifecycle.

Here's an example of adding Sentry initialization code to the custom server example as per the [Next.js documentation](https://nextjs.org/docs/pages/building-your-application/configuring/custom-server):

```JavaScript
// make sure that Sentry is imported and initialized before any other imports.

+ const Sentry = require('@sentry/nextjs');
+
+ Sentry.init({
+   dsn: '___PUBLIC_DSN___',
+   // Your Node.js Sentry configuration...
+ })

const { createServer } = require('http')
const { parse } = require('url')
const next = require('next')

const dev = process.env.NODE_ENV !== 'production'
const hostname = 'localhost'
const port = 3000

const app = next({ dev, hostname, port })
const handle = app.getRequestHandler()

app.prepare().then(() => {
  createServer(async (req, res) => {
    // server code
  })
    .once('error', (err) => {
      // error code
    })
    .listen(port, () => {
      console.log(`> Ready on http://${hostname}:${port}`)
    })
})
```

## Pages in this section

- [New Tracing APIs](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v8-new-performance-api.md)
- [Deprecations in 7.x](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md)

