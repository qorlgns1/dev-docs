---
title: 'Event Loop Block | Sentry for Next.js'
description: 'This integration only works in the Node.js runtime.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block

# Event Loop Block | Sentry for Next.js

This integration only works in the Node.js runtime.

*Import name: `eventLoopBlockIntegration` from `@sentry/node-native`*

The `eventLoopBlockIntegration` can be used to monitor for blocked event loops in all threads of a Node.js application. Stack traces are automatically captured when blocking is detected.

## [Installation](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block.md#installation)

```bash
npm install @sentry/node-native
```

## [Usage](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block.md#usage)

If you instrument your application via the Node.js `--import` flag, Sentry will be started and this instrumentation will be automatically applied to all worker threads.

`instrument.mjs`

```javascript
import { eventLoopBlockIntegration } from "@sentry/node-native";

Sentry.init({
  dsn: "__YOUR_DSN__",
  // Monitor event loop blocking for more than 500ms (stack traces automatically captured)
  integrations: [eventLoopBlockIntegration({ threshold: 500 })],
});
```

`app.mjs`

```javascript
import { Worker } from "worker_threads";

const worker = new Worker(new URL("./worker.mjs", import.meta.url));

// This main thread will be monitored for blocked event loops
```

`worker.mjs`

```javascript
// This worker thread will also be monitored for blocked event loops too
```

Start your application:

```bash
node --import instrument.mjs app.mjs
```

If a thread is blocked for more than the configured threshold, stack traces are automatically captured for all threads and sent to Sentry.

## [Configuration Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block.md#configuration-options)

You can pass a configuration object to the `eventLoopBlockIntegration` to customize the behavior:

```typescript
interface ThreadBlockedIntegrationOptions {
  /**
   * Threshold in milliseconds to trigger an event.
   *
   * Defaults to 1000ms.
   */
  threshold: number;
  /**
   * Maximum number of blocked events to send per clock hour.
   *
   * Defaults to 1.
   */
  maxEventsPerHour: number;
  /**
   * Tags to include with blocked events.
   */
  staticTags: { [key: string]: Primitive };
}
```

## [Example Configuration](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/event-loop-block.md#example-configuration)

```javascript
import { eventLoopBlockIntegration } from "@sentry/node-native";

Sentry.init({
  dsn: "__YOUR_DSN__",
  integrations: [
    eventLoopBlockIntegration({
      threshold: 500, // Trigger after 500ms of blocking (stack traces automatically captured)
      maxEventsPerHour: 5, // Maximum 5 events per hour
      staticTags: {
        component: "main-thread",
        environment: "production",
      },
    }),
  ],
});
```

