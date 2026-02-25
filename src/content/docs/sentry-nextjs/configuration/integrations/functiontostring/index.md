---
title: 'FunctionToString | Next.js용 Sentry'
description: '이 통합은 기본적으로 활성화되어 있습니다. 기본 통합을 수정하려면 여기를 읽어보세요.'
---

원문 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/functiontostring

# FunctionToString | Next.js용 Sentry

*Import name: `Sentry.functionToStringIntegration`*

이 통합은 기본적으로 활성화되어 있습니다. 기본 통합을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 읽어보세요.

이 통합을 사용하면 함수나 메서드가 에러 또는 브레드크럼 핸들러로 래핑된 경우에도 SDK가 원래 함수와 메서드 이름을 제공할 수 있습니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.functionToStringIntegration()],
});
```

