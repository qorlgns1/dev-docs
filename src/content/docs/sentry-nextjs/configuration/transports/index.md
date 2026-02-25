---
title: 'Transports | Next.js용 Sentry'
description: 'JavaScript SDK는 이벤트를 Sentry로 전송하기 위해 를 사용합니다. 최신 브라우저에서는 대부분의 transport가 브라우저의  API를 사용해 이벤트를 전송합니다. 연결 부족으로 전송에 실패하면 transport는 해당 이벤트를 버립니다.'
---

소스 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/transports

# Transports | Next.js용 Sentry

JavaScript SDK는 이벤트를 Sentry로 전송하기 위해 `transport`를 사용합니다. 최신 브라우저에서는 대부분의 transport가 브라우저의 `fetch` API를 사용해 이벤트를 전송합니다. 연결 부족으로 전송에 실패하면 transport는 해당 이벤트를 버립니다.

`init` 호출에서 `transport` 옵션을 설정해 transport를 변경할 수 있습니다. SDK는 몇 가지 내장 transport를 제공하며, 직접 만들 수도 있습니다.

## [`makeBrowserOfflineTransport`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/transports.md#makebrowserofflinetransport)

`makeBrowserOfflineTransport` transport는 브라우저가 오프라인일 때 이벤트를 저장하기 위해 `IndexedDB` API를 사용하는 내장 transport입니다. 브라우저가 다시 온라인 상태가 되면 transport가 저장된 이벤트를 Sentry로 전송합니다. [사용 방법 자세히 보기](https://docs.sentry.io/platforms/javascript/guides/nextjs/best-practices/offline-caching.md)

## [사용자 정의 transport](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/transports.md#custom-transport)

Sentry에 사용자 정의 transport를 제공할 수도 있습니다. transport는 `Transport` 인터페이스를 따라야 합니다:

```javascript
interface Transport {
  send(request: Envelope): Promise<TransportMakeRequestResponse>;
  flush(timeout?: number): Promise<boolean>;
}
```

`@sentry/core`의 `createTransport` 유틸리티를 사용해 일부 보일러플레이트 작업을 도울 수도 있습니다:

```javascript
import { createTransport } from '@sentry/core';
import * from '@sentry/browser';

function makeFetchTransport(
  options
): Transport {
  function makeRequest(request) {
    const requestOptions: RequestInit = {
      body: request.body,
      method: 'POST',
      referrerPolicy: 'origin',
      headers: options.headers,
      ...options.fetchOptions,
    };

    return fetch(options.url, requestOptions).then(response => {
      return {
        statusCode: response.status,
        headers: {
          'x-sentry-rate-limits': response.headers.get('X-Sentry-Rate-Limits'),
          'retry-after': response.headers.get('Retry-After'),
        },
      };
    });
  }

  return createTransport(options, makeRequest);
}

Sentry.init({
  dsn: '___PUBLIC_DSN___',
  transport: makeFetchTransport
});
```

