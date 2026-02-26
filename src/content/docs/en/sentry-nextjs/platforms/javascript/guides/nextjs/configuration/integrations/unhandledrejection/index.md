---
title: 'OnUnhandledRejection | Sentry for Next.js'
description: 'This integration only works inside server environments (Node.js, Bun, Deno).'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unhandledrejection

# OnUnhandledRejection | Sentry for Next.js

This integration only works inside server environments (Node.js, Bun, Deno).

*Import name: `Sentry.onUnhandledRejectionIntegration`*

This integration is enabled by default. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

The `onUnhandledRejectionIntegration` registers handlers to capture global unhandled promise rejections.

```JavaScript
Sentry.init({
  integrations: [Sentry.onUnhandledRejectionIntegration()],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unhandledrejection.md#options)

- [`mode`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unhandledrejection.md#mode)

*Type: `'none' | 'warn' | 'strict'`*

This option defines what to do after capturing an unhandled rejection and mimics the behavior of [node's](https://nodejs.org/api/cli.html#--unhandled-rejectionsmode) `--unhandled-rejection` flag:

* `strict`: Raise the unhandled rejection as an uncaught exception. If the exception is handled, unhandledRejection is emitted.
* `warn`: Always trigger a warning, no matter if the unhandledRejection hook is set or not but do not print the deprecation warning.
* `none`: Silence all warnings.

Defaults to `warn`.

