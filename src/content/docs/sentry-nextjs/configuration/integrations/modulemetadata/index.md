---
title: 'ModuleMetadata | Next.js용 Sentry'
description: '이 통합은 브라우저 환경에서만 동작합니다.'
---

원문 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/modulemetadata

# ModuleMetadata | Next.js용 Sentry

이 통합은 브라우저 환경에서만 동작합니다.

*Import name: `Sentry.moduleMetadataIntegration`*

메타데이터는 Sentry 번들러 플러그인에서 `_experiments.moduleMetadata` 구성 옵션을 사용해 주입할 수 있습니다. 이 통합을 추가하면 번들러 플러그인에 전달된 메타데이터가 모든 이벤트의 스택 프레임에 `module_metadata` 속성으로 추가됩니다. 이를 통해 서로 다른 팀이나 소스에서 발생한 이벤트를 태그하거나 라우팅하는 데 도움을 줄 수 있습니다.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.moduleMetadataIntegration()],
});
```

