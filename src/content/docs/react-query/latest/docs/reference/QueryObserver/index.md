---
title: 'QueryObserver'
description: '는 쿼리를 관찰하고 전환하는 데 사용할 수 있습니다.'
---

Source URL: https://tanstack.com/query/latest/docs/reference/QueryObserver

# QueryObserver

`QueryObserver`는 쿼리를 관찰하고 전환하는 데 사용할 수 있습니다.

```tsx
const observer = new QueryObserver(queryClient, { queryKey: ['posts'] })

const unsubscribe = observer.subscribe((result) => {
  console.log(result)
  unsubscribe()
})
```

**옵션**

`QueryObserver`의 옵션은 [`useQuery`](https://tanstack.com/query/latest/docs/framework/react/reference/useQuery)와 완전히 동일합니다.

