---
title: '쿼리 결과에서 객체 rest 구조 분해를 금지'
description: '쿼리 결과에 객체 rest 구조 분해를 사용하면 쿼리 결과의 모든 필드를 자동으로 구독하게 되어, 불필요한 리렌더링이 발생할 수 있습니다.'
---

Source URL: https://tanstack.com/query/latest/docs/eslint/no-rest-destructuring

# 쿼리 결과에서 객체 rest 구조 분해를 금지

쿼리 결과에 객체 rest 구조 분해를 사용하면 쿼리 결과의 모든 필드를 자동으로 구독하게 되어, 불필요한 리렌더링이 발생할 수 있습니다.
이 규칙은 실제로 필요한 필드만 구독하도록 보장합니다.

## 규칙 세부 사항

이 규칙에서 **잘못된** 코드의 예:

```tsx
/* eslint "@tanstack/query/no-rest-destructuring": "warn" */

const useTodos = () => {
  const { data: todos, ...rest } = useQuery({
    queryKey: ['todos'],
    queryFn: () => api.getTodos(),
  })
  return { todos, ...rest }
}
```

이 규칙에서 **올바른** 코드의 예:

```tsx
const todosQuery = useQuery({
  queryKey: ['todos'],
  queryFn: () => api.getTodos(),
})

// normal object destructuring is fine
const { data: todos } = todosQuery
```

## 사용하지 않아도 되는 경우

`notifyOnChangeProps` 옵션을 수동으로 설정하는 경우, 이 규칙을 비활성화할 수 있습니다.
tracked query를 사용하지 않으므로, 어떤 props가 리렌더링을 트리거해야 하는지 직접 지정해야 합니다.

## 속성

- [x] ✅ 권장
- [ ] 🔧 자동 수정 가능

