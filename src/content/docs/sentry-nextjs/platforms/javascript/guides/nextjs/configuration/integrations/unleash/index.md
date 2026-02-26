---
title: 'Unleash | Next.js용 Sentry'
description: '이 통합은 브라우저 환경 내부에서만 동작합니다. 패키지 기반 설치(예:  또는 )에서만 사용할 수 있습니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/unleash

# Unleash | Next.js용 Sentry

이 통합은 브라우저 환경 내부에서만 동작합니다. 패키지 기반 설치(예: `npm` 또는 `yarn`)에서만 사용할 수 있습니다.

[Unleash](https://www.getunleash.io/) 통합은 Unleash SDK가 생성한 기능 플래그 평가를 추적합니다. 이러한 평가는 메모리에 보관되며, 오류 및 트랜잭션 이벤트 시 Sentry로 전송됩니다. **현재는 Unleash의 isEnabled 메서드에서 반환되는 boolean 플래그 평가만 지원합니다.** 이 통합은 Sentry SDK **8.51.0 이상 버전**에서 사용할 수 있습니다.

*임포트 이름: `Sentry.unleashIntegration`*

이 통합을 사용하기 전에 앱에 Unleash를 설치하고 계측해야 합니다. 자세한 내용은 [Unleash SDK 레퍼런스](https://docs.getunleash.io/reference/sdks/javascript-browser)와 [빠른 시작 가이드](https://docs.getunleash.io/quickstart)를 참고하세요.

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

Sentry SDK v9에서는 `unleashClientClass` 옵션 이름이 `featureFlagClientClass`로 변경되었습니다. 이에 맞게 업데이트해 주세요.

Sentry 웹사이트에서 오류 이벤트에 기능 플래그 "test-flag"와 그 값 "false"가 기록되었는지 확인하세요.

##### 다음 단계

* **코드베이스의 다른 부분에서도 기능 플래그 평가를 추적하세요.** 필요하다면 둘 이상의 SDK에 대해 평가 추적을 설정할 수 있습니다. 자세한 내용은 [문서](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-evaluation-tracking)를 참고하세요.
* **변경 추적 웹훅을 설정하세요.** Sentry가 제공하는 기능 플래그 기능을 최대한 활용하려면 추가 설정 단계가 필요합니다. 기능 플래그 제공자가 기능 플래그 정의 변경 시 Sentry에 알릴 수 있어야 합니다. Sentry 웹훅 URL을 제공자에 등록할 수 있습니다. [설정 방법 알아보기](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-change-tracking).

