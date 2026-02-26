---
title: '낙관적 업데이트'
description: '이 작업은 add-doc 스킬의 전체 워크플로(원문 fetch, SEO frontmatter, 배포 등)와 맞지 않아 사용하지 않았습니다.'
---

이 작업은 add-doc 스킬의 전체 워크플로(원문 fetch, SEO frontmatter, 배포 등)와 맞지 않아 사용하지 않았습니다.

# 낙관적 업데이트

React Query는 뮤테이션이 완료되기 전에 UI를 낙관적으로 업데이트하는 두 가지 방법을 제공합니다. `onMutate` 옵션을 사용해 캐시를 직접 업데이트하거나, `useMutation` 결과에서 반환된 `variables`를 활용해 UI를 업데이트할 수 있습니다.

## UI를 통한 방법

이 방식은 캐시와 직접 상호작용하지 않기 때문에 더 간단합니다.

[//]: # 'ExampleUI1'

```tsx
const addTodoMutation = useMutation({
  mutationFn: (newTodo: string) => axios.post('/api/data', { text: newTodo }),
  // make sure to _return_ the Promise from the query invalidation
  // so that the mutation stays in `pending` state until the refetch is finished
  onSettled: () => queryClient.invalidateQueries({ queryKey: ['todos'] }),
})

const { isPending, submittedAt, variables, mutate, isError } = addTodoMutation
```

[//]: # 'ExampleUI1'

이제 추가된 todo가 들어 있는 `addTodoMutation.variables`에 접근할 수 있습니다. 쿼리가 렌더링되는 UI 목록에서, 뮤테이션이 `isPending` 상태인 동안 목록에 다른 항목을 추가할 수 있습니다.

[//]: # 'ExampleUI2'

```tsx
<ul>
  {todoQuery.items.map((todo) => (
    <li key={todo.id}>{todo.text}</li>
  ))}
  {isPending && <li style={{ opacity: 0.5 }}>{variables}</li>}
</ul>
```

[//]: # 'ExampleUI2'

뮤테이션이 진행 중일 때는 다른 `opacity`로 임시 항목을 렌더링합니다. 완료되면 해당 항목은 자동으로 렌더링되지 않습니다. 리패치가 성공했다면, 목록에서 그 항목을 “정상 항목”으로 확인할 수 있습니다.

뮤테이션이 에러를 내면 항목도 사라집니다. 하지만 원한다면 뮤테이션의 `isError` 상태를 확인해서 계속 보여줄 수도 있습니다. 뮤테이션이 에러로 끝나도 `variables`는 _지워지지 않으므로_, 여전히 접근해 재시도 버튼을 보여줄 수도 있습니다.

[//]: # 'ExampleUI3'

```tsx
{
  isError && (
    <li style={{ color: 'red' }}>
      {variables}
      <button onClick={() => mutate(variables)}>Retry</button>
    </li>
  )
}
```

[//]: # 'ExampleUI3'

### 뮤테이션과 쿼리가 동일한 컴포넌트에 없을 때

이 접근법은 뮤테이션과 쿼리가 같은 컴포넌트에 있을 때 아주 잘 동작합니다. 하지만 전용 `useMutationState` 훅을 통해 다른 컴포넌트의 모든 뮤테이션에도 접근할 수 있습니다. `mutationKey`와 함께 사용하면 가장 좋습니다.

[//]: # 'ExampleUI4'

```tsx
// somewhere in your app
const { mutate } = useMutation({
  mutationFn: (newTodo: string) => axios.post('/api/data', { text: newTodo }),
  onSettled: () => queryClient.invalidateQueries({ queryKey: ['todos'] }),
  mutationKey: ['addTodo'],
})

// access variables somewhere else
const variables = useMutationState<string>({
  filters: { mutationKey: ['addTodo'], status: 'pending' },
  select: (mutation) => mutation.state.variables,
})
```

[//]: # 'ExampleUI4'

동시에 여러 뮤테이션이 실행될 수 있으므로 `variables`는 `Array`가 됩니다. 항목에 고유 키가 필요하다면 `mutation.state.submittedAt`을 선택하면 됩니다. 그러면 동시 낙관적 업데이트를 표시하는 것도 아주 쉬워집니다.

## 캐시를 통한 방법

뮤테이션을 수행하기 전에 상태를 낙관적으로 업데이트하면 뮤테이션이 실패할 가능성이 있습니다. 대부분의 실패 사례에서는 낙관적 쿼리를 리패치해 서버의 실제 상태로 되돌릴 수 있습니다. 하지만 때로는 리패치가 제대로 되지 않거나, 뮤테이션 에러가 리패치를 불가능하게 만드는 서버 문제를 의미할 수도 있습니다. 이때는 업데이트를 롤백하는 선택을 할 수 있습니다.

이를 위해 `useMutation`의 `onMutate` 핸들러 옵션은 값을 반환할 수 있게 해주며, 이 값은 나중에 `onError`와 `onSettled` 핸들러에 마지막 인수로 전달됩니다. 대부분의 경우 롤백 함수를 전달하는 것이 가장 유용합니다.

### 새 todo를 추가할 때 todo 목록 업데이트하기

[//]: # 'Example'

```tsx
const queryClient = useQueryClient()

useMutation({
  mutationFn: updateTodo,
  // When mutate is called:
  onMutate: async (newTodo, context) => {
    // Cancel any outgoing refetches
    // (so they don't overwrite our optimistic update)
    await context.client.cancelQueries({ queryKey: ['todos'] })

    // Snapshot the previous value
    const previousTodos = context.client.getQueryData(['todos'])

    // Optimistically update to the new value
    context.client.setQueryData(['todos'], (old) => [...old, newTodo])

    // Return a result with the snapshotted value
    return { previousTodos }
  },
  // If the mutation fails,
  // use the result returned from onMutate to roll back
  onError: (err, newTodo, onMutateResult, context) => {
    context.client.setQueryData(['todos'], onMutateResult.previousTodos)
  },
  // Always refetch after error or success:
  onSettled: (data, error, variables, onMutateResult, context) =>
    context.client.invalidateQueries({ queryKey: ['todos'] }),
})
```

[//]: # 'Example'

### 단일 todo 업데이트하기

[//]: # 'Example2'

```tsx
useMutation({
  mutationFn: updateTodo,
  // When mutate is called:
  onMutate: async (newTodo, context) => {
    // Cancel any outgoing refetches
    // (so they don't overwrite our optimistic update)
    await context.client.cancelQueries({ queryKey: ['todos', newTodo.id] })

    // Snapshot the previous value
    const previousTodo = context.client.getQueryData(['todos', newTodo.id])

    // Optimistically update to the new value
    context.client.setQueryData(['todos', newTodo.id], newTodo)

    // Return a result with the previous and new todo
    return { previousTodo, newTodo }
  },
  // If the mutation fails, use the result we returned above
  onError: (err, newTodo, onMutateResult, context) => {
    context.client.setQueryData(
      ['todos', onMutateResult.newTodo.id],
      onMutateResult.previousTodo,
    )
  },
  // Always refetch after error or success:
  onSettled: (newTodo, error, variables, onMutateResult, context) =>
    context.client.invalidateQueries({ queryKey: ['todos', newTodo.id] }),
})
```

[//]: # 'Example2'

원한다면 별도의 `onError`와 `onSuccess` 핸들러 대신 `onSettled` 함수를 사용할 수도 있습니다.

[//]: # 'Example3'

```tsx
useMutation({
  mutationFn: updateTodo,
  // ...
  onSettled: async (newTodo, error, variables, onMutateResult, context) => {
    if (error) {
      // do something
    }
  },
})
```

[//]: # 'Example3'

## 언제 어떤 방법을 사용할까

낙관적 결과를 보여줘야 하는 곳이 하나뿐이라면, `variables`를 사용해 UI를 직접 업데이트하는 방식이 코드량이 적고 이해하기도 쉽습니다. 예를 들어, 롤백을 전혀 처리할 필요가 없습니다.

하지만 화면 곳곳에서 업데이트 정보를 알아야 한다면 캐시를 직접 조작하는 방식이 자동으로 이를 처리해 줍니다.

[//]: # 'Materials'

## 추가 자료

TkDodo의 [Concurrent Optimistic Updates](https://tkdodo.eu/blog/concurrent-optimistic-updates-in-react-query) 가이드를 살펴보세요.

[//]: # 'Materials'

