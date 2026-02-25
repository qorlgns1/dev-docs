---
title: 'Statsig | Sentry for Next.js'
description: 'This integration only works inside a browser environment. It is only available from a package-based install (e.g.  or ).'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/statsig

# Statsig | Sentry for Next.js

This integration only works inside a browser environment. It is only available from a package-based install (e.g. `npm` or `yarn`).

The [Statsig](https://www.statsig.com/) integration tracks feature flag evaluations produced by the Statsig JavaScript Client SDK. These evaluations are held in memory and are sent to Sentry on error and transaction events. **At the moment, we only support boolean flag evaluations from Statsig's `checkGate` method**. Learn more about [Statsig feature gates](https://docs.statsig.com/feature-flags/working-with/).

This integration is available in Sentry SDK **versions 9.0.0 and higher**, or **versions 8.55.0 and higher for v8.**

*Import name: `Sentry.statsigIntegration`*

Before using this integration, you need to install and instrument Statsig in your app. Learn more by reading [Statsig's SDK reference](https://docs.statsig.com/client/javascript-sdk) and [quickstart guide](https://docs.statsig.com/guides/first-feature).

```javascript
import * as Sentry from "@sentry/nextjs";
import { StatsigClient } from "@statsig/js-client";

const statsigClient = new StatsigClient(
  YOUR_SDK_KEY,
  { userID: "my-user-id" },
  {},
); // see Statsig SDK reference.

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    Sentry.statsigIntegration({ featureFlagClient: statsigClient }),
  ],
});

await statsigClient.initializeAsync(); // or statsigClient.initializeSync();

const result = statsigClient.checkGate("my-feature-gate");
Sentry.captureException(new Error("something went wrong"));
```

Visit the Sentry website and confirm that your error event has recorded the feature flag "my-feature-gate" and its value "false".

##### Next Steps

* **Track feature flag evaluations in other parts of your codebase.** If needed, you can set up evaluation tracking for more than one SDK. [Read the docs](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-evaluation-tracking) to learn more.
* **Set up your change tracking webhook.** In order to take full advantage of the feature flag capabilities Sentry offers there is an additional setup step needed. Your feature flag provider needs to notify Sentry when a feature flag definition has changed. A Sentry webhook URL can be registered with your provider. [Learn how](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-change-tracking).

