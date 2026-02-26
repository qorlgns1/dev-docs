---
title: '쿼리 취소'
description: 'TanStack Query는 각 쿼리 함수에  인스턴스를 제공합니다. 쿼리가 오래되거나 비활성화되면 이 이 중단(abort)됩니다. 이는 모든 쿼리가 취소 가능함을 의미하며, 필요하다면 쿼리 함수 내부에서 취소에 대응할 수 있습니다. 가장 좋은 점은, 자동 취소의 모든...'
---

# 쿼리 취소

TanStack Query는 각 쿼리 함수에 [`AbortSignal` 인스턴스](https://developer.mozilla.org/docs/Web/API/AbortSignal)를 제공합니다. 쿼리가 오래되거나 비활성화되면 이 `signal`이 중단(abort)됩니다. 이는 모든 쿼리가 취소 가능함을 의미하며, 필요하다면 쿼리 함수 내부에서 취소에 대응할 수 있습니다. 가장 좋은 점은, 자동 취소의 모든 이점을 누리면서도 기존의 async/await 구문을 그대로 사용할 수 있다는 것입니다.

`AbortController` API는 [대부분의 런타임 환경](https://developer.mozilla.org/docs/Web/API/AbortController#browser_compatibility)에서 사용할 수 있지만, 런타임 환경이 이를 지원하지 않는다면 폴리필을 제공해야 합니다. [여러 폴리필](https://www.npmjs.com/search?q=abortcontroller%20polyfill)이 준비되어 있습니다.

## 기본 동작

기본적으로, 프로미스가 해결되기 전에 쿼리가 언마운트되거나 사용되지 않게 되더라도 _취소되지 않습니다_. 즉, 프로미스가 해결된 후에는 결과 데이터가 캐시에 남아 있습니다. 쿼리를 시작했지만 완료되기 전에 컴포넌트를 언마운트한 경우에 유용합니다. 컴포넌트를 다시 마운트했을 때 쿼리가 아직 가비지 컬렉션되지 않았다면 데이터를 사용할 수 있습니다.

그러나 `AbortSignal`을 소비하면 프로미스가 취소되고(예: fetch 중단), 따라서 쿼리도 취소되어야 합니다. 쿼리를 취소하면 상태가 이전 상태로 _되돌려_ 집니다.

## `fetch` 사용하기

[//]: # 'Example'

```tsx
const query = useQuery({
  queryKey: ['todos'],
  queryFn: async ({ signal }) => {
    const todosResponse = await fetch('/todos', {
      // Pass the signal to one fetch
      signal,
    })
    const todos = await todosResponse.json()

    const todoDetails = todos.map(async ({ details }) => {
      const response = await fetch(details, {
        // Or pass it to several
        signal,
      })
      return response.json()
    })

    return Promise.all(todoDetails)
  },
})
```

[//]: # 'Example'

## `axios` [v0.22.0+](https://github.com/axios/axios/releases/tag/v0.22.0) 사용하기

[//]: # 'Example2'

```tsx
import axios from 'axios'

const query = useQuery({
  queryKey: ['todos'],
  queryFn: ({ signal }) =>
    axios.get('/todos', {
      // Pass the signal to `axios`
      signal,
    }),
})
```

[//]: # 'Example2'

### v0.22.0 미만 버전의 `axios` 사용하기

[//]: # 'Example3'

```tsx
import axios from 'axios'

const query = useQuery({
  queryKey: ['todos'],
  queryFn: ({ signal }) => {
    // Create a new CancelToken source for this request
    const CancelToken = axios.CancelToken
    const source = CancelToken.source()

    const promise = axios.get('/todos', {
      // Pass the source token to your request
      cancelToken: source.token,
    })

    // Cancel the request if TanStack Query signals to abort
    signal?.addEventListener('abort', () => {
      source.cancel('Query was cancelled by TanStack Query')
    })

    return promise
  },
})
```

[//]: # 'Example3'

## `XMLHttpRequest` 사용하기

[//]: # 'Example4'

```tsx
const query = useQuery({
  queryKey: ['todos'],
  queryFn: ({ signal }) => {
    return new Promise((resolve, reject) => {
      var oReq = new XMLHttpRequest()
      oReq.addEventListener('load', () => {
        resolve(JSON.parse(oReq.responseText))
      })
      signal?.addEventListener('abort', () => {
        oReq.abort()
        reject()
      })
      oReq.open('GET', '/todos')
      oReq.send()
    })
  },
})
```

[//]: # 'Example4'

## `graphql-request` 사용하기

`request` 메서드에서 `AbortSignal`을 설정할 수 있습니다.

[//]: # 'Example5'

```tsx
const client = new GraphQLClient(endpoint)

const query = useQuery({
  queryKey: ['todos'],
  queryFn: ({ signal }) => {
    client.request({ document: query, signal })
  },
})
```

[//]: # 'Example5'

## v4.0.0 미만 버전의 `graphql-request` 사용하기

`GraphQLClient` 생성자에서 `AbortSignal`을 설정할 수 있습니다.

[//]: # 'Example6'

```tsx
const query = useQuery({
  queryKey: ['todos'],
  queryFn: ({ signal }) => {
    const client = new GraphQLClient(endpoint, {
      signal,
    })
    return client.request(query, variables)
  },
})
```

[//]: # 'Example6'

## 수동 취소

쿼리를 수동으로 취소하고 싶을 때가 있을 수 있습니다. 예를 들어 요청이 완료되기까지 오래 걸린다면, 사용자가 취소 버튼을 눌러 요청을 중단하도록 허용할 수 있습니다. 이를 위해서는 `queryClient.cancelQueries({ queryKey })`를 호출하기만 하면 되며, 이 호출은 쿼리를 취소하고 이전 상태로 되돌립니다. 쿼리 함수에 전달된 `signal`을 소비한 경우, TanStack Query는 프로미스 또한 추가로 취소합니다.

[//]: # 'Example7'

```tsx
const query = useQuery({
  queryKey: ['todos'],
  queryFn: async ({ signal }) => {
    const resp = await fetch('/todos', { signal })
    return resp.json()
  },
})

const queryClient = useQueryClient()

return (
  <button
    onClick={(e) => {
      e.preventDefault()
      queryClient.cancelQueries({ queryKey: ['todos'] })
    }}
  >
    Cancel
  </button>
)
```

[//]: # 'Example7'

## `Cancel Options`

취소 옵션은 쿼리 취소 동작을 제어하는 데 사용됩니다.

```tsx
// Cancel specific queries silently
await queryClient.cancelQueries({ queryKey: ['posts'] }, { silent: true })
```

취소 옵션 객체는 다음 속성을 지원합니다.

- `silent?: boolean`
  - `true`로 설정하면 관찰자(예: `onError` 콜백)와 관련 알림으로의 `CancelledError` 전파를 억제하고, 거부 대신 재시도 프로미스를 반환합니다.
  - 기본값은 `false`입니다.
- `revert?: boolean`
  - `true`로 설정하면 진행 중인 fetch 직전의 상태(데이터와 상태)를 복원하고, `fetchStatus`를 다시 `idle`로 설정하며, 이전 데이터가 없을 때만 예외를 던집니다.
  - 기본값은 `true`입니다.

## 제한 사항

`Suspense` 훅(`useSuspenseQuery`, `useSuspenseQueries`, `useSuspenseInfiniteQuery`)을 사용할 때는 취소가 작동하지 않습니다.

