---
title: '범용 기능 플래그 통합 | Sentry for Next.js'
description: 'Feature Flags 통합을 사용하면 API를 통해 기능 플래그 평가를 수동으로 추적할 수 있습니다. 이러한 평가는 메모리에 보관되며, 오류 및 트랜잭션 이벤트가 발생할 때 Sentry로 전송됩니다. 현재는 boolean 플래그 평가만 지원합니다.'
---

원문 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/featureflags

# 범용 기능 플래그 통합 | Sentry for Next.js

Feature Flags 통합을 사용하면 API를 통해 기능 플래그 평가를 수동으로 추적할 수 있습니다. 이러한 평가는 메모리에 보관되며, 오류 및 트랜잭션 이벤트가 발생할 때 Sentry로 전송됩니다. **현재는 boolean 플래그 평가만 지원합니다.**

이 통합은 Sentry SDK **8.43.0 이상 버전**에서 사용할 수 있습니다.

*가져오기 이름: `Sentry.featureFlagsIntegration` 및 `type Sentry.FeatureFlagsIntegration`*

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

Sentry 웹사이트에서 오류 이벤트에 기능 플래그 "test-flag"와 해당 값 "false"가 기록되었는지 확인하세요.

##### 다음 단계

* **코드베이스의 다른 부분에서도 기능 플래그 평가를 추적하세요.** 필요한 경우 둘 이상의 SDK에 대해 평가 추적을 설정할 수 있습니다. 자세한 내용은 [문서 읽기](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-evaluation-tracking)를 참고하세요.
* **변경 추적 웹훅을 설정하세요.** Sentry가 제공하는 기능 플래그 기능을 최대한 활용하려면 추가 설정 단계가 필요합니다. 기능 플래그 제공자는 기능 플래그 정의가 변경될 때 Sentry에 알려야 합니다. Sentry 웹훅 URL을 제공자에 등록할 수 있습니다. [설정 방법 알아보기](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-change-tracking).

