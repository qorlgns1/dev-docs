---
title: '백그라운드 패칭 지표'
description: '쿼리의  상태만으로도 초기 하드 로딩 상태를 표시하기에 충분하지만, 때로는 쿼리가 백그라운드에서 다시 패칭 중임을 알려 주는 추가 지표를 보여주고 싶을 수 있습니다. 이를 위해 쿼리는  변수의 상태와 관계없이 현재 패칭 상태에 있음을 나타낼 수 있는  불리언도 제공합니...'
---

# 백그라운드 패칭 지표

쿼리의 `status === 'pending'` 상태만으로도 초기 하드 로딩 상태를 표시하기에 충분하지만, 때로는 쿼리가 백그라운드에서 다시 패칭 중임을 알려 주는 추가 지표를 보여주고 싶을 수 있습니다. 이를 위해 쿼리는 `status` 변수의 상태와 관계없이 현재 패칭 상태에 있음을 나타낼 수 있는 `isFetching` 불리언도 제공합니다.

[//]: # 'Example'

```tsx
function Todos() {
  const {
    status,
    data: todos,
    error,
    isFetching,
  } = useQuery({
    queryKey: ['todos'],
    queryFn: fetchTodos,
  })

  return status === 'pending' ? (
    <span>Loading...</span>
  ) : status === 'error' ? (
    <span>Error: {error.message}</span>
  ) : (
    <>
      {isFetching ? <div>Refreshing...</div> : null}

      <div>
        {todos.map((todo) => (
          <Todo todo={todo} />
        ))}
      </div>
    </>
  )
}
```

[//]: # 'Example'

## 전역 백그라운드 패칭 로딩 상태 표시

개별 쿼리의 로딩 상태 외에도 **어떤** 쿼리든 (백그라운드 패칭 포함) 로딩 중일 때 전역 로딩 지표를 표시하려면 `useIsFetching` 훅을 사용할 수 있습니다.

[//]: # 'Example2'

```tsx
import { useIsFetching } from '@tanstack/react-query'

function GlobalLoadingIndicator() {
  const isFetching = useIsFetching()

  return isFetching ? (
    <div>Queries are fetching in the background...</div>
  ) : null
}
```

[//]: # 'Example2'

