---
title: 'BrowserTracing | Next.js용 Sentry'
description: '이 통합은 브라우저 환경에서만 작동합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsertracing

# BrowserTracing | Next.js용 Sentry

이 통합은 브라우저 환경에서만 작동합니다.

*Import name: `Sentry.browserTracingIntegration`*

[tracing](https://docs.sentry.io/product/insights/overview.md)을 사용하면 Sentry가 소프트웨어 성능을 추적하여 처리량(throughput), 지연 시간(latency) 같은 메트릭을 측정하고, 여러 시스템 전반에서 오류의 영향을 보여줍니다. Sentry는 트랜잭션과 스팬으로 구성된 분산 트레이스를 수집하며, 이를 통해 개별 서비스와 해당 서비스 내 개별 작업을 측정합니다.

BrowserTracing 통합은 프런트엔드 애플리케이션을 위한 자동 트레이싱을 설정합니다. 브라우저에서 트랜잭션과 스팬을 수집해 Sentry로 전송합니다.

[BrowserTracing 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md)에 대해 더 알아보세요.

```JavaScript
Sentry.init({
  integrations: [Sentry.browserTracingIntegration()],
});
```

`browserTracingIntegration`에서 사용할 수 있는 전체 옵션 목록은 [Configuration Options](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/automatic-instrumentation.md#configuration-options)를 참고하세요.

