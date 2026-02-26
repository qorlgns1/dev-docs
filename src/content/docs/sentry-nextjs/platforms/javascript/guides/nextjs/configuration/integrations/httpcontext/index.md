---
title: 'HttpContext | Next.js용 Sentry'
description: '이 통합은 브라우저 환경 내부에서만 작동합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpcontext

# HttpContext | Next.js용 Sentry

이 통합은 브라우저 환경 내부에서만 작동합니다.

*Import name: `Sentry.httpContextIntegration`*

이 통합은 기본적으로 활성화되어 있습니다. 기본 통합을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 참고하세요.

이 통합은 URL, user-agent, referrer 및 기타 헤더 같은 HTTP 요청 정보를 이벤트에 첨부합니다. 이를 통해 특정 OS, 브라우저, 버전 정보로 이벤트를 정확하게 분류하고 태그할 수 있습니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.httpContextIntegration()],
});
```

