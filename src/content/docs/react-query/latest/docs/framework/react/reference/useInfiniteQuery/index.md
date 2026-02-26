---
title: 'useInfiniteQuery'
description: 'isFetchingPreviousPage,'
---

출처 URL: https://tanstack.com/query/latest/docs/framework/react/reference/useInfiniteQuery

# useInfiniteQuery

```tsx
const {
  fetchNextPage,
  fetchPreviousPage,
  hasNextPage,
  hasPreviousPage,
  isFetchingNextPage,
  isFetchingPreviousPage,
  promise,
  ...result
} = useInfiniteQuery({
  queryKey,
  queryFn: ({ pageParam }) => fetchPage(pageParam),
  initialPageParam: 1,
  ...options,
  getNextPageParam: (lastPage, allPages, lastPageParam, allPageParams) =>
    lastPage.nextCursor,
  getPreviousPageParam: (firstPage, allPages, firstPageParam, allPageParams) =>
    firstPage.prevCursor,
})
```

**Options**

`useInfiniteQuery` 옵션은 [`useQuery` 훅](https://tanstack.com/query/latest/docs/framework/react/reference/useQuery.md)과 동일하며, 아래 항목이 추가됩니다.

- `queryFn: (context: QueryFunctionContext) => Promise<TData>`
  - **필수** (단, 기본 쿼리 함수 [`defaultQueryFn`](https://tanstack.com/query/latest/docs/framework/react/guides/default-query-function.md)이 정의되지 않은 경우)
  - 쿼리가 데이터를 요청할 때 사용하는 함수입니다.
  - [QueryFunctionContext](https://tanstack.com/query/latest/docs/framework/react/guides/query-functions.md#queryfunctioncontext)를 인자로 받습니다.
  - 데이터를 resolve하거나 오류를 throw하는 Promise를 반환해야 합니다.
- `initialPageParam: TPageParam`
  - **필수**
  - 첫 페이지를 가져올 때 사용할 기본 page param입니다.
- `getNextPageParam: (lastPage, allPages, lastPageParam, allPageParams) => TPageParam | undefined | null`
  - **필수**
  - 새 데이터를 수신하면, 이 함수는 무한 목록의 마지막 페이지와 모든 페이지 배열, 그리고 pageParam 정보를 받습니다.
  - 쿼리 함수의 마지막 선택적 매개변수로 전달할 **단일 변수**를 반환해야 합니다.
  - 다음 페이지가 없을 때는 `undefined` 또는 `null`을 반환합니다.
- `getPreviousPageParam: (firstPage, allPages, firstPageParam, allPageParams) => TPageParam | undefined | null`
  - 새 데이터를 수신하면, 이 함수는 무한 목록의 첫 페이지와 모든 페이지 배열, 그리고 pageParam 정보를 받습니다.
  - 쿼리 함수의 마지막 선택적 매개변수로 전달할 **단일 변수**를 반환해야 합니다.
  - 이전 페이지가 없을 때는 `undefined` 또는 `null`을 반환합니다.
- `maxPages: number | undefined`
  - 무한 쿼리 데이터에 저장할 수 있는 최대 페이지 수입니다.
  - 최대 페이지 수에 도달하면, 지정된 방향에 따라 새 페이지를 가져올 때 첫 페이지 또는 마지막 페이지가 pages 배열에서 제거됩니다.
  - `undefined`이거나 `0`이면 페이지 수에 제한이 없습니다.
  - 기본값은 `undefined`입니다.
  - `maxPages`가 `0`보다 크면 양방향으로 필요한 페이지를 가져올 수 있도록 `getNextPageParam`과 `getPreviousPageParam`을 올바르게 정의해야 합니다.

**Returns**

`useInfiniteQuery`가 반환하는 속성은 [`useQuery` 훅](https://tanstack.com/query/latest/docs/framework/react/reference/useQuery.md)과 동일하지만, 아래 속성이 추가되고 `isRefetching`, `isRefetchError` 동작이 조금 다릅니다.

- `data.pages: TData[]`
  - 모든 페이지가 담긴 배열입니다.
- `data.pageParams: unknown[]`
  - 모든 page param이 담긴 배열입니다.
- `isFetchingNextPage: boolean`
  - `fetchNextPage`로 다음 페이지를 가져오는 동안 `true`입니다.
- `isFetchingPreviousPage: boolean`
  - `fetchPreviousPage`로 이전 페이지를 가져오는 동안 `true`입니다.
- `fetchNextPage: (options?: FetchNextPageOptions) => Promise<UseInfiniteQueryResult>`
  - 다음 “페이지” 결과를 가져오는 함수입니다.
  - `options.cancelRefetch: boolean`이 `true`이면, 이전 호출이 resolve되지 않았더라도 `fetchNextPage`를 반복 호출할 때마다 `queryFn`이 실행됩니다. 또한 이전 호출의 결과는 무시됩니다. `false`이면 첫 호출이 resolve될 때까지 반복 호출이 무효합니다. 기본값은 `true`입니다.
- `fetchPreviousPage: (options?: FetchPreviousPageOptions) => Promise<UseInfiniteQueryResult>`
  - 이전 “페이지” 결과를 가져오는 함수입니다.
  - `options.cancelRefetch: boolean` 동작은 `fetchNextPage`와 동일합니다.
- `hasNextPage: boolean`
  - `getNextPageParam` 옵션을 통해 다음 페이지가 있다고 알려진 경우 `true`입니다.
- `hasPreviousPage: boolean`
  - `getPreviousPageParam` 옵션을 통해 이전 페이지가 있다고 알려진 경우 `true`입니다.
- `isFetchNextPageError: boolean`
  - 다음 페이지를 가져오는 동안 쿼리가 실패하면 `true`입니다.
- `isFetchPreviousPageError: boolean`
  - 이전 페이지를 가져오는 동안 쿼리가 실패하면 `true`입니다.
- `isRefetching: boolean`
  - 백그라운드 리페치가 진행 중일 때 `true`이며, 초기 `pending` 상태나 다음/이전 페이지 페칭은 포함하지 않습니다.
  - `isFetching && !isPending && !isFetchingNextPage && !isFetchingPreviousPage`와 동일합니다.
- `isRefetchError: boolean`
  - 페이지를 리페치하는 동안 쿼리가 실패하면 `true`입니다.
- `promise: Promise<TData>`
  - 쿼리 결과로 resolve되는 안정적인 Promise입니다.
  - 데이터를 가져오기 위해 `React.use()`와 함께 사용할 수 있습니다.
  - `QueryClient`에서 `experimental_prefetchInRender` 기능 플래그를 활성화해야 합니다.

`fetchNextPage` 같은 명령형 페치 호출은 기본 리페치 동작을 방해하여 데이터를 오래된 상태로 만들 수 있습니다. 이러한 함수는 사용자 액션에 대한 응답으로만 호출하거나 `hasNextPage && !isFetching`과 같은 조건을 추가하는 것이 좋습니다.

