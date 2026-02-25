---
title: 'CaptureConsole | Sentry for Next.js'
description: "This integration captures all Console API calls and redirects them to Sentry using the SDK's captureMessage or captureException call, depending on the..."
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/captureconsole

# CaptureConsole | Sentry for Next.js

*Import name: `Sentry.captureConsoleIntegration`*

This integration captures all Console API calls and redirects them to Sentry using the SDK's captureMessage or captureException call, depending on the log level. It then re-triggers to preserve default native behavior:

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.captureConsoleIntegration()],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/captureconsole.md#options)

- [`levels`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/captureconsole.md#levels)

*Type: `string[]`*

Array of methods that should be captured. Defaults to `['log', 'info', 'warn', 'error', 'debug', 'assert']`

