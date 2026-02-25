---
title: 'MySQL2 | Next.js용 Sentry'
description: '이 통합은 Node.js 및 Bun 런타임에서만 동작합니다.'
---

원문 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mysql2

# MySQL2 | Next.js용 Sentry

이 통합은 Node.js 및 Bun 런타임에서만 동작합니다.

*import 이름: `Sentry.mysql2Integration`*

이 통합은 성능 모니터링이 활성화되어 있으면 기본적으로 활성화됩니다. 기본 통합을 수정하려면 [이 문서](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 읽어보세요.

`mysql2Integration`은 [`@opentelemetry/instrumentation-mysql2`](https://www.npmjs.com/package/@opentelemetry/instrumentation-mysql2)를 사용해 스팬을 수집할 수 있도록 `mysql2` 라이브러리에 계측을 추가합니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.mysql2Integration()],
});
```

## [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/mysql2.md#supported-versions)

* `mysql2`: `>= 1.4.2, < 4.0`

