---
title: 'LocalVariables | Sentry for Next.js'
description: 'This integration only works in the Node.js runtime.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/localvariables

# LocalVariables | Sentry for Next.js

This integration only works in the Node.js runtime.

*Import name: `Sentry.localVariablesIntegration`*

This integration is enabled by default. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

This integration captures local variables to exception frames. To enable capturing local variables via the integration, set `includeLocalVariable` to `true` in the SDK configuration.

```JavaScript
Sentry.init({
  includeLocalVariables: true,
});
```

The local variables integration only captures local variables from application code (`in_app = true`). Frames of a stacktrace originating from `node_modules` will not have local variables attached to them.

##### Issues with ESM

Due to an [open Node.js issue](https://github.com/nodejs/node/issues/38439), we are currently unable to capture local variables for unhandled errors when using JavaScript modules (ESM).

To work around this, wrap relevant code in a try-catch block and call `captureException` with the error so that Sentry can capture local variables.

```javascript
try {
  // Your code here
} catch (error) {
  Sentry.captureException(error);
}
```

##### Minified Variables

Minified local variable names attached to exception frames can't be unminified by Sentry at this time. There's an [active proposal](https://github.com/tc39/source-map/blob/main/proposals/scopes.md) for the sourcemaps spec that will add this capability.

##### Incompatibility with Debuggers

Setting `includeLocalVariables` to `true` can and will interfere with other debugger sessions attached to the process. The integration works by briefly pausing execution on thrown exceptions, to collect variables in the scope and then instantly resuming it. You may therefore examine your breakpoints being skipped over when this integration is active.

It is recommended to set `includeLocalVariables` to `false` when intending to use other debugger sessions.

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/localvariables.md#options)

- [`captureAllExceptions`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/localvariables.md#captureallexceptions)

*Type: `boolean`*

Defaults to `true`. If enabled, local variables are captured for both caught and uncaught exceptions.

* When false, only uncaught exceptions will have local variables
* When true, both caught and uncaught exceptions will have local variables.

Capturing local variables for all exceptions can be expensive since the debugger pauses for every throw to collect local variables.

To reduce the likelihood of this feature impacting app performance or throughput, this feature is rate-limited. Once the rate limit is reached, local variables will only be captured for uncaught exceptions until a timeout has been reached.

- [`maxExceptionsPerSecond`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/localvariables.md#maxexceptionspersecond)

*Type: `number`*

The maximum number of exceptions to capture local variables for per second before rate limiting is triggered.

