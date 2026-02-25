---
title: 'Options | Sentry for Next.js'
description: 'The DSN tells the SDK where to send the events. If this is not set, the SDK will not send any events. Learn more about DSN utilization.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options

# Options | Sentry for Next.js

## [Available Options](https://docs.sentry.io/platforms/javascript/configuration/options.md#available-options)

## [Core Options](https://docs.sentry.io/platforms/javascript/configuration/options.md#core-options)

- [dsn](https://docs.sentry.io/platforms/javascript/configuration/options.md#dsn)

| Type | `string` |
| ---- | -------- |

The DSN tells the SDK where to send the events. If this is not set, the SDK will not send any events. Learn more about [DSN utilization](https://docs.sentry.io/product/sentry-basics/dsn-explainer.md#dsn-utilization).

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
});
```

- [orgId](https://docs.sentry.io/platforms/javascript/configuration/options.md#orgId)

| Type              | `` `${number}` \| number `` |
| ----------------- | --------------------------- |
| Only available on | `Server`                    |

The organization ID for your Sentry project.

The SDK will try to extract the organization ID from the DSN. If it cannot be found, or if you need to override it, you can provide the ID with this option. The organization ID is used for trace propagation and features like `strictTraceContinuation`.

The organization ID is used for features like [strict trace continuation](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#strictTraceContinuation).

- [debug](https://docs.sentry.io/platforms/javascript/configuration/options.md#debug)

| Type    | `boolean` |
| ------- | --------- |
| Default | `false`   |

Turns debug mode on or off. If debug is enabled SDK will attempt to print out useful debugging information about what the SDK is doing.

- [release](https://docs.sentry.io/platforms/javascript/configuration/options.md#release)

| Type | `string` |
| ---- | -------- |

Sets the release. Release names are strings, but some formats are detected by Sentry and might be rendered differently. Learn more about how to send release data so Sentry can tell you about regressions between releases and identify the potential source in [the releases documentation](https://docs.sentry.io/product/releases.md) or the [sandbox](https://sandbox.sentry.io/?scenario=releases\&projectSlug=react\&source=docs).

On the server, the SDK will try to read this value from the `SENTRY_RELEASE` environment variable.

In the browser, the SDK will try to read this value from `window.SENTRY_RELEASE.id` if available.

- [environment](https://docs.sentry.io/platforms/javascript/configuration/options.md#environment)

| Type    | `string`     |
| ------- | ------------ |
| Default | `production` |

Sets the environment. Defaults to `development` or `production` depending on whether the application is packaged.

Environments tell you where an error occurred, whether that's in your production system, your staging server, or elsewhere.

Sentry automatically creates an environment when it receives an event with the environment parameter set.

Environments are case-sensitive. The environment name can't contain newlines, spaces or forward slashes, can't be the string "None", or exceed 64 characters. You can't delete environments, but you can hide them.

- [tunnel](https://docs.sentry.io/platforms/javascript/configuration/options.md#tunnel)

| Type | `string` |
| ---- | -------- |

Sets the URL that will be used to transport captured events. This can be used to work around ad-blockers or to have more granular control over events sent to Sentry. Adding your DSN is still required when using this option so necessary attributes can be set on the generated Sentry data. This option **requires the implementation** of a custom server endpoint. Learn more and find examples in [Dealing with Ad-Blockers](https://docs.sentry.io/platforms/javascript/troubleshooting.md#dealing-with-ad-blockers).

- [sendDefaultPii](https://docs.sentry.io/platforms/javascript/configuration/options.md#sendDefaultPii)

| Type    | `boolean` |
| ------- | --------- |
| Default | `false`   |

Set this option to `true` to send default PII data to Sentry. Among other things, enabling this will enable automatic IP address collection on events.

- [maxBreadcrumbs](https://docs.sentry.io/platforms/javascript/configuration/options.md#maxBreadcrumbs)

| Type    | `number` |
| ------- | -------- |
| Default | `100`    |

This variable controls the total amount of breadcrumbs that should be captured. You should be aware that Sentry has a [maximum payload size](https://develop.sentry.dev/sdk/data-model/envelopes/#size-limits) and any events exceeding that payload size will be dropped.

- [attachStacktrace](https://docs.sentry.io/platforms/javascript/configuration/options.md#attachStacktrace)

| Type    | `boolean` |
| ------- | --------- |
| Default | `false`   |

When enabled, stack traces are automatically attached to all messages logged. Stack traces are always attached to exceptions; however, when this option is set, stack traces are also sent with messages. This option, for instance, means that stack traces appear next to all messages captured with `Sentry.captureMessage()`.

Grouping in Sentry is different for events with stack traces and without. As a result, you will get new groups as you enable or disable this flag for certain events.

- [serverName](https://docs.sentry.io/platforms/javascript/configuration/options.md#serverName)

| Type              | `string` |
| ----------------- | -------- |
| Only available on | `Server` |

This option can be used to supply a server name. When provided, the name of the server is sent along and persisted in the event. For many integrations, the server name actually corresponds to the device hostname, even in situations where the machine is not actually a server.

Most SDKs will attempt to auto-discover this value.

- [initialScope](https://docs.sentry.io/platforms/javascript/configuration/options.md#initialScope)

| Type | `CaptureContext` |
| ---- | ---------------- |

Data to be set to the initial scope. Initial scope can be defined either as an object or a callback function, as shown below.

```javascript
// Using an object
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  initialScope: {
    tags: { "my-tag": "my value" },
    user: { id: 42, email: "john.doe@example.com" },
  },
});

// Using a callback function
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  initialScope: (scope) => {
    scope.setTags({ a: "b" });
    return scope;
  },
});
```

- [maxValueLength](https://docs.sentry.io/platforms/javascript/configuration/options.md#maxValueLength)

| Type | `number` |
| ---- | -------- |

Maximum number of characters every string property on events sent to Sentry can have before it will be truncated.

- [normalizeDepth](https://docs.sentry.io/platforms/javascript/configuration/options.md#normalizeDepth)

| Type    | `number` |
| ------- | -------- |
| Default | `3`      |

Sentry SDKs normalize any contextual data to a given depth. Any data beyond this depth will be trimmed and marked using its type instead (`[Object]` or `[Array]`), without walking the tree any further. By default, walking is performed three levels deep.

- [normalizeMaxBreadth](https://docs.sentry.io/platforms/javascript/configuration/options.md#normalizeMaxBreadth)

| Type    | `number` |
| ------- | -------- |
| Default | `1000`   |

This is the maximum number of properties or entries that will be included in any given object or array when the SDK is normalizing contextual data. Any data beyond this depth will be dropped.

- [enabled](https://docs.sentry.io/platforms/javascript/configuration/options.md#enabled)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

Specifies whether this SDK should send events to Sentry. Setting this to `enabled: false` doesn't prevent all overhead from Sentry instrumentation. To disable Sentry completely, depending on environment, call `Sentry.init` conditionally.

- [sendClientReports](https://docs.sentry.io/platforms/javascript/configuration/options.md#sendClientReports)

| Type    | `boolean` |
| ------- | --------- |
| Default | `true`    |

Set this option to `false` to disable sending of client reports. Client reports are a protocol feature that let clients send status reports about themselves to Sentry. They are currently mainly used to emit outcomes for events that were never sent.

- [includeLocalVariables](https://docs.sentry.io/platforms/javascript/configuration/options.md#includeLocalVariables)

| Type              | `boolean` |
| ----------------- | --------- |
| Default           | `false`   |
| Only available on | `Server`  |

Set this option to `true` to add stack local variables to stack traces.

For more advanced configuration options, see the documentation on the [Local Variables integration options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/localvariables.md).

- [integrations](https://docs.sentry.io/platforms/javascript/configuration/options.md#integrations)

| Type    | `Array<Integration> \| (integrations: Array<Integration>) => Array<Integration>` |
| ------- | -------------------------------------------------------------------------------- |
| Default | `[]`                                                                             |

Pass additional integrations that should be initialized with the SDK. Integrations are pieces of code that can be used to extend the SDK's functionality. They can be used to add custom event processors, context providers, or to hook into the SDK's lifecycle.

See [integration docs](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md) for more information.

- [defaultIntegrations](https://docs.sentry.io/platforms/javascript/configuration/options.md#defaultIntegrations)

| Type | `undefined \| false` |
| ---- | -------------------- |

This can be used to disable integrations that are added by default. When set to `false`, no default integrations are added.

See [integration docs](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations) to see how you can modify the default integrations.

- [beforeBreadcrumb](https://docs.sentry.io/platforms/javascript/configuration/options.md#beforeBreadcrumb)

| Type | `(breadcrumb: Breadcrumb, hint?: BreadcrumbHint) => Breadcrumb \| null` |
| ---- | ----------------------------------------------------------------------- |

This function is called with a breadcrumb object before the breadcrumb is added to the scope. When nothing is returned from the function, the breadcrumb is dropped. To pass the breadcrumb through, return the first argument, which contains the breadcrumb object. The callback gets a second argument (called a "hint") which contains the original object from which the breadcrumb was created to further customize what the breadcrumb should look like.

- [transport](https://docs.sentry.io/platforms/javascript/configuration/options.md#transport)

| Type | `(transportOptions: TransportOptions) => Transport` |
| ---- | --------------------------------------------------- |

The JavaScript SDK uses a transport to send events to Sentry. On modern browsers, most transports use the browsers' fetch API to send events. Transports will drop an event if it fails to send due to a lack of connection.

In the browser, a `fetch`-based transport is used by default.

On the server, a `https`-based transport is used by default.

- [transportOptions](https://docs.sentry.io/platforms/javascript/configuration/options.md#transportOptions)

| Type | `TransportOptions` |
| ---- | ------------------ |

Options used to configure the transport. This is an object with the following possible optional keys:

**Options for the node `httpTransport` transport:**

* `headers`: An object containing headers to be sent with every request.
* `proxy`: A proxy used for outbound requests. Can be http or https.
* `caCerts`: A path or list of paths to a CA certificate, or a buffer of CA certificates.
* `httpModule`: A custom HTTP module to use for requests. Defaults to the native `http` and `https` modules.
* `keepAlive`: Determines whether to keep the socket alive between requests. Defaults to `false`.

**Options for the browser `fetch` transport:**

* `headers`: An object containing headers to be sent with every request.
* `fetchOptions`: An object containing options to be passed to the `fetch` call. Used by the SDK's fetch transport.

- [shutdownTimeout](https://docs.sentry.io/platforms/javascript/configuration/options.md#shutdownTimeout)

| Type              | `number` |
| ----------------- | -------- |
| Default           | `2000`   |
| Only available on | `Server` |

Controls how many seconds to wait before shutting down. Sentry SDKs send events from a background queue. This queue is given a certain amount to drain pending events. The default is SDK specific but typically around two seconds. Setting this value too low may cause problems for sending events from command line applications. Setting the value too high will cause the application to block for a long time for users experiencing network connectivity problems.

- [disableInstrumentationWarnings](https://docs.sentry.io/platforms/javascript/configuration/options.md#disableInstrumentationWarnings)

| Type              | `boolean` |
| ----------------- | --------- |
| Default           | `false`   |
| Only available on | `Server`  |

Depending on your setup, the Sentry SDK will try to detect if it has been incorrectly set up. This can result in warnings like this being logged:

> \[Sentry] < libraryName > is not instrumented. This is likely because you required/imported < libraryName > before calling `Sentry.init()`.

Or

> \[Sentry] < libraryName > is not instrumented. Please make sure to initialize Sentry in a separate file that you \`--import\` when running node, see: < docs link >.

This means the SDK detected that the library hasn't been wrapped for automatic performance instrumentation. This may result in some spans not being reported correctly. If this is not affecting you (for example because the warning is a false positive or you do not care about these specific spans), you can disable this warning by setting this option to `true`.

## [Error Monitoring Options](https://docs.sentry.io/platforms/javascript/configuration/options.md#error-monitoring-options)

- [sampleRate](https://docs.sentry.io/platforms/javascript/configuration/options.md#sampleRate)

| Type    | `number` |
| ------- | -------- |
| Default | `1.0`    |

Configures the sample rate for error events, in the range of `0.0` to `1.0`. The default is `1.0`, which means that 100% of error events will be sent. If set to `0.1`, only 10% of error events will be sent. Events are picked randomly.

- [beforeSend](https://docs.sentry.io/platforms/javascript/configuration/options.md#beforeSend)

| Type | `(event: Event, hint: EventHint) => Event \| null` |
| ---- | -------------------------------------------------- |

This function is called with an SDK-specific message or error event object, and can return a modified event object, or `null` to skip reporting the event. This can be used, for instance, for manual PII stripping before sending.

By the time `beforeSend` is executed, all scope data has already been applied to the event. Further modification of the scope won't have any effect.

- [enhanceFetchErrorMessages](https://docs.sentry.io/platforms/javascript/configuration/options.md#enhanceFetchErrorMessages)

| Available since | `10.34.0`                            |
| --------------- | ------------------------------------ |
| Type            | `'always' \| 'report-only' \| false` |
| Default         | `always`                             |

Controls whether fetch error messages are enhanced by appending the request’s hostname. When enabled, generic fetch errors like "Failed to fetch" will be enhanced to include the hostname (e.g., "Failed to fetch (example.com)") to provide better context in Sentry.

Available options:

* `'always'` (default): Modifies the actual error message directly. This may break third-party packages that rely on exact message matching (e.g., `is-network-error`, `p-retry`).
* `'report-only'`: Only enhances the message when sending to Sentry. The original error message remains unchanged, preserving compatibility with third-party packages that also check error messages.
* `false`: Disables hostname enhancement completely.

- [ignoreErrors](https://docs.sentry.io/platforms/javascript/configuration/options.md#ignoreErrors)

| Type    | `Array<string \| RegExp>` |
| ------- | ------------------------- |
| Default | `[]`                      |

A list of strings or regex patterns that match error messages that shouldn't be sent to Sentry. Messages that match these strings or regular expressions will be filtered out before they're sent to Sentry. When using strings, partial matches will be filtered out, so if you need to filter by exact match, use regex patterns instead. By default, all errors are sent.

- [denyUrls](https://docs.sentry.io/platforms/javascript/configuration/options.md#denyUrls)

| Type              | `Array<string \| RegExp>` |
| ----------------- | ------------------------- |
| Default           | `[]`                      |
| Only available on | `Client`                  |

An array of strings or regex patterns that match the URLs of scripts where errors have been created. Errors that have been created on these URLs won't be sent to Sentry. If you use this option, errors will not be sent when the top stack frame file URL contains or matches at least one entry in the `denyUrls` array. All string entries in the array will be matched with `stackFrameUrl.contains(entry)`, while all RegEx entries will be matched with `stackFrameUrl.match(entry)`.

This option checks the source file URL in the stack trace, not the HTTP URL where the error was reported. For more fine grained filtering please refer to [beforeSend](https://docs.sentry.io/platforms/javascript/guides/react/configuration/options.md#beforeSend).

This matching logic applies to captured exceptions not raw message events. By default, all errors are sent.

- [allowUrls](https://docs.sentry.io/platforms/javascript/configuration/options.md#allowUrls)

| Type              | `Array<string \| RegExp>` |
| ----------------- | ------------------------- |
| Default           | `[]`                      |
| Only available on | `Client`                  |

An array of strings or regex patterns that match the URLs of scripts where errors have been created. Only errors that have been created on these URLs will be sent to Sentry. If you use this option, errors will only be sent when the top stack frame file URL contains or matches at least one entry in the allowUrls array. All string entries in the array will be matched with `stackFrameUrl.contains(entry)`, while all RegEx entries will be matched with `stackFrameUrl.match(entry)`.

For example, if you add `'foo.com'` to the array, errors created on `https://bar.com/myfile/foo.com` will be captured because URL will be matched with "contains" logic and the last segment of the URL contains `foo.com`.

This matching logic applies for captured exceptions, not raw message events. By default, all errors are sent.

If your scripts are loaded from `cdn.example.com` and your site is `example.com`, you can set `allowUrls` to the following to exclusively capture errors being created in scripts in these locations:

```javascript
Sentry.init({
  allowUrls: [/https?:\/\/((cdn|www)\.)?example\.com/],
});
```

## [Tracing Options](https://docs.sentry.io/platforms/javascript/configuration/options.md#tracing-options)

- [tracesSampleRate](https://docs.sentry.io/platforms/javascript/configuration/options.md#tracesSampleRate)

| Type | `number` |
| ---- | -------- |

A number between `0` and `1`, controlling the percentage chance a given transaction will be sent to Sentry. (`0` represents 0% while `1` represents 100%.) Applies equally to all transactions created in the app. Either this or `tracesSampler` must be defined to enable tracing.

- [tracesSampler](https://docs.sentry.io/platforms/javascript/configuration/options.md#tracesSampler)

| Type | `(samplingContext: SamplingContext) => number \| boolean` |
| ---- | --------------------------------------------------------- |

A function responsible for determining the percentage chance a given transaction will be sent to Sentry. It will automatically be passed information about the transaction and the context in which it's being created, and must return a number between `0` (0% chance of being sent) and `1` (100% chance of being sent). Can also be used for filtering transactions, by returning 0 for those that are unwanted. Either this or `tracesSampleRate` must be defined to enable tracing.

The `samplingContext` object passed to the function has the following properties:

* `parentSampled`: The sampling decision of the parent transaction. This is `true` if the parent transaction was sampled, and `false` if it was not.
* `name`: The name of the span as it was started.
* `attributes`: The initial attributes of the span.
  <!-- -->
  * `normalizedRequest`: Request information of the currently active HTTP server request, if applicable.

- [tracePropagationTargets](https://docs.sentry.io/platforms/javascript/configuration/options.md#tracePropagationTargets)

| Type | `Array<string \| RegExp>` |
| ---- | ------------------------- |

An optional property that controls which downstream services receive tracing data, in the form of a `sentry-trace` and a `baggage` header attached to any outgoing HTTP requests.

The option may contain a list of strings or regex against which the URLs of outgoing requests are matched. If one of the entries in the list matches the URL of an outgoing request, trace data will be attached to that request. String entries do not have to be full matches, meaning the URL of a request is matched when it *contains* a string provided through the option.

On the browser, all outgoing requests to the same origin will be propagated by default.

On the server, all outgoing requests will be propagated by default.

If you want to disable trace propagation, you can set this option to `[]`.

- [strictTraceContinuation](https://docs.sentry.io/platforms/javascript/configuration/options.md#strictTraceContinuation)

| Type              | `boolean` |
| ----------------- | --------- |
| Default           | `false`   |
| Only available on | `Server`  |

If set to `true`, the SDK will only continue a trace if the organization ID of the incoming trace found in the `baggage` header matches the organization ID of the current Sentry client.

The client's organization ID is extracted from the DSN or can be set with the [`orgId` option](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#orgId).

If the organization IDs do not match, the SDK will start a new trace instead of continuing the incoming one. This is useful to prevent traces of unknown third-party services from being continued in your application.

- [beforeSendTransaction](https://docs.sentry.io/platforms/javascript/configuration/options.md#beforeSendTransaction)

| Type | `(event: TransactionEvent, hint: EventHint) => TransactionEvent \| null` |
| ---- | ------------------------------------------------------------------------ |

This function is called with a transaction event object, and can return a modified transaction event object, or `null` to skip reporting the event. This can be used, for instance, for manual PII stripping before sending.

- [beforeSendSpan](https://docs.sentry.io/platforms/javascript/configuration/options.md#beforeSendSpan)

| Type | `(span: SpanJSON) => SpanJSON` |
| ---- | ------------------------------ |

This function is called with a serialized span object, and can return a modified span object. This might be useful for manually stripping PII from spans. This function is called for root spans as well as for all child spans. If you want to drop the root span, including all of its child spans, use [`beforeSendTransaction`](https://docs.sentry.io/platforms/javascript/configuration/options.md#beforeSendTransaction) instead.

Please note that the `span` you receive as an argument is a serialized object, not a `Span` class instance.

- [ignoreTransactions](https://docs.sentry.io/platforms/javascript/configuration/options.md#ignoreTransactions)

| Type    | `Array<string \| RegExp>` |
| ------- | ------------------------- |
| Default | `[]`                      |

A list of strings or regex patterns that match transaction names that shouldn't be sent to Sentry. Transactions that match these strings or regular expressions will be filtered out before they're sent to Sentry. When using strings, partial matches will be filtered out, so if you need to filter by exact match, use regex patterns instead. By default, transactions spanning typical API health check requests are filtered out.

- [ignoreSpans](https://docs.sentry.io/platforms/javascript/configuration/options.md#ignoreSpans)

| Available since | `10.2.0`                                                                      |
| --------------- | ----------------------------------------------------------------------------- |
| Type            | `Array<string \| RegExp \| {name?: string \| RegExp, op?: string \| RegExp}>` |
| Default         | `[]`                                                                          |

A list of strings or regex patterns matching span names that shouldn't be sent to Sentry. When using strings, partial matches will be filtered out, so if you need to filter by exact match, use regex patterns instead. You can also provide an object with a `name` and `op` property to match both the span name and the operation name. Note that at least `name` or `op` must be provided.

If a root span matches any of the specified patterns, the entire local trace will be dropped. If a child span matches, its children will be reparented to the dropped span's parent span.

By default, no spans are ignored.

Here are some predefined matches for common spans to get you started:

```javascript
Sentry.init({
  ignoreSpans: [
    // Browser connection events
    { op: /^browser\.(cache|connect|DNS)$/ },

    // Fonts
    { op: "resource.other", name: /.+\.(woff2|woff|ttf|eot)$/ },

    // CSS files
    { op: "resource.link", name: /.+\.css.*$/ },

    // JS files
    { op: /resource\.(link|script)/, name: /.+\.js.*$/ },

    // Images
    {
      op: /resource\.(other|img)/,
      name: /.+\.(png|svg|jpe?g|gif|bmp|tiff?|webp|avif|heic?|ico).*$/,
    },

    // Measure spans
    { op: "measure" },
  ],
});
```

- [propagateTraceparent](https://docs.sentry.io/platforms/javascript/configuration/options.md#propagateTraceparent)

| Available since | `10.10.0` |
| --------------- | --------- |
| Type            | `boolean` |
| Default         | `false`   |

If set to `true`, the SDK adds the [W3C `traceparent` header](https://www.w3.org/TR/trace-context/) to outgoing Http requests made via `fetch` or `XMLHttpRequest`. This header is attached in addition to the `sentry-trace` and `baggage` headers. Set this option to `true` if your backend services are instrumented with e.g. OpenTelemetry or other W3C Trace Context compatible libraries and you want to continue traces from the client.

**Important:** Make sure that your backend services' CORS configuration allows the `traceparent` header. Otherwise, requests might be blocked. Use the [`tracePropagationTargets` option](https://docs.sentry.io/platforms/javascript/configuration/options.md#tracepropagationtargets) to control which requests the `traceparent` header is attached to. See [Dealing with CORS Issues](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/dealing-with-cors-issues.md) for more information.

## [Logs Options](https://docs.sentry.io/platforms/javascript/configuration/options.md#logs-options)

- [enableLogs](https://docs.sentry.io/platforms/javascript/configuration/options.md#enableLogs)

| Type    | `boolean` |
| ------- | --------- |
| Default | `false`   |

Set this option to `true` to enable log capturing in Sentry. Only when this is enabled will the `logger` APIs actually send logs to Sentry.

- [beforeSendLog](https://docs.sentry.io/platforms/javascript/configuration/options.md#beforeSendLog)

| Type | `(log: Log) => Log \| null` |
| ---- | --------------------------- |

This function is called with a log object, and can return a modified log object, or `null` to skip sending this log to Sentry. This can be used, for instance, for manual PII stripping before sending, or to add custom attributes to all logs.

## [Session Replay Options](https://docs.sentry.io/platforms/javascript/configuration/options.md#session-replay-options)

- [replaysSessionSampleRate](https://docs.sentry.io/platforms/javascript/configuration/options.md#replaysSessionSampleRate)

| Type              | `number` |
| ----------------- | -------- |
| Only available on | `Client` |

The sample rate for replays that begin recording immediately and last the entirety of the user's session. `1.0` collects all replays, and `0` collects none.

- [replaysOnErrorSampleRate](https://docs.sentry.io/platforms/javascript/configuration/options.md#replaysOnErrorSampleRate)

| Type              | `number` |
| ----------------- | -------- |
| Only available on | `Client` |

The sample rate for replays that are recorded when an error happens. This type of replay will record up to a minute of events prior to the error and continue recording until the session ends. `1.0` collects all sessions with an error, and `0` collects none.

## [Profiling Options](https://docs.sentry.io/platforms/javascript/configuration/options.md#profiling-options)

- [profileSessionSampleRate](https://docs.sentry.io/platforms/javascript/configuration/options.md#profileSessionSampleRate)

| Available since | `10.27.0` |
| --------------- | --------- |
| Type            | `number`  |

A number between `0` and `1` that sets the percentage of how many sessions should have profiling enabled. `1.0` enables profiling in every session, `0.5` enables profiling for 50% of the sessions, and `0` enables it for none. The sampling decision is made once at the beginning of a session. This option is required to enable profiling.

In a server environment, a profiling session starts when the Sentry SDK is initialized and stops when the service terminates. Therefore, the sampling decision is re-evaluated on service restart or redeployment.

In a browser environment, a profiling session corresponds to a user session. A user session starts with a new SDK initialization on page load and ends when the browser tab is closed.

- [profileLifecycle](https://docs.sentry.io/platforms/javascript/configuration/options.md#profileLifecycle)

| Available since | `10.27.0`             |
| --------------- | --------------------- |
| Type            | `"trace" \| "manual"` |
| Default         | `"manual"`            |

Determines how profiling sessions are controlled. It has two modes:

* `'manual'` (default): You control when profiling starts and stops using the `startProfiler()` and `stopProfiler()` functions. In this mode, profile sampling is only affected by `profileSessionSampleRate`.

  Read more about these functions in the [profiling API documentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling.md).
* `'trace'`: Profiling starts and stops automatically with transactions, as long as tracing is enabled. The profiler runs as long as there is at least one sampled transaction. In this mode, profiling is affected by both `profileSessionSampleRate` and your tracing sample rate (`tracesSampleRate` or `tracesSampler`).

- [profilesSampleRate](https://docs.sentry.io/platforms/javascript/configuration/options.md#profilesSampleRate)

| Type | `number` |
| ---- | -------- |

**Deprecated:** Use `profileSessionSampleRate` instead to configure continuous profiling from version 10.27.0 onwards.

A number between `0` and `1`, controlling the percentage chance a given sampled transaction will be profiled. (`0` represents 0% while `1` represents 100%.) Applies equally to all transactions created in the app. This is relative to the tracing sample rate - e.g. `0.5` means 50% of sampled transactions will be profiled.

