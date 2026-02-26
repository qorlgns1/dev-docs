---
title: '쿼리 비활성화/일시 중지'
description: '쿼리가 자동으로 실행되는 것을 막고 싶다면  옵션을 사용할 수 있습니다.  옵션에는 불리언 값을 반환하는 콜백도 전달할 수 있습니다.'
---

Source URL: https://tanstack.com/query/latest/docs/framework/react/guides/disabling-queries

# 쿼리 비활성화/일시 중지

쿼리가 자동으로 실행되는 것을 막고 싶다면 `enabled = false` 옵션을 사용할 수 있습니다. `enabled` 옵션에는 불리언 값을 반환하는 콜백도 전달할 수 있습니다.

`enabled`가 `false`일 때:

- 쿼리에 캐시된 데이터가 있으면 `status === 'success'` 또는 `isSuccess` 상태로 초기화됩니다.
- 쿼리에 캐시된 데이터가 없으면 `status === 'pending'`과 `fetchStatus === 'idle'` 상태에서 시작합니다.
- 마운트 시 자동으로 fetch 하지 않습니다.
- 백그라운드에서 자동으로 refetch 하지 않습니다.
- 일반적으로 쿼리를 다시 가져오게 만드는 쿼리 클라이언트의 `invalidateQueries` 및 `refetchQueries` 호출을 무시합니다.
- `useQuery`에서 반환된 `refetch`로 수동 트리거가 가능하지만, `skipToken`과는 함께 작동하지 않습니다.

> TypeScript 사용자는 `enabled = false`의 대안으로 [skipToken](#typesafe-disabling-of-queries-using-skiptoken)을 선호할 수 있습니다.

[//]: # '예제'

```tsx
function Todos() {
  const { isLoading, isError, data, error, refetch, isFetching } = useQuery({
    queryKey: ['todos'],
    queryFn: fetchTodoList,
    enabled: false,
  })

  return (
    <div>
      <button onClick={() => refetch()}>Fetch Todos</button>

      {data ? (
        <ul>
          {data.map((todo) => (
            <li key={todo.id}>{todo.title}</li>
          ))}
        </ul>
      ) : isError ? (
        <span>Error: {error.message}</span>
      ) : isLoading ? (
        <span>Loading...</span>
      ) : (
        <span>Not ready ...</span>
      )}

      <div>{isFetching ? 'Fetching...' : null}</div>
    </div>
  )
}
```

[//]: # '예제'

쿼리를 완전히 비활성화하면 TanStack Query가 제공하는 수많은 멋진 기능(예: 백그라운드 refetch)을 포기하게 되며, 관용적인 방식도 아닙니다. 이는 선언형 접근법(쿼리가 언제 실행되어야 하는지 의존성을 정의)에서 명령형 모드(여기를 클릭할 때마다 fetch)로 전환합니다. 또한 `refetch`에 매개변수를 전달할 수도 없습니다. 대부분의 경우 원하는 것은 초기 fetch를 지연하는 lazy 쿼리입니다.

## Lazy 쿼리

`enabled` 옵션은 쿼리를 영구적으로 비활성화하는 데뿐만 아니라 나중에 활성화/비활성화하는 데도 사용할 수 있습니다. 좋은 예시는 사용자가 필터 값을 입력했을 때만 첫 요청을 보내고 싶은 필터 폼입니다.

[//]: # '예제2'

```tsx
function Todos() {
  const [filter, setFilter] = React.useState('')

  const { data } = useQuery({
    queryKey: ['todos', filter],
    queryFn: () => fetchTodos(filter),
    // ⬇️ disabled as long as the filter is empty
    enabled: !!filter,
  })

  return (
    <div>
      // 🚀 applying the filter will enable and execute the query
      <FiltersForm onApply={setFilter} />
      {data && <TodosTable data={data} />}
    </div>
  )
}
```

[//]: # '예제2'

### isLoading (이전 명칭: `isInitialLoading`)

Lazy 쿼리는 시작부터 `status: 'pending'` 상태입니다. `pending`은 아직 데이터가 없다는 뜻으로 기술적으로 맞지만, 쿼리가 아직 _enabled_ 상태가 아니어서 현재 데이터를 가져오지 않는다면 이 플래그로 로딩 스피너를 표시하기 어렵습니다.

비활성화된 쿼리나 lazy 쿼리를 사용 중이라면 대신 `isLoading` 플래그를 사용할 수 있습니다. 이 플래그는 다음에서 파생됩니다.

`isPending && isFetching`

따라서 쿼리가 처음으로 fetch 중일 때만 true가 됩니다.

## `skipToken`을 사용한 타입 안전한 쿼리 비활성화

TypeScript를 사용한다면 `skipToken`으로 쿼리를 비활성화할 수 있습니다. 조건에 따라 쿼리를 비활성화하려 하지만 여전히 타입 안전성을 유지하고 싶을 때 유용합니다.

> **중요**: `useQuery`의 `refetch`는 `skipToken`과 함께 작동하지 않습니다. `skipToken`을 사용하는 쿼리에서 `refetch()`를 호출하면 실행할 유효한 쿼리 함수가 없기 때문에 `Missing queryFn` 오류가 발생합니다. 수동으로 쿼리를 트리거해야 한다면 `refetch()`가 정상 동작하는 `enabled: false`를 사용하는 것이 좋습니다. 이 제한을 제외하면 `skipToken`은 `enabled: false`와 동일하게 동작합니다.

[//]: # '예제3'

```tsx
import { skipToken, useQuery } from '@tanstack/react-query'

function Todos() {
  const [filter, setFilter] = React.useState<string | undefined>()

  const { data } = useQuery({
    queryKey: ['todos', filter],
    // ⬇️ disabled as long as the filter is undefined or empty
    queryFn: filter ? () => fetchTodos(filter) : skipToken,
  })

  return (
    <div>
      // 🚀 applying the filter will enable and execute the query
      <FiltersForm onApply={setFilter} />
      {data && <TodosTable data={data} />}
    </div>
  )
}
```

[//]: # '예제3'

