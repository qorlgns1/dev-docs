---
title: 'useQueries'
description: '훅은 가변 개수의 쿼리를 가져오는 데 사용할 수 있습니다.'
---

# useQueries

`useQueries` 훅은 가변 개수의 쿼리를 가져오는 데 사용할 수 있습니다.

```tsx
const ids = [1, 2, 3]
const results = useQueries({
  queries: ids.map((id) => ({
    queryKey: ['post', id],
    queryFn: () => fetchPost(id),
    staleTime: Infinity,
  })),
})
```

**옵션**

`useQueries` 훅은 **queries** 키를 가진 옵션 객체를 받으며, 해당 값은 [`useQuery` 훅](https://tanstack.com/query/latest/docs/framework/react/reference/useQuery.md)과 동일한 쿼리 옵션 객체의 배열입니다 (`QueryClient`는 최상위에서 전달할 수 있으므로 `queryClient` 옵션 제외).

- `queryClient?: QueryClient`
  - 사용자 지정 QueryClient를 제공하려면 사용합니다. 그렇지 않으면 가장 가까운 컨텍스트의 QueryClient가 사용됩니다.
- `combine?: (result: UseQueriesResults) => TCombinedResult`
  - 여러 쿼리의 결과를 단일 값으로 결합하려면 사용합니다.

> 쿼리 객체 배열에서 동일한 쿼리 키를 여러 번 사용하면 쿼리 간 데이터가 일부 공유될 수 있습니다. 이를 방지하려면 쿼리를 중복 제거하고 결과를 원하는 구조로 다시 매핑하는 것을 고려하세요.

**placeholderData**

`placeholderData` 옵션은 `useQueries`에도 존재하지만, `useQuery`와 달리 이전에 렌더링된 쿼리에서 정보를 전달받지 않습니다. 이는 `useQueries`의 입력이 렌더마다 서로 다른 수의 쿼리가 될 수 있기 때문입니다.

**반환값**

`useQueries` 훅은 모든 쿼리 결과를 담은 배열을 반환합니다. 반환 순서는 입력 순서와 동일합니다.

## Combine

여러 결과의 `data`(또는 다른 Query 정보)를 단일 값으로 결합하고 싶다면 `combine` 옵션을 사용할 수 있습니다. 결과는 가능한 한 참조적 안정성을 유지하도록 구조적으로 공유됩니다.

```tsx
const ids = [1, 2, 3]
const combinedQueries = useQueries({
  queries: ids.map((id) => ({
    queryKey: ['post', id],
    queryFn: () => fetchPost(id),
  })),
  combine: (results) => {
    return {
      data: results.map((result) => result.data),
      pending: results.some((result) => result.isPending),
    }
  },
})
```

위 예시에서 `combinedQueries`는 `data`와 `pending` 속성을 가진 객체가 됩니다. Query 결과의 다른 속성은 모두 사라진다는 점에 유의하세요.

### Memoization

`combine` 함수가 다시 실행되는 경우는 다음과 같습니다.

- `combine` 함수 자체의 참조가 변경된 경우
- 어떤 쿼리 결과라도 변경된 경우

즉, 위와 같이 인라인된 `combine` 함수는 렌더마다 실행됩니다. 이를 피하려면 `combine` 함수를 `useCallback`으로 감싸거나, 의존성이 없다면 안정적인 함수 참조로 분리하세요.

