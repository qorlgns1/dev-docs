---
title: 'Generic Pool | Next.js용 Sentry'
description: '이 통합은 Node.js 및 Bun 런타임에서만 동작합니다. SDK 버전  이상이 필요합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/genericpool

# Generic Pool | Next.js용 Sentry

이 통합은 Node.js 및 Bun 런타임에서만 동작합니다. SDK 버전 `8.29.0` 이상이 필요합니다.

*가져오기 이름: `Sentry.genericPoolIntegration`*

이 통합은 성능 모니터링이 활성화되어 있을 때 기본으로 활성화됩니다. 기본 통합을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 참고하세요.

`genericPoolIntegration`은 [`@opentelemetry/instrumentation-generic-pool`](https://www.npmjs.com/package/@opentelemetry/instrumentation-generic-pool)을 사용해 스팬을 캡처할 수 있도록 `generic-pool` 라이브러리에 계측을 추가합니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.genericPoolIntegration()],
});
```

## [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/genericpool.md#supported-versions)

* `generic-pool`: `>=2.0.0 <4`

