---
title: 'OnUncaughtException | Sentry for Next.js'
description: 'This integration only works inside server environments (Node.js, Bun, Deno).'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/onuncaughtexception

# OnUncaughtException | Sentry for Next.js

This integration only works inside server environments (Node.js, Bun, Deno).

*Import name: `Sentry.onUncaughtExceptionIntegration`*

This integration is enabled by default. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

The `onUncaughtExceptionIntegration` registers handlers to capture global uncaught exceptions that would cause the process to exit.

This integration *does not* prevent the process from exiting! If you want to prevent the process from exiting, you should register your own uncaught exception handler and configure `exitEvenIfOtherHandlersAreRegistered: false` in the integration options.

```JavaScript
Sentry.init({
  integrations: [Sentry.onUncaughtExceptionIntegration()],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/onuncaughtexception.md#options)

- [`exitEvenIfOtherHandlersAreRegistered`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/onuncaughtexception.md#exitevenifotherhandlersareregistered)

*Type: `boolean`*

If set to false, the SDK will *not* exit if we detect that another uncaught exception handler is registered.

- [`onFatalError`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/onuncaughtexception.md#onfatalerror)

*Type: `(firstError: Error, secondError: Error | undefined) => void`*

This method is called when an uncaught error would cause the process to exit. `secondError` will be set if the handler was called multiple times. This can happen either because `onFatalError` itself threw, or because an independent error happened somewhere else while `onFatalError` was running.

