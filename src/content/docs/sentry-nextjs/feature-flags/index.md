---
title: '기능 플래그 설정 | Next.js용 Sentry'
description: '기능 플래그를 평가하기 위해 서드파티 SDK를 사용하는 경우, 해당 평가를 추적하도록 Sentry SDK 통합을 활성화할 수 있습니다. 통합은 제공자별로 다릅니다. 지원되는 SDK 문서는 아래에 나와 있습니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags

# 기능 플래그 설정 | Next.js용 Sentry

## [사전 요구 사항](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#prerequisites)

* [JavaScript SDK가 설치되어 있어야 합니다](https://docs.sentry.io/platforms/javascript/guides/nextjs.md).

## [평가 추적 활성화](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-evaluation-tracking)

기능 플래그를 평가하기 위해 서드파티 SDK를 사용하는 경우, 해당 평가를 추적하도록 Sentry SDK 통합을 활성화할 수 있습니다. 통합은 제공자별로 다릅니다. 지원되는 SDK 문서는 아래에 나와 있습니다.

* [LaunchDarkly](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/launchdarkly.md)
* [OpenFeature](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openfeature.md) (여러 제공자 지원)
* [Statsig](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/statsig.md)
* [Unleash](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unleash.md)

- [일반 통합](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#generic-integration)

일반 `featureFlagsIntegration`을 사용하면 기능 플래그 평가를 수동으로 추적할 수 있습니다. 자세한 내용은 [문서](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/featureflags.md)를 참고하세요.

## [변경 추적 활성화](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-change-tracking)

변경 추적을 사용하려면 기능 플래그 제공자에 Sentry webhook을 등록해야 합니다. 설정 방법은 사용하는 제공자의 문서를 확인하세요.

* [Flagsmith](https://docs.sentry.io/organization/integrations/feature-flag/flagsmith.md#change-tracking)
* [LaunchDarkly](https://docs.sentry.io/organization/integrations/feature-flag/launchdarkly.md#change-tracking)
* [Statsig](https://docs.sentry.io/organization/integrations/feature-flag/statsig.md#change-tracking)
* [Unleash](https://docs.sentry.io/organization/integrations/feature-flag/unleash.md#change-tracking)
* [Generic](https://docs.sentry.io/organization/integrations/feature-flag/generic.md#change-tracking)

