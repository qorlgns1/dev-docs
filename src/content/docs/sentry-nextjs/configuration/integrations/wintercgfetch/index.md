---
title: 'WinterCGFetch | Next.js용 Sentry'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/wintercgfetch'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/wintercgfetch

# WinterCGFetch | Next.js용 Sentry

이 통합은 Edge runtime에서만 작동합니다.

*Import 이름: `Sentry.winterCGFetchIntegration`*

이 통합은 기본적으로 활성화되어 있습니다. 기본 통합을 수정하려면 [이 문서](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 읽어보세요.

`winterCGFetchIntegration`은 Edge runtime에서 fetch 요청에 대해 span을 생성하고 tracing 헤더를 첨부합니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.winterCGFetchIntegration()],
});
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/wintercgfetch.md#options)

- [`breadcrumbs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/wintercgfetch.md#breadcrumbs)

*유형: `boolean`*

false로 설정하면 breadcrumbs가 캡처되지 않습니다.

- [`shouldCreateSpanForRequest`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/wintercgfetch.md#shouldcreatespanforrequest)

*유형: `(url: string) => boolean`*

지정한 URL로의 아웃고잉 요청을 추적하기 위해 span을 생성할지 여부를 결정하는 메서드를 정의할 수 있습니다. 기본적으로 모든 아웃고잉 요청에 대해 span이 생성됩니다.

