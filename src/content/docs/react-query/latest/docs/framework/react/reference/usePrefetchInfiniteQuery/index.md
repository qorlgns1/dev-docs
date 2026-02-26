---
title: 'usePrefetchInfiniteQuery'
description: 'usePrefetchInfiniteQuery(options)'
---

# usePrefetchInfiniteQuery

```tsx
usePrefetchInfiniteQuery(options)
```

**옵션**

[`queryClient.prefetchInfiniteQuery`](https://tanstack.com/query/latest/docs/reference/QueryClient.md#queryclientprefetchinfinitequery)에 전달할 수 있는 것은 모두 `usePrefetchInfiniteQuery`에도 전달할 수 있습니다. 아래와 같이 일부 옵션은 필수임을 기억하세요.

- `queryKey: QueryKey`
  - **필수**
  - 렌더링 중에 프리페치할 쿼리 키

- `queryFn: (context: QueryFunctionContext) => Promise<TData>`
  - **필수이지만, 기본 쿼리 함수가 정의되지 않은 경우에만 필요** 자세한 내용은 [Default Query Function](https://tanstack.com/query/latest/docs/framework/react/guides/default-query-function.md)을 참조하세요.

- `initialPageParam: TPageParam`
  - **필수**
  - 첫 페이지를 가져올 때 사용할 기본 페이지 매개변수.

- `getNextPageParam: (lastPage, allPages, lastPageParam, allPageParams) => TPageParam | undefined | null`
  - **필수**
  - 이 쿼리에 새 데이터가 수신되면, 이 함수는 무한 목록의 마지막 페이지와 모든 페이지 배열 전체, 그리고 pageParam 정보를 함께 받습니다.
  - 쿼리 함수에 마지막 선택적 매개변수로 전달될 **단일 변수**를 반환해야 합니다.
  - 다음 페이지가 없음을 나타내려면 `undefined` 또는 `null`을 반환하세요.

- **반환값**

`usePrefetchInfiniteQuery`는 아무 것도 반환하지 않습니다. [`useSuspenseInfiniteQuery`](https://tanstack.com/query/latest/docs/framework/react/reference/useSuspenseInfiniteQuery.md)를 사용하는 컴포넌트를 감싸는 서스펜스 경계 이전에, 렌더링 중 프리페치를 트리거하는 용도로만 사용해야 합니다.

