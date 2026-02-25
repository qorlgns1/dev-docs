---
title: '페이지네이션/지연 쿼리'
description: '페이지네이션된 데이터를 렌더링하는 것은 매우 흔한 UI 패턴이며, TanStack Query에서는 쿼리 키에 페이지 정보를 포함하기만 하면 기본적으로 "그냥 작동"합니다:'
---

# 페이지네이션/지연 쿼리

페이지네이션된 데이터를 렌더링하는 것은 매우 흔한 UI 패턴이며, TanStack Query에서는 쿼리 키에 페이지 정보를 포함하기만 하면 기본적으로 "그냥 작동"합니다:

[//]: # 'Example'

```tsx
const result = useQuery({
  queryKey: ['projects', page],
  queryFn: () => fetchProjects(page),
})
```

[//]: # 'Example'

하지만 이 간단한 예제를 실행해 보면 이상한 점을 발견할 수 있습니다:

**각 새 페이지가 완전히 새로운 쿼리로 취급되기 때문에 UI가 `success` 상태와 `pending` 상태 사이를 계속 오갑니다.**

이런 경험은 최적이 아니며, 안타깝게도 많은 도구가 아직도 이런 방식으로 동작합니다. 그러나 TanStack Query는 다릅니다! 예상하셨겠지만, TanStack Query에는 `placeholderData`라는 멋진 기능이 있어서 이러한 문제를 우회할 수 있습니다.

## `placeholderData`로 더 나은 페이지네이션 쿼리 만들기

쿼리를 위해 pageIndex(또는 커서)를 증가시키고 싶은 아래 예제를 생각해 보세요. `useQuery`를 사용한다면 **기능적으로는 문제가 없지만**, 각 페이지나 커서마다 서로 다른 쿼리가 생성되고 파기되기 때문에 UI가 `success`와 `pending` 상태를 반복하며 튑니다. `placeholderData`를 `(previousData) => previousData`로 설정하거나 TanStack Query에서 내보낸 `keepPreviousData` 함수를 사용하면 다음과 같은 이점을 얻습니다:

- **쿼리 키가 변경되더라도 마지막으로 성공한 페치의 데이터가 새로운 데이터를 요청하는 동안 그대로 제공됩니다.**
- 새로운 데이터가 도착하면 기존 `data`가 자연스럽게 교체되어 새 데이터가 표시됩니다.
- 현재 쿼리가 어떤 데이터를 제공 중인지 알 수 있도록 `isPlaceholderData`를 사용할 수 있습니다.

[//]: # 'Example2'

```tsx
import { keepPreviousData, useQuery } from '@tanstack/react-query'
import React from 'react'

function Todos() {
  const [page, setPage] = React.useState(0)

  const fetchProjects = (page = 0) =>
    fetch('/api/projects?page=' + page).then((res) => res.json())

  const { isPending, isError, error, data, isFetching, isPlaceholderData } =
    useQuery({
      queryKey: ['projects', page],
      queryFn: () => fetchProjects(page),
      placeholderData: keepPreviousData,
    })

  return (
    <div>
      {isPending ? (
        <div>Loading...</div>
      ) : isError ? (
        <div>Error: {error.message}</div>
      ) : (
        <div>
          {data.projects.map((project) => (
            <p key={project.id}>{project.name}</p>
          ))}
        </div>
      )}
      <span>Current Page: {page + 1}</span>
      <button
        onClick={() => setPage((old) => Math.max(old - 1, 0))}
        disabled={page === 0}
      >
        Previous Page
      </button>
      <button
        onClick={() => {
          if (!isPlaceholderData && data.hasMore) {
            setPage((old) => old + 1)
          }
        }}
        // Disable the Next Page button until we know a next page is available
        disabled={isPlaceholderData || !data?.hasMore}
      >
        Next Page
      </button>
      {isFetching ? <span> Loading...</span> : null}
    </div>
  )
}
```

[//]: # 'Example2'

## `placeholderData`로 무한 쿼리 결과 지연시키기

그만큼 흔하진 않지만, `placeholderData` 옵션은 `useInfiniteQuery` 훅에서도 완벽하게 동작하므로 무한 쿼리 키가 시간이 지나며 변경되더라도 사용자가 캐시된 데이터를 계속 볼 수 있도록 부드럽게 연결할 수 있습니다.

