---
title: 'Query Functions'
description: '쿼리 함수는 프로미스를 반환하기만 하면 되는 어떤 함수든 가능합니다. 반환된 프로미스는 데이터를 resolve하거나 에러를 던져야 합니다.'
---

# Query Functions

쿼리 함수는 **프로미스를 반환**하기만 하면 되는 어떤 함수든 가능합니다. 반환된 프로미스는 데이터를 **resolve**하거나 **에러를 던져야** 합니다.

다음은 모두 유효한 쿼리 함수 구성입니다.

[//]: # 'Example'

```tsx
useQuery({ queryKey: ['todos'], queryFn: fetchAllTodos })
useQuery({ queryKey: ['todos', todoId], queryFn: () => fetchTodoById(todoId) })
useQuery({
  queryKey: ['todos', todoId],
  queryFn: async () => {
    const data = await fetchTodoById(todoId)
    return data
  },
})
useQuery({
  queryKey: ['todos', todoId],
  queryFn: ({ queryKey }) => fetchTodoById(queryKey[1]),
})
```

[//]: # 'Example'

## 오류 처리 및 던지기

쿼리가 오류 상태라는 것을 TanStack Query가 판단하려면 쿼리 함수가 반드시 **예외를 던지거나** **거부된 프로미스**를 반환해야 합니다. 쿼리 함수에서 던져지는 모든 에러는 쿼리의 `error` 상태에 저장됩니다.

[//]: # 'Example2'

```tsx
const { error } = useQuery({
  queryKey: ['todos', todoId],
  queryFn: async () => {
    if (somethingGoesWrong) {
      throw new Error('Oh no!')
    }
    if (somethingElseGoesWrong) {
      return Promise.reject(new Error('Oh no!'))
    }

    return data
  },
})
```

[//]: # 'Example2'

## 기본적으로 예외를 던지지 않는 `fetch` 및 기타 클라이언트 사용

`axios`나 `graphql-request` 같은 대부분의 유틸리티는 실패한 HTTP 호출에 대해 자동으로 예외를 던지지만, `fetch`와 같은 일부 유틸리티는 기본적으로 예외를 던지지 않습니다. 그런 경우 직접 예외를 던져야 합니다. 아래는 널리 사용되는 `fetch` API로 이를 처리하는 간단한 방법입니다.

[//]: # 'Example3'

```tsx
useQuery({
  queryKey: ['todos', todoId],
  queryFn: async () => {
    const response = await fetch('/todos/' + todoId)
    if (!response.ok) {
      throw new Error('Network response was not ok')
    }
    return response.json()
  },
})
```

[//]: # 'Example3'

## 쿼리 함수 변수

쿼리 키는 가져오는 데이터를 고유하게 식별하는 용도뿐 아니라 QueryFunctionContext의 일부로 쿼리 함수에 전달됩니다. 반드시 필요한 것은 아니지만, 필요하다면 쿼리 함수를 분리할 수 있도록 해 줍니다.

[//]: # 'Example4'

```tsx
function Todos({ status, page }) {
  const result = useQuery({
    queryKey: ['todos', { status, page }],
    queryFn: fetchTodoList,
  })
}

// Access the key, status and page variables in your query function!
function fetchTodoList({ queryKey }) {
  const [_key, { status, page }] = queryKey
  return new Promise()
}
```

[//]: # 'Example4'

### QueryFunctionContext

`QueryFunctionContext`는 각 쿼리 함수에 전달되는 객체이며 다음으로 구성됩니다.

- `queryKey: QueryKey`: [Query Keys](https://tanstack.com/query/latest/docs/framework/react/guides/query-keys.md)
- `client: QueryClient`: [QueryClient](https://tanstack.com/query/latest/docs/reference/QueryClient.md)
- `signal?: AbortSignal`
  - TanStack Query가 제공하는 [AbortSignal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) 인스턴스
  - [Query Cancellation](https://tanstack.com/query/latest/docs/framework/react/guides/query-cancellation.md)에 사용할 수 있습니다.
- `meta: Record<string, unknown> | undefined`
  - 쿼리에 대한 추가 정보를 담을 수 있는 선택 필드

또한 [Infinite Queries](https://tanstack.com/query/latest/docs/framework/react/guides/infinite-queries.md)는 다음 옵션을 전달받습니다.

- `pageParam: TPageParam`
  - 현재 페이지를 가져오는 데 사용되는 페이지 매개변수
- `direction: 'forward' | 'backward'`
  - **사용 중단(deprecated)**
  - 현재 페이지 가져오기의 진행 방향
  - 현재 페이지 진행 방향이 필요하다면 `getNextPageParam`과 `getPreviousPageParam`에서 반환하는 `pageParam`에 방향 정보를 추가하세요.

