---
title: 'QueryClient'
description: '는 캐시와 상호작용할 때 사용할 수 있습니다:'
---

Source URL: https://tanstack.com/query/latest/docs/reference/QueryClient

# QueryClient

## `QueryClient`

`QueryClient`는 캐시와 상호작용할 때 사용할 수 있습니다:

```tsx
import { QueryClient } from '@tanstack/react-query'

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: Infinity,
    },
  },
})

await queryClient.prefetchQuery({ queryKey: ['posts'], queryFn: fetchPosts })
```

사용 가능한 메서드는 다음과 같습니다:

- [`queryClient.fetchQuery`](#queryclientfetchquery)
- [`queryClient.fetchInfiniteQuery`](#queryclientfetchinfinitequery)
- [`queryClient.prefetchQuery`](#queryclientprefetchquery)
- [`queryClient.prefetchInfiniteQuery`](#queryclientprefetchinfinitequery)
- [`queryClient.getQueryData`](#queryclientgetquerydata)
- [`queryClient.ensureQueryData`](#queryclientensurequerydata)
- [`queryClient.ensureInfiniteQueryData`](#queryclientensureinfinitequerydata)
- [`queryClient.getQueriesData`](#queryclientgetqueriesdata)
- [`queryClient.setQueryData`](#queryclientsetquerydata)
- [`queryClient.getQueryState`](#queryclientgetquerystate)
- [`queryClient.setQueriesData`](#queryclientsetqueriesdata)
- [`queryClient.invalidateQueries`](#queryclientinvalidatequeries)
- [`queryClient.refetchQueries`](#queryclientrefetchqueries)
- [`queryClient.cancelQueries`](#queryclientcancelqueries)
- [`queryClient.removeQueries`](#queryclientremovequeries)
- [`queryClient.resetQueries`](#queryclientresetqueries)
- [`queryClient.isFetching`](#queryclientisfetching)
- [`queryClient.isMutating`](#queryclientismutating)
- [`queryClient.getDefaultOptions`](#queryclientgetdefaultoptions)
- [`queryClient.setDefaultOptions`](#queryclientsetdefaultoptions)
- [`queryClient.getQueryDefaults`](#queryclientgetquerydefaults)
- [`queryClient.setQueryDefaults`](#queryclientsetquerydefaults)
- [`queryClient.getMutationDefaults`](#queryclientgetmutationdefaults)
- [`queryClient.setMutationDefaults`](#queryclientsetmutationdefaults)
- [`queryClient.getQueryCache`](#queryclientgetquerycache)
- [`queryClient.getMutationCache`](#queryclientgetmutationcache)
- [`queryClient.clear`](#queryclientclear)
- [`queryClient.resumePausedMutations`](#queryclientresumepausedmutations)

**Options**

- `queryCache?: QueryCache`
  - 선택 사항
  - 이 클라이언트가 연결되는 쿼리 캐시입니다.
- `mutationCache?: MutationCache`
  - 선택 사항
  - 이 클라이언트가 연결되는 뮤테이션 캐시입니다.
- `defaultOptions?: DefaultOptions`
  - 선택 사항
  - 이 queryClient를 사용하는 모든 쿼리와 뮤테이션의 기본값을 정의합니다.
  - [hydration](https://tanstack.com/query/latest/docs/framework/react/reference/hydration.md)에 사용될 기본값을 정의할 수도 있습니다.

## `queryClient.fetchQuery`

`fetchQuery`는 쿼리를 가져와 캐시에 저장하는 비동기 메서드입니다. 데이터로 resolve되거나 에러로 throw합니다. 결과가 필요 없는 단순 선행 가져오기라면 `prefetchQuery`를 사용하세요.

쿼리가 존재하고 데이터가 무효화되지 않았거나 지정한 `staleTime`보다 오래되지 않았다면 캐시의 데이터가 반환됩니다. 그렇지 않으면 최신 데이터를 가져옵니다.

```tsx
try {
  const data = await queryClient.fetchQuery({ queryKey, queryFn })
} catch (error) {
  console.log(error)
}
```

`staleTime`을 지정해 데이터가 일정 시간 이상 오래됐을 때만 가져오도록 만들 수 있습니다:

```tsx
try {
  const data = await queryClient.fetchQuery({
    queryKey,
    queryFn,
    staleTime: 10000,
  })
} catch (error) {
  console.log(error)
}
```

**Options**

`fetchQuery` 옵션은 [`useQuery`](https://tanstack.com/query/latest/docs/framework/react/reference/useQuery.md)와 동일하지만, 다음 옵션은 제외됩니다: `enabled, refetchInterval, refetchIntervalInBackground, refetchOnWindowFocus, refetchOnReconnect, refetchOnMount, notifyOnChangeProps, throwOnError, select, suspense, placeholderData`; 이들은 useQuery와 useInfiniteQuery 전용입니다. 더 자세한 내용은 [소스 코드](https://github.com/TanStack/query/blob/7cd2d192e6da3df0b08e334ea1cf04cd70478827/packages/query-core/src/types.ts#L119)를 확인하세요.

**Returns**

- `Promise<TData>`

## `queryClient.fetchInfiniteQuery`

`fetchInfiniteQuery`는 `fetchQuery`와 비슷하지만 무한 쿼리를 가져와 캐시할 때 사용합니다.

```tsx
try {
  const data = await queryClient.fetchInfiniteQuery({ queryKey, queryFn })
  console.log(data.pages)
} catch (error) {
  console.log(error)
}
```

**Options**

`fetchInfiniteQuery` 옵션은 [`fetchQuery`](#queryclientfetchquery)와 동일합니다.

**Returns**

- `Promise<InfiniteData<TData, TPageParam>>`

## `queryClient.prefetchQuery`

`prefetchQuery`는 `useQuery` 등으로 필요하거나 렌더링되기 전에 쿼리를 미리 가져올 수 있는 비동기 메서드입니다. 동작은 `fetchQuery`와 같지만, 데이터를 반환하거나 에러를 throw하지 않습니다.

```tsx
await queryClient.prefetchQuery({ queryKey, queryFn })
```

설정에 기본 queryFn을 사용하면서도 활용할 수 있습니다!

```tsx
await queryClient.prefetchQuery({ queryKey })
```

**Options**

`prefetchQuery` 옵션은 [`fetchQuery`](#queryclientfetchquery)와 동일합니다.

**Returns**

- `Promise<void>`
  - 가져올 필요가 없으면 즉시, 쿼리를 실행해야 하면 완료 후 resolve되는 promise가 반환됩니다. 데이터를 반환하거나 에러를 throw하지 않습니다.

## `queryClient.prefetchInfiniteQuery`

`prefetchInfiniteQuery`는 `prefetchQuery`와 비슷하지만 무한 쿼리를 미리 가져와 캐시할 때 사용합니다.

```tsx
await queryClient.prefetchInfiniteQuery({ queryKey, queryFn })
```

**Options**

`prefetchInfiniteQuery` 옵션은 [`fetchQuery`](#queryclientfetchquery)와 동일합니다.

**Returns**

- `Promise<void>`
  - 가져올 필요가 없으면 즉시, 쿼리를 실행해야 하면 완료 후 resolve되는 promise가 반환됩니다. 데이터를 반환하거나 에러를 throw하지 않습니다.

## `queryClient.getQueryData`

`getQueryData`는 기존 쿼리의 캐시 데이터를 가져올 수 있는 동기 함수입니다. 쿼리가 없으면 `undefined`를 반환합니다.

```tsx
const data = queryClient.getQueryData(queryKey)
```

**Options**

- `queryKey: QueryKey`: [Query Keys](https://tanstack.com/query/latest/docs/framework/react/guides/query-keys.md)

**Returns**

- `data: TQueryFnData | undefined`
  - 캐시된 쿼리의 데이터이며, 쿼리가 없으면 `undefined`입니다.

## `queryClient.ensureQueryData`

`ensureQueryData`는 기존 쿼리의 캐시 데이터를 가져올 수 있는 비동기 함수입니다. 쿼리가 없으면 `queryClient.fetchQuery`를 호출하고 그 결과를 반환합니다.

```tsx
const data = await queryClient.ensureQueryData({ queryKey, queryFn })
```

**Options**

- [`fetchQuery`](#queryclientfetchquery)와 동일한 옵션
- `revalidateIfStale: boolean`
  - 선택 사항
  - 기본값은 `false`
  - `true`로 설정하면 데이터가 오래됐을 때 백그라운드에서 다시 가져오지만, 캐시된 데이터는 즉시 반환합니다.

**Returns**

- `Promise<TData>`

## `queryClient.ensureInfiniteQueryData`

`ensureInfiniteQueryData`는 기존 무한 쿼리의 캐시 데이터를 가져올 수 있는 비동기 함수입니다. 쿼리가 없으면 `queryClient.fetchInfiniteQuery`를 호출하고 그 결과를 반환합니다.

```tsx
const data = await queryClient.ensureInfiniteQueryData({
  queryKey,
  queryFn,
  initialPageParam,
  getNextPageParam,
})
```

**Options**

- [`fetchInfiniteQuery`](#queryclientfetchinfinitequery)와 동일한 옵션
- `revalidateIfStale: boolean`
  - 선택 사항
  - 기본값은 `false`
  - `true`로 설정하면 데이터가 오래됐을 때 백그라운드에서 다시 가져오지만, 캐시된 데이터는 즉시 반환합니다.

**Returns**

- `Promise<InfiniteData<TData, TPageParam>>`

## `queryClient.getQueriesData`

`getQueriesData`는 여러 쿼리의 캐시 데이터를 가져올 수 있는 동기 함수입니다. 전달된 queryKey나 queryFilter와 일치하는 쿼리만 반환하며, 일치 항목이 없으면 빈 배열을 반환합니다.

```tsx
const data = queryClient.getQueriesData(filters)
```

**Options**

- `filters: QueryFilters`: [Query Filters](https://tanstack.com/query/latest/docs/framework/react/guides/filters.md#query-filters)
  - 필터를 전달하면 queryKey가 필터와 일치하는 데이터가 반환됩니다.

**Returns**

- `[queryKey: QueryKey, data: TQueryFnData | undefined][]`
  - 일치하는 쿼리 키와 데이터로 구성된 튜플 배열이며, 일치 항목이 없으면 `[]`입니다. 각 튜플은 쿼리 키와 해당 데이터를 담습니다.

**Caveats**

각 튜플의 반환 데이터 구조가 다양할 수 있기 때문에(예: "active" 쿼리만 반환하는 필터는 서로 다른 데이터 타입을 포함할 수 있음) `TData` 제네릭은 기본적으로 `unknown`입니다. `TData`에 더 구체적 타입을 제공한다면, 모든 튜플의 데이터 항목이 동일한 타입이라고 가정하는 것입니다.

이 구분은 반환 구조를 알고 있는 TS 개발자를 위한 편의 기능에 가깝습니다.

## `queryClient.setQueryData`

`setQueryData`는 쿼리의 캐시 데이터를 즉시 업데이트할 수 있는 동기 함수입니다. 쿼리가 존재하지 않으면 새로 생성됩니다. **쿼리가 기본 `gcTime`인 5분 안에 쿼리 훅에 의해 사용되지 않으면 해당 쿼리는 가비지 컬렉션 됩니다.** 여러 쿼리를 한 번에 업데이트하고 queryKey를 부분 매칭하려면 [`queryClient.setQueriesData`](#queryclientsetqueriesdata)를 사용해야 합니다.

> `setQueryData`와 `fetchQuery`의 차이는, `setQueryData`는 동기적으로 동작하며 이미 동기적으로 사용할 데이터가 있다고 가정한다는 점입니다. 데이터를 비동기로 가져와야 한다면 쿼리 키를 다시 가져오거나 `fetchQuery`로 비동기 가져오기를 처리하는 것이 좋습니다.

```tsx
queryClient.setQueryData(queryKey, updater)
```

**Options**

- `queryKey: QueryKey`: [Query Keys](https://tanstack.com/query/latest/docs/framework/react/guides/query-keys.md)
- `updater: TQueryFnData | undefined | ((oldData: TQueryFnData | undefined) => TQueryFnData | undefined)`
  - 함수가 아닌 값을 전달하면 데이터가 해당 값으로 업데이트됩니다.
  - 함수를 전달하면 기존 데이터를 인자로 받아 새 값을 반환해야 합니다.

**Using an updater value**

```tsx
setQueryData(queryKey, newData)
```

값이 `undefined`이면 쿼리 데이터는 업데이트되지 않습니다.

**Using an updater function**

구문 편의를 위해 현재 데이터 값을 받아 새 값을 반환하는 업데이트 함수도 전달할 수 있습니다:

```tsx
setQueryData(queryKey, (oldData) => newData)
```

업데이트 함수가 `undefined`를 반환하면 쿼리 데이터는 업데이트되지 않습니다. 업데이트 함수가 입력으로 `undefined`를 받으면 `undefined`를 반환해 업데이트를 중단하고 새 캐시 항목을 만들지 않을 수 있습니다.

**Immutability**

`setQueryData`를 통한 업데이트는 반드시 **불변 방식**으로 수행해야 합니다. `oldData`나 `getQueryData`로 가져온 데이터를 직접 변경하여 캐시에 쓰지 마세요.

## `queryClient.getQueryState`

`getQueryState`는 기존 쿼리의 상태를 가져올 수 있는 동기 함수입니다. 쿼리가 없으면 `undefined`를 반환합니다.

```tsx
const state = queryClient.getQueryState(queryKey)
console.log(state.dataUpdatedAt)
```

**Options**

- `queryKey: QueryKey`: [Query Keys](https://tanstack.com/query/latest/docs/framework/react/guides/query-keys.md)

## `queryClient.setQueriesData`

`setQueriesData`는 필터 함수나 queryKey 부분 매칭을 사용해 여러 쿼리의 캐시 데이터를 즉시 업데이트할 수 있는 동기 함수입니다. 전달된 queryKey나 queryFilter와 일치하는 쿼리만 업데이트되며, 새로운 캐시 항목은 생성되지 않습니다. 내부적으로는 각각의 기존 쿼리에 대해 [`setQueryData`](#queryclientsetquerydata)가 호출됩니다.

```tsx
queryClient.setQueriesData(filters, updater)
```

**Options**

- `filters: QueryFilters`: [Query Filters](https://tanstack.com/query/latest/docs/framework/react/guides/filters.md#query-filters)
  - 필터를 전달하면 필터와 일치하는 queryKey가 업데이트됩니다.
- `updater: TQueryFnData | (oldData: TQueryFnData | undefined) => TQueryFnData`
  - 각 일치 queryKey에 대해 호출될 [setQueryData](#queryclientsetquerydata) 업데이트 함수 또는 새 데이터입니다.

## `queryClient.invalidateQueries`

`invalidateQueries` 메서드는 쿼리 키나 쿼리의 접근 가능한 속성/상태를 기준으로 캐시에 있는 단일 또는 여러 쿼리를 무효화하고 다시 가져오도록 할 수 있습니다. 기본적으로 일치하는 모든 쿼리는 즉시 무효화되며, 활성 쿼리는 백그라운드에서 다시 가져옵니다.

- **활성 쿼리가 다시 가져오지 않도록** 하고 단순히 무효화만 하고 싶다면 `refetchType: 'none'` 옵션을 사용하세요.
- **비활성 쿼리도 다시 가져오고 싶다면** `refetchType: 'all'` 옵션을 사용하세요.
- 다시 가져올 때는 [queryClient.refetchQueries](#queryclientrefetchqueries)가 호출됩니다.

```tsx
await queryClient.invalidateQueries(
  {
    queryKey: ['posts'],
    exact,
    refetchType: 'active',
  },
  { throwOnError, cancelRefetch },
)
```

**Options**

- `filters?: QueryFilters`: [Query Filters](https://tanstack.com/query/latest/docs/framework/react/guides/filters.md#query-filters)

- `queryKey?: QueryKey`: [Query Keys](https://tanstack.com/query/latest/docs/framework/react/guides/query-keys.md)
  - `refetchType?: 'active' | 'inactive' | 'all' | 'none'`
    - 기본값은 `'active'`
    - `active`로 설정하면 refetch 조건에 맞고 `useQuery` 등을 통해 현재 렌더링 중인 쿼리만 백그라운드에서 다시 가져옵니다.
    - `inactive`로 설정하면 refetch 조건에 맞지만 `useQuery` 등을 통해 **활성 렌더링 중이 아닌** 쿼리만 백그라운드에서 다시 가져옵니다.
    - `all`로 설정하면 refetch 조건에 맞는 모든 쿼리를 백그라운드에서 다시 가져옵니다.
    - `none`으로 설정하면 어떤 쿼리도 다시 가져오지 않고, refetch 조건에 맞는 쿼리들은 무효 상태로만 표시됩니다.
- `options?: InvalidateOptions`:
  - `throwOnError?: boolean`
    - `true`로 설정하면 쿼리 refetch 작업 중 하나라도 실패할 경우 이 메서드가 오류를 throw 합니다.
  - `cancelRefetch?: boolean`
    - 기본값은 `true`
      - 기본적으로는 새로운 요청을 보내기 전에 현재 실행 중인 요청을 취소합니다.
    - `false`로 설정하면 이미 실행 중인 요청이 있을 때는 refetch를 수행하지 않습니다.

## `queryClient.refetchQueries`

`refetchQueries` 메서드는 특정 조건을 기반으로 쿼리를 다시 가져오는 데 사용합니다.

예시:

```tsx
// refetch all queries:
await queryClient.refetchQueries()

// refetch all stale queries:
await queryClient.refetchQueries({ stale: true })

// refetch all active queries partially matching a query key:
await queryClient.refetchQueries({ queryKey: ['posts'], type: 'active' })

// refetch all active queries exactly matching a query key:
await queryClient.refetchQueries({
  queryKey: ['posts', 1],
  type: 'active',
  exact: true,
})
```

**Options**

- `filters?: QueryFilters`: [Query Filters](https://tanstack.com/query/latest/docs/framework/react/guides/filters.md#query-filters)
- `options?: RefetchOptions`:
  - `throwOnError?: boolean`
    - `true`로 설정하면 쿼리 refetch 작업 중 하나라도 실패할 경우 이 메서드가 오류를 throw 합니다.
  - `cancelRefetch?: boolean`
    - 기본값은 `true`
      - 기본적으로는 새로운 요청을 보내기 전에 현재 실행 중인 요청을 취소합니다.
    - `false`로 설정하면 이미 실행 중인 요청이 있을 때는 refetch를 수행하지 않습니다.

**Returns**

이 함수는 모든 쿼리의 refetch가 완료되면 resolve되는 promise를 반환합니다. 기본적으로 쿼리 refetch가 실패하더라도 오류를 throw하지 않지만, `throwOnError` 옵션을 `true`로 설정하여 동작을 변경할 수 있습니다.

**Notes**

- 비활성 관찰자만 가지고 있어 "disabled" 상태인 쿼리는 절대 다시 가져오지 않습니다.
- Static StaleTime을 가진 관찰자만 보유해 "static" 상태인 쿼리도 다시 가져오지 않습니다.

## `queryClient.cancelQueries`

`cancelQueries` 메서드는 쿼리 키나 그 밖에 접근 가능한 속성/상태를 기준으로 진행 중인 쿼리를 취소할 때 사용합니다.

낙관적 업데이트를 수행하는 경우에 특히 유용하며, 완료 시점에 낙관적 업데이트를 덮어쓰지 않도록 모든 쿼리 refetch를 취소해야 할 때 자주 사용됩니다.

```tsx
await queryClient.cancelQueries(
  { queryKey: ['posts'], exact: true },
  { silent: true },
)
```

**Options**

- `filters?: QueryFilters`: [Query Filters](https://tanstack.com/query/latest/docs/framework/react/guides/filters.md#query-filters)
- `cancelOptions?: CancelOptions`: [Cancel Options](https://tanstack.com/query/latest/docs/framework/react/guides/query-cancellation.md#cancel-options)

**Returns**

이 메서드는 아무 것도 반환하지 않습니다.

## `queryClient.removeQueries`

`removeQueries` 메서드는 쿼리 키나 그 밖에 접근 가능한 속성/상태를 기준으로 캐시에서 쿼리를 제거하는 데 사용합니다.

```tsx
queryClient.removeQueries({ queryKey, exact: true })
```

**Options**

- `filters?: QueryFilters`: [Query Filters](https://tanstack.com/query/latest/docs/framework/react/guides/filters.md#query-filters)

**Returns**

이 메서드는 아무 것도 반환하지 않습니다.

## `queryClient.resetQueries`

`resetQueries` 메서드는 쿼리 키나 접근 가능한 다른 속성/상태를 기준으로 캐시에 있는 쿼리를 초기 상태로 되돌리는 데 사용합니다.

이 메서드는 구독자에게 알림을 보내며(모든 구독자를 제거하는 `clear`와 다름), 쿼리를 로드 이전 상태로 리셋합니다(`invalidateQueries`와 다름). 쿼리에 `initialData`가 있으면 그 데이터로 리셋되며, 활성 쿼리는 다시 가져옵니다.

```tsx
queryClient.resetQueries({ queryKey, exact: true })
```

**Options**

- `filters?: QueryFilters`: [Query Filters](https://tanstack.com/query/latest/docs/framework/react/guides/filters.md#query-filters)
- `options?: ResetOptions`:
  - `throwOnError?: boolean`
    - `true`로 설정하면 쿼리 refetch 작업 중 하나라도 실패할 경우 이 메서드가 오류를 throw 합니다.
  - `cancelRefetch?: boolean`
    - 기본값은 `true`
      - 기본적으로는 새로운 요청을 보내기 전에 현재 실행 중인 요청을 취소합니다.
    - `false`로 설정하면 이미 실행 중인 요청이 있을 때는 refetch를 수행하지 않습니다.

**Returns**

이 메서드는 모든 활성 쿼리가 다시 가져와졌을 때 resolve되는 promise를 반환합니다.

## `queryClient.isFetching`

`isFetching` 메서드는 캐시에서 현재 fetching 중인 쿼리(백그라운드 fetching, 새 페이지 로드, 더 많은 무한 쿼리 결과 로딩 포함)의 개수를 나타내는 `integer`를 반환합니다.

```tsx
if (queryClient.isFetching()) {
  console.log('At least one query is fetching!')
}
```

TanStack Query는 수동으로 쿼리 캐시에 구독하지 않고도 컴포넌트에서 이 상태를 구독할 수 있는 [`useIsFetching`](https://tanstack.com/query/latest/docs/framework/react/reference/useIsFetching.md) 훅도 제공합니다.

**Options**

- `filters?: QueryFilters`: [Query Filters](https://tanstack.com/query/latest/docs/framework/react/guides/filters.md#query-filters)

**Returns**

이 메서드는 fetching 중인 쿼리의 수를 반환합니다.

## `queryClient.isMutating`

`isMutating` 메서드는 캐시에서 현재 fetching 중인 뮤테이션의 개수를 나타내는 `integer`를 반환합니다.

```tsx
if (queryClient.isMutating()) {
  console.log('At least one mutation is fetching!')
}
```

TanStack Query는 뮤테이션 캐시에 수동으로 구독하지 않고도 컴포넌트에서 이 상태를 구독할 수 있는 [`useIsMutating`](https://tanstack.com/query/latest/docs/framework/react/reference/useIsMutating.md) 훅도 제공합니다.

**Options**

- `filters: MutationFilters`: [Mutation Filters](https://tanstack.com/query/latest/docs/framework/react/guides/filters.md#mutation-filters)

**Returns**

이 메서드는 fetching 중인 뮤테이션의 수를 반환합니다.

## `queryClient.getDefaultOptions`

`getDefaultOptions` 메서드는 클라이언트 생성 시 또는 `setDefaultOptions`로 설정된 기본 옵션을 반환합니다.

```tsx
const defaultOptions = queryClient.getDefaultOptions()
```

## `queryClient.setDefaultOptions`

`setDefaultOptions` 메서드는 이 queryClient에 대한 기본 옵션을 동적으로 설정할 때 사용합니다. 이전에 정의된 기본 옵션은 덮어씁니다.

```tsx
queryClient.setDefaultOptions({
  queries: {
    staleTime: Infinity,
  },
})
```

## `queryClient.getQueryDefaults`

`getQueryDefaults` 메서드는 특정 쿼리에 대해 설정된 기본 옵션을 반환합니다.

```tsx
const defaultOptions = queryClient.getQueryDefaults(['posts'])
```

> 여러 쿼리 기본값이 주어진 쿼리 키와 일치하면 등록 순서에 따라 병합됩니다.
> [`setQueryDefaults`](#queryclientsetquerydefaults)를 참고하세요.

## `queryClient.setQueryDefaults`

`setQueryDefaults`는 특정 쿼리에 대한 기본 옵션을 설정하는 데 사용할 수 있습니다.

```tsx
queryClient.setQueryDefaults(['posts'], { queryFn: fetchPosts })

function Component() {
  const { data } = useQuery({ queryKey: ['posts'] })
}
```

**Options**

- `queryKey: QueryKey`: [Query Keys](https://tanstack.com/query/latest/docs/framework/react/guides/query-keys.md)
- `options: QueryOptions`

> [`getQueryDefaults`](#queryclientgetquerydefaults)에서 언급했듯이 쿼리 기본값의 등록 순서는 중요합니다.
> `getQueryDefaults`가 일치하는 기본값을 병합하므로, 등록은 **가장 일반적인 키**에서 **가장 구체적인 키** 순서로 진행해야 합니다.
> 이렇게 하면 보다 구체적인 기본값이 일반적인 기본값을 덮어씁니다.

## `queryClient.getMutationDefaults`

`getMutationDefaults` 메서드는 특정 뮤테이션에 대해 설정된 기본 옵션을 반환합니다.

```tsx
const defaultOptions = queryClient.getMutationDefaults(['addPost'])
```

## `queryClient.setMutationDefaults`

`setMutationDefaults`는 특정 뮤테이션에 대한 기본 옵션을 설정하는 데 사용할 수 있습니다.

```tsx
queryClient.setMutationDefaults(['addPost'], { mutationFn: addPost })

function Component() {
  const { data } = useMutation({ mutationKey: ['addPost'] })
}
```

**Options**

- `mutationKey: unknown[]`
- `options: MutationOptions`

> [`setQueryDefaults`](#queryclientsetquerydefaults)와 마찬가지로 등록 순서가 중요합니다.

## `queryClient.getQueryCache`

`getQueryCache` 메서드는 이 클라이언트가 연결된 쿼리 캐시를 반환합니다.

```tsx
const queryCache = queryClient.getQueryCache()
```

## `queryClient.getMutationCache`

`getMutationCache` 메서드는 이 클라이언트가 연결된 뮤테이션 캐시를 반환합니다.

```tsx
const mutationCache = queryClient.getMutationCache()
```

## `queryClient.clear`

`clear` 메서드는 연결된 모든 캐시를 초기화합니다.

```tsx
queryClient.clear()
```

## `queryClient.resumePausedMutations`

네트워크 연결이 없어 일시 중지된 뮤테이션을 재개하는 데 사용할 수 있습니다.

```tsx
queryClient.resumePausedMutations()
```

