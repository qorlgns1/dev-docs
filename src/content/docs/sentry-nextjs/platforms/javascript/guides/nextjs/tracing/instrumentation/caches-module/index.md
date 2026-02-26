---
title: '캐시 계측 | Next.js용 Sentry'
description: '캐시는 데이터 조회를 더 빠르게 만들어 애플리케이션 성능을 향상시키는 데 사용할 수 있습니다. 잠재적으로 느린 데이터 계층에서 데이터를 가져오는 대신(최상의 경우) 애플리케이션이 메모리에서 데이터를 가져오기 때문입니다. 캐싱은 Q\\&A 포털, 게임, 미디어 공유, 소셜...'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/caches-module

# 캐시 계측 | Next.js용 Sentry

캐시는 데이터 조회를 더 빠르게 만들어 애플리케이션 성능을 향상시키는 데 사용할 수 있습니다. 잠재적으로 느린 데이터 계층에서 데이터를 가져오는 대신(최상의 경우) 애플리케이션이 메모리에서 데이터를 가져오기 때문입니다. 캐싱은 Q\&A 포털, 게임, 미디어 공유, 소셜 네트워킹 같은 애플리케이션의 읽기 중심 워크로드를 가속화할 수 있습니다.

Sentry는 [캐시 모니터링 대시보드](https://sentry.io/orgredirect/organizations/:orgslug/insights/backend/caches/)를 제공하며, Sentry의 Redis 통합을 사용해 자동 계측할 수 있습니다(곧 더 많은 통합이 추가될 예정).

## [Redis 클라이언트를 사용한 계측](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/caches-module.md#instrumentation-with-redis-clients)

`ioredis` 또는 `redis` 같은 Redis 클라이언트로 데이터를 캐시하는 경우, `redisIntegration` 옵션 안에 `cachePrefixes`를 지정해야 합니다. 이 설정을 통해 Sentry는 정의된 접두사를 가진 키에 대한 접근을 "cache operations"로 분류할 수 있습니다.

```javascript
Sentry.init({
  integrations: [
    redisIntegration({
      cachePrefixes: ["posts:", "authors:"],
    }),
  ],
});
```

## [수동 계측](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/caches-module.md#manual-instrumentation)

Sentry의 Redis 통합 외 다른 방식을 사용 중이라면, 아래 단계에 따라 [Cache Module](https://sentry.io/orgredirect/organizations/:orgslug/insights/backend/caches/)을 수동으로 계측해야 합니다.

두 개의 span을 만들어야 합니다. 하나는 캐시에 무언가를 넣는 작업을 나타내고, 다른 하나는 캐시에서 무언가를 가져오는 작업을 나타냅니다.

설정 가능한 데이터에 대한 자세한 내용은 [Cache Module Developer Specification](https://develop.sentry.dev/sdk/performance/modules/caches/)을 참고하세요.

- [1단계: 캐시에 데이터를 넣을 때 Span 추가](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/caches-module.md#step-1-add-span-when-putting-data-into-the-cache)

다음 커스텀 계측 지침에 따라 캐시 설정 span을 전송하세요:

1. 사용 중인 캐시 라이브러리로 캐시 값을 설정합니다.
2. 캐시된 값을 사용하는 애플리케이션 부분을 `Sentry.startSpan(...)`으로 감쌉니다.
3. `name`을 "Setting auth cache"처럼 설명적인 값으로 설정합니다.
4. `op`를 `cache.set`으로 설정합니다.
5. `cache.key`를 설정하는 키를 나타내는 문자열 배열로 설정합니다.
6. 선택적으로 `cache.item_size` 같은 다른 속성도 설정할 수 있습니다. (자세한 내용은 [Cache Module Span Data Conventions](https://develop.sentry.dev/sdk/performance/modules/caches/#span-data) 참고)

(위에서 설명한 단계는 스니펫에도 문서화되어 있습니다.)

`my-cache.js`

```javascript
const key = "myCacheKey123";
const value = "The value I want to cache.";

Sentry.startSpan(
  {
    name: key,
    attributes: {
      "cache.key": [key],
      "cache.item_size": JSON.stringify(value).length, // Warning: if value is very big this could use lots of memory
      "network.peer.address": "cache.example.com/supercache",
      "network.peer.port": 9000,
    },
    op: "cache.put",
  },
  (span) => {
    // Set a key in your caching using your custom caching solution
    my_caching.set(key, value);
  },
);
```

- [2단계: 캐시에서 데이터를 조회할 때 Span 추가](https://docs.sentry.io/platforms/javascript/guides/nextjs/tracing/instrumentation/caches-module.md#step-2-add-span-when-retrieving-data-from-the-cache)

사용 중인 캐시가 위에서 언급한 자동 계측을 지원하지 않는다면, 아래 커스텀 계측 지침을 사용해 대신 캐시 span을 전송할 수 있습니다:

1. 사용 중인 캐시 라이브러리에서 캐시된 값을 가져옵니다.
2. 캐시에서 가져오는 애플리케이션 부분을 `Sentry.startSpan(...)`으로 감쌉니다.
3. `name`을 "Getting auth cache"처럼 설명적인 값으로 설정합니다.
4. `op`를 `cache.get`으로 설정합니다.
5. `cache.key`를 설정하는 키를 나타내는 문자열 배열로 설정합니다.
6. `cache.hit`을 캐시에서 값을 성공적으로 가져왔는지 여부를 나타내는 boolean 값으로 설정합니다.
7. 선택적으로 `cache.item_size` 같은 다른 속성도 설정할 수 있습니다. (자세한 내용은 [Cache Module Span Data Conventions](https://develop.sentry.dev/sdk/performance/modules/caches/#span-data) 참고.) (위에서 설명한 단계는 스니펫에도 문서화되어 있습니다.)

`my-cache.js`

```javascript
const key = "myCacheKey123";

Sentry.startSpan(
  {
    name: key,
    attributes: {
      "cache.key": [key],
      "network.peer.address": "cache.example.com/supercache",
      "network.peer.port": 9000,
    },
    op: "cache.get",
  },
  (span) => {
    // Set a key in your caching using your custom caching solution
    const value = my_caching.get(key);
    const cacheHit = Boolean(value);
    if (cacheHit) {
      span.setAttribute("cache.item_size", JSON.stringify(value).length, // Warning: if value is very big this could use lots of memory);
    }
    span.setAttribute("cache.hit", cacheHit);
  }
);
```

이제 필요한 span이 올바르게 설정되었습니다. [Cache dashboard](https://sentry.io/orgredirect/organizations/:orgslug/insights/backend/caches/)로 이동해 캐시 성능을 확인하세요.

