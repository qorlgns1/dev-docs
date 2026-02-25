---
title: 'Pino | Sentry for Next.js'
description: 'This integration only works in the Node.js runtime. Requires SDK version  or higher.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino

# Pino | Sentry for Next.js

This integration only works in the Node.js runtime. Requires SDK version `10.18.0` or higher.

*Import name: `Sentry.pinoIntegration`*

The `pinoIntegration` adds instrumentation for the `pino` library so that calls to the pino logger are captured as logs. Optionally, you can capture calls to the pino logger as errors.

```JavaScript
Sentry.init({
  enableLogs: true,
  integrations: [Sentry.pinoIntegration()],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md#options)

- [`error`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md#error)

Configure how pino logs are captured as Sentry errors.

#
- [`levels`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md#levels)

* Type: `Array<'trace' | 'debug' | 'info' | 'warn' | 'error' | 'fatal'>`
* Default: `[]`

Levels that trigger capturing of events. When a pino log message is logged at one of these levels, it will be captured as a Sentry error event.

#
- [`handled`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md#handled)

* Type: `boolean`
* Default: `true`

By default, Sentry will mark captured errors as handled. Set this to `false` if you want to mark them as unhandled instead.

- [`log`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md#log)

Configure how pino logs are captured as Sentry logs.

#
- [`levels`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md#levels-1)

* Type: `Array<'trace' | 'debug' | 'info' | 'warn' | 'error' | 'fatal'>`
* Default: `["trace", "debug", "info", "warn", "error", "fatal"]`

Levels that trigger capturing of logs. Logs are only captured if `enableLogs` is enabled in your Sentry configuration.

## [Supported Versions](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md#supported-versions)

* `pino`: `>=8.0.0 <11`

## [Examples](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md#examples)

- [Send only info, error, and warn log levels to Sentry](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md#send-only-info-error-and-warn-log-levels-to-sentry)

```js
Sentry.init({
  enableLogs: true,
  integrations: [
    Sentry.pinoIntegration({ log: { levels: ["info", "warn", "error"] } }),
  ],
});
```

- [Send errors to Sentry](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/pino.md#send-errors-to-sentry)

```js
Sentry.init({
  enableLogs: true,
  integrations: [
    Sentry.pinoIntegration({ error: { levels: ["warn", "error"] } }),
  ],
});
```

