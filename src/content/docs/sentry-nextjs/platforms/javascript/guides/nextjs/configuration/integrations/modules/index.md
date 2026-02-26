---
title: '모듈 | Next.js용 Sentry'
description: '이 통합은 서버 환경(Node.js, Bun, Deno)에서만 작동합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/modules

# 모듈 | Next.js용 Sentry

이 통합은 서버 환경(Node.js, Bun, Deno)에서만 작동합니다.

*가져오기 이름: `Sentry.modulesIntegration`*

이 통합은 기본적으로 활성화되어 있습니다. 기본 통합 구성을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 참고하세요.

`modulesIntegration`은 설치된 node 모듈/패키지 정보를 이벤트에 수집합니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.modulesIntegration()],
});
```

