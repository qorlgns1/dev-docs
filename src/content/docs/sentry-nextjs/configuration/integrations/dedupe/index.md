---
title: 'Dedupe | Next.js용 Sentry'
description: '이 통합은 기본적으로 활성화되어 있습니다. 기본 통합을 수정하려면 여기를 읽어보세요.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/dedupe

# Dedupe | Next.js용 Sentry

*Import name: `Sentry.dedupeIntegration`*

이 통합은 기본적으로 활성화되어 있습니다. 기본 통합을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 읽어보세요.

이 통합은 특정 이벤트를 중복 제거합니다. 중복 오류를 많이 수신하는 경우 유용할 수 있습니다. 참고로 Sentry는 스택 트레이스와 핑거프린트만 비교합니다.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.dedupeIntegration()],
});
```

