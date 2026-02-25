---
title: '서버 렌더링 & 하이드레이션'
description: '이 가이드에서는 서버 렌더링과 함께 React Query를 사용하는 방법을 배웁니다.'
---

# 서버 렌더링 & 하이드레이션

이 가이드에서는 서버 렌더링과 함께 React Query를 사용하는 방법을 배웁니다.

배경 지식이 필요하다면 [Prefetching & Router Integration](https://tanstack.com/query/latest/docs/framework/react/guides/prefetching.md) 가이드를 읽어 보세요. 그 전에 [Performance & Request Waterfalls 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/request-waterfalls.md)도 확인하는 것이 좋습니다.

스트리밍, Server Components, 새로운 Next.js 앱 라우터 같은 고급 서버 렌더링 패턴이 궁금하다면 [Advanced Server Rendering 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr.md)를 참고하세요.

코드를 바로 보고 싶다면 아래의 [전체 Next.js 페이지 라우터 예제](#full-nextjs-pages-router-example)나 [전체 Remix 예제](#full-remix-example)로 건너뛰어도 됩니다.

## 서버 렌더링 & React Query

서버 렌더링은 무엇일까요? 이 가이드는 기본 개념을 알고 있다고 가정하지만, React Query와 어떤 관계가 있는지 잠시 짚고 넘어가겠습니다. 서버 렌더링은 사용자가 페이지를 불러오는 즉시 볼 수 있도록 서버에서 초기 HTML을 생성하는 행위입니다. 이는 페이지가 요청될 때마다 즉석에서 실행될 수도 있고(SSR), 이전 요청이 캐시되었거나 빌드 시점(SSG)에 미리 실행될 수도 있습니다.

Request Waterfalls 가이드를 읽었다면 다음과 같은 내용을 기억할 수 있습니다:

```
1. |-> Markup (without content)
2.   |-> JS
3.     |-> Query
```

클라이언트 렌더링 애플리케이션에서는 사용자가 화면에서 어떤 콘텐츠라도 보기 전에 최소한 위와 같은 세 번의 서버 왕복이 필요합니다. 서버 렌더링은 이를 아래와 같이 바꿔 줍니다:

```
1. |-> Markup (with content AND initial data)
2.   |-> JS
```

**1.**이 완료되는 즉시 사용자는 콘텐츠를 볼 수 있고 **2.**가 끝나면 페이지는 상호작용 가능해집니다. 필요한 초기 데이터가 마크업에 포함되어 있으므로 **3.** 단계는 적어도 데이터를 재검증하기 전까지는 클라이언트에서 실행할 필요가 없습니다.

이 모든 것은 클라이언트 관점입니다. 서버에서는 마크업을 생성/렌더링하기 전에 데이터를 **prefetch**해야 하고, 해당 데이터를 마크업에 포함할 수 있는 직렬화 가능한 형식으로 **dehydrate**해야 합니다. 클라이언트에서는 React Query 캐시에 데이터를 **hydrate**해 새로 fetch하지 않도록 해야 합니다.

계속 읽으며 React Query로 이 세 단계를 구현하는 방법을 알아보세요.

## Suspense에 대한 짧은 메모

이 가이드는 기본 `useQuery` API를 사용합니다. 권장하진 않지만 **모든 쿼리를 항상 prefetch**한다면 이를 `useSuspenseQuery`로 바꿀 수도 있습니다. 이렇게 하면 클라이언트에서 로딩 상태를 위해 `<Suspense>`를 활용할 수 있습니다.

`useSuspenseQuery`를 사용할 때 쿼리를 prefetch하는 것을 잊으면, 어떤 프레임워크를 사용하느냐에 따라 결과가 달라집니다. 어떤 경우에는 데이터가 Suspend되어 서버에서 fetch되지만 클라이언트로 hydrate되지 않아 다시 fetch됩니다. 이 경우 서버와 클라이언트가 서로 다른 내용을 렌더링하려 했기 때문에 마크업 하이드레이션 불일치가 발생합니다.

## 초기 설정

React Query를 사용할 때 첫 단계는 항상 `queryClient`를 만들고 애플리케이션을 `<QueryClientProvider>`로 감싸는 것입니다. 서버 렌더링 시에는 `queryClient` 인스턴스를 **앱 내부**, React 상태(또는 인스턴스 ref)에서 생성하는 것이 중요합니다. **이렇게 해야 서로 다른 사용자나 요청 간에 데이터가 공유되지 않으면서도** 컴포넌트 라이프사이클당 한 번만 `queryClient`를 만들 수 있습니다.

Next.js 페이지 라우터:

```tsx
// _app.tsx
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'

// NEVER DO THIS:
// const queryClient = new QueryClient()
//
// Creating the queryClient at the file root level makes the cache shared
// between all requests and means _all_ data gets passed to _all_ users.
// Besides being bad for performance, this also leaks any sensitive data.

export default function MyApp({ Component, pageProps }) {
  // Instead do this, which ensures each request has its own cache:
  const [queryClient] = React.useState(
    () =>
      new QueryClient({
        defaultOptions: {
          queries: {
            // With SSR, we usually want to set some default staleTime
            // above 0 to avoid refetching immediately on the client
            staleTime: 60 * 1000,
          },
        },
      }),
  )

  return (
    <QueryClientProvider client={queryClient}>
      <Component {...pageProps} />
    </QueryClientProvider>
  )
}
```

Remix:

```tsx
// app/root.tsx
import { Outlet } from '@remix-run/react'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'

export default function MyApp() {
  const [queryClient] = React.useState(
    () =>
      new QueryClient({
        defaultOptions: {
          queries: {
            // With SSR, we usually want to set some default staleTime
            // above 0 to avoid refetching immediately on the client
            staleTime: 60 * 1000,
          },
        },
      }),
  )

  return (
    <QueryClientProvider client={queryClient}>
      <Outlet />
    </QueryClientProvider>
  )
}
```

## `initialData`로 빠르게 시작하기

가장 빠른 시작 방법은 prefetch와 관련해 React Query를 전혀 개입시키지 않고 `dehydrate`/`hydrate` API도 사용하지 않는 것입니다. 대신 `useQuery`의 `initialData` 옵션으로 원시 데이터를 전달하면 됩니다. `getServerSideProps`를 사용하는 Next.js 페이지 라우터 예제를 보겠습니다.

```tsx
export async function getServerSideProps() {
  const posts = await getPosts()
  return { props: { posts } }
}

function Posts(props) {
  const { data } = useQuery({
    queryKey: ['posts'],
    queryFn: getPosts,
    initialData: props.posts,
  })

  // ...
}
```

이 방법은 `getStaticProps`나 이전의 `getInitialProps`에서도 작동하며, 동등한 기능을 가진 다른 프레임워크에서도 동일한 패턴을 적용할 수 있습니다. Remix에서 동일한 예시는 다음과 같습니다:

```tsx
export async function loader() {
  const posts = await getPosts()
  return json({ posts })
}

function Posts() {
  const { posts } = useLoaderData<typeof loader>()

  const { data } = useQuery({
    queryKey: ['posts'],
    queryFn: getPosts,
    initialData: posts,
  })

  // ...
}
```

설정이 최소화되어 있어 일부 상황에서 빠른 해결책이 될 수 있지만, 전체 접근 방식과 비교하면 **몇 가지 트레이드오프**가 있습니다:

- 트리 더 깊은 곳의 컴포넌트에서 `useQuery`를 호출한다면 `initialData`를 그 지점까지 내려줘야 합니다.
- 동일한 쿼리를 여러 위치에서 `useQuery`로 호출할 경우, 단 한 곳에만 `initialData`를 넘기면 앱이 변경되면서 쉽게 깨질 수 있습니다. `initialData`를 가진 `useQuery` 컴포넌트를 제거하거나 이동하면 더 깊은 곳의 `useQuery`가 데이터를 받지 못할 수 있습니다. 필요한 모든 쿼리에 `initialData`를 넘기는 것도 번거로울 수 있습니다.
- 쿼리가 서버에서 언제 fetch되었는지 알 수 없으므로 `dataUpdatedAt`과 재-fetch 필요 여부는 페이지가 로드된 시점을 기준으로 합니다.
- 쿼리에 이미 캐시된 데이터가 있다면 `initialData`는 이 데이터를 절대 덮어쓰지 않습니다. **새 데이터가 더 최신이더라도 마찬가지**입니다.
  - 이것이 왜 특히 문제인지 이해하려면 위의 `getServerSideProps` 예제를 떠올려 보세요. 한 페이지를 여러 번 오가면 `getServerSideProps`는 매번 호출되어 새 데이터를 fetch하지만, `initialData` 옵션을 사용하기 때문에 클라이언트 캐시와 데이터는 갱신되지 않습니다.

전체 하이드레이션 솔루션을 설정하는 일은 간단하고 이런 단점이 없습니다. 나머지 문서는 이 전체 접근법에 초점을 맞춥니다.

## 하이드레이션 API 사용하기

조금 더 설정하면 preload 단계에서 `queryClient`로 쿼리를 prefetch하고, 그 직렬화된 버전을 앱 렌더링 부분에 전달하여 재사용할 수 있습니다. 이렇게 하면 위 단점들을 피할 수 있습니다. 전체 Next.js 페이지 라우터와 Remix 예제로 건너뛰어도 되지만, 일반적인 흐름은 다음과 같습니다:

- 프레임워크의 로더 함수에서 `const queryClient = new QueryClient(options)`를 생성합니다.
- 로더 함수에서 prefetch하려는 각 쿼리에 대해 `await queryClient.prefetchQuery(...)`를 호출합니다.
  - 가능하다면 `await Promise.all(...)`을 사용해 쿼리를 병렬로 fetch하세요.
  - prefetch하지 않는 쿼리가 있어도 괜찮습니다. 이러한 쿼리는 서버 렌더링되지 않고, 애플리케이션이 상호작용 가능해진 후 클라이언트에서 fetch됩니다. 사용자 인터랙션 이후에만 노출되거나 페이지 아래쪽에 위치한 콘텐츠에 유용합니다.
- 로더에서 `dehydrate(queryClient)`를 반환합니다. 반환 구문은 프레임워크마다 다릅니다.
- 트리를 `<HydrationBoundary state={dehydratedState}>`로 감싸는데, `dehydratedState`는 프레임워크 로더에서 전달받습니다. 이 값 역시 프레임워크마다 얻는 방식이 다릅니다.
  - 각 라우트에서 수행할 수도 있고, 예제처럼 최상단에서 설정해 보일러플레이트를 줄일 수도 있습니다.

> 흥미로운 점은 실제로 _세 개의_ `queryClient`가 관여한다는 것입니다. 프레임워크 로더는 렌더링 이전에 실행되는 일종의 "preloading" 단계이며, 여기에는 prefetch를 담당하는 고유한 `queryClient`가 있습니다. 이 단계에서 얻은 dehydrated 결과는 서버 렌더링 과정과 클라이언트 렌더링 과정 **양쪽**에 전달되며, 각 과정은 자체 `queryClient`를 가집니다. 덕분에 서로 같은 데이터로 시작해 동일한 마크업을 반환할 수 있습니다.

> Server Components는 React 컴포넌트 트리의 일부를 "preload"(미리 렌더)할 수 있는 또 다른 형태의 "preloading" 단계입니다. 자세한 내용은 [Advanced Server Rendering 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr.md)를 확인하세요.

### 전체 Next.js 페이지 라우터 예제

> 앱 라우터 문서는 [Advanced Server Rendering 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr.md)를 참고하세요.

초기 설정:

```tsx
// _app.tsx
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'

export default function MyApp({ Component, pageProps }) {
  const [queryClient] = React.useState(
    () =>
      new QueryClient({
        defaultOptions: {
          queries: {
            // With SSR, we usually want to set some default staleTime
            // above 0 to avoid refetching immediately on the client
            staleTime: 60 * 1000,
          },
        },
      }),
  )

  return (
    <QueryClientProvider client={queryClient}>
      <Component {...pageProps} />
    </QueryClientProvider>
  )
}
```

각 라우트에서:

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

### 전체 Remix 예제

초기 설정:

```tsx
// app/root.tsx
import { Outlet } from '@remix-run/react'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'

export default function MyApp() {
  const [queryClient] = React.useState(
    () =>
      new QueryClient({
        defaultOptions: {
          queries: {
            // With SSR, we usually want to set some default staleTime
            // above 0 to avoid refetching immediately on the client
            staleTime: 60 * 1000,
          },
        },
      }),
  )

  return (
    <QueryClientProvider client={queryClient}>
      <Outlet />
    </QueryClientProvider>
  )
}
```

각 라우트에서(중첩 라우트에서도 동일하게 적용 가능):

```tsx
// app/routes/posts.tsx
import { json } from '@remix-run/node'
import {
  dehydrate,
  HydrationBoundary,
  QueryClient,
  useQuery,
} from '@tanstack/react-query'

export async function loader() {
  const queryClient = new QueryClient()

  await queryClient.prefetchQuery({
    queryKey: ['posts'],
    queryFn: getPosts,
  })

  return json({ dehydratedState: dehydrate(queryClient) })
}

function Posts() {
  // This useQuery could just as well happen in some deeper child to
  // the <PostsRoute>, data will be available immediately either way
  const { data } = useQuery({ queryKey: ['posts'], queryFn: getPosts })

  // This query was not prefetched on the server and will not start
  // fetching until on the client, both patterns are fine to mix
  const { data: commentsData } = useQuery({
    queryKey: ['posts-comments'],
    queryFn: getComments,
  })

  // ...
}

export default function PostsRoute() {
  const { dehydratedState } = useLoaderData<typeof loader>()
  return (
    <HydrationBoundary state={dehydratedState}>
      <Posts />
    </HydrationBoundary>
  )
}
```

## 선택 사항 - 보일러플레이트 제거

모든 라우트에 다음 코드를 반복하는 것은 보일러플레이트처럼 보일 수 있습니다:

```tsx
export default function PostsRoute({ dehydratedState }) {
  return (
    <HydrationBoundary state={dehydratedState}>
      <Posts />
    </HydrationBoundary>
  )
}
```

이 방식에도 문제가 있는 것은 아니지만, Next.js에서 보일러플레이트를 줄이고 싶다면 아래와 같이 설정을 수정할 수 있습니다:

```tsx
// _app.tsx
import {
  HydrationBoundary,
  QueryClient,
  QueryClientProvider,
} from '@tanstack/react-query'

export default function MyApp({ Component, pageProps }) {
  const [queryClient] = React.useState(() => new QueryClient())

  return (
    <QueryClientProvider client={queryClient}>
      <HydrationBoundary state={pageProps.dehydratedState}>
        <Component {...pageProps} />
      </HydrationBoundary>
    </QueryClientProvider>
  )
}

// pages/posts.tsx
// Remove PostsRoute with the HydrationBoundary and instead export Posts directly:
export default function Posts() { ... }
```

Remix에서는 조금 더 복잡하므로 [use-dehydrated-state](https://github.com/maplegrove-io/use-dehydrated-state) 패키지를 살펴보는 것을 권장합니다.

## 의존 쿼리 prefetch

Prefetching 가이드에서는 [의존 쿼리 prefetch](https://tanstack.com/query/latest/docs/framework/react/guides/prefetching.md#dependent-queries--code-splitting)를 학습했는데, 이를 프레임워크 로더에서 어떻게 구현할까요? 아래 코드는 [Dependent Queries 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/dependent-queries.md)에서 가져온 예시입니다:

```tsx
// Get the user
const { data: user } = useQuery({
  queryKey: ['user', email],
  queryFn: getUserByEmail,
})

const userId = user?.id

// Then get the user's projects
const {
  status,
  fetchStatus,
  data: projects,
} = useQuery({
  queryKey: ['projects', userId],
  queryFn: getProjectsByUser,
  // The query will not execute until the userId exists
  enabled: !!userId,
})
```

이를 서버 렌더링할 수 있도록 prefetch하려면 어떻게 해야 할까요? 예시는 다음과 같습니다:

```tsx
// For Remix, rename this to loader instead
export async function getServerSideProps() {
  const queryClient = new QueryClient()

  const user = await queryClient.fetchQuery({
    queryKey: ['user', email],
    queryFn: getUserByEmail,
  })

  if (user?.userId) {
    await queryClient.prefetchQuery({
      queryKey: ['projects', userId],
      queryFn: getProjectsByUser,
    })
  }

  // For Remix:
  // return json({ dehydratedState: dehydrate(queryClient) })
  return { props: { dehydratedState: dehydrate(queryClient) } }
}
```

물론 훨씬 복잡해질 수 있지만, 로더 함수는 결국 자바스크립트이므로 언어의 모든 기능을 활용해 로직을 구성할 수 있습니다. 서버 렌더링하려는 모든 쿼리를 반드시 prefetch하세요.

## 오류 처리

React Query는 우아한 강등(graceful degradation)을 기본 전략으로 사용합니다. 이는 다음을 의미합니다:

- `queryClient.prefetchQuery(...)`는 절대 오류를 던지지 않습니다.
- `dehydrate(...)`는 실패한 쿼리가 아니라 성공한 쿼리만 포함합니다.

이로 인해 실패한 쿼리는 클라이언트에서 재시도되고, 서버 렌더링 출력에는 전체 콘텐츠 대신 로딩 상태가 포함됩니다.

좋은 기본값이긴 하지만, 상황에 따라 원하는 결과가 아닐 수도 있습니다. 중요한 콘텐츠가 없을 경우 상황에 맞게 404나 500 상태 코드로 응답하고 싶을 수 있습니다. 이런 경우에는 실패 시 오류를 던지는 `queryClient.fetchQuery(...)`를 사용해 적절히 처리하세요.

```tsx
let result

try {
  result = await queryClient.fetchQuery(...)
} catch (error) {
  // Handle the error, refer to your framework documentation
}

// You might also want to check and handle any invalid `result` here
```

어떤 이유로든 실패한 쿼리를 dehydrated 상태에 포함해 재시도를 피하고 싶다면, `shouldDehydrateQuery` 옵션으로 기본 함수를 오버라이드해 자체 로직을 구현할 수 있습니다:

```tsx
dehydrate(queryClient, {
  shouldDehydrateQuery: (query) => {
    // This will include all queries, including failed ones,
    // but you can also implement your own logic by inspecting `query`
    return true
  },
})
```

## 직렬화

Next.js에서 `return { props: { dehydratedState: dehydrate(queryClient) } }` 또는 Remix에서 `return json({ dehydratedState: dehydrate(queryClient) })`를 호출하면, 프레임워크가 `queryClient`의 `dehydratedState` 표현을 직렬화하여 마크업에 포함하고 클라이언트로 전달합니다.

기본적으로 이러한 프레임워크는 안전하게 직렬화/파싱할 수 있는 값만 반환하도록 지원하므로 `undefined`, `Error`, `Date`, `Map`, `Set`, `BigInt`, `Infinity`, `NaN`, `-0`, 정규식 등을 지원하지 않습니다. 따라서 쿼리에서 이러한 값을 반환할 수도 없습니다. 이런 값을 반환하고 싶다면 [superjson](https://github.com/blitz-js/superjson) 같은 패키지를 살펴보세요.

맞춤형 SSR 설정을 사용하고 있다면 이 단계를 직접 처리해야 합니다. 처음 떠오르는 방법이 `JSON.stringify(dehydratedState)`일 수 있지만, 기본적으로 `<script>alert('Oh no..')</script>` 같은 내용을 이스케이프하지 않기 때문에 애플리케이션에 **XSS 취약성**을 쉽게 초래할 수 있습니다. [superjson](https://github.com/blitz-js/superjson) 역시 값을 이스케이프하지 않으므로 추가적인 이스케이프 단계를 넣지 않는 이상 맞춤형 SSR 환경에서 단독으로 사용하기에 안전하지 않습니다. 대신 [Serialize JavaScript](https://github.com/yahoo/serialize-javascript)나 [devalue](https://github.com/Rich-Harris/devalue)처럼 기본적으로 XSS 주입에 안전한 라이브러리를 사용할 것을 권장합니다.

## 요청 폭포수에 관한 메모

[Performance & Request Waterfalls 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/request-waterfalls.md)에서 서버 렌더링이 복잡한 중첩 폭포수 중 하나를 어떻게 바꾸는지 다시 살펴보겠다고 언급했습니다. [특정 코드 예시](https://tanstack.com/query/latest/docs/framework/react/guides/request-waterfalls#code-splitting)를 확인해 보세요. 리마인드 차원에서, 우리는 `<Feed>` 컴포넌트 내부에 `<GraphFeedItem>` 컴포넌트를 코드 스플릿해 두었습니다. 피드에 그래프 아이템이 포함되어 있을 때만 렌더링되고, 두 컴포넌트는 각각 자신의 데이터를 가져옵니다. 클라이언트 렌더링에서는 다음과 같은 요청 폭포수가 발생합니다:

```
1. |> Markup (without content)
2.   |> JS for <Feed>
3.     |> getFeed()
4.       |> JS for <GraphFeedItem>
5.         |> getGraphDataById()
```

서버 렌더링의 좋은 점은 위 과정을 다음과 같이 바꿀 수 있다는 것입니다:

```
1. |> Markup (with content AND initial data)
2.   |> JS for <Feed>
2.   |> JS for <GraphFeedItem>
```

이제 쿼리가 클라이언트에서 더 이상 가져와지지 않고, 해당 데이터가 마크업에 포함되었다는 점에 주목하세요. `<GraphFeedItem>`이 서버에서 렌더링되었기 때문에 클라이언트에서도 이 JS가 필요하다는 것을 알 수 있고, 이 청크에 대한 스크립트 태그를 마크업에 삽입할 수 있으므로 JS를 병렬로 로드할 수 있습니다. 서버에서는 여전히 다음과 같은 요청 폭포수가 있습니다:

```
1. |> getFeed()
2.   |> getGraphDataById()
```

피드를 가져오기 전에 그래프 데이터 역시 필요한지 알 수 없기 때문에 두 쿼리는 서로 의존적입니다. 하지만 이 작업은 일반적으로 지연 시간이 더 낮고 안정적인 서버에서 일어나므로 크게 문제가 되지 않는 경우가 많습니다.

훌륭하죠, 대부분의 폭포수를 평탄화했습니다! 하지만 함정이 있습니다. 이 페이지를 `/feed` 페이지라고 부르고, `/posts` 같은 다른 페이지도 있다고 가정해 봅시다. 주소창에 `www.example.com/feed`를 직접 입력하고 엔터를 누르면 서버 렌더링의 모든 이점을 누릴 수 있습니다. 그러나 `www.example.com/posts`를 입력한 다음 `/feed` 링크를 **클릭**하면 다시 다음 상황으로 돌아갑니다:

```
1. |> JS for <Feed>
2.   |> getFeed()
3.     |> JS for <GraphFeedItem>
4.       |> getGraphDataById()
```

SPA에서는 서버 렌더링이 초기 페이지 로드에만 작동하고, 그 이후 내비게이션에는 적용되지 않기 때문입니다.

현대적인 프레임워크는 초기 코드와 데이터를 병렬로 가져와 이 문제를 해결하려고 합니다. 예를 들어 이 가이드에서 설명한 사전 가져오기 패턴(종속 쿼리를 사전 가져오는 방법 포함)을 적용한 Next.js나 Remix를 사용한다면 실제로는 다음과 같을 것입니다:

```
1. |> JS for <Feed>
1. |> getFeed() + getGraphDataById()
2.   |> JS for <GraphFeedItem>
```

이 방식이 훨씬 좋지만, 이를 더욱 개선하려면 서버 컴포넌트로 단일 왕복으로 평탄화할 수 있습니다. 자세한 내용은 [고급 서버 렌더링 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr.md)에서 확인하세요.

## 팁, 트릭, 주의사항

### 서버에서 쿼리가 가져온 시점을 기준으로 신선도를 측정합니다

쿼리는 `dataUpdatedAt`이 언제였는지에 따라 신선한지 여부가 결정됩니다. 여기서 주의할 점은 서버 시간이 정확해야 한다는 것이지만, UTC 시간이 사용되므로 시간대는 고려하지 않아도 됩니다.

`staleTime`의 기본값이 `0`이므로, 페이지 로드 시 백그라운드에서 쿼리가 기본적으로 다시 가져와집니다. 마크업을 캐시하지 않는다면 특히, 이중 페칭을 피하기 위해 더 높은 `staleTime`을 사용하는 것이 좋을 수 있습니다.

이러한 오래된 쿼리의 재페칭은 CDN에 마크업을 캐시할 때 완벽하게 어울립니다! 페이지 자체의 캐시 시간을 충분히 길게 설정해 서버에서 페이지를 다시 렌더링할 필요를 줄이면서도, 쿼리의 `staleTime`을 더 낮게 설정해 사용자가 페이지에 방문하는 즉시 백그라운드에서 데이터를 다시 가져올 수 있게 할 수 있습니다. 예를 들어 페이지를 일주일 동안 캐시하되, 데이터가 하루 이상 오래되었으면 페이지 로드시 자동으로 다시 가져오도록 설정할 수 있습니다.

### 서버에서 높은 메모리 사용량

요청마다 `QueryClient`를 생성하는 경우 React Query는 이 클라이언트에 대해 고립된 캐시를 생성하며, 이는 `gcTime` 기간 동안 메모리에 유지됩니다. 이 기간 동안 요청 수가 많다면 서버에서 높은 메모리 사용량으로 이어질 수 있습니다.

서버에서 `gcTime`의 기본값은 `Infinity`이므로 수동 가비지 컬렉션이 비활성화되고, 요청이 끝나면 자동으로 메모리가 해제됩니다. 명시적으로 `Infinity`가 아닌 `gcTime`을 설정했다면 캐시를 일찍 비우는 책임이 여러분에게 있습니다.

`gcTime`을 `0`으로 설정하는 것은 피하세요. [Hydration Boundary](https://tanstack.com/query/latest/docs/framework/react/reference/hydration.md#hydrationboundary)가 렌더링을 위해 필요한 데이터를 캐시에 넣지만, 렌더링이 완료되기 전에 가비지 컬렉터가 데이터를 제거하면 하이드레이션 오류가 발생할 수 있기 때문입니다. 더 짧은 `gcTime`이 필요한 경우 `2 * 1000`으로 설정해 애플리케이션이 데이터를 참조할 수 있는 충분한 시간을 확보하는 것을 권장합니다.

요청 처리가 완료되고 탈수된 상태를 클라이언트로 보낸 후 캐시가 더 이상 필요하지 않을 때 메모리 사용량을 줄이려면 [`queryClient.clear()`](https://tanstack.com/query/latest/docs/reference/QueryClient.md#queryclientclear) 호출을 추가할 수 있습니다.

또는 더 작은 `gcTime`을 설정할 수도 있습니다.

### Next.js 리라이트에 대한 주의사항

[Next.js의 리라이트 기능](https://nextjs.org/docs/app/api-reference/next-config-js/rewrites)을 [Automatic Static Optimization](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization) 또는 `getStaticProps`와 함께 사용한다면 주의해야 할 점이 있습니다. React Query에 의한 두 번째 하이드레이션이 발생하기 때문입니다. 이는 [Next.js가 리라이트를 파싱](https://nextjs.org/docs/app/api-reference/next-config-js/rewrites#rewrite-parameters)하고, 하이드레이션 이후 클라이언트에서 파라미터를 수집해 `router.query`에 제공해야 하기 때문입니다.

그 결과, 모든 하이드레이션 데이터의 참조 동일성이 사라져 데이터가 컴포넌트의 props로 사용되거나 `useEffect`/`useMemo`의 의존성 배열로 사용되는 곳마다 트리거가 발생할 수 있습니다.

