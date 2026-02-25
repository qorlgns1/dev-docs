---
title: '컨텍스트 | Next.js용 Sentry'
description: '이 통합은 Node.js 런타임에서만 작동합니다.'
---

소스 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodecontext

# 컨텍스트 | Next.js용 Sentry

이 통합은 Node.js 런타임에서만 작동합니다.

*가져오기 이름: `Sentry.nodeContextIntegration`*

이 통합은 기본적으로 활성화되어 있습니다. 기본 통합을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 참고하세요.

`nodeContextIntegration`은 SDK가 실행 중인 환경 및 디바이스에 대한 컨텍스트를 수집하고, 이 정보를 이벤트에 첨부합니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.nodeContextIntegration()],
});
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodecontext.md#options)

- [`app`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodecontext.md#app)

*유형: `boolean`*

false로 설정하면 앱 컨텍스트를 수집하지 않습니다.

- [`os`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodecontext.md#os)

*유형: `boolean`*

false로 설정하면 OS 컨텍스트를 수집하지 않습니다.

- [`device`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodecontext.md#device)

*유형: `boolean | { cpu?: boolean; memory?: boolean; }`*

false로 설정하면 디바이스 컨텍스트를 수집하지 않습니다.

- [`culture`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodecontext.md#culture)

*유형: `boolean`*

false로 설정하면 문화권 컨텍스트를 수집하지 않습니다.

- [`cloudResource`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodecontext.md#cloudresource)

*유형: `boolean`*

false로 설정하면 클라우드 리소스 컨텍스트를 수집하지 않습니다.

