---
title: 'Redis | Next.js용 Sentry'
description: '이 통합은 Node.js 및 Bun 런타임에서만 작동합니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/redis

# Redis | Next.js용 Sentry

이 통합은 Node.js 및 Bun 런타임에서만 작동합니다.

*가져오기 이름: `Sentry.redisIntegration`*

이 통합은 성능 모니터링이 활성화되어 있을 때 기본적으로 활성화됩니다. 기본 통합을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 참고하세요.

`redisIntegration`은 [`@opentelemetry/instrumentation-ioredis`](https://www.npmjs.com/package/@opentelemetry/instrumentation-ioredis) 및 [`@opentelemetry/instrumentation-redis-4`](https://www.npmjs.com/package/@opentelemetry/instrumentation-redis-4)를 사용해 스팬을 수집하기 위해 `ioredis` 및 `redis` 라이브러리에 대한 계측을 추가합니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.redisIntegration()],
});
```

## [지원 버전](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/redis.md#supported-versions)

* `ioredis`: `>=2.0.0 <6`
* `redis`: `>=4.0.0`

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/redis.md#options)

- [`cachePrefixes`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/redis.md#cacheprefixes)

*유형: `(string)[]`*

캐시 스팬으로 수집해야 하는 캐시 키의 접두사를 정의합니다. 예를 들어 이를 `['user:']`로 설정하면 `user:`로 시작하는 캐시 키가 수집됩니다.

