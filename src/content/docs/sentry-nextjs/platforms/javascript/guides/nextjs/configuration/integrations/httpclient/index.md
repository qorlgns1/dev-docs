---
title: 'HttpClient | Next.js용 Sentry'
description: '이 통합은 브라우저 환경 내부에서만 동작합니다.'
---

원문 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpclient

# HttpClient | Next.js용 Sentry

이 통합은 브라우저 환경 내부에서만 동작합니다.

*Import 이름: `Sentry.httpClientIntegration`*

이 통합은 Fetch 및 XHR의 실패한 요청에서 발생한 오류를 캡처하고, 요청 및 응답 정보를 첨부합니다.

기본적으로 오류 이벤트에는 헤더 또는 쿠키 데이터가 포함되지 않습니다. 이 동작은 루트 `Sentry.init({})` 설정에서 `sendDefaultPii: true`를 설정해 변경할 수 있습니다.

```javascript
import * as Sentry from "@sentry/browser";

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.httpClientIntegration()]

  // This option is required for capturing headers and cookies.
  sendDefaultPii: true,
});
```

##### 참고

Fetch 및 XHR API의 한계로 인해, 요청 및 응답에 대한 쿠키와 헤더 수집은 최선의 노력(best effort) 기반으로 이루어집니다. 즉, 통합이 생성한 이벤트에서 일부 헤더가 누락될 수 있습니다.

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpclient.md#options)

- [`failedRequestStatusCodes`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpclient.md#failedrequeststatuscodes)

*유형: `(number|[number, number])[]`*

이 배열에는 `[begin, end]`(양 끝값 포함) 형태의 튜플, 단일 상태 코드 또는 둘의 조합을 넣을 수 있습니다. 기본값: `[[500, 599]]`

- [`failedRequestTargets`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpclient.md#failedrequesttargets)

*유형: `(string|RegExp)[]`*

고려해야 할 요청 대상 배열입니다. 예를 들어 `['http://example.com/api/test']`는 이 URL로의 모든 요청을 실패로 해석합니다. 이 배열에는 정규식, 문자열 또는 둘의 조합을 넣을 수 있습니다. 기본값: `[/.*/]`

- [`sendDefaultPii`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/httpclient.md#senddefaultpii)

*유형: `boolean`*

이 옵션은 통합 옵션이 아니라 루트 Sentry.init 옵션에 지정해야 합니다!

헤더와 쿠키를 캡처하려면 이 옵션이 필요합니다.

