---
title: 'Console | Next.js용 Sentry'
description: '이 통합은 콘솔 로그를 breadcrumb로 수집합니다(오류 컨텍스트에 매우 유용합니다!). 하지만 애플리케이션 전체에서 로그를 검색하고 쿼리해야 한다면, 대신 Sentry Logs를 사용하세요. 를 설정하고, SDK 구성에 Sentry console logging i...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/console

# Console | Next.js용 Sentry

##### 혹시 logs를 찾고 계셨나요?

이 통합은 콘솔 로그를 breadcrumb로 수집합니다(오류 컨텍스트에 매우 유용합니다!). 하지만 애플리케이션 전체에서 로그를 검색하고 쿼리해야 한다면, 대신 [Sentry Logs](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md)를 사용하세요. `enableLogs: true`를 설정하고, SDK 구성에 [Sentry console logging integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#integrations)을 추가하세요.

*Import name: `Sentry.consoleIntegration`*

이 통합은 기본적으로 활성화되어 있습니다. 기본 통합을 수정하고 싶다면 [this](https://docs.sentry.io/platforms/javascript/guides/express/configuration/integrations.md#modifying-default-integrations)를 읽어보세요.

`consoleIntegration`은 콘솔 로그에 대한 breadcrumb를 생성합니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.consoleIntegration()],
});
```

