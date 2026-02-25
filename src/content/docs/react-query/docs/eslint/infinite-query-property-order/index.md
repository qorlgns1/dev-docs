---
title: '무한 쿼리에서 추론에 민감한 속성의 올바른 순서를 보장하세요'
description: '다음 함수들에서는 전달되는 객체의 속성 순서가 타입 추론 때문에 중요합니다:'
---

# 무한 쿼리에서 추론에 민감한 속성의 올바른 순서를 보장하세요

다음 함수들에서는 전달되는 객체의 속성 순서가 타입 추론 때문에 중요합니다:

- `useInfiniteQuery`
- `useSuspenseInfiniteQuery`
- `infiniteQueryOptions`

올바른 속성 순서는 다음과 같습니다:

- `queryFn`
- `getPreviousPageParam`
- `getNextPageParam`

그 외 모든 속성은 타입 추론에 의존하지 않으므로 순서에 민감하지 않습니다.

## 규칙 상세

이 규칙에서 **잘못된** 코드 예시:

```tsx
/* eslint "@tanstack/query/infinite-query-property-order": "warn" */
import { useInfiniteQuery } from '@tanstack/react-query'

const query = useInfiniteQuery({
  queryKey: ['projects'],
  getNextPageParam: (lastPage) => lastPage.nextId ?? undefined,
  queryFn: async ({ pageParam }) => {
    const response = await fetch(`/api/projects?cursor=${pageParam}`)
    return await response.json()
  },
  initialPageParam: 0,
  getPreviousPageParam: (firstPage) => firstPage.previousId ?? undefined,
  maxPages: 3,
})
```

이 규칙에서 **올바른** 코드 예시:

```tsx
/* eslint "@tanstack/query/infinite-query-property-order": "warn" */
import { useInfiniteQuery } from '@tanstack/react-query'

const query = useInfiniteQuery({
  queryKey: ['projects'],
  queryFn: async ({ pageParam }) => {
    const response = await fetch(`/api/projects?cursor=${pageParam}`)
    return await response.json()
  },
  initialPageParam: 0,
  getPreviousPageParam: (firstPage) => firstPage.previousId ?? undefined,
  getNextPageParam: (lastPage) => lastPage.nextId ?? undefined,
  maxPages: 3,
})
```

## 속성

- [x] ✅ 권장
- [x] 🔧 자동 수정 가능

