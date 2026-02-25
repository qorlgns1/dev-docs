---
title: 'BrowserProfiling | Next.js용 Sentry'
description: '이 통합은 브라우저 환경 내부에서만 동작합니다.'
---

원문 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browserprofiling

# BrowserProfiling | Next.js용 Sentry

이 통합은 브라우저 환경 내부에서만 동작합니다.

*Import name: `Sentry.browserProfilingIntegration`*

[Profiling](https://docs.sentry.io/product/explore/profiling.md)은 기존 트레이싱을 넘어 더 깊은 수준의 가시성을 제공하여, 커스텀 계측의 필요를 줄이고 프로덕션 환경의 애플리케이션 코드 수준까지 정밀하게 확인할 수 있게 해줍니다.

BrowserProfiling 통합은 프런트엔드 애플리케이션을 위한 자동 성능 프로파일링을 설정합니다. 브라우저의 [JS Self-Profiling API](https://wicg.github.io/js-self-profiling/)를 통해 프로파일을 수집해 Sentry로 전송합니다. 이 통합을 사용하려면 [BrowserTracing 통합](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsertracing.md)도 활성화되어 있어야 합니다.

[BrowserProfiling 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling.md)에 대해 더 알아보세요.

```JavaScript
Sentry.init({
  integrations: [Sentry.browserProfilingIntegration()],
});
```

