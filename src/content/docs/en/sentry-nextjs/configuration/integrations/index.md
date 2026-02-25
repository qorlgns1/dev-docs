---
title: 'Integrations | Sentry for Next.js'
description: 'The Sentry SDK uses integrations to hook into the functionality of popular libraries to automatically instrument your application and give you the bes...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations

# Integrations | Sentry for Next.js

The Sentry SDK uses integrations to hook into the functionality of popular libraries to automatically instrument your application and give you the best data out of the box.

Integrations automatically add error instrumentation, performance instrumentation, and/or extra context information to your application. Some are enabled by default, but you can disable them or modify their settings.

Next.js can operate within three runtimes: the Node.js.js runtime, the browser runtime, and the Edge runtime. However, it's important to note that not all integrations are compatible with all of these runtimes.

Depending on whether an integration enhances the functionality of a particular runtime, such as the BrowserTracing integration for the browser runtime or the RequestData integration for the Node.js.js runtime, you can only include these integrations in their respective configuration files:

* For the browser runtime, add integrations to `instrumentation-client.(js|ts)`.
* For Node.js.js, add integrations to your Sentry setup in `instrumentation.(js|ts)`.
* For the Edge runtime, add integrations to your Sentry setup in `instrumentation.(js|ts)`.

- [Common Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#common-integrations)

|                                                                                                                                           | **Auto Enabled** | **Errors** | **Tracing** | **Additional Context** |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------- | ----------- | ---------------------- |
| [`dedupeIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/dedupe.md)                     | ✓                | ✓          |             |                        |
| [`functionToStringIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/functiontostring.md) | ✓                |            |             |                        |
| [`inboundFiltersIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/inboundfilters.md)     | ✓                | ✓          |             |                        |
| [`linkedErrorsIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/linkederrors.md)         | ✓                | ✓          |             |                        |
| [`captureConsoleIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/captureconsole.md)     |                  |            |             | ✓                      |
| [`extraErrorDataIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/extraerrordata.md)     |                  |            |             | ✓                      |
| [`rewriteFramesIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/rewriteframes.md)       |                  | ✓          |             |                        |

- [Browser Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#browser-integrations)

|                                                                                                                                             | **Auto Enabled** | **Errors** | **Tracing** | **Replay** | **Additional Context** |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------- | ----------- | ---------- | ---------------------- |
| [`breadcrumbsIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md)             | ✓                |            |             |            | ✓                      |
| [`browserApiErrorsIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors.md)   | ✓                | ✓          |             |            |                        |
| [`browserSessionIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsersession.md)       | ✓                |            |             |            | ✓                      |
| [`browserTracingIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsertracing.md)       | ✓                |            | ✓           |            | ✓                      |
| [`globalHandlersIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/globalhandlers.md)       | ✓                | ✓          |             |            |                        |
| [`httpContextIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpcontext.md)             | ✓                |            |             |            | ✓                      |
| [`browserProfilingIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserprofiling.md)   |                  |            | ✓           |            |                        |
| [`contextLinesIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/contextlines.md)           |                  | ✓          |             |            |                        |
| [`featureFlagsIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/featureflags.md)           |                  |            |             |            | ✓                      |
| [`graphqlClientIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphqlclient.md)         |                  |            |             |            | ✓                      |
| [`httpClientIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpclient.md)               |                  | ✓          |             |            |                        |
| [`launchDarklyIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/launchdarkly.md)           |                  |            |             |            | ✓                      |
| [`moduleMetadataIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/modulemetadata.md)       |                  |            |             |            | ✓                      |
| [`openFeatureIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openfeature.md)             |                  |            |             |            | ✓                      |
| [`replayCanvasIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/replaycanvas.md)           |                  |            |             | ✓          |                        |
| [`replayIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/replay.md)                       |                  |            |             | ✓          | ✓                      |
| [`reportingObserverIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/reportingobserver.md) |                  | ✓          |             |            |                        |
| [`statsigIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/statsig.md)                     |                  |            |             |            | ✓                      |
| [`supabaseIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md)                   |                  | ✓          | ✓           |            |                        |
| [`unleashIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unleash.md)                     |                  |            |             |            | ✓                      |

- [Server (Node.js, Edge) Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#server-nodejs-edge-integrations)

|                                                                                                                                 | **Auto Enabled** | **Errors** | **Tracing** | **Additional Context** |
| ------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------- | ----------- | ---------------------- |
| [`requestDataIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/requestdata.md) | ✓                |            | ✓           |                        |

- [Node.js Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#nodejs-integrations)

|                                                                                                                                                 | **Auto Enabled** | **Errors** | **Tracing** | **Additional Context** |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------- | ----------- | ---------------------- |
| [`amqplibIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/amqplib.md)                         | ✓                |            | ✓           |                        |
| [`consoleIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/console.md)                         | ✓                |            |             | ✓                      |
| [`contextLinesIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/contextlines.md)               | ✓                | ✓          |             |                        |
| [`genericPoolIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/genericpool.md)                 | ✓                |            | ✓           |                        |
| [`graphqlIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphql.md)                         | ✓                |            | ✓           |                        |
| [`httpIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md)                               | ✓                | ✓          | ✓           | ✓                      |
| [`kafkaIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/kafka.md)                             | ✓                |            | ✓           |                        |
| [`lruMemoizerIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/lrumemoizer.md)                 | ✓                |            | ✓           |                        |
| [`modulesIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/modules.md)                         | ✓                |            |             | ✓                      |
| [`mongoIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mongo.md)                             | ✓                |            | ✓           |                        |
| [`mongooseIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mongoose.md)                       | ✓                |            | ✓           |                        |
| [`mysqlIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mysql.md)                             | ✓                |            | ✓           |                        |
| [`mysql2Integration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mysql2.md)                           | ✓                |            | ✓           |                        |
| [`nodeContextIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodecontext.md)                 | ✓                |            |             | ✓                      |
| [`nativeNodeFetchIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodefetch.md)               | ✓                |            | ✓           | ✓                      |
| [`onUncaughtExceptionIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/onuncaughtexception.md) | ✓                | ✓          |             |                        |
| [`onUnhandledRejectionIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unhandledrejection.md) | ✓                | ✓          |             |                        |
| [`postgresIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/postgres.md)                       | ✓                |            | ✓           |                        |
| [`redisIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/redis.md)                             | ✓                |            | ✓           |                        |
| [`requestDataIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/requestdata.md)                 | ✓                |            | ✓           |                        |
| [`tediousIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/tedious.md)                         | ✓                |            | ✓           |                        |
| [`dataloaderIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/dataloader.md)                   | ✓                |            | ✓           |                        |
| [`childProcessIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/childProcess.md)               | ✓                |            |             | ✓                      |
| [`prismaIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma.md)                           | ✓                |            | ✓           |                        |
| [`anrIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anr.md)                                 |                  | ✓          |             |                        |
| [`eventLoopBlockIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block.md)         |                  | ✓          |             |                        |
| [`extraErrorDataIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/extraerrordata.md)           |                  |            |             | ✓                      |
| [`fsIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/fs.md)                                   |                  |            | ✓           |                        |
| [`knexIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/knex.md)                               |                  |            | ✓           |                        |
| [`localVariablesIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/localvariables.md)           |                  | ✓          |             |                        |
| [`nodeProfilingIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodeprofiling.md)             |                  |            | ✓           |                        |
| [`trpcMiddleware`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/trpc.md)                                |                  | ✓          | ✓           | ✓                      |
| [`vercelAiIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/vercelai.md)                       | ✓                |            | ✓           | ✓                      |
| [`openAIIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md)                           | ✓                |            | ✓           |                        |
| [`anthropicAIIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md)                   | ✓                | ✓          | ✓           |                        |
| [`googleGenAIIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md)                | ✓                | ✓          | ✓           |                        |
| [`langChainIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langchain.md)                     | ✓                | ✓          | ✓           |                        |
| [`zodErrorsIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/zodErrors.md)                     |                  |            |             | ✓                      |
| [`pinoIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md)                               |                  | ✓          |             |                        |

- [Edge Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#edge-integrations)

|                                                                                                                                     | **Auto Enabled** | **Errors** | **Tracing** | **Additional Context** |
| ----------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------- | ----------- | ---------------------- |
| [`winterCGFetchIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/wintercgfetch.md) | ✓                |            | ✓           | ✓                      |
| [`vercelAiIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/vercelai.md)           |                  |            | ✓           |                        |

## [Modifying Default Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)

To disable system integrations, set `defaultIntegrations: false` when calling `init()`.

To override their settings, provide a new instance with your config to the `integrations` option. For example, to turn off browser capturing console calls:

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  integrations: [
    Sentry.breadcrumbsIntegration({
      console: false,
    }),
  ],

});
```

## [Adding an Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#adding-an-integration)

You can add additional integrations in your `init` call:

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.reportingObserverIntegration()],
});
```

Alternatively, you can add integrations via `Sentry.addIntegration()`. This is useful if you only want to enable an integration in a specific environment or if you want to load an integration later. For all other cases, we recommend you use the `integrations` option.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  integrations: [],
});

Sentry.addIntegration(Sentry.reportingObserverIntegration());
```

## [Lazy Loading Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#lazy-loading-integrations)

Lazy-loading lets you add pluggable integrations without increasing the initial bundle size. You can do this in two ways:

- [1. Dynamic Import (recommended)](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#1-dynamic-import-recommended)

You can add the integration with a dynamic import using `import()`. This method loads the integration from the npm package. To avoid running into issues with `import()`, you should use a bundler that supports dynamic imports. If you're using a tool like Vite for your project, the bundling process is probably already set up.

`instrumentation-client.ts`

```javascript
Sentry.init({
  // Note, Replay is NOT instantiated below:
  integrations: [],
});
```

Then, somewhere in your application, for example in a `useEffect` hook, you can lazy-load the Replay integration:

```javascript
import("@sentry/nextjs").then((lazyLoadedSentry) => {
  Sentry.addIntegration(lazyLoadedSentry.replayIntegration());
});
```

- [2. Load from CDN with `lazyLoadIntegration()`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#2-load-from-cdn-with-lazyloadintegration)

You can also lazy-load pluggable integrations via `Sentry.lazyLoadIntegration()`. This will attempt to load the integration from the Sentry CDN. Note that this function will reject if it fails to load the integration from the Sentry CDN, which can happen if a user has an ad-blocker or if there's a network problem. You should always make sure that rejections are handled for this function in your application.

```javascript
async function loadHttpClient() {
  const httpClientIntegration = await Sentry.lazyLoadIntegration(
    "httpClientIntegration",
  );
  Sentry.addIntegration(httpClientIntegration());
}
```

Lazy loading is available for the following integrations:

* `replayIntegration`
* `replayCanvasIntegration`
* `feedbackIntegration`
* `feedbackModalIntegration`
* `feedbackScreenshotIntegration`
* `captureConsoleIntegration`
* `contextLinesIntegration`
* `linkedErrorsIntegration`
* `dedupeIntegration`
* `extraErrorDataIntegration`
* `httpClientIntegration`
* `reportingObserverIntegration`
* `rewriteFramesIntegration`
* `browserProfilingIntegration`

## [Removing a Default Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#removing-a-default-integration)

If you only want to remove a single or some of the default integrations, instead of disabling all of them with `defaultIntegrations: false`, you can use the following syntax to filter out the ones you don't want.

This example removes the integration for adding breadcrumbs to the event, which is enabled by default:

```javascript
Sentry.init({
  // ...
  integrations: function (integrations) {
    // integrations will be all default integrations
    return integrations.filter(function (integration) {
      return integration.name !== "Breadcrumbs";
    });
  },
});
```

## [Custom Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#custom-integrations)

You can also create [custom integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/custom.md).

## [Available Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#available-integrations)

*
- [RequestData](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/requestdata.md)

  Adds data from incoming requests to transaction and error events that occur during request handling done by the backend. (default)

*
- [Amqplib](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/amqplib.md)

  Adds instrumentation for Amqplib. (default)

*
- [Anr](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anr.md)

  Capture events when the event loop is blocked and the application is no longer responding.

*
- [Anthropic](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md)

  Adds instrumentation for the Anthropic SDK.

*
- [Breadcrumbs](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md)

  Wraps native browser APIs to capture breadcrumbs. (default)

*
- [BrowserApiErrors](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors.md)

  Wraps native time and events APIs (\`setTimeout\`, \`setInterval\`, \`requestAnimationFrame\`, \`addEventListener/removeEventListener\`) in \`try/catch\` blocks to handle async exceptions. (default)

*
- [BrowserProfiling](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserprofiling.md)

  Capture profiling data for the Browser.

*
- [BrowserSession](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsersession.md)

  Track healthy Sessions in the Browser.

*
- [BrowserTracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsertracing.md)

  Capture performance data for the Browser.

*
- [CaptureConsole](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/captureconsole.md)

  Captures all Console API calls via \`captureException\` or \`captureMessage\`.

*
- [Child Process Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/childProcess.md)

  Adds instrumentation for child processes and worker threads (default)

*
- [Console](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/console.md)

  Capture console logs as breadcrumbs. (default)

*
- [Context](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodecontext.md)

  Capture context about the environment and the device that the client is running on, and add it to events. (default)

*
- [ContextLines](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/contextlines.md)

  Adds source code from inline JavaScript of the current page's HTML.

*
- [Dataloader](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/dataloader.md)

  Adds instrumentation for Dataloader.

*
- [Dedupe](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/dedupe.md)

  Deduplicate certain events to avoid receiving duplicate errors. (default)

*
- [Event Loop Block](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block.md)

  Monitor for blocked event loops in all threads of a Node.js application.

*
- [ExtraErrorData](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/extraerrordata.md)

  Extracts all non-native attributes from the error object and attaches them to the event as extra data.

*
- [FileSystem](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/fs.md)

  Adds instrumentation for filesystem operations.

*
- [FunctionToString](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/functiontostring.md)

  Allows the SDK to provide original functions and method names, even when those functions or methods are wrapped by our error or breadcrumb handlers. (default)

*
- [Generic Feature Flags Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/featureflags.md)

  Learn how to attach custom feature flag data to Sentry error events.

*
- [Generic Pool](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/genericpool.md)

  Adds instrumentation for Generic Pool. (default)

*
- [GlobalHandlers](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/globalhandlers.md)

  Attaches global handlers to capture uncaught exceptions and unhandled rejections. (default)

*
- [Google Gen AI](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md)

  Adds instrumentation for Google Gen AI SDK.

*
- [GraphQL](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphql.md)

  Adds instrumentation for GraphQL. (default)

*
- [GraphQLClient](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphqlclient.md)

  Enhance spans and breadcrumbs with data from GraphQL requests.

*
- [Http](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md)

  Capture spans & breadcrumbs for http requests. (default)

*
- [HttpClient](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpclient.md)

  Captures errors on failed requests from Fetch and XHR and attaches request and response information.

*
- [HttpContext](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpcontext.md)

  Attaches HTTP request information, such as URL, user-agent, referrer, and other headers to the event. (default)

*
- [InboundFilters](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/inboundfilters.md)

  Allows you to ignore specific errors based on the type, message, or URLs in a given exception. (default)

*
- [Kafka](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/kafka.md)

  Adds instrumentation for KafkaJS. (default)

*
- [Knex](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/knex.md)

  Adds instrumentation for Knex.

*
- [LangChain](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langchain.md)

  Adds instrumentation for LangChain.

*
- [LangGraph](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md)

  Adds instrumentation for the LangGraph SDK.

*
- [LaunchDarkly](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/launchdarkly.md)

  Learn how to use Sentry with LaunchDarkly.

*
- [LinkedErrors](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/linkederrors.md)

  Allows you to configure linked errors. (default)

*
- [LocalVariables](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/localvariables.md)

  Add local variables to exception frames. (default)

*
- [LRU Memoizer](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/lrumemoizer.md)

  Adds instrumentation for LRU Memoizer. (default)

*
- [ModuleMetadata](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/modulemetadata.md)

  Adds module metadata to stack frames.

*
- [Modules](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/modules.md)

  Add node modules / packages to the event. (default)

*
- [MongoDB](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mongo.md)

  Adds instrumentation for MongoDB. (default)

*
- [Mongoose](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mongoose.md)

  Adds instrumentation for Mongoose. (default)

*
- [MySQL](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mysql.md)

  Adds instrumentation for MySQL. (default)

*
- [MySQL2](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mysql2.md)

  Adds instrumentation for MySQL2. (default)

*
- [NodeFetch](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodefetch.md)

  Capture spans & breadcrumbs for node fetch requests. (default)

*
- [NodeProfiling](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodeprofiling.md)

  Capture profiling data for Node.js applications.

*
- [OnUncaughtException](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/onuncaughtexception.md)

  Registers handlers to capture global uncaught exceptions. (default)

*
- [OnUnhandledRejection](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unhandledrejection.md)

  Registers handlers to capture global unhandled promise rejections. (default)

*
- [OpenAI](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md)

  Adds instrumentation for the OpenAI SDK.

*
- [OpenFeature](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openfeature.md)

  Learn how to use Sentry with OpenFeature.

*
- [Pino](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md)

  Capture logs and errors from Pino.

*
- [Postgres](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/postgres.md)

  Adds instrumentation for Postgres. (default)

*
- [Prisma](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma.md)

  Adds instrumentation for Prisma. (default)

*
- [Redis](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/redis.md)

  Adds instrumentation for Redis. (default)

*
- [Replay](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/replay.md)

  Capture a video-like reproduction of what was happening in the user's browser.

*
- [ReplayCanvas](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/replaycanvas.md)

  Capture session replays from HTML canvas elements.

*
- [ReportingObserver](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/reportingobserver.md)

  Captures the reports collected via the \`ReportingObserver\` interface and sends them to Sentry.

*
- [RewriteFrames](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/rewriteframes.md)

  Allows you to apply a transformation to each frame of the stack trace.

*
- [Statsig](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/statsig.md)

  Learn how to use Sentry with Statsig.

*
- [Supabase](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md)

  Adds instrumentation for Supabase client operations.

*
- [Tedious](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/tedious.md)

  Adds instrumentation for Tedious. (default)

*
- [trpcMiddleware](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/trpc.md)

  Capture spans & errors for tRPC handlers.

*
- [Unleash](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unleash.md)

  Learn how to use Sentry with Unleash.

*
- [Vercel AI](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/vercelai.md)

  Adds instrumentation for Vercel AI SDK.

*
- [WebWorker](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/webworker.md)

  Connect Web Workers with the SDK running on the main thread

*
- [WinterCGFetch](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/wintercgfetch.md)

  Creates spans and attaches tracing headers to fetch requests on edge runtimes. (default)

*
- [ZodErrors](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/zodErrors.md)

  Adds additional data to Zod validation errors.

## Pages in this section

- [RequestData](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/requestdata.md)
- [Amqplib](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/amqplib.md)
- [Anr](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anr.md)
- [Anthropic](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anthropic.md)
- [Breadcrumbs](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md)
- [BrowserApiErrors](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserapierrors.md)
- [BrowserProfiling](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserprofiling.md)
- [BrowserSession](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsersession.md)
- [BrowserTracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsertracing.md)
- [CaptureConsole](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/captureconsole.md)
- [Child Process Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/childProcess.md)
- [Console](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/console.md)
- [Context](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodecontext.md)
- [ContextLines](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/contextlines.md)
- [Dataloader](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/dataloader.md)
- [Dedupe](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/dedupe.md)
- [Event Loop Block](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block.md)
- [ExtraErrorData](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/extraerrordata.md)
- [FileSystem](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/fs.md)
- [FunctionToString](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/functiontostring.md)
- [Generic Feature Flags Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/featureflags.md)
- [Generic Pool](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/genericpool.md)
- [GlobalHandlers](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/globalhandlers.md)
- [Google Gen AI](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/google-genai.md)
- [GraphQL](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphql.md)
- [GraphQLClient](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/graphqlclient.md)
- [Http](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md)
- [HttpClient](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpclient.md)
- [HttpContext](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpcontext.md)
- [InboundFilters](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/inboundfilters.md)
- [Kafka](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/kafka.md)
- [Knex](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/knex.md)
- [LangChain](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langchain.md)
- [LangGraph](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/langgraph.md)
- [LaunchDarkly](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/launchdarkly.md)
- [LinkedErrors](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/linkederrors.md)
- [LocalVariables](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/localvariables.md)
- [LRU Memoizer](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/lrumemoizer.md)
- [ModuleMetadata](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/modulemetadata.md)
- [Modules](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/modules.md)
- [MongoDB](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mongo.md)
- [Mongoose](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mongoose.md)
- [MySQL](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mysql.md)
- [MySQL2](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mysql2.md)
- [NodeFetch](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodefetch.md)
- [NodeProfiling](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodeprofiling.md)
- [OnUncaughtException](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/onuncaughtexception.md)
- [OnUnhandledRejection](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unhandledrejection.md)
- [OpenAI](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openai.md)
- [OpenFeature](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openfeature.md)
- [Pino](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md)
- [Postgres](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/postgres.md)
- [Prisma](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma.md)
- [Prisma](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/prisma__v8.x.md)
- [Redis](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/redis.md)
- [Replay](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/replay.md)
- [ReplayCanvas](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/replaycanvas.md)
- [ReportingObserver](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/reportingobserver.md)
- [RewriteFrames](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/rewriteframes.md)
- [Statsig](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/statsig.md)
- [Supabase](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/supabase.md)
- [Tedious](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/tedious.md)
- [trpcMiddleware](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/trpc.md)
- [Unleash](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unleash.md)
- [Vercel AI](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/vercelai.md)
- [WebWorker](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/webworker.md)
- [WinterCGFetch](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/wintercgfetch.md)
- [ZodErrors](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/zodErrors.md)
- [Custom Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/custom.md)

