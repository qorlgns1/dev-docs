---
title: '서스펜스'
description: 'React Query는 React의 Data Fetching용 Suspense와도 함께 사용할 수 있습니다. 이를 위해 다음과 같은 전용 훅을 제공합니다:'
---

# 서스펜스

React Query는 React의 Data Fetching용 Suspense와도 함께 사용할 수 있습니다. 이를 위해 다음과 같은 전용 훅을 제공합니다:

- [useSuspenseQuery](https://tanstack.com/query/latest/docs/framework/react/reference/useSuspenseQuery.md)
- [useSuspenseInfiniteQuery](https://tanstack.com/query/latest/docs/framework/react/reference/useSuspenseInfiniteQuery.md)
- [useSuspenseQueries](https://tanstack.com/query/latest/docs/framework/react/reference/useSuspenseQueries.md)
- 추가로 `useQuery().promise`와 `React.use()`(Experimental)도 사용할 수 있습니다.

서스펜스 모드를 사용할 때는 `status` 상태 및 `error` 객체가 필요하지 않으며, 대신 `React.Suspense` 컴포넌트를 사용합니다(`fallback` prop 사용과 오류를 포착하기 위한 React 에러 바운더리 포함). 서스펜스 모드 설정 방법을 더 알아보려면 [Resetting Error Boundaries](#resetting-error-boundaries)를 읽고 [Suspense Example](https://tanstack.com/query/latest/docs/framework/react/examples/suspense)을 확인하세요.

뮤테이션에서 오류를 가장 가까운 에러 바운더리로 전파하고 싶다면(쿼리와 유사하게) `throwOnError` 옵션을 `true`로 설정하면 됩니다.

쿼리에서 서스펜스 모드를 활성화하기:

```tsx
import { useSuspenseQuery } from '@tanstack/react-query'

const { data } = useSuspenseQuery({ queryKey, queryFn })
```

이 방식은 TypeScript와도 잘 맞는데, 서스펜스와 ErrorBoundary가 오류와 로딩 상태를 처리하므로 `data`가 정의되어 있음이 보장되기 때문입니다.

반대로, 쿼리를 조건부로 활성화/비활성화할 수 없게 됩니다. 그러나 서스펜스를 사용하면 하나의 컴포넌트 안에 있는 모든 쿼리가 직렬로 가져오기 때문에 종속 쿼리에는 일반적으로 필요하지 않습니다.

이 쿼리에는 `placeholderData`도 존재하지 않습니다. 업데이트 중에 UI가 fallback으로 대체되는 것을 방지하려면, QueryKey를 변경하는 업데이트를 [startTransition](https://react.dev/reference/react/Suspense#preventing-unwanted-fallbacks)으로 감싸세요.

### throwOnError 기본값

모든 오류가 기본적으로 가장 가까운 Error Boundary에 던져지는 것은 아니며, 표시할 다른 데이터가 없을 때만 오류를 던집니다. 즉, 쿼리가 한 번이라도 캐시에 데이터를 성공적으로 가져왔다면, 데이터가 `stale`한 경우에도 컴포넌트는 렌더링됩니다. 따라서 `throwOnError`의 기본값은 다음과 같습니다:

```
throwOnError: (error, query) => typeof query.state.data === 'undefined'
```

`throwOnError`를 변경할 수 없기 때문에(그렇게 하면 `data`가 잠재적으로 `undefined`가 될 수 있음), 모든 오류를 Error Boundary에서 처리하고 싶다면 수동으로 오류를 던져야 합니다:

```tsx
import { useSuspenseQuery } from '@tanstack/react-query'

const { data, error, isFetching } = useSuspenseQuery({ queryKey, queryFn })

if (error && !isFetching) {
  throw error
}

// continue rendering data
```

## 에러 바운더리 재설정

쿼리에서 **suspense** 또는 **throwOnError**를 사용하든, 오류가 발생한 후 다시 렌더링할 때 재시도를 원한다는 사실을 쿼리에 알릴 방법이 필요합니다.

`QueryErrorResetBoundary` 컴포넌트나 `useQueryErrorResetBoundary` 훅으로 쿼리 오류를 재설정할 수 있습니다.

컴포넌트를 사용할 때는 해당 컴포넌트 경계 내의 모든 쿼리 오류가 재설정됩니다:

```tsx
import { QueryErrorResetBoundary } from '@tanstack/react-query'
import { ErrorBoundary } from 'react-error-boundary'

const App = () => (
  <QueryErrorResetBoundary>
    {({ reset }) => (
      <ErrorBoundary
        onReset={reset}
        fallbackRender={({ resetErrorBoundary }) => (
          <div>
            There was an error!
            <Button onClick={() => resetErrorBoundary()}>Try again</Button>
          </div>
        )}
      >
        <Page />
      </ErrorBoundary>
    )}
  </QueryErrorResetBoundary>
)
```

훅을 사용할 때는 가장 가까운 `QueryErrorResetBoundary` 내의 쿼리 오류가 재설정됩니다. 경계가 정의되지 않았다면 전역적으로 재설정됩니다:

```tsx
import { useQueryErrorResetBoundary } from '@tanstack/react-query'
import { ErrorBoundary } from 'react-error-boundary'

const App = () => {
  const { reset } = useQueryErrorResetBoundary()
  return (
    <ErrorBoundary
      onReset={reset}
      fallbackRender={({ resetErrorBoundary }) => (
        <div>
          There was an error!
          <Button onClick={() => resetErrorBoundary()}>Try again</Button>
        </div>
      )}
    >
      <Page />
    </ErrorBoundary>
  )
}
```

## Fetch-on-render vs Render-as-you-fetch

`fetch-on-render` 솔루션으로서 React Query는 기본 `suspense` 모드에서 추가 설정 없이도 매우 잘 동작합니다. 즉, 컴포넌트가 마운트되려고 할 때 쿼리 가져오기를 트리거하고 서스펜드하지만, 해당 컴포넌트를 가져와 마운트한 이후에만 실행됩니다. 한 단계 더 나아가 **render-as-you-fetch** 모델을 구현하고 싶다면, 라우팅 콜백 및/또는 사용자 상호작용 이벤트에서 [Prefetching](https://tanstack.com/query/latest/docs/framework/react/guides/prefetching.md)을 구현하여 쿼리가 마운트되기 전에, 더 나아가 부모 컴포넌트를 가져오거나 마운트하기도 전에 로딩을 시작하도록 권장합니다.

## 스트리밍이 있는 서버 사이드 서스펜스

`NextJs`를 사용한다면 서버에서의 Suspense를 위한 **experimental** 통합 패키지 `@tanstack/react-query-next-experimental`을 사용할 수 있습니다. 이 패키지는 클라이언트 컴포넌트에서 `useSuspenseQuery`를 호출하기만 하면 서버에서 데이터를 가져올 수 있게 해줍니다. SuspenseBoundary가 해제될 때 서버에서 클라이언트로 결과가 스트리밍됩니다.

이를 위해 앱을 `ReactQueryStreamedHydration` 컴포넌트로 감싸세요:

```tsx
// app/providers.tsx
'use client'

import {
  isServer,
  QueryClient,
  QueryClientProvider,
} from '@tanstack/react-query'
import * as React from 'react'
import { ReactQueryStreamedHydration } from '@tanstack/react-query-next-experimental'

function makeQueryClient() {
  return new QueryClient({
    defaultOptions: {
      queries: {
        // With SSR, we usually want to set some default staleTime
        // above 0 to avoid refetching immediately on the client
        staleTime: 60 * 1000,
      },
    },
  })
}

let browserQueryClient: QueryClient | undefined = undefined

function getQueryClient() {
  if (isServer) {
    // Server: always make a new query client
    return makeQueryClient()
  } else {
    // Browser: make a new query client if we don't already have one
    // This is very important, so we don't re-make a new client if React
    // suspends during the initial render. This may not be needed if we
    // have a suspense boundary BELOW the creation of the query client
    if (!browserQueryClient) browserQueryClient = makeQueryClient()
    return browserQueryClient
  }
}

export function Providers(props: { children: React.ReactNode }) {
  // NOTE: Avoid useState when initializing the query client if you don't
  //       have a suspense boundary between this and the code that may
  //       suspend because React will throw away the client on the initial
  //       render if it suspends and there is no boundary
  const queryClient = getQueryClient()

  return (
    <QueryClientProvider client={queryClient}>
      <ReactQueryStreamedHydration>
        {props.children}
      </ReactQueryStreamedHydration>
    </QueryClientProvider>
  )
}
```

자세한 내용은 [NextJs Suspense Streaming Example](https://tanstack.com/query/latest/docs/framework/react/examples/nextjs-suspense-streaming)과 [Advanced Rendering & Hydration](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr.md) 가이드를 확인하세요.

## `useQuery().promise`와 `React.use()` 사용(Experimental)

> 이 기능을 활성화하려면 `QueryClient`를 생성할 때 `experimental_prefetchInRender` 옵션을 `true`로 설정해야 합니다.

**예제 코드:**

```tsx
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      experimental_prefetchInRender: true,
    },
  },
})
```

**사용법:**

```tsx
import React from 'react'
import { useQuery } from '@tanstack/react-query'
import { fetchTodos, type Todo } from './api'

function TodoList({ query }: { query: UseQueryResult<Todo[]> }) {
  const data = React.use(query.promise)

  return (
    <ul>
      {data.map((todo) => (
        <li key={todo.id}>{todo.title}</li>
      ))}
    </ul>
  )
}

export function App() {
  const query = useQuery({ queryKey: ['todos'], queryFn: fetchTodos })

  return (
    <>
      <h1>Todos</h1>
      <React.Suspense fallback={<div>Loading...</div>}>
        <TodoList query={query} />
      </React.Suspense>
    </>
  )
}
```

더 완전한 예제는 [GitHub의 suspense example](https://github.com/TanStack/query/tree/main/examples/react/suspense)을 참고하세요.

Next.js 스트리밍 예제는 [GitHub의 nextjs-suspense-streaming example](https://github.com/TanStack/query/tree/main/examples/react/nextjs-suspense-streaming)을 참고하세요.

