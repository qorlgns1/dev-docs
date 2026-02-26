---
title: '쿼리 훅의 결과를 React 훅 의존성 배열에 직접 넣지 않기'
description: '다음 쿼리 훅에서 반환되는 객체는 참조 안정성(referential stability)이 없습니다:'
---

Source URL: https://tanstack.com/query/latest/docs/eslint/no-unstable-deps

# 쿼리 훅의 결과를 React 훅 의존성 배열에 직접 넣지 않기

다음 쿼리 훅에서 반환되는 객체는 참조 안정성(referential stability)이 **없습니다**:

- `useQuery`
- `useSuspenseQuery`
- `useQueries`
- `useSuspenseQueries`
- `useInfiniteQuery`
- `useSuspenseInfiniteQuery`
- `useMutation`

해당 훅들이 반환한 객체를 React 훅(예: `useEffect`, `useMemo`, `useCallback`)의 의존성 배열에 직접 넣으면 **안 됩니다**.  
대신 쿼리 훅의 반환값을 구조 분해한 뒤, 구조 분해한 값을 React 훅의 의존성 배열에 전달하세요.

## 규칙 상세

이 규칙에서 **잘못된** 코드 예시:

```tsx
/* eslint "@tanstack/query/no-unstable-deps": "warn" */
import { useCallback } from 'React'
import { useMutation } from '@tanstack/react-query'

function Component() {
  const mutation = useMutation({ mutationFn: (value: string) => value })
  const callback = useCallback(() => {
    mutation.mutate('hello')
  }, [mutation])
  return null
}
```

이 규칙에서 **올바른** 코드 예시:

```tsx
/* eslint "@tanstack/query/no-unstable-deps": "warn" */
import { useCallback } from 'React'
import { useMutation } from '@tanstack/react-query'

function Component() {
  const { mutate } = useMutation({ mutationFn: (value: string) => value })
  const callback = useCallback(() => {
    mutate('hello')
  }, [mutate])
  return null
}
```

## 속성

- [x] ✅ 권장
- [ ] 🔧 자동 수정 가능

