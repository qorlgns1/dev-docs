---
title: 'Kafka | Next.js용 Sentry'
description: '이 통합은 Node.js 및 Bun 런타임에서만 작동합니다. SDK 버전  이상이 필요합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/kafka

# Kafka | Next.js용 Sentry

이 통합은 Node.js 및 Bun 런타임에서만 작동합니다. SDK 버전 `8.30.0` 이상이 필요합니다.

*임포트 이름: `Sentry.kafkaIntegration`*

이 통합은 성능 모니터링이 활성화되면 기본적으로 활성화됩니다. 기본 통합을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 참고하세요.

`kafkaIntegration`은 [`@opentelemetry/instrumentation-kafkajs`](https://www.npmjs.com/package/@opentelemetry/instrumentation-kafkajs)를 사용해 span을 수집할 수 있도록 `kafkajs` 라이브러리에 대한 계측을 추가합니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.kafkaIntegration()],
});
```

## [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/kafka.md#supported-versions)

* `kafkajs`: `>=0.1.0 <3`

