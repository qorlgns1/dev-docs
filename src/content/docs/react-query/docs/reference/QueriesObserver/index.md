---
title: 'QueriesObserver'
description: '요청이 단순 번역이라 add-doc 스킬(번거로운 크롤·배포 포함)을 적용하지 않고 직접 처리했어요.'
---

요청이 단순 번역이라 add-doc 스킬(번거로운 크롤·배포 포함)을 적용하지 않고 직접 처리했어요.

# QueriesObserver

## `QueriesObserver`

`QueriesObserver`는 여러 개의 쿼리를 관찰할 때 사용할 수 있습니다.

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

`QueriesObserver`의 옵션은 [`useQueries`](https://tanstack.com/query/latest/docs/framework/react/reference/useQueries)와 완전히 동일합니다.

다른 섹션 번역 필요하면 알려 주세요.

