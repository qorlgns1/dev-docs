---
title: 'useMutation()에서 타입 추론에 민감한 속성의 올바른 순서 보장'
description: '다음 함수들에서는 전달된 객체의 속성 순서가 타입 추론 때문에 중요합니다:'
---

Source URL: https://tanstack.com/query/latest/docs/eslint/mutation-property-order

# useMutation()에서 타입 추론에 민감한 속성의 올바른 순서 보장

다음 함수들에서는 전달된 객체의 속성 순서가 타입 추론 때문에 중요합니다:

- `useMutation()`

올바른 속성 순서는 다음과 같습니다:

- `onMutate`
- `onError`
- `onSettled`

다른 모든 속성은 타입 추론에 의존하지 않으므로 순서에 민감하지 않습니다.

## 규칙 상세

이 규칙에서 **잘못된** 코드 예시:

```tsx
/* eslint "@tanstack/query/mutation-property-order": "warn" */
import { useMutation } from '@tanstack/react-query'

const mutation = useMutation({
  mutationFn: () => Promise.resolve('success'),
  onSettled: () => {
    results.push('onSettled-promise')
    return Promise.resolve('also-ignored') // Promise<string> (should be ignored)
  },
  onMutate: async () => {
    results.push('onMutate-async')
    await sleep(1)
    return { backup: 'async-data' }
  },
  onError: async () => {
    results.push('onError-async-start')
    await sleep(1)
    results.push('onError-async-end')
  },
})
```

이 규칙에서 **올바른** 코드 예시:

```tsx
/* eslint "@tanstack/query/mutation-property-order": "warn" */
import { useMutation } from '@tanstack/react-query'

const mutation = useMutation({
  mutationFn: () => Promise.resolve('success'),
  onMutate: async () => {
    results.push('onMutate-async')
    await sleep(1)
    return { backup: 'async-data' }
  },
  onError: async () => {
    results.push('onError-async-start')
    await sleep(1)
    results.push('onError-async-end')
  },
  onSettled: () => {
    results.push('onSettled-promise')
    return Promise.resolve('also-ignored') // Promise<string> (should be ignored)
  },
})
```

## 속성

- [x] ✅ 권장됨
- [x] 🔧 자동 수정 가능

