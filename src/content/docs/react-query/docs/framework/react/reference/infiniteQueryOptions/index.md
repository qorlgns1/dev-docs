---
title: 'infiniteQueryOptions'
description: 'infiniteQueryOptions({'
---

# infiniteQueryOptions

```tsx
infiniteQueryOptions({
  queryKey,
  ...options,
})
```

**옵션**

`infiniteQueryOptions`에는 [`useInfiniteQuery`](https://tanstack.com/query/latest/docs/framework/react/reference/useInfiniteQuery.md)에 전달할 수 있는 거의 모든 값을 전달할 수 있습니다. 일부 옵션은 `queryClient.prefetchInfiniteQuery`와 같은 함수로 전달되면 효과가 없지만, TypeScript는 이러한 초과 프로퍼티를 허용합니다.

- `queryKey: QueryKey`
  - **필수**
  - 옵션을 생성할 때 사용할 쿼리 키입니다.

자세한 내용은 [useInfiniteQuery](https://tanstack.com/query/latest/docs/framework/react/reference/useInfiniteQuery.md)를 참조하세요.

