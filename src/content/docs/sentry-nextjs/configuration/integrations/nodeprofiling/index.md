---
title: 'NodeProfiling | Next.js용 Sentry'
description: '이 통합은 Node.js 런타임에서만 동작합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodeprofiling

# NodeProfiling | Next.js용 Sentry

이 통합은 Node.js 런타임에서만 동작합니다.

`nodeProfilingIntegration`은 `@sentry/profiling-node` 패키지에서 가져와야 합니다.

[프로파일링](https://docs.sentry.io/product/explore/profiling.md)은 기존 트레이싱에 더해 한층 깊은 가시성을 제공하여, 커스텀 계측의 필요성을 줄이고 프로덕션 환경에서 애플리케이션 코드 수준의 정밀한 가시성을 가능하게 합니다.

NodeProfiling 통합은 Node.js 애플리케이션을 위한 자동 성능 프로파일링을 설정합니다. v8을 통해 프로파일을 수집하고 이를 Sentry로 전송합니다. 이 통합을 사용하려면 성능 모니터링도 활성화되어 있어야 합니다.

[NodeProfiling 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/profiling.md)에 대해 더 알아보세요.

```JavaScript
const Sentry = require("@sentry/node");
const { nodeProfilingIntegration } = require("@sentry/profiling-node");

Sentry.init({
  integrations: [nodeProfilingIntegration()],
});
```

