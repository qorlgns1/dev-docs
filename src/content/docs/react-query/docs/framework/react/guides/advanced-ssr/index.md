---
title: '고급 서버 렌더링'
description: '스트리밍, Server Components, Next.js 앱 라우터에서 React Query를 활용하는 방법을 모두 다루는 고급 서버 렌더링 가이드에 오신 것을 환영합니다.'
---

# 고급 서버 렌더링

스트리밍, Server Components, Next.js 앱 라우터에서 React Query를 활용하는 방법을 모두 다루는 고급 서버 렌더링 가이드에 오신 것을 환영합니다.

SSR에서 React Query를 사용하는 기초를 다루는 [Server Rendering & Hydration 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/ssr.md)와 함께, [Performance & Request Waterfalls](https://tanstack.com/query/latest/docs/framework/react/guides/request-waterfalls.md) 및 [Prefetching & Router Integration](https://tanstack.com/query/latest/docs/framework/react/guides/prefetching.md)도 배경 지식으로 읽어 두면 좋습니다.

시작하기 전에, SSR 가이드에서 소개한 `initialData` 접근법이 Server Components에서도 작동하지만, 여기서는 하이드레이션 API에 초점을 맞춥니다.

## Server Components & Next.js 앱 라우터

여기서 Server Components를 깊게 다루지는 않지만, 핵심은 초기 페이지 렌더링뿐 아니라 **페이지 전환 시에도** 서버에서만 실행된다는 점입니다. Next.js의 `getServerSideProps`/`getStaticProps`, Remix의 `loader`처럼 서버에서만 실행된다는 점은 비슷하지만, 해당 함수들이 데이터만 반환할 수 있는 것과 달리 Server Components는 훨씬 많은 일을 할 수 있습니다. 다만 React Query와 관련된 부분은 데이터이므로 여기에 집중해 봅시다.

SSR 가이드에서 다뤘던 [프레임워크 로더에서 미리 가져온 데이터를 앱으로 전달](https://tanstack.com/query/latest/docs/framework/react/guides/ssr.md#using-the-hydration-apis)하는 방법을 Server Components와 Next.js 앱 라우터에 어떻게 적용할까요? 이를 생각하는 가장 좋은 시작점은 Server Components를 "또 다른 프레임워크 로더" 정도로 간주하는 것입니다.

### 용어에 대한 짧은 메모

지금까지 가이드에서는 _server_와 _client_를 이야기했습니다. 혼란스럽지만 이것이 _Server Components_와 _Client Components_에 1:1로 대응하지는 않습니다. Server Components는 서버에서만 실행되지만, Client Components는 실제로 두 환경에서 모두 실행될 수 있습니다. 초기 _서버 렌더링_ 단계에서도 렌더링될 수 있기 때문입니다.

이렇게 생각할 수 있습니다. Server Components도 _렌더링_을 하지만 항상 서버에서 일어나는 "로더 단계" 동안에 실행되고, Client Components는 "애플리케이션 단계"에서 실행됩니다. 이 애플리케이션은 SSR 동안 서버에서, 혹은 브라우저 같은 환경에서 실행될 수 있습니다. 애플리케이션이 어디에서 실행되는지, SSR 중에 실행되는지는 프레임워크마다 다를 수 있습니다.

### 초기 설정

React Query 설정의 첫 단계는 항상 `queryClient`를 만들고 애플리케이션을 `QueryClientProvider`로 감싸는 것입니다. Server Components에서도 대부분의 프레임워크에서 동일하며, 차이가 있다면 파일명 규칙 정도입니다.

```tsx
// In Next.js, this file would be called: app/providers.tsx
'use client'

// Since QueryClientProvider relies on useContext under the hood, we have to put 'use client' on top
import {
  isServer,
  QueryClient,
  QueryClientProvider,
} from '@tanstack/react-query'

function makeQueryClient() {
  return new QueryClient({
    defaultOptions: {
      queries: {
        // With SSR, we usually want to set some default staleTime
        // above 0 to avoid refetching immediately on the client
        staleTime: 60 * 1000,
      },
    },
  })
}

let browserQueryClient: QueryClient | undefined = undefined

function getQueryClient() {
  if (isServer) {
    // Server: always make a new query client
    return makeQueryClient()
  } else {
    // Browser: make a new query client if we don't already have one
    // This is very important, so we don't re-make a new client if React
    // suspends during the initial render. This may not be needed if we
    // have a suspense boundary BELOW the creation of the query client
    if (!browserQueryClient) browserQueryClient = makeQueryClient()
    return browserQueryClient
  }
}

export default function Providers({ children }: { children: React.ReactNode }) {
  // NOTE: Avoid useState when initializing the query client if you don't
  //       have a suspense boundary between this and the code that may
  //       suspend because React will throw away the client on the initial
  //       render if it suspends and there is no boundary
  const queryClient = getQueryClient()

  return (
    <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
  )
}
```

```tsx
// In Next.js, this file would be called: app/layout.tsx
import Providers from './providers'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head />
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  )
}
```

SSR 가이드에서 했던 것과 거의 동일하지만, 이번에는 두 개의 파일로 나눠야 합니다.

### 데이터 프리패칭 및 디/하이드레이션

다음으로 실제로 데이터를 프리패치하고, 디하이드레이트한 뒤 다시 하이드레이트하는 방법을 살펴봅시다. **Next.js Pages Router**에서는 다음과 같았습니다.

```tsx
// pages/posts.tsx
import {
  dehydrate,
  HydrationBoundary,
  QueryClient,
  useQuery,
} from '@tanstack/react-query'

// This could also be getServerSideProps
export async function getStaticProps() {
  const queryClient = new QueryClient()

  await queryClient.prefetchQuery({
    queryKey: ['posts'],
    queryFn: getPosts,
  })

  return {
    props: {
      dehydratedState: dehydrate(queryClient),
    },
  }
}

function Posts() {
  // This useQuery could just as well happen in some deeper child to
  // the <PostsRoute>, data will be available immediately either way
  //
  // Note that we are using useQuery here instead of useSuspenseQuery.
  // Because this data has already been prefetched, there is no need to
  // ever suspend in the component itself. If we forget or remove the
  // prefetch, this will instead fetch the data on the client, while
  // using useSuspenseQuery would have had worse side effects.
  const { data } = useQuery({ queryKey: ['posts'], queryFn: getPosts })

  // This query was not prefetched on the server and will not start
  // fetching until on the client, both patterns are fine to mix
  const { data: commentsData } = useQuery({
    queryKey: ['posts-comments'],
    queryFn: getComments,
  })

  // ...
}

export default function PostsRoute({ dehydratedState }) {
  return (
    <HydrationBoundary state={dehydratedState}>
      <Posts />
    </HydrationBoundary>
  )
}
```

이를 앱 라우터로 전환하는 것도 상당히 비슷하며, 다만 구성을 조금 옮기기만 하면 됩니다. 먼저 프리패칭을 담당할 Server Component를 만듭니다.

```tsx
// app/posts/page.tsx
import {
  dehydrate,
  HydrationBoundary,
  QueryClient,
} from '@tanstack/react-query'
import Posts from './posts'

export default async function PostsPage() {
  const queryClient = new QueryClient()

  await queryClient.prefetchQuery({
    queryKey: ['posts'],
    queryFn: getPosts,
  })

  return (
    // Neat! Serialization is now as easy as passing props.
    // HydrationBoundary is a Client Component, so hydration will happen there.
    <HydrationBoundary state={dehydrate(queryClient)}>
      <Posts />
    </HydrationBoundary>
  )
}
```

이제 Client Component 부분을 살펴봅니다.

```tsx
// app/posts/posts.tsx
'use client'

export default function Posts() {
  // This useQuery could just as well happen in some deeper
  // child to <Posts>, data will be available immediately either way
  const { data } = useQuery({
    queryKey: ['posts'],
    queryFn: () => getPosts(),
  })

  // This query was not prefetched on the server and will not start
  // fetching until on the client, both patterns are fine to mix.
  const { data: commentsData } = useQuery({
    queryKey: ['posts-comments'],
    queryFn: getComments,
  })

  // ...
}
```

위 예제들의 좋은 점은 Next.js 전용인 부분이 파일 이름뿐이라는 점입니다. Server Components를 지원하는 다른 프레임워크에서도 나머지 내용은 동일하게 보일 것입니다.

SSR 가이드에서는 모든 라우트마다 `<HydrationBoundary>`를 추가해야 하는 보일러플레이트를 제거할 수 있다고 언급했는데, Server Components에서는 불가능합니다.

> NOTE: TypeScript `5.1.3` 미만 및 `@types/react` `18.2.8` 미만 버전에서 async Server Components 사용 시 타입 오류가 발생한다면 두 버전을 최신으로 업데이트하는 것이 좋습니다. 대신 일시적인 해결책으로, 해당 컴포넌트를 다른 컴포넌트에서 호출할 때 `{/* @ts-expect-error Server Component */}`를 추가할 수도 있습니다. 자세한 내용은 Next.js 13 문서의 [Async Server Component TypeScript Error](https://nextjs.org/docs/app/building-your-application/configuring/typescript#async-server-component-typescript-error)를 참고하세요.

> NOTE: `Only plain objects, and a few built-ins, can be passed to Server Actions. Classes or null prototypes are not supported.` 오류가 발생한다면, queryFn에 함수 참조를 전달하지 **않고** 함수를 호출했는지 확인하세요. queryFn 인수에는 다양한 속성이 있으며 모두 직렬화 가능한 것은 아닙니다. 자세한 내용은 [Server Action only works when queryFn isn't a reference](https://github.com/TanStack/query/issues/6264)를 참고하세요.

### Server Components 중첩

Server Components의 장점은 React 트리의 여러 레벨에서 중첩될 수 있다는 점입니다. 이를 통해 애플리케이션 최상단이 아니라 실제로 데이터를 사용하는 지점에 더 가까이에서 데이터를 프리패치할 수 있습니다(마치 Remix 로더와 유사). 다음 예시는 간단히 한 Server Component가 다른 Server Component를 렌더링하는 경우입니다(간결함을 위해 Client Components는 제외했습니다).

```tsx
// app/posts/page.tsx
import {
  dehydrate,
  HydrationBoundary,
  QueryClient,
} from '@tanstack/react-query'
import Posts from './posts'
import CommentsServerComponent from './comments-server'

export default async function PostsPage() {
  const queryClient = new QueryClient()

  await queryClient.prefetchQuery({
    queryKey: ['posts'],
    queryFn: getPosts,
  })

  return (
    <HydrationBoundary state={dehydrate(queryClient)}>
      <Posts />
      <CommentsServerComponent />
    </HydrationBoundary>
  )
}

// app/posts/comments-server.tsx
import {
  dehydrate,
  HydrationBoundary,
  QueryClient,
} from '@tanstack/react-query'
import Comments from './comments'

export default async function CommentsServerComponent() {
  const queryClient = new QueryClient()

  await queryClient.prefetchQuery({
    queryKey: ['posts-comments'],
    queryFn: getComments,
  })

  return (
    <HydrationBoundary state={dehydrate(queryClient)}>
      <Comments />
    </HydrationBoundary>
  )
}
```

보시다시피 `<HydrationBoundary>`를 여러 곳에서 사용하는 것도 괜찮고, 프리패칭을 위해 여러 `queryClient`를 생성하고 디하이드레이트하는 것도 가능합니다.

`CommentsServerComponent`를 렌더링하기 전에 `getPosts`를 await하기 때문에 서버 측 워터폴이 생긴다는 점에 주목하세요.

```
1. |> getPosts()
2.   |> getComments()
```

데이터에 대한 서버 대기시간이 짧다면 큰 문제가 아닐 수도 있지만, 그래도 짚고 넘어갈 가치가 있습니다.

Next.js에서는 `page.tsx`뿐 아니라 `layout.tsx`, [parallel routes](https://nextjs.org/docs/app/building-your-application/routing/parallel-routes)에서도 데이터를 프리패치할 수 있습니다. 이들은 모두 라우팅의 일부이기 때문에 Next.js는 요청을 병렬로 처리할 수 있습니다. 위에서 `CommentsServerComponent`를 parallel route로 표현했다면 워터폴이 자동으로 평탄화됩니다.

더 많은 프레임워크가 Server Components를 지원하게 되면 각기 다른 라우팅 규칙이 등장할 수도 있습니다. 사용하는 프레임워크 문서를 꼭 확인하세요.

### 대안: 프리패칭에 단일 `queryClient` 사용

위 예제에서는 데이터를 가져오는 각 Server Component마다 새로운 `queryClient`를 생성했습니다. 이것이 권장되는 방식이지만, 원한다면 모든 Server Component에서 재사용되는 단일 클라이언트를 만들 수도 있습니다.

```tsx
// app/getQueryClient.tsx
import { QueryClient } from '@tanstack/react-query'
import { cache } from 'react'

// cache() is scoped per request, so we don't leak data between requests
const getQueryClient = cache(() => new QueryClient())
export default getQueryClient
```

이 접근법의 장점은 Server Component에서 호출되는 모든 위치(유틸리티 함수 포함)에서 `getQueryClient()`를 호출해 이 클라이언트를 가져올 수 있다는 것입니다. 단점은 `dehydrate(getQueryClient())`를 호출할 때마다 현재 Server Component와 관련 없는, 이미 직렬화했던 쿼리까지 포함해 _전체_ `queryClient`를 직렬화한다는 점입니다. 이는 불필요한 오버헤드를 초래합니다.

Next.js는 `fetch()`를 활용하는 요청을 이미 중복 제거하지만, queryFn에서 다른 것을 사용하거나 요청을 자동으로 디듀프하지 않는 프레임워크를 사용한다면, 직렬화 중복이 있더라도 위에서 설명한 단일 `queryClient` 방식이 더 타당할 수 있습니다.

> 향후 개선 아이디어로는 마지막 `dehydrateNew()` 호출 이후 _새롭게_ 추가된 쿼리만 직렬화하는 `dehydrateNew()` 함수(명칭 미정)를 고려 중입니다. 관심이 있다면 연락 주세요!

### 데이터 소유권과 재검증

Server Components에서는 데이터 소유권과 재검증에 대해 생각하는 것이 중요합니다. 왜 그런지 이해하기 위해 위 예제를 약간 수정해 봅시다.

```tsx
// app/posts/page.tsx
import {
  dehydrate,
  HydrationBoundary,
  QueryClient,
} from '@tanstack/react-query'
import Posts from './posts'

export default async function PostsPage() {
  const queryClient = new QueryClient()

  // Note we are now using fetchQuery()
  const posts = await queryClient.fetchQuery({
    queryKey: ['posts'],
    queryFn: getPosts,
  })

  return (
    <HydrationBoundary state={dehydrate(queryClient)}>
      {/* This is the new part */}
      <div>Nr of posts: {posts.length}</div>
      <Posts />
    </HydrationBoundary>
  )
}
```

이제 `getPosts` 쿼리의 데이터를 Server Component와 Client Component에서 모두 렌더링하고 있습니다. 초기 페이지 렌더에서는 문제가 없지만, `staleTime`이 지난 시점에 쿼리가 클라이언트에서 어떤 이유로 재검증된다면 어떻게 될까요?

React Query는 _Server Component를 재검증_하는 방법을 모르기 때문에, 클라이언트에서 데이터를 다시 가져오고 React가 게시물 목록을 다시 렌더링하면 `Nr of posts: {posts.length}` 값은 동기화되지 않게 됩니다.

`staleTime: Infinity`를 설정하면 React Query가 재검증을 하지 않으므로 괜찮지만, 애초에 React Query를 사용하는 목적과 맞지 않을 수 있습니다.

React Query와 Server Components의 조합이 의미 있는 경우는 다음과 같습니다.

- React Query를 사용하는 앱이 있고, 모든 데이터 페칭을 다시 작성하지 않고 Server Components로 마이그레이션하고 싶은 경우
- 익숙한 프로그래밍 패러다임을 유지하면서 Server Components의 장점을 필요한 곳에만 도입하고 싶은 경우
- React Query가 다루는 사용 사례가 있고, 선택한 프레임워크가 이를 제공하지 않는 경우

Server Components와 React Query를 언제 함께 써야 하는지 일반적인 조언을 하기는 어렵습니다. **새로운 Server Components 앱을 시작한다면, 프레임워크가 제공하는 데이터 페칭 도구만으로 먼저 시작하고, 정말 필요할 때까지 React Query를 도입하지 않도록 권장합니다.** 필요가 없을 수도 있는데, 그럼 괜찮습니다. 작업에 맞는 도구를 쓰면 됩니다!

만약 React Query를 사용한다면, 오류를 처리해야 하는 경우가 아니라면 `queryClient.fetchQuery`를 피하는 것이 좋습니다. 사용하더라도 결과를 서버에서 렌더링하거나 다른 컴포넌트(심지어 Client Component)에게 전달하지 마세요.

React Query 관점에서 Server Components는 데이터를 프리패치하는 장소에 불과하다고 생각하세요.

물론 Server Components가 일부 데이터를 소유하고, Client Components가 다른 데이터를 소유해도 괜찮지만, 두 현실이 서로 어긋나지 않도록 주의하세요.

## Server Components와 스트리밍

Next.js 앱 라우터는 준비가 끝난 애플리케이션 부분을 가능한 한 빨리 브라우저로 스트리밍하여, 아직 로딩 중인 콘텐츠를 기다리지 않고 완료된 콘텐츠를 즉시 보여줍니다. 이는 `<Suspense>` 경계를 기준으로 이루어집니다. 또한 `loading.tsx` 파일을 만들면 자동으로 `<Suspense>` 경계가 생성된다는 점에 유의하세요.

앞서 설명한 프리패칭 패턴을 사용하면 React Query는 이러한 스트리밍 방식과 완벽하게 호환됩니다. 각 Suspense 경계에 필요한 데이터가 준비되면 Next.js가 콘텐츠를 렌더링해 브라우저로 스트리밍할 수 있습니다. 위에서 설명한 것처럼 `useQuery`를 사용하더라도, 실제 중단(suspend)은 프리패칭을 `await`할 때 발생하므로 문제 없습니다.

React Query v5.40.0부터는 이런 기능을 위해 모든 프리패치를 `await`할 필요가 없습니다. `pending` 상태의 쿼리도 디하이드레이트하여 클라이언트로 전송할 수 있습니다. 덕분에 프리패치를 가능한 한 이른 시점에 시작하되, 전체 Suspense 경계를 막지 않고, 쿼리가 완료되는 대로 _데이터_를 클라이언트로 스트리밍할 수 있습니다. 예를 들어 사용자 상호작용 후에만 보이는 콘텐츠를 미리 가져오거나, 무한 쿼리의 첫 페이지를 `await`해 렌더링하고 페이지 2는 렌더링을 막지 않고 프리패치하고 싶을 때 유용합니다.

이 기능을 활용하려면 `queryClient`가 `pending` 쿼리도 `dehydrate`하도록 지시해야 합니다. 전역으로 설정하거나 `dehydrate` 호출 시 옵션을 전달할 수 있습니다.

또한 `getQueryClient()` 함수를 서버 컴포넌트와 클라이언트 프로바이더에서 모두 사용하려면 `app/providers.tsx` 파일 밖으로 옮겨야 합니다.

```tsx
// app/get-query-client.ts
import {
  isServer,
  QueryClient,
  defaultShouldDehydrateQuery,
} from '@tanstack/react-query'

function makeQueryClient() {
  return new QueryClient({
    defaultOptions: {
      queries: {
        staleTime: 60 * 1000,
      },
      dehydrate: {
        // include pending queries in dehydration
        shouldDehydrateQuery: (query) =>
          defaultShouldDehydrateQuery(query) ||
          query.state.status === 'pending',
        shouldRedactErrors: (error) => {
          // We should not catch Next.js server errors
          // as that's how Next.js detects dynamic pages
          // so we cannot redact them.
          // Next.js also automatically redacts errors for us
          // with better digests.
          return false
        },
      },
    },
  })
}

let browserQueryClient: QueryClient | undefined = undefined

export function getQueryClient() {
  if (isServer) {
    // Server: always make a new query client
    return makeQueryClient()
  } else {
    // Browser: make a new query client if we don't already have one
    // This is very important, so we don't re-make a new client if React
    // suspends during the initial render. This may not be needed if we
    // have a suspense boundary BELOW the creation of the query client
    if (!browserQueryClient) browserQueryClient = makeQueryClient()
    return browserQueryClient
  }
}
```

> Note: React가 Promise를 직렬화할 수 있기 때문에 Next.js와 Server Components에서 작동합니다. Promise를 Client Component에 전달하면 와이어를 통해 직렬화됩니다.

그다음 할 일은 `HydrationBoundary`를 제공하는 것뿐이며, 더 이상 프리패치를 `await`할 필요가 없습니다.

```tsx
// app/posts/page.tsx
import { dehydrate, HydrationBoundary } from '@tanstack/react-query'
import { getQueryClient } from './get-query-client'
import Posts from './posts'

// the function doesn't need to be `async` because we don't `await` anything
export default function PostsPage() {
  const queryClient = getQueryClient()

  // look ma, no await
  queryClient.prefetchQuery({
    queryKey: ['posts'],
    queryFn: getPosts,
  })

  return (
    <HydrationBoundary state={dehydrate(queryClient)}>
      <Posts />
    </HydrationBoundary>
  )
}
```

클라이언트에서는 Promise가 자동으로 QueryCache에 저장됩니다. 이제 서버에서 생성된 해당 Promise를 활용하기 위해 `Posts` 컴포넌트 안에서 `useSuspenseQuery`를 호출할 수 있습니다:

```tsx
// app/posts/posts.tsx
'use client'

export default function Posts() {
  const { data } = useSuspenseQuery({ queryKey: ['posts'], queryFn: getPosts })

  // ...
}
```

> `useSuspenseQuery` 대신 `useQuery`를 사용할 수도 있으며, Promise는 동일하게 감지됩니다. 다만 이 경우 NextJs는 서스펜드하지 않으므로 컴포넌트가 `pending` 상태에서 렌더링되고, 콘텐츠의 서버 렌더링도 비활성화됩니다.

JSON이 아닌 데이터 타입을 사용하면서 서버에서 쿼리 결과를 직렬화한다면, 경계의 양쪽에서 데이터를 동일한 형식으로 유지하도록 `dehydrate.serializeData`와 `hydrate.deserializeData` 옵션을 지정해 각각 직렬화/역직렬화를 수행할 수 있습니다:

```tsx
// app/get-query-client.ts
import { QueryClient, defaultShouldDehydrateQuery } from '@tanstack/react-query'
import { deserialize, serialize } from './transformer'

function makeQueryClient() {
  return new QueryClient({
    defaultOptions: {
      // ...
      hydrate: {
        deserializeData: deserialize,
      },
      dehydrate: {
        serializeData: serialize,
      },
    },
  })
}

// ...
```

```tsx
// app/posts/page.tsx
import {
  dehydrate,
  HydrationBoundary,
  QueryClient,
} from '@tanstack/react-query'
import { getQueryClient } from './get-query-client'
import { serialize } from './transformer'
import Posts from './posts'

export default function PostsPage() {
  const queryClient = getQueryClient()

  // look ma, no await
  queryClient.prefetchQuery({
    queryKey: ['posts'],
    queryFn: () => getPosts().then(serialize), // <-- serialize the data on the server
  })

  return (
    <HydrationBoundary state={dehydrate(queryClient)}>
      <Posts />
    </HydrationBoundary>
  )
}
```

```tsx
// app/posts/posts.tsx
'use client'

export default function Posts() {
  const { data } = useSuspenseQuery({ queryKey: ['posts'], queryFn: getPosts })

  // ...
}
```

이제 `getPosts` 함수는 예를 들어 `Temporal` datetime 객체를 반환할 수 있고, 변환기가 해당 데이터 타입을 직렬화/역직렬화할 수 있다면 클라이언트에서도 동일하게 직렬화/역직렬화됩니다.

자세한 내용은 [Next.js App with Prefetching Example](https://tanstack.com/query/latest/docs/framework/react/examples/nextjs-app-prefetching)을 참고하세요.

### Streaming과 Persist Adapter 사용하기

[Streaming with Server Components](#streaming-with-server-components) 기능과 함께 persist adapter를 사용할 경우, Promise를 스토리지에 저장하지 않도록 주의해야 합니다. 보류 중인 쿼리는 탈수되어 클라이언트로 스트리밍될 수 있으므로, 퍼시스터를 성공한 쿼리만 유지하도록 구성해야 합니다:

```tsx
<PersistQueryClientProvider
  client={queryClient}
  persistOptions={{
    persister,
    // We don't want to save promises into the storage, so we only persist successful queries
    dehydrateOptions: { shouldDehydrateQuery: defaultShouldDehydrateQuery },
  }}
>
  {children}
</PersistQueryClientProvider>
```

이렇게 하면 성공적으로 완료된 쿼리만 스토리지에 저장되어, 보류 중인 Promise 직렬화 문제를 예방할 수 있습니다.

## Next.js에서 프리패칭 없이 실험적인 스트리밍

초기 페이지 로드 **및** 이후 페이지 이동 모두에서 요청 폭포를 평탄화하는 위의 프리패칭 솔루션을 권장하지만, 프리패칭 없이도 스트리밍 SSR이 동작하도록 하는 실험적인 방법이 있습니다: `@tanstack/react-query-next-experimental`

이 패키지를 사용하면 클라이언트 컴포넌트에서 `useSuspenseQuery`를 호출하는 것만으로 서버에서 데이터를 가져올 수 있습니다. 결과는 SuspenseBoundary가 해결되는 순서대로 서버에서 클라이언트로 스트리밍됩니다. `<Suspense>` 경계로 감싸지 않고 `useSuspenseQuery`를 호출하면, fetch가 완료될 때까지 HTML 응답이 시작되지 않습니다. 상황에 따라 의도적으로 그렇게 할 수도 있지만 TTFB에 악영향을 줄 수 있다는 점을 기억하세요.

이를 위해 앱을 `ReactQueryStreamedHydration` 컴포넌트로 감싸면 됩니다:

```tsx
// app/providers.tsx
'use client'

import {
  isServer,
  QueryClient,
  QueryClientProvider,
} from '@tanstack/react-query'
import * as React from 'react'
import { ReactQueryStreamedHydration } from '@tanstack/react-query-next-experimental'

function makeQueryClient() {
  return new QueryClient({
    defaultOptions: {
      queries: {
        // With SSR, we usually want to set some default staleTime
        // above 0 to avoid refetching immediately on the client
        staleTime: 60 * 1000,
      },
    },
  })
}

let browserQueryClient: QueryClient | undefined = undefined

function getQueryClient() {
  if (isServer) {
    // Server: always make a new query client
    return makeQueryClient()
  } else {
    // Browser: make a new query client if we don't already have one
    // This is very important, so we don't re-make a new client if React
    // suspends during the initial render. This may not be needed if we
    // have a suspense boundary BELOW the creation of the query client
    if (!browserQueryClient) browserQueryClient = makeQueryClient()
    return browserQueryClient
  }
}

export function Providers(props: { children: React.ReactNode }) {
  // NOTE: Avoid useState when initializing the query client if you don't
  //       have a suspense boundary between this and the code that may
  //       suspend because React will throw away the client on the initial
  //       render if it suspends and there is no boundary
  const queryClient = getQueryClient()

  return (
    <QueryClientProvider client={queryClient}>
      <ReactQueryStreamedHydration>
        {props.children}
      </ReactQueryStreamedHydration>
    </QueryClientProvider>
  )
}
```

자세한 내용은 [NextJs Suspense Streaming Example](https://tanstack.com/query/latest/docs/framework/react/examples/nextjs-suspense-streaming)을 확인하세요.

이 접근법의 가장 큰 장점은 SSR을 위해 더 이상 수동으로 쿼리를 프리패치할 필요가 없고, 여전히 결과를 스트리밍할 수 있다는 점입니다. 덕분에 뛰어난 DX와 낮은 코드 복잡도를 얻을 수 있습니다.

단점은 Performance & Request Waterfalls 가이드의 [복잡한 요청 폭포 예시](https://tanstack.com/query/latest/docs/framework/react/guides/request-waterfalls.md#code-splitting)를 다시 보면 쉽게 이해할 수 있습니다. 프리패칭이 있는 서버 컴포넌트는 초기 페이지 로드와 이후 내비게이션 모두에서 요청 폭포를 사실상 제거합니다. 반면 이 프리패칭 없는 접근은 초기 로드에서만 폭포를 평탄화하고, 페이지 이동 시에는 원래 예시처럼 깊은 폭포가 다시 발생합니다:

```
1. |> JS for <Feed>
2.   |> getFeed()
3.     |> JS for <GraphFeedItem>
4.       |> getGraphDataById()
```

이는 `getServerSideProps`/`getStaticProps`보다도 더 나쁜데, 해당 방식에서는 데이터와 코드를 최소한 병렬로 가져올 수 있기 때문입니다.

DX·반복·배포 속도와 낮은 코드 복잡도를 성능보다 더 중시하거나, 쿼리가 깊게 중첩되지 않았거나, `useSuspenseQueries` 같은 도구로 병렬 fetching을 통해 요청 폭포를 잘 관리하고 있다면, 이 트레이드오프를 택하는 것도 좋은 선택이 될 수 있습니다.

> 두 접근법을 조합하는 것도 가능할지 모르지만, 아직 저희도 시도해 보지 않았습니다. 시도해 보신다면 경험을 공유하거나, 이 문서를 업데이트해 주시면 더욱 좋겠습니다!

## 마무리

서버 컴포넌트와 스트리밍은 아직 비교적 새로운 개념이며, React Query가 어떻게 적합하고 API를 어떻게 개선할 수 있을지 계속 고민 중입니다. 제안, 피드백, 버그 리포트를 언제든 환영합니다!

또한 이 새로운 패러다임의 모든 디테일을 한 번의 가이드로 모두 설명하기는 어렵습니다. 여기서 빠진 정보가 있거나 콘텐츠 개선 아이디어가 있다면 언제든 연락주시거나, 더 나아가 아래의 "Edit on GitHub" 버튼을 눌러 직접 도와주세요.

[//]: # 'Materials'

## 추가 읽을거리

서버 컴포넌트를 함께 사용할 때 애플리케이션이 React Query의 이점을 얻을 수 있는지 알고 싶다면 [You Might Not Need React Query](https://tkdodo.eu/blog/you-might-not-need-react-query) 글을 참고하세요.

[//]: # 'Materials'

