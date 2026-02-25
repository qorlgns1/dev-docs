---
title: 'OpenFeature | Next.js용 Sentry'
description: '이 통합은 브라우저 환경 내부에서만 동작합니다. 패키지 기반 설치(예:  또는 )에서만 사용할 수 있습니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/openfeature

# OpenFeature | Next.js용 Sentry

이 통합은 브라우저 환경 내부에서만 동작합니다. 패키지 기반 설치(예: `npm` 또는 `yarn`)에서만 사용할 수 있습니다.

[OpenFeature](https://openfeature.dev/) 통합은 OpenFeature SDK에서 생성된 기능 플래그 평가를 추적합니다. 이 SDK는 다양한 기능 플래그 제공업체에서 지원됩니다. 전체 목록은 [OpenFeature ecosystem 페이지](https://openfeature.dev/ecosystem/?instant_search%5BrefinementList%5D%5Btype%5D%5B0%5D=Provider\&instant_search%5BrefinementList%5D%5BallTechnologies%5D%5B0%5D=JavaScript)에서 확인하세요.

플래그 평가는 메모리에 보관되며 오류 및 트랜잭션 이벤트 시 Sentry로 전송됩니다. **현재는 boolean 플래그 평가만 지원합니다.** 이 통합은 Sentry SDK **버전 8.43.0 이상**에서 사용할 수 있습니다.

*가져오기 이름: `Sentry.openFeatureIntegration` 및 `Sentry.OpenFeatureIntegrationHook`*

이 통합을 사용하기 전에, 앱에 [OpenFeature SDK](https://www.npmjs.com/package/@openfeature/web-sdk)를 설치하고 계측해야 합니다. 자세한 내용은 OpenFeature의 [SDK 문서](https://openfeature.dev/docs/reference/technologies/client/web/) 및 [provider 문서](https://openfeature.dev/docs/reference/concepts/provider)를 참고하세요.

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

Sentry 웹사이트에서 오류 이벤트에 기능 플래그 "test-flag"와 해당 값 "false"가 기록되었는지 확인하세요.

##### 다음 단계

* **코드베이스의 다른 부분에서도 기능 플래그 평가를 추적하세요.** 필요한 경우 둘 이상의 SDK에 대해 평가 추적을 설정할 수 있습니다. 자세한 내용은 [문서](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-evaluation-tracking)를 참고하세요.
* **변경 추적 webhook을 설정하세요.** Sentry가 제공하는 기능 플래그 기능을 최대한 활용하려면 추가 설정 단계가 필요합니다. 기능 플래그 정의가 변경될 때 기능 플래그 제공업체가 Sentry에 알릴 수 있어야 합니다. Sentry webhook URL을 제공업체에 등록할 수 있습니다. [설정 방법 알아보기](https://docs.sentry.io/platforms/javascript/guides/nextjs/feature-flags.md#enable-change-tracking).

