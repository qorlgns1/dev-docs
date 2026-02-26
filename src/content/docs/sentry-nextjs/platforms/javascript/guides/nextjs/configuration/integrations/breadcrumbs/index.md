---
title: 'Breadcrumbs | Next.js용 Sentry'
description: '이 통합은 콘솔 로그를 breadcrumb로 수집합니다(오류 컨텍스트 파악에 매우 유용합니다!). 하지만 애플리케이션 전체에서 로그를 검색하고 쿼리해야 한다면 대신 Sentry Logs를 사용하세요. 를 설정하고, SDK 구성에 Sentry console logging...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs

# Breadcrumbs | Next.js용 Sentry

##### 혹시 logs를 찾고 계셨나요?

이 통합은 콘솔 로그를 breadcrumb로 수집합니다(오류 컨텍스트 파악에 매우 유용합니다!). 하지만 애플리케이션 전체에서 로그를 검색하고 쿼리해야 한다면 대신 [Sentry Logs](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md)를 사용하세요. `enableLogs: true`를 설정하고, SDK 구성에 [Sentry console logging integration](https://docs.sentry.io/platforms/javascript/guides/nextjs/logs.md#integrations)을 추가하세요.

이 통합은 브라우저 환경 내부에서만 동작합니다.

*Import name: `Sentry.breadcrumbsIntegration`*

이 통합은 기본적으로 활성화되어 있습니다. 기본 통합을 수정하고 싶다면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 읽어보세요.

`breadcrumbsIntegration`은 breadcrumb를 수집하기 위해 네이티브 API를 래핑합니다.

기본적으로 Sentry SDK는 breadcrumb를 추가하기 위해 브라우저 API인 `console`, `dom`, `fetch`, `history`, `xhr`를 래핑합니다. 아래 옵션을 통해 애플리케이션의 특정 부분에 대한 breadcrumb 수집을 제외할 수 있습니다(예: `console.log` 호출은 breadcrumb로 수집하지 않도록 설정).

```JavaScript
Sentry.init({
  integrations: [
    Sentry.breadcrumbsIntegration({
      console: true,
      dom: true,
      fetch: true,
      history: true,
      xhr: true,
    }),
  ],
});
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md#options)

- [`console`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md#console)

*Type: `boolean`*

`console.log`, `console.debug` 등의 호출을 기록합니다.

- [`dom`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md#dom)

*Type: `boolean` | `{ serializeAttribute: string | string[] }`*

모든 클릭 및 키 입력 이벤트를 기록합니다.

`serializeAttribute` 키를 가진 객체가 제공되면, Breadcrumbs 통합은 breadcrumb 트레일을 생성하는 동안 DOM 요소에서 지정된 속성을 찾습니다. 일치하는 요소는 `id`나 `class` 이름 대신 해당 사용자 정의 속성과 함께 표시됩니다.

- [`fetch`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md#fetch)

*Type: `boolean`*

Fetch API로 수행된 HTTP 요청을 기록합니다.

- [`history`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md#history)

*Type: `boolean`*

`history.pushState` 및 관련 API 호출을 기록합니다.

- [`sentry`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md#sentry)

*Type: `boolean`*

이벤트를 서버로 전송할 때마다 기록합니다.

- [`xhr`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/breadcrumbs.md#xhr)

*Type: `boolean`*

XHR API로 수행된 HTTP 요청을 기록합니다.

