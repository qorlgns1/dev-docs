---
title: 'Postgres | Next.js용 Sentry'
description: '이 통합은 Node.js 및 Bun 런타임에서만 작동합니다.'
---

원문 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/postgres

# Postgres | Next.js용 Sentry

이 통합은 Node.js 및 Bun 런타임에서만 작동합니다.

*Import name: `Sentry.postgresIntegration`*

이 통합은 성능 모니터링이 활성화되어 있으면 기본적으로 활성화됩니다. 기본 통합을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 참고하세요.

`postgresIntegration`은 [`@opentelemetry/instrumentation-pg`](https://www.npmjs.com/package/@opentelemetry/instrumentation-pg)를 사용해 스팬을 수집하기 위해 `pg` 라이브러리에 계측을 추가합니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.postgresIntegration()],
});
```

## [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/postgres.md#supported-versions)

* `pg`: `>=8 <9`

