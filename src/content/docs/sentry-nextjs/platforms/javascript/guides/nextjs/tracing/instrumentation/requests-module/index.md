---
title: 'HTTP 요청 계측하기 | Sentry for Next.js'
description: '설정할 수 있는 데이터에 대한 자세한 내용은 Requests Module developer specifications를 참고하세요.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/requests-module

# HTTP 요청 계측하기 | Sentry for Next.js

[Requests](https://docs.sentry.io/product/insights/requests.md)를 설정하기 위한 사전 조건으로, 먼저 [tracing 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing.md)을 완료해야 합니다. 이 작업이 끝나면 JavaScript SDK가 자동으로 나가는 HTTP 요청을 계측합니다. 이 방식이 사용 사례에 맞지 않는다면, 이 가이드를 따라 요청을 수동으로 계측하세요.

설정할 수 있는 데이터에 대한 자세한 내용은 [Requests Module developer specifications](https://develop.sentry.dev/sdk/performance/modules/requests/)를 참고하세요.

## [HTTP 요청을 Span으로 감싸기](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/requests-module.md#wrap-http-requests-in-a-span)

span 데이터 속성의 전체 목록은 [HTTP Span Data Conventions](https://develop.sentry.dev/sdk/performance/span-data-conventions/#http)을 참고하세요.

다음은 HTTP 요청을 수행하는 계측된 함수의 예시입니다.

`my-request.js`

```javascript
async function makeRequest(method, url) {
  return await Sentry.startSpan(
    { op: "http.client", name: `${method} ${url}` },
    async (span) => {
      const parsedURL = new URL(url, location.origin);

      span.setAttribute("http.request.method", method);

      span.setAttribute("server.address", parsedURL.hostname);
      span.setAttribute("server.port", parsedURL.port || undefined);

      const response = await fetch(url, {
        method,
      });

      span.setAttribute("http.response.status_code", response.status);
      span.setAttribute(
        "http.response_content_length",
        Number(response.headers.get("content-length")),
      );

      // A good place to set other span attributes

      return response;
    },
  );
}
```

