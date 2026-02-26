---
title: 'InfiniteQueryObserver'
description: '는 무한 쿼리를 관찰하고 전환하는 데 사용할 수 있습니다.'
---

Source URL: https://tanstack.com/query/latest/docs/reference/InfiniteQueryObserver

# InfiniteQueryObserver

## `InfiniteQueryObserver`

`InfiniteQueryObserver`는 무한 쿼리를 관찰하고 전환하는 데 사용할 수 있습니다.

```tsx
const observer = new InfiniteQueryObserver(queryClient, {
  queryKey: ['posts'],
  queryFn: fetchPosts,
  getNextPageParam: (lastPage, allPages) => lastPage.nextCursor,
  getPreviousPageParam: (firstPage, allPages) => firstPage.prevCursor,
})

const unsubscribe = observer.subscribe((result) => {
  console.log(result)
  unsubscribe()
})
```

**옵션**

`InfiniteQueryObserver`의 옵션은 [`useInfiniteQuery`](https://tanstack.com/query/latest/docs/framework/react/reference/useInfiniteQuery)와 완전히 동일합니다.

