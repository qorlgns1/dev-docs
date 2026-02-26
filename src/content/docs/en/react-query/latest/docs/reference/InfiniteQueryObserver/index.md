---
title: 'InfiniteQueryObserver'
description: 'The  can be used to observe and switch between infinite queries.'
---

Source URL: https://tanstack.com/query/latest/docs/reference/InfiniteQueryObserver

# InfiniteQueryObserver

## `InfiniteQueryObserver`

The `InfiniteQueryObserver` can be used to observe and switch between infinite queries.

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

**Options**

The options for the `InfiniteQueryObserver` are exactly the same as those of [`useInfiniteQuery`](https://tanstack.com/query/latest/docs/framework/react/reference/useInfiniteQuery).

