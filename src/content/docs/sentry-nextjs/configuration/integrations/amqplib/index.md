---
title: 'Amqplib | Next.js용 Sentry'
description: '이 통합은 Node.js 및 Bun 런타임에서만 작동합니다. SDK 버전  이상이 필요합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/amqplib

# Amqplib | Next.js용 Sentry

이 통합은 Node.js 및 Bun 런타임에서만 작동합니다. SDK 버전 `8.32.0` 이상이 필요합니다.

*가져오기 이름: `Sentry.amqplibIntegration`*

이 통합은 성능 모니터링이 활성화되어 있으면 기본적으로 활성화됩니다. 기본 통합 구성을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 참고하세요.

`amqplibIntegration`은 [`@opentelemetry/instrumentation-amqplib`](https://www.npmjs.com/package/@opentelemetry/instrumentation-amqplib)을 사용해 스팬을 수집할 수 있도록 `amqplib` 라이브러리에 계측을 추가합니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.amqplibIntegration()],
});
```

## [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/amqplib.md#supported-versions)

* `amqplib`: `>=0.5.5 <1`

