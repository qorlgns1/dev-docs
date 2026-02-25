---
title: 'Unleash | Sentry for Next.js'
description: 'This integration only works inside a browser environment. It is only available from a package-based install (e.g.  or ).'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unleash

# Unleash | Sentry for Next.js

This integration only works inside a browser environment. It is only available from a package-based install (e.g. `npm` or `yarn`).

The [Unleash](https://www.getunleash.io/) integration tracks feature flag evaluations produced by the Unleash SDK. These evaluations are held in memory and are sent to Sentry on error and transaction events. **At the moment, we only support boolean flag evaluations from Unleash's isEnabled method.** This integration is available in Sentry SDK **versions 8.51.0 or higher.**

*Import names: `Sentry.unleashIntegration`*

Before using this integration, you need to install and instrument Unleash in your app. Learn more by reading [Unleash's SDK reference](https://docs.getunleash.io/reference/sdks/javascript-browser) and [quickstart](https://docs.getunleash.io/quickstart).

```javascript
import * as Sentry from "@sentry/nextjs";
import { UnleashClient } from "unleash-proxy-client";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    Sentry.unleashIntegration({ featureFlagClientClass: UnleashClient }),
  ],
});

const unleash = new UnleashClient({
  url: "https://<your-unleash-instance>/api/frontend",
  clientKey: "<your-client-side-token>",
  appName: "my-webapp",
});

unleash.start();

// Evaluate a flag with a default value. You may have to wait for your client to synchronize first.
unleash.isEnabled("test-flag");

Sentry.captureException(new Error("Something went wrong!"));
```

The `unleashClientClass` option has been renamed to `featureFlagClientClass` in v9 of the Sentry SDK. Please update accordingly.

Visit the Sentry website and confirm that your error event has recorded the feature flag "test-flag" and its value "false".

##### Next Steps

* **Track feature flag evaluations in other parts of your codebase.** If needed, you can set up evaluation tracking for more than one SDK. [Read the docs](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-evaluation-tracking) to learn more.
* **Set up your change tracking webhook.** In order to take full advantage of the feature flag capabilities Sentry offers there is an additional setup step needed. Your feature flag provider needs to notify Sentry when a feature flag definition has changed. A Sentry webhook URL can be registered with your provider. [Learn how](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-change-tracking).

