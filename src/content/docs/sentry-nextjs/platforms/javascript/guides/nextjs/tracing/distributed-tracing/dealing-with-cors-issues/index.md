---
title: 'CORS 문제 다루기 | Next.js용 Sentry'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/dealing-with-cors-issues'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/dealing-with-cors-issues

# CORS 문제 다루기 | Next.js용 Sentry

프런트엔드와 백엔드가 서로 다른 도메인에 호스팅되어 있다면(예: 프런트엔드는 `https://example.com`, 백엔드는 `https://api.example.com`), 브라우저에서 요청이 차단되지 않도록 백엔드의 [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Headers) 헤더를 설정해야 합니다.

## [트레이스 전파 이해하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/dealing-with-cors-issues.md#understanding-trace-propagation)

Sentry는 모든 외부 요청에 `sentry-trace` 및 `baggage`(선택적으로 `traceparent`) 헤더를 붙이지 않습니다. 대신 `tracePropagationTargets` 설정 옵션에 지정한 패턴과 URL이 일치하는 요청에만 이 헤더를 추가합니다.

기본적으로 `tracePropagationTargets`는 `['localhost', /^\//]`로 설정되어 있으며, 이는 트레이스 헤더가 다음 요청에만 추가된다는 뜻입니다.

* URL에 `localhost`가 포함된 요청(예: `http://localhost:3000/api`)
* URL이 `/`로 시작하는 요청(예: `/api/users`, `/graphql`)

이 기본 동작은 서드파티 서비스로 트레이스 데이터가 전송되는 것을 방지하고, 잠재적인 CORS 문제를 피하는 데 도움이 됩니다.

## [트레이스 전파 설정하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/dealing-with-cors-issues.md#configuring-trace-propagation)

서로 다른 도메인 간에 분산 트레이싱을 활성화하려면, `tracePropagationTargets`에 백엔드 서비스 URL을 포함하도록 설정해야 합니다.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.browserTracingIntegration()],
  tracePropagationTargets: [
    "localhost", // For local development
    /^\/api\//, // For same-origin API calls
    "https://api.example.com", // For your backend domain
    "https://auth.example.com", // For additional services
  ],
});
```

## [CORS 헤더 설정하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/dealing-with-cors-issues.md#configuring-cors-headers)

`tracePropagationTargets`에 백엔드 도메인을 포함하도록 설정했다면, 이제 트레이스 헤더를 허용하도록 백엔드를 설정해야 합니다.

```bash
Access-Control-Allow-Headers: sentry-trace, baggage
```

서버의 정확한 설정은 환경에 따라 달라지지만, 중요한 점은 `sentry-trace`와 `baggage` 헤더를 모두 허용하는 것입니다.

- [W3C traceparent 헤더](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/dealing-with-cors-issues.md#w3c-traceparent-header)

[`propagateTraceparent` option](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/options.md#propagateTraceparent)을 `true`로 설정한 경우, `traceparent` 헤더도 허용해야 합니다.

```bash
Access-Control-Allow-Headers: sentry-trace, baggage, traceparent
```

## [트레이스 전파 비활성화하기](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/distributed-tracing/dealing-with-cors-issues.md#disabling-trace-propagation)

분산 트레이싱을 완전히 비활성화하고 어떤 트레이스 헤더도 전송되지 않게 하려면 다음과 같이 설정하세요.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  // Empty array prevents all trace header propagation
  tracePropagationTargets: [],
});
```

