---
title: '요청 격리 | Sentry for Next.js'
description: '서버 사이드 환경에서는 격리 스코프가 요청 경계를 기준으로 자동으로 포크됩니다. 이 작업은 SDK가 자동으로 수행합니다. 그 결과, 각 요청은 자체 격리 스코프를 가지며, 격리 스코프에 설정된 데이터는 해당 요청 중에 캡처된 이벤트에만 적용됩니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/request-isolation

# 요청 격리 | Sentry for Next.js

서버 사이드 환경에서는 [격리 스코프](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md)가 요청 경계를 기준으로 자동으로 포크됩니다. 이 작업은 SDK가 자동으로 수행합니다. 그 결과, 각 요청은 자체 격리 스코프를 가지며, 격리 스코프에 설정된 데이터는 해당 요청 중에 캡처된 이벤트에만 적용됩니다.

하지만 격리가 필요할 수 있는 다른 경우도 있습니다. 예를 들어 백그라운드 작업이나 코드의 특정 부분을 격리하고 싶을 때입니다. 이런 경우에는 `Sentry.withIsolationScope()`를 사용해 전달한 콜백 내부에서 유효한 새 격리 스코프를 만들 수 있습니다. [withIsolationScope](https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/scopes.md#using-withisolationscope) 사용에 대해 자세히 알아보세요.

다음 예시는 `withIsolationScope`를 사용해 특정 작업 실행에 데이터를 연결하는 방법을 보여줍니다.

```javascript
async function job(jobId) {
  return Sentry.withIsolationScope(async () => {
    // Only valid for events in this callback
    Sentry.setTag("jobId", jobId);
    await doSomething();
  });
}
```

