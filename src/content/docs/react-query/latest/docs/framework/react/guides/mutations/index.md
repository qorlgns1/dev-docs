---
title: '변이(Mutations)'
description: '쿼리와 달리, 변이는 일반적으로 데이터를 생성·업데이트·삭제하거나 서버 부수 효과를 수행할 때 사용합니다. 이를 위해 TanStack Query는  훅을 제공합니다.'
---

# 변이(Mutations)

쿼리와 달리, 변이는 일반적으로 데이터를 생성·업데이트·삭제하거나 서버 부수 효과를 수행할 때 사용합니다. 이를 위해 TanStack Query는 `useMutation` 훅을 제공합니다.

다음은 서버에 새 todo를 추가하는 변이 예시입니다:

[//]: # 'Example'

```tsx
function App() {
  const mutation = useMutation({
    mutationFn: (newTodo) => {
      return axios.post('/todos', newTodo)
    },
  })

  return (
    <div>
      {mutation.isPending ? (
        'Adding todo...'
      ) : (
        <>
          {mutation.isError ? (
            <div>An error occurred: {mutation.error.message}</div>
          ) : null}

          {mutation.isSuccess ? <div>Todo added!</div> : null}

          <button
            onClick={() => {
              mutation.mutate({ id: new Date(), title: 'Do Laundry' })
            }}
          >
            Create Todo
          </button>
        </>
      )}
    </div>
  )
}
```

[//]: # 'Example'

변이는 어느 순간이든 다음 상태 중 하나만 가질 수 있습니다:

- `isIdle` 또는 `status === 'idle'` - 변이가 현재 유휴 상태이거나 초기화/재설정된 상태
- `isPending` 또는 `status === 'pending'` - 변이가 현재 실행 중
- `isError` 또는 `status === 'error'` - 변이 실행 중 오류 발생
- `isSuccess` 또는 `status === 'success'` - 변이가 성공했으며 변이 데이터 사용 가능

이러한 기본 상태 외에도, 변이 상태에 따라 더 많은 정보를 확인할 수 있습니다:

- `error` - 변이가 `error` 상태라면 `error` 속성을 통해 오류에 접근할 수 있습니다.
- `data` - 변이가 `success` 상태라면 `data` 속성을 통해 데이터를 확인할 수 있습니다.

위 예시에서 볼 수 있듯, `mutate` 함수를 호출할 때 **단일 변수 또는 객체**를 전달해 변이 함수에 변수를 넘길 수 있습니다.

단순히 변수를 넘기는 것만으로는 특별할 것 없지만, `onSuccess` 옵션, [Query Client의 `invalidateQueries` 메서드](https://tanstack.com/query/latest/docs/reference/QueryClient.md#queryclientinvalidatequeries), [Query Client의 `setQueryData` 메서드](https://tanstack.com/query/latest/docs/reference/QueryClient.md#queryclientsetquerydata)와 함께 사용하면 변이는 매우 강력한 도구가 됩니다.

[//]: # 'Info1'

> 중요: `mutate` 함수는 비동기 함수이므로 **React 16 및 이전 버전**에서는 이벤트 콜백에서 직접 사용할 수 없습니다. `onSubmit`에서 이벤트에 접근해야 한다면 `mutate`를 다른 함수로 감싸야 합니다. 이는 [React 이벤트 풀링](https://reactjs.org/docs/legacy-event-pooling.html) 때문입니다.

[//]: # 'Info1'
[//]: # 'Example2'

```tsx
// This will not work in React 16 and earlier
const CreateTodo = () => {
  const mutation = useMutation({
    mutationFn: (event) => {
      event.preventDefault()
      return fetch('/api', new FormData(event.target))
    },
  })

  return <form onSubmit={mutation.mutate}>...</form>
}

// This will work
const CreateTodo = () => {
  const mutation = useMutation({
    mutationFn: (formData) => {
      return fetch('/api', formData)
    },
  })
  const onSubmit = (event) => {
    event.preventDefault()
    mutation.mutate(new FormData(event.target))
  }

  return <form onSubmit={onSubmit}>...</form>
}
```

[//]: # 'Example2'

## 변이 상태 초기화

때때로 변이 요청의 `error`나 `data`를 비워야 할 때가 있습니다. 이를 위해 `reset` 함수를 사용할 수 있습니다:

[//]: # 'Example3'

```tsx
const CreateTodo = () => {
  const [title, setTitle] = useState('')
  const mutation = useMutation({ mutationFn: createTodo })

  const onCreateTodo = (e) => {
    e.preventDefault()
    mutation.mutate({ title })
  }

  return (
    <form onSubmit={onCreateTodo}>
      {mutation.error && (
        <h5 onClick={() => mutation.reset()}>{mutation.error}</h5>
      )}
      <input
        type="text"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <br />
      <button type="submit">Create Todo</button>
    </form>
  )
}
```

[//]: # 'Example3'

## 변이 부수 효과

`useMutation`에는 변이 라이프사이클의 어느 시점에서든 간단하게 부수 효과를 처리할 수 있는 몇 가지 보조 옵션이 있습니다. 이는 [변이 이후 쿼리 무효화 및 재패치](https://tanstack.com/query/latest/docs/framework/react/guides/invalidations-from-mutations.md), [낙관적 업데이트](https://tanstack.com/query/latest/docs/framework/react/guides/optimistic-updates.md)에 모두 유용합니다.

[//]: # 'Example4'

```tsx
useMutation({
  mutationFn: addTodo,
  onMutate: (variables, context) => {
    // A mutation is about to happen!

    // Optionally return a result containing data to use when for example rolling back
    return { id: 1 }
  },
  onError: (error, variables, onMutateResult, context) => {
    // An error happened!
    console.log(`rolling back optimistic update with id ${onMutateResult.id}`)
  },
  onSuccess: (data, variables, onMutateResult, context) => {
    // Boom baby!
  },
  onSettled: (data, error, variables, onMutateResult, context) => {
    // Error or success... doesn't matter!
  },
})
```

[//]: # 'Example4'

각 콜백 함수에서 프로미스를 반환하면, 다음 콜백이 호출되기 전에 먼저 해당 프로미스를 `await` 합니다:

[//]: # 'Example5'

```tsx
useMutation({
  mutationFn: addTodo,
  onSuccess: async () => {
    console.log("I'm first!")
  },
  onSettled: async () => {
    console.log("I'm second!")
  },
})
```

[//]: # 'Example5'

`mutate`를 호출할 때 `useMutation`에 정의된 콜백 외에 **추가 콜백을 트리거**하고 싶을 수도 있습니다. 이는 컴포넌트별 부수 효과를 실행할 때 유용합니다. 이를 위해 변이 변수 뒤에 `mutate` 함수에 동일한 콜백 옵션을 전달할 수 있습니다. 지원되는 옵션은 `onSuccess`, `onError`, `onSettled`입니다. 단, 컴포넌트가 변이가 끝나기 _전에_ 언마운트되면 이러한 추가 콜백은 실행되지 않는다는 점을 기억하세요.

[//]: # 'Example6'

```tsx
useMutation({
  mutationFn: addTodo,
  onSuccess: (data, variables, onMutateResult, context) => {
    // I will fire first
  },
  onError: (error, variables, onMutateResult, context) => {
    // I will fire first
  },
  onSettled: (data, error, variables, onMutateResult, context) => {
    // I will fire first
  },
})

mutate(todo, {
  onSuccess: (data, variables, onMutateResult, context) => {
    // I will fire second!
  },
  onError: (error, variables, onMutateResult, context) => {
    // I will fire second!
  },
  onSettled: (data, error, variables, onMutateResult, context) => {
    // I will fire second!
  },
})
```

[//]: # 'Example6'

### 연속 변이

연속 변이를 처리할 때 `onSuccess`, `onError`, `onSettled` 콜백의 동작에는 약간의 차이가 있습니다. 이를 `mutate` 함수에 전달하면, 컴포넌트가 여전히 마운트된 경우에만 _한 번만_ 실행됩니다. 이는 `mutate` 함수가 호출될 때마다 변이 옵저버가 제거되었다가 다시 구독되기 때문입니다. 반면, `useMutation` 핸들러는 `mutate`가 호출될 때마다 실행됩니다.

> 대부분의 경우 `useMutation`에 전달하는 `mutationFn`은 비동기입니다. 이때 변이가 완료되는 순서는 `mutate` 함수 호출 순서와 다를 수 있다는 점을 유념하세요.

[//]: # 'Example7'

```tsx
useMutation({
  mutationFn: addTodo,
  onSuccess: (data, variables, onMutateResult, context) => {
    // Will be called 3 times
  },
})

const todos = ['Todo 1', 'Todo 2', 'Todo 3']
todos.forEach((todo) => {
  mutate(todo, {
    onSuccess: (data, variables, onMutateResult, context) => {
      // Will execute only once, for the last mutation (Todo 3),
      // regardless which mutation resolves first
    },
  })
})
```

[//]: # 'Example7'

## 프로미스

성공 시 해결되고 오류 시 throw되는 프로미스를 얻으려면 `mutate` 대신 `mutateAsync`를 사용하세요. 이를 통해 부수 효과를 조합할 수 있습니다.

[//]: # 'Example8'

```tsx
const mutation = useMutation({ mutationFn: addTodo })

try {
  const todo = await mutation.mutateAsync(todo)
  console.log(todo)
} catch (error) {
  console.error(error)
} finally {
  console.log('done')
}
```

[//]: # 'Example8'

## 재시도

기본적으로 TanStack Query는 오류 발생 시 변이를 재시도하지 않지만, `retry` 옵션을 사용하면 가능합니다:

[//]: # 'Example9'

```tsx
const mutation = useMutation({
  mutationFn: addTodo,
  retry: 3,
})
```

[//]: # 'Example9'

디바이스가 오프라인이라 변이가 실패한 경우, 디바이스가 다시 연결되면 동일한 순서로 재시도됩니다.

## 변이 영속화

필요하다면 변이를 스토리지에 영속화하고 나중에 재개할 수 있습니다. 이는 하이드레이션 함수로 처리합니다:

[//]: # 'Example10'

```tsx
const queryClient = new QueryClient()

// Define the "addTodo" mutation
queryClient.setMutationDefaults(['addTodo'], {
  mutationFn: addTodo,
  onMutate: async (variables, context) => {
    // Cancel current queries for the todos list
    await context.client.cancelQueries({ queryKey: ['todos'] })

    // Create optimistic todo
    const optimisticTodo = { id: uuid(), title: variables.title }

    // Add optimistic todo to todos list
    context.client.setQueryData(['todos'], (old) => [...old, optimisticTodo])

    // Return a result with the optimistic todo
    return { optimisticTodo }
  },
  onSuccess: (result, variables, onMutateResult, context) => {
    // Replace optimistic todo in the todos list with the result
    context.client.setQueryData(['todos'], (old) =>
      old.map((todo) =>
        todo.id === onMutateResult.optimisticTodo.id ? result : todo,
      ),
    )
  },
  onError: (error, variables, onMutateResult, context) => {
    // Remove optimistic todo from the todos list
    context.client.setQueryData(['todos'], (old) =>
      old.filter((todo) => todo.id !== onMutateResult.optimisticTodo.id),
    )
  },
  retry: 3,
})

// Start mutation in some component:
const mutation = useMutation({ mutationKey: ['addTodo'] })
mutation.mutate({ title: 'title' })

// If the mutation has been paused because the device is for example offline,
// Then the paused mutation can be dehydrated when the application quits:
const state = dehydrate(queryClient)

// The mutation can then be hydrated again when the application is started:
hydrate(queryClient, state)

// Resume the paused mutations:
queryClient.resumePausedMutations()
```

[//]: # 'Example10'

### 오프라인 변이 영속화

[persistQueryClient 플러그인](https://tanstack.com/query/latest/docs/framework/react/plugins/persistQueryClient.md)으로 오프라인 변이를 영속화한 경우, 기본 변이 함수를 제공하지 않으면 페이지를 새로고침했을 때 변이를 재개할 수 없습니다.

이는 기술적 제한 때문입니다. 외부 스토리지에 영속화할 때는 변이 상태만 저장되며, 함수는 직렬화할 수 없습니다. 하이드레이션 이후 변이를 트리거하는 컴포넌트가 마운트되어 있지 않을 수 있어 `resumePausedMutations` 호출 시 `No mutationFn found` 오류가 발생할 수 있습니다.

[//]: # 'Example11'

```tsx
const persister = createSyncStoragePersister({
  storage: window.localStorage,
})
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      gcTime: 1000 * 60 * 60 * 24, // 24 hours
    },
  },
})

// we need a default mutation function so that paused mutations can resume after a page reload
queryClient.setMutationDefaults(['todos'], {
  mutationFn: ({ id, data }) => {
    return api.updateTodo(id, data)
  },
})

export default function App() {
  return (
    <PersistQueryClientProvider
      client={queryClient}
      persistOptions={{ persister }}
      onSuccess={() => {
        // resume mutations after initial restore from localStorage was successful
        queryClient.resumePausedMutations()
      }}
    >
      <RestOfTheApp />
    </PersistQueryClientProvider>
  )
}
```

[//]: # 'Example11'

쿼리와 변이를 모두 다루는 포괄적인 [오프라인 예제](https://tanstack.com/query/latest/docs/framework/react/examples/offline)도 제공하고 있습니다.

## 변이 범위

기본적으로 모든 변이는 병렬로 실행됩니다. 동일한 변이의 `.mutate()`를 여러 번 호출해도 마찬가지입니다. 이를 방지하려면 변이에 `scope`와 `id`를 지정할 수 있습니다. 동일한 `scope.id`를 가진 변이는 직렬로 실행되며, 이미 해당 범위에서 진행 중인 변이가 있다면 트리거 시 `isPaused: true` 상태로 시작합니다. 이들은 큐에 들어가고, 큐에서 자신의 차례가 되면 자동으로 재개됩니다.

[//]: # 'ExampleScopes'

```tsx
const mutation = useMutation({
  mutationFn: addTodo,
  scope: {
    id: 'todo',
  },
})
```

[//]: # 'ExampleScopes'
[//]: # 'Materials'

## 추가 자료

변이에 대해 더 알고 싶다면 [TkDodo의 React Query에서 Mutations 마스터하기](https://tkdodo.eu/blog/mastering-mutations-in-react-query) 글을 참고하세요.

[//]: # 'Materials'

