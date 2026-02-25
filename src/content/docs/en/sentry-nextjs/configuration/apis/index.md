---
title: 'APIs | Sentry for Next.js'
description: 'This page shows all available top-level APIs of the SDK. You can use these APIs as the primary way to:'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis

# APIs | Sentry for Next.js

This page shows all available top-level APIs of the SDK. You can use these APIs as the primary way to:

* Configure the SDK after initialization
* Manually capture different types of events
* Enrich events with additional data
* ... and more!

These APIs are functions that you can use as follows - they are all available on the top-level `Sentry` object:

```javascript
import * as Sentry from "@sentry/browser";

Sentry.setTag("tag", "value");
```

## [Available APIs](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#available-apis)

## [Core APIs](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#core-apis)

- [init](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#init)

```
function init(options: InitOptions): Client | undefined
```

Initialize the SDK with the given options. See<!-- --> <!-- -->[Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md) for the options you can pass to `init`.

- [getClient](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#getClient)

```
function getClient(): Client | undefined
```

Returns the currently active client.

- [setCurrentClient](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setCurrentClient)

```
function setCurrentClient(client: Client): void
```

Make the given client the current client. You do not need this if you use `init()`, this is only necessary if you are manually setting up a client.

- [lastEventId](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#lastEventId)

```
function lastEventId(): string | undefined
```

Returns the ID of the last sent error event. Note that this does not guarantee that this event ID exists, as it may have been dropped along the way.

- [flush](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#flush)

```
function flush(timeout?: number): Promise<boolean>
```

Parameters

timeout

```
number
```

Maximum time in ms the client should wait to flush its event queue. Omitting this parameter will cause the client to wait until all events are sent before resolving the promise.

Flushes all pending events.

- [isEnabled](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#isEnabled)

```
function isEnabled(): boolean
```

Returns true if the SDK is initialized & enabled.

- [close](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#close)

```
function close(timeout?: number): Promise<boolean>
```

Parameters

timeout

```
number
```

Maximum time in ms the client should wait to flush its event queue. Omitting this parameter will cause the client to wait until all events are sent before resolving the promise.

Flushes all pending events and disables the SDK. Note that this does not remove any listeners the SDK may have set up. After a call to `close`, the current client cannot be used anymore. It's important to only call `close` immediately before shutting down the application.

Alternatively, the [`flush`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#flush) method drains the event queue while keeping the client enabled for continued use.

- [addEventProcessor](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#addEventProcessor)

```
function addEventProcessor(processor: EventProcessor): void
```

Parameters

processor

```
(event: Event, hint: EventHint) => Event | null | Promise<Event | null>
```

Adds an event processor to the SDK. An event processor receives every event before it is sent to Sentry. It can either mutate the event (and return it) or return `null` to discard the event. Event processors can also return a promise, but it is recommended to use this only when necessary as it slows down event processing.

Event processors added via `Sentry.addEventProcessor()` will be applied to all events in your current request.

If you want to add an event processor that only applies to certain events, you can also add one to a scope as follows:

```javascript
Sentry.withScope((scope) => {
  scope.addEventProcessor((event) => {
    // this will only be applied to events captured within this scope
    return event;
  });

  Sentry.captureException(new Error("test"));
});
```

What is the difference to \`beforeSend\` / \`beforeSendTransaction\`?

`beforeSend` and `beforeSendTransaction` are guaranteed to be run last, after all other event processors, (which means they get the final version of the event right before it's sent, hence the name). Event processors added with `addEventProcessor` are run in an undetermined order, which means changes to the event may still be made after the event processor runs.

There can only be a single `beforeSend` / `beforeSendTransaction` processor, but you can add multiple event processors via `addEventProcessor()`.

- [addIntegration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#addIntegration)

```
function addIntegration(integration: Integration): void
```

Adds an integration to the SDK. This can be used to conditionally add integrations after `Sentry.init()` has been called. Note that it is recommended to pass integrations to `init` instead of calling this method, where possible.

See [Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md) for more information on how to use integrations.

- [lazyLoadIntegration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#lazyLoadIntegration)

Only available on Client

```
function lazyLoadIntegration(name: string, scriptNonce?: string): Promise<IntegrationFn>
```

Lazy load an integration. This expects the name to be e.g. `replayIntegration`. It will load the script from the CDN, and return a promise that resolves to the integration function, which can then be called and added to the SDK using `addIntegration`:

```javascript
Sentry.lazyLoadIntegration("replayIntegration")
  .then((replayIntegration) => {
    Sentry.addIntegration(replayIntegration());
  })
  .catch((error) => {
    // Make sure to handle errors here!
    // This rejects e.g. if the CDN bundle cannot be loaded
  });
```

If you use a bundler, using e.g. `const { replayIntegration } = await import('@sentry/browser')` is recommended instead.

See [Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md) for more information on how to use integrations.

## [Capturing Events](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#capturing-events)

- [captureException](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#captureException)

```
function captureException(
exception: unknown,
captureContext?: CaptureContext
): EventId
```

Parameters

exception\*

```
unknown
```

The exception to capture. For best results, pass an \`Error\` object but it accepts any kind of value.

captureContext

```
CaptureContext {
user?: User {
id?: string | number,
email?: string,
ip_address?: string,
username?: string,
}
level?: "fatal" | "error" | "warning" | "log" | "info" | "debug",
// Additional data that should be sent with the exception.
extra?: Record<string, unknown>,
// Additional tags that should be sent with the exception.
tags?: Record<string, string>,
contexts?: Record<string, Record<string, unknown>>,
fingerprint?: string[],
}
```

Optional additional data to attach to the Sentry event.

Capture an exception event and send it to Sentry. Note that you can pass not only `Error` objects, but also other objects as `exception` - in that case, the SDK will attempt to serialize the object for you, and the stack trace will be generated by the SDK and may be less accurate.

- [captureMessage](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#captureMessage)

```
function captureMessage(
message: string,
captureContext?: CaptureContext | SeverityLevel
): EventId
```

Parameters

message\*

```
string
```

The message to capture.

captureContext

```
CaptureContext {
user?: User {
id?: string | number,
email?: string,
ip_address?: string,
username?: string,
}
level?: "fatal" | "error" | "warning" | "log" | "info" | "debug",
// Additional data that should be sent with the exception.
extra?: Record<string, unknown>,
// Additional tags that should be sent with the exception.
tags?: Record<string, string>,
contexts?: Record<string, Record<string, unknown>>,
fingerprint?: string[],
}
```

Optional additional data to attach to the Sentry event.

Capture a message event and send it to Sentry. Optionally, instead of a `CaptureContext`, you can also pass a `SeverityLevel` as second argument, e.g. `"error"` or `"warning"`.

Messages show up as issues on your issue stream, with the message as the issue name.

## [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#enriching-events)

- [setTag](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setTag)

```
function setTag(key: string, value: string): void
```

Set a tag to be sent with Sentry events.

* Tag keys have a maximum length of 32 characters and can contain only letters (`a-zA-Z`), numbers (`0-9`), underscores (`_`), periods (`.`), colons (`:`), and dashes (`-`).
* Tag values have a maximum length of 200 characters and they cannot contain the newline (`\n`) character.

- [setTags](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setTags)

```
function setTags(tags: Record<string, string>): void
```

Set multiple tags to be sent with Sentry events.

- [setContext](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setContext)

```
function setContext(name: string, context: Record<string, unknown>): void
```

Set a context to be sent with Sentry events. Custom contexts allow you to attach arbitrary data to an event. You cannot search these, but they are viewable on the issue page - if you need to be able to filter for certain data, use [tags](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setTag) instead. Pass `null` as the context value to clear a previously set context.

There are no restrictions on context name. In the context object, all keys are allowed except for `type`, which is used internally.

By default, Sentry SDKs normalize nested structured context data up to three levels deep. Any data beyond this depth will be trimmed and marked using its type instead. To adjust this default, use the [`normalizeDepth`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#normalize-depth) SDK option.

Learn more about conventions for common contexts in the [contexts interface developer documentation](https://develop.sentry.dev/sdk/foundations/transport/event-payloads/contexts/).

Example

Context data is structured and can contain any data you want:

```javascript
Sentry.setContext("character", {
  name: "Mighty Fighter",
  age: 19,
  attack_type: "melee",
});
```

- [setExtra](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setExtra)

```
function setExtra(name: string, extra: unknown): void
```

Set additional data to be sent with Sentry events.

- [setExtras](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setExtras)

```
function setExtras(extras: Record<string, unknown>): void
```

Set multiple additional data entries to be sent with Sentry events.

- [setUser](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setUser)

```
function setUser(user: User | null): void
```

Parameters

user

```
User {
// Your internal identifier for the user
id?: string | number,
// Sentry is aware of email addresses and can display things such as Gravatars and unlock messaging capabilities
email?: string,
// Typically used as a better label than the internal id
username?: string,
// The user's IP address. If the user is unauthenticated, Sentry uses the IP address as a unique identifier for the user
ip_address?: string,
}
```

Set a user to be sent with Sentry events. Set to `null` to unset the user. In addition to the specified properties of the `User` object, you can also add additional arbitrary key/value pairs.

Capturing User IP-Addresses

On the server, the IP address will be inferred from the incoming HTTP request, if available. This is automatically done if you have configured `sendDefaultPii: true` in your [SDK configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#sendDefaultPii).

On the browser, if the users' `ip_address` is set to `"{{ auto }}"`, Sentry will infer the IP address from the connection between your app and Sentrys' server. `{{auto}}` is automatically set if you have configured `sendDefaultPii: true` in your [SDK configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#sendDefaultPii).

To ensure your users' IP addresses are never stored in your event data, you can go to your project settings, click on "Security & Privacy", and enable "Prevent Storing of IP Addresses" or use Sentry's [server-side data scrubbing](https://docs.sentry.io/security-legal-pii/scrubbing.md) to remove `$user.ip_address`. Adding such a rule ultimately overrules any other logic.

Setting The User For the Current Request

`Sentry.setUser()` will set the user for the currently active request - see [Request Isolation](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/request-isolation.md) for more information. For example, if you want to set the user for a single request, you can do this like this:

```javascript
// Your route handler, for example:
app.get("/my-route", (req, res) => {
  // Get the user from somewhere
  const user = req.user;

  // Set the user data for this request only
  Sentry.setUser({
    id: user.id,
    email: user.email,
    username: user.username,
  });

  res.send("Hello World");
});
```

Or if you want to set the user for all requests, you could use a middleware like this:

```javascript
// Add a middleware, for example:
app.use((req, res, next) => {
  // Get the user from somewhere
  const user = req.user;

  // Set the user data for all requests
  if (user) {
    Sentry.setUser({
      id: user.id,
      email: user.email,
      username: user.username,
    });
  } else {
    Sentry.setUser(null);
  }

  next();
});
```

- [addBreadcrumb](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#addBreadcrumb)

```
function addBreadcrumb(breadcrumb: Breadcrumb, hint?: Hint): void
```

Parameters

breadcrumb\*

```
Breadcrumb {
// If a message is provided, it is rendered as text with all whitespace preserved.
message?: string,
// The type influences how a breadcrumb is rendered in Sentry. When in doubt, leave it at `default`.
type?: "default" | "debug" | "error" | "info" | "navigation" | "http" | "query" | "ui" | "user",
// The level is used in the UI to emphasize or deemphasize the breadcrumb.
level?: "fatal" | "error" | "warning" | "log" | "info" | "debug",
// Typically it is a module name or a descriptive string. For instance, `ui.click` could be used to indicate that a click happened
category?: string,
// Additional data that should be sent with the breadcrumb.
data?: Record<string, unknown>,
}
```

hint

```
Record<string, unknown>
```

A hint object containing additional information about the breadcrumb.

You can manually add breadcrumbs whenever something interesting happens. For example, you might manually record a breadcrumb if the user authenticates or another state change occurs.

## [Tracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#tracing)

- [startSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#startSpan)

```
function startSpan<T>(options: StartSpanOptions, callback: (span: Span) => T): T
```

Parameters

options\*

```
StartSpanOptions {
name: string,
// Attributes to add to the span.
attributes?: Record<string, string | number | boolean | null | undefined>,
// The timestamp to use for the span start. If not provided, the current time will be used.
startTime?: number,
// The operation name for the span. This is used to group spans in the UI
op?: string,
// If true, the span will be forced to be sent as a transaction, even if it is not the root span.
forceTransaction?: boolean,
// The parent span for the new span. If not provided, the current span will be used.
parentSpan?: Span | null,
// If true, the span will only be created if there is an active span.
onlyIfParent?: boolean,
}
```

callback\*

```
(span: Span) => T
```

Starts a new span, that is active in the provided callback. This span will be a child of the currently active span, if there is one.

Any spans created inside of the callback will be children of this span.

The started span will automatically be ended when the callback returns, and will thus measure the duration of the callback. The callback can also be an async function.

Examples

```javascript
// Synchronous example
Sentry.startSpan({ name: "my-span" }, (span) => {
  measureThis();
});

// Asynchronous example
const status = await Sentry.startSpan(
  { name: "my-span" },
  async (span) => {
    const status = await doSomething();
    return status;
  },
);
```

See [Tracing Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md) for more information on how to work with spans.

- [startInactiveSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#startInactiveSpan)

```
function startInactiveSpan<T>(options: StartSpanOptions): Span
```

Parameters

options\*

```
StartSpanOptions {
name: string,
// Attributes to add to the span.
attributes?: Record<string, string | number | boolean | null | undefined>,
// The timestamp to use for the span start. If not provided, the current time will be used.
startTime?: number,
// The operation name for the span. This is used to group spans in the UI
op?: string,
// If true, the span will be forced to be sent as a transaction, even if it is not the root span.
forceTransaction?: boolean,
// The parent span for the new span. If not provided, the current span will be used.
parentSpan?: Span | null,
// If true, the span will only be created if there is an active span.
onlyIfParent?: boolean,
}
```

Starts a new span. This span will be a child of the currently active span, if there is one. The returned span has to be ended manually via `span.end()` when the span is done.

Examples

```javascript
const span = Sentry.startInactiveSpan({ name: "my-span" });
doSomething();
span.end();
```

See [Tracing Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md) for more information on how to work with spans.

- [startSpanManual](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#startSpanManual)

```
function startSpanManual<T>(options: StartSpanOptions, callback: (span: Span) => T): T
```

Parameters

options\*

```
StartSpanOptions {
name: string,
// Attributes to add to the span.
attributes?: Record<string, string | number | boolean | null | undefined>,
// The timestamp to use for the span start. If not provided, the current time will be used.
startTime?: number,
// The operation name for the span. This is used to group spans in the UI
op?: string,
// If true, the span will be forced to be sent as a transaction, even if it is not the root span.
forceTransaction?: boolean,
// The parent span for the new span. If not provided, the current span will be used.
parentSpan?: Span | null,
// If true, the span will only be created if there is an active span.
onlyIfParent?: boolean,
}
```

callback\*

```
(span: Span) => T
```

Starts a new span, that is active in the provided callback. This span will be a child of the currently active span, if there is one.

Any spans created inside of the callback will be children of this span.

The started span will *not* automatically end - you have to call `span.end()` when the span is done. Please note that the span will still only be the parent span of spans created inside of the callback, while the callback is active. In most cases, you will want to use `startSpan` or `startInactiveSpan` instead.

Examples

```javascript
const status = await Sentry.startSpanManual(
  { name: "my-span" },
  async (span) => {
    const status = await doSomething();
    span.end();
    return status;
  },
);
```

See [Tracing Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md) for more information on how to work with spans.

- [setActiveSpanInBrowser](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setActiveSpanInBrowser)

Only available on Client

```
function setActiveSpanInBrowser(span: Span): void
```

Available since: `v10.15.0`

Sets the passed span as the active span on the current scope. You most likely don't need this functionality and should [use `startSpan`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#startSpan) instead. However, in some situations, you might prefer a span being active outside of a callback. In this case, the combination of [`startInactiveSpan`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#startInactiveSpan) with this function allows you to start a span, hold a reference to it and keep it active until you end it, without the active duration being bound to the callback (as opposed to [`startSpanManual`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#startSpanManual)).

Examples

```javascript
let checkoutSpan;

on("startCheckout", () => {
  checkoutSpan = Sentry.startInactiveSpan({ name: "checkout-flow" });
  Sentry.setActiveSpanInBrowser(checkoutSpan);
});

doSomeWork();

on("endCheckout", () => {
  // Ending the span automatically removes it as the active span on the scope
  checkoutSpan.end();
});
```

See [Tracing Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation.md) for more information on how to work with spans.

- [continueTrace](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#continueTrace)

```
function continueTrace<T>(options: TraceOptions, callback: () => T): T
```

Parameters

options

```
TraceOptions {
// The sentry-trace header.
sentryTrace?: string,
// The baggage header.
baggage?: string,
}
```

callback

```
() => T
```

The callback to continue the trace.

Continues a trace in the provided callback. Any spans created inside of the callback will be linked to the trace.

- [suppressTracing](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#suppressTracing)

```
function suppressTracing<T>(callback: () => T): T
```

Ensure that all spans created inside of the provided callback are not sent to Sentry.

- [startNewTrace](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#startNewTrace)

```
function startNewTrace<T>(callback: () => T): T
```

Start a new trace that is active in the provided callback.

- [startBrowserTracingPageLoadSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#startBrowserTracingPageLoadSpan)

Only available on Client

```
function startBrowserTracingPageLoadSpan(client: Client, options: StartSpanOptions): Span | undefined
```

Start an pageload span that will be automatically ended when the page is considered idle. If a pageload/navigation span is currently ongoing, it will automatically be ended first. In most cases, you do not need to call this, as the `browserTracingIntegration` will automatically do that for you. However, if you opt-out of pageload spans, you can use this method to manually start such a span. Please note that this function will do nothing if `browserTracingIntegration` has not been enabled.

- [startBrowserTracingNavigationSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#startBrowserTracingNavigationSpan)

Only available on Client

```
function startBrowserTracingNavigationSpan(client: Client, options: StartSpanOptions): Span | undefined
```

Start an navigation span that will be automatically ended when the page is considered idle. If a pageload/navigation span is currently ongoing, it will automatically be ended first. In most cases, you do not need to call this, as the `browserTracingIntegration` will automatically do that for you. However, if you opt-out of navigation spans, you can use this method to manually start such a span. Please note that this function will do nothing if `browserTracingIntegration` has not been enabled.

- [reportPageLoaded](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#reportPageLoaded)

Only available on Client

```
function reportPageLoaded(): void
```

Available since: `v10.13.0`

Signals to the Sentry SDK that the initial page was fully loaded. Requires the [`enableReportPageLoaded` option](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#enableReportPageLoaded) in `browserTracingIntegration` to be set to `true`. Once called, the SDK ends the pageload span automatically,

By default, the SDK takes care of ending the pageload span automatically, based on a period of inactivity where no new child spans are added to the pageload trace. You can alternatively use explicit pageload reporting if the inactivity heuristics of `browserTracingIntegration` don't work well for your use case. However, you must ensure that you call `reportPageLoaded` in every situation. If `reportPageLoaded` is not called, the pageload span will be ended after 30 seconds or whatever custom value is set on the [`finalTimeout` option](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#enableReportPageLoaded).

Examples

```javascript
Sentry.init({
  // 1. Enable manual page load reporting:
  integrations: [
    browserTracingIntegration({ enableReportPageLoaded: true }),
  ],
});

// 2. Whenever you consider the page loaded:
Sentry.reportPageLoaded();
```

## [Tracing Utilities](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#tracing-utilities)

These utilities can be used for more advanced tracing use cases.

- [spanToJSON](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#spanToJSON)

```
function spanToJSON(span: Span): SpanJSON
```

Convert a span to a JSON object.

- [updateSpanName](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#updateSpanName)

```
function updateSpanName(span: Span, name: string): void
```

Update the name of a span. Use this over `span.updateName(name)` to ensure that the span is updated in all backends.

- [setHttpStatus](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setHttpStatus)

```
function setHttpStatus(span: Span, httpStatus: number): void
```

Set the status of a span based on the given http status code.

- [getActiveSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#getActiveSpan)

```
function getActiveSpan(): Span | undefined
```

Get the currently active span.

- [getRootSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#getRootSpan)

```
function getRootSpan(span: Span): Span
```

Get the root span of a span.

- [withActiveSpan](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#withActiveSpan)

```
function withActiveSpan<T>(span: Span | null, callback: (scope: Scope) => T): T
```

Runs the provided callback with the given span as the active span. If `null` is provided, the callback will have no active span.

- [setConversationId](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#setConversationId)

```
function setConversationId(conversationId: string | null): void
```

Set a conversation ID that will be automatically applied to all subsequent AI spans within the current scope. This is useful for tracking multiple AI API calls that are part of the same conversation, allowing you to analyze entire conversation flows in Sentry.

The conversation ID is stored on the isolation scope and automatically added as the `gen_ai.conversation.id` attribute to all AI-related spans. To unset the conversation ID, pass `null`.

Example

```javascript
import * as Sentry from '@sentry/node';

// Set conversation ID for all subsequent spans
Sentry.setConversationId('conv_abc123');

// All AI spans will now include the gen_ai.conversation.id attribute
await openai.chat.completions.create({...});

// To unset it
Sentry.setConversationId(null);
```

See [AI Agent Monitoring](https://docs.sentry.io/platforms/javascript/guides/nextjs/ai-agent-monitoring.md) for more information on tracking AI conversations.

## [Sessions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#sessions)

Sessions allow you to track the release health of your application. See the [Releases & Health](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/releases.md#sessions) page for more information.

- [startSession](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#startSession)

```
function startSession(): Session
```

Starts a new session.

- [endSession](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#endSession)

```
function endSession(): void
```

Ends the current session (but does not send it to Sentry).

- [captureSession](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#captureSession)

```
function captureSession(end = false): void
```

Sends the current session on the scope to Sentry. Pass `true` as argument to end the session first.

## [Scopes](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#scopes)

See [Scopes](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md) for more information on how to use scopes, as well as for an explanation of the different types of scopes (current scope, isolation scope, and global scope).

- [withScope](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#withScope)

```
function withScope(callback: (scope: Scope) => void): void
```

Forks the current scope and calls the callback with the forked scope.

- [withIsolationScope](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#withIsolationScope)

```
function withIsolationScope(callback: (scope: Scope) => void): void
```

Forks the current isolation scope and calls the callback with the forked scope.

- [getCurrentScope](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#getCurrentScope)

```
function getCurrentScope(): Scope
```

Returns the [current scope](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#current-scope).

Note that in most cases you should not use this API, but instead use `withScope` to generate and access a local scope. There are no guarantees about the consistency of `getCurrentScope` across different parts of your application, as scope forking may happen under the hood at various points.

- [getIsolationScope](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#getIsolationScope)

```
function getIsolationScope(): Scope
```

Returns the current<!-- -->

[isolation scope](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#isolation-scope)

.

- [getGlobalScope](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#getGlobalScope)

```
function getGlobalScope(): Scope
```

Returns the<!-- -->

[global scope](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#global-scope)

.

## [User Feedback](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#user-feedback)

- [captureFeedback](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#captureFeedback)

```
function captureFeedback(feedback: Feedback, hint?: Hint): string
```

Parameters

feedback

```
Feedback {
message: string,
name?: string,
email?: string,
url?: string,
source?: string,
// The event id that this feedback is associated with.
associatedEventId?: string,
tags?: Record<string, string>,
}
```

The feedback to capture.

hint

```
Hint {
// Optional additional data to attach to the Sentry event.
captureContext?: CaptureContext {
user?: User {
id?: string | number,
email?: string,
ip_address?: string,
username?: string,
}
level?: "fatal" | "error" | "warning" | "log" | "info" | "debug",
// Additional data that should be sent with the exception.
extra?: Record<string, unknown>,
// Additional tags that should be sent with the exception.
tags?: Record<string, string>,
contexts?: Record<string, Record<string, unknown>>,
fingerprint?: string[],
}
}
```

Optional hint object containing additional information about the feedback.

Send user feedback to Sentry.

- [getFeedback](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#getFeedback)

```
function getFeedback(): ReturnType<feedbackIntegration> | undefined
```

Get the feedback integration, if it has been added. This can be used to access the feedback integration in a type-safe way.

- [sendFeedback](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#sendFeedback)

```
function sendFeedback(feedback: Feedback, hint?: Hint): Promise<string>
```

Parameters

feedback

```
Feedback {
message: string,
name?: string,
email?: string,
url?: string,
source?: string,
// The event id that this feedback is associated with.
associatedEventId?: string,
tags?: Record<string, string>,
}
```

The feedback to capture.

hint

```
Hint {
// Optional additional data to attach to the Sentry event.
captureContext?: CaptureContext {
user?: User {
id?: string | number,
email?: string,
ip_address?: string,
username?: string,
}
level?: "fatal" | "error" | "warning" | "log" | "info" | "debug",
// Additional data that should be sent with the exception.
extra?: Record<string, unknown>,
// Additional tags that should be sent with the exception.
tags?: Record<string, string>,
contexts?: Record<string, Record<string, unknown>>,
fingerprint?: string[],
}
}
```

Optional hint object containing additional information about the feedback.

This method is similar to [`captureFeedback`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#capturefeedback), but it returns a promise that resolves only when the feedback was successfully sent to Sentry. It will reject if the feedback cannot be sent.

## [Cron Monitoring](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#cron-monitoring)

- [captureCheckIn](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#captureCheckIn)

Only available on Server

```
function captureCheckIn(checkIn: CheckIn, monitorConfig?: MonitorConfig): string
```

Parameters

checkIn\*

```
CheckIn {
status: "ok" | "error" | "in_progress",
monitorSlug: string,
checkInId?: string,
duration?: number,
}
```

monitorConfig

```
MonitorConfig {
schedule: { type: "crontab", value: string } | { type: "interval", value: number, unit: "year" | "month" | "day" | "hour" | "minute" },
checkinMargin?: number,
maxRuntime?: number,
timezone?: string,
failureIssueThreshold?: number,
recoveryThreshold?: number,
}
```

Create a cron monitor check in and send it to Sentry.

- [withMonitor](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#withMonitor)

Only available on Server

```
function withMonitor(
monitorSlug: string,
callback: () => any,
monitorConfig?: MonitorConfig
): string
```

Parameters

monitorSlug\*

```
string
```

callback\*

```
() => any
```

monitorConfig

```
MonitorConfig {
schedule: { type: "crontab", value: string } | { type: "interval", value: number, unit: "year" | "month" | "day" | "hour" | "minute" },
checkinMargin?: number,
maxRuntime?: number,
timezone?: string,
failureIssueThreshold?: number,
recoveryThreshold?: number,
}
```

Wraps a callback with a cron monitor check in. The check in will be sent to Sentry when the callback finishes.

## [Server Actions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#server-actions)

- [withServerActionInstrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#withServerActionInstrumentation)

```
function withServerActionInstrumentation(
serverActionName: string,
options?: Options,
callback: A
): Promise<ReturnType<A>>
```

To instrument Next.js Server Actions, wrap their content in `withServerActionInstrumentation`, along with a name to describe your server action. You can optionally pass form data and headers to record them, and configure the wrapper to record the Server Action responses.

Examples

```tsx
import * as Sentry from "@sentry/nextjs";
import { headers } from "next/headers";

export default function ServerComponent() {
  async function myServerAction(formData: FormData) {
    "use server";
    return await Sentry.withServerActionInstrumentation(
      "myServerAction", // The name you want to associate this Server Action with in Sentry
      {
        formData, // Optionally pass in the form data
        headers: await headers(), // Optionally pass in headers
        recordResponse: true, // Optionally record the server action response
      },
      async () => {
        // ... Your Server Action code

        return { name: "John Doe" };
      },
    );
  }

  return (
    <form action={myServerAction}>
      <input type="text" name="some-input-value" />
      <button type="submit">Run Action</button>
    </form>
  );
}
```

## [Route and Data Fetching Instrumentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#route-and-data-fetching-instrumentation)

- [wrapApiHandlerWithSentry](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#wrapApiHandlerWithSentry)

```
function wrapApiHandlerWithSentry(
apiHandler: NextApiHandler,
parameterizedRoute: string
): NextApiHandler
```

Instrument the provided API route handler with Sentry for error and performance monitoring. This function wraps the handler exported from the user's API page route file (which may or may not already be wrapped with `withSentry`).

- [wrapGetInitialPropsWithSentry](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#wrapGetInitialPropsWithSentry)

```
function wrapGetInitialPropsWithSentry(
origGetInitialProps: GetInitialProps
): GetInitialProps
```

Instrument a `getInitialProps` function with Sentry error and performance monitoring by creating and returning a wrapped version of the function.

- [wrapGetServerSidePropsWithSentry](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#wrapGetServerSidePropsWithSentry)

```
function wrapGetServerSidePropsWithSentry(
origGetInitialProps: GetInitialProps,
parameterizedRoute: string
): GetServerSideProps
```

Instrument a `getServerSideProps` function with Sentry error and performance monitoring by creating and returning a wrapped version of the function.

- [wrapGetStaticPropsWithSentry](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#wrapGetStaticPropsWithSentry)

```
function wrapGetStaticPropsWithSentry(
origGetStaticPropsa: GetStaticProps<Props>,
_parameterizedRoute: string
): GetStaticProps<Props>
```

Instrument a `getStaticProps` function with Sentry error and performance monitoring by creating and returning a wrapped version of the function.

- [wrapErrorGetInitialPropsWithSentry](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#wrapErrorGetInitialPropsWithSentry)

```
function wrapErrorGetInitialPropsWithSentry(
origErrorGetInitialProps: ErrorGetInitialProps
): ErrorGetInitialProps
```

Instrument a `getInitialProps` function in a custom error page (`_error.js`) with Sentry error and performance monitoring by creating and returning a wrapped version of the function.

- [wrapAppGetInitialPropsWithSentry](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#wrapAppGetInitialPropsWithSentry)

```
function wrapAppGetInitialPropsWithSentry(
origAppGetInitialProps: AppGetInitialProps
): AppGetInitialProps
```

Instrument a `getInitialProps` function in a custom app (`_app.js`) with Sentry error and performance monitoring by creating and returning a wrapped version of the function.

- [wrapDocumentGetInitialPropsWithSentry](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/apis.md#wrapDocumentGetInitialPropsWithSentry)

```
function wrapDocumentGetInitialPropsWithSentry(
origDocumentGetInitialProps: DocumentGetInitialProps
): DocumentGetInitialProps
```

Instrument a `getInitialProps` function in a custom document (`_document.js`) with Sentry error and performance monitoring by creating and returning a wrapped version of the function.

