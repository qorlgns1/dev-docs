---
title: 'Tedious | Next.js용 Sentry'
description: '이 통합은 Node.js 및 Bun 런타임에서만 동작합니다. SDK 버전  이상이 필요합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/tedious

# Tedious | Next.js용 Sentry

이 통합은 Node.js 및 Bun 런타임에서만 동작합니다. SDK 버전 `8.38.0` 이상이 필요합니다.

*가져오기 이름: `Sentry.tediousIntegration`*

이 통합은 성능 모니터링이 활성화되어 있을 때 기본적으로 활성화됩니다. 기본 통합을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 참고하세요.

`tediousIntegration`은 [`@opentelemetry/instrumentation-tedious`](https://www.npmjs.com/package/@opentelemetry/instrumentation-tedious)를 사용해 스팬을 수집할 수 있도록 `tedious` 라이브러리에 대한 계측을 추가합니다.

```javascript
Sentry.init({
  integrations: [Sentry.tediousIntegration()],
});
```

## [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/tedious.md#supported-versions)

* `tedious`: `>=1.11.0 <20`

