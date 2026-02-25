---
title: '무한 쿼리'
description: '기존 데이터 집합에 데이터를 계속 덧붙여 “더 보기”를 제공하거나 “무한 스크롤”을 구현하는 것은 매우 흔한 UI 패턴입니다. TanStack Query는 이러한 목록을 위해 의 확장판인 를 제공합니다.'
---

# 무한 쿼리

기존 데이터 집합에 데이터를 계속 덧붙여 “더 보기”를 제공하거나 “무한 스크롤”을 구현하는 것은 매우 흔한 UI 패턴입니다. TanStack Query는 이러한 목록을 위해 `useQuery`의 확장판인 `useInfiniteQuery`를 제공합니다.

`useInfiniteQuery`를 사용하면 다음과 같은 차이점을 확인할 수 있습니다.

- `data`가 이제 무한 쿼리 데이터를 담는 객체입니다.
- `data.pages` 배열에는 페치된 페이지가 들어 있습니다.
- `data.pageParams` 배열에는 각 페이지를 가져오는 데 사용된 페이지 파라미터가 들어 있습니다.
- `fetchNextPage`와 `fetchPreviousPage` 함수를 사용할 수 있으며, `fetchNextPage`는 필수입니다.
- 초기 페이지 파라미터를 지정하기 위한 `initialPageParam` 옵션이 새로 제공되며 필수입니다.
- 추가 데이터를 로드할 수 있는지 여부와 필요한 정보를 판단하기 위해 `getNextPageParam`과 `getPreviousPageParam` 옵션을 사용할 수 있습니다. 이 정보는 쿼리 함수의 추가 인자로 전달됩니다.
- `hasNextPage` 불리언이 제공되며, `getNextPageParam`이 `null`이나 `undefined`가 아닌 값을 반환하면 `true`입니다.
- `hasPreviousPage` 불리언이 제공되며, `getPreviousPageParam`이 `null`이나 `undefined`가 아닌 값을 반환하면 `true`입니다.
- `isFetchingNextPage`와 `isFetchingPreviousPage` 불리언으로 백그라운드 새로 고침 상태와 추가 로딩 상태를 구분할 수 있습니다.

> 참고: `initialData`나 `placeholderData` 옵션은 `data.pages`와 `data.pageParams` 속성을 가진 객체 구조와 동일해야 합니다.

## 예시

`cursor` 인덱스를 기준으로 한 번에 3개의 `projects` 페이지를 반환하고, 다음 프로젝트 묶음을 가져오는 데 사용할 수 있는 커서를 함께 돌려주는 API가 있다고 가정해 보겠습니다.

```tsx
fetch('/api/projects?cursor=0')
// { data: [...], nextCursor: 3}
fetch('/api/projects?cursor=3')
// { data: [...], nextCursor: 6}
fetch('/api/projects?cursor=6')
// { data: [...], nextCursor: 9}
fetch('/api/projects?cursor=9')
// { data: [...] }
```

이 정보를 바탕으로 “더 보기” UI를 만들려면 다음과 같이 하면 됩니다.

- `useInfiniteQuery`가 기본적으로 첫 데이터 묶음을 요청할 때까지 기다립니다.
- 다음 쿼리에 필요한 정보를 `getNextPageParam`에서 반환합니다.
- `fetchNextPage` 함수를 호출합니다.

[//]: # 'Example'

```tsx
import { useInfiniteQuery } from '@tanstack/react-query'

function Projects() {
  const fetchProjects = async ({ pageParam }) => {
    const res = await fetch('/api/projects?cursor=' + pageParam)
    return res.json()
  }

  const {
    data,
    error,
    fetchNextPage,
    hasNextPage,
    isFetching,
    isFetchingNextPage,
    status,
  } = useInfiniteQuery({
    queryKey: ['projects'],
    queryFn: fetchProjects,
    initialPageParam: 0,
    getNextPageParam: (lastPage, pages) => lastPage.nextCursor,
  })

  return status === 'pending' ? (
    <p>Loading...</p>
  ) : status === 'error' ? (
    <p>Error: {error.message}</p>
  ) : (
    <>
      {data.pages.map((group, i) => (
        <React.Fragment key={i}>
          {group.data.map((project) => (
            <p key={project.id}>{project.name}</p>
          ))}
        </React.Fragment>
      ))}
      <div>
        <button
          onClick={() => fetchNextPage()}
          disabled={!hasNextPage || isFetching}
        >
          {isFetchingNextPage
            ? 'Loading more...'
            : hasNextPage
              ? 'Load More'
              : 'Nothing more to load'}
        </button>
      </div>
      <div>{isFetching && !isFetchingNextPage ? 'Fetching...' : null}</div>
    </>
  )
}
```

[//]: # 'Example'

이미 진행 중인 페치가 있을 때 `fetchNextPage`를 호출하면 백그라운드에서 일어나는 데이터 새로 고침을 덮어쓸 위험이 있습니다. 목록을 렌더링하면서 동시에 `fetchNextPage`를 트리거하는 경우 특히 주의해야 합니다.

InfiniteQuery에는 동시에 하나의 페치만 진행될 수 있습니다. 모든 페이지가 단일 캐시 항목을 공유하므로 동시에 두 번 페치하려고 하면 데이터가 덮어쓰일 수 있습니다.

동시 페치를 허용하려면 `fetchNextPage`에 `{ cancelRefetch: false }` 옵션(기본값: true)을 사용할 수 있습니다.

충돌 없이 매끄럽게 쿼리하려면, 특히 사용자가 직접 호출을 제어하지 않는 상황에서는 쿼리가 `isFetching` 상태가 아닌지 확인하는 것이 좋습니다.

[//]: # 'Example1'

```jsx
<List onEndReached={() => hasNextPage && !isFetching && fetchNextPage()} />
```

[//]: # 'Example1'

## 무한 쿼리를 다시 가져와야 할 때는 어떻게 되나요?

무한 쿼리가 `stale` 상태가 되어 리패치가 필요하면 각 그룹이 첫 번째 그룹부터 `순차적으로` 페치됩니다. 이렇게 하면 기본 데이터가 변경되더라도 오래된 커서를 사용해 중복되거나 누락되는 기록을 막을 수 있습니다. 무한 쿼리 결과가 queryCache에서 제거되면 페이지네이션은 초기 상태로 재시작되고 최초 그룹만 요청됩니다.

## 양방향 무한 리스트를 구현하려면?

`getPreviousPageParam`, `fetchPreviousPage`, `hasPreviousPage`, `isFetchingPreviousPage` 속성과 함수를 활용하면 양방향 리스트를 구현할 수 있습니다.

[//]: # 'Example3'

```tsx
useInfiniteQuery({
  queryKey: ['projects'],
  queryFn: fetchProjects,
  initialPageParam: 0,
  getNextPageParam: (lastPage, pages) => lastPage.nextCursor,
  getPreviousPageParam: (firstPage, pages) => firstPage.prevCursor,
})
```

[//]: # 'Example3'

## 페이지를 역순으로 표시하고 싶다면?

때로는 페이지를 역순으로 보여주고 싶을 수 있습니다. 이 경우 `select` 옵션을 사용할 수 있습니다.

[//]: # 'Example4'

```tsx
useInfiniteQuery({
  queryKey: ['projects'],
  queryFn: fetchProjects,
  select: (data) => ({
    pages: [...data.pages].reverse(),
    pageParams: [...data.pageParams].reverse(),
  }),
})
```

[//]: # 'Example4'

## 무한 쿼리를 수동으로 업데이트하고 싶다면?

### 첫 페이지만 수동으로 제거하기

[//]: # 'Example5'

```tsx
queryClient.setQueryData(['projects'], (data) => ({
  pages: data.pages.slice(1),
  pageParams: data.pageParams.slice(1),
}))
```

[//]: # 'Example5'

### 개별 페이지에서 단일 값을 수동으로 제거하기

[//]: # 'Example6'

```tsx
const newPagesArray =
  oldPagesArray?.pages.map((page) =>
    page.filter((val) => val.id !== updatedId),
  ) ?? []

queryClient.setQueryData(['projects'], (data) => ({
  pages: newPagesArray,
  pageParams: data.pageParams,
}))
```

[//]: # 'Example6'

### 첫 페이지만 유지하기

[//]: # 'Example7'

```tsx
queryClient.setQueryData(['projects'], (data) => ({
  pages: data.pages.slice(0, 1),
  pageParams: data.pageParams.slice(0, 1),
}))
```

[//]: # 'Example7'

항상 pages와 pageParams의 데이터 구조를 동일하게 유지해야 합니다!

## 페이지 수를 제한하고 싶다면?

일부 사용 사례에서는 성능과 UX 개선을 위해 쿼리 데이터에 저장되는 페이지 수를 제한하고 싶을 수 있습니다.

- 사용자가 많은 페이지를 로드할 수 있을 때(메모리 사용량)
- 수십 개 페이지를 포함한 무한 쿼리를 리패치해야 할 때(네트워크 사용량: 모든 페이지가 순차적으로 페치됨)

해결책은 “제한된 무한 쿼리”를 사용하는 것입니다. `getNextPageParam`과 `getPreviousPageParam`과 함께 `maxPages` 옵션을 사용하면 양방향으로 필요한 시점에만 페이지를 가져올 수 있습니다.

다음 예제에서는 쿼리 데이터의 pages 배열에 최대 3페이지만 유지합니다. 리패치가 필요하면 이 3페이지만 순차적으로 다시 가져옵니다.

[//]: # 'Example8'

```tsx
useInfiniteQuery({
  queryKey: ['projects'],
  queryFn: fetchProjects,
  initialPageParam: 0,
  getNextPageParam: (lastPage, pages) => lastPage.nextCursor,
  getPreviousPageParam: (firstPage, pages) => firstPage.prevCursor,
  maxPages: 3,
})
```

[//]: # 'Example8'

## API가 커서를 반환하지 않으면 어떻게 하나요?

API가 커서를 반환하지 않는다면 `pageParam`을 커서처럼 사용할 수 있습니다. `getNextPageParam`과 `getPreviousPageParam`은 현재 페이지의 `pageParam`도 함께 받으므로 이를 활용해 다음/이전 페이지 파라미터를 계산할 수 있습니다.

[//]: # 'Example9'

```tsx
return useInfiniteQuery({
  queryKey: ['projects'],
  queryFn: fetchProjects,
  initialPageParam: 0,
  getNextPageParam: (lastPage, allPages, lastPageParam) => {
    if (lastPage.length === 0) {
      return undefined
    }
    return lastPageParam + 1
  },
  getPreviousPageParam: (firstPage, allPages, firstPageParam) => {
    if (firstPageParam <= 1) {
      return undefined
    }
    return firstPageParam - 1
  },
})
```

[//]: # 'Example9'
[//]: # 'Materials'

## 추가 읽을거리

무한 쿼리가 내부적으로 어떻게 동작하는지 더 잘 이해하려면 [How Infinite Queries work](https://tkdodo.eu/blog/how-infinite-queries-work) 글을 참고하세요.

[//]: # 'Materials'

