---
title: 'ReportingObserver | Sentry for Next.js'
description: 'This integration only works inside a browser environment.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/reportingobserver

# ReportingObserver | Sentry for Next.js

This integration only works inside a browser environment.

*Import name: `Sentry.reportingObserverIntegration`*

This integration hooks into the [Reporting API](https://developer.mozilla.org/en-US/docs/Web/API/Reporting_API) and sends captured events through to Sentry. It can be configured to handle specific issue types only.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.reportingObserverIntegration()],
});
```

## [Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/reportingobserver.md#options)

- [`types`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/reportingobserver.md#types)

*Type: `('crash'|'deprecation'|'intervention')[]`*

Only handle the given issue types. By default, all issue types are handled.

