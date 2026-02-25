---
title: 'WebWorker | Sentry for Next.js'
description: "This integration, together with , establishes communication between the browser's main thread and one or more WebWorkers. It listens to worker message..."
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/webworker

# WebWorker | Sentry for Next.js

*Import name: `Sentry.webWorkerIntegration`*

This integration, together with `Sentry.registerWebWorker()`, establishes communication between the browser's main thread and one or more [WebWorkers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API). It listens to worker messages from the passed workers and forwards them to the main thread.

Read our [Web Worker Guide](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/web-workers.md) for more information.

What does this integration do?

This integration listens to a message sent from the worker when it calls `Sentry.registerWebWorker({ self })`. The purpose is to sync source map information (debugIds) between the main thread and the worker so that worker errors caught by the main thread SDK are properly mapped to the worker's source code.

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/webworker.md#options)

- [`worker`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/webworker.md#worker)

*Type: `Worker | Array<Worker>`*

The web worker(s) to listen to. Every worker must call `Sentry.registerWebWorker({ self })` to register itself with the SDK.

## [Methods](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/webworker.md#methods)

- [`addWorker(worker: Worker)`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/webworker.md#addworkerworker-worker)

Adds a worker to the integration, after the integraion was already initialized and added to the SDK. This is useful if you have workers that are initialized at later point in your application's lifecycle. Note that every worker must call `Sentry.registerWebWorker({ self })` to register itself with the SDK.

