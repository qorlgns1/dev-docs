---
title: 'Anr | Next.js용 Sentry'
description: '이 통합은 Node.js 런타임에서만 동작합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anr

# Anr | Next.js용 Sentry

**사용 중단됨**: 이 통합은 더 이상 사용되지 않습니다. 더 나은 성능과 더 포괄적인 모니터링을 위해 대신 [`eventLoopBlockIntegration`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/anr/event-loop-block.md)을 사용하세요.

이 통합은 Node.js 런타임에서만 동작합니다.

*가져오기 이름: `Sentry.anrIntegration`*

`anrIntegration`은 애플리케이션 무응답(ANR)/이벤트 루프 정지 오류를 캡처하여 Sentry 이벤트로 보고합니다. 자세한 내용은 [이벤트 루프 블록 감지](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/event-loop-block.md) 문서를 참고하세요.

```JavaScript
Sentry.init({
  integrations: [Sentry.anrIntegration({ captureStackTrace: true })],
});
```

