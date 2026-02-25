---
title: '쿼리 키를 위한 완전한 의존성'
description: '쿼리 키는 쿼리 함수의 의존성 배열처럼 봐야 합니다.  내부에서 사용하는 모든 변수는 쿼리 키에 추가되어야 합니다.'
---

Source URL: https://tanstack.com/query/latest/docs/eslint/exhaustive-deps

# 쿼리 키를 위한 완전한 의존성

쿼리 키는 쿼리 함수의 의존성 배열처럼 봐야 합니다. `queryFn` 내부에서 사용하는 모든 변수는 쿼리 키에 추가되어야 합니다.  
이렇게 하면 쿼리가 각각 독립적으로 캐시되고, 변수가 변경될 때 쿼리가 자동으로 다시 가져와지도록 보장할 수 있습니다.

## 규칙 상세

이 규칙에서 **잘못된** 코드 예시:

```tsx
/* eslint "@tanstack/query/exhaustive-deps": "error" */

useQuery({
  queryKey: ['todo'],
  queryFn: () => api.getTodo(todoId),
})

const todoQueries = {
  detail: (id) => ({ queryKey: ['todo'], queryFn: () => api.getTodo(id) }),
}
```

이 규칙에서 **올바른** 코드 예시:

```tsx
useQuery({
  queryKey: ['todo', todoId],
  queryFn: () => api.getTodo(todoId),
})

const todoQueries = {
  detail: (id) => ({ queryKey: ['todo', id], queryFn: () => api.getTodo(id) }),
}
```

## 사용하지 않아도 되는 경우

쿼리 키 규칙을 신경 쓰지 않는다면, 이 규칙은 필요하지 않습니다.

## 속성

- [x] ✅ 권장됨
- [x] 🔧 자동 수정 가능

