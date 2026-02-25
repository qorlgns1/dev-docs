---
title: 'ReplayCanvas | Next.js용 Sentry'
description: '이 통합은 브라우저 환경 내부에서만 작동합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/replaycanvas

# ReplayCanvas | Next.js용 Sentry

이 통합은 브라우저 환경 내부에서만 작동합니다.

*가져오기 이름: `Sentry.replayCanvasIntegration`*

Replay Canvas 통합은 HTML canvas 요소에서 [Session Replays](https://docs.sentry.io/product/session-replay.md)를 캡처하는 데 사용할 수 있습니다. 이 기능을 사용하려면 Replay 통합이 활성화되어 있어야 합니다.

현재 canvas 녹화에는 PII 스크러빙이 지원되지 않습니다!

[Canvas 통합으로 Session Replay 설정하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md#canvas-recording)에서 자세히 알아보세요.

```JavaScript
Sentry.init({
  integrations: [Sentry.replayCanvasIntegration()],
});
```

