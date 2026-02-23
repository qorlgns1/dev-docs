---
title: '가이드: ISR'
description: 'Incremental Static Regeneration(ISR)은 다음을 가능하게 합니다:'
---

# 가이드: ISR | Next.js

출처 URL: https://nextjs.org/docs/app/guides/incremental-static-regeneration

# 증분 정적 재생성(ISR)을 구현하는 방법

마지막 업데이트 2026년 2월 20일

예제

  * [Next.js Commerce](https://vercel.com/templates/next.js/nextjs-commerce)
  * [On-Demand ISR](https://on-demand-isr.vercel.app)
  * [Next.js Forms](https://github.com/vercel/next.js/tree/canary/examples/next-forms)

Incremental Static Regeneration(ISR)은 다음을 가능하게 합니다:

  * 전체 사이트를 다시 빌드하지 않고 정적 콘텐츠를 업데이트
  * 대부분의 요청에 대해 사전 렌더링된 정적 페이지를 제공해 서버 부하 감소
  * 페이지에 적절한 `cache-control` 헤더가 자동으로 추가되도록 보장
  * 긴 `next build` 시간 없이 방대한 수의 콘텐츠 페이지 처리

다음은 최소 예제입니다:

app/blog/[id]/page.tsx

JavaScriptTypeScript
[code]
    interface Post {
      id: string
      title: string
      content: string
    }

    // Next.js will invalidate the cache when a
    // request comes in, at most once every 60 seconds.
    export const revalidate = 60

    export async function generateStaticParams() {
      const posts: Post[] = await fetch('https://api.vercel.app/blog').then((res) =>
        res.json()
      )
      return posts.map((post) => ({
        id: String(post.id),
      }))
    }

    export default async function Page({
      params,
    }: {
      params: Promise<{ id: string }>
    }) {
      const { id } = await params
      const post: Post = await fetch(`https://api.vercel.app/blog/${id}`).then(
        (res) => res.json()
      )
      return (
        <main>
          <h1>{post.title}</h1>
          <p>{post.content}</p>
        </main>
      )
    }
[/code]

이 예제가 작동하는 방식은 다음과 같습니다:

  1. `next build` 중에 알려진 모든 블로그 게시물이 생성됩니다.
  2. 이 페이지들(예: `/blog/1`)에 대한 모든 요청은 캐시되며 즉시 응답합니다.
  3. 60초가 지나면 다음 요청은 캐시된(지금은 오래된) 페이지를 계속 반환합니다.
  4. 캐시가 무효화되고 새로운 페이지 버전이 백그라운드에서 생성되기 시작합니다.
  5. 생성이 완료되면 다음 요청은 업데이트된 페이지를 반환하고 이후 요청을 위해 캐시합니다.
  6. `/blog/26` 요청이 들어오고 해당 페이지가 존재하면, 페이지는 온디맨드로 생성됩니다. 이 동작은 다른 [dynamicParams](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamicparams) 값을 사용해 변경할 수 있습니다. 하지만 게시물이 존재하지 않으면 404가 반환됩니다.

## 참고자료[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#reference)

### 라우트 세그먼트 구성[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#route-segment-config)

  * [`revalidate`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#revalidate)
  * [`dynamicParams`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamicparams)

### 함수[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#functions)

  * [`revalidatePath`](https://nextjs.org/docs/app/api-reference/functions/revalidatePath)
  * [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)

## 예제[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#examples)

### 시간 기반 재검증[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#time-based-revalidation)

이 예제는 /blog에서 블로그 게시물 목록을 가져와 표시합니다. 한 시간이 지나면 다음 방문자는 빠른 응답을 위해 캐시된(오래된) 페이지 버전을 즉시 받습니다. 동시에 Next.js는 백그라운드에서 새로운 버전 생성을 트리거합니다. 새로운 버전이 성공적으로 생성되면 캐시된 버전을 교체하고, 이후 방문자는 업데이트된 콘텐츠를 받습니다.

app/blog/page.tsx

JavaScriptTypeScript
[code]
    interface Post {
      id: string
      title: string
      content: string
    }

    export const revalidate = 3600 // invalidate every hour

    export default async function Page() {
      const data = await fetch('https://api.vercel.app/blog')
      const posts: Post[] = await data.json()
      return (
        <main>
          <h1>Blog Posts</h1>
          <ul>
            {posts.map((post) => (
              <li key={post.id}>{post.title}</li>
            ))}
          </ul>
        </main>
      )
    }
[/code]

revalidate 시간을 길게 설정하는 것이 좋습니다. 예를 들어 1초 대신 1시간을 권장합니다. 더 정밀한 제어가 필요하다면 온디맨드 재검증을 사용하세요. 실시간 데이터가 필요하면 [동적 렌더링](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)으로 전환하는 것을 고려하세요.

### `revalidatePath`를 사용한 온디맨드 재검증[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#on-demand-revalidation-with-revalidatepath)

더 정밀한 재검증이 필요하면 `revalidatePath` 함수를 사용해 캐시된 페이지를 온디맨드로 무효화하세요.

예를 들어, 새 게시물을 추가한 뒤 아래 서버 액션이 호출된다고 가정합니다. Server Component에서 데이터를 가져오는 방식이 `fetch`든 데이터베이스 연결이든 상관없이, 이 함수는 전체 라우트에 대한 캐시를 무효화합니다. 해당 라우트에 대한 다음 요청은 재생성을 트리거하고 최신 데이터를 제공하며, 이후 요청을 위해 다시 캐시됩니다.

> **참고:** `revalidatePath`는 캐시 항목을 무효화하지만 재생성은 다음 요청 시에 발생합니다. 다음 요청을 기다리지 않고 즉시 캐시 항목을 적극적으로 재생성하려면 Pages 라우터의 [`res.revalidate`](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#on-demand-validation-with-resrevalidate) 메서드를 사용할 수 있습니다. App Router에서도 적극적 재생성을 지원하기 위한 새로운 메서드를 추가하는 작업을 진행 중입니다.

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'

    import { revalidatePath } from 'next/cache'

    export async function createPost() {
      // Invalidate the cache for the /posts route
      revalidatePath('/posts')
    }
[/code]

[데모 보기](https://on-demand-isr.vercel.app) 및 [소스 코드 살펴보기](https://github.com/vercel/on-demand-isr).

### `revalidateTag`를 사용한 온디맨드 재검증[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#on-demand-revalidation-with-revalidatetag)

대부분의 경우 전체 경로를 재검증하는 것이 좋습니다. 더 세밀한 제어가 필요하면 `revalidateTag` 함수를 사용할 수 있습니다. 예를 들어 개별 `fetch` 호출에 태그를 지정할 수 있습니다:

app/blog/page.tsx

JavaScriptTypeScript
[code]
    export default async function Page() {
      const data = await fetch('https://api.vercel.app/blog', {
        next: { tags: ['posts'] },
      })
      const posts = await data.json()
      // ...
    }
[/code]

ORM을 사용하거나 데이터베이스에 연결하는 경우 `unstable_cache`를 사용할 수 있습니다:

app/blog/page.tsx

JavaScriptTypeScript
[code]
    import { unstable_cache } from 'next/cache'
    import { db, posts } from '@/lib/db'

    const getCachedPosts = unstable_cache(
      async () => {
        return await db.select().from(posts)
      },
      ['posts'],
      { revalidate: 3600, tags: ['posts'] }
    )

    export default async function Page() {
      const posts = getCachedPosts()
      // ...
    }
[/code]

그런 다음 [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data) 또는 [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route)에서 `revalidateTag`를 사용할 수 있습니다:

app/actions.ts

JavaScriptTypeScript
[code]
    'use server'

    import { revalidateTag } from 'next/cache'

    export async function createPost() {
      // Invalidate all data tagged with 'posts'
      revalidateTag('posts')
    }
[/code]

### 처리되지 않은 예외 다루기[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#handling-uncaught-exceptions)

데이터를 재검증하는 동안 오류가 발생하면 마지막으로 성공적으로 생성된 데이터가 캐시에서 계속 제공됩니다. 이후 요청에서 Next.js는 데이터 재검증을 다시 시도합니다. [오류 처리 자세히 알아보기](https://nextjs.org/docs/app/getting-started/error-handling).

### 캐시 위치 사용자 지정[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#customizing-the-cache-location)

Next.js 캐시 위치를 구성하여 캐시된 페이지와 데이터를 영구 스토리지에 보존하거나, Next.js 애플리케이션의 여러 컨테이너나 인스턴스 간에 캐시를 공유할 수 있습니다. [자세히 알아보기](https://nextjs.org/docs/app/guides/self-hosting#caching-and-isr).

## 문제 해결[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#troubleshooting)

### 로컬 개발에서 캐시된 데이터 디버깅[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#debugging-cached-data-in-local-development)

`fetch` API를 사용하는 경우 추가 로깅을 추가해 어떤 요청이 캐시되었는지 또는 캐시되지 않았는지 파악할 수 있습니다. [`logging` 옵션](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging)에 대해 자세히 알아보세요.

next.config.js
[code]
    module.exports = {
      logging: {
        fetches: {
          fullUrl: true,
        },
      },
    }
[/code]

### 프로덕션 동작 검증[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#verifying-correct-production-behavior)

프로덕션에서 페이지가 올바르게 캐시되고 재검증되는지 확인하려면 `next build`를 실행한 뒤 `next start`로 프로덕션 Next.js 서버를 실행하여 로컬에서 테스트할 수 있습니다.

이를 통해 프로덕션 환경과 동일한 방식으로 ISR 동작을 검증할 수 있습니다. 추가 디버깅이 필요하면 `.env` 파일에 다음 환경 변수를 추가하세요:

.env
[code]
    NEXT_PRIVATE_DEBUG_CACHE=1
[/code]

이렇게 하면 Next.js 서버 콘솔이 ISR 캐시 적중과 미스를 로깅합니다. 출력 내용을 확인해 `next build` 동안 어떤 페이지가 생성되었는지, 그리고 경로가 온디맨드로 접근될 때 페이지가 어떻게 업데이트되는지 확인할 수 있습니다.

## 주의 사항[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#caveats)

  * ISR은 Node.js 런타임(기본값)을 사용할 때만 지원됩니다.
  * ISR은 [Static Export](https://nextjs.org/docs/app/guides/static-exports)를 생성할 때는 지원되지 않습니다.
  * 정적으로 렌더링된 라우트에서 여러 `fetch` 요청이 있고 각기 다른 `revalidate` 주기를 갖는 경우, 가장 짧은 시간이 ISR에 사용됩니다. 하지만 이러한 재검증 주기는 [데이터 캐시](https://nextjs.org/docs/app/guides/caching#data-cache)에서는 그대로 적용됩니다.
  * 라우트에서 사용하는 `fetch` 요청 중 하나라도 `revalidate` 시간이 `0`이거나 명시적으로 `no-store`인 경우 해당 라우트는 [동적으로 렌더링](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)됩니다.
  * 온디맨드 ISR 요청에는 프록시가 실행되지 않으므로 경로 재작성이나 프록시의 로직이 적용되지 않습니다. 정확한 경로를 재검증하도록 하세요. 예를 들어, 재작성된 `/post-1` 대신 `/post/1`을 사용해야 합니다.

## 플랫폼 지원[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#platform-support)

배포 옵션| 지원 여부
---|---
[Node.js server](https://nextjs.org/docs/app/getting-started/deploying#nodejs-server)| 예
[Docker container](https://nextjs.org/docs/app/getting-started/deploying#docker)| 예
[Static export](https://nextjs.org/docs/app/getting-started/deploying#static-export)| 아니요
[Adapters](https://nextjs.org/docs/app/getting-started/deploying#adapters)| 플랫폼별

Next.js를 셀프 호스팅할 때 [ISR을 구성](https://nextjs.org/docs/app/guides/self-hosting#caching-and-isr)하는 방법을 알아보세요.

## 버전 기록[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#version-history)

버전| 변경 사항

---|---
`v14.1.0`| 사용자 지정 `cacheHandler`가 안정화되었습니다.
`v13.0.0`| App Router가 도입되었습니다.
`v12.2.0`| Pages Router: On-Demand ISR이 안정화되었습니다.
`v12.0.0`| Pages Router: [Bot-aware ISR fallback](https://nextjs.org/blog/next-12#bot-aware-isr-fallback)이 추가되었습니다.
`v9.5.0`| Pages Router: [Stable ISR introduced](https://nextjs.org/blog/next-9-5)이 도입되었습니다.

보내기
