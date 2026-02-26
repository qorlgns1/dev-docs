---
title: 'Generic Feature Flags Integration | Sentry for Next.js'
description: 'The Feature Flags integration allows you to manually track feature flag evaluations through an API. These evaluations are held in memory and sent to S...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/featureflags

# Generic Feature Flags Integration | Sentry for Next.js

The Feature Flags integration allows you to manually track feature flag evaluations through an API. These evaluations are held in memory and sent to Sentry on error and transaction events. **At the moment, we only support boolean flag evaluations.**

This integration is available in Sentry SDK **versions 8.43.0 or higher.**

*Import names: `Sentry.featureFlagsIntegration` and `type Sentry.FeatureFlagsIntegration`*

```typescript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.featureFlagsIntegration()],
});

const flagsIntegration =
  Sentry.getClient()?.getIntegrationByName<Sentry.FeatureFlagsIntegration>(
    "FeatureFlags",
  );
if (flagsIntegration) {
  flagsIntegration.addFeatureFlag("test-flag", false);
} else {
  // Something went wrong, check your DSN and/or integrations
}
Sentry.captureException(new Error("Something went wrong!"));
```

Visit the Sentry website and confirm that your error event has recorded the feature flag "test-flag" and its value "false".

##### Next Steps

* **Track feature flag evaluations in other parts of your codebase.** If needed, you can set up evaluation tracking for more than one SDK. [Read the docs](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-evaluation-tracking) to learn more.
* **Set up your change tracking webhook.** In order to take full advantage of the feature flag capabilities Sentry offers there is an additional setup step needed. Your feature flag provider needs to notify Sentry when a feature flag definition has changed. A Sentry webhook URL can be registered with your provider. [Learn how](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-change-tracking).

