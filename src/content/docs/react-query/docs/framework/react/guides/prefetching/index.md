---
title: '프리패칭 & 라우터 통합'
description: '특정 데이터가 필요할 것 같을 때, 프리패칭을 사용해 그 데이터를 미리 캐시에 채워두면 더 빠른 경험을 제공할 수 있습니다.'
---

# 프리패칭 & 라우터 통합

특정 데이터가 필요할 것 같을 때, 프리패칭을 사용해 그 데이터를 미리 캐시에 채워두면 더 빠른 경험을 제공할 수 있습니다.

프리패칭 패턴에는 몇 가지가 있습니다:

1. 이벤트 핸들러에서
2. 컴포넌트에서
3. 라우터 통합을 통해
4. 서버 렌더링 중(또 다른 형태의 라우터 통합)

이 가이드에서는 처음 세 가지를 살펴보고, 네 번째는 [서버 렌더링 & 하이드레이션 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/ssr.md)와 [고급 서버 렌더링 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr.md)에서 자세히 다룹니다.

프리패칭의 구체적인 용례 중 하나는 Request Waterfall을 피하는 것입니다. 이에 대한 배경과 설명은 [Performance & Request Waterfalls 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/request-waterfalls.md)를 참고하세요.

## prefetchQuery & prefetchInfiniteQuery

여러 프리패칭 패턴을 보기 전에 `prefetchQuery`와 `prefetchInfiniteQuery` 함수부터 살펴보겠습니다. 기본 사항은 다음과 같습니다:

- 기본적으로 이 함수들은 `queryClient`에 설정된 기본 `staleTime`을 사용해 캐시에 있는 기존 데이터가 신선한지, 다시 가져와야 하는지를 판단합니다.
- `prefetchQuery({ queryKey: ['todos'], queryFn: fn, staleTime: 5000 })`처럼 특정 `staleTime`을 전달할 수도 있습니다.
  - 이 `staleTime`은 프리패칭에만 사용되므로, 각 `useQuery` 호출에도 별도로 설정해야 합니다.
  - `staleTime`을 무시하고 캐시에 데이터가 있으면 항상 반환하도록 하려면 `ensureQueryData` 함수를 사용할 수 있습니다.
  - 팁: 서버에서 프리패칭할 때는 해당 `queryClient`에 기본 `staleTime`을 `0`보다 크게 설정하면 매번 특정 `staleTime`을 넘길 필요가 없습니다.
- 프리패칭된 쿼리에 대해 `useQuery` 인스턴스가 하나도 나타나지 않으면, `gcTime`에 지정된 시간이 지나면 삭제되고 가비지 컬렉션됩니다.
- 이 함수들은 `Promise<void>`를 반환하므로 쿼리 데이터를 반환하지 않습니다. 데이터가 필요하다면 `fetchQuery`/`fetchInfiniteQuery`를 사용하세요.
- 프리패칭 함수는 오류를 던지지 않습니다. 일반적으로 `useQuery`에서 다시 가져오려 하기 때문에 우아한 폴백이 됩니다. 오류를 잡아야 한다면 `fetchQuery`/`fetchInfiniteQuery`를 사용하세요.

다음은 `prefetchQuery`를 사용하는 방법입니다:

[//]: # 'ExamplePrefetchQuery'

```tsx
const prefetchTodos = async () => {
  // The results of this query will be cached like a normal query
  await queryClient.prefetchQuery({
    queryKey: ['todos'],
    queryFn: fetchTodos,
  })
}
```

[//]: # 'ExamplePrefetchQuery'

Infinite Query도 일반 Query처럼 프리패치할 수 있습니다. 기본적으로 쿼리의 첫 페이지만 프리패치되어 주어진 QueryKey 아래 저장됩니다. 여러 페이지를 프리패치하려면 `pages` 옵션을 사용해야 하며, 이때 `getNextPageParam` 함수도 제공해야 합니다:

[//]: # 'ExamplePrefetchInfiniteQuery'

```tsx
const prefetchProjects = async () => {
  // The results of this query will be cached like a normal query
  await queryClient.prefetchInfiniteQuery({
    queryKey: ['projects'],
    queryFn: fetchProjects,
    initialPageParam: 0,
    getNextPageParam: (lastPage, pages) => lastPage.nextCursor,
    pages: 3, // prefetch the first 3 pages
  })
}
```

[//]: # 'ExamplePrefetchInfiniteQuery'

이제 이러한 함수와 다른 방법을 다양한 상황에서 어떻게 사용할 수 있는지 살펴봅시다.

## 이벤트 핸들러에서 프리패치하기

가장 직관적인 프리패칭 형태는 사용자가 무언가와 상호작용할 때 실행하는 것입니다. 이 예제에서는 `queryClient.prefetchQuery`를 사용해 `onMouseEnter` 또는 `onFocus`에서 프리패칭을 시작합니다.

[//]: # 'ExampleEventHandler'

```tsx
function ShowDetailsButton() {
  const queryClient = useQueryClient()

  const prefetch = () => {
    queryClient.prefetchQuery({
      queryKey: ['details'],
      queryFn: getDetailsData,
      // Prefetch only fires when data is older than the staleTime,
      // so in a case like this you definitely want to set one
      staleTime: 60000,
    })
  }

  return (
    <button onMouseEnter={prefetch} onFocus={prefetch} onClick={...}>
      Show Details
    </button>
  )
}
```

[//]: # 'ExampleEventHandler'

## 컴포넌트에서 프리패치하기

컴포넌트 라이프사이클 중 프리패칭은 어떤 자식이나 하위 컴포넌트가 특정 데이터를 필요로 한다는 것을 알고 있지만, 다른 쿼리가 로딩을 마칠 때까지 렌더링할 수 없는 상황에서 유용합니다. 이를 설명하기 위해 Request Waterfall 가이드의 예제를 가져오겠습니다:

[//]: # 'ExampleComponent'

```tsx
function Article({ id }) {
  const { data: articleData, isPending } = useQuery({
    queryKey: ['article', id],
    queryFn: getArticleById,
  })

  if (isPending) {
    return 'Loading article...'
  }

  return (
    <>
      <ArticleHeader articleData={articleData} />
      <ArticleBody articleData={articleData} />
      <Comments id={id} />
    </>
  )
}

function Comments({ id }) {
  const { data, isPending } = useQuery({
    queryKey: ['article-comments', id],
    queryFn: getArticleCommentsById,
  })

  ...
}
```

[//]: # 'ExampleComponent'

이렇게 하면 다음과 같은 요청 워터폴이 발생합니다:

```
1. |> getArticleById()
2.   |> getArticleCommentsById()
```

그 가이드에서 언급했듯이, 이 워터폴을 평탄화하고 성능을 개선하는 한 가지 방법은 `getArticleCommentsById` 쿼리를 부모로 끌어올려 결과를 prop으로 전달하는 것입니다. 그러나 컴포넌트가 관련이 없거나 사이에 여러 단계가 있는 경우처럼 실행하기 어렵거나 바람직하지 않을 수 있습니다.

그럴 때는 대신 부모에서 쿼리를 프리패치할 수 있습니다. 가장 간단한 방법은 쿼리를 사용하되 결과를 무시하는 것입니다:

[//]: # 'ExampleParentComponent'

```tsx
function Article({ id }) {
  const { data: articleData, isPending } = useQuery({
    queryKey: ['article', id],
    queryFn: getArticleById,
  })

  // Prefetch
  useQuery({
    queryKey: ['article-comments', id],
    queryFn: getArticleCommentsById,
    // Optional optimization to avoid rerenders when this query changes:
    notifyOnChangeProps: [],
  })

  if (isPending) {
    return 'Loading article...'
  }

  return (
    <>
      <ArticleHeader articleData={articleData} />
      <ArticleBody articleData={articleData} />
      <Comments id={id} />
    </>
  )
}

function Comments({ id }) {
  const { data, isPending } = useQuery({
    queryKey: ['article-comments', id],
    queryFn: getArticleCommentsById,
  })

  ...
}
```

[//]: # 'ExampleParentComponent'

이렇게 하면 `'article-comments'`가 즉시 가져와져 워터폴을 평탄화합니다:

```
1. |> getArticleById()
1. |> getArticleCommentsById()
```

[//]: # 'Suspense'

Suspense와 함께 프리패칭하려면 약간 다르게 해야 합니다. `useSuspenseQueries`를 프리패칭에 사용할 수 없습니다. 프리패칭이 컴포넌트 렌더링을 막아버리기 때문입니다. 또 `useQuery`를 프리패칭에 사용할 수도 없습니다. Suspense 쿼리가 해결된 후에야 프리패칭이 시작되기 때문입니다. 이 시나리오에서는 라이브러리에서 제공하는 [`usePrefetchQuery`](https://tanstack.com/query/latest/docs/framework/react/reference/usePrefetchQuery.md) 또는 [`usePrefetchInfiniteQuery`](https://tanstack.com/query/latest/docs/framework/react/reference/usePrefetchInfiniteQuery.md) 훅을 사용할 수 있습니다.

데이터가 실제로 필요한 컴포넌트에서는 `useSuspenseQuery`를 사용할 수 있습니다. 나중에 이 컴포넌트를 별도의 `<Suspense>` 경계로 감싸서, 우리가 프리패치하는 "보조" 쿼리가 "주요" 데이터 렌더링을 막지 않도록 하는 것이 좋을 수도 있습니다.

```tsx
function ArticleLayout({ id }) {
  usePrefetchQuery({
    queryKey: ['article-comments', id],
    queryFn: getArticleCommentsById,
  })

  return (
    <Suspense fallback="Loading article">
      <Article id={id} />
    </Suspense>
  )
}

function Article({ id }) {
  const { data: articleData, isPending } = useSuspenseQuery({
    queryKey: ['article', id],
    queryFn: getArticleById,
  })

  ...
}
```

또 다른 방법은 쿼리 함수 내부에서 프리패칭하는 것입니다. 기사 데이터를 가져올 때마다 댓글도 필요할 가능성이 크다면 합리적입니다. 이를 위해 `queryClient.prefetchQuery`를 사용합니다:

```tsx
const queryClient = useQueryClient()
const { data: articleData, isPending } = useQuery({
  queryKey: ['article', id],
  queryFn: (...args) => {
    queryClient.prefetchQuery({
      queryKey: ['article-comments', id],
      queryFn: getArticleCommentsById,
    })

    return getArticleById(...args)
  },
})
```

이펙트에서 프리패칭하는 것도 가능하지만, 같은 컴포넌트에서 `useSuspenseQuery`를 사용 중이라면 이 이펙트는 쿼리가 끝난 뒤에야 실행된다는 점을 주의하세요. 이는 원하지 않는 동작일 수 있습니다.

```tsx
const queryClient = useQueryClient()

useEffect(() => {
  queryClient.prefetchQuery({
    queryKey: ['article-comments', id],
    queryFn: getArticleCommentsById,
  })
}, [queryClient, id])
```

정리하자면, 컴포넌트 라이프사이클 중 쿼리를 프리패치하려면 상황에 맞게 다음 중 하나를 선택하세요:

- `usePrefetchQuery` 또는 `usePrefetchInfiniteQuery` 훅을 사용해 서스펜스 경계 전에 프리패치
- `useQuery` 또는 `useSuspenseQueries`를 사용하고 결과를 무시
- 쿼리 함수 내부에서 프리패치
- 이펙트에서 프리패치

이제 조금 더 고급 사례를 살펴봅시다.

[//]: # 'Suspense'

### 의존 쿼리 & 코드 스플리팅

때로는 다른 fetch 결과에 따라 조건부로 프리패칭하고 싶을 때가 있습니다. [Performance & Request Waterfalls 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/request-waterfalls.md)에서 가져온 다음 예제를 보세요:

[//]: # 'ExampleConditionally1'

```tsx
// This lazy loads the GraphFeedItem component, meaning
// it wont start loading until something renders it
const GraphFeedItem = React.lazy(() => import('./GraphFeedItem'))

function Feed() {
  const { data, isPending } = useQuery({
    queryKey: ['feed'],
    queryFn: getFeed,
  })

  if (isPending) {
    return 'Loading feed...'
  }

  return (
    <>
      {data.map((feedItem) => {
        if (feedItem.type === 'GRAPH') {
          return <GraphFeedItem key={feedItem.id} feedItem={feedItem} />
        }

        return <StandardFeedItem key={feedItem.id} feedItem={feedItem} />
      })}
    </>
  )
}

// GraphFeedItem.tsx
function GraphFeedItem({ feedItem }) {
  const { data, isPending } = useQuery({
    queryKey: ['graph', feedItem.id],
    queryFn: getGraphDataById,
  })

  ...
}
```

[//]: # 'ExampleConditionally1'

해당 가이드에서 언급했듯이 이 예제는 다음과 같은 이중 요청 워터폴을 유발합니다:

```
1. |> getFeed()
2.   |> JS for <GraphFeedItem>
3.     |> getGraphDataById()
```

API 구조를 바꿔 `getFeed()`가 필요한 경우 `getGraphDataById()` 데이터를 함께 반환하도록 하지 못한다면, `getFeed->getGraphDataById` 워터폴을 제거할 방법은 없습니다. 하지만 조건부 프리패칭을 활용해 코드와 데이터를 병렬로 로드할 수는 있습니다. 앞서 설명했듯 여러 방식이 있지만, 이번에는 쿼리 함수에서 수행해 보겠습니다:

[//]: # 'ExampleConditionally2'

```tsx
function Feed() {
  const queryClient = useQueryClient()
  const { data, isPending } = useQuery({
    queryKey: ['feed'],
    queryFn: async (...args) => {
      const feed = await getFeed(...args)

      for (const feedItem of feed) {
        if (feedItem.type === 'GRAPH') {
          queryClient.prefetchQuery({
            queryKey: ['graph', feedItem.id],
            queryFn: getGraphDataById,
          })
        }
      }

      return feed
    }
  })

  ...
}
```

[//]: # 'ExampleConditionally2'

이렇게 하면 코드와 데이터를 병렬로 로드할 수 있습니다:

```
1. |> getFeed()
2.   |> JS for <GraphFeedItem>
2.   |> getGraphDataById()
```

하지만 트레이드오프가 있습니다. `getGraphDataById` 코드가 이제 `JS for <GraphFeedItem>` 대신 부모 번들에 포함됩니다. 따라서 상황에 따라 어떤 성능 트레이드오프가 최선인지 판단해야 합니다. `GraphFeedItem`이 자주 나타난다면 부모에 코드를 포함하는 것이 아마 가치가 있을 것입니다. 매우 드물다면 그렇지 않을 수 있습니다.

[//]: # 'Router'

## 라우터 통합

컴포넌트 트리에서 데이터 페칭을 수행하면 Request Waterfall이 쉽게 발생할 수 있고, 이를 해결하기 위한 다양한 방법은 애플리케이션 전체에 누적되면서 번거로울 수 있습니다. 이런 경우 프리패칭을 라우터 단계에 통합하는 방식이 매력적입니다.

이 접근 방식에서는 각 _라우트_가 해당 컴포넌트 트리에 필요한 데이터를 미리 선언합니다. 서버 렌더링은 렌더링 시작 전에 모든 데이터가 로드되어야 했기 때문에, SSR 앱에서는 전통적으로 이 접근 방식이 지배적이었습니다. 지금도 흔히 사용되며, 자세한 내용은 [서버 렌더링 & 하이드레이션 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/ssr.md)에서 확인할 수 있습니다.

여기서는 클라이언트 측 사례에 집중해 [TanStack Router](https://tanstack.com/router)와 함께 사용하는 예제를 살펴보겠습니다. 예제는 간결함을 위해 많은 설정과 보일러플레이트를 생략했으며, 전체 React Query 예제는 [TanStack Router 문서](https://tanstack.com/router/latest/docs)의 [full React Query example](https://tanstack.com/router/latest/docs/framework/react/examples/basic-react-query-file-based)에서 확인할 수 있습니다.

라우터 단계에서 통합할 때는 모든 데이터가 준비될 때까지 해당 라우트의 렌더링을 _차단_하거나, 결과를 기다리지 않고 프리패칭만 시작할 수 있습니다. 이렇게 하면 가능한 한 빨리 라우트 렌더링을 시작할 수 있습니다. 두 접근 방식을 혼합해 일부 중요한 데이터만 기다리고, 나머지 보조 데이터는 로딩이 끝나기 전에 렌더링을 시작할 수도 있습니다. 이 예제에서는 `/article` 라우트를 설정해 기사 데이터가 모두 로드될 때까지 렌더링을 차단하고, 댓글은 가능한 빨리 프리패칭하되 댓글 로딩이 끝나지 않았더라도 라우트 렌더링을 막지 않도록 구성합니다.

```tsx
const queryClient = new QueryClient()
const routerContext = new RouterContext()
const rootRoute = routerContext.createRootRoute({
  component: () => { ... }
})

const articleRoute = new Route({
  getParentRoute: () => rootRoute,
  path: 'article',
  beforeLoad: () => {
    return {
      articleQueryOptions: { queryKey: ['article'], queryFn: fetchArticle },
      commentsQueryOptions: { queryKey: ['comments'], queryFn: fetchComments },
    }
  },
  loader: async ({
    context: { queryClient },
    routeContext: { articleQueryOptions, commentsQueryOptions },
  }) => {
    // Fetch comments asap, but don't block
    queryClient.prefetchQuery(commentsQueryOptions)

    // Don't render the route at all until article has been fetched
    await queryClient.prefetchQuery(articleQueryOptions)
  },
  component: ({ useRouteContext }) => {
    const { articleQueryOptions, commentsQueryOptions } = useRouteContext()
    const articleQuery = useQuery(articleQueryOptions)
    const commentsQuery = useQuery(commentsQueryOptions)

    return (
      ...
    )
  },
  errorComponent: () => 'Oh crap!',
})
```

다른 라우터와의 통합도 가능합니다. 다른 데모는 [react-router](https://tanstack.com/query/latest/docs/framework/react/examples/react-router)를 참고하세요.

[//]: # 'Router'

## 쿼리를 수동으로 준비하기

이미 쿼리에 필요한 데이터를 동기적으로 보유하고 있다면 프리패칭할 필요가 없습니다. [Query Client의 `setQueryData` 메서드](https://tanstack.com/query/latest/docs/reference/QueryClient.md#queryclientsetquerydata)를 사용해 쿼리의 캐시 결과를 키로 직접 추가하거나 업데이트할 수 있습니다.

[//]: # 'ExampleManualPriming'

```tsx
queryClient.setQueryData(['todos'], todos)
```

[//]: # 'ExampleManualPriming'
[//]: # 'Materials'

## 추가 읽을거리

쿼리 캐시에 데이터를 실제 fetch 전에 넣는 방법을 심층적으로 알아보려면 [TkDodo의 Seeding the Query Cache 글](https://tkdodo.eu/blog/seeding-the-query-cache)을 참고하세요.

서버 측 라우터 및 프레임워크와 통합하는 방법은 방금 본 내용과 매우 유사하지만, 데이터를 서버에서 클라이언트로 전달해 캐시에 하이드레이션해야 한다는 점이 추가됩니다. 그 방법을 배우려면 [서버 렌더링 & 하이드레이션 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/ssr.md)를 이어서 읽어보세요.

[//]: # 'Materials'

