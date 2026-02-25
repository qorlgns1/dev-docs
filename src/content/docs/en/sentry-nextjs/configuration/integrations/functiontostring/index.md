---
title: 'FunctionToString | Sentry for Next.js'
description: "This integration is enabled by default. If you'd like to modify your default integrations, read this."
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/functiontostring

# FunctionToString | Sentry for Next.js

*Import name: `Sentry.functionToStringIntegration`*

This integration is enabled by default. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

This integration allows the SDK to provide original functions and method names, even when those functions or methods are wrapped by our error or breadcrumb handlers.

```JavaScript
Sentry.init({
  integrations: [Sentry.functionToStringIntegration()],
});
```

