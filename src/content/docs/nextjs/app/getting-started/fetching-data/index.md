---
title: '시작하기: 데이터 가져오기'
description: '마지막 업데이트: 2026년 2월 20일'
---

# 시작하기: 데이터 가져오기 | Next.js

출처 URL: https://nextjs.org/docs/app/getting-started/fetching-data

[앱 라우터](https://nextjs.org/docs/app)[시작하기](https://nextjs.org/docs/app/getting-started)데이터 가져오기

페이지 복사

# 데이터 가져오기

마지막 업데이트: 2026년 2월 20일

이 페이지에서는 [서버 및 클라이언트 컴포넌트](https://nextjs.org/docs/app/getting-started/server-and-client-components)에서 데이터를 가져오는 방법과 데이터에 의존하는 컴포넌트를 [스트리밍](https://nextjs.org/docs/app/getting-started/fetching-data#streaming)하는 방법을 안내합니다.

## 데이터 가져오기[](https://nextjs.org/docs/app/getting-started/fetching-data#fetching-data)

### 서버 컴포넌트[](https://nextjs.org/docs/app/getting-started/fetching-data#server-components)

서버 컴포넌트에서는 다음과 같은 비동기 I/O를 사용해 데이터를 가져올 수 있습니다.

  1. [`fetch` API](https://nextjs.org/docs/app/getting-started/fetching-data#with-the-fetch-api)
  2. [ORM 또는 데이터베이스](https://nextjs.org/docs/app/getting-started/fetching-data#with-an-orm-or-database)
  3. `fs`와 같은 Node.js API로 파일 시스템 읽기



#### `fetch` API 사용하기[](https://nextjs.org/docs/app/getting-started/fetching-data#with-the-fetch-api)

`fetch` API로 데이터를 가져오려면 컴포넌트를 비동기 함수로 만들고 `fetch` 호출을 `await` 하세요. 예:

app/blog/page.tsx

JavaScriptTypeScript
[code]
    export default async function Page() {
      const data = await fetch('https://api.vercel.app/blog')
      const posts = await data.json()
      return (
        <ul>
          {posts.map((post) => (
            <li key={post.id}>{post.title}</li>
          ))}
        </ul>
      )
    }
[/code]

> **알아두면 좋은 점:**
> 
>   * `fetch` 응답은 기본적으로 캐시되지 않습니다. 그러나 Next.js는 라우트를 [사전 렌더링](https://nextjs.org/docs/app/guides/caching#static-rendering)하고 결과를 캐시하여 성능을 향상시킵니다. [동적 렌더링](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)으로 전환하려면 `{ cache: 'no-store' }` 옵션을 사용하세요. 자세한 내용은 [`fetch` API Reference](https://nextjs.org/docs/app/api-reference/functions/fetch)를 참고하세요.
>   * 개발 중에는 가시성과 디버깅을 위해 `fetch` 호출을 로깅할 수 있습니다. [`logging` API reference](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging)를 확인하세요.
> 


#### ORM 또는 데이터베이스 사용하기[](https://nextjs.org/docs/app/getting-started/fetching-data#with-an-orm-or-database)

서버 컴포넌트는 서버에서 렌더링되므로 ORM이나 데이터베이스 클라이언트를 사용해 안전하게 DB 쿼리를 실행할 수 있습니다. 컴포넌트를 비동기 함수로 만들고 호출을 `await` 하세요.

app/blog/page.tsx

JavaScriptTypeScript
[code]
    import { db, posts } from '@/lib/db'
     
    export default async function Page() {
      const allPosts = await db.select().from(posts)
      return (
        <ul>
          {allPosts.map((post) => (
            <li key={post.id}>{post.title}</li>
          ))}
        </ul>
      )
    }
[/code]

### 클라이언트 컴포넌트[](https://nextjs.org/docs/app/getting-started/fetching-data#client-components)

클라이언트 컴포넌트에서는 다음 두 가지 방식으로 데이터를 가져올 수 있습니다.

  1. React의 [`use` API](https://react.dev/reference/react/use)
  2. [SWR](https://swr.vercel.app/) 또는 [React Query](https://tanstack.com/query/latest) 같은 커뮤니티 라이브러리



#### `use` API로 데이터 스트리밍하기[](https://nextjs.org/docs/app/getting-started/fetching-data#streaming-data-with-the-use-api)

React의 [`use` API](https://react.dev/reference/react/use)를 사용하면 서버에서 클라이언트로 데이터를 [스트리밍](https://nextjs.org/docs/app/getting-started/fetching-data#streaming)할 수 있습니다. 먼저 서버 컴포넌트에서 데이터를 가져오고, 프라미스를 클라이언트 컴포넌트의 prop으로 전달하세요.

app/blog/page.tsx

JavaScriptTypeScript
[code]
    import Posts from '@/app/ui/posts'
    import { Suspense } from 'react'
     
    export default function Page() {
      // Don't await the data fetching function
      const posts = getPosts()
     
      return (
        <Suspense fallback={<div>Loading...</div>}>
          <Posts posts={posts} />
        </Suspense>
      )
    }
[/code]

그다음 클라이언트 컴포넌트에서 `use` API로 프라미스를 읽습니다.

app/ui/posts.tsx

JavaScriptTypeScript
[code]
    'use client'
    import { use } from 'react'
     
    export default function Posts({
      posts,
    }: {
      posts: Promise<{ id: string; title: string }[]>
    }) {
      const allPosts = use(posts)
     
      return (
        <ul>
          {allPosts.map((post) => (
            <li key={post.id}>{post.title}</li>
          ))}
        </ul>
      )
    }
[/code]

위 예제에서 `<Posts>` 컴포넌트는 [`<Suspense>` 경계](https://react.dev/reference/react/Suspense) 안에 래핑되어 있으므로 프라미스가 resolve되는 동안 폴백 UI가 표시됩니다. [스트리밍](https://nextjs.org/docs/app/getting-started/fetching-data#streaming)에 대해 더 알아보세요.

#### 커뮤니티 라이브러리[](https://nextjs.org/docs/app/getting-started/fetching-data#community-libraries)

클라이언트 컴포넌트에서 데이터를 가져오기 위해 [SWR](https://swr.vercel.app/)이나 [React Query](https://tanstack.com/query/latest) 같은 커뮤니티 라이브러리를 사용할 수 있습니다. 이러한 라이브러리는 캐싱, 스트리밍 등 고유한 동작을 제공합니다. 예를 들어, SWR을 사용하면 다음과 같습니다.

app/blog/page.tsx

JavaScriptTypeScript
[code]
    'use client'
    import useSWR from 'swr'
     
    const fetcher = (url) => fetch(url).then((r) => r.json())
     
    export default function BlogPage() {
      const { data, error, isLoading } = useSWR(
        'https://api.vercel.app/blog',
        fetcher
      )
     
      if (isLoading) return <div>Loading...</div>
      if (error) return <div>Error: {error.message}</div>
     
      return (
        <ul>
          {data.map((post: { id: string; title: string }) => (
            <li key={post.id}>{post.title}</li>
          ))}
        </ul>
      )
    }
[/code]

## 요청 중복 제거 및 데이터 캐싱[](https://nextjs.org/docs/app/getting-started/fetching-data#deduplicate-requests-and-cache-data)

`fetch` 요청을 중복 제거하는 한 가지 방법은 [요청 메모이제이션](https://nextjs.org/docs/app/guides/caching#request-memoization)입니다. 이 메커니즘은 단일 렌더 패스에서 동일한 URL과 옵션으로 `GET` 또는 `HEAD`를 호출하면 요청을 하나로 결합합니다. 기본으로 동작하며, `fetch`에 Abort 시그널을 전달해 [옵트아웃](https://nextjs.org/docs/app/guides/caching#opting-out)할 수 있습니다.

요청 메모이제이션의 범위는 요청 수명과 동일합니다.

`fetch` 옵션에서 `cache: 'force-cache'`를 설정하는 등 Next.js의 [데이터 캐시](https://nextjs.org/docs/app/guides/caching#data-cache)를 사용해 `fetch` 요청을 중복 제거할 수도 있습니다.

데이터 캐시는 현재 렌더 패스와 이후 요청 간에 데이터를 공유할 수 있게 해줍니다.

만약 `fetch`를 _사용하지 않고_ ORM이나 데이터베이스를 직접 사용한다면 [React `cache`](https://react.dev/reference/react/cache) 함수로 데이터 액세스를 래핑하세요.

app/lib/data.ts

JavaScriptTypeScript
[code]
    import { cache } from 'react'
    import { db, posts, eq } from '@/lib/db'
     
    export const getPost = cache(async (id: string) => {
      const post = await db.query.posts.findFirst({
        where: eq(posts.id, parseInt(id)),
      })
    })
[/code]

## 스트리밍[](https://nextjs.org/docs/app/getting-started/fetching-data#streaming)

> **경고:** 아래 내용은 애플리케이션에서 [`cacheComponents` 구성 옵션](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)을 활성화했다는 전제입니다. 이 플래그는 Next.js 15 카나리에서 도입되었습니다.

서버 컴포넌트에서 데이터를 가져오면 요청마다 서버에서 데이터가 가져와지고 렌더링됩니다. 느린 데이터 요청이 있으면 모든 데이터가 준비될 때까지 전체 라우트 렌더링이 차단됩니다.

초기 로드 시간과 사용자 경험을 개선하려면 페이지 HTML을 작은 청크로 나누어 서버에서 클라이언트로 순차적으로 전송하는 스트리밍을 활용할 수 있습니다.

애플리케이션에서 스트리밍을 활용하는 방법은 두 가지입니다.

  1. [`loading.js` 파일](https://nextjs.org/docs/app/getting-started/fetching-data#with-loadingjs)로 페이지를 래핑
  2. [`<Suspense>`](https://nextjs.org/docs/app/getting-started/fetching-data#with-suspense)로 컴포넌트를 래핑



### `loading.js` 사용하기[](https://nextjs.org/docs/app/getting-started/fetching-data#with-loadingjs)

페이지와 동일한 폴더 안에 `loading.js` 파일을 만들어 데이터를 가져오는 동안 **전체 페이지**를 스트리밍할 수 있습니다. 예를 들어 `app/blog/page.js`를 스트리밍하려면 `app/blog` 폴더에 파일을 추가하세요.

app/blog/loading.tsx

JavaScriptTypeScript
[code]
    export default function Loading() {
      // Define the Loading UI here
      return <div>Loading...</div>
    }
[/code]

내비게이션 시 사용자는 레이아웃과 [로딩 상태](https://nextjs.org/docs/app/getting-started/fetching-data#creating-meaningful-loading-states)를 즉시 확인할 수 있고, 페이지 렌더링이 완료되면 새 콘텐츠로 자동 교체됩니다.

백그라운드에서는 `loading.js`가 `layout.js` 안에 중첩되어 `page.js`와 그 하위 요소 전체를 `<Suspense>` 경계로 자동 래핑합니다.

이 접근 방식은 라우트 세그먼트(레이아웃, 페이지)에 적합하지만 더 세밀한 스트리밍이 필요하면 `<Suspense>`를 사용하세요.

### `<Suspense>` 사용하기[](https://nextjs.org/docs/app/getting-started/fetching-data#with-suspense)

`<Suspense>`를 사용하면 페이지에서 스트리밍할 영역을 더 세밀하게 제어할 수 있습니다. 예를 들어 `<Suspense>` 경계 밖의 콘텐츠는 즉시 보여 주고, 경계 안의 블로그 글 목록은 스트리밍할 수 있습니다.

app/blog/page.tsx

JavaScriptTypeScript
[code]
    import { Suspense } from 'react'
    import BlogList from '@/components/BlogList'
    import BlogListSkeleton from '@/components/BlogListSkeleton'
     
    export default function BlogPage() {
      return (
        <div>
          {/* This content will be sent to the client immediately */}
          <header>
            <h1>Welcome to the Blog</h1>
            <p>Read the latest posts below.</p>
          </header>
          <main>
            {/* If there's any dynamic content inside this boundary, it will be streamed in */}
            <Suspense fallback={<BlogListSkeleton />}>
              <BlogList />
            </Suspense>
          </main>
        </div>
      )
    }
[/code]

### 의미 있는 로딩 상태 만들기[](https://nextjs.org/docs/app/getting-started/fetching-data#creating-meaningful-loading-states)

즉시 표시되는 로딩 상태는 내비게이션 직후 사용자에게 보여지는 폴백 UI입니다. 최고의 사용자 경험을 위해 앱이 응답 중임을 이해할 수 있도록 의미 있는 로딩 상태를 설계하는 것이 좋습니다. 예를 들어 스켈레톤, 스피너 또는 커버 사진·제목처럼 앞으로 표시될 화면의 일부를 보여 줄 수 있습니다.

개발 환경에서는 [React DevTools](https://react.dev/learn/react-developer-tools)를 사용해 컴포넌트의 로딩 상태를 미리 보고 검사할 수 있습니다.

## 예시[](https://nextjs.org/docs/app/getting-started/fetching-data#examples)

### 순차적 데이터 가져오기[](https://nextjs.org/docs/app/getting-started/fetching-data#sequential-data-fetching)

순차적 데이터 가져오기는 한 요청이 다른 요청의 데이터에 의존할 때 발생합니다.

예를 들어 `<Playlists>`는 `artistID`가 필요하므로 `<Artist>`가 완료된 후에만 데이터를 가져올 수 있습니다.

app/artist/[username]/page.tsx

JavaScriptTypeScript
[code]
    export default async function Page({
      params,
    }: {
      params: Promise<{ username: string }>
    }) {
      const { username } = await params
      // Get artist information
      const artist = await getArtist(username)
     
      return (

<>
          <h1>{artist.name}</h1>
          {/* Show fallback UI while the Playlists component is loading */}
          <Suspense fallback={<div>Loading...</div>}>
            {/* Pass the artist ID to the Playlists component */}
            <Playlists artistID={artist.id} />
          </Suspense>
        </>
      )
    }
     
    async function Playlists({ artistID }: { artistID: string }) {
      // Use the artist ID to fetch playlists
      const playlists = await getArtistPlaylists(artistID)
     
      return (
        <ul>
          {playlists.map((playlist) => (
            <li key={playlist.id}>{playlist.name}</li>
          ))}
        </ul>
      )
    }
[/code]

이 예제에서 `<Suspense>`는 아티스트 데이터가 로드된 뒤 플레이리스트를 스트리밍하도록 허용합니다. 그러나 페이지는 어떤 내용을 표시하기 전에 여전히 아티스트 데이터를 기다립니다. 이를 방지하려면 전체 페이지 컴포넌트를 `<Suspense>` 경계로 감싸(예: [`loading.js` 파일](https://nextjs.org/docs/app/getting-started/fetching-data#with-loadingjs)을 사용) 즉시 로딩 상태를 표시할 수 있습니다.

첫 번째 요청이 모든 것을 차단하므로 데이터 소스가 이를 빠르게 해결할 수 있는지 확인하세요. 요청을 더 이상 최적화할 수 없다면, 데이터 변경 빈도가 낮은 경우 결과를 [캐시](https://nextjs.org/docs/app/getting-started/fetching-data#deduplicate-requests-and-cache-data)하는 것을 고려하세요.

### 병렬 데이터 패칭[](https://nextjs.org/docs/app/getting-started/fetching-data#parallel-data-fetching)

병렬 데이터 패칭은 경로의 데이터 요청을 미리 시작하여 동시에 실행될 때 발생합니다.

기본적으로 [레이아웃과 페이지](https://nextjs.org/docs/app/getting-started/layouts-and-pages)는 병렬로 렌더링됩니다. 따라서 각 세그먼트는 가능한 한 빨리 데이터 가져오기를 시작합니다.

그러나 어떤 컴포넌트 내부에서도, 서로 다음에 위치한 여러 `async`/`await` 요청은 여전히 순차적으로 실행될 수 있습니다. 예를 들어, `getArtist`가 해결될 때까지 `getAlbums`는 차단됩니다:

app/artist/[username]/page.tsx

JavaScriptTypeScript
[code]
    import { getArtist, getAlbums } from '@/app/lib/data'
     
    export default async function Page({ params }) {
      // These requests will be sequential
      const { username } = await params
      const artist = await getArtist(username)
      const albums = await getAlbums(username)
      return <div>{artist.name}</div>
    }
[/code]

`fetch`를 호출하여 여러 요청을 시작한 다음 [`Promise.all`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)로 기다리세요. `fetch`가 호출되는 즉시 요청이 시작됩니다.

app/artist/[username]/page.tsx

JavaScriptTypeScript
[code]
    import Albums from './albums'
     
    async function getArtist(username: string) {
      const res = await fetch(`https://api.example.com/artist/${username}`)
      return res.json()
    }
     
    async function getAlbums(username: string) {
      const res = await fetch(`https://api.example.com/artist/${username}/albums`)
      return res.json()
    }
     
    export default async function Page({
      params,
    }: {
      params: Promise<{ username: string }>
    }) {
      const { username } = await params
     
      // Initiate requests
      const artistData = getArtist(username)
      const albumsData = getAlbums(username)
     
      const [artist, albums] = await Promise.all([artistData, albumsData])
     
      return (
        <>
          <h1>{artist.name}</h1>
          <Albums list={albums} />
        </>
      )
    }
[/code]

> **알아두면 좋아요:** `Promise.all`을 사용할 때 하나의 요청이라도 실패하면 전체 작업이 실패합니다. 이를 처리하려면 [`Promise.allSettled`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled) 메서드를 사용할 수 있습니다.

### 데이터 프리로딩[](https://nextjs.org/docs/app/getting-started/fetching-data#preloading-data)

차단되는 요청 위에서 미리 호출하는 유틸리티 함수를 만들어 데이터를 프리로드할 수 있습니다. `<Item>`은 `checkIsAvailable()` 함수에 따라 조건부로 렌더링됩니다.

`preload()`를 `checkIsAvailable()`보다 먼저 호출하여 `<Item/>`의 데이터 의존성을 미리 시작할 수 있습니다. `<Item/>`이 렌더링될 때쯤에는 해당 데이터가 이미 가져와집니다.

app/item/[id]/page.tsx

JavaScriptTypeScript
[code]
    import { getItem, checkIsAvailable } from '@/lib/data'
     
    export default async function Page({
      params,
    }: {
      params: Promise<{ id: string }>
    }) {
      const { id } = await params
      // starting loading item data
      preload(id)
      // perform another asynchronous task
      const isAvailable = await checkIsAvailable()
     
      return isAvailable ? <Item id={id} /> : null
    }
     
    const preload = (id: string) => {
      // void evaluates the given expression and returns undefined
      // https://developer.mozilla.org/docs/Web/JavaScript/Reference/Operators/void
      void getItem(id)
    }
     
    export async function Item({ id }: { id: string }) {
      const result = await getItem(id)
      // ...
    }
[/code]

또한 React의 [`cache` 함수](https://react.dev/reference/react/cache)와 [`server-only` 패키지](https://www.npmjs.com/package/server-only)를 사용하여 재사용 가능한 유틸리티 함수를 만들 수 있습니다. 이 접근 방식은 데이터 가져오기 함수를 캐시하고 서버에서만 실행되도록 보장합니다.

utils/get-item.ts

JavaScriptTypeScript
[code]
    import { cache } from 'react'
    import 'server-only'
    import { getItem } from '@/lib/data'
     
    export const preload = (id: string) => {
      void getItem(id)
    }
     
    export const getItem = cache(async (id: string) => {
      // ...
    })
[/code]

## API 레퍼런스

이 페이지에서 언급된 기능에 대해 더 알아보려면 API 레퍼런스를 확인하세요.

### [데이터 보안Next.js에 내장된 데이터 보안 기능을 살펴보고 애플리케이션 데이터를 보호하기 위한 모범 사례를 배우세요.](https://nextjs.org/docs/app/guides/data-security)### [fetch확장된 fetch 함수의 API 레퍼런스입니다.](https://nextjs.org/docs/app/api-reference/functions/fetch)### [loading.jsloading.js 파일의 API 레퍼런스입니다.](https://nextjs.org/docs/app/api-reference/file-conventions/loading)### [loggingNext.js를 개발 모드로 실행할 때 데이터 가져오기 로그를 구성합니다.](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging)### [taint객체와 값을 오염(taint)하도록 활성화합니다.](https://nextjs.org/docs/app/api-reference/config/next-config-js/taint)

도움이 되었나요?

지원됨.

보내기
