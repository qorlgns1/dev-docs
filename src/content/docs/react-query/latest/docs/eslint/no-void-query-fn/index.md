---
title: 'query 함수에서 void 반환 금지'
description: 'query 함수는 TanStack Query에 의해 캐시될 값을 반환해야 합니다. 값을 반환하지 않는 함수( 함수)는 예기치 않은 동작을 유발할 수 있으며, 구현상의 실수를 나타낼 수 있습니다.'
---

Source URL: https://tanstack.com/query/latest/docs/eslint/no-void-query-fn

# query 함수에서 void 반환 금지

query 함수는 TanStack Query에 의해 캐시될 값을 반환해야 합니다. 값을 반환하지 않는 함수(`void` 함수)는 예기치 않은 동작을 유발할 수 있으며, 구현상의 실수를 나타낼 수 있습니다.

## 규칙 세부 정보

이 규칙에서 **잘못된** 코드 예시:

```tsx
/* eslint "@tanstack/query/no-void-query-fn": "error" */

useQuery({
  queryKey: ['todos'],
  queryFn: async () => {
    await api.todos.fetch() // Function doesn't return the fetched data
  },
})
```

이 규칙에서 **올바른** 코드 예시:

```tsx
/* eslint "@tanstack/query/no-void-query-fn": "error" */
useQuery({
  queryKey: ['todos'],
  queryFn: async () => {
    const todos = await api.todos.fetch()
    return todos
  },
})
```

## 속성

- [x] ✅ 권장됨
- [ ] 🔧 수정 가능

