---
title: 'useQuery'
description: 'initialDataUpdatedAt,'
---

출처 URL: https://tanstack.com/query/latest/docs/framework/react/reference/useQuery

# useQuery

```tsx
const {
  data,
  dataUpdatedAt,
  error,
  errorUpdatedAt,
  failureCount,
  failureReason,
  fetchStatus,
  isError,
  isFetched,
  isFetchedAfterMount,
  isFetching,
  isInitialLoading,
  isLoading,
  isLoadingError,
  isPaused,
  isPending,
  isPlaceholderData,
  isRefetchError,
  isRefetching,
  isStale,
  isSuccess,
  isEnabled,
  promise,
  refetch,
  status,
} = useQuery(
  {
    queryKey,
    queryFn,
    gcTime,
    enabled,
    networkMode,
    initialData,
    initialDataUpdatedAt,
    meta,
    notifyOnChangeProps,
    placeholderData,
    queryKeyHashFn,
    refetchInterval,
    refetchIntervalInBackground,
    refetchOnMount,
    refetchOnReconnect,
    refetchOnWindowFocus,
    retry,
    retryOnMount,
    retryDelay,
    select,
    staleTime,
    structuralSharing,
    subscribed,
    throwOnError,
  },
  queryClient,
)
```

**매개변수1 (Options)**

- `queryKey: unknown[]`
  - **필수**
  - 이 쿼리에 사용할 쿼리 키입니다.
  - 쿼리 키는 안정적인 해시로 해시됩니다. 자세한 내용은 [Query Keys](https://tanstack.com/query/latest/docs/framework/react/guides/query-keys.md)를 참고하세요.
  - `enabled`가 `false`로 설정되지 않는 한, 이 키가 변경되면 쿼리가 자동으로 업데이트됩니다.
- `queryFn: (context: QueryFunctionContext) => Promise<TData>`
  - **필수(기본 쿼리 함수가 정의되지 않은 경우에만)** 자세한 내용은 [Default Query Function](https://tanstack.com/query/latest/docs/framework/react/guides/default-query-function.md)을 참고하세요.
  - 쿼리가 데이터를 요청할 때 사용할 함수입니다.
  - [QueryFunctionContext](https://tanstack.com/query/latest/docs/framework/react/guides/query-functions.md#queryfunctioncontext)를 입력으로 받습니다.
  - 데이터를 resolve하거나 오류를 throw하는 Promise를 반환해야 하며, 데이터는 `undefined`가 될 수 없습니다.
- `enabled: boolean | (query: Query) => boolean`
  - 이 값을 `false`로 설정하면 쿼리가 자동 실행되지 않습니다.
  - [Dependent Queries](https://tanstack.com/query/latest/docs/framework/react/guides/dependent-queries.md)에 활용할 수 있습니다.
- `networkMode: 'online' | 'always' | 'offlineFirst'`
  - 선택 사항
  - 기본값은 `'online'`
  - 자세한 내용은 [Network Mode](https://tanstack.com/query/latest/docs/framework/react/guides/network-mode.md)를 참고하세요.
- `retry: boolean | number | (failureCount: number, error: TError) => boolean`
  - `false`이면 실패한 쿼리를 기본적으로 재시도하지 않습니다.
  - `true`이면 실패한 쿼리를 무한히 재시도합니다.
  - `number`(예: `3`)로 설정하면 실패 횟수가 해당 숫자에 도달할 때까지 재시도합니다.
  - 함수로 설정하면 `failureCount`(첫 재시도는 `0`)와 `error`를 인수로 받아 재시도 여부를 결정합니다.
  - 기본값은 클라이언트에서 `3`, 서버에서 `0`입니다.
- `retryOnMount: boolean`
  - `false`로 설정하면 에러가 있을 때 마운트 시 재시도하지 않습니다. 기본값은 `true`입니다.
- `retryDelay: number | (retryAttempt: number, error: TError) => number`
  - 이 함수는 `retryAttempt` 정수와 실제 Error를 받아 다음 시도 전 지연 시간을 밀리초로 반환합니다.
  - `attempt => Math.min(attempt > 1 ? 2 ** attempt * 1000 : 1000, 30 * 1000)` 같은 함수는 지수 백오프를 적용합니다.
  - `attempt => attempt * 1000` 같은 함수는 선형 백오프를 적용합니다.
- `staleTime: number | 'static' | ((query: Query) => number | 'static')`
  - 선택 사항
  - 기본값은 `0`
  - 데이터가 오래된 것으로 간주되는 밀리초 단위 시간입니다. 이 값은 정의된 훅에만 적용됩니다.
  - `Infinity`로 설정하면 수동으로 무효화하지 않는 이상 데이터가 오래되지 않습니다.
  - 함수로 설정하면 쿼리를 인수로 받아 `staleTime`을 계산합니다.
  - `'static'`으로 설정하면 데이터는 오래된 것으로 간주되지 않습니다.
- `gcTime: number | Infinity`
  - 기본값은 `5 * 60 * 1000`(5분)이며 SSR 중에는 `Infinity`
  - 사용되지 않거나 비활성화된 캐시 데이터가 메모리에 남아 있는 밀리초 단위 시간입니다. 쿼리 캐시가 사용되지 않거나 비활성화되면 이 기간 후에 가비지 컬렉션됩니다. 서로 다른 시간이 지정되면 가장 긴 값이 사용됩니다.
  - 참고: 허용되는 최대 시간은 약 [24일](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout#maximum_delay_value)이지만 [timeoutManager.setTimeoutProvider](https://tanstack.com/query/latest/docs/reference/timeoutManager.md#timeoutmanagersettimeoutprovider)를 사용하면 우회할 수 있습니다.
  - `Infinity`로 설정하면 가비지 컬렉션이 비활성화됩니다.
- `queryKeyHashFn: (queryKey: QueryKey) => string`
  - 선택 사항
  - 지정하면 이 함수가 `queryKey`를 문자열로 해시하는 데 사용됩니다.
- `refetchInterval: number | false | ((query: Query) => number | false | undefined)`
  - 선택 사항
  - 숫자로 설정하면 모든 쿼리가 해당 밀리초 주기로 계속 재요청합니다.
  - 함수로 설정하면 쿼리를 인수로 받아 주기를 계산합니다.
- `refetchIntervalInBackground: boolean`
  - 선택 사항
  - `true`로 설정하면 `refetchInterval`로 연속 재요청하도록 설정된 쿼리가 탭/창이 백그라운드에 있을 때도 재요청합니다.
- `refetchOnMount: boolean | "always" | ((query: Query) => boolean | "always")`
  - 선택 사항
  - 기본값은 `true`
  - `true`이면 데이터가 오래된 경우 마운트 시 재요청합니다.
  - `false`이면 마운트 시 재요청하지 않습니다.
  - `"always"`이면(`staleTime: 'static'`이 아닌 한) 항상 마운트 시 재요청합니다.
  - 함수로 설정하면 쿼리를 인수로 받아 값을 계산합니다.
- `refetchOnWindowFocus: boolean | "always" | ((query: Query) => boolean | "always")`
  - 선택 사항
  - 기본값은 `true`
  - `true`이면 데이터가 오래된 경우 창 포커스 시 재요청합니다.
  - `false`이면 창 포커스 시 재요청하지 않습니다.
  - `"always"`이면(`staleTime: 'static'`이 아닌 한) 항상 창 포커스 시 재요청합니다.
  - 함수로 설정하면 쿼리를 인수로 받아 값을 계산합니다.
- `refetchOnReconnect: boolean | "always" | ((query: Query) => boolean | "always")`
  - 선택 사항
  - 기본값은 `true`
  - `true`이면 데이터가 오래된 경우 재연결 시 재요청합니다.
  - `false`이면 재연결 시 재요청하지 않습니다.
  - `"always"`이면(`staleTime: 'static'`이 아닌 한) 항상 재연결 시 재요청합니다.
  - 함수로 설정하면 쿼리를 인수로 받아 값을 계산합니다.
- `notifyOnChangeProps: string[] | "all" | (() => string[] | "all" | undefined)`
  - 선택 사항
  - 설정하면 나열된 속성이 변경될 때만 컴포넌트가 리렌더링됩니다.
  - 예를 들어 `['data', 'error']`로 설정하면 `data` 또는 `error` 속성이 변경될 때만 리렌더링됩니다.
  - `"all"`로 설정하면 스마트 추적에서 제외되어 쿼리가 업데이트될 때마다 리렌더링됩니다.
  - 함수로 설정하면 속성 목록을 계산하기 위해 실행됩니다.
  - 기본적으로 속성 접근이 추적되며, 추적된 속성 중 하나가 변경될 때만 리렌더링됩니다.
- `select: (data: TData) => unknown`
  - 선택 사항
  - 쿼리 함수가 반환하는 데이터의 일부를 변환 또는 선택하는 데 사용할 수 있습니다. 반환되는 `data` 값에만 영향을 주며, 쿼리 캐시에 저장되는 값에는 영향을 주지 않습니다.
  - `data`가 변경되거나 `select` 함수 참조 자체가 변경될 때만 실행됩니다. 최적화를 위해 `useCallback`으로 감싸세요.
- `initialData: TData | () => TData`
  - 선택 사항
  - 설정하면 쿼리가 아직 생성되거나 캐시되지 않았을 때 쿼리 캐시의 초기 데이터로 사용됩니다.
  - 함수로 설정하면 공유/루트 쿼리 초기화 중 **한 번만** 호출되며, 초기 데이터를 동기적으로 반환해야 합니다.
  - `staleTime`이 설정되지 않은 이상 초기 데이터는 기본적으로 오래된 것으로 간주됩니다.
  - `initialData`는 캐시에 **영구 저장**됩니다.
- `initialDataUpdatedAt: number | (() => number | undefined)`
  - 선택 사항
  - 설정하면 `initialData` 자체가 마지막으로 업데이트된 시간(밀리초)을 나타내는 값으로 사용됩니다.
- `placeholderData: TData | (previousValue: TData | undefined, previousQuery: Query | undefined) => TData`
  - 선택 사항
  - 설정하면 쿼리가 `pending` 상태일 때 이 쿼리 옵저버의 플레이스홀더 데이터로 사용됩니다.
  - `placeholderData`는 캐시에 **영구 저장되지 않습니다.**
  - 함수로 제공하면 첫 번째 인수로 이전에 감시한 쿼리 데이터(가능한 경우)가, 두 번째 인수로 전체 previousQuery 인스턴스가 전달됩니다.
- `structuralSharing: boolean | (oldData: unknown | undefined, newData: unknown) => unknown`
  - 선택 사항
  - 기본값은 `true`
  - `false`로 설정하면 쿼리 결과 간 구조적 공유가 비활성화됩니다.
  - 함수로 설정하면 이전 데이터와 새 데이터가 이 함수를 거치며, 쿼리에 사용할 최종 데이터를 결합해야 합니다. 이렇게 하면 직렬화할 수 없는 값이 포함된 경우에도 이전 데이터의 참조를 유지해 성능을 향상시킬 수 있습니다.
- `subscribed: boolean`
  - 선택 사항
  - 기본값은 `true`
  - `false`로 설정하면 이 `useQuery` 인스턴스는 캐시에 구독되지 않습니다. 즉, `queryFn`을 자체적으로 트리거하지 않으며, 다른 방법으로 캐시에 데이터가 들어와도 업데이트를 받지 않습니다.
- `throwOnError: undefined | boolean | (error: TError, query: Query) => boolean`
  - 렌더 단계에서 오류를 throw해 가장 가까운 에러 바운더리로 전달하고 싶다면 `true`로 설정하세요.
  - `suspense`의 기본 오류 throw 동작을 비활성화하려면 `false`로 설정하세요.
  - 함수로 설정하면 오류와 쿼리를 받아, 에러 바운더리에 오류를 표시할지(`true`) 상태로 반환할지(`false`) 결정해야 합니다.
- `meta: Record<string, unknown>`
  - 선택 사항
  - 설정하면 쿼리 캐시 항목에 필요한 추가 정보를 저장하며, `query`를 사용할 수 있는 어디서든 접근할 수 있고 `queryFn`에 제공되는 `QueryFunctionContext`에도 포함됩니다.

**매개변수2 (QueryClient)**

- `queryClient?: QueryClient`
  - 사용자 정의 QueryClient를 사용하려면 이 값을 지정하세요. 그렇지 않으면 가장 가까운 컨텍스트의 QueryClient가 사용됩니다.

**반환값**

- `status: QueryStatus`
  - 다음 중 하나입니다.
    - 캐시된 데이터가 없고 아직 쿼리 시도가 완료되지 않았다면 `pending`.
    - 쿼리 시도가 오류로 끝났다면 `error`. `error` 속성에는 시도된 fetch에서 받은 오류가 포함됩니다.
    - 오류 없이 응답을 받아 데이터를 표시할 준비가 되면 `success`. `enabled`가 `false`이고 아직 fetch되지 않았다면 쿼리 초기화 시 제공한 첫 `initialData`가 `data`가 됩니다.
- `isPending: boolean`
  - 위 `status` 변수에서 파생된 편의용 불리언입니다.
- `isSuccess: boolean`
  - 위 `status` 변수에서 파생된 편의용 불리언입니다.
- `isError: boolean`
  - 위 `status` 변수에서 파생된 편의용 불리언입니다.
- `isLoadingError: boolean`
  - 첫 fetch에서 쿼리가 실패하면 `true`입니다.
- `isRefetchError: boolean`
  - 재요청 중 쿼리가 실패하면 `true`입니다.
- `data: TData`
  - 기본값은 `undefined`.
  - 쿼리에서 마지막으로 성공적으로 resolve된 데이터입니다.
- `dataUpdatedAt: number`
  - 쿼리가 가장 최근에 `status`를 `"success"`로 반환한 시점의 타임스탬프입니다.
- `error: null | TError`
  - 기본값은 `null`
  - 쿼리에 대한 오류 객체로, 오류가 throw되었을 때 설정됩니다.
- `errorUpdatedAt: number`
  - 쿼리가 가장 최근에 `status`를 `"error"`로 반환한 시점의 타임스탬프입니다.
- `isStale: boolean`
  - 캐시의 데이터가 무효화되었거나 지정한 `staleTime`보다 오래되면 `true`입니다.
- `isPlaceholderData: boolean`
  - 표시 중인 데이터가 플레이스홀더 데이터라면 `true`입니다.
- `isFetched: boolean`
  - 쿼리가 fetch되었다면 `true`입니다.
- `isFetchedAfterMount: boolean`
  - 컴포넌트가 마운트된 후 쿼리가 fetch되었다면 `true`입니다.
  - 이 속성을 사용해 이전에 캐시된 데이터를 숨길 수 있습니다.
- `fetchStatus: FetchStatus`

- `fetching`: 쿼리 함수가 실행 중일 때 `true`입니다. 초기 `pending`뿐 아니라 백그라운드 재조회도 포함됩니다.
  - `paused`: 쿼리가 가져오기를 원했지만 `paused`된 상태입니다.
  - `idle`: 쿼리가 가져오기를 수행하지 않는 상태입니다.
  - 자세한 내용은 [Network Mode](https://tanstack.com/query/latest/docs/framework/react/guides/network-mode.md)를 참고하세요.
- `isFetching: boolean`
  - 위의 `fetchStatus` 변수에서 파생된 boolean으로, 편의를 위해 제공됩니다.
- `isPaused: boolean`
  - 위의 `fetchStatus` 변수에서 파생된 boolean으로, 편의를 위해 제공됩니다.
- `isRefetching: boolean`
  - 백그라운드 재조회가 진행 중일 때 `true`이며, 초기 `pending`은 포함하지 않습니다.
  - `isFetching && !isPending`와 동일합니다.
- `isLoading: boolean`
  - 쿼리에 대한 첫 가져오기 요청이 진행 중일 때 `true`입니다.
  - `isFetching && isPending`와 동일합니다.
- `isInitialLoading: boolean`
  - **deprecated**
  - `isLoading`의 별칭으로, 다음 메이저 버전에서 제거될 예정입니다.
- `isEnabled: boolean`
  - 이 쿼리 옵저버가 활성화되어 있으면 `true`, 그렇지 않으면 `false`입니다.
- `failureCount: number`
  - 해당 쿼리의 실패 횟수입니다.
  - 쿼리가 실패할 때마다 증가합니다.
  - 쿼리가 성공하면 `0`으로 초기화됩니다.
- `failureReason: null | TError`
  - 쿼리 재시도의 실패 원인입니다.
  - 쿼리가 성공하면 `null`로 초기화됩니다.
- `errorUpdateCount: number`
  - 모든 오류의 합계입니다.
- `refetch: (options: { throwOnError: boolean, cancelRefetch: boolean }) => Promise<UseQueryResult>`
  - 쿼리를 수동으로 재조회하는 함수입니다.
  - 쿼리가 오류를 일으키면 오류는 로그에만 기록됩니다. 오류를 던지려면 `throwOnError: true` 옵션을 전달하세요.
  - `cancelRefetch?: boolean`
    - 기본값은 `true`입니다.
      - 기본적으로는 새 요청을 만들기 전에 현재 실행 중인 요청을 취소합니다.
    - `false`로 설정하면 이미 요청이 실행 중인 경우 재조회가 수행되지 않습니다.
- `promise: Promise<TData>`
  - 쿼리의 데이터로 resolve되는 안정적인 프라미스입니다.
  - `QueryClient`에서 `experimental_prefetchInRender` 기능 플래그를 활성화해야 합니다.

