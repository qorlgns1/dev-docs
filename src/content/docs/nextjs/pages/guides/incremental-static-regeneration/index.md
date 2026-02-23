---
title: '가이드: ISR'
description: '증분 정적 재생성(ISR)을 사용하면 다음을 수행할 수 있습니다.'
---

# 가이드: ISR | Next.js

Source URL: https://nextjs.org/docs/pages/guides/incremental-static-regeneration

Copy page

# 증분 정적 재생성(ISR) 구현 방법

Last updated February 20, 2026

예시

  * [Next.js Commerce](https://vercel.com/templates/next.js/nextjs-commerce)
  * [On-Demand ISR](https://on-demand-isr.vercel.app)
  * [Next.js Forms](https://github.com/vercel/next.js/tree/canary/examples/next-forms)

증분 정적 재생성(ISR)을 사용하면 다음을 수행할 수 있습니다.

  * 전체 사이트를 다시 빌드하지 않고도 정적 콘텐츠를 업데이트
  * 대부분의 요청에 대해 사전 렌더링된 정적 페이지를 제공하여 서버 부하 감소
  * 페이지에 적절한 `cache-control` 헤더가 자동으로 추가되도록 보장
  * 긴 `next build` 시간 없이 대량의 콘텐츠 페이지 처리

다음은 최소 예시입니다:

pages/blog/[id].tsx

JavaScriptTypeScript
```
    import type { GetStaticPaths, GetStaticProps } from 'next'

    interface Post {
      id: string
      title: string
      content: string
    }

    interface Props {
      post: Post
    }

    export const getStaticPaths: GetStaticPaths = async () => {
      const posts = await fetch('https://api.vercel.app/blog').then((res) =>
        res.json()
      )
      const paths = posts.map((post: Post) => ({
        params: { id: String(post.id) },
      }))

      return { paths, fallback: 'blocking' }
    }

    export const getStaticProps: GetStaticProps<Props> = async ({
      params,
    }: {
      params: { id: string }
    }) => {
      const post = await fetch(`https://api.vercel.app/blog/${params.id}`).then(
        (res) => res.json()
      )

      return {
        props: { post },
        // Next.js will invalidate the cache when a
        // request comes in, at most once every 60 seconds.
        revalidate: 60,
      }
    }

    export default function Page({ post }: Props) {
      return (
        <main>
          <h1>{post.title}</h1>
          <p>{post.content}</p>
        </main>
      )
    }
```

이 예시는 다음과 같이 동작합니다:

  1. `next build` 과정에서 알려진 모든 블로그 게시물이 생성됩니다
  2. 이러한 페이지(예: `/blog/1`)에 대한 모든 요청은 캐시되어 즉시 응답됩니다
  3. 60초가 지나면 다음 요청은 캐시된(현재는 오래된) 페이지를 계속 반환합니다
  4. 캐시가 무효화되고 페이지의 새 버전이 백그라운드에서 생성되기 시작합니다
  5. 생성이 성공하면 다음 요청은 업데이트된 페이지를 반환하고 향후 요청을 위해 캐시합니다
  6. `/blog/26`이 요청되고 존재한다면, 해당 페이지는 온디맨드로 생성됩니다. 이 동작은 다른 [fallback](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-false) 값을 사용해 변경할 수 있습니다. 하지만 게시물이 존재하지 않으면 404가 반환됩니다.

## Reference[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#reference)

### Functions[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#functions-1)

  * [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)
  * [`res.revalidate`](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#response-helpers)

## Examples[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#examples)

### `res.revalidate()`를 사용한 온디맨드 검증[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#on-demand-validation-with-resrevalidate)

보다 정밀한 재검증 방법이 필요하면 `res.revalidate`를 사용해 API Router에서 온디맨드로 새 페이지를 생성하십시오.

예를 들어, `/api/revalidate?secret=<token>`에서 이 API Route를 호출해 특정 블로그 게시물을 재검증할 수 있습니다. Next.js 앱만 알고 있는 비밀 토큰을 생성하세요. 이 비밀 토큰은 재검증 API Route에 대한 무단 접근을 방지하는 데 사용됩니다.

pages/api/revalidate.ts

JavaScriptTypeScript
```
    import type { NextApiRequest, NextApiResponse } from 'next'

    export default async function handler(
      req: NextApiRequest,
      res: NextApiResponse
    ) {
      // Check for secret to confirm this is a valid request
      if (req.query.secret !== process.env.MY_SECRET_TOKEN) {
        return res.status(401).json({ message: 'Invalid token' })
      }

      try {
        // This should be the actual path not a rewritten path
        // e.g. for "/posts/[id]" this should be "/posts/1"
        await res.revalidate('/posts/1')
        return res.json({ revalidated: true })
      } catch (err) {
        // If there was an error, Next.js will continue
        // to show the last successfully generated page
        return res.status(500).send('Error revalidating')
      }
    }
```

온디맨드 재검증을 사용 중이라면 `getStaticProps` 안에 `revalidate` 시간을 지정할 필요가 없습니다. Next.js는 기본값 `false`(재검증 없음)를 사용하며, `res.revalidate()`가 호출될 때만 페이지를 온디맨드로 재검증합니다.

### 처리되지 않은 예외 다루기[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#handling-uncaught-exceptions)

백그라운드 재생성 처리 중 `getStaticProps` 내부에서 오류가 발생하거나 수동으로 오류를 던지면, 마지막으로 성공적으로 생성된 페이지가 계속 표시됩니다. 이후 요청에서 Next.js는 `getStaticProps` 호출을 다시 시도합니다.

pages/blog/[id].tsx

JavaScriptTypeScript
```
    import type { GetStaticProps } from 'next'

    interface Post {
      id: string
      title: string
      content: string
    }

    interface Props {
      post: Post
    }

    export const getStaticProps: GetStaticProps<Props> = async ({
      params,
    }: {
      params: { id: string }
    }) => {
      // If this request throws an uncaught error, Next.js will
      // not invalidate the currently shown page and
      // retry getStaticProps on the next request.
      const res = await fetch(`https://api.vercel.app/blog/${params.id}`)
      const post: Post = await res.json()

      if (!res.ok) {
        // If there is a server error, you might want to
        // throw an error instead of returning so that the cache is not updated
        // until the next successful request.
        throw new Error(`Failed to fetch posts, received status ${res.status}`)
      }

      return {
        props: { post },
        // Next.js will invalidate the cache when a
        // request comes in, at most once every 60 seconds.
        revalidate: 60,
      }
    }
```

### 캐시 위치 커스터마이징[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#customizing-the-cache-location)

캐시된 페이지와 데이터를 지속 가능한 스토리지에 보존하거나, 여러 컨테이너 또는 Next.js 인스턴스 간에 캐시를 공유하려면 Next.js 캐시 위치를 구성할 수 있습니다. [자세히 알아보기](https://nextjs.org/docs/app/guides/self-hosting#caching-and-isr).

## Troubleshooting[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#troubleshooting)

### 로컬 개발에서 캐시된 데이터 디버깅[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#debugging-cached-data-in-local-development)

`fetch` API를 사용하는 경우, 요청이 캐시되었는지 여부를 파악하기 위해 추가 로깅을 추가할 수 있습니다. [`logging` 옵션에 대해 더 알아보기](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging).

next.config.js
```
    module.exports = {
      logging: {
        fetches: {
          fullUrl: true,
        },
      },
    }
```

### 프로덕션 동작 검증[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#verifying-correct-production-behavior)

프로덕션에서 페이지가 올바르게 캐시되고 재검증되는지 확인하려면 `next build` 후 `next start`를 실행해 프로덕션 Next.js 서버를 로컬에서 테스트할 수 있습니다.

이렇게 하면 프로덕션 환경에서와 동일하게 ISR 동작을 확인할 수 있습니다. 추가 디버깅이 필요하면 `.env` 파일에 다음 환경 변수를 추가하세요:

.env
```
    NEXT_PRIVATE_DEBUG_CACHE=1
```

이렇게 하면 Next.js 서버 콘솔이 ISR 캐시 히트 및 미스를 로그로 출력합니다. `next build` 중에 생성되는 페이지와 경로에 접근할 때 페이지가 어떻게 업데이트되는지 출력을 통해 확인할 수 있습니다.

## Caveats[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#caveats)

  * ISR은 Node.js 런타임(기본값)을 사용할 때만 지원됩니다.
  * [Static Export](https://nextjs.org/docs/app/guides/static-exports)를 생성할 때는 ISR이 지원되지 않습니다.
  * 온디맨드 ISR 요청에는 Proxy가 실행되지 않으므로 경로 재작성이나 Proxy 로직이 적용되지 않습니다. 정확한 경로를 재검증하도록 하세요. 예를 들어, 재작성된 `/post-1` 대신 `/post/1`을 사용합니다.

## Platform Support[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#platform-support)

Deployment Option| Supported
---|---
[Node.js server](https://nextjs.org/docs/app/getting-started/deploying#nodejs-server)| Yes
[Docker container](https://nextjs.org/docs/app/getting-started/deploying#docker)| Yes
[Static export](https://nextjs.org/docs/app/getting-started/deploying#static-export)| No
[Adapters](https://nextjs.org/docs/app/getting-started/deploying#adapters)| Platform-specific

Next.js를 셀프 호스팅할 때 [ISR을 구성](https://nextjs.org/docs/app/guides/self-hosting#caching-and-isr)하는 방법을 알아보세요.

## 버전 기록[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#version-history)

Version| Changes
---|---
`v14.1.0`| 사용자 정의 `cacheHandler`가 안정화되었습니다.
`v13.0.0`| App Router가 도입되었습니다.
`v12.2.0`| Pages Router: 온디맨드 ISR이 안정화되었습니다
`v12.0.0`| Pages Router: [Bot-aware ISR fallback](https://nextjs.org/blog/next-12#bot-aware-isr-fallback)이 추가되었습니다.
`v9.5.0`| Pages Router: [ISR 안정화](https://nextjs.org/blog/next-9-5).

Was this helpful?

supported.

Send