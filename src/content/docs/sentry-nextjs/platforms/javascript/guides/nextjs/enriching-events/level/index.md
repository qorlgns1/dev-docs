---
title: '이벤트 레벨 | Sentry for Next.js'
description: '레벨은 로깅 레벨과 유사하며, 일반적으로 SDK에서 기본으로 추가됩니다. 에서 전용 레벨을 직접 지정하거나, scope에 레벨을 설정해 모든 이벤트에 적용할 수 있습니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/enriching-events/level

# 이벤트 레벨 | Sentry for Next.js

레벨은 로깅 레벨과 유사하며, 일반적으로 SDK에서 기본으로 추가됩니다. `captureMessage`에서 전용 레벨을 직접 지정하거나, scope에 레벨을 설정해 모든 이벤트에 적용할 수 있습니다.

scope 밖에서 레벨을 설정하려면, 이벤트별로 `captureMessage()`를 호출하면 됩니다:

```javascript
Sentry.captureMessage("this is a debug message", "debug");
```

사용 가능한 레벨은 `"fatal"`, `"error"`, `"warning"`, `"log"`, `"info"`, `"debug"`입니다.

scope 내에서 레벨을 설정하려면 `setLevel()`을 호출할 수 있습니다:

```javascript
Sentry.getCurrentScope().setLevel("warning");
```

또는 이벤트별로:

```javascript
Sentry.withScope(function (scope) {
  scope.setLevel("info");

  // The exception has the event level set by the scope (info).
  Sentry.captureException(new Error("custom error"));
});

// Outside of withScope, the Event level will have their previous value restored.
// The exception has the event level set (error).
Sentry.captureException(new Error("custom error 2"));
```

