---
title: 'ModuleMetadata | Sentry for Next.js'
description: 'This integration only works inside a browser environment.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/modulemetadata

# ModuleMetadata | Sentry for Next.js

This integration only works inside a browser environment.

*Import name: `Sentry.moduleMetadataIntegration`*

Metadata can be injected by the Sentry bundler plugins using the `_experiments.moduleMetadata` config option. Once this integration is added, the metadata passed to the bundler plugin will be added to the stack frames of all events under the `module_metadata` property. This can be used to help tag or route events from different teams or sources.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.moduleMetadataIntegration()],
});
```

