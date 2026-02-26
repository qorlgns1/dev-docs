---
title: '쿼리 무효화'
description: '쿼리가 다시 가져오기 전에 오래되기를 기다리는 전략은, 특히 사용자의 행동으로 인해 특정 쿼리 데이터가 확실히 오래되었다는 것을 아는 경우에는 항상 통하지 않습니다. 이런 상황을 위해  는 쿼리를 지능적으로 오래된 상태로 표시하고 필요하면 다시 가져올 수 있게 해주는 ...'
---

<!-- Using add-doc skill to follow translation workflow -->

# 쿼리 무효화

쿼리가 다시 가져오기 전에 오래되기를 기다리는 전략은, 특히 사용자의 행동으로 인해 특정 쿼리 데이터가 확실히 오래되었다는 것을 아는 경우에는 항상 통하지 않습니다. 이런 상황을 위해 `QueryClient` 는 쿼리를 지능적으로 오래된 상태로 표시하고 필요하면 다시 가져올 수 있게 해주는 `invalidateQueries` 메서드를 제공합니다!

[//]: # 'Example'

```tsx
// Invalidate every query in the cache
queryClient.invalidateQueries()
// Invalidate every query with a key that starts with `todos`
queryClient.invalidateQueries({ queryKey: ['todos'] })
```

[//]: # 'Example'

> 참고: 정규화된 캐시를 사용하는 다른 라이브러리는 명령형 방식이나 스키마 추론을 통해 로컬 쿼리를 새 데이터로 업데이트하려고 시도하지만, TanStack Query 는 정규화된 캐시를 유지하면서 발생하는 수작업을 피할 수 있도록 **타깃 무효화, 백그라운드 재가져오기, 궁극적으로는 원자적 업데이트** 를 위한 도구를 제공합니다.

쿼리가 `invalidateQueries` 로 무효화되면 두 가지가 발생합니다.

- 쿼리가 오래된 상태로 표시됩니다. 이 오래된 상태는 `useQuery` 또는 관련 훅에서 사용 중인 어떤 `staleTime` 설정도 무시합니다.
- 해당 쿼리가 `useQuery` 또는 관련 훅을 통해 현재 렌더링 중이라면, 백그라운드에서 다시 가져옵니다.

## `invalidateQueries` 를 활용한 쿼리 매칭

`invalidateQueries`, `removeQueries` (그리고 부분 쿼리 매칭을 지원하는 다른 API) 를 사용할 때는 접두사로 여러 쿼리를 매칭하거나, 아주 구체적으로 정확한 쿼리 하나만 매칭할 수도 있습니다. 사용할 수 있는 필터 유형에 대한 정보는 [Query Filters](https://tanstack.com/query/latest/docs/framework/react/guides/filters.md#query-filters) 를 참고하세요.

이 예시에서는 쿼리 키가 `todos` 로 시작하는 모든 쿼리를 무효화하기 위해 `todos` 접두사를 사용할 수 있습니다.

[//]: # 'Example2'

```tsx
import { useQuery, useQueryClient } from '@tanstack/react-query'

// Get QueryClient from the context
const queryClient = useQueryClient()

queryClient.invalidateQueries({ queryKey: ['todos'] })

// Both queries below will be invalidated
const todoListQuery = useQuery({
  queryKey: ['todos'],
  queryFn: fetchTodoList,
})
const todoListQuery = useQuery({
  queryKey: ['todos', { page: 1 }],
  queryFn: fetchTodoList,
})
```

[//]: # 'Example2'

`invalidateQueries` 메서드에 더 구체적인 쿼리 키를 전달하면 특정 변수를 가진 쿼리만 무효화할 수도 있습니다.

[//]: # 'Example3'

```tsx
queryClient.invalidateQueries({
  queryKey: ['todos', { type: 'done' }],
})

// The query below will be invalidated
const todoListQuery = useQuery({
  queryKey: ['todos', { type: 'done' }],
  queryFn: fetchTodoList,
})

// However, the following query below will NOT be invalidated
const todoListQuery = useQuery({
  queryKey: ['todos'],
  queryFn: fetchTodoList,
})
```

[//]: # 'Example3'

`invalidateQueries` API 는 매우 유연하므로, 추가 변수나 하위 키가 없는 `todos` 쿼리만 **정확히** 무효화하고 싶다면 `invalidateQueries` 메서드에 `exact: true` 옵션을 전달하면 됩니다.

[//]: # 'Example4'

```tsx
queryClient.invalidateQueries({
  queryKey: ['todos'],
  exact: true,
})

// The query below will be invalidated
const todoListQuery = useQuery({
  queryKey: ['todos'],
  queryFn: fetchTodoList,
})

// However, the following query below will NOT be invalidated
const todoListQuery = useQuery({
  queryKey: ['todos', { type: 'done' }],
  queryFn: fetchTodoList,
})
```

[//]: # 'Example4'

더 **세밀한** 제어가 필요하다면, `invalidateQueries` 메서드에 프레디케이트 함수를 전달할 수 있습니다. 이 함수는 쿼리 캐시의 각 `Query` 인스턴스를 전달받아 해당 쿼리를 무효화할지 여부에 따라 `true` 또는 `false` 를 반환할 수 있게 해줍니다.

[//]: # 'Example5'

```tsx
queryClient.invalidateQueries({
  predicate: (query) =>
    query.queryKey[0] === 'todos' && query.queryKey[1]?.version >= 10,
})

// The query below will be invalidated
const todoListQuery = useQuery({
  queryKey: ['todos', { version: 20 }],
  queryFn: fetchTodoList,
})

// The query below will be invalidated
const todoListQuery = useQuery({
  queryKey: ['todos', { version: 10 }],
  queryFn: fetchTodoList,
})

// However, the following query below will NOT be invalidated
const todoListQuery = useQuery({
  queryKey: ['todos', { version: 5 }],
  queryFn: fetchTodoList,
})
```

[//]: # 'Example5'

