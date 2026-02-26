---
title: 'MongoDB | Next.js용 Sentry'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mongo'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mongo

# MongoDB | Next.js용 Sentry

이 통합은 Node.js 및 Bun 런타임에서만 작동합니다.

*임포트 이름: `Sentry.mongoIntegration`*

이 통합은 성능 모니터링이 활성화되면 기본적으로 활성화됩니다. 기본 통합을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 참고하세요.

`mongoIntegration`은 [`@opentelemetry/instrumentation-mongodb`](https://www.npmjs.com/package/@opentelemetry/instrumentation-mongodb)를 사용해 스팬을 수집할 수 있도록 `mongodb` 라이브러리에 계측을 추가합니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.mongoIntegration()],
});
```

## [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mongo.md#supported-versions)

* `mongodb`: `>=3.3 <7`

