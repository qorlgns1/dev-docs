---
title: '가이드: 셀프 호스팅'
description: 'Next.js 앱을 배포할 때는 인프라에 따라 다양한 기능이 어떻게 처리될지 구성하고 싶을 수 있습니다.'
---

# 가이드: 셀프 호스팅 | Next.js

Source URL: https://nextjs.org/docs/pages/guides/self-hosting

Copy page

# Next.js 애플리케이션을 셀프 호스팅하는 방법

Last updated February 20, 2026

Next.js 앱을 [배포](https://nextjs.org/docs/app/getting-started/deploying)할 때는 인프라에 따라 다양한 기능이 어떻게 처리될지 구성하고 싶을 수 있습니다.

> **🎥 시청:** Next.js 셀프 호스팅에 대해 더 알아보기 → [YouTube (45분)](https://www.youtube.com/watch?v=sIVL4JMqRfc).

## Reverse Proxy[](https://nextjs.org/docs/pages/guides/self-hosting#reverse-proxy)

셀프 호스팅 시 Next.js 서버를 인터넷에 직접 노출하기보다 nginx와 같은 리버스 프록시를 앞단에 두는 것이 권장됩니다. 리버스 프록시는 비정상 요청, 느린 연결 공격, 페이로드 크기 제한, 레이트 리밋 등 보안 관련 작업을 처리하여 Next.js 서버의 부담을 덜어줍니다. 이렇게 하면 서버는 요청 검증 대신 렌더링에 자원을 집중할 수 있습니다.

## Image Optimization[](https://nextjs.org/docs/pages/guides/self-hosting#image-optimization)

`next start`로 배포할 때 `next/image`를 통한 [Image Optimization](https://nextjs.org/docs/app/api-reference/components/image)은 추가 설정 없이도 셀프 호스팅에서 작동합니다. 별도의 이미지 최적화 서비스를 쓰고 싶다면 [image loader를 구성](https://nextjs.org/docs/app/api-reference/components/image#loader)할 수 있습니다.

[정적 내보내기](https://nextjs.org/docs/app/guides/static-exports#image-optimization)에서도 `next.config.js`에 사용자 정의 image loader를 정의해 Image Optimization을 사용할 수 있습니다. 이미지는 빌드가 아니라 런타임에 최적화된다는 점을 유의하세요.

> **알아두면 좋아요:**
>
>   * glibc 기반 리눅스 시스템에서는 과도한 메모리 사용을 막기 위해 Image Optimization에 [추가 구성](https://sharp.pixelplumbing.com/install#linux-memory-allocator)이 필요할 수 있습니다.
>   * 최적화된 이미지의 [캐싱 동작](https://nextjs.org/docs/app/api-reference/components/image#minimumcachettl)과 TTL 설정 방법을 자세히 알아보세요.
>   * 이미지를 별도로 직접 최적화하더라도 `next/image` 사용의 이점을 유지하기 위해 [Image Optimization을 비활성화](https://nextjs.org/docs/app/api-reference/components/image#unoptimized)할 수 있습니다.
>

## Proxy[](https://nextjs.org/docs/pages/guides/self-hosting#proxy)

[Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)는 `next start`로 배포할 때 추가 설정 없이 셀프 호스팅에서 동작합니다. 다만 들어오는 요청에 접근해야 하므로 [정적 내보내기](https://nextjs.org/docs/app/guides/static-exports)를 사용할 때는 지원되지 않습니다.

Proxy는 모든 Node.js API의 부분집합인 [Edge runtime](https://nextjs.org/docs/app/api-reference/edge)을 사용하여 애플리케이션의 모든 라우트나 에셋 앞단에서 낮은 지연 시간을 보장합니다. 이러한 동작을 원하지 않으면 Proxy를 [완전한 Node.js 런타임](https://nextjs.org/blog/next-15-2#nodejs-middleware-experimental)에서 실행할 수 있습니다.

모든 Node.js API가 필요한 로직(또는 외부 패키지)을 추가하려면 해당 로직을 [Server Component](https://nextjs.org/docs/app/getting-started/server-and-client-components)로 [layout](https://nextjs.org/docs/app/api-reference/file-conventions/layout)으로 옮길 수 있습니다. 예를 들어 [headers](https://nextjs.org/docs/app/api-reference/functions/headers) 검사나 [redirect](https://nextjs.org/docs/app/api-reference/functions/redirect) 수행입니다. 또한 헤더, 쿠키, 쿼리 파라미터를 사용해 `next.config.js`에서 [redirect](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#header-cookie-and-query-matching) 또는 [rewrite](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites#header-cookie-and-query-matching)를 구성할 수 있습니다. 그래도 해결되지 않으면 [맞춤형 서버](https://nextjs.org/docs/pages/guides/custom-server)를 사용할 수도 있습니다.

## Environment Variables[](https://nextjs.org/docs/pages/guides/self-hosting#environment-variables)

Next.js는 빌드 타임과 런타임 환경 변수를 모두 지원합니다.

**기본적으로 환경 변수는 서버에서만 사용할 수 있습니다.** 브라우저에 환경 변수를 노출하려면 `NEXT_PUBLIC_` 접두사를 붙여야 합니다. 하지만 이러한 공개 환경 변수는 `next build` 중 JavaScript 번들에 인라인됩니다.

런타임 환경 변수를 읽으려면 `getServerSideProps` 또는 [App Router를 점진적으로 도입](https://nextjs.org/docs/app/guides/migrating/app-router-migration)하는 방법을 권장합니다.

이를 통해 서로 다른 값을 가진 여러 환경에 새로운 Docker 이미지를 프로모션할 수 있습니다.

> **알아두면 좋아요:**
>
>   * [`register` 함수](https://nextjs.org/docs/app/guides/instrumentation)를 사용해 서버 시작 시 코드를 실행할 수 있습니다.
>

## Caching and ISR[](https://nextjs.org/docs/pages/guides/self-hosting#caching-and-isr)

Next.js는 응답, 생성된 정적 페이지, 빌드 출력, 이미지·폰트·스크립트 같은 기타 정적 에셋을 캐시할 수 있습니다.

페이지 캐싱과 재검증([Incremental Static Regeneration](https://nextjs.org/docs/app/guides/incremental-static-regeneration))은 **동일한 공유 캐시**를 사용합니다. 기본적으로 이 캐시는 Next.js 서버의 파일 시스템(디스크)에 저장됩니다. **Pages Router와 App Router 모두 셀프 호스팅 시 자동으로 동작합니다.**

캐시된 페이지와 데이터를 내구성 있는 스토리지에 영구 저장하거나 여러 컨테이너/인스턴스 간에 캐시를 공유하려면 Next.js 캐시 위치를 구성할 수 있습니다.

### Automatic Caching[](https://nextjs.org/docs/pages/guides/self-hosting#automatic-caching)

  * Next.js는 진정한 불변 에셋에 `public, max-age=31536000, immutable`인 `Cache-Control` 헤더를 설정합니다. 이는 오버라이드할 수 없습니다. 이러한 불변 파일은 파일 이름에 SHA 해시가 포함되어 있어 무기한 안전하게 캐시할 수 있습니다. 예: [Static Image Imports](https://nextjs.org/docs/app/getting-started/images#local-images). 이미지는 [TTL을 구성](https://nextjs.org/docs/app/api-reference/components/image#minimumcachettl)할 수 있습니다.
  * Incremental Static Regeneration(ISR)은 `s-maxage: <revalidate in getStaticProps>, stale-while-revalidate` 값을 가진 `Cache-Control` 헤더를 설정합니다. 이 재검증 시간은 초 단위로 [`getStaticProps` 함수](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)에 정의됩니다. `revalidate: false`를 설정하면 기본적으로 1년 캐시 기간이 적용됩니다.
  * 동적으로 렌더링된 페이지는 사용자별 데이터를 캐시하지 않도록 `private, no-cache, no-store, max-age=0, must-revalidate` 값을 가진 `Cache-Control` 헤더를 설정합니다. 이는 App Router와 Pages Router 모두에 적용됩니다. [Draft Mode](https://nextjs.org/docs/app/guides/draft-mode)도 포함됩니다.

### Static Assets[](https://nextjs.org/docs/pages/guides/self-hosting#static-assets)

정적 에셋을 다른 도메인이나 CDN에 호스팅하려면 `next.config.js`에서 `assetPrefix` [구성](https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix)을 사용할 수 있습니다. Next.js는 JavaScript나 CSS 파일을 가져올 때 해당 asset prefix를 사용합니다. 에셋을 별도 도메인으로 분리하면 DNS 및 TLS 해상도에 추가 시간이 소요되는 단점이 있습니다.

[`assetPrefix` 자세히 알아보기](https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix).

### Configuring Caching[](https://nextjs.org/docs/pages/guides/self-hosting#configuring-caching)

기본적으로 생성된 캐시 에셋은 메모리(기본 50mb)와 디스크에 저장됩니다. Kubernetes 같은 컨테이너 오케스트레이션 플랫폼에서 Next.js를 호스팅하면 각 파드가 캐시 사본을 갖습니다. 파드 간에 캐시가 기본적으로 공유되지 않아 오래된 데이터가 표시될 수 있으므로, Next.js 캐시를 구성해 캐시 핸들러를 제공하고 메모리 캐싱을 비활성화할 수 있습니다.

셀프 호스팅 시 ISR/Data Cache 위치를 구성하려면 `next.config.js` 파일에서 사용자 정의 핸들러를 설정하세요:

next.config.js
[code]
    module.exports = {
      cacheHandler: require.resolve('./cache-handler.js'),
      cacheMaxMemorySize: 0, // disable default in-memory caching
    }
[/code]

그다음 프로젝트 루트에 `cache-handler.js`를 생성합니다. 예:

cache-handler.js
[code]
    const cache = new Map()

    module.exports = class CacheHandler {
      constructor(options) {
        this.options = options
      }

      async get(key) {
        // This could be stored anywhere, like durable storage
        return cache.get(key)
      }

      async set(key, data, ctx) {
        // This could be stored anywhere, like durable storage
        cache.set(key, {
          value: data,
          lastModified: Date.now(),
          tags: ctx.tags,
        })
      }

      async revalidateTag(tags) {
        // tags is either a string or an array of strings
        tags = [tags].flat()
        // Iterate over all entries in the cache
        for (let [key, value] of cache) {
          // If the value's tags include the specified tag, delete this entry
          if (value.tags.some((tag) => tags.includes(tag))) {
            cache.delete(key)
          }
        }
      }

      // If you want to have temporary in memory cache for a single request that is reset
      // before the next request you can leverage this method
      resetRequestCache() {}
    }
[/code]

사용자 정의 캐시 핸들러를 사용하면 Next.js 애플리케이션을 호스팅하는 모든 파드의 일관성을 보장할 수 있습니다. 예를 들어 [Redis](https://github.com/vercel/next.js/tree/canary/examples/cache-handler-redis)나 AWS S3 등 원하는 위치에 캐시 값을 저장할 수 있습니다.

> **알아두면 좋아요:**
>
>   * `revalidatePath`는 캐시 태그 위에 제공되는 편의 레이어입니다. `revalidatePath`를 호출하면 지정한 페이지에 대한 기본 특수 태그로 `revalidateTag` 함수가 호출됩니다.
>

## Build Cache[](https://nextjs.org/docs/pages/guides/self-hosting#build-cache)

Next.js는 `next build` 중 애플리케이션의 제공 버전을 식별하는 ID를 생성합니다. 동일한 빌드를 사용해 여러 컨테이너를 구동해야 합니다.

각 환경 단계마다 다시 빌드한다면 컨테이너 간에 사용할 일관된 빌드 ID를 생성해야 합니다. `next.config.js`에서 `generateBuildId` 명령을 사용하세요:

next.config.js
[code]
    module.exports = {
      generateBuildId: async () => {
        // This could be anything, using the latest git hash
        return process.env.GIT_HASH
      },
    }
[/code]

## Multi-Server Deployments[](https://nextjs.org/docs/pages/guides/self-hosting#multi-server-deployments)

다중 서버 인스턴스(예: 로드 밸런서 뒤의 컨테이너)에서 Next.js를 실행할 때는 일관된 동작을 위한 추가 고려 사항이 있습니다.

### Server Functions 암호화 키[](https://nextjs.org/docs/pages/guides/self-hosting#server-functions-encryption-key)

Next.js는 클라이언트로 보내기 전에 [Server Function](https://nextjs.org/docs/app/getting-started/updating-data) 클로저 변수를 암호화합니다. 기본적으로 빌드마다 고유한 암호화 키가 생성됩니다.

여러 서버 인스턴스를 실행할 때는 모든 인스턴스가 동일한 암호화 키를 사용해야 합니다. 그렇지 않으면 한 인스턴스가 암호화한 Server Function을 다른 인스턴스가 복호화하지 못해 "Failed to find Server Action" 오류가 발생합니다.

`NEXT_SERVER_ACTIONS_ENCRYPTION_KEY` 환경 변수를 사용해 일관된 암호화 키를 설정하세요. 이 키는 유효한 AES 키 길이(16, 24, 32바이트)의 base64 인코딩 값이어야 합니다. Next.js는 기본적으로 32바이트 키를 생성합니다.
[code]
    NEXT_SERVER_ACTIONS_ENCRYPTION_KEY=your-generated-key next build
[/code]

빌드 출력에 키가 포함되며 런타임에 자동으로 사용됩니다. 자세한 내용은 [Data Security guide](https://nextjs.org/docs/app/guides/data-security#overwriting-encryption-keys-advanced)를 참고하세요.

### Deployment identifier[](https://nextjs.org/docs/pages/guides/self-hosting#deployment-identifier)

롤링 배포 동안 버전 편차 보호를 활성화하려면 [`deploymentId`](https://nextjs.org/docs/app/api-reference/config/next-config-js/deploymentId)를 구성하세요. 이렇게 하면 클라이언트가 항상 일관된 배포 버전에서 자산을 받을 수 있습니다.

### Shared cache[](https://nextjs.org/docs/pages/guides/self-hosting#shared-cache)

기본적으로 Next.js는 인스턴스 간에 공유되지 않는 인메모리 캐시를 사용합니다. 일관된 캐싱 동작을 원한다면 외부 스토리지에 데이터를 저장하는 [custom cache handler](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers)와 함께 [`'use cache: remote'`](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote)를 사용하세요.

## Version Skew[](https://nextjs.org/docs/pages/guides/self-hosting#version-skew)

여러 인스턴스에서 셀프 호스팅하거나 롤링 배포를 수행할 때 [version skew](https://nextjs.org/docs/app/glossary#version-skew)가 다음과 같은 문제를 일으킬 수 있습니다:

  * **누락된 자산** : 클라이언트가 서버에 더 이상 존재하지 않는 JavaScript 또는 CSS 파일을 요청
  * **Server Function 불일치** : 클라이언트가 이전 빌드의 ID로 Server Function을 호출하여 서버가 더 이상 인식하지 못함
  * **내비게이션 실패** : 이전 배포에서 사전 가져온 페이지 데이터가 새로운 서버와 호환되지 않음

Next.js는 [`deploymentId`](https://nextjs.org/docs/app/api-reference/config/next-config-js/deploymentId)를 사용해 버전 편차를 감지하고 처리합니다. 배포 ID를 구성하면:

  * 정적 자산에 `?dpl=<deploymentId>` 쿼리 매개변수가 포함됩니다.
  * 클라이언트 측 내비게이션 요청에 `x-deployment-id` 헤더가 포함됩니다.
  * 서버는 클라이언트의 배포 ID와 자신의 배포 ID를 비교합니다.

불일치가 감지되면 Next.js는 클라이언트 측 내비게이션 대신 하드 내비게이션(전체 페이지 새로고침)을 트리거하여 클라이언트가 일관된 배포 버전에서 자산을 가져오도록 보장합니다.

next.config.js
[code]
    module.exports = {
      deploymentId: process.env.DEPLOYMENT_VERSION,
    }
[/code]

> **알아두면 좋아요:** 애플리케이션이 새로고침되면 페이지 내비게이션 사이에서 상태를 유지하도록 설계되지 않은 경우 애플리케이션 상태가 손실될 수 있습니다. URL 상태나 로컬 스토리지는 유지되지만 `useState` 같은 컴포넌트 상태는 사라집니다.

## Manual Graceful Shutdowns[](https://nextjs.org/docs/pages/guides/self-hosting#manual-graceful-shutdowns)

셀프 호스팅 시 `SIGTERM` 또는 `SIGINT` 신호로 서버가 종료될 때 코드를 실행하고 싶을 수 있습니다.

환경 변수 `NEXT_MANUAL_SIG_HANDLE`을 `true`로 설정한 뒤 `_document.js` 파일 내에서 해당 신호에 대한 핸들러를 등록할 수 있습니다. 이 환경 변수는 `.env` 파일이 아닌 `package.json` 스크립트에 직접 등록해야 합니다.

> **알아두면 좋아요** : `next dev`에서는 수동 신호 처리를 사용할 수 없습니다.

package.json
[code]
    {
      "scripts": {
        "dev": "next dev",
        "build": "next build",
        "start": "NEXT_MANUAL_SIG_HANDLE=true next start"
      }
    }
[/code]

pages/_document.js
[code]
    if (process.env.NEXT_MANUAL_SIG_HANDLE) {
      process.on('SIGTERM', () => {
        console.log('Received SIGTERM: cleaning up')
        process.exit(0)
      })
      process.on('SIGINT', () => {
        console.log('Received SIGINT: cleaning up')
        process.exit(0)
      })
    }
[/code]

보내기
