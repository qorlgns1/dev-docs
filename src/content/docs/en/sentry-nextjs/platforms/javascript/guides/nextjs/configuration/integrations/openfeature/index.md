---
title: 'OpenFeature | Sentry for Next.js'
description: 'This integration only works inside a browser environment. It is only available from a package-based install (e.g.  or ).'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openfeature

# OpenFeature | Sentry for Next.js

This integration only works inside a browser environment. It is only available from a package-based install (e.g. `npm` or `yarn`).

The [OpenFeature](https://openfeature.dev/) integration tracks feature flag evaluations produced by the OpenFeature SDK. This SDK is supported by a broad range of feature flagging providers. For the full list, visit [OpenFeature's ecosystem page](https://openfeature.dev/ecosystem/?instant_search%5BrefinementList%5D%5Btype%5D%5B0%5D=Provider\&instant_search%5BrefinementList%5D%5BallTechnologies%5D%5B0%5D=JavaScript).

The flag evaluations are held in memory and are sent to Sentry on error and transaction events. **At the moment, we only support boolean flag evaluations.** This integration is available in Sentry SDK **versions 8.43.0 or higher.**

*Import name: `Sentry.openFeatureIntegration` and `Sentry.OpenFeatureIntegrationHook`*

Before using this integration, you need to install and instrument the [OpenFeature SDK](https://www.npmjs.com/package/@openfeature/web-sdk) in your app. Learn more by reading OpenFeature's [SDK docs](https://openfeature.dev/docs/reference/technologies/client/web/) and [provider docs](https://openfeature.dev/docs/reference/concepts/provider).

```javascript
import * as Sentry from "@sentry/nextjs";
import { OpenFeature } from "@openfeature/web-sdk";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.openFeatureIntegration()],
});

OpenFeature.setProvider(new MyProviderOfChoice());
OpenFeature.addHooks(new Sentry.OpenFeatureIntegrationHook());

const client = OpenFeature.getClient();
const result = client.getBooleanValue("test-flag", false); // evaluate with a default value
Sentry.captureException(new Error("Something went wrong!"));
```

Visit the Sentry website and confirm that your error event has recorded the feature flag "test-flag" and its value "false".

##### Next Steps

* **Track feature flag evaluations in other parts of your codebase.** If needed, you can set up evaluation tracking for more than one SDK. [Read the docs](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-evaluation-tracking) to learn more.
* **Set up your change tracking webhook.** In order to take full advantage of the feature flag capabilities Sentry offers there is an additional setup step needed. Your feature flag provider needs to notify Sentry when a feature flag definition has changed. A Sentry webhook URL can be registered with your provider. [Learn how](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-change-tracking).

