---
title: 'Http | Next.js용 Sentry'
description: '이 통합은 서버 환경(Node.js, Bun, Deno)에서만 작동합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http

# Http | Next.js용 Sentry

이 통합은 서버 환경(Node.js, Bun, Deno)에서만 작동합니다.

*가져오기 이름: `Sentry.httpIntegration`*

이 통합은 기본적으로 활성화되어 있습니다. 기본 통합을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 참고하세요.

`httpIntegration`은 두 가지 작업을 수행합니다:

1. HTTP 요청에 대한 breadcrumb를 수집합니다.
2. 나가는 HTTP 요청에 대한 span을 수집합니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.httpIntegration()],
});
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#options)

- [`breadcrumbs`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#breadcrumbs)

*타입: `boolean`* (기본값: `true`)

`false`로 설정하면 breadcrumb를 수집하지 않습니다.

- [`spans`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#spans)

*타입: `boolean`* (기본값: `false`)

`true`로 설정하면 나가는 HTTP 요청에 대한 span이 생성됩니다.

- [`maxIncomingRequestBodySize`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#maxincomingrequestbodysize)

*타입: `'none' | 'small' | 'medium' | 'always'`* (기본값: `'medium'`)

이벤트에 첨부되는 들어오는 HTTP 요청 본문의 최대 크기를 제어합니다.

사용 가능한 옵션:

* 'none': 요청 본문을 첨부하지 않습니다
* 'small': 최대 1,000바이트의 요청 본문을 첨부합니다
* 'medium': 최대 10,000바이트의 요청 본문을 첨부합니다 (기본값)
* 'always': 요청 본문을 항상 첨부합니다

단, `'always'` 설정을 사용해도 성능 및 보안상의 이유로 1MB를 초과하는 본문은 절대 첨부되지 않습니다.

- [`ignoreIncomingRequestBody`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#ignoreincomingrequestbody)

*타입: `(url: string, request: RequestOptions) => boolean`*

주어진 콜백이 `true`를 반환하는 URL의 들어오는 HTTP 요청에 대해 요청 본문을 무시할 수 있습니다. 본문이 필요 없고 수집을 피하고 싶은 장시간 실행 요청에 유용합니다.

콜백 함수는 두 개의 인수를 받습니다:

* `url`: 프로토콜, 호스트, 포트, 경로, 쿼리 문자열을 포함한 들어오는 요청의 전체 URL입니다. 예: `https://example.com/users?name=John`.
* `request`: 들어오는 요청의 옵션을 담고 있는 `RequestOptions` 타입 객체입니다. 요청 메서드나 헤더 같은 속성으로 필터링할 때 사용할 수 있습니다.

- [`ignoreOutgoingRequests`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#ignoreoutgoingrequests)

*타입: `(url: string, request: RequestOptions) => boolean`*

URL을 기준으로 나가는 요청을 필터링하는 메서드를 정의할 수 있습니다. 이 메서드가 `true`를 반환하면 해당 나가는 요청에 대해 span이나 breadcrumb를 수집하지 않습니다.

콜백 함수는 두 개의 인수를 받습니다:

* `url`: 프로토콜, 호스트, 포트, 경로, 쿼리 문자열을 포함한 나가는 요청의 전체 URL입니다. 예: `https://example.com/users?name=John`.
* `request`: 나가는 요청의 옵션을 담고 있는 `RequestOptions` 타입 객체입니다. 요청 메서드나 헤더 같은 속성으로 필터링할 때 사용할 수 있습니다.

- [`ignoreIncomingRequests`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#ignoreincomingrequests)

*타입: `(urlPath: string, request: IncomingMessage) => boolean`*

URL을 기준으로 들어오는 요청을 필터링하는 메서드를 정의할 수 있습니다. 이 메서드가 `true`를 반환하면 해당 들어오는 요청에 대해 span 또는 transaction을 수집하지 않습니다.

콜백 함수는 두 개의 인수를 받습니다:

* `urlPath`: 들어오는 요청의 URL 경로이며, 가능한 경우 쿼리 문자열을 포함합니다. 예: `/users?name=John`.
* `request`: 들어오는 요청을 담고 있는 `IncomingMessage` 타입 객체입니다. 요청 메서드나 헤더 같은 속성으로 필터링할 때 사용할 수 있습니다.

- [`ignoreStaticAssets`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#ignorestaticassets)

*타입: `boolean`* (기본값: `true`)

`true`로 설정하면 이미지, 폰트 및 기타 파일 같은 정적 에셋에 대해 span을 수집하지 않습니다.

- [`disableIncomingRequestSpans`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#disableincomingrequestspans)

*타입: `boolean`*

`true`로 설정하면 들어오는 요청에 대한 span이 생성되지 않습니다.

- [`dropSpansForIncomingRequestStatusCodes`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#dropspansforincomingrequeststatuscodes)

*타입: `(number | [number, number])[]`* (기본값: `[[401, 404], [301, 303], [305, 399]]`)

지정한 상태 코드의 들어오는 HTTP 요청에 대해서는 span을 수집하지 않습니다. 기본적으로 일부 3xx 및 4xx 상태 코드의 span은 무시됩니다. 개별 상태 코드(숫자) 또는 범위(`(2`개 요소 배열 `[start, end]`로, `start`와 `end` 모두 포함)를 담을 수 있는 배열을 기대합니다.

예를 들어 `[[300, 399], 404]`는 모든 3xx 상태 코드(300~399, 양끝 포함)와 404 상태 코드를 무시합니다.

- [`trackIncomingRequestsAsSessions`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#trackincomingrequestsassessions)

*타입: `boolean`* (기본값: `true`)

이 통합이 들어오는 요청에 대해 [Sessions](https://docs.sentry.io/product/releases/health.md#sessions)를 생성해 Sentry에서 릴리스의 상태와 crash-free 비율을 추적할지 결정합니다. [Release Health](https://docs.sentry.io/product/releases/health.md)에 대해 더 알아보세요.

- [`sessionFlushingDelayMS`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#sessionflushingdelayms)

*타입: `number`* (기본값: `60000`)

세션 집계로 세션이 플러시되기 전까지의 지연 시간(밀리초)입니다. 이 값은 세션 데이터가 Sentry로 전송되는 빈도를 제어합니다.

- [`instrumentation`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/http.md#instrumentation)

[기반 OpenTelemetry Instrumentation](https://www.npmjs.com/package/@opentelemetry/instrumentation-http)에도 일부 훅을 전달할 수 있습니다:

```typescript
httpIntegration({
  instrumentation?: {
    requestHook?: (span: Span, req: ClientRequest | HTTPModuleRequestIncomingMessage) => void;
    responseHook?: (span: Span, response: HTTPModuleRequestIncomingMessage | ServerResponse) => void;
    applyCustomAttributesOnSpan?: (
      span: Span,
      request: ClientRequest | HTTPModuleRequestIncomingMessage,
      response: HTTPModuleRequestIncomingMessage | ServerResponse,
    ) => void;
});
```

