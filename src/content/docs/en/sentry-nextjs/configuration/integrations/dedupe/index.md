---
title: 'Dedupe | Sentry for Next.js'
description: "This integration is enabled by default. If you'd like to modify your default integrations, read this."
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/dedupe

# Dedupe | Sentry for Next.js

*Import name: `Sentry.dedupeIntegration`*

This integration is enabled by default. If you'd like to modify your default integrations, read [this](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations).

This integration deduplicates certain events. It can be helpful if you're receiving many duplicate errors. Note, that Sentry only compares stack traces and fingerprints.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.dedupeIntegration()],
});
```

