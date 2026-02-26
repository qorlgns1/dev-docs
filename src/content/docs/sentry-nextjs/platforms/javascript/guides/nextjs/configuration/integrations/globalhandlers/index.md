---
title: 'GlobalHandlers | Next.js용 Sentry'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/globalhandlers'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/globalhandlers

# GlobalHandlers | Next.js용 Sentry

이 통합은 Browser 및 Deno 런타임에서만 작동합니다.

*가져오기 이름: `Sentry.globalHandlersIntegration`*

이 통합은 기본적으로 활성화되어 있습니다. 기본 통합을 수정하려면 [이 문서](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 읽어보세요.

이 통합은 전역 핸들러를 연결해 포착되지 않은 예외와 처리되지 않은 거부를 수집합니다. 기본적으로 오류와 처리되지 않은 promise 거부를 수집합니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.globalHandlersIntegration({ onerror: true, onunhandledrejection: true })],
});
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/globalhandlers.md#options)

- [`onerror`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/globalhandlers.md#onerror)

*유형: `boolean`*

`onerror`로 전파된 오류를 수집합니다.

- [`onunhandledrejection`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/globalhandlers.md#onunhandledrejection)

*유형: `boolean`*

처리되지 않은 promise 거부를 수집합니다.

