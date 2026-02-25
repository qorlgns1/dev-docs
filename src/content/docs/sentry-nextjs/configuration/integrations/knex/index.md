---
title: 'Knex | Next.js용 Sentry'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/knex'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/knex

# Knex | Next.js용 Sentry

이 통합은 Node.js 및 Bun 런타임에서만 작동합니다. SDK 버전 `8.38.0` 이상이 필요합니다.

*임포트 이름: `Sentry.knexIntegration`*

`knexIntegration`은 [`@opentelemetry/instrumentation-knex`](https://www.npmjs.com/package/@opentelemetry/instrumentation-knex)를 사용해 스팬을 캡처할 수 있도록 `knex` 라이브러리에 대한 인스트루먼테이션을 추가합니다.

```javascript
Sentry.init({
  integrations: [Sentry.knexIntegration()],
});
```

## [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/knex.md#supported-versions)

* `dataloader`: `>=0.10.0 <4`

