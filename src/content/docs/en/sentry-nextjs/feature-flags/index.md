---
title: 'Set Up Feature Flags | Sentry for Next.js'
description: 'If you use a third-party SDK to evaluate feature flags, you can enable a Sentry SDK integration to track those evaluations. Integrations are provider ...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags

# Set Up Feature Flags | Sentry for Next.js

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#prerequisites)

* You have the [JavaScript SDK installed](https://docs.sentry.io/platforms/javascript/guides/nextjs.md).

## [Enable Evaluation Tracking](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-evaluation-tracking)

If you use a third-party SDK to evaluate feature flags, you can enable a Sentry SDK integration to track those evaluations. Integrations are provider specific. Documentation for supported SDKs is listed below.

* [LaunchDarkly](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/launchdarkly.md)
* [OpenFeature](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openfeature.md) (multiple providers supported)
* [Statsig](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/statsig.md)
* [Unleash](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unleash.md)

- [Generic Integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#generic-integration)

The generic `featureFlagsIntegration` allows you to manually track feature flag evaluations. Read the [documentation](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/featureflags.md) to learn more.

## [Enable Change Tracking](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-change-tracking)

Change tracking requires registering a Sentry webhook with a feature flag provider. For set up instructions, visit the documentation for your provider:

* [Flagsmith](https://docs.sentry.io/organization/integrations/feature-flag/flagsmith.md#change-tracking)
* [LaunchDarkly](https://docs.sentry.io/organization/integrations/feature-flag/launchdarkly.md#change-tracking)
* [Statsig](https://docs.sentry.io/organization/integrations/feature-flag/statsig.md#change-tracking)
* [Unleash](https://docs.sentry.io/organization/integrations/feature-flag/unleash.md#change-tracking)
* [Generic](https://docs.sentry.io/organization/integrations/feature-flag/generic.md#change-tracking)

