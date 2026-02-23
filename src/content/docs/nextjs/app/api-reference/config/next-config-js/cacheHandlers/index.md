---
title: 'next.config.js: cacheHandlers'
description: '원본 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers'
---

# next.config.js: cacheHandlers | Next.js

원본 URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers

# cacheHandlers

마지막 업데이트: 2026년 2월 20일

`cacheHandlers` 구성은 [`'use cache'`](https://nextjs.org/docs/app/api-reference/directives/use-cache) 및 [`'use cache: remote'`](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote)에 사용할 사용자 정의 캐시 저장소 구현을 정의할 수 있게 해 줍니다. 이를 통해 캐시된 컴포넌트와 함수를 외부 서비스에 저장하거나 캐싱 동작을 사용자 지정할 수 있습니다. [`'use cache: private'`](https://nextjs.org/docs/app/api-reference/directives/use-cache-private)는 구성할 수 없습니다.

## 사용자 지정 캐시 핸들러를 사용할 시점[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#when-to-use-custom-cache-handlers)

**대부분의 애플리케이션은 사용자 지정 캐시 핸들러가 필요하지 않습니다.** 기본 메모리 내 캐시는 일반적인 사용 사례에서 잘 작동합니다.

사용자 지정 캐시 핸들러는 여러 인스턴스 간에 캐시를 공유해야 하거나 캐시 저장 위치를 변경해야 하는 고급 시나리오용입니다. 예를 들어 외부 스토리지(키-값 저장소 등)를 위한 사용자 지정 `remote` 핸들러를 구성한 다음, 코드에서 메모리 내 캐싱에는 `'use cache'`를, 외부 저장소에는 `'use cache: remote'`를 사용하여 동일한 애플리케이션 내에서 서로 다른 캐싱 전략을 적용할 수 있습니다.

**인스턴스 간 캐시 공유**

기본 메모리 내 캐시는 각 Next.js 프로세스에 격리됩니다. 여러 서버나 컨테이너를 실행하는 경우 각 인스턴스는 다른 인스턴스와 공유되지 않는 자체 캐시를 가지며 재시작 시 손실됩니다.

사용자 지정 핸들러를 사용하면 모든 Next.js 인스턴스가 액세스할 수 있는 공유 스토리지 시스템(예: Redis, Memcached, DynamoDB 등)과 통합할 수 있습니다.

**스토리지 유형 변경**

기본 메모리 내 방식과 다르게 캐시를 저장하고 싶을 수 있습니다. 사용자 지정 핸들러를 구현하여 캐시를 디스크, 데이터베이스 또는 외부 캐싱 서비스에 저장할 수 있습니다. 이유에는 재시작 간 지속성, 메모리 사용량 감소, 기존 인프라와의 통합 등이 포함됩니다.

## 사용법[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#usage)

사용자 지정 캐시 핸들러를 구성하려면:

  1. 별도 파일에서 캐시 핸들러를 정의합니다. 구현 세부 정보는 [examples](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#examples)를 참고하세요.
  2. Next 구성 파일에서 해당 파일 경로를 참조합니다.

next.config.ts

JavaScriptTypeScript
[code]
    import type { NextConfig } from 'next'

    const nextConfig: NextConfig = {
      cacheHandlers: {
        default: require.resolve('./cache-handlers/default-handler.js'),
        remote: require.resolve('./cache-handlers/remote-handler.js'),
      },
    }

    export default nextConfig
[/code]

### 핸들러 유형[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#handler-types)

  * **`default`** : `'use cache'` 지시문에서 사용됩니다.
  * **`remote`** : `'use cache: remote'` 지시문에서 사용됩니다.

`cacheHandlers`를 구성하지 않으면 Next.js는 `default`와 `remote` 모두에 대해 메모리 내 LRU(Least Recently Used) 캐시를 사용합니다. 참고용으로 [기본 구현](https://github.com/vercel/next.js/blob/canary/packages/next/src/server/lib/cache-handlers/default.ts)을 확인할 수 있습니다.

`sessions`, `analytics`와 같은 추가 명명된 핸들러를 정의하고 `'use cache: <name>'`으로 참조할 수도 있습니다.

`'use cache: private'`는 캐시 핸들러를 사용하지 않으며 사용자 지정할 수 없습니다.

## API Reference[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#api-reference)

캐시 핸들러는 다음 메서드가 포함된 [`CacheHandler`](https://github.com/vercel/next.js/blob/canary/packages/next/src/server/lib/cache-handlers/types.ts) 인터페이스를 구현해야 합니다.

### `get()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#get)

주어진 캐시 키에 대한 캐시 항목을 가져옵니다.
[code]
    get(cacheKey: string, softTags: string[]): Promise<CacheEntry | undefined>
[/code]

매개변수| 타입| 설명
---|---|---
`cacheKey`| `string`| 캐시 항목에 대한 고유 키입니다.
`softTags`| `string[]`| 오래되었는지 확인할 태그(일부 캐시 전략에서 사용됨)입니다.

찾은 경우 `CacheEntry` 객체를 반환하고, 없거나 만료된 경우 `undefined`를 반환합니다.

`get` 메서드는 스토리지에서 캐시 항목을 가져오고 `revalidate` 시간에 따라 만료되었는지 확인한 뒤, 누락되었거나 만료된 항목에 대해 `undefined`를 반환해야 합니다.
[code]
    const cacheHandler = {
      async get(cacheKey, softTags) {
        const entry = cache.get(cacheKey)
        if (!entry) return undefined

        // Check if expired
        const now = Date.now()
        if (now > entry.timestamp + entry.revalidate * 1000) {
          return undefined
        }

        return entry
      },
    }
[/code]

### `set()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#set)

주어진 캐시 키에 대한 캐시 항목을 저장합니다.
[code]
    set(cacheKey: string, pendingEntry: Promise<CacheEntry>): Promise<void>
[/code]

매개변수| 타입| 설명
---|---|---
`cacheKey`| `string`| 항목을 저장할 고유 키입니다.
`pendingEntry`| `Promise<CacheEntry>`| 캐시 항목으로 해석되는 프로미스입니다.

이 메서드가 호출될 때 항목은 아직 완료되지 않았을 수 있습니다(값 스트림 작성이 진행 중일 수 있음). 핸들러는 항목을 처리하기 전에 프로미스를 기다려야 합니다.

`Promise<void>`를 반환합니다.

`set` 메서드는 캐시 항목이 생성 중일 수 있으므로 저장하기 전에 반드시 `pendingEntry` 프로미스를 await 해야 합니다. 프로미스가 해결되면 캐시 시스템에 항목을 저장하세요.
[code]
    const cacheHandler = {
      async set(cacheKey, pendingEntry) {
        // Wait for the entry to be ready
        const entry = await pendingEntry

        // Store in your cache system
        cache.set(cacheKey, entry)
      },
    }
[/code]

### `refreshTags()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#refreshtags)

새 요청을 시작하기 전에 외부 태그 서비스와 동기화하기 위해 주기적으로 호출됩니다.
[code]
    refreshTags(): Promise<void>
[/code]

여러 인스턴스나 서비스 간에 캐시 무효화를 조율할 때 유용합니다. 메모리 내 캐시에서는 아무 작업이 필요 없을 수 있습니다.

`Promise<void>`를 반환합니다.

메모리 내 캐시에서는 무시할 수 있고, 분산 캐시에서는 요청 처리 전에 외부 서비스나 데이터베이스에서 태그 상태를 동기화하는 데 사용하세요.
[code]
    const cacheHandler = {
      async refreshTags() {
        // For in-memory cache, no action needed
        // For distributed cache, sync tag state from external service
      },
    }
[/code]

### `getExpiration()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#getexpiration)

태그 집합에 대한 최대 재검증 타임스탬프를 가져옵니다.
[code]
    getExpiration(tags: string[]): Promise<number>
[/code]

매개변수| 타입| 설명
---|---|---
`tags`| `string[]`| 만료를 확인할 태그 배열입니다.

반환값:

  * 태그가 한 번도 재검증되지 않은 경우 `0`
  * 가장 최근 재검증을 나타내는 타임스탬프(밀리초)
  * `Infinity`(소프트 태그 확인을 `get` 메서드에서 처리하려는 경우)

태그 재검증 타임스탬프를 추적하지 않는다면 `0`을 반환하세요. 그렇지 않다면 제공된 모든 태그 중 가장 최근 재검증 타임스탬프를 찾습니다. 소프트 태그 확인을 `get` 메서드에서 처리하려면 `Infinity`를 반환하세요.
[code]
    const cacheHandler = {
      async getExpiration(tags) {
        // Return 0 if not tracking tag revalidation
        return 0

        // Or return the most recent revalidation timestamp
        // return Math.max(...tags.map(tag => tagTimestamps.get(tag) || 0));
      },
    }
[/code]

### `updateTags()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#updatetags)

태그가 재검증되거나 만료될 때 호출됩니다.
[code]
    updateTags(tags: string[], durations?: { expire?: number }): Promise<void>
[/code]

매개변수| 타입| 설명
---|---|---
`tags`| `string[]`| 업데이트할 태그 배열입니다.
`durations`| `{ expire?: number }`| 선택 사항인 만료 지속 시간(초)입니다.

핸들러는 이러한 태그를 무효화하도록 내부 상태를 업데이트해야 합니다.

`Promise<void>`를 반환합니다.

태그가 재검증되면 핸들러는 해당 태그를 포함한 모든 캐시 항목을 무효화해야 합니다. 캐시를 순회하여 제공된 목록과 일치하는 태그가 있는 항목을 제거하세요.
[code]
    const cacheHandler = {
      async updateTags(tags, durations) {
        // Invalidate all cache entries with matching tags
        for (const [key, entry] of cache.entries()) {
          if (entry.tags.some((tag) => tags.includes(tag))) {
            cache.delete(key)
          }
        }
      },
    }
[/code]

## CacheEntry 타입[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#cacheentry-type)

[`CacheEntry`](https://github.com/vercel/next.js/blob/canary/packages/next/src/server/lib/cache-handlers/types.ts) 객체는 다음 구조를 가집니다.
[code]
    interface CacheEntry {
      value: ReadableStream<Uint8Array>
      tags: string[]
      stale: number
      timestamp: number
      expire: number
      revalidate: number
    }
[/code]

속성| 타입| 설명
---|---|---
`value`| `ReadableStream<Uint8Array>`| 스트림 형태의 캐시된 데이터입니다.
`tags`| `string[]`| 캐시 태그(소프트 태그 제외)입니다.
`stale`| `number`| 클라이언트 측 오래됨 허용 기간(초)입니다.
`timestamp`| `number`| 항목이 생성된 시점(밀리초 단위 타임스탬프)입니다.
`expire`| `number`| 항목을 사용할 수 있는 기간(초)입니다.
`revalidate`| `number`| 항목을 다시 검증해야 하는 시점까지의 기간(초)입니다.

> **알아두면 좋은 점** :
>
>   * `value`는 [`ReadableStream`](https://developer.mozilla.org/docs/Web/API/ReadableStream)입니다. 스트림 데이터를 읽고 저장해야 한다면 [`.tee()`](https://developer.mozilla.org/docs/Web/API/ReadableStream/tee)를 사용하세요.
>   * 스트림이 부분 데이터와 함께 오류가 발생하면 핸들러가 부분 캐시를 유지할지 폐기할지 결정해야 합니다.
>

## Examples[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#examples)

### 기본 메모리 내 캐시 핸들러[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#basic-in-memory-cache-handler)

스토리지로 `Map`을 사용하는 최소 구현 예시입니다. 핵심 개념을 보여 주며, LRU 제거, 오류 처리, 태그 관리를 포함한 프로덕션 수준 구현은 [기본 캐시 핸들러](https://github.com/vercel/next.js/blob/canary/packages/next/src/server/lib/cache-handlers/default.ts)를 참조하세요.

cache-handlers/memory-handler.js
[code]
    const cache = new Map()
    const pendingSets = new Map()

    module.exports = {
      async get(cacheKey, softTags) {
        // Wait for any pending set operation to complete
        const pendingPromise = pendingSets.get(cacheKey)
        if (pendingPromise) {
          await pendingPromise
        }

        const entry = cache.get(cacheKey)
        if (!entry) {
          return undefined
        }

        // Check if entry has expired
        const now = Date.now()
        if (now > entry.timestamp + entry.revalidate * 1000) {
          return undefined
        }

        return entry
      },

      async set(cacheKey, pendingEntry) {
        // Create a promise to track this set operation
        let resolvePending
        const pendingPromise = new Promise((resolve) => {
          resolvePending = resolve
        })
[/code]

pendingSets.set(cacheKey, pendingPromise)

        try {
          // Wait for the entry to be ready
          const entry = await pendingEntry

          // Store the entry in the cache
          cache.set(cacheKey, entry)
        } finally {
          resolvePending()
          pendingSets.delete(cacheKey)
        }
      },

      async refreshTags() {
        // No-op for in-memory cache
      },

      async getExpiration(tags) {
        // Return 0 to indicate no tags have been revalidated
        return 0
      },

      async updateTags(tags, durations) {
        // Implement tag-based invalidation
        for (const [key, entry] of cache.entries()) {
          if (entry.tags.some((tag) => tags.includes(tag))) {
            cache.delete(key)
          }
        }
      },
    }
[/code]

### 외부 스토리지 패턴[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#external-storage-pattern)

Redis나 데이터베이스 같은 영속 스토리지를 사용하려면 캐시 엔트리를 직렬화해야 합니다. 다음은 간단한 Redis 예시입니다:

cache-handlers/redis-handler.js
[code]
    const { createClient } = require('redis')

    const client = createClient({ url: process.env.REDIS_URL })
    client.connect()

    module.exports = {
      async get(cacheKey, softTags) {
        // Retrieve from Redis
        const stored = await client.get(cacheKey)
        if (!stored) return undefined

        // Deserialize the entry
        const data = JSON.parse(stored)

        // Reconstruct the ReadableStream from stored data
        return {
          value: new ReadableStream({
            start(controller) {
              controller.enqueue(Buffer.from(data.value, 'base64'))
              controller.close()
            },
          }),
          tags: data.tags,
          stale: data.stale,
          timestamp: data.timestamp,
          expire: data.expire,
          revalidate: data.revalidate,
        }
      },

      async set(cacheKey, pendingEntry) {
        const entry = await pendingEntry

        // Read the stream to get the data
        const reader = entry.value.getReader()
        const chunks = []

        try {
          while (true) {
            const { done, value } = await reader.read()
            if (done) break
            chunks.push(value)
          }
        } finally {
          reader.releaseLock()
        }

        // Combine chunks and serialize for Redis storage
        const data = Buffer.concat(chunks.map((chunk) => Buffer.from(chunk)))

        await client.set(
          cacheKey,
          JSON.stringify({
            value: data.toString('base64'),
            tags: entry.tags,
            stale: entry.stale,
            timestamp: entry.timestamp,
            expire: entry.expire,
            revalidate: entry.revalidate,
          }),
          { EX: entry.expire } // Use Redis TTL for automatic expiration
        )
      },

      async refreshTags() {
        // No-op for basic Redis implementation
        // Could sync with external tag service if needed
      },

      async getExpiration(tags) {
        // Return 0 to indicate no tags have been revalidated
        // Could query Redis for tag expiration timestamps if tracking them
        return 0
      },

      async updateTags(tags, durations) {
        // Implement tag-based invalidation if needed
        // Could iterate over keys with matching tags and delete them
      },
    }
[/code]

## 플랫폼 지원[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#platform-support)

배포 옵션| 지원 여부
---|---
[Node.js 서버](https://nextjs.org/docs/app/getting-started/deploying#nodejs-server)| 예
[Docker 컨테이너](https://nextjs.org/docs/app/getting-started/deploying#docker)| 예
[Static export](https://nextjs.org/docs/app/getting-started/deploying#static-export)| 아니요
[Adapters](https://nextjs.org/docs/app/getting-started/deploying#adapters)| 플랫폼별

## 버전 기록[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#version-history)

버전| 변경 사항
---|---
`v16.0.0`| `cacheHandlers`가 도입되었습니다.

## 관련 항목

관련 API 레퍼런스를 확인하세요.

- [use cache](https://nextjs.org/docs/app/api-reference/directives/use-cache)
  - Next.js 애플리케이션에서 데이터를 캐시하기 위해 "use cache" 지침을 사용하는 방법을 알아보세요.

- [use cache: remote](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote)
  - 원격 캐시 핸들러를 사용해 지속적이고 공유되는 캐싱을 위한 "use cache: remote" 지침을 사용하는 방법을 알아보세요.

- [use cache: private](https://nextjs.org/docs/app/api-reference/directives/use-cache-private)
  - 런타임 요청 API에 접근하는 함수를 캐시하기 위한 "use cache: private" 지침의 활용법을 알아보세요.

- [cacheLife](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife)
  - Next.js에서 cacheLife 구성을 설정하는 방법을 알아보세요.

보내기
