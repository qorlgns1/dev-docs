---
title: 'NodeFetch | Next.js용 Sentry'
description: '이 통합은 Node.js 및 Bun 런타임에서만 동작합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/nodefetch

# NodeFetch | Next.js용 Sentry

이 통합은 Node.js 및 Bun 런타임에서만 동작합니다.

*Import name: `Sentry.nativeNodeFetchIntegration`*

이 통합은 v8.0.0부터 기본적으로 활성화되어 있습니다. 기본 통합을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nuxt/configuration/integrations.md#modifying-default-integrations)를 읽어보세요.

`nativeNodeFetchIntegration`은 두 가지를 수행합니다:

1. fetch 요청에 대한 span을 수집합니다.
2. fetch 요청에 대한 breadcrumb를 수집합니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.nativeNodeFetchIntegration()],
});
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nuxt/configuration/integrations/nodefetch.md#options)

- [`breadcrumbs`](https://docs.sentry.io/platforms/javascript/guides/nuxt/configuration/integrations/nodefetch.md#breadcrumbs)

*Type: `boolean`*

false로 설정하면 breadcrumb는 수집되지 않습니다.

- [`ignoreOutgoingRequests`](https://docs.sentry.io/platforms/javascript/guides/nuxt/configuration/integrations/nodefetch.md#ignoreoutgoingrequests)

*Type: `(url: string) => boolean`*

URL을 기준으로 나가는 요청을 필터링하는 메서드를 정의할 수 있습니다. 메서드가 `true`를 반환하면 해당 요청은 무시됩니다.

- [`spans`](https://docs.sentry.io/platforms/javascript/guides/nuxt/configuration/integrations/nodefetch.md#spans)

*Type: `boolean`*

false로 설정하면 span은 수집되지 않습니다.

- [`requestHook`](https://docs.sentry.io/platforms/javascript/guides/nuxt/configuration/integrations/nodefetch.md#requesthook)

*Type: `(span: Span, request: Request) => void`*

나가는 fetch 요청에 대해 사용자 지정 속성을 추가하거나 span을 수정할 수 있는 콜백 함수입니다. 이 함수는 span과 네이티브 fetch `Request` 객체를 인자로 호출됩니다.

- [`responseHook`](https://docs.sentry.io/platforms/javascript/guides/nuxt/configuration/integrations/nodefetch.md#responsehook)

*Type: `(span: Span, response: Response) => void`*

나가는 fetch 요청의 응답을 기반으로 사용자 지정 속성을 추가하거나 span을 수정할 수 있는 콜백 함수입니다. 이 함수는 span과 네이티브 fetch `Response` 객체를 인자로 호출됩니다.

