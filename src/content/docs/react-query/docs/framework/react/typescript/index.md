---
title: 'TypeScript'
description: 'React Query는 이제 TypeScript로 작성되어 라이브러리와 프로젝트 모두에서 타입 안정성을 보장합니다!'
---

# TypeScript

React Query는 이제 **TypeScript**로 작성되어 라이브러리와 프로젝트 모두에서 타입 안정성을 보장합니다!

유념해야 할 사항:

- 현재 타입은 **v4.7** 이상의 TypeScript 사용이 필요합니다.
- 이 저장소의 타입 변경은 **하위 호환성이 깨지지 않는** 것으로 간주되며, 일반적으로 **패치** 세부 버전으로 릴리스됩니다(그렇지 않으면 모든 타입 개선이 메이저 버전이 될 것입니다!).
- **react-query 패키지 버전을 특정 패치 릴리스로 고정하고, 릴리스마다 타입이 수정되거나 개선될 수 있다는 기대를 가지고 업그레이드할 것을 적극 권장합니다.**
- 타입과 관련 없는 React Query의 공개 API는 여전히 매우 엄격하게 semver를 따릅니다.

## Type Inference

React Query의 타입은 일반적으로 매우 잘 흐르므로 직접 타입 주석을 제공하지 않아도 됩니다.

[//]: # 'TypeInference1'

```tsx
const { data } = useQuery({
  //    ^? const data: number | undefined
  queryKey: ['test'],
  queryFn: () => Promise.resolve(5),
})
```

[typescript playground](https://www.typescriptlang.org/play?#code/JYWwDg9gTgLgBAbzgVwM4FMCKz1QJ5wC+cAZlBCHAORToCGAxjALQCOO+VAsAFC8MQAdqnhIAJnRh0icALwoM2XHgAUAbSqDkIAEa4qAXQA0cFQEo5APjgAFciGAYAdLVQQANgDd0KgKxmzXgB6ILgw8IA9AH5eIA)

[//]: # 'TypeInference1'
[//]: # 'TypeInference2'

```tsx
const { data } = useQuery({
  //      ^? const data: string | undefined
  queryKey: ['test'],
  queryFn: () => Promise.resolve(5),
  select: (data) => data.toString(),
})
```

[typescript playground](https://www.typescriptlang.org/play?#code/JYWwDg9gTgLgBAbzgVwM4FMCKz1QJ5wC+cAZlBCHAORToCGAxjALQCOO+VAsAFCiSw4dAB7AIqUuUpURY1Nx68YeMOjgBxcsjBwAvIjjAAJgC44AO2QgARriK9eDCOdTwS6GAwAWmiNon6ABQAlGYAClLAGAA8vtoA2gC6AHx6qbLiAHQA5h6BVAD02Vpg8sGZMF7o5oG0qJAuarqpdQ0YmUZ0MHTBDjxOLvBInd1EeigY2Lh4gfFUxX6lVIkANKQe3nGlvTwFBXAHhwB6APxwA65wI3RmW0lwAD4o5kboJMDm6Ea8QA)

[//]: # 'TypeInference2'

`queryFn`의 반환 타입이 명확하게 정의되어 있을 때 가장 잘 작동합니다. 대부분의 데이터 페칭 라이브러리가 기본적으로 `any`를 반환하므로, 타입이 올바르게 지정된 함수로 추출했는지 확인하세요.

[//]: # 'TypeInference3'

```tsx
const fetchGroups = (): Promise<Group[]> =>
  axios.get('/groups').then((response) => response.data)

const { data } = useQuery({ queryKey: ['groups'], queryFn: fetchGroups })
//      ^? const data: Group[] | undefined
```

[typescript playground](https://www.typescriptlang.org/play?#code/JYWwDg9gTgLgBAbzgVwM4FMCKz1QJ5wC+cAZlBCHAORToCGAxjALQCOO+VAsAFCiSw4dAB7AIqUuUpURY1Nx68YeMOjgBxcsjBwAvIjjAAJgC44AO2QgARriK9eDCOdTwS6GAwAWmiNon6ABQAlGYAClLAGAA8vtoA2gC6AHx6qbLiAHQA5h6BVAD02Vpg8sGZMF7o5oG0qJAuarqpdQ0YmUZ0MHTBDjxOLvBInd1EeigY2Lh4gfFUxX6lVIkANKQe3nGlvTwFBXAHhwB6APxwA65wI3RmW0lwAD4o5kboJMDm6Ea8QA)

[//]: # 'TypeInference3'

## Type Narrowing

React Query는 `status` 필드와 파생된 상태 부울 플래그로 판별되는 [판별 가능한 유니온 타입](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes-func.html#discriminated-unions)을 쿼리 결과에 사용합니다. 이를 통해 `success` 상태를 확인하고 `data`가 정의되어 있음을 보장할 수 있습니다.

[//]: # 'TypeNarrowing'

```tsx
const { data, isSuccess } = useQuery({
  queryKey: ['test'],
  queryFn: () => Promise.resolve(5),
})

if (isSuccess) {
  data
  //  ^? const data: number
}
```

[typescript playground](https://www.typescriptlang.org/play?#code/JYWwDg9gTgLgBAbzgVwM4FMCKz1QJ5wC+cAZlBCHAORToCGAxjALQCOO+VAsAFC8MQAdqnhIAJnRh0ANHGCoAysgYN0qVETgBeFBmy48ACgDaVGGphUAurMMBKbQD44ABXIh56AHS1UEADYAbuiGAKx2dry8wCRwhvJKKmqoDgi8cBlwElK8APS5GQB6APy8hLxAA)

[//]: # 'TypeNarrowing'

## Typing the error field

에러 타입은 기본적으로 `Error`이며, 대부분의 사용자가 기대하는 값입니다.

[//]: # 'TypingError'

```tsx
const { error } = useQuery({ queryKey: ['groups'], queryFn: fetchGroups })
//      ^? const error: Error
```

[typescript playground](https://www.typescriptlang.org/play?#code/JYWwDg9gTgLgBAbzgVwM4FMCKz1QJ5wC+cAZlBCHAOQACMAhgHaoMDGA1gPRTr2swBaAI458VALAAoUJFhx6AD2ARUpcpSqLlqCZKkw8YdHADi5ZGDgBeRHGAATAFxxGyEACNcRKVNYRm8CToMKwAFmYQFqo2ABQAlM4ACurAGAA8ERYA2gC6AHzWBVoqAHQA5sExVJxl5mA6cSUwoeiMMTyokMzGVgUdXRgl9vQMcT6SfgG2uORQRNYoGNi4eDFZVLWR9VQ5ADSkwWGZ9WOSnJxwl1cAegD8QA)

[//]: # 'TypingError'

사용자 정의 에러를 throw하거나 `Error`가 아닌 것을 throw하고 싶다면 에러 필드의 타입을 지정할 수 있습니다.

[//]: # 'TypingError2'

```tsx
const { error } = useQuery<Group[], string>(['groups'], fetchGroups)
//      ^? const error: string | null
```

[//]: # 'TypingError2'

그러나 이렇게 하면 `useQuery`의 다른 제네릭에 대한 타입 추론이 더 이상 작동하지 않는 단점이 있습니다. `Error`가 아닌 것을 throw하는 것은 일반적으로 좋은 관행이 아니므로, `AxiosError`와 같은 서브클래스가 있다면 _타입 내로잉_을 사용하여 에러 필드를 보다 구체적으로 만들 수 있습니다.

[//]: # 'TypingError3'

```tsx
import axios from 'axios'

const { error } = useQuery({ queryKey: ['groups'], queryFn: fetchGroups })
//      ^? const error: Error | null

if (axios.isAxiosError(error)) {
  error
  // ^? const error: AxiosError
}
```

[typescript playground](https://www.typescriptlang.org/play?#code/JYWwDg9gTgLgBAbzgVwM4FMCKz1QJ5wC+cAZlBCHAOQACMAhgHaoMDGA1gPRTr2swBaAI458VALAAoUJFhx6AD2ARUpcpSqLlqCZKkw8YdHADi5ZGDgBeRHGAATAFxxGyEACNcRKVNYRm8CToMKwAFmYQFqo2ABQAlM4ACurAGAA8ERYA2gC6AHzWBVoqAHQA5sExVJxl5mA6cSUwoeiMMTyokMzGVgUdXRgl9vQMcT6SfgG2uORQRNYoGNi4eDFIIisA0uh4zllUtZH1VDkANHAb+ABijM5BIeF1qoRjkpyccJ9fAHoA-OPAEhwGLFVAlVIAQSUKgAolBZjEZtA4nFEFJPkioOi4O84H8pIQgA)

[//]: # 'TypingError3'

### Registering a global Error

TanStack Query v5는 `Register` 인터페이스를 수정하여 모든 곳에 글로벌 Error 타입을 설정할 수 있는 방법을 제공합니다. 이렇게 하면 호출 측에서 제네릭을 지정할 필요 없이 여전히 추론이 작동하면서 에러 필드가 지정된 타입으로 유지됩니다. 호출 측에서 명시적으로 타입 내로잉을 수행하도록 강제하고 싶다면 `defaultError`를 `unknown`으로 설정하세요.

[//]: # 'RegisterErrorType'

```tsx
import '@tanstack/react-query'

declare module '@tanstack/react-query' {
  interface Register {
    // Use unknown so call sites must narrow explicitly.
    defaultError: unknown
  }
}

const { error } = useQuery({ queryKey: ['groups'], queryFn: fetchGroups })
//      ^? const error: unknown | null
```

[//]: # 'RegisterErrorType'
[//]: # 'TypingMeta'

## Typing meta

### Registering global Meta

[글로벌 에러 타입 등록](#registering-a-global-error)과 마찬가지로 글로벌 `Meta` 타입도 등록할 수 있습니다. 이렇게 하면 [queries](https://tanstack.com/query/latest/docs/framework/react/reference/useQuery.md)와 [mutations](https://tanstack.com/query/latest/docs/framework/react/reference/useMutation.md)의 선택적 `meta` 필드가 일관되고 타입 안정성을 유지합니다. 등록된 타입은 `meta`가 객체로 남을 수 있도록 `Record<string, unknown>`을 확장해야 합니다.

```ts
import '@tanstack/react-query'

interface MyMeta extends Record<string, unknown> {
  // Your meta type definition.
}

declare module '@tanstack/react-query' {
  interface Register {
    queryMeta: MyMeta
    mutationMeta: MyMeta
  }
}
```

[//]: # 'TypingMeta'
[//]: # 'TypingQueryAndMutationKeys'

## Typing query and mutation keys

### Registering the query and mutation key types

[글로벌 에러 타입 등록](#registering-a-global-error)과 유사하게, 글로벌 `QueryKey` 및 `MutationKey` 타입을 등록할 수도 있습니다. 이를 통해 애플리케이션 계층 구조와 일치하는 키에 더 많은 구조를 제공하고 라이브러리 전체에서 타입을 유지할 수 있습니다. 키가 배열로 남도록 등록된 타입은 `Array` 타입을 확장해야 합니다.

```ts
import '@tanstack/react-query'

type QueryKey = ['dashboard' | 'marketing', ...ReadonlyArray<unknown>]

declare module '@tanstack/react-query' {
  interface Register {
    queryKey: QueryKey
    mutationKey: QueryKey
  }
}
```

[//]: # 'TypingQueryAndMutationKeys'
[//]: # 'TypingQueryOptions'

## Typing Query Options

`useQuery`에 쿼리 옵션을 인라인하면 자동으로 타입 추론이 이뤄집니다. 그러나 `useQuery`와 `prefetchQuery` 등에서 공유하기 위해 쿼리 옵션을 별도 함수로 추출하고 싶을 수 있습니다. 이 경우 타입 추론을 잃게 됩니다. 이를 다시 얻으려면 `queryOptions` 헬퍼를 사용할 수 있습니다.

```ts
import { queryOptions } from '@tanstack/react-query'

function groupOptions() {
  return queryOptions({
    queryKey: ['groups'],
    queryFn: fetchGroups,
    staleTime: 5 * 1000,
  })
}

useQuery(groupOptions())
queryClient.prefetchQuery(groupOptions())
```

또한 `queryOptions`가 반환하는 `queryKey`는 연관된 `queryFn`을 인지하므로, 해당 타입 정보를 활용해 `queryClient.getQueryData`와 같은 함수도 그 타입을 이해하도록 만들 수 있습니다.

```ts
function groupOptions() {
  return queryOptions({
    queryKey: ['groups'],
    queryFn: fetchGroups,
    staleTime: 5 * 1000,
  })
}

const data = queryClient.getQueryData(groupOptions().queryKey)
//     ^? const data: Group[] | undefined
```

`queryOptions` 없이 사용하면 `data`의 타입은 `unknown`이 되며, 제네릭을 전달해야만 타입을 지정할 수 있습니다.

```ts
const data = queryClient.getQueryData<Group[]>(['groups'])
```

`queryOptions`를 통한 타입 추론은 `queryClient.getQueriesData`에서는 작동하지 않습니다. 해당 함수는 다양한 `unknown` 데이터를 포함하는 튜플 배열을 반환하기 때문입니다. 쿼리가 반환할 데이터 타입을 확신한다면 명시적으로 지정하세요.

```ts
const entries = queryClient.getQueriesData<Group[]>(groupOptions().queryKey)
//     ^? const entries: Array<[QueryKey, Group[] | undefined]>
```

## Typing Mutation Options

`queryOptions`와 마찬가지로, `mutationOptions`를 사용해 변이 옵션을 별도 함수로 추출할 수 있습니다.

```ts
function groupMutationOptions() {
  return mutationOptions({
    mutationKey: ['addGroup'],
    mutationFn: addGroup,
  })
}

useMutation({
  ...groupMutationOptions(),
  onSuccess: () => queryClient.invalidateQueries({ queryKey: ['groups'] }),
})
useIsMutating(groupMutationOptions())
queryClient.isMutating(groupMutationOptions())
```

[//]: # 'TypingQueryOptions'

## Typesafe disabling of queries using `skipToken`

TypeScript를 사용하는 경우 `skipToken`을 사용해 쿼리를 비활성화할 수 있습니다. 이는 조건에 따라 쿼리를 비활성화하면서도 타입 안전성을 유지하고 싶을 때 유용합니다. 자세한 내용은 [Disabling Queries](https://tanstack.com/query/latest/docs/framework/react/guides/disabling-queries.md) 가이드를 참고하세요.

[//]: # 'Materials'

## Further Reading

타입 추론과 관련된 팁은 [React Query and TypeScript](https://tkdodo.eu/blog/react-query-and-type-script) 글을 참고하세요. 최고의 타입 안전성을 얻는 방법은 [Type-safe React Query](https://tkdodo.eu/blog/type-safe-react-query)에서 확인할 수 있습니다. [`queryOptions` 헬퍼](https://tkdodo.eu/blog/the-query-options-api)가 타입 추론과 어떻게 작동하는지는 [The Query Options API](https://tkdodo.eu/blog/the-query-options-api)에서 설명합니다.

[//]: # 'Materials'

