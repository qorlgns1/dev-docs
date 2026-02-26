---
title: 'Mutation 응답으로부터의 업데이트'
description: '서버에서 객체를 업데이트하는 뮤테이션을 다룰 때, 새 객체가 뮤테이션 응답으로 자동 반환되는 경우가 흔합니다. 해당 항목의 쿼리를 다시 패치하여 이미 보유한 데이터를 위해 네트워크 호출을 낭비하기보다는, 뮤테이션 함수가 반환한 객체를 활용해 Query Client의  ...'
---

# Mutation 응답으로부터의 업데이트

서버에서 객체를 **업데이트**하는 뮤테이션을 다룰 때, 새 객체가 뮤테이션 응답으로 자동 반환되는 경우가 흔합니다. 해당 항목의 쿼리를 다시 패치하여 이미 보유한 데이터를 위해 네트워크 호출을 낭비하기보다는, 뮤테이션 함수가 반환한 객체를 활용해 [Query Client의 `setQueryData`](https://tanstack.com/query/latest/docs/reference/QueryClient.md#queryclientsetquerydata) 메서드로 기존 쿼리를 즉시 새 데이터로 갱신할 수 있습니다.

[//]: # 'Example'

```tsx
const queryClient = useQueryClient()

const mutation = useMutation({
  mutationFn: editTodo,
  onSuccess: (data) => {
    queryClient.setQueryData(['todo', { id: 5 }], data)
  },
})

mutation.mutate({
  id: 5,
  name: 'Do the laundry',
})

// The query below will be updated with the response from the
// successful mutation
const { status, data, error } = useQuery({
  queryKey: ['todo', { id: 5 }],
  queryFn: fetchTodoById,
})
```

[//]: # 'Example'

`onSuccess` 로직을 재사용 가능한 뮤테이션에 연결하고 싶다면, 다음과 같이 커스텀 훅을 생성할 수 있습니다.

[//]: # 'Example2'

```tsx
const useMutateTodo = () => {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: editTodo,
    // Notice the second argument is the variables object that the `mutate` function receives
    onSuccess: (data, variables) => {
      queryClient.setQueryData(['todo', { id: variables.id }], data)
    },
  })
}
```

[//]: # 'Example2'

## 불변성

`setQueryData`를 통한 업데이트는 _불변_ 방식으로 수행해야 합니다. 캐시에서 가져온 데이터를 제자리에서 변경하여 캐시에 직접 쓰려는 시도는 **절대 금지**입니다. 처음에는 잘 작동하는 것처럼 보여도 결국 미묘한 버그로 이어질 수 있습니다.

[//]: # 'Example3'

```tsx
queryClient.setQueryData(['posts', { id }], (oldData) => {
  if (oldData) {
    // ❌ do not try this
    oldData.title = 'my new post title'
  }
  return oldData
})

queryClient.setQueryData(
  ['posts', { id }],
  // ✅ this is the way
  (oldData) =>
    oldData
      ? {
          ...oldData,
          title: 'my new post title',
        }
      : oldData,
)
```

[//]: # 'Example3'

