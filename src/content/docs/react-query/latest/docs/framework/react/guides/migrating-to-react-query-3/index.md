---
title: 'React Query 3로 마이그레이션하기'
description: '이전 버전의 React Query는 훌륭했고 새로운 기능, 더 많은 매직, 전반적으로 더 나은 사용 경험을 가져왔습니다. 덕분에 많은 사용자가 채택했고 수많은 피드백(이슈/기여)이 쏟아져 라이브러리를 더욱 다듬어야 할 부분도 드러났습니다. v3는 이런 부분을 정밀하게 ...'
---

# React Query 3로 마이그레이션하기

이전 버전의 React Query는 훌륭했고 새로운 기능, 더 많은 매직, 전반적으로 더 나은 사용 경험을 가져왔습니다. 덕분에 많은 사용자가 채택했고 수많은 피드백(이슈/기여)이 쏟아져 라이브러리를 더욱 다듬어야 할 부분도 드러났습니다. v3는 이런 부분을 정밀하게 다듬은 버전입니다.

## 개요

- 더 확장 가능하고 테스트하기 쉬운 캐시 구성
- 향상된 SSR 지원
- 어디서든 데이터 지연(usePaginatedQuery였던 기능) 사용
- 양방향 Infinite Query
- 쿼리 데이터 셀렉터
- 사용 전에 쿼리/뮤테이션 기본값을 완전하게 구성
- 선택적 렌더링 최적화를 위한 더 세밀한 제어
- 새 `useQueries` 훅! (가변 길이 병렬 쿼리 실행)
- `useIsFetching()` 훅에 쿼리 필터 지원 추가
- 뮤테이션 재시도/오프라인/재생 지원
- React 바깥에서도 쿼리/뮤테이션 관찰
- React Query 코어 로직을 원하는 곳 어디서나 사용
- `react-query/devtools`를 통한 번들/공존 Devtools
- 웹 스토리지로 캐시 지속성 제공(`react-query/persistQueryClient-experimental`, `react-query/createWebStoragePersistor-experimental` 실험 기능)

## 호환성 깨짐 변경 사항

### `QueryCache`가 `QueryClient`, 하위 수준의 `QueryCache`, `MutationCache` 인스턴스로 분리되었습니다.

`QueryCache`는 모든 쿼리를, `MutationCache`는 모든 뮤테이션을 포함하며, `QueryClient`는 구성 설정과 상호작용을 담당합니다.

이로 인한 이점:

- 다양한 유형의 캐시를 허용
- 다른 구성을 가진 여러 클라이언트가 동일한 캐시 사용 가능
- SSR에서 공유 캐시에 활용할 수 있도록 클라이언트가 쿼리를 추적
- 클라이언트 API가 일반 사용에 더 집중
- 개별 컴포넌트를 테스트하기 쉬움

`new QueryClient()`를 만들면 직접 전달하지 않은 경우 `QueryCache`와 `MutationCache`가 자동 생성됩니다.

```tsx
import { QueryClient } from 'react-query'

const queryClient = new QueryClient()
```

### `ReactQueryConfigProvider`와 `ReactQueryCacheProvider`가 `QueryClientProvider`로 대체되었습니다.

쿼리와 뮤테이션의 기본 옵션은 이제 `QueryClient`에서 지정할 수 있습니다.

**이제 defaultConfig가 아니라 defaultOptions라는 점에 주의하세요.**

```tsx
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      // query options
    },
    mutations: {
      // mutation options
    },
  },
})
```

`QueryClientProvider` 컴포넌트가 애플리케이션에 `QueryClient`를 연결하는 데 사용됩니다.

```tsx
import { QueryClient, QueryClientProvider } from 'react-query'

const queryClient = new QueryClient()

function App() {
  return <QueryClientProvider client={queryClient}>...</QueryClientProvider>
}
```

### 기본 `QueryCache`는 완전히 제거되었습니다.

앞서 폐기 예정이라고 알렸듯이, 메인 패키지에서 생성되거나 내보내지는 기본 `QueryCache`가 더 이상 없습니다. **반드시 `new QueryClient()` 또는 `new QueryCache()`를 통해 직접 생성해야 합니다(`new QueryClient({ queryCache })`에 전달 가능).**

### 더 이상 사용되지 않던 `makeQueryCache` 유틸리티가 제거되었습니다.

정말 오래 기다렸지만 이제야 없어졌습니다 :)

### `QueryCache.prefetchQuery()`가 `QueryClient.prefetchQuery()`로 이동했습니다.

새 `QueryClient.prefetchQuery()` 함수는 async이지만 **쿼리 데이터는 반환하지 않습니다**. 데이터가 필요하면 새 `QueryClient.fetchQuery()` 함수를 사용하세요.

```tsx
// Prefetch a query:
await queryClient.prefetchQuery('posts', fetchPosts)

// Fetch a query:
try {
  const data = await queryClient.fetchQuery('posts', fetchPosts)
} catch (error) {
  // Error handling
}
```

### `ReactQueryErrorResetBoundary`와 `QueryCache.resetErrorBoundaries()`가 `QueryErrorResetBoundary`, `useQueryErrorResetBoundary()`로 대체되었습니다.

이 두 가지 조합으로 이전과 동일한 경험을 제공하면서도 어떤 컴포넌트 트리를 리셋할지 더 세밀하게 제어할 수 있습니다. 자세한 내용은 아래를 참조하세요.

- [QueryErrorResetBoundary](https://tanstack.com/query/latest/docs/framework/react/reference/QueryErrorResetBoundary.md)
- [useQueryErrorResetBoundary](https://tanstack.com/query/latest/docs/framework/react/reference/useQueryErrorResetBoundary.md)

### `QueryCache.getQuery()`가 `QueryCache.find()`로 대체되었습니다.

이제 캐시에서 개별 쿼리를 찾을 때는 `QueryCache.find()`를 사용하세요.

### `QueryCache.getQueries()`가 `QueryCache.findAll()`로 이동했습니다.

이제 여러 쿼리를 찾을 때는 `QueryCache.findAll()`을 사용하세요.

### `QueryCache.isFetching`이 `QueryClient.isFetching()`으로 이동했습니다.

**이제 프로퍼티가 아니라 함수라는 점에 주의하세요.**

### `useQueryCache` 훅이 `useQueryClient` 훅으로 대체되었습니다.

해당 컴포넌트 트리에 제공된 `queryClient`를 반환하며 이름만 바꿔주면 거의 그대로 사용할 수 있습니다.

### 쿼리 키의 각 부분이 더 이상 자동으로 쿼리 함수로 전달되지 않습니다.

이제 인라인 함수를 사용하는 방식이 매개변수를 쿼리 함수에 전달하는 권장 방식입니다.

```tsx
// Old
useQuery(['post', id], (_key, id) => fetchPost(id))

// New
useQuery(['post', id], () => fetchPost(id))
```

여전히 인라인 함수를 쓰고 싶지 않다면 새로 전달되는 `QueryFunctionContext`를 사용할 수 있습니다.

```tsx
useQuery(['post', id], (context) => fetchPost(context.queryKey[1]))
```

### Infinite Query 페이지 매개변수가 이제 `QueryFunctionContext.pageParam`을 통해 전달됩니다.

기존에는 쿼리 함수에서 마지막 쿼리 키 매개변수로 추가했지만 일부 패턴에는 어려움이 있었습니다.

```tsx
// Old
useInfiniteQuery(['posts'], (_key, pageParam = 0) => fetchPosts(pageParam))

// New
useInfiniteQuery(['posts'], ({ pageParam = 0 }) => fetchPosts(pageParam))
```

### usePaginatedQuery()가 `keepPreviousData` 옵션으로 대체되었습니다.

새 `keepPreviousData` 옵션은 `useQuery`, `useInfiniteQuery` 모두에서 사용할 수 있으며 동일한 “지연” 효과를 제공합니다.

```tsx
import { useQuery } from 'react-query'

function Page({ page }) {
  const { data } = useQuery(['page', page], fetchPage, {
    keepPreviousData: true,
  })
}
```

### useInfiniteQuery()가 이제 양방향입니다.

`useInfiniteQuery()` 인터페이스가 변경되어 양방향 무한 리스트를 완전히 지원합니다.

- `options.getFetchMore` → `options.getNextPageParam`
- `queryResult.canFetchMore` → `queryResult.hasNextPage`
- `queryResult.fetchMore` → `queryResult.fetchNextPage`
- `queryResult.isFetchingMore` → `queryResult.isFetchingNextPage`
- `options.getPreviousPageParam` 옵션 추가
- `queryResult.hasPreviousPage` 프로퍼티 추가
- `queryResult.fetchPreviousPage` 프로퍼티 추가
- `queryResult.isFetchingPreviousPage` 추가
- Infinite Query의 `data`는 `{ pages: [data, data, data], pageParams: [...] }` 형식의 객체가 됩니다.

한 방향:

```tsx
const { data, fetchNextPage, hasNextPage, isFetchingNextPage } =
  useInfiniteQuery(
    'projects',
    ({ pageParam = 0 }) => fetchProjects(pageParam),
    {
      getNextPageParam: (lastPage, pages) => lastPage.nextCursor,
    },
  )
```

양방향:

```tsx
const {
  data,
  fetchNextPage,
  fetchPreviousPage,
  hasNextPage,
  hasPreviousPage,
  isFetchingNextPage,
  isFetchingPreviousPage,
} = useInfiniteQuery(
  'projects',
  ({ pageParam = 0 }) => fetchProjects(pageParam),
  {
    getNextPageParam: (lastPage, pages) => lastPage.nextCursor,
    getPreviousPageParam: (firstPage, pages) => firstPage.prevCursor,
  },
)
```

한 방향 역순:

```tsx
const { data, fetchNextPage, hasNextPage, isFetchingNextPage } =
  useInfiniteQuery(
    'projects',
    ({ pageParam = 0 }) => fetchProjects(pageParam),
    {
      select: (data) => ({
        pages: [...data.pages].reverse(),
        pageParams: [...data.pageParams].reverse(),
      }),
      getNextPageParam: (lastPage, pages) => lastPage.nextCursor,
    },
  )
```

### Infinite Query 데이터에 이제 페이지 배열과 해당 페이지를 가져온 pageParams가 포함됩니다.

이를 통해 데이터와 pageParams를 더 쉽게 조작할 수 있습니다. 예: 첫 페이지와 그에 해당하는 params 제거.

```tsx
queryClient.setQueryData(['projects'], (data) => ({
  pages: data.pages.slice(1),
  pageParams: data.pageParams.slice(1),
}))
```

### useMutation은 이제 배열이 아닌 객체를 반환합니다.

예전 방식은 `useState`를 처음 발견했을 때 같은 기분을 줬지만 오래가지 못했습니다. 이제 뮤테이션 반환값은 단일 객체입니다.

```tsx
// Old:
const [mutate, { status, reset }] = useMutation()

// New:
const { mutate, status, reset } = useMutation()
```

### `mutation.mutate`는 더 이상 Promise를 반환하지 않습니다.

- `[mutate]` 변수는 `mutation.mutate` 함수로 변경되었습니다.
- `mutation.mutateAsync` 함수가 추가되었습니다.

많은 사용자가 Promise가 일반 Promise처럼 동작할 것으로 기대했기에 이러한 변경을 했습니다.

이제 `mutate` 함수가 `mutate`, `mutateAsync`로 분리되었습니다.

콜백을 사용할 때는 `mutate` 함수를 사용합니다.

```tsx
const { mutate } = useMutation({ mutationFn: addTodo })

mutate('todo', {
  onSuccess: (data) => {
    console.log(data)
  },
  onError: (error) => {
    console.error(error)
  },
  onSettled: () => {
    console.log('settled')
  },
})
```

async/await를 사용할 때는 `mutateAsync` 함수를 사용합니다.

```tsx
const { mutateAsync } = useMutation({ mutationFn: addTodo })

try {
  const data = await mutateAsync('todo')
  console.log(data)
} catch (error) {
  console.error(error)
} finally {
  console.log('settled')
}
```

### useQuery 객체 문법이 압축된 구성 방식으로 바뀌었습니다.

```tsx
// Old:
useQuery({
  queryKey: 'posts',
  queryFn: fetchPosts,
  config: { staleTime: Infinity },
})

// New:
useQuery({
  queryKey: 'posts',
  queryFn: fetchPosts,
  staleTime: Infinity,
})
```

### QueryOptions.enabled 옵션이 설정되면 반드시 불리언(`true`/`false`)이어야 합니다.

`enabled` 옵션은 이제 값이 `false`일 때만 쿼리를 비활성화합니다.
필요하다면 `!!userId`, `Boolean(userId)`로 캐스팅할 수 있으며 불리언이 아닌 값이 전달되면 오류가 발생합니다.

### QueryOptions.initialStale 옵션이 제거되었습니다.

`initialStale` 옵션은 제거되었고, 초기 데이터는 일반 데이터처럼 다뤄집니다.
즉 `initialData`를 제공하면 기본적으로 마운트 시 재페치됩니다.
즉시 재페치하지 않으려면 `staleTime`을 정의하세요.

### `QueryOptions.forceFetchOnMount` 옵션이 `refetchOnMount: 'always'`로 대체되었습니다.

`refetchOn____` 옵션이 너무 많아져서 정리했습니다.

### `QueryOptions.refetchOnMount` 옵션이 이제 해당 부모 컴포넌트에만 적용됩니다.

v2에서는 `refetchOnMount`가 `false`이면 추가 컴포넌트도 마운트 시 재페치를 막았습니다.
v3에서는 옵션을 설정한 컴포넌트에서만 재페치가 발생하지 않습니다.

### `QueryOptions.queryFnParamsFilter`가 새 `QueryFunctionContext` 객체로 대체되었습니다.

`queryFnParamsFilter` 옵션이 제거된 이유는 쿼리 함수가 이제 쿼리 키 대신 `QueryFunctionContext` 객체를 받기 때문입니다.

`QueryFunctionContext`에도 쿼리 키가 포함되어 있으므로 여전히 쿼리 함수 내에서 필터링할 수 있습니다.

### `QueryOptions.notifyOnStatusChange` 옵션이 새 `notifyOnChangeProps`, `notifyOnChangePropsExclusions` 옵션으로 대체되었습니다.

이제 컴포넌트가 언제 리렌더링해야 하는지 더 세밀하게 구성할 수 있습니다.

`data`, `error` 프로퍼티가 변경될 때만 리렌더링:

```tsx
import { useQuery } from 'react-query'

function User() {
  const { data } = useQuery(['user'], fetchUser, {
    notifyOnChangeProps: ['data', 'error'],
  })
  return <div>Username: {data.username}</div>
}
```

`isStale` 프로퍼티가 변경될 때 리렌더링 방지:

```tsx
import { useQuery } from 'react-query'

function User() {
  const { data } = useQuery(['user'], fetchUser, {
    notifyOnChangePropsExclusions: ['isStale'],
  })
  return <div>Username: {data.username}</div>
}
```

### `QueryResult.clear()` 함수가 `QueryResult.remove()`로 이름이 변경되었습니다.

`clear`라는 이름과 달리 실제로는 캐시에서 쿼리를 제거했으므로 기능에 맞게 이름을 바꿨습니다.

### `QueryResult.updatedAt` 프로퍼티가 `QueryResult.dataUpdatedAt`, `QueryResult.errorUpdatedAt`으로 분리되었습니다.

데이터와 오류가 동시에 존재할 수 있기 때문에 `updatedAt`을 두 개의 프로퍼티로 나눴습니다.

### `setConsole()`이 새 `setLogger()` 함수로 대체되었습니다.

```tsx
import { setLogger } from 'react-query'

// Log with Sentry
setLogger({
  error: (error) => {
    Sentry.captureException(error)
  },
})

// Log with Winston
setLogger(winston.createLogger())
```

### React Native에서는 더 이상 로거를 재정의할 필요가 없습니다.

React Native에서 쿼리 실패 시 에러 화면이 표시되지 않도록 콘솔을 수동으로 변경해야 했습니다.

```tsx
import { setConsole } from 'react-query'

setConsole({
  log: console.log,
  warn: console.warn,
  error: console.warn,
})
```

v3에서는 **React Native에서 React Query를 사용하면 자동으로 처리됩니다.**

### 타입스크립트

#### `QueryStatus`가 [enum](https://www.typescriptlang.org/docs/handbook/enums.html#string-enums)에서 [유니언 타입](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#union-types)으로 변경되었습니다.

쿼리나 뮤테이션의 status 프로퍼티를 QueryStatus enum 값과 비교하던 경우 이제 각 프로퍼티에 해당하는 문자열 리터럴과 비교해야 합니다.

따라서 enum 프로퍼티를 다음과 같이 문자열 리터럴로 변경해야 합니다.

- `QueryStatus.Idle` -> `'idle'`
- `QueryStatus.Loading` -> `'loading'`
- `QueryStatus.Error` -> `'error'`
- `QueryStatus.Success` -> `'success'`

필요한 변경 예시는 다음과 같습니다.

```tsx
- import { useQuery, QueryStatus } from 'react-query'; // [!code --]
+ import { useQuery } from 'react-query'; // [!code ++]

const { data, status } = useQuery(['post', id], () => fetchPost(id))

- if (status === QueryStatus.Loading) { // [!code --]
+ if (status === 'loading') { // [!code ++]
  ...
}

- if (status === QueryStatus.Error) { // [!code --]
+ if (status === 'error') { // [!code ++]
  ...
}
```

## 새로운 기능

#### Query Data Selector

`useQuery`, `useInfiniteQuery` 훅에 `select` 옵션이 추가되어 쿼리 결과의 일부를 선택하거나 변환할 수 있습니다.

```tsx
import { useQuery } from 'react-query'

function User() {
  const { data } = useQuery(['user'], fetchUser, {
    select: (user) => user.username,
  })
  return <div>Username: {data}</div>
}
```

`notifyOnChangeProps` 옵션을 `['data', 'error']`로 설정하면 선택한 데이터가 변경될 때만 리렌더링합니다.

#### 가변 길이 병렬 쿼리 실행을 위한 useQueries() 훅

`useQuery`를 반복문에서 실행하고 싶었나요? 훅의 규칙상 안 되지만 새 `useQueries()` 훅으로 가능합니다!

```tsx
import { useQueries } from 'react-query'

function Overview() {
  const results = useQueries([
    { queryKey: ['post', 1], queryFn: fetchPost },
    { queryKey: ['post', 2], queryFn: fetchPost },
  ])
  return (
    <ul>
      {results.map(({ data }) => data && <li key={data.id}>{data.title})</li>)}
    </ul>
  )
}
```

#### 재시도/오프라인 뮤테이션

기본적으로 React Query는 뮤테이션이 오류일 때 재시도하지 않지만 `retry` 옵션으로 재시도가 가능합니다.

```tsx
const mutation = useMutation({
  mutationFn: addTodo,
  retry: 3,
})
```

디바이스가 오프라인이라서 뮤테이션이 실패하면, 다시 연결될 때 동일한 순서로 재시도됩니다.

#### 뮤테이션 지속

뮤테이션을 스토리지에 저장해두었다가 나중에 재개할 수 있습니다. 자세한 내용은 뮤테이션 문서를 참조하세요.

#### QueryObserver

`QueryObserver`를 사용하면 쿼리를 생성하거나 관찰할 수 있습니다.

```tsx
const observer = new QueryObserver(queryClient, { queryKey: 'posts' })

const unsubscribe = observer.subscribe((result) => {
  console.log(result)
  unsubscribe()
})
```

#### InfiniteQueryObserver

`InfiniteQueryObserver`는 무한 쿼리를 생성하거나 관찰할 때 사용할 수 있습니다:

```tsx
const observer = new InfiniteQueryObserver(queryClient, {
  queryKey: 'posts',
  queryFn: fetchPosts,
  getNextPageParam: (lastPage, allPages) => lastPage.nextCursor,
  getPreviousPageParam: (firstPage, allPages) => firstPage.prevCursor,
})

const unsubscribe = observer.subscribe((result) => {
  console.log(result)
  unsubscribe()
})
```

#### QueriesObserver

`QueriesObserver`는 여러 쿼리를 생성하거나 관찰할 때 사용할 수 있습니다:

```tsx
const observer = new QueriesObserver(queryClient, [
  { queryKey: ['post', 1], queryFn: fetchPost },
  { queryKey: ['post', 2], queryFn: fetchPost },
])

const unsubscribe = observer.subscribe((result) => {
  console.log(result)
  unsubscribe()
})
```

#### 특정 쿼리에 대한 기본 옵션 설정

`QueryClient.setQueryDefaults()` 메서드는 특정 쿼리에 대한 기본 옵션을 설정할 때 사용할 수 있습니다:

```tsx
queryClient.setQueryDefaults(['posts'], { queryFn: fetchPosts })

function Component() {
  const { data } = useQuery(['posts'])
}
```

#### 특정 뮤테이션에 대한 기본 옵션 설정

`QueryClient.setMutationDefaults()` 메서드는 특정 뮤테이션에 대한 기본 옵션을 설정할 때 사용할 수 있습니다:

```tsx
queryClient.setMutationDefaults(['addPost'], { mutationFn: addPost })

function Component() {
  const { mutate } = useMutation({ mutationKey: ['addPost'] })
}
```

#### useIsFetching()

`useIsFetching()` 훅은 이제 필터를 받아 특정 유형의 쿼리에만 스피너를 표시하도록 하는 등의 제어가 가능합니다:

```tsx
const fetches = useIsFetching({ queryKey: ['posts'] })
```

#### Core 분리

React Query의 코어는 이제 React와 완전히 분리되어, 단독으로 혹은 다른 프레임워크에서도 사용할 수 있습니다. 코어 기능만 가져오려면 `react-query/core` 엔트리 포인트를 사용하세요:

```tsx
import { QueryClient } from 'react-query/core'
```

### Devtools는 이제 메인 레포와 npm 패키지에 포함됨

Devtools는 이제 `react-query` 패키지 자체에 포함되어 있으며 `react-query/devtools`로 임포트할 수 있습니다. 기존의 `react-query-devtools` 임포트를 `react-query/devtools`로 교체하기만 하면 됩니다.

