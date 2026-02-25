---
title: '쿼리 기본'
description: '쿼리는 고유 키에 연결된 비동기 데이터 소스에 대한 선언적 의존성입니다. 쿼리는 어떤 Promise 기반 메서드(예: GET, POST)를 통해서든 서버에서 데이터를 가져오는 데 사용할 수 있습니다. 서버의 데이터를 수정하는 메서드를 사용한다면 Mutations를 사용...'
---

Source URL: https://tanstack.com/query/latest/docs/framework/react/guides/queries

# 쿼리

## 쿼리 기본

쿼리는 **고유 키**에 연결된 비동기 데이터 소스에 대한 선언적 의존성입니다. 쿼리는 어떤 Promise 기반 메서드(예: GET, POST)를 통해서든 서버에서 데이터를 가져오는 데 사용할 수 있습니다. 서버의 데이터를 수정하는 메서드를 사용한다면 [Mutations](https://tanstack.com/query/latest/docs/framework/react/guides/mutations.md)를 사용하는 것이 좋습니다.

컴포넌트나 커스텀 훅에서 쿼리를 구독하려면 최소한 다음을 포함해 `useQuery` 훅을 호출하세요.

- **쿼리의 고유 키**
- Promise 를 반환하는 함수. 이 함수는
  - 데이터를 resolve 하거나
  - 오류를 throw 합니다.

[//]: # 'Example'

```tsx
import { useQuery } from '@tanstack/react-query'

function App() {
  const info = useQuery({ queryKey: ['todos'], queryFn: fetchTodoList })
}
```

[//]: # 'Example'

제공한 **고유 키**는 내부적으로 재요청, 캐싱, 앱 전반의 쿼리 공유에 사용됩니다.

`useQuery`가 반환하는 쿼리 결과는 템플릿 작성이나 기타 데이터 활용에 필요한 모든 정보를 포함합니다.

[//]: # 'Example2'

```tsx
const result = useQuery({ queryKey: ['todos'], queryFn: fetchTodoList })
```

[//]: # 'Example2'

`result` 객체에는 생산성을 높이는 데 알아두어야 할 몇 가지 중요한 상태가 있습니다. 쿼리는 어느 순간이든 다음 상태 중 하나에만 속합니다.

- `isPending` 또는 `status === 'pending'` - 아직 데이터가 없는 상태
- `isError` 또는 `status === 'error'` - 쿼리 실행 중 오류 발생
- `isSuccess` 또는 `status === 'success'` - 쿼리가 성공해 데이터를 사용할 수 있음

이 기본 상태 외에도 상태에 따라 더 많은 정보를 얻을 수 있습니다.

- `error` - 쿼리가 `isError` 상태이면 `error` 프로퍼티로 오류를 확인할 수 있습니다.
- `data` - 쿼리가 `isSuccess` 상태이면 `data` 프로퍼티로 데이터를 확인할 수 있습니다.
- `isFetching` - 어떤 상태이든 쿼리가 데이터를 가져오는 중(백그라운드 재요청 포함)이면 `isFetching` 값이 `true`입니다.

**대부분**의 쿼리에서는 `isPending` 상태를 먼저 확인하고, 그다음 `isError` 상태를 확인한 뒤, 데이터가 있다고 가정하고 성공 상태를 렌더링하면 충분합니다.

[//]: # 'Example3'

```tsx
function Todos() {
  const { isPending, isError, data, error } = useQuery({
    queryKey: ['todos'],
    queryFn: fetchTodoList,
  })

  if (isPending) {
    return <span>Loading...</span>
  }

  if (isError) {
    return <span>Error: {error.message}</span>
  }

  // We can assume by this point that `isSuccess === true`
  return (
    <ul>
      {data.map((todo) => (
        <li key={todo.id}>{todo.title}</li>
      ))}
    </ul>
  )
}
```

[//]: # 'Example3'

불리언 대신 `status` 상태를 활용할 수도 있습니다.

[//]: # 'Example4'

```tsx
function Todos() {
  const { status, data, error } = useQuery({
    queryKey: ['todos'],
    queryFn: fetchTodoList,
  })

  if (status === 'pending') {
    return <span>Loading...</span>
  }

  if (status === 'error') {
    return <span>Error: {error.message}</span>
  }

  // also status === 'success', but "else" logic works, too
  return (
    <ul>
      {data.map((todo) => (
        <li key={todo.id}>{todo.title}</li>
      ))}
    </ul>
  )
}
```

[//]: # 'Example4'

TypeScript 는 `pending`과 `error`를 먼저 확인한 뒤 `data` 에 접근하면 해당 타입을 자동으로 좁혀 줍니다.

### FetchStatus

`status` 필드 외에도 다음 옵션을 가진 추가 `fetchStatus` 프로퍼티를 사용할 수 있습니다.

- `fetchStatus === 'fetching'` - 현재 데이터를 가져오는 중입니다.
- `fetchStatus === 'paused'` - 데이터를 가져오려 했지만 일시 중지되었습니다. 자세한 내용은 [Network Mode](https://tanstack.com/query/latest/docs/framework/react/guides/network-mode.md) 가이드를 참고하세요.
- `fetchStatus === 'idle'` - 지금은 아무 작업도 하지 않습니다.

### 두 가지 상태가 필요한 이유

백그라운드 재요청과 stale-while-revalidate 로직 덕분에 `status` 와 `fetchStatus` 조합은 다양합니다. 예를 들면:

- `success` 상태의 쿼리는 보통 `idle` fetchStatus 지만, 백그라운드 재요청이 진행 중이면 `fetching`일 수도 있습니다.
- 마운트되었지만 데이터가 없는 쿼리는 보통 `pending` 상태와 `fetching` fetchStatus 를 갖지만, 네트워크 연결이 없으면 `paused` 가 될 수도 있습니다.

즉, 실제로 데이터를 가져오지 않더라도 쿼리가 `pending` 상태일 수 있다는 점을 기억하세요. 경험칙은 다음과 같습니다.

- `status` 는 `data` 에 관한 정보를 제공합니다. 데이터가 있습니까?
- `fetchStatus` 는 `queryFn` 에 관한 정보를 제공합니다. 실행 중입니까?

[//]: # 'Materials'

## 추가 읽을거리

상태를 확인하는 다른 방식이 궁금하다면 [TkDodo 의 글](https://tkdodo.eu/blog/status-checks-in-react-query)을 참고하세요.

[//]: # 'Materials'

