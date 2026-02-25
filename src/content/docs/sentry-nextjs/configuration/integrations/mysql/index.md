---
title: 'MySQL | Next.js용 Sentry'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mysql'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mysql

# MySQL | Next.js용 Sentry

이 통합은 Node.js 및 Bun 런타임에서만 작동합니다.

*가져오기 이름: `Sentry.mysqlIntegration`*

이 통합은 성능 모니터링이 활성화되어 있을 때 기본적으로 활성화됩니다. 기본 통합을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 읽어보세요.

`mysqlIntegration`은 [`@opentelemetry/instrumentation-mysql`](https://www.npmjs.com/package/@opentelemetry/instrumentation-mysql)을 사용해 스팬을 수집할 수 있도록 `mysql` 라이브러리에 계측을 추가합니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.mysqlIntegration()],
});
```

## [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mysql.md#supported-versions)

* `mysql`: `2.x`

