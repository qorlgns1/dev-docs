---
title: 'Dataloader | Next.js용 Sentry'
description: '이 통합은 Node.js 및 Bun 런타임에서만 동작합니다. SDK 버전  이상이 필요합니다.'
---

원문 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/dataloader

# Dataloader | Next.js용 Sentry

이 통합은 Node.js 및 Bun 런타임에서만 동작합니다. SDK 버전 `8.31.0` 이상이 필요합니다.

*임포트 이름: `Sentry.dataloaderIntegration`*

`dataloaderIntegration`은 [`@opentelemetry/instrumentation-dataloader`](https://www.npmjs.com/package/@opentelemetry/instrumentation-dataloader)를 사용해 span을 수집할 수 있도록 `dataloader` 라이브러리에 계측을 추가합니다.

```javascript
Sentry.init({
  integrations: [Sentry.dataloaderIntegration()],
});
```

## [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/dataloader.md#supported-versions)

* `dataloader`: `>=2.0.0 <3`

