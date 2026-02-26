---
title: 'Child Process Integration | Sentry for Next.js'
description: 'This integration only works in Node.js  and requires SDK version  or higher.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/childProcess

# Child Process Integration | Sentry for Next.js

This integration only works in Node.js `>=20` and requires SDK version `8.39.0` or higher.

*Import name: `Sentry.childProcessIntegration`*

This integration is enabled by default. If you'd like to modify your default integrations, read [Modifying Default Integrations](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

The `childProcessIntegration` captures breadcrumbs and events for `child_process` and `worker_threads` errors and `child_process` non-zero exit codes.

```JavaScript
Sentry.init({
  integrations: [Sentry.childProcessIntegration()],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/childProcess.md#options)

- [`includeChildProcessArgs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/childProcess.md#includechildprocessargs)

*Type: `boolean`*

If set to `true`, the integration will include the arguments used to start child processes.

- [`captureWorkerErrors`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/childProcess.md#captureworkererrors)

*Type: `boolean`*

By default, this option is `true`. If set to `false`, the integration will not capture errors from worker threads.

