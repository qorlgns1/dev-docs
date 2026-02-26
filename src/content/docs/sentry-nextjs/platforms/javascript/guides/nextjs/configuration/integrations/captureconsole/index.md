---
title: 'CaptureConsole | Next.js용 Sentry'
description: '이 통합은 모든 Console API 호출을 캡처하고, 로그 레벨에 따라 SDK의 captureMessage 또는 captureException 호출을 사용해 Sentry로 리디렉션합니다. 그런 다음 기본 네이티브 동작을 유지하기 위해 다시 트리거합니다:'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/captureconsole

# CaptureConsole | Next.js용 Sentry

*임포트 이름: `Sentry.captureConsoleIntegration`*

이 통합은 모든 Console API 호출을 캡처하고, 로그 레벨에 따라 SDK의 captureMessage 또는 captureException 호출을 사용해 Sentry로 리디렉션합니다. 그런 다음 기본 네이티브 동작을 유지하기 위해 다시 트리거합니다:

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.captureConsoleIntegration()],
});
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/captureconsole.md#options)

- [`levels`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/captureconsole.md#levels)

*유형: `string[]`*

캡처해야 하는 메서드 배열입니다. 기본값은 `['log', 'info', 'warn', 'error', 'debug', 'assert']`입니다.

