---
title: '성능 & 요청 폭포'
description: '애플리케이션 성능은 넓고 복잡한 주제이며, React Query 자체가 API를 더 빠르게 만들 수는 없지만 최상의 성능을 위해 React Query를 사용할 때 주의해야 할 사항들은 있습니다.'
---

# 성능 & 요청 폭포

애플리케이션 성능은 넓고 복잡한 주제이며, React Query 자체가 API를 더 빠르게 만들 수는 없지만 최상의 성능을 위해 React Query를 사용할 때 주의해야 할 사항들은 있습니다.

React Query 또는 컴포넌트 내부에서 데이터를 가져올 수 있게 해주는 모든 데이터 패칭 라이브러리를 사용할 때 가장 큰 성능 함정은 요청 폭포(request waterfall)입니다. 이 페이지의 나머지 부분에서는 그것이 무엇인지, 어떻게 감지할 수 있는지, 그리고 이를 피하기 위해 애플리케이션이나 API를 어떻게 재구성할 수 있는지를 설명합니다.

[Prefetching & Router Integration 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/prefetching.md)는 이를 기반으로, 애플리케이션이나 API를 재구성하기 어렵거나 불가능할 때 미리 데이터를 프리패치하는 방법을 다룹니다.

[Server Rendering & Hydration 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/ssr.md)는 서버에서 데이터를 프리패치하고 그 데이터를 클라이언트로 전달해 다시 가져올 필요가 없도록 하는 방법을 설명합니다.

[Advanced Server Rendering 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr.md)는 이러한 패턴을 서버 컴포넌트와 스트리밍 서버 렌더링에 적용하는 방법을 더 깊이 다룹니다.

## 요청 폭포란 무엇인가?

요청 폭포는 하나의 리소스(코드, CSS, 이미지, 데이터 등)에 대한 요청이 다른 리소스 요청이 완료된 _이후에야_ 시작하는 상황을 말합니다.

웹 페이지를 생각해 봅시다. CSS나 JS 등을 로드하기 전에 브라우저는 먼저 마크업을 로드해야 합니다. 이것이 요청 폭포입니다.

```
1. |-> Markup
2.   |-> CSS
2.   |-> JS
2.   |-> Image
```

CSS를 JS 파일 안에서 가져온다면 이제 이중 폭포가 됩니다.

```
1. |-> Markup
2.   |-> JS
3.     |-> CSS
```

그 CSS가 배경 이미지를 사용한다면 삼중 폭포가 됩니다.

```
1. |-> Markup
2.   |-> JS
3.     |-> CSS
4.       |-> Image
```

요청 폭포를 가장 잘 포착하고 분석하는 방법은 보통 브라우저 개발자 도구의 “Network” 탭을 여는 것입니다.

각 폭포는 최소 한 번의 서버 왕복을 의미하며, 리소스가 로컬에 캐시되어 있지 않은 이상 그렇습니다(실제로는 브라우저가 연결을 설정하기 위해 추가적인 핑퐁이 필요할 수 있으니 더 많은 왕복이 있을 수 있지만 여기서는 무시하겠습니다). 이 때문에 요청 폭포의 부정적인 영향은 사용자 지연(latency)에 크게 좌우됩니다. 삼중 폭포 예시를 생각해 봅시다. 이는 실제로 4번의 서버 왕복을 의미합니다. 250ms 지연(3G 네트워크나 열악한 네트워크 환경에서 흔함)을 가정하면, **지연 시간만** 따졌을 때 총 4\*250=1000ms가 됩니다. 이를 2번의 왕복만 필요한 첫 번째 예시처럼 평평하게 만들 수 있다면 500ms가 되어, 배경 이미지를 로드하는 시간을 절반으로 줄일 수도 있습니다!

## 요청 폭포 & React Query

이제 React Query를 생각해 봅시다. 우선 서버 렌더링이 없는 경우를 살펴보겠습니다. 쿼리를 실행하기 전에 JS를 로드해야 하므로, 데이터를 화면에 표시하기 전부터 이미 이중 폭포가 존재합니다.

```
1. |-> Markup
2.   |-> JS
3.     |-> Query
```

이를 바탕으로 React Query에서 요청 폭포를 야기할 수 있는 몇 가지 패턴과 이를 피하는 방법을 살펴보겠습니다.

- 단일 컴포넌트 폭포 / 직렬 쿼리
- 중첩 컴포넌트 폭포
- 코드 스플리팅

### 단일 컴포넌트 폭포 / 직렬 쿼리

하나의 컴포넌트가 먼저 한 쿼리를 가져오고, 그다음 다른 쿼리를 가져오면 요청 폭포가 발생합니다. 두 번째 쿼리가 첫 번째 쿼리의 데이터를 필요로 하는 [종속 쿼리](https://tanstack.com/query/latest/docs/framework/react/guides/dependent-queries.md)일 때 이런 일이 발생합니다.

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

항상 가능한 것은 아니지만, 최적의 성능을 위해 API를 재구성해 두 쿼리를 하나로 가져올 수 있다면 가장 좋습니다. 위 예시에서 `getProjectsByUser`를 호출하기 위해 먼저 `getUserByEmail`을 가져오는 대신, 새로운 `getProjectsByUserEmail` 쿼리를 도입하면 폭포를 평탄화할 수 있습니다.

> API를 재구성하지 않고 종속 쿼리를 완화하는 또 다른 방법은 지연이 더 낮은 서버로 폭포를 옮기는 것입니다. 이는 [Advanced Server Rendering 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr.md)에서 다루는 서버 컴포넌트의 핵심 아이디어입니다.

직렬 쿼리의 또 다른 예시는 React Query를 Suspense와 함께 사용할 때입니다.

```tsx
function App () {
  // The following queries will execute in serial, causing separate roundtrips to the server:
  const usersQuery = useSuspenseQuery({ queryKey: ['users'], queryFn: fetchUsers })
  const teamsQuery = useSuspenseQuery({ queryKey: ['teams'], queryFn: fetchTeams })
  const projectsQuery = useSuspenseQuery({ queryKey: ['projects'], queryFn: fetchProjects })

  // Note that since the queries above suspend rendering, no data
  // gets rendered until all of the queries finished
  ...
}
```

일반 `useQuery`에서는 이 쿼리들이 병렬로 발생한다는 점에 주의하세요.

다행히도 이는 간단히 해결할 수 있습니다. 컴포넌트에 여러 개의 서스펜스 쿼리가 있을 때는 항상 `useSuspenseQueries` 훅을 사용하면 됩니다.

```tsx
const [usersQuery, teamsQuery, projectsQuery] = useSuspenseQueries({
  queries: [
    { queryKey: ['users'], queryFn: fetchUsers },
    { queryKey: ['teams'], queryFn: fetchTeams },
    { queryKey: ['projects'], queryFn: fetchProjects },
  ],
})
```

### 중첩 컴포넌트 폭포

중첩 컴포넌트 폭포는 부모와 자식 컴포넌트 모두가 쿼리를 포함하고, 부모가 자신의 쿼리가 끝날 때까지 자식을 렌더링하지 않을 때 발생합니다. 이는 `useQuery`와 `useSuspenseQuery` 모두에서 일어날 수 있습니다.

자식이 부모의 데이터를 기반으로 조건부 렌더링을 하거나, 자식이 쿼리를 위해 부모 결과의 일부를 props로 전달받아야 한다면, _종속_ 중첩 컴포넌트 폭포입니다.

먼저 자식이 부모에 **의존하지 않는** 예시를 살펴봅시다.

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

`<Comments>`가 부모로부터 `id` props를 받지만, 그 id는 `<Article>`이 렌더링될 때 이미 사용 가능하므로 기사와 댓글을 동시에 가져오지 못할 이유가 없습니다. 실제 애플리케이션에서는 자식이 훨씬 깊게 중첩될 수 있어 이와 같은 폭포를 발견하고 해결하기가 더 까다롭지만, 예시에서는 댓글 쿼리를 부모로 끌어올려 폭포를 평탄화할 수 있습니다.

```tsx
function Article({ id }) {
  const { data: articleData, isPending: articlePending } = useQuery({
    queryKey: ['article', id],
    queryFn: getArticleById,
  })

  const { data: commentsData, isPending: commentsPending } = useQuery({
    queryKey: ['article-comments', id],
    queryFn: getArticleCommentsById,
  })

  if (articlePending) {
    return 'Loading article...'
  }

  return (
    <>
      <ArticleHeader articleData={articleData} />
      <ArticleBody articleData={articleData} />
      {commentsPending ? (
        'Loading comments...'
      ) : (
        <Comments commentsData={commentsData} />
      )}
    </>
  )
}
```

이제 두 쿼리는 병렬로 실행됩니다. Suspense를 사용 중이라면 이 두 쿼리를 하나의 `useSuspenseQueries`로 결합하는 것이 좋습니다.

또 다른 방법은 `<Article>` 컴포넌트에서 댓글을 프리패치하거나, 라우터 수준에서 페이지 로드/네비게이션 시 두 쿼리를 프리패치하는 것입니다. 자세한 내용은 [Prefetching & Router Integration 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/prefetching.md)를 참고하세요.

다음으로 _종속 중첩 컴포넌트 폭포_ 예시를 봅시다.

```tsx
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

function GraphFeedItem({ feedItem }) {
  const { data, isPending } = useQuery({
    queryKey: ['graph', feedItem.id],
    queryFn: getGraphDataById,
  })

  ...
}
```

두 번째 쿼리 `getGraphDataById`는 두 가지 방식으로 부모에 의존합니다. 첫째, `feedItem`이 그래프일 때만 실행되며, 둘째, 부모로부터 `id`가 필요합니다.

```
1. |> getFeed()
2.   |> getGraphDataById()
```

이 예시에서는 단순히 쿼리를 부모로 끌어올리거나 프리패치를 추가하는 것만으로 폭포를 쉽게 평탄화할 수 없습니다. 가이드의 앞부분에서 다룬 종속 쿼리 예시처럼, 한 가지 선택지는 `getFeed` 쿼리에 그래프 데이터를 포함하도록 API를 리팩터링하는 것입니다. 더 고급 해결책은 서버 컴포넌트를 사용해 폭포를 지연이 낮은 서버로 옮기는 것이지만([Advanced Server Rendering 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr.md) 참고), 이는 매우 큰 아키텍처적 변화일 수 있다는 점을 유념하세요.

여기저기 몇 개의 쿼리 폭포가 있어도 좋은 성능을 낼 수 있지만, 요청 폭포는 흔한 성능 문제이므로 항상 주의를 기울여야 합니다. 특히 코드 스플리팅과 결합될 때 교묘하게 나타나는 버전을 다음에서 살펴보겠습니다.

### 코드 스플리팅

애플리케이션의 JS 코드를 작은 청크로 나누고 필요한 부분만 로드하는 것은 좋은 성능을 위한 핵심 단계입니다. 그러나 종종 요청 폭포를 유발한다는 단점이 있습니다. 그 코드 스플릿된 청크에 쿼리가 포함되어 있다면 문제는 더 심각해집니다.

약간 수정한 Feed 예시를 살펴봅시다.

[//]: # 'LazyExample'

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

[//]: # 'LazyExample'

이 예시는 다음과 같은 이중 폭포를 갖습니다.

```
1. |> getFeed()
2.   |> JS for <GraphFeedItem>
3.     |> getGraphDataById()
```

하지만 이는 예시 코드만 봤을 때이고, 실제로 이 페이지를 처음 로드할 때는 그래프를 렌더링하기 전에 서버로 5번 왕복해야 합니다!

```
1. |> Markup
2.   |> JS for <Feed>
3.     |> getFeed()
4.       |> JS for <GraphFeedItem>
5.         |> getGraphDataById()
```

서버 렌더링 시에는 양상이 조금 다르며, 이는 [Server Rendering & Hydration 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/ssr.md)에서 더 자세히 다룹니다. 또한 `<Feed>`를 포함하는 라우트 자체가 코드 스플릿되는 경우도 흔하므로 또 하나의 홉이 추가될 수 있습니다.

코드 스플리팅 상황에서는 `getGraphDataById` 쿼리를 `<Feed>` 컴포넌트로 끌어올려 조건부로 실행하거나, 조건부 프리패치를 추가하는 것이 도움이 될 수 있습니다. 그러면 해당 쿼리를 코드와 병렬로 가져올 수 있어 예시는 다음과 같이 바뀝니다.

```
1. |> getFeed()
2.   |> getGraphDataById()
2.   |> JS for <GraphFeedItem>
```

이것은 분명한 트레이드오프입니다. 이제 `getGraphDataById`의 데이터 패칭 코드가 `<Feed>`와 같은 번들에 포함되므로, 어떤 선택이 더 나은지 평가해야 합니다. 자세한 방법은 [Prefetching & Router Integration 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/prefetching.md)에서 확인하세요.

> 다음 두 선택지 사이의 트레이드오프:
>
> - 거의 사용하지 않더라도 모든 데이터 패칭 코드를 메인 번들에 포함
> - 데이터 패칭 코드를 코드 스플릿 번들에 넣되 요청 폭포를 감수
>
> 는 그다지 좋지 않으며, 이것이 서버 컴포넌트가 탄생한 동기 중 하나였습니다. 서버 컴포넌트를 사용하면 두 문제를 모두 피할 수 있으며, 이것이 React Query에 어떻게 적용되는지 더 알고 싶다면 [Advanced Server Rendering 가이드](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr.md)를 참고하세요.

## 요약 및 시사점

요청 폭포는 매우 흔하고 복잡한 성능 문제이며 많은 트레이드오프가 있습니다. 애플리케이션에 우연히 도입하기 쉬운 몇 가지 사례는 다음과 같습니다.

- 부모에 이미 쿼리가 있는 줄 모르고 자식에 쿼리를 추가
- 자식에 이미 쿼리가 있는 줄 모르고 부모에 쿼리를 추가
- 쿼리가 있는 자손을 가진 컴포넌트를, 쿼리가 있는 조상을 가진 새로운 부모로 이동
- 기타 등등

이러한 우발적 복잡성 때문에 요청 폭포에 주의를 기울이고 애플리케이션을 정기적으로 확인하는 것이 좋습니다(네트워크 탭을 가끔씩 살펴보는 것이 한 방법입니다!). 좋은 성능을 위해 모든 폭포를 반드시 평탄화할 필요는 없지만, 영향이 큰 것들은 주시하세요.

다음 가이드에서는 [Prefetching & Router Integration](https://tanstack.com/query/latest/docs/framework/react/guides/prefetching.md)을 활용해 폭포를 평탄화하는 추가 방법을 살펴보겠습니다.

