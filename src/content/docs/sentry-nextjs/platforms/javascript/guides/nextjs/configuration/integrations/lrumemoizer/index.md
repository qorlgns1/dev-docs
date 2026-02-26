---
title: 'LRU Memoizer | Sentry for Next.js'
description: '이 통합은 Node.js 및 Bun 런타임에서만 작동합니다. SDK 버전  이상이 필요합니다.'
---

원문 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/lrumemoizer

# LRU Memoizer | Sentry for Next.js

이 통합은 Node.js 및 Bun 런타임에서만 작동합니다. SDK 버전 `8.33.0` 이상이 필요합니다.

*가져오기 이름: `Sentry.lruMemoizerIntegration`*

이 통합은 성능 모니터링이 활성화되면 기본적으로 활성화됩니다. 기본 통합을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 읽어보세요.

`lruMemoizerIntegration`은 [`@opentelemetry/instrumentation-lru-memoizer`](https://www.npmjs.com/package/@opentelemetry/instrumentation-lru-memoizer)를 사용해 스팬을 수집할 수 있도록 `lru-memoizer` 라이브러리에 계측을 추가합니다.

```javascript
Sentry.init({
  integrations: [Sentry.lruMemoizerIntegration()],
});
```

## [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/lrumemoizer.md#supported-versions)

* `lru-memoizer`: `>=1.3.0 <3`

