---
title: '빠른 시작'
description: '이 코드 스니펫은 React Query의 3가지 핵심 개념을 매우 간단히 보여줍니다:'
---

# 빠른 시작

이 코드 스니펫은 React Query의 3가지 핵심 개념을 매우 간단히 보여줍니다:

- [Queries](https://tanstack.com/query/latest/docs/framework/react/guides/queries.md)
- [Mutations](https://tanstack.com/query/latest/docs/framework/react/guides/mutations.md)
- [Query Invalidation](https://tanstack.com/query/latest/docs/framework/react/guides/query-invalidation.md)

[//]: # 'Example'

완전히 동작하는 예제를 찾고 있다면 [간단한 StackBlitz 예제](https://tanstack.com/query/latest/docs/framework/react/examples/simple)를 확인해 주세요.

```tsx
import {
  useQuery,
  useMutation,
  useQueryClient,
  QueryClient,
  QueryClientProvider,
} from '@tanstack/react-query'
import { getTodos, postTodo } from '../my-api'

// Create a client
const queryClient = new QueryClient()

function App() {
  return (
    // Provide the client to your App
    <QueryClientProvider client={queryClient}>
      <Todos />
    </QueryClientProvider>
  )
}

function Todos() {
  // Access the client
  const queryClient = useQueryClient()

  // Queries
  const query = useQuery({ queryKey: ['todos'], queryFn: getTodos })

  // Mutations
  const mutation = useMutation({
    mutationFn: postTodo,
    onSuccess: () => {
      // Invalidate and refetch
      queryClient.invalidateQueries({ queryKey: ['todos'] })
    },
  })

  return (
    <div>
      <ul>
        {query.data?.map((todo) => (
          <li key={todo.id}>{todo.title}</li>
        ))}
      </ul>

      <button
        onClick={() => {
          mutation.mutate({
            id: Date.now(),
            title: 'Do Laundry',
          })
        }}
      >
        Add Todo
      </button>
    </div>
  )
}

render(<App />, document.getElementById('root'))
```

[//]: # 'Example'

이 세 가지 개념이 React Query 핵심 기능의 대부분을 구성합니다. 다음 문서 섹션에서는 이러한 핵심 개념 각각을 매우 자세히 다룹니다.

