---
title: 'QueriesObserver'
description: 'The  can be used to observe multiple queries.'
---

Source URL: https://tanstack.com/query/latest/docs/reference/QueriesObserver

# QueriesObserver

## `QueriesObserver`

The `QueriesObserver` can be used to observe multiple queries.

```tsx
const observer = new QueriesObserver(queryClient, [
  { queryKey: ['post', 1], queryFn: fetchPost },
  { queryKey: ['post', 2], queryFn: fetchPost },
])

const unsubscribe = observer.subscribe((result) => {
  console.log(result)
  unsubscribe()
})
```

**Options**

The options for the `QueriesObserver` are exactly the same as those of [`useQueries`](https://tanstack.com/query/latest/docs/framework/react/reference/useQueries).

