---
title: 'usePrefetchQuery'
description: 'usePrefetchQuery(options)'
---

# usePrefetchQuery

```tsx
usePrefetchQuery(options)
```

**옵션**

[`queryClient.prefetchQuery`](https://tanstack.com/query/latest/docs/reference/QueryClient.md#queryclientprefetchquery)에 전달할 수 있는 모든 값을 `usePrefetchQuery`에도 전달할 수 있습니다. 아래와 같이 일부 옵션은 필수입니다.

- `queryKey: QueryKey`
  - **Required**
  - 렌더링 중에 프리페치할 쿼리 키

- `queryFn: (context: QueryFunctionContext) => Promise<TData>`
  - **Required, but only if no default query function has been defined** 자세한 내용은 [Default Query Function](https://tanstack.com/query/latest/docs/framework/react/guides/default-query-function.md)을 참고하세요.

**반환값**

`usePrefetchQuery`는 아무것도 반환하지 않습니다. [`useSuspenseQuery`](https://tanstack.com/query/latest/docs/framework/react/reference/useSuspenseQuery.md)를 사용하는 컴포넌트를 감싸는 서스펜스 경계 이전에, 렌더링 중 프리페치만 실행하는 용도로 사용해야 합니다.

