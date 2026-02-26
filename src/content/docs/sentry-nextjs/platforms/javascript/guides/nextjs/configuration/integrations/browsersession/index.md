---
title: 'BrowserSession | Next.js용 Sentry'
description: '이 통합은 브라우저 환경에서만 동작합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsersession

# BrowserSession | Next.js용 Sentry

이 통합은 브라우저 환경에서만 동작합니다.

*가져오기 이름: `Sentry.browserSessionIntegration`*

Sentry의 [Release Health](https://docs.sentry.io/product/releases/health.md) 기능을 사용하면 사용자 채택률과 애플리케이션의 크래시 없는 비율을 추적할 수 있습니다. BrowserSession 통합이 활성화되면 사용자가 페이지나 애플리케이션을 로드할 때마다 자동으로 세션을 생성합니다. 이 세션은 릴리스 헬스를 추적하는 데 사용됩니다. 활성 세션 중에 오류가 수집되면 해당 세션은 문제 있는 세션으로 표시됩니다. [세션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/releases.md#sessions)에 대해 더 알아보세요.

```JavaScript
Sentry.init({
  integrations: [Sentry.browserSessionIntegration()],
});
```

## [구성 옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsersession.md#configuration-options)

- [lifecycle](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/browsersession.md#lifecycle)

| 사용 가능 버전 | `10.39.0`           |
| -------------- | ------------------- |
| 타입           | `'route' \| 'page'` |
| 기본값         | `'route'`           |

하나의 세션이 얼마나 오래 유지되는지, 그리고 언제 새 세션이 시작되는지를 제어합니다.

* `'route'`: [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API)를 기준으로 라우트가 변경될 때 새 세션이 시작됩니다. 이것이 기본 동작입니다. 단일 페이지 애플리케이션(SPA)을 구축하는 경우 소프트 내비게이션마다 세션이 하나씩 생성됩니다.
* `'page'`: 하드 페이지 새로고침 또는 내비게이션으로 페이지가 변경될 때 새 세션이 시작됩니다. 단일 페이지 애플리케이션(SPA)을 구축하면서 사용자가 애플리케이션 내에서 이동할 때 여러 라우트에 걸쳐 하나의 세션을 추적하고 싶을 때 유용합니다.

