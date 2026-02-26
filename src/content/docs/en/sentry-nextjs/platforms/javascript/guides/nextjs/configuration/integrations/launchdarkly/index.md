---
title: 'LaunchDarkly | Sentry for Next.js'
description: 'This integration only works inside a browser environment. It is only available from a package-based install (e.g.  or ).'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/launchdarkly

# LaunchDarkly | Sentry for Next.js

This integration only works inside a browser environment. It is only available from a package-based install (e.g. `npm` or `yarn`).

The [LaunchDarkly](https://launchdarkly.com/) integration tracks feature flag evaluations produced by the LaunchDarkly SDK. These evaluations are held in memory and are sent to Sentry on error and transaction events. **At the moment, we only support boolean flag evaluations.** This integration is available in Sentry SDK **versions 8.43.0 or higher.**

*Import names: `Sentry.launchDarklyIntegration` and `Sentry.buildLaunchDarklyFlagUsedHandler`*

Before using this integration, you need to install and instrument the [LaunchDarkly SDK](https://www.npmjs.com/package/launchdarkly-js-client-sdk) in your app. Learn more by reading [LaunchDarkly's docs](https://docs.launchdarkly.com/sdk/client-side/javascript).

```javascript
import * as Sentry from "@sentry/nextjs";
import * as LaunchDarkly from "launchdarkly-js-client-sdk";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.launchDarklyIntegration()],
});

const ldClient = LaunchDarkly.initialize(
  "my-client-ID",
  { kind: "user", key: "my-user-context-key" },
  { inspectors: [Sentry.buildLaunchDarklyFlagUsedHandler()] },
);

// Evaluate a flag with a default value. You may have to wait for your client to initialize first.
ldClient?.variation("test-flag", false);

Sentry.captureException(new Error("Something went wrong!"));
```

Visit the Sentry website and confirm that your error event has recorded the feature flag "test-flag" and its value "false".

##### Next Steps

* **Track feature flag evaluations in other parts of your codebase.** If needed, you can set up evaluation tracking for more than one SDK. [Read the docs](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-evaluation-tracking) to learn more.
* **Set up your change tracking webhook.** In order to take full advantage of the feature flag capabilities Sentry offers there is an additional setup step needed. Your feature flag provider needs to notify Sentry when a feature flag definition has changed. A Sentry webhook URL can be registered with your provider. [Learn how](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-change-tracking).

