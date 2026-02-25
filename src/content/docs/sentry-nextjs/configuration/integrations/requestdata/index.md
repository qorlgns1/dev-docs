---
title: 'RequestData | Next.js용 Sentry'
description: '이 통합은 백엔드에서 요청 처리 중 발생하는 트랜잭션 및 오류 이벤트에 들어오는 요청의 데이터를 추가합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/requestdata

# RequestData | Next.js용 Sentry

*가져오기 이름: `Sentry.Integrations.RequestData`*

이 통합은 백엔드에서 요청 처리 중 발생하는 트랜잭션 및 오류 이벤트에 들어오는 요청의 데이터를 추가합니다.

이 통합은 서버에서만 사용할 수 있습니다.

## [옵션:](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/requestdata.md#options)

* `include` (object)

이벤트에 어떤 유형의 데이터를 추가할지 제어합니다:

```javascript
{
  cookies: boolean; // default: true,
  data: boolean; // default: true,
  headers: boolean; // default: true,
  ip: boolean; // default: false,
  query_string: boolean; // default: true,
  url: boolean; // default: true,
}
```

* `transactionNamingSchema` (string)

트랜잭션이 어떻게 보고될지 제어합니다. 옵션은 'path' (`/some/route`), 'methodPath' (`GET /some/route`), 'handler'(사용 가능한 경우 라우트 핸들러 함수 이름)입니다. 기본값은 `methodPath`입니다.

