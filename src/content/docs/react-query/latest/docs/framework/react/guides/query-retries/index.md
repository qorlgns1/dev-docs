---
title: '쿼리 재시도'
description: '쿼리가 실패하면(쿼리 함수가 오류를 던지면) TanStack Query는 해당 요청이 연속 재시도 최대 횟수(기본값 )에 도달하지 않았거나 재시도 허용 여부를 결정하는 함수를 제공한 경우 자동으로 쿼리를 다시 시도합니다.'
---

# 쿼리 재시도

`useQuery` 쿼리가 실패하면(쿼리 함수가 오류를 던지면) TanStack Query는 해당 요청이 연속 재시도 최대 횟수(기본값 `3`)에 도달하지 않았거나 재시도 허용 여부를 결정하는 함수를 제공한 경우 자동으로 쿼리를 다시 시도합니다.

전역 수준과 개별 쿼리 수준 모두에서 재시도를 구성할 수 있습니다.

- `retry = false`로 설정하면 재시도를 비활성화합니다.
- `retry = 6`으로 설정하면 함수가 던진 최종 오류를 표시하기 전에 실패한 요청을 6번 재시도합니다.
- `retry = true`로 설정하면 실패한 요청을 무한히 재시도합니다.
- `retry = (failureCount, error) => ...`로 설정하면 요청이 실패한 이유에 따른 사용자 지정 로직을 구현할 수 있습니다. `failureCount`는 첫 번째 재시도 시도에서 `0`부터 시작합니다.

[//]: # 'Info'

> 서버에서는 서버 렌더링을 가능한 한 빠르게 하기 위해 재시도 기본값이 `0`입니다.

[//]: # 'Info'
[//]: # 'Example'

```tsx
import { useQuery } from '@tanstack/react-query'

// Make a specific query retry a certain number of times
const result = useQuery({
  queryKey: ['todos', 1],
  queryFn: fetchTodoListPage,
  retry: 10, // Will retry failed requests 10 times before displaying an error
})
```

[//]: # 'Example'

> 정보: `error` 속성의 내용은 마지막 재시도 시도 전까지 `useQuery` 응답의 `failureReason` 속성에 포함됩니다. 따라서 위 예시에서 오류가 지속되면 처음 9번의 재시도(총 10회 시도) 동안 오류 내용은 `failureReason` 속성에 속하며, 모든 재시도가 끝난 후에도 오류가 계속되면 마지막 시도 이후 `error`에 포함됩니다.

## 재시도 지연

기본적으로 TanStack Query의 재시도는 요청이 실패하자마자 수행되지 않습니다. 표준대로 각 재시도 시도에 점진적으로 백오프 지연이 적용됩니다.

기본 `retryDelay`는 각 시도마다 두 배로 증가하지만(시작값 `1000`ms) 30초를 넘지 않습니다:

[//]: # 'Example2'

```tsx
// Configure for all queries
import {
  QueryCache,
  QueryClient,
  QueryClientProvider,
} from '@tanstack/react-query'

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retryDelay: (attemptIndex) => Math.min(1000 * 2 ** attemptIndex, 30000),
    },
  },
})

function App() {
  return <QueryClientProvider client={queryClient}>...</QueryClientProvider>
}
```

[//]: # 'Example2'

권장되지는 않지만 Provider와 개별 쿼리 옵션 모두에서 `retryDelay` 함수/정수를 재정의할 수 있습니다. 함수를 대신해 정수를 설정하면 지연 시간은 항상 동일합니다:

[//]: # 'Example3'

```tsx
const result = useQuery({
  queryKey: ['todos'],
  queryFn: fetchTodoList,
  retryDelay: 1000, // Will always wait 1000ms to retry, regardless of how many retries
})
```

[//]: # 'Example3'

## 백그라운드 재시도 동작

`refetchInterval`과 함께 `refetchIntervalInBackground: true`를 사용할 때 브라우저 탭이 비활성화되면 재시도가 일시 중지됩니다. 이는 재시도가 일반 refetch와 동일한 포커스 동작을 따르기 때문입니다.

백그라운드에서 연속 재시도가 필요하다면 재시도를 비활성화하고 사용자 지정 refetch 전략을 구현하는 것을 고려하세요:

[//]: # 'Example4'

```tsx
const result = useQuery({
  queryKey: ['todos'],
  queryFn: fetchTodos,
  refetchInterval: (query) => {
    // Refetch more frequently when in error state
    return query.state.status === 'error' ? 5000 : 30000
  },
  refetchIntervalInBackground: true,
  retry: false, // Disable built-in retries
})
```

[//]: # 'Example4'

이 접근 방식은 백그라운드에서 refetch를 유지하면서 재시도 타이밍을 직접 제어할 수 있게 해줍니다.

