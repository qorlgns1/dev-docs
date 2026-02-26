---
title: 'Deprecations in 7.x | Sentry for Next.js'
description: 'To fix most of the deprecations on , you can use the  codemod to automatically update your SDK usage.  requires Node 18+.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations

# Deprecations in 7.x | Sentry for Next.js

To fix most of the deprecations on `7.x`, you can use the [`@sentry/migr8`](https://www.npmjs.com/package/@sentry/migr8) codemod to automatically update your SDK usage. `@sentry/migr8` requires Node 18+.

```bash
npx @sentry/migr8@latest
```

Our migration tool will let you select which updates to run, and automatically update your code. In some cases, we cannot automatically change code for you. These will be marked with a `TODO(sentry)` comment instead. Make sure to review all code changes after running `@sentry/migr8`!

## [List of Deprecations](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#list-of-deprecations)

The following is a list of the most important deprecations that happened in `7.x`. Please see the [detailed migration docs](https://github.com/getsentry/sentry-javascript/blob/develop/MIGRATION.md#deprecations-in-7x) on GitHub for a comprehensive list of all deprecations.

- [Deprecate class-based integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-class-based-integrations)

*Deprecation introduced in `7.100.0`.*

In v7, integrations are classes and can be added as e.g. `integrations: [new Sentry.Integrations.ContextLines()]`. In v8, integrations will not be classes anymore, but instead functions. Both the use as a class, as well as accessing integrations from the `Integrations.XXX` hash, is deprecated in favor of using the new functional integrations

* for example, `new Integrations.LinkedErrors()` becomes `linkedErrorsIntegration()`.

The following list shows how integrations should be migrated:

Client-side Integrations:

| Old                                 | New                              |
| ----------------------------------- | -------------------------------- |
| `new BrowserTracing()`              | `browserTracingIntegration()`    |
| `new InboundFilters()`              | `inboundFiltersIntegration()`    |
| `new FunctionToString()`            | `functionToStringIntegration()`  |
| `new LinkedErrors()`                | `linkedErrorsIntegration()`      |
| `new ModuleMetadata()`              | `moduleMetadataIntegration()`    |
| `new Replay()`                      | `replayIntegration()`            |
| `new ReplayCanvas()`                | `replayCanvasIntegration()`      |
| `new Feedback()`                    | `feedbackIntegration()`          |
| `new CaptureConsole()`              | `captureConsoleIntegration()`    |
| `new Debug()`                       | `debugIntegration()`             |
| `new Dedupe()`                      | `dedupeIntegration()`            |
| `new ExtraErrorData()`              | `extraErrorDataIntegration()`    |
| `new ReportingObserver()`           | `reportingObserverIntegration()` |
| `new RewriteFrames()`               | `rewriteFramesIntegration()`     |
| `new SessionTiming()`               | `sessionTimingIntegration()`     |
| `new HttpClient()`                  | `httpClientIntegration()`        |
| `new ContextLines()`                | `contextLinesIntegration()`      |
| `new Breadcrumbs()`                 | `breadcrumbsIntegration()`       |
| `new GlobalHandlers()`              | `globalHandlersIntegration()`    |
| `new HttpContext()`                 | `httpContextIntegration()`       |
| `new TryCatch()`                    | `browserApiErrorsIntegration()`  |
| `new BrowserProfilingIntegration()` | `browserProfilingIntegration()`  |

Server-side Integrations:

| Old                          | New                                 |
| ---------------------------- | ----------------------------------- |
| `new InboundFilters()`       | `inboundFiltersIntegration()`       |
| `new FunctionToString()`     | `functionToStringIntegration()`     |
| `new LinkedErrors()`         | `linkedErrorsIntegration()`         |
| `new RequestData()`          | `requestDataIntegration()`          |
| `new CaptureConsole()`       | `captureConsoleIntegration()`       |
| `new Debug()`                | `debugIntegration()`                |
| `new Dedupe()`               | `dedupeIntegration()`               |
| `new ExtraErrorData()`       | `extraErrorDataIntegration()`       |
| `new RewriteFrames()`        | `rewriteFramesIntegration()`        |
| `new SessionTiming()`        | `sessionTimingIntegration()`        |
| `new Console()`              | `consoleIntegration()`              |
| `new Context()`              | `nodeContextIntegration()`          |
| `new Modules()`              | `modulesIntegration()`              |
| `new OnUncaughtException()`  | `onUncaughtExceptionIntegration()`  |
| `new OnUnhandledRejection()` | `onUnhandledRejectionIntegration()` |
| `new ContextLines()`         | `contextLinesIntegration()`         |
| `new LocalVariables()`       | `localVariablesIntegration()`       |
| `new Spotlight()`            | `spotlightIntegration()`            |
| `new Anr()`                  | `anrIntegration()`                  |
| `new Hapi()`                 | `hapiIntegration()`                 |
| `new Undici()`               | `nativeNodeFetchIntegration()`      |
| `new Http()`                 | `httpIntegration()`                 |
| `new ProfilingIntegration()` | `nodeProfilingIntegration()`        |

- [Deprecated `BrowserTracing` integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecated-browsertracing-integration)

*Deprecation introduced in `7.100.0`.*

The `BrowserTracing` integration, together with the custom routing instrumentations passed to it, are deprecated in v8.

Instead, you should use `Sentry.browserTracingIntegration()`.

Browser tracing is automatically set up for you in these packages so you do not need to change you code unless you were using the `BrowserTracing` class directly.

`instrumentation-client.js`

```JavaScript
 import * as Sentry from "@sentry/nextjs";

 Sentry.init({
   dsn: "___PUBLIC_DSN___",
-  integrations: [new Sentry.BrowserTracing()],
+  integrations: [Sentry.browserTracingIntegration()],
 });
```

- [Deprecate `getIntegration()` and `getIntegrationById()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-getintegration-and-getintegrationbyid)

*Deprecation introduced in `7.94.0`.*

This deprecates `getIntegrationById()` and `getIntegration()` on the client. Instead, use `getIntegrationByName()`. You can optionally pass an integration generic to make it easier to work with.

```TypeScript
const replay = getClient().getIntegrationByName<Replay>("Replay");
```

- [Deprecate `Hub`](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-hub)

*Deprecation introduced in `7.110.0`.*

The `Hub` has been a very important part of the Sentry SDK API up until now. Hubs were the SDK's "unit of concurrency" to keep track of data across threads and to scope data to certain parts of your code. Because it is overly complicated and confusing to power users, it is going to be replaced by a set of new APIs: the "new Scope API".

`Scope`s have existed before in the SDK but we are now expanding on them because we have found them powerful enough to fully cover the `Hub` API.

If you are using the `Hub` right now, see the following table on how to migrate to the new API:

| Old `Hub` API          | New `Scope` API                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------ |
| `new Hub()`            | `withScope()`, `withIsolationScope()` or `new Scope()`                               |
| hub.isOlderThan()      | REMOVED - Was used to compare `Hub` instances, which are gonna be removed            |
| hub.bindClient()       | A combination of `scope.setClient()` and `client.init()`                             |
| hub.pushScope()        | `Sentry.withScope()`                                                                 |
| hub.popScope()         | `Sentry.withScope()`                                                                 |
| hub.withScope()        | `Sentry.withScope()`                                                                 |
| getClient()            | `Sentry.getClient()`                                                                 |
| getScope()             | `Sentry.getCurrentScope()` to get the currently active scope                         |
| getIsolationScope()    | `Sentry.getIsolationScope()`                                                         |
| getStack()             | REMOVED - The stack used to hold scopes. Scopes are used directly now                |
| getStackTop()          | REMOVED - The stack used to hold scopes. Scopes are used directly now                |
| captureException()     | `Sentry.captureException()`                                                          |
| captureMessage()       | `Sentry.captureMessage()`                                                            |
| captureEvent()         | `Sentry.captureEvent()`                                                              |
| addBreadcrumb()        | `Sentry.addBreadcrumb()`                                                             |
| setUser()              | `Sentry.setUser()`                                                                   |
| setTags()              | `Sentry.setTags()`                                                                   |
| setExtras()            | `Sentry.setExtras()`                                                                 |
| setTag()               | `Sentry.setTag()`                                                                    |
| setExtra()             | `Sentry.setExtra()`                                                                  |
| setContext()           | `Sentry.setContext()`                                                                |
| configureScope()       | REMOVED - Scopes are now the unit of concurrency                                     |
| run()                  | `Sentry.withScope()` or `Sentry.withIsolationScope()`                                |
| getIntegration()       | `client.getIntegration()`                                                            |
| startTransaction()     | `Sentry.startSpan()`, `Sentry.startInactiveSpan()` or `Sentry.startSpanManual()`     |
| traceHeaders()         | REMOVED - The closest equivalent is now `spanToTraceHeader(getActiveSpan())`         |
| captureSession()       | `Sentry.captureSession()`                                                            |
| startSession()         | `Sentry.startSession()`                                                              |
| endSession()           | `Sentry.endSession()`                                                                |
| shouldSendDefaultPii() | REMOVED - The closest equivalent is `Sentry.getClient().getOptions().sendDefaultPii` |

The `Hub` constructor is also deprecated and will be removed in the next major version. If you are creating Hubs for multi-client use like so:

```TypeScript
// OLD
const hub = new Hub();
hub.bindClient(client);
makeMain(hub);
```

instead initialize the client as follows:

```TypeScript
// NEW
Sentry.withIsolationScope(() => {
  Sentry.setCurrentClient(client);
  client.init();
});
```

If you are using the Hub to capture events like so:

```TypeScript
// OLD
const client = new Client();
const hub = new Hub(client);
hub.captureException();
```

instead capture isolated events as follows:

```TypeScript
// NEW
const client = new Client();
const scope = new Scope();
scope.setClient(client);
scope.captureException();
```

- [Deprecate `addGlobalEventProcessor` in favor of `addEventProcessor`](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-addglobaleventprocessor-in-favor-of-addeventprocessor)

*Deprecation introduced in `7.85.0`.*

Instead of using `addGlobalEventProcessor`, you should use `addEventProcessor` which does not add the event processor globally, but to the current client.

For the vast majority of cases, the behavior of these should be the same. Only in the case where you have multiple clients will this differ - but you'll likely want to add event processors per-client then anyhow, not globally.

In v8, we will remove the global event processors overall, as that allows us to avoid keeping global state that is not necessary.

- [Deprecate `configureScope` in favor of using `getCurrentScope()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-configurescope-in-favor-of-using-getcurrentscope)

*Deprecation introduced in `7.89.0`.*

Instead of updating the scope in a callback via `configureScope()`, you should access it via `getCurrentScope()` and configure it directly:

```js
Sentry.getCurrentScope().setTag("xx", "yy");
```

- [Deprecate `pushScope` & `popScope` in favor of `withScope`](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-pushscope--popscope-in-favor-of-withscope)

*Deprecation introduced in `7.89.0`.*

Instead of manually pushing/popping a scope, you should use `Sentry.withScope(callback: (scope: Scope))` instead.

- [Deprecate arguments for `startSpan()` APIs](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-arguments-for-startspan-apis)

*Deprecation introduced in `7.93.0`.*

In v8, the API to start a new span will be reduced from the currently available options. Going forward, only these arguments will be passable to `startSpan()`, `startSpanManual()` and `startInactiveSpan()`:

* `name`
* `attributes`
* `origin`
* `op`
* `startTime`
* `scope`

- [Deprecate `startTransaction()` & `span.startChild()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-starttransaction--spanstartchild)

*Deprecation introduced in `7.93.0`.*

In v8, the old performance API `startTransaction()` (and `hub.startTransaction()`), as well as `span.startChild()`, will be removed. Instead, use the new performance APIs:

* `startSpan()`
* `startSpanManual()`
* `startInactiveSpan()`

- [Deprecated `transactionContext` passed to `tracesSampler`](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecated-transactioncontext-passed-to-tracessampler)

*Deprecation introduced in `7.100.0`.*

Instead of an `transactionContext` being passed to the `tracesSampler` callback, the callback will directly receive `name` and `attributes` going forward. You can use these to make your sampling decisions, while `transactionContext` will be removed in `8.x`. Note that the `attributes` are only the attributes at span creation time, and some attributes may only be set later during the span lifecycle (and thus not be available during sampling).

- [Deprecate `scope.getSpan()` and `scope.setSpan()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-scopegetspan-and-scopesetspan)

*Deprecation introduced in `7.93.0`.*

Instead, you can get the currently active span via `Sentry.getActiveSpan()`. Setting a span on the scope happens automatically when you use the new performance APIs `startSpan()` and `startSpanManual()`.

- [Deprecate `scope.getTransaction()` and `getActiveTransaction()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/migration/v7-to-v8/v7-deprecations.md#deprecate-scopegettransaction-and-getactivetransaction)

*Deprecation introduced in `7.93.0`.*

Instead, you should not rely on the active transaction, but just use `startSpan()` APIs, which handle this for you.

