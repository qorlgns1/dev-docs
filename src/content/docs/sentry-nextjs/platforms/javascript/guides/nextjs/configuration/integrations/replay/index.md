---
title: 'Replay | Next.js용 Sentry'
description: '이 통합은 브라우저 환경에서만 작동합니다.'
---

원문 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/replay

# Replay | Next.js용 Sentry

이 통합은 브라우저 환경에서만 작동합니다.

*가져오기 이름: `Sentry.replayIntegration`*

[Session Replay](https://docs.sentry.io/product/explore/session-replay.md)는 사용자의 브라우저에서 이슈 발생 전, 발생 중, 발생 후에 어떤 일이 있었는지를 동영상처럼 재현해 보여 주어, 오류나 지연(latency) 문제의 근본 원인을 더 빠르게 파악할 수 있도록 도와줍니다. 브라우저의 DevTools에서 영감을 받은 하나의 통합 UI에서 애플리케이션의 DOM 상태를 되감아 다시 확인하고, 마우스 클릭, 스크롤, 네트워크 요청, 콘솔 항목 같은 주요 사용자 상호작용을 볼 수 있습니다.

[Session Replay 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/session-replay.md)에 대해 더 알아보세요.

```JavaScript
Sentry.init({
  integrations: [Sentry.replayIntegration()],
});
```

