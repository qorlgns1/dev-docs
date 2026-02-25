---
title: 'Statsig | Sentry for Next.js'
description: '이 통합은 브라우저 환경 내부에서만 동작합니다. 또한 패키지 기반 설치(예:  또는 )에서만 사용할 수 있습니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/statsig

# Statsig | Sentry for Next.js

이 통합은 브라우저 환경 내부에서만 동작합니다. 또한 패키지 기반 설치(예: `npm` 또는 `yarn`)에서만 사용할 수 있습니다.

[Statsig](https://www.statsig.com/) 통합은 Statsig JavaScript Client SDK가 생성한 기능 플래그 평가를 추적합니다. 이러한 평가는 메모리에 보관되며, 오류 및 트랜잭션 이벤트 발생 시 Sentry로 전송됩니다. **현재는 Statsig의 `checkGate` 메서드에서 생성된 불리언 플래그 평가만 지원합니다**. 자세한 내용은 [Statsig feature gates](https://docs.statsig.com/feature-flags/working-with/)를 참고하세요.

이 통합은 Sentry SDK **9.0.0 이상 버전**, 또는 **v8의 경우 8.55.0 이상 버전**에서 사용할 수 있습니다.

*Import name: `Sentry.statsigIntegration`*

이 통합을 사용하기 전에, 앱에 Statsig를 설치하고 계측해야 합니다. 자세한 내용은 [Statsig's SDK reference](https://docs.statsig.com/client/javascript-sdk)와 [quickstart guide](https://docs.statsig.com/guides/first-feature)를 확인하세요.

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

Sentry 웹사이트에서 오류 이벤트에 기능 플래그 "my-feature-gate"와 해당 값 "false"가 기록되었는지 확인하세요.

##### Next Steps

* **코드베이스의 다른 부분에서 기능 플래그 평가 추적하기.** 필요한 경우 둘 이상의 SDK에 대해 평가 추적을 설정할 수 있습니다. 자세한 내용은 [Read the docs](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-evaluation-tracking)를 참고하세요.
* **변경 추적 웹훅 설정하기.** Sentry가 제공하는 기능 플래그 기능을 최대한 활용하려면 추가 설정 단계가 필요합니다. 기능 플래그 제공자는 기능 플래그 정의가 변경될 때 Sentry에 알려야 합니다. Sentry 웹훅 URL을 제공자에 등록할 수 있습니다. [Learn how](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-change-tracking).

