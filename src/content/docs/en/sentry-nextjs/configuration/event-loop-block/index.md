---
title: 'Event Loop Block Detection | Sentry for Next.js'
description: 'Event Loop Block detection monitors when the Node.js main thread event loop is blocked for more than a specified threshold. The Node SDK reports these...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/event-loop-block

# Event Loop Block Detection | Sentry for Next.js

Event Loop Block detection monitors when the Node.js main thread event loop is blocked for more than a specified threshold. The Node SDK reports these events to Sentry with automatically captured stack traces to help identify blocking code.

This feature is currently in Beta. Beta features are still in progress and may have bugs. We recognize the irony.

Event loop block detection is not supported for [Node.js clusters](https://nodejs.org/api/cluster.html).

## [Event Loop Block Integration (Recommended)](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/event-loop-block.md#event-loop-block-integration-recommended)

For the best performance and comprehensive monitoring, we recommend using the [`eventLoopBlockIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block.md) from the `@sentry/node-native` package. Stack traces are automatically captured when blocking is detected. This integration can monitor all threads in your Node.js application and provides better performance compared to the deprecated ANR integration.

```javascript
import * as Sentry from "@sentry/node";
import { eventLoopBlockIntegration } from "@sentry/node-native";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [eventLoopBlockIntegration({ threshold: 1000 })],
});
```

For detailed usage instructions and configuration options, see the [`eventLoopBlockIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block.md) documentation.

## [Deprecated Application Not Responding (ANR) Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/event-loop-block.md#deprecated-application-not-responding-anr-integration)

**Deprecated**: The `anrIntegration` is deprecated. Please use the [`eventLoopBlockIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block.md) instead for better performance and more comprehensive monitoring.

*(Available in version 7.91.0 and above)*

The legacy ANR integration is still available but deprecated. If you're currently using it, we recommend migrating to the new `eventLoopBlockIntegration`.

ANR detection requires Node 16 or higher and can only be used in the Node.js runtime.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.anrIntegration({ captureStackTrace: true })],
});
```

- [Legacy ANR Configuration Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/event-loop-block.md#legacy-anr-configuration-options)

The deprecated ANR integration supports the following configuration options:

```ts
interface Options {
  /**
   * Interval to send heartbeat messages to the ANR thread.
   *
   * Defaults to 50ms.
   */
  pollInterval: number;
  /**
   * Threshold in milliseconds to trigger an ANR event.
   *
   * Defaults to 5000ms.
   */
  anrThreshold: number;
  /**
   * Whether to capture a stack trace when the ANR event is triggered.
   *
   * Defaults to `false`.
   *
   * This uses the node debugger which enables the inspector API.
   */
  captureStackTrace: boolean;
}
```

- [Legacy ANR Implementation and Overhead](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/event-loop-block.md#legacy-anr-implementation-and-overhead)

ANR detection with the legacy Node SDK uses a worker thread to monitor the event loop in the main app thread. The main app thread sends a heartbeat message to the ANR worker thread every 50ms. If the ANR worker does not receive a heartbeat message for 5 seconds, it triggers an ANR event. If the `captureStackTrace` option is enabled, the ANR worker uses the `inspector` module to capture stack traces via the [v8 inspector API](https://nodejs.org/api/inspector.html).

Once an ANR event is reported, the ANR worker thread exits to prevent further duplicate events and the main app thread will continue to run as usual.

Overhead from Node.js ANR tracking should be minimal. With no ANR detected, the only overhead in the main app thread is polling the ANR worker over IPC every 50ms by default. The ANR worker thread consumes around 10-20 MB of RAM to keep track of the polling. Once an ANR has been detected, the main thread is paused briefly in the debugger to capture the stack trace frames. At this point, the event loop has been blocked for seconds so the debugging overhead is negligible.

