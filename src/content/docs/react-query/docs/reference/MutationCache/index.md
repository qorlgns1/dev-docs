---
title: 'MutationCache'
description: "import { MutationCache } from '@tanstack/react-query'"
---

# MutationCache

`MutationCache`는 뮤테이션을 저장하는 공간입니다.

**일반적으로 `QueryClient`를 사용하므로 MutationCache와 직접 상호 작용할 일은 거의 없습니다.**

```tsx
import { MutationCache } from '@tanstack/react-query'

const mutationCache = new MutationCache({
  onError: (error) => {
    console.log(error)
  },
  onSuccess: (data) => {
    console.log(data)
  },
})
```

사용 가능한 메서드는 다음과 같습니다.

- [`getAll`](#mutationcachegetall)
- [`subscribe`](#mutationcachesubscribe)
- [`clear`](#mutationcacheclear)

**옵션**

- `onError?: (error: unknown, variables: unknown, onMutateResult: unknown, mutation: Mutation, mutationFnContext: MutationFunctionContext) => Promise<unknown> | unknown`
  - 선택 사항
  - 어떤 뮤테이션에서 오류가 발생하면 호출됩니다.
  - Promise를 반환하면 완료될 때까지 대기합니다.
- `onSuccess?: (data: unknown, variables: unknown, onMutateResult: unknown, mutation: Mutation, mutationFnContext: MutationFunctionContext) => Promise<unknown> | unknown`
  - 선택 사항
  - 어떤 뮤테이션이 성공하면 호출됩니다.
  - Promise를 반환하면 완료될 때까지 대기합니다.
- `onSettled?: (data: unknown | undefined, error: unknown | null, variables: unknown, onMutateResult: unknown, mutation: Mutation, mutationFnContext: MutationFunctionContext) => Promise<unknown> | unknown`
  - 선택 사항
  - 어떤 뮤테이션이 완료(성공 또는 실패)되면 호출됩니다.
  - Promise를 반환하면 완료될 때까지 대기합니다.
- `onMutate?: (variables: unknown, mutation: Mutation, mutationFnContext: MutationFunctionContext) => Promise<unknown> | unknown`
  - 선택 사항
  - 어떤 뮤테이션이 실행되기 전에 호출됩니다.
  - Promise를 반환하면 완료될 때까지 대기합니다.

## Global callbacks

MutationCache의 `onError`, `onSuccess`, `onSettled`, `onMutate` 콜백은 이러한 이벤트를 전역 수준에서 처리할 때 사용할 수 있습니다. 이는 QueryClient에 제공되는 `defaultOptions`와 다음과 같은 차이가 있습니다.

- `defaultOptions`는 각 Mutation이 덮어쓸 수 있지만, 전역 콜백은 **항상** 호출됩니다.
- `onMutate`에서는 결과 값을 반환할 수 없습니다.

## `mutationCache.getAll`

`getAll`은 캐시에 포함된 모든 뮤테이션을 반환합니다.

> 참고: 대부분의 애플리케이션에서는 필요하지 않지만, 드물게 뮤테이션에 대한 추가 정보가 필요할 때 유용할 수 있습니다.

```tsx
const mutations = mutationCache.getAll()
```

**반환 값**

- `Mutation[]`
  - 캐시에서 가져온 Mutation 인스턴스

## `mutationCache.subscribe`

`subscribe` 메서드를 사용하면 뮤테이션 캐시 전체를 구독하여, 뮤테이션 상태 변경이나 업데이트·추가·삭제처럼 캐시에 발생하는 안전하고 알려진 업데이트를 통지받을 수 있습니다.

```tsx
const callback = (event) => {
  console.log(event.type, event.mutation)
}

const unsubscribe = mutationCache.subscribe(callback)
```

**옵션**

- `callback: (mutation?: MutationCacheNotifyEvent) => void`
  - 캐시가 업데이트될 때마다 뮤테이션 캐시와 함께 호출됩니다.

**반환 값**

- `unsubscribe: Function => void`
  - 이 함수를 호출하면 콜백이 뮤테이션 캐시에서 구독 해제됩니다.

## `mutationCache.clear`

`clear` 메서드는 캐시를 완전히 비우고 새롭게 시작할 때 사용할 수 있습니다.

```tsx
mutationCache.clear()
```

