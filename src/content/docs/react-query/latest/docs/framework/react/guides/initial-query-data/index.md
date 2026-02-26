---
title: '초기 Query 데이터'
description: '캐시에 필요한 쿼리 데이터를 미리 공급하는 방법은 다양합니다.'
---

# 초기 Query 데이터

캐시에 필요한 쿼리 데이터를 미리 공급하는 방법은 다양합니다.

- 선언형:
  - 쿼리에 `initialData` 를 제공해 캐시가 비어 있을 때 미리 채웁니다.
- 명령형:
  - [`queryClient.prefetchQuery` 로 데이터를 미리 가져오기](https://tanstack.com/query/latest/docs/framework/react/guides/prefetching.md)
  - [`queryClient.setQueryData` 를 사용해 캐시에 직접 데이터 넣기](https://tanstack.com/query/latest/docs/framework/react/guides/prefetching.md)

## `initialData` 로 쿼리 미리 채우기

앱 내부에 쿼리의 초기 데이터가 이미 존재해 바로 전달할 수 있는 경우가 있습니다. 이때 `config.initialData` 옵션을 사용하면 초기 데이터를 지정해 초기 로딩 상태를 건너뛸 수 있습니다.

> 중요: `initialData` 는 캐시에 지속되므로 플레이스홀더나 불완전한 데이터를 넘기지 말고, 그런 경우에는 `placeholderData` 를 사용하세요.

[//]: # 'Example'

```tsx
const result = useQuery({
  queryKey: ['todos'],
  queryFn: () => fetch('/todos'),
  initialData: initialTodos,
})
```

[//]: # 'Example'

### `staleTime` 과 `initialDataUpdatedAt`

기본적으로 `initialData` 는 방금 가져온 것처럼 완전히 최신으로 취급됩니다. 따라서 `staleTime` 옵션에 의해 해석되는 방식에도 영향을 줍니다.

- `initialData` 만 설정하고 `staleTime` 을 생략한 경우(기본값 `staleTime: 0`), 쿼리는 마운트 즉시 다시 가져옵니다.

  [//]: # 'Example2'

  ```tsx
  // Will show initialTodos immediately, but also immediately refetch todos after mount
  const result = useQuery({
    queryKey: ['todos'],
    queryFn: () => fetch('/todos'),
    initialData: initialTodos,
  })
  ```

  [//]: # 'Example2'

- `initialData` 와 `staleTime` 을 `1000`ms 로 설정하면, 해당 시간 동안 쿼리 함수에서 방금 받아온 것처럼 데이터가 신선하다고 간주됩니다.

  [//]: # 'Example3'

  ```tsx
  // Show initialTodos immediately, but won't refetch until another interaction event is encountered after 1000 ms
  const result = useQuery({
    queryKey: ['todos'],
    queryFn: () => fetch('/todos'),
    initialData: initialTodos,
    staleTime: 1000,
  })
  ```

  [//]: # 'Example3'

- 그렇다면 `initialData` 가 완전히 최신이 아니라면 어떻게 해야 할까요? 이때 가장 정확한 구성은 `initialDataUpdatedAt` 옵션입니다. 이 옵션은 `initialData` 가 마지막으로 업데이트된 시간을 밀리초 단위 숫자(JS 타임스탬프, 예: `Date.now()` 반환값)로 전달할 수 있게 해줍니다. 유닉스 타임스탬프가 있다면 `1000` 을 곱해 JS 타임스탬프로 변환해야 한다는 점에 유의하세요.

  [//]: # 'Example4'

  ```tsx
  // Show initialTodos immediately, but won't refetch until another interaction event is encountered after 1000 ms
  const result = useQuery({
    queryKey: ['todos'],
    queryFn: () => fetch('/todos'),
    initialData: initialTodos,
    staleTime: 60 * 1000, // 1 minute
    // This could be 10 seconds ago or 10 minutes ago
    initialDataUpdatedAt: initialTodosUpdatedTimestamp, // eg. 1608412420052
  })
  ```

  [//]: # 'Example4'

  이 옵션을 사용하면 `staleTime` 이 원래 목적(데이터가 얼마나 최신이어야 하는지 결정)에 맞게 작동하면서, `initialData` 가 `staleTime` 보다 오래된 경우 마운트 시 다시 가져오도록 할 수 있습니다. 위 예에서 데이터는 1분 이내에 최신이어야 하며, 쿼리에 `initialData` 의 마지막 업데이트 시간을 알려줌으로써 다시 가져올지 여부를 쿼리가 스스로 판단합니다.

  > 데이터를 **미리 가져온 데이터** 로 취급하고 싶다면 `prefetchQuery` 또는 `fetchQuery` API 로 캐시를 먼저 채워 두어 `staleTime` 을 `initialData` 와 독립적으로 구성할 수 있게 하세요.

### Initial Data 함수

쿼리의 초기 데이터를 가져오는 과정이 무겁거나 매 렌더마다 실행하고 싶지 않다면, `initialData` 값으로 함수를 전달할 수 있습니다. 이 함수는 쿼리가 초기화될 때 한 번만 실행되어 메모리와 CPU 자원을 절약합니다.

[//]: # 'Example5'

```tsx
const result = useQuery({
  queryKey: ['todos'],
  queryFn: () => fetch('/todos'),
  initialData: () => getExpensiveTodos(),
})
```

[//]: # 'Example5'

### 캐시에서 가져온 Initial Data

상황에 따라 다른 쿼리의 캐시 결과를 이용해 초기 데이터를 제공할 수 있습니다. 예를 들어 todos 리스트 쿼리의 캐시 데이터를 찾아 특정 todo 항목을 얻고, 이를 개별 todo 쿼리의 초기 데이터로 사용할 수 있습니다.

[//]: # 'Example6'

```tsx
const result = useQuery({
  queryKey: ['todo', todoId],
  queryFn: () => fetch('/todos'),
  initialData: () => {
    // Use a todo from the 'todos' query as the initial data for this todo query
    return queryClient.getQueryData(['todos'])?.find((d) => d.id === todoId)
  },
})
```

[//]: # 'Example6'

### `initialDataUpdatedAt` 과 함께 캐시에서 가져오는 Initial Data

캐시에서 초기 데이터를 얻는다는 것은, 해당 데이터를 찾아오는 소스 쿼리가 오래되었을 가능성이 크다는 뜻입니다. 인위적으로 `staleTime` 을 조정해 즉시 다시 가져오는 것을 막기보다는, 소스 쿼리의 `dataUpdatedAt` 값을 `initialDataUpdatedAt` 에 전달하는 것이 좋습니다. 이렇게 하면 초기 데이터를 제공했더라도 쿼리 인스턴스가 다시 가져와야 하는 시점을 스스로 판단할 수 있는 모든 정보를 갖게 됩니다.

[//]: # 'Example7'

```tsx
const result = useQuery({
  queryKey: ['todos', todoId],
  queryFn: () => fetch(`/todos/${todoId}`),
  initialData: () =>
    queryClient.getQueryData(['todos'])?.find((d) => d.id === todoId),
  initialDataUpdatedAt: () =>
    queryClient.getQueryState(['todos'])?.dataUpdatedAt,
})
```

[//]: # 'Example7'

### 조건부 캐시 Initial Data

초기 데이터를 찾기 위해 사용하는 소스 쿼리가 오래됐다면, 캐시 데이터를 아예 쓰지 않고 서버에서 다시 가져오고 싶을 수 있습니다. 이 결정을 쉽게 하려면 `queryClient.getQueryState` 메서드를 사용해 소스 쿼리에 대한 추가 정보를 얻으세요. 여기에는 쿼리가 충분히 "신선"한지 판단할 수 있는 `state.dataUpdatedAt` 타임스탬프가 포함됩니다.

[//]: # 'Example8'

```tsx
const result = useQuery({
  queryKey: ['todo', todoId],
  queryFn: () => fetch(`/todos/${todoId}`),
  initialData: () => {
    // Get the query state
    const state = queryClient.getQueryState(['todos'])

    // If the query exists and has data that is no older than 10 seconds...
    if (state && Date.now() - state.dataUpdatedAt <= 10 * 1000) {
      // return the individual todo
      return state.data.find((d) => d.id === todoId)
    }

    // Otherwise, return undefined and let it fetch from a hard loading state!
  },
})
```

[//]: # 'Example8'
[//]: # 'Materials'

## 더 읽을거리

`Initial Data` 와 `Placeholder Data` 를 비교하려면 [TkDodo의 글](https://tkdodo.eu/blog/placeholder-and-initial-data-in-react-query)을 참고하세요.

[//]: # 'Materials'

